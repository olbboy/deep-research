# Verification Log — Coast FIRE claim check

**Ngày:** 2026-09-09 · **Gói kèm:** `findings-packet-260909-0015-coast-fire-claim-verification.md`

## KIQ (câu hỏi thiết yếu, theo essential-questions MODE=VERIFY)

| # | Câu hỏi | Loại | Trạng thái |
|---|---|---|---|
| ★★★ K1 | Quan tâm tới Coast FIRE có đang tăng không? | `[RESEARCH]` | ✅ sufficient |
| ★★★ K2 | Quy mô tuyệt đối có đủ để gọi "sốt" không? | `[RESEARCH]` | ✅ sufficient |
| ★★★ K3 | Có phải hiện tượng **của giới trẻ** không? | `[RESEARCH]` | ⬜ diminishing → BLIND SPOT |
| ★★★ K4 | Công thức là gì, tham số nào chỉnh được? | `[FACT]` | ✅ sufficient |
| ★ K5 | Các tham số mặc định có ổn định giữa các nguồn? | `[RESEARCH]` | ✅ sufficient |
| ★ K6 | Chế độ hỏng / phản biện đã ghi nhận? | `[JUDGMENT]` | ✅ sufficient |
| ○ K7 | Ai đặt ra thuật ngữ, khi nào? | `[FACT]` | ⬜ không giải được |

**Bẫy đã tránh (Step 2 triage):** Claim A trông như `[FACT]` nhưng thực chất là `[JUDGMENT]` — "sốt" là từ định tính không có ngưỡng. Cách xử: tách A thành 4 mệnh đề con đo được (A1–A4), đo từng cái riêng. Không ép Claim A thành một verdict đúng/sai duy nhất (dogmatic absolutism), cũng không quy về "tuỳ cảm nhận" (subjective relativism).

## Các pass thu thập

| Pass | Nội dung | Công cụ | Kết quả |
|---|---|---|---|
| 1 | Toàn cảnh tiếng Anh | serper `--gl us`, brave | OK |
| 2 | **Tiếng Việt (bắt buộc)** | serper `--gl vn --hl vi` | OK — 0 nguồn riêng về Coast FIRE |
| 3 | Synonym (Coast FI, coasting to FI) | brave, serper | OK |
| 4 | Cụm biến thể FIRE (Lean/Fat/Barista/Chubby) | serper + RedPulse | OK |
| 5 | Thẩm sâu số mâu thuẫn | jina-read trang gốc | OK |
| 6 | Nền tảng (Reddit, Trends, học thuật) | Trends API, RedPulse, Scholar | Một phần (xem lỗi) |
| — | Vòng đối kháng đa tác tử | Workflow `deep-research` | 105 tác tử · 100 claim · 74 phiếu (22 bác / 52 giữ) |

## Nguồn sơ cấp tự mở kiểm (không qua trung gian)

| Nguồn | Cách lấy | Dùng cho |
|---|---|---|
| Google Trends API | tự viết script, 4 rổ truy vấn riêng | A1, A2, A3, A9 |
| creditkarma.com (trang gốc + phần Methodology) | jina-read | A5 |
| walletburst.com/tools/coast-fire-calc/ | jina-read | B1 |
| Công thức Coast FIRE | tự chạy lại bằng Python, quan hệ Fisher chính xác | B2 |
| CrossRef DOI registry `10.1108/JCM-07-2021-4788` | agent verify | Điểm mù #3 |
| Vanguard *How America Saves 2025* (PDF 112 tr.) | agent verify tải + pdftotext | A6 |

## Vòng 3 — Độc lập nguồn

Nhóm theo registrable domain. `serper` / `brave` / `searxng` là **index, không phải nguồn** — origin tính theo từng URL.

