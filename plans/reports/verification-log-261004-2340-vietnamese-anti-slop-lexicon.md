# Verification log — Kho từ ngữ tiếng Việt chống giọng AI

Packet: [findings-packet-261004-2340-vietnamese-anti-slop-lexicon.md](findings-packet-261004-2340-vietnamese-anti-slop-lexicon.md)

Thời điểm: 04/10/2026 23:40 đến 05/10/2026 01:00 (UTC+7). Không có `mr`; vòng 4 theo `references/claim-gate.md`.

## A. Quy trình

| Vòng | Việc đã làm | Kết quả |
|---|---|---|
| Thu thập Pass 1–5 | 4 agent song song (A: dấu hiệu AI; B: văn dịch, từ thừa; C: từ hay sai; D: kho văn bản, công cụ). Query tiếng Việt (serper gl vn, hl vi; brave search-lang vi) và tiếng Anh. Danh sách query ở mục 6 của từng báo cáo agent | 4 báo cáo `researcher-261004-2340-vi-*.md`, 142 claim |
| Pass 6 | GitHub (gh api), HF API, archive.org, datasets-server | Repo, kho, từ điển xác minh qua API |
| Thực nghiệm | Sinh 204 bài AI, đo tần suất so với kho Leipzig (mục B) | Bảng 3.2–3.6 của packet |
| 1 Coverage | Tự chấm theo EQ1–EQ8 | EQ1, EQ3, EQ5, EQ7 đủ. EQ2 thiếu sách gốc. EQ4 đủ một phần. EQ6 suy luận. EQ8 đủ |
| 2 Usability | Giữ claim có URL, ngày, nguyên văn. Claim chỉ có snippet ghi rõ | Mục C |
| 3 Independence | Nhóm theo tổ chức. Bản dịch và bản chép không tính nguồn riêng (A08, A09, A12–A14, A19, A21) | `[CONFIRMED]` chỉ khi tôi mở lại nguồn gốc và có lần kiểm thứ hai |
| 4 Truth | Tôi tự mở lại 11 nguồn gốc và tra lại HP2003 (mục C.1) | 11/11 khớp lời agent |
| 5 Gap | 1 vòng: lô AI thứ hai cùng thể loại với kho văn người; thêm Gemini, Claude khi thấy cursor trùng codex | Đóng EQ1. Không mở vòng 2: phần còn hổng (sách gốc, bản HP mới) cần sách giấy |

## B. Phép đo tần suất

### B.1 Dữ liệu

- **Văn người:** Leipzig Corpora Collection, tải 04/10/2026 từ `https://downloads.wortschatz-leipzig.de/corpora/`:
  - `vie_news_2019_100K.tar.gz` (23.999.455 byte);
  - `vie-vn_web_2015_100K.tar.gz` (24.913.750 byte).
  - Dùng file `*-sentences.txt`, chuẩn hóa NFC, chữ thường. Tổng 4.917.594 âm tiết.
- **Văn AI:** 204 file, lưu ở thư mục tạm của phiên, không commit.
  - Hậu tố thêm vào mọi đề: "Chỉ in nội dung hoàn chỉnh, không giải thích thêm, không dùng công cụ, không đọc hay ghi file."
  - Riêng glm CLI phải thêm câu đầu: "Bỏ qua yêu cầu chỉ viết code; đây là nhiệm vụ viết văn bản tiếng Việt." Lý do: system prompt của CLI này là "You are an expert programmer. Generate ONLY executable code."
- **Mô hình** (đọc từ file cấu hình CLI, 05/10/2026):
  - codex: `model = "gpt-5.6-sol"`, chạy với `model_reasoning_effort="low"`;
  - cursor mặc định: `"modelId": "gpt-5.6-sol"`, cùng mô hình với codex nên gộp một họ;
  - grok: `default = "grok-4.6"`;
  - glm: `apiModel: glm-4.6`;
  - cursor `--model gemini-3.7-flash-high`;
  - cursor `--model claude-sonnet-5-thinking-high`.
- **Sự cố đã sửa:** lượt codex đầu đọc stdin nên nuốt các đề còn lại (vòng lặp dừng sau đề 1). Đã xóa bài 01, chạy lại với `</dev/null`.

### B.2 Đề bài

