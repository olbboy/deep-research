#!/usr/bin/env python3
"""Local SearXNG runtime: install on first use, start, health-check, stop.

SearXNG (https://github.com/searxng/searxng) is a self-hosted metasearch engine.
It has no hosted API, so the collector needs a local instance. This module makes
`collect.py searxng` self-sufficient:

    ensure_running()  -> healthy instance at BASE_URL, bootstrapping if needed
    stop()            -> stop what we started (never touches other processes)
    status()          -> dict describing mode / health / paths

Two runtimes, chosen automatically (override with SEARXNG_RUNTIME=docker|source):

    docker  - official image, container `deep-research-searxng`, host port 8888
    source  - git clone + venv (Python >= 3.11) when Docker is not available

Everything lives under ~/.local/share/deep-research/searxng so the skill repo
stays clean. Port and container name are fixed so re-runs reuse, never duplicate.
"""

from __future__ import annotations

import os
import secrets
import shutil
import signal
import subprocess
import sys
import time
import urllib.error
import urllib.request
from pathlib import Path

PORT = 8888
BASE_URL = f"http://127.0.0.1:{PORT}"
CONTAINER = "deep-research-searxng"
IMAGE = "docker.io/searxng/searxng:latest"
REPO = "https://github.com/searxng/searxng"

HOME_DIR = Path(os.environ.get("DEEP_RESEARCH_HOME", Path.home() / ".local" / "share" / "deep-research"))
ROOT = HOME_DIR / "searxng"
CONFIG_DIR = ROOT / "config"          # mounted to /etc/searxng in docker mode
DATA_DIR = ROOT / "data"              # mounted to /var/cache/searxng in docker mode
SRC_DIR = ROOT / "src"                # source mode: git checkout
VENV_DIR = ROOT / "venv"              # source mode: virtualenv
PID_FILE = ROOT / "searxng.pid"
LOG_FILE = ROOT / "searxng.log"
SETTINGS = CONFIG_DIR / "settings.yml"

HEALTH_TIMEOUT_S = 240  # first docker pull can take a while


# ------------------------------------------------------------------ health


def is_healthy(timeout: float = 3.0) -> bool:
    try:
        with urllib.request.urlopen(f"{BASE_URL}/healthz", timeout=timeout) as resp:
            return resp.status == 200
    except (urllib.error.URLError, OSError):
        return False


def wait_healthy(seconds: int) -> None:
    deadline = time.monotonic() + seconds
    while time.monotonic() < deadline:
        if is_healthy():
            return
        time.sleep(2)
    raise RuntimeError(f"SearXNG did not become healthy within {seconds}s; see {LOG_FILE} or `docker logs {CONTAINER}`")


# ---------------------------------------------------------------- settings


def write_settings() -> None:
    """Minimal settings.yml: JSON API on, limiter off (it needs Valkey).

    Bind/port are left at SearXNG defaults: source mode already listens on
    127.0.0.1:8888, and the docker image binds via its own entrypoint (0.0.0.0:8080),
    so one file serves both runtimes.
    """
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    if SETTINGS.exists():
        return
    SETTINGS.write_text(
        "use_default_settings: true\n"
        "general:\n  instance_name: deep-research\n  debug: false\n"
        f"server:\n  limiter: false\n  image_proxy: false\n  secret_key: \"{secrets.token_hex(32)}\"\n"
        "search:\n  formats:\n    - html\n    - json\n  safe_search: 0\n  autocomplete: \"\"\n",
        encoding="utf-8",
    )


# ------------------------------------------------------------------ docker


def docker_available() -> bool:
    if not shutil.which("docker"):
        return False
    return subprocess.run(["docker", "info"], capture_output=True).returncode == 0


def docker_container_state() -> str | None:
    """'running' | 'exited' | ... | None when the container does not exist."""
    out = subprocess.run(
        ["docker", "ps", "-a", "--filter", f"name=^{CONTAINER}$", "--format", "{{.State}}"],
        capture_output=True, text=True,
    ).stdout.strip()
    return out or None


