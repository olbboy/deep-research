# Cổng claim (fallback khi không có kiem-chung-thong-tin)

Ưu tiên skill `kiem-chung-thong-tin` (TKC v2.0 × ACV v3.0). File này chỉ khi skill đó **không** có trong catalog.

Không viết battlecard / playbook. Chỉ gắn verdict + tag cho findings packet.

## Phải kiểm

Số liệu, khẳng định cạnh tranh, luật, dự đoán, nhân-quả.
Định nghĩa ổn định và số nội bộ user: spot-check.

## Bảy bước

1. **Triage** — fact / prediction / interpretation. `depth` 1–3, `stakes` LOW/MED/HIGH, `domain`, `live_search`. Tiền / chiến lược → `stakes=HIGH`, `live_search=YES`.
2. **Phân rã (TKC)** — tách umbrella theo phạm vi (toàn cầu vs địa phương; SW vs HW vs dịch vụ).
3. **Giả thuyết** — H1 ủng hộ · H2 đối lập / số khác · H3 phụ thuộc định nghĩa · H-null.
4. **Bằng chứng** — 3–5 query đa góc; nguồn ≤18 tháng, độc lập; tam giác kỹ thuật · thị trường · đồng thuận + phản chứng. `weight = credibility×0.4 + recency×0.2 + independence×0.2 + expert_consensus×0.2`; loại `<0.3`.
5. **Chống thiên kiến** — base-rate, cherry-pick khung thời gian, tương quan ≠ nhân quả. `stakes=HIGH` → red-team. Thị phần = adoption hiện tại; CAGR = tiềm năng tăng; dòng vốn = cơ hội kỳ vọng — không cái nào = độ chín kỹ thuật.
6. **Tổng hợp** — verdict + mức tin cậy. Cờ human-review nếu `max(P)<0.65` hoặc `stakes=HIGH` hoặc nhiều ngụy biện — đúng 3 câu hỏi chuyên gia.
7. **Kết luận sắc thái** — chấp nhận "Phức tạp hơn claim" thay vì ép nhị phân.

Nếu `kiem-chung-thong-tin` chạy: giữ nguyên khối tiếng Việt trong log.

## Bước 4.5 — Độc lập nguồn (trước khi gắn tag)

| `source_type` | Ví dụ |
|---------------|--------|
| AI-search | `codex`, `gemini-deep-research`, `glm-search`, Grok/Cursor search |
| non-AI | World Bank, FRED, SEC, filing, trang hãng, primary |

`[CONFIRMED]` chỉ khi ≥1 non-AI **hoặc** ≥2 AI-search khác **primary origin**.
Hai AI-search chung origin = 1 nguồn → trần `[ASSESSED]`.

```bash
mr verify-sources "<url1>" "<url2>" ... --json
```

Không `mr`: nhóm registrable domain; bỏ URL giả `codex://` / `grok://`. Analyst vẫn phải xác nhận origin là sơ cấp (bài syndicate không tính origin riêng).

## Mapping tag

Xem `findings-packet.md`. Đúng+Cao không được thành `[CONFIRMED]` nếu 4.5 không cho phép.