- **Gắn `[CONFIRMED]` cho A1–A2:** hai origin sơ cấp tách biệt — hành vi tìm kiếm (trends.google.com) và xuất bản báo chí (nerdwallet.com, usatoday.com, businessinsider.com, investopedia.com…). Hai cơ chế sinh dữ liệu độc lập nhau.
- **Gắn `[CONFIRMED]` cho B:** walletburst.com (nguồn sơ cấp) + tôi tự tái lập phép toán + ChooseFI/Financial Samurai/Kiplinger/Empower nêu độc lập cùng công thức.
- **Hạ xuống `[LOW CONFIDENCE]`:** con số 53% Gen Z. Mọi bài báo trích nó đều quy về **một** origin duy nhất (creditkarma.com). The Hill, Bloomberg… không phải nguồn độc lập thứ hai.

## Vòng 4 — Truth gate: các claim bị bác / hạ cấp

| Claim | Xử lý | Lý do |
|---|---|---|
| "53% Gen Z theo FIRE" ⇒ chứng minh Coast FIRE hot | **Bác** | Khảo sát không hề nhắc Coast FIRE; đo tự-nhận-diện; n=1.006 cho **toàn bộ** thế hệ, nhóm con Gen Z nhỏ; panel marketing thương hiệu |
| Vanguard chứng minh xu hướng tiết kiệm của giới trẻ do FIRE | **Bác** | Đọc nguyên PDF: 0 lần nhắc FIRE/Gen Z/Millennial. Tăng tiết kiệm quy cho tự-động-ghi-danh (10%→61% số quỹ), không phải phong trào |
| Coast FIRE là hiện tượng đại chúng | **Bác** | Trends: 0–1 điểm khi `401k` = 44–80 |
| r/coastFIRE "51.000+ thành viên" (firenum.com) | **Hạ cấp** | Không ghi ngày; mâu thuẫn RedPulse 128.333 (ghi rõ 08/09/2026). Giữ cả hai trong log theo Zero Data Loss |
| r/Fire 1.007.269 vs 893.489 | **Giữ cả dải** | Hai origin, số vênh; nhiều khả năng RedPulse cache cũ. Không lấy trung bình |
| Trinity Study = "100% thành công" (walletburst tự mô tả) | **Gắn cờ** | Mạnh hơn nghiên cứu gốc; con số thường trích cho 50/50 @4%/30 năm là ~95% |
| SWR = 4% là hằng số | **Bác** | Bengen 4,0→4,5→4,7→5,25-5,5%; Morningstar 3,3→4,0→3,9%. Hai phương pháp khác bản chất, **không hoà giải, giữ cả hai dải** |
| "Không có văn liệu học thuật nào về FIRE" *(giả định ban đầu của tôi)* | **Tự bác** | Scholar search của tôi trả nhiễu → tôi suy sai. Agent verify tìm ra Khan & Pandey (JCM 2023), xác nhận qua CrossRef. **Đã sửa trong packet.** |

## Lỗi công cụ (ghi để tái lập)

| Công cụ | Lỗi | Cách vòng qua |
|---|---|---|
| Reddit `about.json` | HTTP 403 (chặn bot) | RedPulse + snippet SERP từ reddit.com |
| `r.jina.ai` → reddit.com | "blocked by network security" | như trên |
| The Hill | trang chống bot | tìm thẳng origin gốc (creditkarma.com) — **tốt hơn** cho vòng 3 |
| serper `--type news` + dấu ngoặc kép | HTTP 400 "Query pattern not allowed for free accounts" | chuyển brave `--type news` |
| Google Scholar qua serper | ~90% nhiễu (hàng hải, cháy rừng) | agent verify + CrossRef |
| RedPulse r/leanfire, r/fatFIRE | regex không khớp | bỏ; không cần cho kết luận |
| `timeout` (macOS) | không có lệnh | bỏ, dựa vào timeout của harness |

## Dừng

Đạt điều kiện dừng: mọi claim trọng yếu đã có verdict · không còn `Sai` trong packet · hổng đã nêu tên (K3, K7) · coverage `sufficient` trên K1/K2/K4/K5/K6, `diminishing` trên K3. **Không** chạy vòng gap thứ 2 — K3 (phân bố tuổi Coast FIRE) không tồn tại dữ liệu công khai, thêm vòng nữa không đổi kết quả.

## Câu mở