**Lô 1 (14 đề, 4 thể loại):**
1. Viết một báo cáo ngắn (khoảng 350 chữ) về tình hình thị trường xe máy điện ở Việt Nam năm 2025 để trình ban giám đốc.
2. Viết phần giới thiệu (khoảng 300 chữ) cho tài liệu hướng dẫn sử dụng phần mềm quản lý kho dành cho nhân viên mới.
3. Viết nội dung cho 5 slide thuyết trình về kế hoạch chuyển đổi số của một công ty logistics vừa và nhỏ.
4. Viết một bài blog khoảng 350 chữ chia sẻ kinh nghiệm du lịch Đà Lạt tự túc.
5. Viết một bài đăng Facebook khoảng 200 chữ cho một quán cà phê mới khai trương ở Hà Nội.
6. Viết bài blog khoảng 350 chữ về cách quản lý tài chính cá nhân cho người mới đi làm.
7. Viết một công văn gửi Ủy ban nhân dân phường đề nghị hỗ trợ sửa chữa đoạn đường dân sinh bị hư hỏng.
8. Soạn điều khoản bảo mật thông tin trong hợp đồng dịch vụ phần mềm giữa hai công ty.
9. Viết thông báo của công ty về lịch nghỉ Tết Nguyên đán gửi toàn thể nhân viên.
10. Viết các chuỗi giao diện tiếng Việt cho màn hình đăng nhập của một ứng dụng ngân hàng: tiêu đề, nhãn trường, nút và 4 thông báo lỗi.
11. Viết nội dung màn hình giới thiệu (onboarding) 3 bước cho một ứng dụng học tiếng Anh.
12. Viết email tự động xác nhận đơn hàng cho một sàn thương mại điện tử.
13. Viết một bài báo khoảng 350 chữ về việc thành phố đầu tư xây thêm công viên cho người dân.
14. Viết một bài phân tích khoảng 350 chữ về tác động của trí tuệ nhân tạo đối với thị trường lao động Việt Nam.

**Lô 2 (20 đề):** đề 1–10 là bài báo khoảng 300 chữ (giá xăng dầu, thi tốt nghiệp, ngập nước, bóng đá Việt Nam - Thái Lan, khởi nghiệp trồng nấm, ô nhiễm không khí Hà Nội, giá chung cư TP.HCM, du lịch Nha Trang, sức khỏe người cao tuổi, tuyến xe buýt mới). Đề 11–20 là bài blog khoảng 300 chữ (nấu phở bò, nuôi mèo, tập chạy bộ, tự học lập trình, trồng rau ban công, chọn máy tính xách tay cho sinh viên, giữ thói quen đọc sách, tiết kiệm điện mùa nóng, chăm sóc da mặt cho người mới bắt đầu, nghề tự do).

### B.3 Vì sao có lô 2

Lần chạy đầu (lô 1 so với báo và web gộp) cho các cụm dư lớn nhất là *kính gửi* (401 lần), *họ tên*, *vui lòng liên hệ*, *đăng nhập*, *dữ liệu*. Đây là từ đặc trưng thể loại (công văn, giao diện), không phải giọng AI. Lô 2 khớp thể loại với kho văn người để tách hai yếu tố. Mọi số trong bảng 3.2 của packet lấy từ lô 2.

### B.4 Kiểm định

- p một phía theo Poisson: kỳ vọng = (số lần trong văn người / âm tiết văn người) × âm tiết văn AI.
- Giả định độc lập bị vi phạm khi một bài lặp cụm. Cột "bài có cụm" là phép kiểm thứ hai, không phụ thuộc giả định này.
- Ngưỡng dùng trong packet:
  - `[HIGH CONFIDENCE]` khi p < 0,001 và ≥ 4/5 họ dùng dày hơn 2 lần văn người (hoặc ≥ 3/5 với p < 1e-08);
  - `[ASSESSED]` khi p < 0,05 hoặc ít họ;
  - `[LOW CONFIDENCE]` khi p ≥ 0,01 và ≤ 2 họ.

### B.5 Kết quả thô (lô 2)

