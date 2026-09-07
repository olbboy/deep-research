# Vòng thu thập và kiểm chứng

Dùng bởi `SKILL.md`. Không merge `config.yml`. Không xếp tier competitor cho CI.

Chạy Pass 1–5 bắt buộc. Pass 6 khi tín hiệu nền tảng quan trọng. Query song song khi runtime cho phép.

## Pass 1 — Toàn cảnh (tiếng Anh / nguồn quốc tế)

Mục tiêu: bản đồ toàn cục, báo cáo, số liệu neo.

Query mỗi synonym của chủ đề:

```
"<synonym> market size share 2025 2026"
"<synonym> key players landscape"
"<topic> industry report forecast CAGR"
```

Ưu tiên Codex / Grok / Cursor / Perplexity khi có. Hết quota → `search_web`.

Collector kèm skill: `collect.py serper "<query>" --gl us --hl en` **và** `collect.py brave "<query>"` cho cùng query — hai index khác nhau, lệch nhau là tín hiệu cần Pass 5. Báo cáo/CAGR: thêm `serper --type scholar`.

## Pass 2 — Ngôn ngữ địa phương

Với **mỗi** thị trường trong scope, search bằng ngôn ngữ / thuật ngữ địa phương.

Việt Nam: **bắt buộc** query tiếng Việt. Tiếng Anh về Việt Nam không thay được.

Collector: `collect.py serper "<query tiếng Việt>" --gl vn --hl vi` và `collect.py brave "<query tiếng Việt>" --search-lang vi` (Brave không có `--country VN`, giữ `ALL`).

## Pass 3 — Mở synonym / phân loại khác

Cùng hiện tượng, tên ngành khác. Ví dụ: "AI camera" bỏ sót video analytics software.

Collector: `collect.py searxng "<synonym>" --language vi` — một lệnh gom nhiều engine, `suggestions[]` trong output gợi synonym mới; `--categories science` cho học thuật.

## Pass 4 — Cạnh / cụm

Tìm thực thể được nhắc trong báo chí, "alternatives to", bảng key players.
Nếu phát hiện cụm có tên ("Big N", nhóm địa phương): lấy **đủ** thành viên. Thiếu → thêm ngay.

Không cứng hóa danh sách cụm — phát hiện theo topic.

Collector: `searxng "<topic> alternatives"` và `searxng "<topic> key players" --categories news --time-range year` để gom thành viên cụm từ nhiều engine cùng lúc.

## Pass 5 — Thẩm sâu + bịt hổng

Deep search cho KIQ còn trống và số liệu mâu thuẫn.
Thiếu tool sâu → thêm `search_web` có năm, phạm vi, đơn vị.

Collector: `serper --type news --tbs qdr:y` / `brave --type news --freshness pm` cho tin mới; `jina-search "<KIQ>"` khi cần nội dung trang ngay; `jina-read <url>` để mở **trang gốc** của mọi số liệu mâu thuẫn trước khi sang vòng kiểm.

## Pass 6 — Nền tảng (khuyến nghị)

Khi kiến trúc / sentiment / hiring quan trọng:

- GitHub, YouTube, RSS, đọc trang gốc
- X / LinkedIn nếu backend sẵn

Có `mr`: `mr collect agent-reach` / `mr collect grok-search --mode x`. Không `mr`: web tool + URL gốc, hoặc `jina-read` cho GitHub README / blog / trang hãng (`--with-links` để lấy link con).

## Rút claim

Từ toàn bộ pass, liệt kê material claim:

1. Số liệu (size, CAGR, doanh thu, share, giá, KPI)
2. Khẳng định cạnh tranh (hạng, #1, funding, M&A)
3. Luật / nghĩa vụ / ngày hiệu lực
4. Dự đoán / "nhanh nhất"
5. Nhân-quả / chiến lược

Sự thật định nghĩa ổn định và số nội bộ của user: chỉ spot-check.

## Năm vòng kiểm

### 1 — Coverage

Câu hỏi: bằng chứng đã trả lời KIQ chưa?

```bash
mr verify doctor
mr verify fanout "<KIQ>"
mr verify track "<KIQ>"
```

| Gợi ý | Việc làm |
|-------|----------|
| `sufficient` | Đóng KIQ này |
| `continue` | Tool tiếp |
| `escalate` | Đổi họ model hoặc viết lại câu |
| `diminishing` | Dừng; ghi `⬜ BLIND SPOT` |

Không `mr`: tự chấm — có số + đơn vị + thời điểm + URL kiểm được thì đủ để sang vòng 2.

### 2 — Usability

Câu hỏi: câu trả lời nào sourced, dated, checkable?

```bash
mr verify select "<KIQ>" --from-db --persist --json
```

Giữ figure chỉ câu thua mới có (Zero Data Loss). Xung đột số → `stakes=HIGH` vào vòng 4.
Điểm verifier **không** đổi thẻ tin cậy.

### 3 — Independence

Câu hỏi: origin sơ cấp có tách không?

```bash
mr verify-sources "<url1>" "<url2>" ... --json
```

Hai AI-search chung một origin = 1 nguồn. `[CONFIRMED]` cần ≥1 nguồn non-AI **hoặc** ≥2 origin sơ cấp khác nhau.
Không `mr`: nhóm bằng registrable domain; bỏ `codex://`, `grok://`.
`serper` / `brave` / `jina-search` / `searxng` là **index**, không phải nguồn: origin = `origin` của từng kết quả. Cùng một URL hiện ở cả Serper lẫn Brave vẫn là **1** origin. Xác nhận origin sơ cấp bằng `jina-read`.

### 4 — Truth

Ưu tiên `kiem-chung-thong-tin`. Vắng → `claim-gate.md`.
Tiền / chiến lược: `stakes=HIGH`, `live_search=YES`.

### 5 — Gap

Chỉ re-collect KIQ còn mở hoặc conflict. **Tối đa 2** vòng gap rồi hard-stop: `diminishing` / `escalate` / `⬜ BLIND SPOT`.

## Dừng

Dừng khi mọi claim trọng yếu có verdict, không `Sai` trong packet, hổng đã nêu, hoặc coverage `diminishing`/`sufficient` trên mọi KIQ đã hỏi.
