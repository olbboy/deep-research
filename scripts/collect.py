#!/usr/bin/env python3
"""Deep-research collectors: Serper (Google SERP), Brave Search, Jina (search + reader), SearXNG (local metasearch).

Every sub-command prints ONE normalized JSON document to stdout so the research
loop can treat all providers the same way:

    {"provider": ..., "kind": ..., "query": ..., "fetched_at": ..., "results": [...]}

Each result carries `origin` (registrable domain of the result URL) because the
Independence round groups evidence by origin, never by the search engine that
surfaced it. Search engines are index/transport only; they are NOT sources.

API keys are read from the environment first, then from `.env` files in
priority order: skill-local `.env` -> ~/.claude/skills/.env -> ~/.claude/.env.
Keys are never printed.
"""

from __future__ import annotations

import argparse
import json
import os
import ssl
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timedelta, timezone
from pathlib import Path

SKILL_ROOT = Path(__file__).resolve().parent.parent
SAIGON_TZ = timezone(timedelta(hours=7))
DEFAULT_TIMEOUT_S = 30

# Two-label suffixes such as `com.vn`, `co.uk`, `gov.vn` need three labels to
# identify the registrable domain. Kept intentionally small (KISS).
SECOND_LEVEL_SUFFIXES = {"com", "co", "net", "org", "gov", "edu", "ac", "or"}


# --------------------------------------------------------------------------- env


def load_env() -> None:
    """Populate os.environ from .env files without overriding existing values."""
    candidates = [
        SKILL_ROOT / ".env",
        Path.home() / ".claude" / "skills" / ".env",
        Path.home() / ".claude" / ".env",
    ]
    for path in candidates:
        if not path.exists():
            continue
        for line in path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, _, value = line.partition("=")
            os.environ.setdefault(key.strip(), value.strip().strip('"').strip("'"))


def require_key(name: str) -> str:
    load_env()
    value = os.environ.get(name, "").strip()
    if not value:
        fail(f"{name} not set. Add it to ~/.claude/.env (see .env.example).", code=2)
    return value


# -------------------------------------------------------------------------- http


def ssl_context() -> ssl.SSLContext:
    """python.org builds on macOS ship without root CAs; prefer certifi when present."""
    try:
        import certifi  # bundled with `requests` in the skills venv

        return ssl.create_default_context(cafile=certifi.where())
    except ImportError:
        return ssl.create_default_context()


def http_json(url: str, *, headers: dict, body: dict | None = None, timeout: int) -> dict:
    """POST when `body` is given, otherwise GET. Returns parsed JSON or exits."""
    data = json.dumps(body).encode("utf-8") if body is not None else None
    req = urllib.request.Request(url, data=data, headers=headers, method="POST" if data else "GET")
    host = urllib.parse.urlsplit(url).netloc
    for attempt in range(2):  # one retry, only for 429 (Brave free tier = 1 request/second)
        try:
            with urllib.request.urlopen(req, timeout=timeout, context=ssl_context()) as resp:
                raw = resp.read()
            break
        except urllib.error.HTTPError as exc:
            if exc.code == 429 and attempt == 0:
                time.sleep(1.5)
                continue
            detail = exc.read().decode("utf-8", "replace")[:300]
            fail(f"HTTP {exc.code} from {host}: {detail}", code=3)
        except urllib.error.URLError as exc:
            fail(f"network error for {host}: {exc.reason}", code=3)
    try:
        return json.loads(raw.decode("utf-8"))
    except json.JSONDecodeError:
        fail("provider returned non-JSON body", code=3)


def fail(message: str, *, code: int) -> None:
    print(json.dumps({"error": message}), file=sys.stderr)
    sys.exit(code)


# ------------------------------------------------------------------- normalize


def origin_of(url: str) -> str:
    """Registrable domain, e.g. https://www.vnexpress.net/a -> vnexpress.net."""
    host = urllib.parse.urlsplit(url).hostname or ""
    host = host.lower().removeprefix("www.")
    labels = host.split(".")
    if len(labels) >= 3 and labels[-2] in SECOND_LEVEL_SUFFIXES:
        return ".".join(labels[-3:])
    return ".".join(labels[-2:]) if len(labels) >= 2 else host


def result(rank: int, title: str, url: str, snippet: str, date: str | None, **extra) -> dict:
    return {
        "rank": rank,
        "title": title or "",
        "url": url or "",
        "snippet": snippet or "",
        "date": date,
        "origin": origin_of(url or ""),
        "source_type": "non-AI",  # search index / page fetch, not an LLM answer
        **extra,
    }