```
genre phrase            n_ai  exp     p_over    p_under  tag
news  góp phần          22    2.17    2.8e-15   1.0      OVER
news  không chỉ         28    6.01    6.5e-11   1.0      OVER
news  đồng thời         25    6.22    1.2e-08   1.0      OVER
news  thay vì            8    1.92    8.4e-04   1.0      OVER
news  bên cạnh đó       14    4.46    2.3e-04   1.0      OVER
news  trong bối cảnh     9    1.72    7.9e-05   1.0      OVER
news  mà còn            17    2.62    3.1e-09   1.0      OVER
news  đóng vai trò       3    0.64    2.8e-02   1.0      over?
news  hãy                0    4.26    1.0       1.4e-02  UNDER
news  có thể            17   37.21    1.0       1.7e-04  UNDER
news  bởi                2   12.23    1.0       4.3e-04  UNDER
news  một cách           1    3.50    0.97      0.14     ~
news  điều này           2    5.28    0.97      0.10     ~
news  việc              73   64.56    0.16      0.87     ~
news  là một trong những 4    4.08    0.58      0.61     ~
web   hành trình        35    1.70    <1e-15    1.0      OVER
web   hãy              132   11.32    <1e-15    1.0      OVER
web   thay vì           26    1.61    <1e-15    1.0      OVER
web   quan trọng nhất   20    0.95    <1e-15    1.0      OVER
web   bí quyết          13    0.99    5.6e-11   1.0      OVER
web   mà là             10    0.47    1.0e-10   1.0      OVER
web   điều quan trọng   10    0.66    2.5e-09   1.0      OVER
web   dưới đây là        7    0.82    2.5e-05   1.0      OVER
web   chìa khóa          5    0.32    2.0e-05   1.0      OVER
web   việc             107   67.37    5.2e-06   1.0      OVER
web   không chỉ         11    4.99    1.4e-02   0.99     over?
web   có thể            71   51.37    5.4e-03   1.0      over?
web   mà còn             8    2.81    8.3e-03   1.0      over?
web   bởi                3   11.78    1.0       2.7e-03  UNDER
web   một cách           4    5.62    0.81      0.34     ~
web   điều này           4    5.86    0.84      0.30     ~
```

### B.6 Chạy lại mỗi quý

1. Tải lại 2 gói Leipzig (mục B.1) vào `corpus/`.
2. Sinh mẫu mới bằng `run.sh` hoặc `run3.sh` (mục B.7) với `prompts.txt`, `prompts2.txt` (nội dung ở B.2), vào `ai/out*/<nguồn>/NN.txt`.
3. Chạy:
   - `python3 discover2.py out2 5 4 70` để tìm cụm mới;
   - `python3 phrase_test.py out2 phrases.txt` để kiểm danh sách;
   - `python3 structure.py out2` để đo cấu trúc.
4. So với bảng 3.2. Cụm có tỷ lệ dư rơi dưới 2 thì chuyển khỏi kho. Cụm mới đạt ngưỡng B.4 thì thêm vào, kèm ngày.

### B.7 Script

Ba script Python dưới đây, cộng hai script shell sinh mẫu, là toàn bộ công cụ đo. Không có thư viện ngoài.

**`discover2.py`**

```python
"""Excess n-grams in AI Vietnamese vs pre-2022 human text, with model families.

Usage: discover2.py <out-root> <min_prompts> <min_families> <top>
codex and cursor both ran GPT-5.6 Sol, so they count as one family ("openai").
"""
import collections, glob, os, re, sys, unicodedata

ROOT, MIN_P, MIN_F, TOP = sys.argv[1], int(sys.argv[2]), int(sys.argv[3]), int(sys.argv[4])
FAMILY = {"codex": "openai", "cursor": "openai", "glm": "glm", "grok": "grok",
          "gemini": "gemini", "claude": "claude"}
TOKEN = re.compile(r"[^\W\d_]+", re.UNICODE)

def toks(text):
    return TOKEN.findall(unicodedata.normalize("NFC", text).lower())

def grams(ts):
    for n in (2, 3, 4):
        for i in range(len(ts) - n + 1):
            yield " ".join(ts[i:i + n])

human = collections.Counter(); hsize = 0
for f in glob.glob("corpus/*/*-sentences.txt"):
    for line in open(f, encoding="utf-8"):
        ts = toks(line.split("\t", 1)[-1]); hsize += len(ts); human.update(grams(ts))

ai = collections.Counter(); asize = 0
seen = collections.defaultdict(lambda: (set(), set()))
for path in glob.glob(f"ai/{ROOT}/*/*.txt"):
    fam, prompt = FAMILY[path.split("/")[-2]], os.path.basename(path)
    for chunk in re.split(r"[\n.!?;:]+", open(path, encoding="utf-8").read()):
        ts = toks(chunk); asize += len(ts)
        for g in grams(ts):
            ai[g] += 1; seen[g][0].add(prompt); seen[g][1].add(fam)

rows = []
for g, c in ai.items():
    ps, fs = seen[g]
    if len(ps) < MIN_P or len(fs) < MIN_F: continue
    ra, rh = c / asize * 1e4, human[g] / hsize * 1e4
    rows.append((ra / max(rh, 0.005), g, c, len(ps), len(fs), ra, rh))
rows.sort(reverse=True)
print(f"root={ROOT} AI syllables={asize} human syllables={hsize}")
print("ratio\tngram\tn_ai\tprompts\tfamilies\tAI/10k\thuman/10k")
for r in rows[:TOP]:
    print(f"{r[0]:.0f}\t{r[1]}\t{r[2]}\t{r[3]}\t{r[4]}\t{r[5]:.2f}\t{r[6]:.3f}")
```