def start_docker() -> None:
    write_settings()
    DATA_DIR.mkdir(parents=True, exist_ok=True)
    state = docker_container_state()
    if state == "running":
        return
    if state:  # exists but stopped: reuse, do not create a duplicate
        subprocess.run(["docker", "start", CONTAINER], check=True, capture_output=True)
        return
    subprocess.run(
        ["docker", "run", "-d", "--name", CONTAINER,
         "-p", f"127.0.0.1:{PORT}:8080",
         "-v", f"{CONFIG_DIR}:/etc/searxng", "-v", f"{DATA_DIR}:/var/cache/searxng",
         IMAGE],
        check=True, capture_output=True,
    )


# ------------------------------------------------------------------ source


def find_python() -> str | None:
    for name in ("python3.13", "python3.12", "python3.11"):
        if shutil.which(name):
            return name
    return None


def install_source(python: str) -> None:
    """One-time: shallow clone + venv + editable install (mirrors the official manual install)."""
    ROOT.mkdir(parents=True, exist_ok=True)
    if not (SRC_DIR / "searx").exists():
        subprocess.run(["git", "clone", "--depth", "1", REPO, str(SRC_DIR)], check=True)
    venv_python = VENV_DIR / "bin" / "python"
    if not venv_python.exists():
        subprocess.run([python, "-m", "venv", str(VENV_DIR)], check=True)
    pip = [str(venv_python), "-m", "pip", "install", "-q", "-U"]
    subprocess.run(pip + ["pip", "setuptools", "wheel"], check=True)
    subprocess.run(pip + ["pyyaml", "msgspec", "typing-extensions", "pybind11"], check=True)
    subprocess.run(pip + ["--use-pep517", "--no-build-isolation", "-e", str(SRC_DIR)], check=True)


def source_pid() -> int | None:
    try:
        pid = int(PID_FILE.read_text().strip())
        os.kill(pid, 0)  # signal 0 = existence check only
        return pid
    except (FileNotFoundError, ValueError, ProcessLookupError, PermissionError):
        return None


def start_source() -> None:
    python = find_python()
    if not python:
        raise RuntimeError("SearXNG source mode needs Python >= 3.11 (python3.11/3.12/3.13 on PATH) or Docker")
    write_settings()
    if not (VENV_DIR / "bin" / "python").exists() or not (SRC_DIR / "searx").exists():
        install_source(python)
    if source_pid():
        return
    env = {**os.environ, "SEARXNG_SETTINGS_PATH": str(SETTINGS)}
    with LOG_FILE.open("ab") as log:
        proc = subprocess.Popen(
            [str(VENV_DIR / "bin" / "python"), "-m", "searx.webapp"],
            cwd=SRC_DIR, env=env, stdout=log, stderr=subprocess.STDOUT,
            start_new_session=True,  # survive the collector process exiting
        )
    PID_FILE.write_text(str(proc.pid))


# -------------------------------------------------------------------- api


def choose_mode() -> str:
    forced = os.environ.get("SEARXNG_RUNTIME", "auto").lower()
    if forced in ("docker", "source"):
        return forced
    return "docker" if docker_available() else "source"


def ensure_running() -> str:
    """Return the mode that serves BASE_URL, bootstrapping on first use."""
    if is_healthy():
        return "docker" if docker_container_state() == "running" else "source" if source_pid() else "external"
    mode = choose_mode()
    print(f'{{"info": "starting SearXNG ({mode}) on {BASE_URL}; first run installs it"}}', file=sys.stderr)
    if mode == "docker":
        if not docker_available():
            raise RuntimeError("SEARXNG_RUNTIME=docker but Docker is not available")
        start_docker()
    else:
        start_source()
    wait_healthy(HEALTH_TIMEOUT_S)
    return mode


def stop() -> str:
    """Stop only the instance this module started. Returns what was stopped."""
    stopped = []
    if shutil.which("docker") and docker_container_state() == "running":
        subprocess.run(["docker", "stop", CONTAINER], check=True, capture_output=True)
        stopped.append("docker")
    pid = source_pid()
    if pid:
        os.killpg(os.getpgid(pid), signal.SIGTERM)
        PID_FILE.unlink(missing_ok=True)
        stopped.append("source")
    return ",".join(stopped) or "nothing"


def status() -> dict:
    return {
        "healthy": is_healthy(),
        "base_url": BASE_URL,
        "docker_container": docker_container_state() if shutil.which("docker") else None,
        "source_pid": source_pid(),
        "root": str(ROOT),
        "settings": str(SETTINGS) if SETTINGS.exists() else None,
    }