def envelope(provider: str, kind: str, query: str, results: list, raw: dict | None, **meta) -> dict:
    doc = {
        "provider": provider,
        "kind": kind,
        "query": query,
        "fetched_at": datetime.now(SAIGON_TZ).isoformat(timespec="seconds"),
        "count": len(results),
        "results": results,
        **meta,
    }
    if raw is not None:
        doc["raw"] = raw
    return doc


# ------------------------------------------------------------------ providers


def run_serper(args: argparse.Namespace) -> dict:
    key = require_key("SERPER_API_KEY")
    body = {"q": args.query, "num": args.num, "page": args.page, "gl": args.gl, "hl": args.hl}
    if args.tbs:
        body["tbs"] = args.tbs  # e.g. qdr:y = past year
    data = http_json(
        f"https://google.serper.dev/{args.type}",
        headers={"X-API-KEY": key, "Content-Type": "application/json"},
        body=body,
        timeout=args.timeout,
    )
    items = data.get("organic") or data.get("news") or []
    results = [
        result(i, it.get("title"), it.get("link"), it.get("snippet"), it.get("date"), source=it.get("source"))
        for i, it in enumerate(items, 1)
    ]
    meta = {"gl": args.gl, "hl": args.hl, "type": args.type}
    if data.get("knowledgeGraph"):
        meta["knowledge_graph"] = data["knowledgeGraph"]
    if data.get("relatedSearches"):
        meta["related_searches"] = [r.get("query") for r in data["relatedSearches"]]
    return envelope("serper", args.type, args.query, results, data if args.raw else None, **meta)


def run_brave(args: argparse.Namespace) -> dict:
    key = require_key("BRAVE_API_KEY")
    params = {"q": args.query, "count": args.count, "country": args.country, "search_lang": args.search_lang}
    if args.freshness:
        params["freshness"] = args.freshness  # pd | pw | pm | py
    endpoint = "web" if args.type == "web" else "news"
    data = http_json(
        f"https://api.search.brave.com/res/v1/{endpoint}/search?" + urllib.parse.urlencode(params),
        headers={"Accept": "application/json", "X-Subscription-Token": key},
        timeout=args.timeout,
    )
    items = data.get("web", {}).get("results", []) if endpoint == "web" else data.get("results", [])
    results = [
        result(i, it.get("title"), it.get("url"), it.get("description"), it.get("page_age") or it.get("age"))
        for i, it in enumerate(items, 1)
    ]
    meta = {"country": args.country, "search_lang": args.search_lang, "type": args.type}
    return envelope("brave", args.type, args.query, results, data if args.raw else None, **meta)


def run_jina_search(args: argparse.Namespace) -> dict:
    key = require_key("JINA_API_KEY")
    headers = {"Authorization": f"Bearer {key}", "Accept": "application/json"}
    if args.site:
        headers["X-Site"] = args.site
    if args.no_content:
        headers["X-Respond-With"] = "no-content"
    data = http_json(
        "https://s.jina.ai/?" + urllib.parse.urlencode({"q": args.query}),
        headers=headers,
        timeout=args.timeout,
    )
    results = []
    for i, it in enumerate(data.get("data") or [], 1):
        content = (it.get("content") or "")[: args.max_chars] if not args.no_content else ""
        results.append(result(i, it.get("title"), it.get("url"), it.get("description"), None, content=content))
    return envelope("jina", "search", args.query, results, data if args.raw else None, site=args.site)


def run_jina_read(args: argparse.Namespace) -> dict:
    key = require_key("JINA_API_KEY")
    headers = {"Authorization": f"Bearer {key}", "Accept": "application/json"}
    if args.with_links:
        headers["X-With-Links-Summary"] = "true"
    data = http_json(f"https://r.jina.ai/{args.url}", headers=headers, timeout=args.timeout)
    page = data.get("data") or {}
    content = page.get("content") or ""
    doc = envelope(
        "jina", "read", args.url, [], data if args.raw else None,
        title=page.get("title"),
        url=page.get("url") or args.url,
        origin=origin_of(page.get("url") or args.url),
        source_type="non-AI",
        content=content[: args.max_chars],
        truncated=len(content) > args.max_chars,
        links=page.get("links"),
    )
    doc.pop("results")
    doc.pop("count")
    return doc