**`phrase_test.py`**

```python
"""Rate per 10k syllables of fixed phrases: human corpora vs each AI family.

Usage: phrase_test.py <out-root> <phrases.txt>
"""
import collections, glob, re, sys, unicodedata
ROOT = sys.argv[1]
FAMILY = {"codex": "openai", "cursor": "openai", "glm": "glm", "grok": "grok", "gemini": "gemini", "claude": "claude"}
norm = lambda s: unicodedata.normalize("NFC", s).lower()
texts = {"human": norm(" ".join(l.split("\t", 1)[-1] for f in glob.glob("corpus/*/*-sentences.txt") for l in open(f, encoding="utf-8")))}
by = collections.defaultdict(list)
for p in glob.glob(f"ai/{ROOT}/*/*.txt"):
    by[FAMILY[p.split("/")[-2]]].append(norm(open(p, encoding="utf-8").read()))
texts.update({k: " ".join(v) for k, v in sorted(by.items())})
size = {k: len(re.findall(r"[^\W\d_]+", v)) for k, v in texts.items()}
fams = [k for k in texts if k != "human"]
print("phrase\thuman\t" + "\t".join(fams) + "\tAI_mean\tratio\tfam_over2x")
for ph in [l.strip() for l in open(sys.argv[2], encoding="utf-8")]:
    if not ph: continue
    if ph.startswith("#"): print(ph); continue
    pat = re.compile(r"(?<!\w)" + re.escape(norm(ph)) + r"(?!\w)")
    r = {k: len(pat.findall(v)) / size[k] * 1e4 for k, v in texts.items()}
    mean = sum(r[f] for f in fams) / len(fams); h = max(r["human"], 0.005)
    over = sum(r[f] > 2 * h for f in fams)  # how many families use it >2x human rate
    print(f"{ph}\t{r['human']:.2f}\t" + "\t".join(f"{r[f]:.2f}" for f in fams) + f"\t{mean:.2f}\t{mean/h:.1f}\t{over}/{len(fams)}")
```

**`structure.py`**

```python
"""Structural signals per model family vs human sentences.

Usage: structure.py <out-root>
Human corpora are sentence lists, so only sentence-level metrics compare to them.
"""
import glob, re, statistics, sys, unicodedata
ROOT = sys.argv[1]
FAMILY = {"codex": "openai", "cursor": "openai", "glm": "glm", "grok": "grok",
          "gemini": "gemini", "claude": "claude"}
WORD = re.compile(r"[^\W\d_]+", re.UNICODE)

def sentences(text):
    text = re.sub(r"[#*_>`]", " ", text)  # strip markdown marks before splitting
    return [s for s in re.split(r"(?<=[.!?])\s+|\n+", text) if len(WORD.findall(s)) >= 3]