1. Nguồn gốc câu cần kiểm (K7 chưa giải: ngay r/coastFIRE cũng gọi nguồn gốc thuật ngữ là "a true mystery").
2. Bối cảnh Việt Nam **chưa kiểm** — bộ mặc định Mỹ (7%/3%/4%) dựa trên lịch sử thị trường Mỹ và có mặc định an sinh xã hội Mỹ; cần vòng nghiên cứu riêng, không suy ra được từ gói này.

---

## Hậu kiểm — kết quả cuối của workflow (bổ sung 00:50)

**Thống kê run:** 105 tác tử · 105 xong · **0 lỗi** · 1.435 lượt gọi tool · ~11,79 triệu token subagent · 46 phút 8 giây.

### ⚠️ Payload tổng hợp cuối bị hỏng — không dùng

Bước synthesis cuối trả về placeholder chẩn đoán thay vì findings thật:

```
"summary": "Test minimal payload to diagnose schema error."
"findings": [{"claim":"Test claim.", "sources":["https://example.com"], "evidence":"Test evidence."}]
"caveats": "Test caveat."   "openQuestions": ["Test question?"]
```

→ Agent synthesis gặp lỗi schema và phát payload tối thiểu. **Không có claim nào trong `findings` được dùng.** Gói phát hiện được dựng từ `journal.jsonl` (100 claim thô + 74 phiếu verify có bằng chứng đầy đủ) và từ nguồn sơ cấp tôi tự mở kiểm. Mảng `refuted` **có** giá trị thật và đã được xử lý dưới đây.

### Xử lý 8 claim bị bác

| Claim bị bác | Phiếu | Tôi có dùng? | Xử lý |
|---|---|---|---|
| Vanguard *HAS 2025* "không có phân tách theo tuổi/thế hệ" | 0–3 | **Chỉ dùng nửa đúng** | Nửa "0 lần nhắc FIRE/Gen Z/Millennial" được cả 3 phiếu xác nhận qua pdftotext → giữ. Nửa "không có phân tách tuổi" **sai** → bỏ, và **dùng chính dữ liệu tuổi đó** làm bằng chứng mạnh hơn (A4, A6) |
| "53% Gen Z theo FIRE" | 0–3 | Có, làm **bằng chứng ngược** | Trùng khớp: cả 3 phiếu bác đúng trên 3 lý do tôi đã nêu. Bổ sung mẫu con ~120–135, sai số ±8–9pp, và đối chiếu SoFi ~4% |
| Bengen 4,7% (bản dẫn Wikipedia) | 1–2 | Có, **nhưng qua nguồn khác** | Bác nhắm *nguồn* (Wikipedia tam cấp) và nửa "4,8%" vô căn cứ — **không** nhắm số 4,7%. Bản dẫn CNBC + bengenfs.com + Kiplinger được giữ 0-bác. → Đã đổi sang nguồn sơ cấp, thêm tên sách, thêm điều kiện 30 năm/đa dạng hoá, **loại 4,8%** |
| Fortune: công thức Coast FIRE | 0–3 | **Không** | Công thức trong gói lấy từ walletburst (sơ cấp) + tôi tự tái lập. Fortune cắm lợi suất danh nghĩa vào số mũ — sai; walletburst dùng lợi suất **thực**. Gói đã đúng từ đầu |
| Empower định nghĩa Coast FIRE | 0–3 | **Không** | — |
| Yahoo: ví dụ "Leslie" | 1–2 | **Không** | — |
| Yahoo: phản biện Jahanzeb Nawaz | 0–3 | **Không** | — |
| CNBC: ví dụ 25 tuổi/$175k | 0–3 | **Không** | Riêng phần "FIRE number = thu nhập × 25 ≡ ÷ 4%" trong cùng bài **được giữ** (0-bác, xác minh trực tiếp bằng curl) |

**Kết luận hậu kiểm:** không claim `Sai` nào lọt vào gói. Một chỗ tôi tự sửa (văn liệu học thuật), một chỗ đổi nguồn (Bengen), một chỗ nửa-đúng-nửa-sai được tách và phần sai bị loại (Vanguard) — phần sai đó lại sinh ra bằng chứng mạnh hơn cho câu hỏi "giới trẻ".