def run_searxng(args: argparse.Namespace) -> dict:
    """Local SearXNG metasearch; bootstraps the instance on first use (no API key)."""
    import searxng_runtime as sx  # sibling module, imported lazily to keep other providers light

    if args.stop:
        return {"provider": "searxng", "kind": "stop", "stopped": sx.stop()}
    if args.status:
        return {"provider": "searxng", "kind": "status", **sx.status()}
    if not args.query:
        fail("searxng needs a query (or --status / --stop)", code=2)
    try:
        mode = sx.ensure_running()
    except (RuntimeError, OSError) as exc:
        fail(f"searxng bootstrap failed: {exc}", code=3)
    params = {"q": args.query, "format": "json", "pageno": args.pageno, "safesearch": args.safesearch}
    if args.categories:
        params["categories"] = args.categories
    if args.engines:
        params["engines"] = args.engines
    if args.language:
        params["language"] = args.language
    if args.time_range:
        params["time_range"] = args.time_range
    data = http_json(f"{sx.BASE_URL}/search?" + urllib.parse.urlencode(params), headers={"Accept": "application/json"}, timeout=args.timeout)
    results = [
        result(i, it.get("title"), it.get("url"), it.get("content"), it.get("publishedDate"),
               engines=it.get("engines") or [it.get("engine")], score=it.get("score"))
        for i, it in enumerate(data.get("results") or [], 1)
    ]
    meta = {
        "runtime": mode,
        "language": args.language,
        "categories": args.categories,
        "answers": data.get("answers") or [],
        "suggestions": data.get("suggestions") or [],
        "unresponsive_engines": data.get("unresponsive_engines") or [],
    }
    return envelope("searxng", "search", args.query, results, data if args.raw else None, **meta)


# ------------------------------------------------------------------------ cli


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="collect.py", description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="provider", required=True)

    def common(sp: argparse.ArgumentParser) -> None:
        sp.add_argument("--raw", action="store_true", help="include the provider's raw response under `raw`")
        sp.add_argument("--out", type=Path, help="also write the JSON document to this file")
        sp.add_argument("--timeout", type=int, default=DEFAULT_TIMEOUT_S)

    s = sub.add_parser("serper", help="Google SERP via serper.dev (search | news | scholar)")
    s.add_argument("query")
    s.add_argument("--type", choices=["search", "news", "scholar"], default="search")
    s.add_argument("--num", type=int, default=10)
    s.add_argument("--page", type=int, default=1)
    s.add_argument("--gl", default="us", help="country code, e.g. vn")
    s.add_argument("--hl", default="en", help="UI language, e.g. vi")
    s.add_argument("--tbs", help="time filter: qdr:d | qdr:w | qdr:m | qdr:y")
    common(s)
    s.set_defaults(func=run_serper)

    b = sub.add_parser("brave", help="Brave Search API (independent index; web | news)")
    b.add_argument("query")
    b.add_argument("--type", choices=["web", "news"], default="web")
    b.add_argument("--count", type=int, default=10)
    b.add_argument("--country", default="ALL", help="Brave enum (US, GB, JP, ...); VN is NOT supported, keep ALL + --search-lang vi")
    b.add_argument("--search-lang", default="en", help="e.g. vi")
    b.add_argument("--freshness", choices=["pd", "pw", "pm", "py"], help="past day/week/month/year")
    common(b)
    b.set_defaults(func=run_brave)

    js = sub.add_parser("jina-search", help="Jina s.jina.ai: search that returns page content")
    js.add_argument("query")
    js.add_argument("--site", help="restrict to a domain, e.g. vnexpress.net")
    js.add_argument("--no-content", action="store_true", help="titles/urls only (cheaper)")
    js.add_argument("--max-chars", type=int, default=4000, help="truncate each page's content")
    common(js)
    js.set_defaults(func=run_jina_search)

    jr = sub.add_parser("jina-read", help="Jina r.jina.ai: fetch one URL as clean markdown")
    jr.add_argument("url")
    jr.add_argument("--with-links", action="store_true", help="append a links summary")
    jr.add_argument("--max-chars", type=int, default=20000)
    common(jr)
    jr.set_defaults(func=run_jina_read)
    sx = sub.add_parser("searxng", help="local SearXNG metasearch (auto-installs on first use; no API key)")
    sx.add_argument("query", nargs="?")
    sx.add_argument("--categories", help="general | news | science | it | ... (comma-separated)")
    sx.add_argument("--engines", help="comma-separated engine names, e.g. google,bing,duckduckgo")
    sx.add_argument("--language", help="e.g. vi, en, vi-VN")
    sx.add_argument("--time-range", choices=["day", "month", "year"])
    sx.add_argument("--pageno", type=int, default=1)
    sx.add_argument("--safesearch", type=int, choices=[0, 1, 2], default=0)
    sx.set_defaults(timeout=60)
    sx.add_argument("--status", action="store_true", help="report runtime state and exit")
    sx.add_argument("--stop", action="store_true", help="stop the local instance this skill started")
    common(sx)
    sx.set_defaults(func=run_searxng)
    return p


def main(argv: list[str] | None = None) -> None:
    args = build_parser().parse_args(argv)
    doc = args.func(args)
    text = json.dumps(doc, ensure_ascii=False, indent=2)
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(text, encoding="utf-8")
    print(text)


if __name__ == "__main__":
    main()