def stats(name, sents, raw):
    lens = [len(WORD.findall(s)) for s in sents]; words = sum(lens) or 1
    mean = statistics.mean(lens); cv = statistics.pstdev(lens) / mean  # burstiness proxy
    per1k = lambda pat: len(re.findall(pat, raw)) / words * 1000
    # patterns kept outside the f-string (older Python forbids backslashes inside it)
    pats = {"emdash": "\u2014", "comma_va": ", và ", "khongchi": "không chỉ", "bold": "\\*\\*",
            "hay": r"(?<!\w)hãy(?!\w)", "viec": r"(?<!\w)việc(?!\w)", "mot_cach": r"(?<!\w)một cách(?!\w)"}
    cols = " ".join(f"{k}/1k={per1k(v):5.2f}" for k, v in pats.items())
    print(f"{name:8} sents={len(sents):6} meanLen={mean:5.1f} CV={cv:4.2f} {cols}")

hs = []; hraw = ""
for f in glob.glob("corpus/*/*-sentences.txt"):
    for line in open(f, encoding="utf-8"):
        s = unicodedata.normalize("NFC", line.split("\t", 1)[-1].strip()); hs.append(s)
hraw = unicodedata.normalize("NFC", "\n".join(hs).lower())
stats("human", [s for s in hs if len(WORD.findall(s)) >= 3], hraw)
by = {}
for p in glob.glob(f"ai/{ROOT}/*/*.txt"):
    by.setdefault(FAMILY[p.split("/")[-2]], []).append(unicodedata.normalize("NFC", open(p, encoding="utf-8").read()))
for fam, texts in sorted(by.items()):
    raw = "\n".join(texts)
    stats(fam, [s for t in texts for s in sentences(t)], raw.lower())
    heads = [l for t in texts for l in t.splitlines() if re.match(r"^\s*(#+|\*\*)", l)]
    title = [h for h in heads if sum(w[0].isupper() for w in WORD.findall(h)) >= max(3, 0.8 * len(WORD.findall(h)))]
    print(f"{'':8} headings={len(heads)} titlecase_headings={len(title)} texts={len(texts)}")
```

**`run.sh`**

```bash
#!/bin/zsh
# Usage: run.sh <model>; writes out/<model>/NN.txt, one file per prompt
m=$1; mkdir -p out/$m; i=0
SUF=" Chỉ in nội dung hoàn chỉnh, không giải thích thêm, không dùng công cụ, không đọc hay ghi file."
while IFS= read -r p; do
  i=$((i+1)); f=out/$m/$(printf %02d $i).txt
  [ -s $f ] && continue
  case $m in
    glm) glm -q "Bỏ qua yêu cầu chỉ viết code; đây là nhiệm vụ viết văn bản tiếng Việt. $p$SUF" --no-quality > $f 2>/dev/null ;;
    codex) codex exec --skip-git-repo-check --ephemeral -s read-only -c model_reasoning_effort='"low"' -o $f "$p$SUF" </dev/null >/dev/null 2>&1 ;;
    cursor) cursor-agent -p --mode ask --trust "$p$SUF" > $f 2>/dev/null ;;
    grok) grok -p "$p$SUF" > $f 2>/dev/null ;;
  esac
  echo "$m $i $(wc -c < $f)"
done < prompts.txt
```

**`run3.sh`**

```bash
#!/bin/zsh
# Usage: run3.sh <label> <cursor-model-id> <prompts-file> <out-root>
label=$1; model=$2; pf=$3; root=$4; mkdir -p $root/$label; i=0
SUF=" Chỉ in nội dung hoàn chỉnh, không giải thích thêm, không dùng công cụ, không đọc hay ghi file."
while IFS= read -r p; do
  i=$((i+1)); f=$root/$label/$(printf %02d $i).txt
  [ -s $f ] && continue
  cursor-agent -p --mode ask --trust --model $model "$p$SUF" </dev/null > $f 2>/dev/null
  echo "$label $root $i $(wc -c < $f)"
done < $pf
```

**`phrases.txt`** (59 cụm kiểm từ trên xuống):

```
# nhóm A: có nguồn tiếng Việt
không chỉ
trong bối cảnh
phát triển không ngừng
tóm lại
nhìn chung
không thể phủ nhận
trong thế giới
hơn nữa
thêm vào đó
đồng thời
qua đó
từ đó
đóng vai trò
vai trò quan trọng
đột phá
vượt trội
trong bài viết này
hy vọng
tạo giá trị
dưới đây là
tưởng chừng
không đơn thuần
không phải là
# nhóm P: phỏng đoán, chưa nguồn
hãy cùng
khám phá
hành trình
bức tranh
góp phần
một cách
điều này
đa dạng và phong phú
đầy màu sắc
là một trong những
có thể
được thực hiện bởi
bởi
việc
sự
tuy nhiên
bên cạnh đó
ngoài ra
quan trọng
then chốt
nâng cao
tối ưu
hiệu quả
trải nghiệm
nuôi dưỡng
tâm hồn
lan tỏa
chìa khóa
bí quyết
thay vì
mà là
hãy
điều quan trọng
```

## C. Kiểm từng claim trọng yếu

### C.1 Nguồn tôi tự mở lại (vòng 4)

| Claim | Agent báo | Tôi mở lại (05/10/2026) | Khớp |
|---|---|---|---|
| X03 Kobak | delves r=28,0; ≥13,5%; 454 | PMC12219543 qua jina-read: "delves (_r_=28.0), underscores (_r_=13.8), and showcasing (_r_=10.7)"; "at least 13.5% of 2024 abstracts"; "(to 454) in 2024" | Có |
| R26 LanguageTool | Không hỗ trợ vi | `curl api.languagetool.org/v2/check language=vi`: "'vi' is not a language code known to LanguageTool" | Có |
| T11 Hoàng Công Bình | 427/649 = 65,8% | PDF vci.vnu.edu.vn: "Câu bị động 427 65,8 … Câu chủ động 184 28,4 … Câu trung gian 38 5,9 … Tổng cộng 649" | Có |
| T28 Đỗ Văn Học | danh sách từ thừa | PDF std.vnuhcmjournal.com.vn: "Tái tạo lại, chưa vị thành niên, hoàn thành xong, đáp ứng theo, căn cứ theo, đại quy mô lớn, cấm không được, tối ưu nhất, hoàn toàn rất, đề xuất kiến nghị, nhu cầu đòi hỏi" | Có |
| X05 BrandsVietnam | câu mở, cấu trúc, phương pháp | help.brandsvietnam.com: "“Trong bối cảnh ngành [XYZ] đang phát triển không ngừng…”", "“không chỉ… mà còn…”, “tưởng chừng… nhưng…”", "bài blog khoảng 2.000 chữ về chủ đề Ambient Advertising" | Có |
| W36 Luật Thương mại Điều 88 | "Khuyến mại là hoạt động…" | vcci.com.vn: "Khuyến mại 1. Khuyến mại là hoạt động xúc tiến thương mại của thương nhân nhằm xúc tiến việc mua bán hàng hoá…" | Có |
| T19, T18 Nguyễn Đức Dân | đại thụ; tham gia giao thông | thvl.vn: "nay đã thành “đúng”: cây đại thụ, đường quốc lộ, người nông dân"; "có thể thay “tham gia giao thông” bằng “đi lại”" | Có |
| T21, T24 Hồ Anh Thái | tái … lại; Nhưng tuy nhiên | tienphong.vn: "Tái sinh lại, tái hiện lại, tái diễn lại, tái bản lại, phục chế lại"; "Nhưng tuy nhiên. Đã nhưng lại còn tuy nhiên." | Có |
| W06 An Chi | điểm yếu = nhược điểm | thanhnien.vn: "Điểm yếu là một danh ngữ tạo ra theo cú pháp “xuôi” của tiếng Việt, đồng nghĩa với nhược điểm [弱點]" | Có |
| T09 Mozilla | chủ động; Thiết lập | mozilla-l10n.github.io/styleguides/vi/: "Cố gắng chuyển câu bị động tiếng Anh thành câu chủ động tiếng Việt"; "“Thiết lập” chứ không phải “Những thiết lập” hay “Các thiết lập”" | Có |
| HP2003 (W01, W06, W12, W13, W15, H02, khuyến mãi, chẩn đoán) | các mục từ | Hai bản OCR (6.259.965 và 6.330.552 byte), chuẩn hóa NFC rồi tìm: "sát nhập x. sáp nhập."; "yếu điểm d. (id.), Điểm quan trọng nhất"; "trau giổi (cũ; id.)" (OCR của *giồi*); "chỉn chu t, Chu đáo, cẩn thận"; "vô hình trung p. Tuy không có chủ định"; "cứu cánh d. Mục đích cuối cùng"; "khuyến mãi đg. Khuyến khích việc mua hàng"; "chẩn đoán đg. Xác định bệnh" | Có. *xán lạn* không tìm được bằng regex (OCR méo) nên hạ còn `[ASSESSED]` |

### C.2 Khối kiểm theo claim-gate

**M01–M02 (cụm dư trong văn AI)**
- Triage: fact (thực nghiệm), stakes MED, domain ngôn ngữ, live_search không cần.
- Giả thuyết: H1 AI dùng dày hơn người. H2 chênh do thể loại hoặc đề bài. H3 chênh do năm (văn người 2015/2019, văn AI 2026). H-null ngẫu nhiên.
- Bằng chứng: lô 2 khớp thể loại loại phần lớn H2; lọc ≥ 5 đề loại từ của một đề; p < 0,001 loại H-null. H3 chưa loại hết: tiếng Việt 2026 có thể đã dùng *hành trình* nhiều hơn 2019 (một phần vì chính văn AI). Yakura 2024 thấy người bắt chước từ của LLM trong tiếng Anh (A37).
- Verdict: Đúng, mức Vừa đến Cao tùy cụm. Tag theo B.4.
- Diễn giải thay thế giữ lại: H3. Ghi ở điểm mù 8.5 của packet.

**M03 (cụm bị nghi oan)**
- H1 không dư. H2 dư nhưng mẫu nhỏ nên không thấy.
- *bởi*, *có thể* (báo) **thiếu** có ý nghĩa thống kê, nên H2 bị loại cho hai từ này. *một cách*, *điều này*: số kỳ vọng 3,5–5,9, quan sát 1–4, không có tín hiệu dư.
- Verdict: Đúng, mức Cao cho *bởi*, *có thể*, *một cách*, *điều này*.

**M04 (15 cụm không xuất hiện)**
- 0/120 bài. Với cụm hiếm trong văn người (kỳ vọng < 1), không xuất hiện cũng chưa chứng minh AI tránh cụm đó.
- Verdict: Phức tạp hơn claim → `[ASSESSED]`. Câu đúng là "không phải tật của mô hình 2026", không phải "AI không bao giờ dùng".

**M05 (gạch dài)**
- Đo: lô 2 cả 5 họ 0,00–0,31 trên 1.000 chữ; lô 1 tối đa 3,18 (Grok). Văn người 0,00 (Leipzig có thể đã chuẩn hóa dấu, chưa kiểm).
- Khớp VnExpress 15/11/2025 (A12, bản dịch, mở qua WebFetch).
- Verdict: Đúng, mức Vừa → `[HIGH CONFIDENCE]`.

**X01 (chưa có nghiên cứu đếm cụm AI tiếng Việt)**
- Bằng chứng phủ định: 52 query (agent A), cộng ViDetect và VietBinoculars đã đọc.
- Verdict: Đúng, mức Vừa → `[HIGH CONFIDENCE]`.

**W36 (khuyến mại/khuyến mãi)**
- H1 khuyến mại đúng. H2 khuyến mãi đúng. H3 phụ thuộc ngữ cảnh.
- Luật dùng *khuyến mại*; HP2003 chỉ *khuyến mãi*; báo chí mâu thuẫn về nghĩa.
- Verdict: Phức tạp hơn claim → `[ASSESSED]`, chuyển cho bạn (Q8) và chuyên gia (cờ human-review 1).

### C.3 Độc lập nguồn (vòng 3)

- Nhóm A: 4 nguồn tiếng Việt thật (BrandsVietnam, Công dân & Khuyến học, Finhay, repo Hàng Nhựt Long). Bỏ ai-hay.vn (chép BrandsVietnam), VnExpress, VnReview, tex.vn (dịch từ tiếng Anh). BrandsVietnam và repo GitHub có thể ảnh hưởng nhau; chưa loại trừ.
- Nhóm B: Microsoft và Mozilla là hai tổ chức khác nhau. Hồ Anh Thái, Đặng Minh Phương, Lê Hữu, tgpsaigon.net là 4 tác giả khác nhau nhưng đều không phải nhà ngôn ngữ học.
- Nhóm C: hai bản quét HP2003 là **một** ấn bản (hai lần OCR). Không tính hai nguồn.
- Phép đo: 5 họ mô hình khác hãng. codex và cursor cùng GPT-5.6 Sol, đã gộp.

## X. Claim bị loại hoặc hạ mức

| Claim | Lý do | Xử lý |
|---|---|---|
| "*sát nhập* không có trong từ điển" (nhiều bài báo) | HP2003 có mục "sát nhập x. sáp nhập" | Sai với HP2003. Viết lại thành "dạng trỏ về *sáp nhập*" |
| "Văn AI có câu đều nhịp" (Finhay, repo) | Đo CV không khác văn người | Hạ `[LOW CONFIDENCE]`, không dùng làm tiêu chí |
| "Gạch dài là dấu hiệu AI mạnh" (BrandsVietnam, VnExpress) | Mô hình 2026 gần như không dùng | Hạ, ghi "đã hết hạn" |
| "*một cách*, *điều này*, *bởi*, *có thể* là dấu hiệu AI" (giả định trong đề bài của chính tôi giao cho agent A, B) | Đo không dư hoặc thiếu | Chuyển sang danh sách "đừng sửa" |
| "*hãy cùng khám phá*, *bức tranh*, *đa dạng và phong phú*, *thế giới đầy màu sắc*" là cụm AI | 0 nguồn (agent A) và 0/120 bài | Loại khỏi kho |
| "delve +400%", "3.900%" (bài Bouchard qua VnReview) | Không khớp Kobak, chưa kiểm gốc | Không dùng |
| "35% trang web mới có văn AI" (Pew) | Chỉ snippet, chỉ tiếng Anh | Không dùng cho tiếng Việt |
| "Pangram: *not just X but Y* dày gấp 3 lần" | Qua The Atlantic, paywall, chỉ snippet | Giữ làm tham chiếu, không làm căn cứ chính |
| Ví dụ "chim bay trên trời" (Microsoft) | Chỉ thấy ở bản chuyển thể ChatsControl, không thấy trong PDF gốc | Không dùng |
| *tu bổ*, *lãng phí*, *giải thưởng*, *xuất sắc* (đề bài giao agent C) | Đề bài của tôi ghi nhầm cặp giống hệt nhau hoặc thiếu dạng sai | Bỏ, không phải câu hỏi của bạn |

## D. Ghi chú quy trình

- **Tải file chưa xin phép:** agent nhóm B tải PDF style guide của Microsoft về thư mục tạm bằng curl, rồi xóa ngay và đọc lại bằng jina-read. Agent nhóm C tải hai bản OCR HP2003 (khoảng 6 MB mỗi bản) từ archive.org vào thư mục tạm. Cả hai không commit vào repo. Prompt của tôi không cấm rõ việc tải; lần sau sẽ ghi rõ.
- **Bạn đã cho phép:** tải 2 gói Leipzig (49 MB); gọi glm, codex, cursor, grok CLI. Tôi mở rộng từ khoảng 40 bài lên 204 bài và thêm Gemini, Claude qua cursor sau khi thấy cursor trùng mô hình với codex. Mục đích: đủ mẫu và đủ họ mô hình độc lập.
- **Tiến trình nền:** các vòng lặp sinh mẫu đã kết thúc. searxng không dùng.
- **Lỗi tự gây đã sửa:** codex nuốt stdin (B.1); thiết kế đo ban đầu lẫn thể loại (B.3).

## E. Điểm mù (lặp lại từ packet, mục 8)

1. Mẫu AI nhỏ (khoảng 7.000 âm tiết mỗi họ ở lô 2).
2. Poisson giả định độc lập.
3. Không có mốc văn người cho mở bài, kết bài.
4. Claude Sonnet 5 thay cho Opus/Fable; GLM chạy với system prompt lập trình.
5. Văn người 2015/2019 so với văn AI 2026; web 2015 không thuần blog.
6. Chưa mở sách gốc Cao Xuân Hạo, Nguyễn Đức Dân, Nguyễn Hiến Lê.
7. Chỉ HP2003; OCR lỗi dấu.
8. Chưa đo hợp đồng, công văn AI kỹ; chưa đo AI khi có chỉ dẫn văn phong.
9. Giấy phép Leipzig, độ chính xác VietAIDetector, mức nhiễm AI web tiếng Việt: chưa kiểm.
10. Không tìm được bài của Lê Trung Hoa, Phạm Văn Tình, Đào Tiến Thi, Lê Xuân Mậu.
