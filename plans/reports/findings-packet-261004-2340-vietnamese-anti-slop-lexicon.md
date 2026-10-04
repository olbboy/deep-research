---
title: "Findings packet — Kho từ ngữ và văn bản mẫu giúp agent viết tiếng Việt chính xác, không lộ giọng AI"
generated: "2026-10-05"
timezone: "UTC+7"
tools: "runtime-web (collect.py: serper, brave, jina-search, jina-read), WebSearch/WebFetch (agent), archive.org OCR, gh api, HF API; 4 agent thu thập song song; phép đo tần suất tự chạy: 204 bài do 5 họ mô hình viết, so với 200.000 câu tiếng Việt thu trước 2022 (Leipzig Corpora)"
verifier_engine: "none (không có `mr`); vòng 4 theo claim-gate; phép đo dùng kiểm định Poisson một phía"
---

# Findings packet — Kho từ ngữ tiếng Việt chống giọng AI

Nhật ký kiểm từng claim, cách đo, đề bài, claim bị loại: [verification-log-261004-2340-vietnamese-anti-slop-lexicon.md](verification-log-261004-2340-vietnamese-anti-slop-lexicon.md)

Nối tiếp: [findings-packet-261003-1136-vietnamese-standard-usage.md](findings-packet-261003-1136-vietnamese-standard-usage.md) (chính tả, số, tiền, viết hoa). Packet này không lặp lại phần đó.

## 0. Tóm tắt 60 giây

1. **Trước phiên này chưa ai đếm "giọng AI" trong tiếng Việt.**
   - Hai nghiên cứu phát hiện văn AI tiếng Việt (ViDetect 2024, VietBinoculars 2025) dùng bộ phân loại máy, không nêu cụm từ nào làm lộ (A26–A31).
   - Các danh sách "cụm AI" đang lưu hành dựa trên 1 prompt, 1 chủ đề (BrandsVietnam) hoặc ý kiến cá nhân (A01–A16).
   - Vì vậy tôi tự đo. 5 họ mô hình viết 204 bài. Bài được so với 4,9 triệu âm tiết báo và web tiếng Việt thu trước khi có ChatGPT (mục 3).
2. **Giọng AI tiếng Việt có thật, đo được, và khác nhau theo thể loại.**
   - Bài báo: *góp phần* dày gấp 10 lần văn người; *mà còn* 6,5 lần; *trong bối cảnh* 5 lần; *không chỉ*, *đồng thời*, *thay vì* 4–5 lần.
   - Bài blog: *hành trình*, *mà là*, *quan trọng nhất* dày gấp khoảng 21 lần; *thay vì* 16 lần; *điều quan trọng*, *chìa khóa* 15 lần; *bí quyết* 13 lần; *hãy* 12 lần. *Hành trình* có mặt trong 25 trên 60 bài blog.
3. **Nhiều "dấu hiệu AI" đang lưu hành là sai, ít nhất với mô hình 2026.**
   - Đo được ngang hoặc ít hơn văn người: *một cách*, *có thể*, *điều này*, *bởi* (AI dùng *bởi* ít hơn hẳn), *là một trong những*.
   - Gần như không xuất hiện: *bức tranh*, *hãy cùng khám phá*, *đa dạng và phong phú*, *thế giới đầy màu sắc*, *không thể phủ nhận*, *hơn nữa*, *thêm vào đó*.
   - Gạch dài (—) gần như đã biến mất: 0–3 lần trên 1.000 chữ.
4. **Dấu hiệu tụ ở kết bài, không ở mở bài.** Trong 120 bài báo và blog, đoạn cuối chứa:
   - *hành trình*: 18 bài;
   - *Hãy…*: 15 bài;
   - câu cảm thán: 14 bài;
   - *không chỉ… mà còn*: 12 bài;
   - *Tóm lại/Cuối cùng*: 11 bài.
   Mở bài theo khuôn chỉ có 4 bài.
5. **Claude, mô hình các agent của bạn đang dùng, có tật riêng:**
   - *hãy bắt đầu*, *đừng quên*, *kiên trì*;
   - mẫu *điều quan trọng không phải là X, mà là Y*;
   - tiêu đề và nút giao diện viết hoa mọi chữ (*Đăng Nhập Ngân Hàng Số*).
6. **Kho từ ngữ (mục 4) có 6 lớp, mỗi mục ghi căn cứ:**
   - cờ giọng AI theo thể loại (đo được);
   - mẫu cấu trúc;
   - danh sách "đừng sửa" (bị nghi oan);
   - văn dịch;
   - từ thừa;
   - 22 cặp từ hay viết sai, kiểm trên Từ điển Hoàng Phê 2003.
7. **Kho văn bản mẫu và công cụ (mục 5):**
   - Kho sạch AI chắc chắn: CC-100 (2018), Leipzig (2014–2021), viTenTen (2017–2018, trả phí).
   - FineWeb-2 có khoảng 28% thuộc 2023–2024.
   - **Không có công cụ tự động nào bắt được giọng văn hay ngữ pháp tiếng Việt.** LanguageTool không hỗ trợ tiếng Việt. Hunspell chỉ bắt âm tiết gõ sai.
8. **Quy tắc dùng (bạn chốt Q7, Q12):** coi cụm là cờ theo mật độ, không phải danh sách cấm. Viết lại khi một đoạn có ≥ 3 cờ, hoặc cả bài có ≥ 4 cờ trên mỗi 300 chữ. Ngưỡng này bắt oan 0,2–0,4% văn người trong phép thử.
9. **Đã chép vào skill (Q6):** `viet-chuyen-nghiep/review/tu-ngu.md` (mới); sửa `review/anti-ai.md`, `review/lead.md`, `SKILL.md`, `writing-foundation/hieu-chinh-quy.md`. Chưa commit.
10. **Vì sao dùng cờ thay cho danh sách cấm:** Russell 2025, Bouchard 2026, Wikipedia; và chính phép đo này (tật đổi theo mô hình, theo thể loại).

---

## 1. Objective, phạm vi, cách làm

- **Câu hỏi chủ:** agent cần kho từ ngữ và kho văn bản mẫu nào để viết tiếng Việt đúng và không lộ giọng AI; mỗi mục dựa trên căn cứ nào?
- **Bạn chốt đầu phiên (Q1–Q3):**
  - làm cả hai loại kho;
  - phủ 4 thể loại: báo cáo, tài liệu, slide; mạng xã hội, blog; văn bản gửi cơ quan, hợp đồng; giao diện phần mềm;
  - ghi vào báo cáo trước, chép sang skill sau.
- **Bạn cho phép (Q4–Q5):**
  - tải 2 kho Leipzig (49 MB, thư mục tạm);
  - dùng glm, codex, cursor, grok CLI để sinh mẫu văn AI.
- **Thời điểm cắt:** 05/10/2026, 01:00 (UTC+7).
- **Bộ câu hỏi** (skill essential-questions, mode ANALYZE + VERIFY):

| # | Câu hỏi | Loại | Ưu tiên | Ai trả lời |
|---|---|---|---|---|
| EQ1 | Văn AI tiếng Việt có dấu hiệu nào đã được ghi nhận, và dấu hiệu nào đo được? | RESEARCH | ★★★ | Agent A + phép đo |
| EQ2 | Câu dịch sát tiếng Anh có dạng nào, ai đã phê phán? | RESEARCH | ★★★ | Agent B |
| EQ3 | Từ nào hay viết sai, dùng sai nghĩa; từ điển nói gì? | FACT | ★★★ | Agent C + tôi tra lại HP2003 |
| EQ4 | Từ thừa, lặp nghĩa nào có nguồn? | FACT | ★★ | Agent B |
| EQ5 | Kho văn bản, từ điển mở nào dùng được, kho nào chưa lẫn văn AI? | FACT | ★★★ | Agent D |
| EQ6 | Ranh giới văn sáo và khuôn mẫu bắt buộc ở từng thể loại? | JUDGMENT | ★★ | Tổng hợp |
| EQ7 | Tell nằm ở từ hay cấu trúc; sửa quá tay có hại không? | JUDGMENT | ★★ | Agent A + phép đo |
| EQ8 | Có công cụ tự động kiểm tiếng Việt không? | FACT | ★ | Agent D |

- **Giả định đã kiểm:** "giọng AI tiếng Việt giống tiếng Anh". Kết quả: **sai một phần.** *Không chỉ… mà còn* thì khớp. Nhưng gạch dài và *delve*-kiểu (*bức tranh*, *khám phá*) không khớp.
- **Thẻ tin cậy:**
  - `[CONFIRMED]`: tôi tự mở nguồn gốc và có ít nhất một lần kiểm độc lập (agent khác hoặc bản thứ hai).
  - `[HIGH CONFIDENCE]`: một lần mở nguồn gốc; hoặc kết quả đo có p < 0,001 ở ≥ 4/5 họ mô hình.
  - `[ASSESSED]`: suy luận, tổng hợp, nguồn mâu thuẫn; hoặc kết quả đo yếu (p < 0,05, ít họ mô hình).
  - `[LOW CONFIDENCE]`: một nguồn yếu hoặc chỉ snippet.
  - `[BLIND SPOT]`: chưa kiểm được.

## 2. Từ điển (định nghĩa một lần)

| Từ | Nghĩa |
|---|---|
| **Giọng AI (AI slop)** | Văn đúng ngữ pháp nhưng sáo, chung chung, lặp khuôn, nhìn là biết máy viết. |
| **Cờ (flag)** | Cụm từ hay cấu trúc báo hiệu "nên xem lại", không phải lỗi chắc chắn. |
| **Mật độ** | Số lần xuất hiện trên một đơn vị độ dài (ở đây: trên 10.000 âm tiết hoặc 1.000 chữ). |
| **Tỷ lệ dư (ratio)** | Mật độ trong văn AI chia mật độ trong văn người cùng thể loại. 10 nghĩa là AI dùng dày gấp 10 lần. |
| **p (kiểm định Poisson)** | Xác suất thấy chênh lệch lớn như vậy nếu AI thật ra dùng cụm đó như người. p < 0,001: gần như chắc không do may rủi. |
| **Họ mô hình** | Nhóm mô hình cùng hãng: OpenAI (GPT), xAI (Grok), Zhipu (GLM), Google (Gemini), Anthropic (Claude). |
| **Văn dịch (translationese)** | Câu tiếng Việt giữ cấu trúc tiếng Anh: bị động thừa, giới từ dịch sát, số nhiều thừa. |
| **Corpus** | Kho văn bản lớn gom sẵn để nghiên cứu. |
| **HP2003** | Từ điển tiếng Việt, Hoàng Phê chủ biên, Viện Ngôn ngữ học, in lần thứ 9, 2003 (bản quét archive.org). |
| **id.** | Nhãn "ít dùng" trong từ điển Hoàng Phê. |

---

## 3. Phép đo: văn AI tiếng Việt khác văn người ở đâu

### 3.1 Cách đo (chi tiết ở nhật ký, mục B)

- **Văn người:** Leipzig Corpora (Đại học Leipzig), không chọn lọc, thu trước khi có ChatGPT (11/2022):
  - `vie_news_2019_100K`: 100.000 câu báo năm 2019, 2.413.124 âm tiết;
  - `vie-vn_web_2015_100K`: 100.000 câu web năm 2015, 2.504.470 âm tiết.
- **Văn AI:** 34 đề × 6 nguồn = 204 bài. Đề viết như người dùng bình thường, không kèm chỉ dẫn văn phong, nên kết quả đo **giọng mặc định** của mô hình.

| Nguồn | Mô hình | Họ |
|---|---|---|
| codex CLI | GPT-5.6 Sol | OpenAI |
| cursor CLI (mặc định) | GPT-5.6 Sol (trùng codex, tính chung một họ) | OpenAI |
| grok CLI | Grok 4.6 | xAI |
| glm CLI | GLM-4.6 | Zhipu |
| cursor `--model gemini-3.7-flash-high` | Gemini 3.7 Flash | Google |
| cursor `--model claude-sonnet-5-thinking-high` | Claude Sonnet 5 | Anthropic |

- **Hai lô đề:**
  - Lô 1, 14 đề: trải 4 thể loại bạn chọn. Dùng để xem từng thể loại.
  - Lô 2, 20 đề: 10 bài báo, 10 bài blog, **cùng thể loại với kho văn người**. Dùng cho phép so chính. Lý do: lô 1 so với báo và web chỉ ra từ đặc trưng thể loại (*kính gửi*, *đăng nhập*), không ra giọng AI.
- **So khớp:** bài báo AI so với báo 2019; bài blog AI so với web 2015.
- **Hai cách tìm cụm:**
  - Từ dưới lên: mọi cụm 2–4 âm tiết dày bất thường, có mặt ở ≥ 5 đề và ≥ 4 họ mô hình (theo cách của Kobak 2024).
  - Từ trên xuống: kiểm 59 cụm mà agent, báo chí, cộng đồng nêu.

### 3.2 Kết quả: cụm dày bất thường trong văn AI

Số liệu nguyên văn từ phép đo. "Bài có cụm" đếm trên 60 bài cùng thể loại. "Họ > 2×" đếm họ mô hình dùng cụm dày hơn 2 lần văn người.

**Bài báo** (AI 20.459 âm tiết; người 2.413.124):

| Cụm | AI | Người | Tỷ lệ dư | p | Bài có cụm | Họ > 2× | Tag |
|---|---|---|---|---|---|---|---|
| góp phần | 22 | 256 | 10,1 | 2,8e-15 | 18/60 | 4/5 (trừ Grok) | [HIGH CONFIDENCE] |
| mà còn | 17 | 309 | 6,5 | 3,1e-09 | 17/60 | chưa tách | [HIGH CONFIDENCE] |
| trong bối cảnh | 9 | 203 | 5,2 | 7,9e-05 | 8/60 | 3/5 (OpenAI dày nhất) | [ASSESSED] |
| không chỉ | 28 | 709 | 4,7 | 6,5e-11 | 26/60 | 5/5 | [HIGH CONFIDENCE] |
| thay vì | 8 | 226 | 4,2 | 8,4e-04 | 8/60 | 5/5 | [HIGH CONFIDENCE] |
| đồng thời | 25 | 734 | 4,0 | 1,2e-08 | 23/60 | 5/5 | [HIGH CONFIDENCE] |
| bên cạnh đó | 14 | 526 | 3,1 | 2,3e-04 | 14/60 | 3/5 | [ASSESSED] |
| đóng vai trò | 3 | 76 | 4,7 | 0,028 | 3/60 | 2/5 | [LOW CONFIDENCE] |

**Bài blog** (AI 19.816 âm tiết; người 2.504.470):

| Cụm | AI | Người | Tỷ lệ dư | p | Bài có cụm | Họ > 2× | Tag |
|---|---|---|---|---|---|---|---|
| mà là | 10 | 60 | 21,1 | 1,0e-10 | 10/60 | 4/5 | [HIGH CONFIDENCE] |
| quan trọng nhất | 20 | 120 | 21,1 | < 1e-15 | 18/60 | 5/5 | [HIGH CONFIDENCE] |
| hành trình | 35 | 215 | 20,6 | < 1e-15 | 25/60 | 4/5 (trừ Grok) | [HIGH CONFIDENCE] |
| thay vì | 26 | 204 | 16,1 | < 1e-15 | 22/60 | 5/5 | [HIGH CONFIDENCE] |
| chìa khóa | 5 | 40 | 15,8 | 2,0e-05 | 5/60 | 3/5 | [ASSESSED] |
| điều quan trọng | 10 | 84 | 15,0 | 2,5e-09 | 10/60 | 3/5 | [HIGH CONFIDENCE] |
| bí quyết | 13 | 125 | 13,1 | 5,6e-11 | 11/60 | 4/5 | [HIGH CONFIDENCE] |
| hãy | 132 | 1.431 | 11,7 | < 1e-15 | 47/60 | 5/5 | [HIGH CONFIDENCE] |
| dưới đây là | 7 | 104 | 8,5 | 2,5e-05 | 7/60 | 4/5 | [HIGH CONFIDENCE] |
| không chỉ | 11 | 631 | 2,2 | 0,014 | 11/60 | 3/5 | [ASSESSED] |
| việc | 107 | 8.515 | 1,6 | 5,2e-06 | 38/60 | 1/5 | [ASSESSED] (dư nhẹ) |

**Từ dưới lên (lô 2, ≥ 5 đề, ≥ 4 họ)**, ngoài các cụm trên:
- *hãy bắt đầu* (16 lần, 7 đề, 5 họ, dư 85 lần);
- *là một hành trình* (9 lần, 6 đề, dư 220 lần);
- *cũng góp phần* (dư 41 lần);
- *mà còn tạo* (dư 51 lần);
- *sự kiên nhẫn*, *kiên trì*, *đều đặn*;
- *bạn không cần* (dư 31 lần);
- *rõ rệt*, *lâu dài*.

Đã loại vì là nhiễu đề bài: *giờ cao điểm* (đề giao thông), *người mới bắt đầu* (có sẵn trong đề).

**Đọc bảng thế nào:**
- Cùng một từ có thể là cờ ở thể loại này mà không phải ở thể loại khác.
- *hãy* không xuất hiện lần nào trong 60 bài báo AI, nhưng có mặt ở 47/60 bài blog.
- *góp phần* dư 10 lần trong bài báo, nhưng bình thường trong blog.

### 3.3 Bị nghi oan: đừng sửa các từ này chỉ vì "nghe như AI"

| Cụm | Báo: AI / dự kiến | Blog: AI / dự kiến | Kết luận | Tag |
|---|---|---|---|---|
| một cách | 1 / 3,5 | 4 / 5,6 | Không dư | [HIGH CONFIDENCE] |
| có thể | 17 / 37,2 (ít hơn, p = 1,7e-04) | 71 / 51,4 (dư nhẹ, p = 0,005) | Không phải cờ | [HIGH CONFIDENCE] |
| bởi | 2 / 12,2 (ít hơn, p = 4,3e-04) | 3 / 11,8 (ít hơn, p = 0,003) | AI dùng *bởi* **ít** hơn người | [HIGH CONFIDENCE] |
| điều này | 2 / 5,3 | 4 / 5,9 | Không dư | [HIGH CONFIDENCE] |
| là một trong những | 4 / 4,1 | 7 / 3,4 | Không dư rõ (Claude hay mở bài bằng cụm này, xem 3.6) | [ASSESSED] |
| việc | 73 / 64,6 | 107 / 67,4 | Báo: không dư. Blog: dư nhẹ 1,6 lần | [ASSESSED] |
| bức tranh, hãy cùng, đa dạng và phong phú, đầy màu sắc, không thể phủ nhận, trong thế giới, hơn nữa, thêm vào đó, tưởng chừng, không đơn thuần, tạo giá trị, then chốt, tâm hồn, vượt trội, trong bài viết này | 0 lần trong cả 120 bài lô 2 | | Không xuất hiện ở mô hình 2026. Có thể từng đúng với ChatGPT 2023–2024 (chưa kiểm) | [ASSESSED] |

**Hình dung cụ thể:** agent sửa *"Hệ thống được vận hành bởi đội kỹ thuật"* thành *"Đội kỹ thuật vận hành hệ thống"*. Câu sau gọn hơn, nên nên sửa vì lý do văn dịch (mục 4.4). Nhưng nếu agent sửa vì nghĩ đó là "dấu hiệu AI" thì sai lý do: phép đo cho thấy AI dùng *bởi* ít hơn người.

### 3.4 Cấu trúc

| Chỉ số | Văn người | OpenAI | Grok | GLM | Gemini | Claude | Tag |
|---|---|---|---|---|---|---|---|
| Độ dài câu trung bình (âm tiết, lô 2) | 24,6 | 23,8 | 15,6 | 21,1 | 24,2 | 26,7 | [HIGH CONFIDENCE] |
| Độ biến thiên độ dài câu (CV, lô 2) | 0,45 | 0,40 | 0,48 | 0,47 | 0,47 | 0,48 | [ASSESSED] |
| Gạch dài (—) trên 1.000 chữ, lô 2 / lô 1 | 0,00 | 0,00 / 1,40 | 0,31 / 3,18 | 0,31 / 0,33 | 0,00 / 0,16 | 0,00 / 0,78 | [HIGH CONFIDENCE] |
| Dấu phẩy trước "và" trên 1.000 chữ, lô 2 | 0,31 | 0,52 | 2,66 | 1,22 | 0,15 | 1,15 | [HIGH CONFIDENCE] |
| Dấu `**` (in đậm) trên 1.000 chữ, lô 1 | 0 | 8,2 | 11,8 | 10,9 | 44,2 | 6,3 | [HIGH CONFIDENCE] |
| Tiêu đề viết hoa mọi chữ (số tiêu đề), lô 1 | | 4/47 | 2/36 | 7/25 | 21/87 | 4/17 | [HIGH CONFIDENCE] |

**Hệ quả:**
- **Gạch dài không còn là dấu hiệu đáng tin.** Mô hình 2026 hầu như không dùng nó trong tiếng Việt, khớp tin OpenAI sửa ChatGPT tháng 11/2025 (A12). Quy ước "không dùng gạch dài" của bạn vẫn giữ được, nhưng lý do là văn phong, không phải chống AI.
- **"Câu đều nhịp" chưa có bằng chứng.** CV của AI xấp xỉ văn người. Cách đo này thô: câu người lấy ngẫu nhiên, không theo bài. Chưa đủ để kết luận.
- **Dấu phẩy trước "và"** là tật của Grok, GLM, Claude. Microsoft cũng khuyên bỏ (D02 của packet 03/10).
- **In đậm và tiêu đề Title Case** là tật lớn nhất ở thể loại báo cáo, tài liệu (lô 1), nhất là Gemini.

### 3.5 Mở bài và kết bài (lô 2, 120 bài có ≥ 2 đoạn)

| Mẫu | Đoạn đầu | Đoạn cuối | Họ mô hình (đoạn cuối) |
|---|---|---|---|
| *… hành trình …* | 1 | **18** | OpenAI 7, GLM 5, Gemini 3, Claude 3 |
| *Hãy …* (kêu gọi) | | **15** | GLM 5, Gemini 4, OpenAI 3, Claude 3 |
| Kết bằng câu cảm thán `!` | | **14** | GLM 7, Gemini 3, Claude 3, OpenAI 1 |
| *không chỉ … mà còn* | | **12** | Gemini 5, OpenAI 3, Claude 2, GLM 2 |
| *Tóm lại / Nhìn chung / Kết luận / Cuối cùng* | | **11** | OpenAI 7, Claude 3, Gemini 1 |
| *Chúc bạn …* | | 3 | GLM 2, Claude 1 |
| Câu hỏi tu từ | 2 | | |
| *X là một trong những / là một cột mốc* | 2 | | |

- Grok không rơi vào mẫu kết bài nào.
- **Chưa có mốc văn người cho kết bài**, vì kho Leipzig là câu rời, không còn bài (điểm mù 8.3). Tag `[ASSESSED]`.

**Hình dung:** một bài blog GPT về chạy bộ kết bằng *"Chạy bộ không chỉ giúp bạn khỏe hơn mà còn là hành trình khám phá bản thân. Hãy bắt đầu ngay hôm nay!"*. Câu này gom 4 cờ trong 2 câu. Không cụm nào sai ngữ pháp, nhưng cả bốn cùng lúc là chữ ký của máy.

### 3.6 Tật riêng của Claude (lô 2, 20 bài, 6.970 âm tiết)

| Tật | Bằng chứng | Tag |
|---|---|---|
| *hãy bắt đầu* | 4 lần, 4 đề, dư 123 lần | [ASSESSED] (mẫu nhỏ) |
| *đừng quên* | 4 lần, 4 đề, dư 50 lần | [ASSESSED] |
| *kiên trì* | 6 lần, 6 đề, dư 38 lần | [ASSESSED] |
| *điều quan trọng không phải là X, mà là Y* | 3/20 bài Claude (GPT 1, Gemini 1). Ví dụ: "điều quan trọng không phải là đọc nhiều, mà là đọc đều" | [ASSESSED] |
| *góp phần* trong bài báo | 28,06 trên 10.000 âm tiết, gấp 26 lần báo 2019 | [ASSESSED] |
| Title Case ở giao diện | "Đăng Nhập Ngân Hàng Số", "Nút: Đăng Nhập" (lô 1, đề 10). Trái Microsoft tr. 24 (packet 03/10, mục 4.2) | [HIGH CONFIDENCE] |
| Title Case ở tiêu đề bài | "Bắt Đầu Chạy Bộ: Những Bước Đi Đầu Tiên" | [HIGH CONFIDENCE] |

Lưu ý: mẫu đo bằng Claude Sonnet 5 qua cursor. Agent của bạn có thể chạy Opus hoặc Fable, nên tật có thể khác (điểm mù 8.4).

---

## 4. Kho từ ngữ

Cách dùng: đọc mục 7 trước. Cột "Cách sửa" là **đề xuất của tôi**, trừ chỗ ghi nguồn.

### 4.1 Cờ giọng AI theo thể loại (từ phép đo)

| Thể loại | Cờ mạnh (p < 0,001, ≥ 4 họ) | Cờ vừa | Cách sửa |
|---|---|---|---|
| Báo cáo, bài phân tích, tin | *góp phần*, *không chỉ… mà còn*, *đồng thời*, *thay vì* | *trong bối cảnh*, *bên cạnh đó*, *đóng vai trò* | Nói kết quả đo được: thay *"góp phần nâng cao hiệu quả"* bằng *"giảm thời gian xử lý từ 5 xuống 2 ngày"*. Tách *không chỉ A mà còn B* thành hai ý ngang hàng nối bằng *và*, hoặc chỉ giữ ý chính. Mở đầu bằng sự kiện, ngày, con số, bỏ *"Trong bối cảnh…"* (A01 cũng khuyên vậy) |
| Blog, mạng xã hội, hướng dẫn | *hành trình*, *mà là*, *quan trọng nhất*, *thay vì*, *điều quan trọng*, *bí quyết*, *hãy*, *dưới đây là* | *chìa khóa*, *kiên trì*, *bạn không cần* | Gọi đúng tên việc: *"tập chạy 3 tuần"*, không *"hành trình chạy bộ"*. Nói thẳng điều khẳng định, bỏ vế phủ định tự dựng. Giữ tối đa 1–2 câu *hãy* mỗi bài, đặt ở bước làm cụ thể. Bỏ *"Dưới đây là…"*, vào thẳng ý (A05) |
| Mọi thể loại, đoạn kết | Đoạn cuối có ≥ 2 trong: *hành trình*, *hãy*, `!`, *không chỉ… mà còn*, *tóm lại/cuối cùng* | | Kết bằng thông tin cuối cùng hoặc việc cần làm tiếp; không tóm lại, không kêu gọi chung chung |
| Giao diện | Title Case trên nút, tiêu đề | *Vui lòng* lặp ở mọi thông báo lỗi (4/4 lỗi ở GLM, Gemini, Grok) | *Đăng nhập*, không *Đăng Nhập*. Với *vui lòng*: chưa có nguồn quy định, ghi nhận là thói quen, không sửa cứng |
| Công văn, hợp đồng | Không đo được giọng AI riêng | | Xem 4.8: khuôn mẫu bắt buộc không phải giọng AI |

### 4.2 Mẫu cấu trúc

| Mẫu | Căn cứ | Mức | Cách sửa |
|---|---|---|---|
| Phủ định dựng sẵn rồi khẳng định: *không phải X, mà là Y*; *điều quan trọng không phải là…* | Đo: *mà là* dư 21 lần ở blog; Claude 3/20 bài. Nguồn: A10 (Đỗ Tho 2026), A14; tiếng Anh: Pangram qua The Atlantic (A45, snippet) | [HIGH CONFIDENCE] | Chỉ nói Y. Giữ X khi người đọc thật sự đang tin X |
| *không chỉ… mà còn* lặp | Đo: 26/60 bài báo AI. Nguồn: BrandsVietnam (A02), A10, A16 | [CONFIRMED] | Mỗi bài tối đa 1 lần, khi hai vế thật sự chênh nhau |
| In đậm nhãn đầu dòng, tiêu đề phần trong văn kể | Đo: in đậm 6–44 trên 1.000 chữ (văn người 0). Skill `anti-ai.md` đã có | [HIGH CONFIDENCE] | Văn xuôi; in đậm chỉ cho cảnh báo |
| Tiêu đề Title Case | Đo: 4/5 họ. Microsoft tr. 24, Mozilla (packet 03/10, V06) | [CONFIRMED] | Viết hoa kiểu câu |
| Dấu phẩy trước *và* | Đo: Grok gấp 8,6 lần, Claude 3,7 lần. Microsoft (D02, packet 03/10) | [HIGH CONFIDENCE] | Bỏ dấu phẩy |
| Bịa ví dụ, nguồn, chiến dịch | BrandsVietnam (A06): "phần lớn ví dụ đều do chatbot này bịa ra" | [HIGH CONFIDENCE] | Mọi ví dụ phải có nguồn mở được, không có thì bỏ |
| Sót lời dẫn của mô hình (*Dưới đây là phiên bản…*) | A06; đo *dưới đây là* dư 8,5 lần ở blog | [HIGH CONFIDENCE] | Soát trước khi gửi |
| Câu đều nhịp | Finhay (A15), repo (A16); đo CV không khác văn người | [LOW CONFIDENCE] | Không dùng làm tiêu chí |
| Gạch dài (—) nối mệnh đề | BrandsVietnam (A04); đo 0–3 trên 1.000 chữ ở mô hình 2026 | [ASSESSED]: đã hết hạn | Giữ quy ước nội bộ, không coi là dấu hiệu AI |

### 4.3 Danh sách "đừng sửa"

Agent **không** được sửa các từ sau chỉ với lý do "nghe như AI". Có thể sửa vì lý do khác (gọn hơn, rõ hơn) khi nêu được lý do đó.

- *một cách*, *có thể*, *điều này*, *bởi*, *việc* (trong văn báo cáo), *là một trong những*, *tuy nhiên*, *ngoài ra*, *sự*: phép đo cho thấy không dư (3.3).
- *được* bị động: 65,8% câu bị động tiếng Anh vẫn được dịch thành bị động tiếng Việt trong khảo sát 649 câu (T11, Hoàng Công Bình 2015). Microsoft giữ *"sẽ được gửi cho Microsoft"* làm ví dụ đúng (T06).
- *chia xẻ* (chia thành nhiều phần): từ khác, không phải lỗi của *chia sẻ* (W08).
- *trau giồi*: HP2003 ghi "cũ; id.", là dạng cũ, không phải lỗi chính tả (W12).
- *nghe phong phanh*: HP2003 ghi khẩu ngữ "Như phong thanh" (H05).
- *cây đại thụ*, *người nông dân*, *đường quốc lộ*: thừa về gốc, nhưng Nguyễn Đức Dân ghi "nay đã thành đúng" (T19).

**Vì sao danh sách này quan trọng:** Russell 2025 thấy người ít kinh nghiệm hay gán nhầm từ "sang" và giọng trung tính là AI (A40). Agent sửa quá tay sẽ đẩy văn sang lộn xộn có chủ đích, tức tạo ra dấu hiệu AI mới (`hieu-chinh-quy.md` của skill writing-foundation cũng cảnh báo điều này).

### 4.4 Văn dịch (có nguồn)

| Dạng | Sai | Sửa | Nguồn | Mức |
|---|---|---|---|---|
| Danh từ hóa "thất bại" | *Lưu hình ảnh thất bại.* | *Không lưu được hình ảnh.* | Microsoft 2.1.3 (T01) | [CONFIRMED] |
| "không thành công" | *Tải về không thành công* | *Không tải được* | Microsoft 2.1.4 (T04) | [HIGH CONFIDENCE] |
| Mệnh đề *mà … sẽ thực hiện* | *Xác định hành động mà máy chủ sẽ thực hiện khi gặp các loại lỗi* | *Chỉ rõ thao tác cho máy chủ khi gặp các dạng lỗi* | Microsoft (T05) | [HIGH CONFIDENCE] |
| Chủ ngữ giả "It is" | *Nó khó để làm…* | *Khó làm…* | Microsoft (T07) | [HIGH CONFIDENCE] |
| Số nhiều thừa | *Các thiết lập*, *Những thiết lập* (cho "Settings") | *Thiết lập* | Mozilla (T09), Microsoft (T02) | [CONFIRMED] |
| Bị động tiếng Anh | *Danh hiệu quý tộc không được ban tặng bởi Hợp chủng quốc* (câu mẫu do agent dựng) | *Hợp chủng quốc không ban tặng bất cứ danh hiệu quý tộc nào* (bản dịch trong khảo sát) | Mozilla: "Cố gắng chuyển câu bị động tiếng Anh thành câu chủ động tiếng Việt"; Nguyễn Quốc Hùng 2007 qua Wikipedia (T10); T11 | [CONFIRMED] là khuyến nghị; **không cấm** *được* |
| Dịch sát "Feel free to" | *Cứ thoải mái trả lời email này…* | *Vui lòng trả lời email này nếu bạn có bất kỳ thắc mắc nào khác.* | Microsoft (T02) | [HIGH CONFIDENCE] |
| Trạng ngữ nuốt chủ ngữ | *Theo khảo sát mới đây của các nhà nghiên cứu, cho thấy…* | *Khảo sát … cho thấy…* (bản sửa của tôi) | Nguyễn Đức Dân dẫn Nguyễn Kim Thản 1975 (T17) | [HIGH CONFIDENCE] |
| Chuỗi Hán Việt dài | *phương tiện tham gia giao thông* | *phương tiện đi lại* | Nguyễn Đức Dân (T18) | [CONFIRMED] |
| Câu dài theo thứ tự gốc | (khái quát) | Cắt câu dài, chuyển mệnh đề quan hệ dài lên trước | Wikipedia vi, Cẩm nang dịch thuật (T10) | [ASSESSED] |

**Chưa có nguồn có tên**, không đưa vào luật: *một cách + tính từ*, lạm dụng *việc/sự*, *nó* chỉ vật, *đóng vai trò*, *có thể* thừa, *Có một…*, *Điều này*, *của* thừa, *với/cho* dịch "with/for" (T, mục 2 báo cáo nhóm B). Phép đo ở 3.3 còn cho thấy *một cách*, *có thể*, *điều này* không dư trong văn AI.

### 4.5 Từ thừa, lặp nghĩa (có nguồn)

| Thừa | Gọn | Nguồn | Mức |
|---|---|---|---|
| tái sinh lại, tái hiện lại, tái diễn lại, tái bản lại, tái tạo lại | bỏ *lại* | Hồ Anh Thái, Tiền Phong 22/06/2014 (T21); Đỗ Văn Học 2015 (T28) | [CONFIRMED] |
| hồi phục lại, phục chế lại | hồi phục, phục chế | Hồ Anh Thái (T21) | [HIGH CONFIDENCE] |
| tối ưu nhất, tối đa nhất, hoàn toàn rất | tối ưu, tối đa | Hồ Anh Thái (T22); Đỗ Văn Học (T28) | [HIGH CONFIDENCE] |
| các quý vị, những quý vị | quý vị, các vị | Đặng Minh Phương, Nhân Dân 19/06/2011 (T25); Lê Hữu (T26); tgpsaigon.net dẫn Từ điển 2005 (T27) | [HIGH CONFIDENCE] (3 nguồn, cả ba không phải học thuật) |
| nhiều những, rất nhiều những | nhiều | Lê Hữu (T26) | [LOW CONFIDENCE] |
| hoàn thành xong, căn cứ theo, đáp ứng theo, cấm không được, đại quy mô lớn, đề xuất kiến nghị, nhu cầu đòi hỏi, chưa vị thành niên, xét theo đề nghị | hoàn thành, căn cứ, đáp ứng, cấm, quy mô lớn, đề xuất, nhu cầu, vị thành niên, xét đề nghị | Đỗ Văn Học, Tạp chí Phát triển KH&CN, ĐHQG-HCM, 2015 (T28) | [CONFIRMED] (tôi mở lại bản gốc) |
| Nhưng tuy nhiên, Nhưng mặc dù vậy, Ở bên trong nội tâm | Nhưng / Tuy nhiên; Trong nội tâm | Hồ Anh Thái (T24) | [CONFIRMED] |
| đặc thù riêng, đặc trưng riêng | đặc thù, đặc trưng | Hồ Anh Thái (T22) | [HIGH CONFIDENCE] |
| bước tiến bộ | tiến bộ / bước tiến | Đặng Minh Phương (T25) | [HIGH CONFIDENCE] |
| trên địa bàn Hà Nội | Hà Nội | Đặng Minh Phương (T25) | [HIGH CONFIDENCE] |
| cô gái trẻ, chàng trai trẻ | cô gái, chàng trai | Hồ Anh Thái (T23) | [LOW CONFIDENCE] (một nhà văn) |
| người họa sĩ, nhà triết gia, nhà doanh nhân | họa sĩ, triết gia, doanh nhân | Hồ Anh Thái (T23); chính tác giả nói "có ngày được vào từ điển" | [ASSESSED] (tranh cãi) |

### 4.6 Cặp từ hay viết sai hoặc dùng sai nghĩa

Căn cứ chính: HP2003. Tôi tự tra lại các mục đánh dấu ✔ trên bản OCR.

| Đúng | Sai hoặc lẫn | Nghĩa (HP2003) | Căn cứ thêm | Tag |
|---|---|---|---|---|
| sáp nhập | sát nhập | "Nhập vào với nhau làm một". HP2003 có mục "sát nhập x. sáp nhập" ✔, tức ghi nhận như dạng trỏ về *sáp nhập* | TTXVN chốt "sáp nhập" | [CONFIRMED]; câu "sát nhập không có trong từ điển" là **sai** với HP2003 |
| bàng quan (thờ ơ) | bàng quang (bọng đái) | Hai từ khác nghĩa | | [HIGH CONFIDENCE] |
| xán lạn | sáng lạn, sán lạn | "Rực rỡ, huy hoàng" | Hoàng Tuấn Công 2023; Vietlex 2016 qua trích dẫn | [ASSESSED] (từ điển chính tả Nguyễn Văn Khang ghi *sán lạn*, chưa mở sách) |
| chẩn đoán | chuẩn đoán | ✔ "Xác định bệnh, dựa theo triệu chứng…" | | [HIGH CONFIDENCE] |
| tham quan | thăm quan | Chỉ có *tham quan* | Hoàng Tuấn Công 10/2023 | [HIGH CONFIDENCE]. Đừng giải thích bằng "thuần Việt không ghép với Hán Việt": lý lẽ này đã bị chính Hoàng Tuấn Công bác |
| điểm yếu, nhược điểm | yếu điểm (khi muốn nói điểm yếu) | ✔ yếu điểm "(id.) Điểm quan trọng nhất" | An Chi, Thanh Niên 07/10/2018 ✔ | [CONFIRMED] |
| giành (tranh lấy) / dành (để riêng) | lẫn hai từ | *giành thị trường, giành giải*; *dành tiền, dành cho ai* | TTXVN | [HIGH CONFIDENCE] |
| chia sẻ | chia sẽ | "Cùng chia với nhau để cùng hưởng hoặc cùng chịu" | *chia xẻ* là từ khác (chia thành phần) | [HIGH CONFIDENCE] |
| sơ suất | sơ xuất | | | [HIGH CONFIDENCE] (chỉ HP2003) |
| xác suất | xác xuất | | | [HIGH CONFIDENCE] (chỉ HP2003) |
| kiểm soát | kiểm xoát | | | [HIGH CONFIDENCE] (chỉ HP2003) |
| trau dồi | (trau giồi: dạng cũ) | ✔ "trau giồi (cũ; id.)" | | [CONFIRMED] |
| chỉn chu | chỉnh chu | ✔ "Chu đáo, cẩn thận" | Wiktionary ghi "chỉnh chu (từ sai chính tả)" | [CONFIRMED] |
| dè bỉu | dè biểu | | | [LOW CONFIDENCE] (OCR dấu không chắc) |
| vô hình trung | vô hình chung | ✔ "Tuy không có chủ định…" | Kênh14, Thiếu niên Tiền phong | [CONFIRMED] |
| độc giả | đọc giả | | Kênh14 dẫn HP 2000 tr. 336 | [HIGH CONFIDENCE] |
| cọ xát | cọ sát | | | [HIGH CONFIDENCE] (chỉ HP2003) |
| chấp bút | chắp bút | "Viết thành văn bản theo ý kiến đã thống nhất của tập thể" | TS Lê Thị Bích Hồng, Tuổi Trẻ 09/11/2016 | [CONFIRMED] |
| chín muồi | chín mùi | | Kênh14 dẫn HP 2000 và Nguyễn Kim Thản 2005 | [HIGH CONFIDENCE] |
| tựu trung | tựu chung | | | [HIGH CONFIDENCE] |
| nhậm chức | nhận chức | | | [HIGH CONFIDENCE] (chỉ HP2003) |
| giả thiết ≠ giả thuyết | coi là một | Giả thiết: điều cho trước; giả thuyết: điều nêu ra để giải thích, chưa kiểm chứng | | [HIGH CONFIDENCE] |
| cứu cánh = mục đích cuối cùng | dùng như *cứu tinh* | ✔ "Mục đích cuối cùng. Nghệ thuật là phương tiện, không phải là cứu cánh" | TTXVN dẫn Đào Duy Anh | [CONFIRMED] |
| vị tha = vì người khác | hiểu là *tha thứ* (nên dùng *bao dung*) | "Có tinh thần chăm lo một cách vô tư đến lợi ích của người khác" | TTXVN | [HIGH CONFIDENCE] |

### 4.7 Chọn theo ngữ cảnh (chuyên gia, từ điển bất đồng)

| Cặp | Phía A | Phía B | Đề xuất cho agent |
|---|---|---|---|
| khuyến mại / khuyến mãi | Luật Thương mại 2005, Điều 88: "Khuyến mại là hoạt động xúc tiến thương mại…" ✔ (bản VCCI) | HP2003 chỉ có "khuyến mãi đg. Khuyến khích việc mua hàng" ✔; Tuổi Trẻ 2022 và VnExpress 2026 gán nghĩa ngược nhau | *khuyến mại* mọi nơi (bạn chốt Q8). Trích nguyên văn thì giữ như nguồn |
| phong thanh / phong phanh | Bài báo gọi *phong phanh* là dùng nhầm | HP2003 ghi khẩu ngữ | Văn trang trọng: *phong thanh* |
| yếu điểm | Nghĩa gốc: điểm quan trọng (An Chi, HP2003) | Dùng như *điểm yếu* rất phổ biến; Bùi Đức Tịnh: nghĩa phổ biến lâu dần được công nhận | Viết *điểm yếu, nhược điểm* |
| khả năng | HP2003 nghĩa 1: "Cái có thể xuất hiện, có thể xảy ra…" (vd *bão có khả năng đổ bộ*) | Tuổi Trẻ 2016 phê dùng sai nghĩa gốc (không rõ trường hợp) | Đừng sửa *có khả năng* thành *có thể* chỉ vì lý do này |

### 4.8 Theo thể loại: chỗ khuôn mẫu là đúng, không phải giọng AI

| Thể loại | Khuôn mẫu bắt buộc hoặc chuẩn | Không coi là giọng AI | Căn cứ |
|---|---|---|---|
| Văn bản gửi cơ quan | Quốc hiệu, tiêu ngữ, *Kính gửi*, *Căn cứ…*, *Trân trọng*, *Nơi nhận* | Phép đo lô 1 thấy *kính gửi* dư 401 lần so với báo, nhưng đó là đặc trưng thể loại | NĐ 30/2020 (packet 03/10, L08) |
| Hợp đồng | *Điều 1…*, *Bên A/Bên B*, câu điều kiện dài, lặp định nghĩa | Lặp từ có chủ đích để tránh hiểu nhầm | Mẫu hợp đồng TT 02/2023/TT-BXD (R39). Đỗ Văn Học (T29): văn bản nhà nước "tuyệt đối tránh việc dùng thừa từ", tức vẫn áp 4.5 |
| Giao diện | Câu ngắn, viết hoa kiểu câu, *Không … được* cho lỗi | *Vui lòng* (chưa có căn cứ để sửa) | Microsoft (T01, T04), Mozilla (T09) |
| Báo cáo, slide | Tiêu đề nêu kết luận, số có đơn vị và ngày | Bảng, gạch đầu dòng khi là danh sách thật | packet 03/10 mục 6; skill `data-report-writer` |
| Blog, mạng xã hội | Ngôi thứ nhất, giọng riêng (hồ sơ `voice-profile`) | Viết tắt, tiếng lóng theo đối tượng (ViLexNorm) | writing-foundation; R30 |

---

## 5. Kho văn bản mẫu, từ điển, công cụ

### 5.1 Kho văn bản để đối chiếu giọng người

| Kho | Năm thu | Sạch văn AI? | Giấy phép | Truy cập | Tag |
|---|---|---|---|---|---|
| Leipzig Corpora vie (news 2019/2020, web 2015, mixed 2014, wikipedia 2016/2021) | 2014–2021 | Có | Chưa đọc được (site chặn bot) | Tải trực tiếp `downloads.wortschatz-leipzig.de/corpora/` (tôi đã tải 2 gói 100K) | [CONFIRMED] |
| CC-100 vi | 2018 | Có | Không tuyên bố quyền cho phần chuẩn bị | `data.statmt.org/cc-100/`, ~29,5 GB nén | [HIGH CONFIDENCE] |
| viTenTen (Sketch Engine) | 05/2017–01/2018 | Có | Trả phí | Tra trên web | [HIGH CONFIDENCE] |
| OSCAR 23.01 vi | CC 11–12/2022 | Sát ngưỡng | Metadata CC0 | Khai form trên HF | [HIGH CONFIDENCE] |
| FineWeb-2 vie | 2013–04/2024 | **Lẫn**: ~28% mẫu thuộc 2023–2024 (agent lấy 29 khối, ±8 điểm) | ODC-By | HF, lọc theo trường `date` | [ASSESSED] |
| binhvq news-corpus | 2018–2021 | Có | Không có cho dữ liệu | **Ngừng phân phối từ 08/2026** | [HIGH CONFIDENCE] |
| Wikipedia vi dump | đến 10/2026 | Có thể lẫn | CC BY-SA 4.0 | Dump trước 11/2022 không còn trên dumps.wikimedia.org | [HIGH CONFIDENCE] |

**Đo mức nhiễm AI của web tiếng Việt:** chưa ai đo. Pew 08/2026 chỉ đo tiếng Anh; Thompson 2024 đo dịch máy đa ngôn ngữ nhưng không tách tiếng Việt (R15–R17). `[BLIND SPOT]`.

### 5.2 Văn bản mẫu theo thể loại (đọc giọng chuẩn)

| Thể loại | Nguồn | Ghi chú |
|---|---|---|
| Hành chính | NĐ 30/2020, Phụ lục III | Mẫu thể thức |
| Hợp đồng | TT 02/2023/TT-BXD (mẫu hợp đồng xây dựng); mẫu kèm NĐ 145/2020 (lao động) | Hiệu lực 2026 chưa kiểm |
| Báo cáo số liệu | Cục Thống kê, Báo cáo kinh tế - xã hội quý III và 9 tháng 2026 (đăng 03/10/2026) | Giọng hành chính hiện hành |
| Báo cáo phân tích | VEPR, Báo cáo Thường niên Kinh tế Việt Nam | Viết gốc tiếng Việt (snippet) |
| Báo cáo phân tích (cẩn thận) | World Bank, *Điểm lại* bản tiếng Việt | Có thể là bản dịch, đọc để nhận diện văn dịch |
| Giao diện | Microsoft Terminology (TBX ~176 MB), Mozilla Pontoon `vi.tbx` (109 KB), applelocalization.com (không chính thức) | Ba hãng dịch khác nhau, cần chọn một (Q10) |
| Sổ tay tòa soạn | **Không có** bản công khai của Tuổi Trẻ, VnExpress (R37) | |

### 5.3 Từ điển

| Từ điển | Dùng cho | Giấy phép | Tag |
|---|---|---|---|
| HP2003 (archive.org, 2 bản quét) | Căn cứ chính cho 4.6. OCR lỗi dấu hỏi/ngã | Còn bản quyền, chỉ tra cứu | [CONFIRMED] |
| Wiktionary vi | Tra nhanh, nhiều mục từ Hồ Ngọc Đức | CC BY-SA | [HIGH CONFIDENCE] |
| Hồ Ngọc Đức (FVDP) | Danh sách từ; trang gốc đã 404, có bản lưu 04/2026 | GPL | [HIGH CONFIDENCE] |
| hvdic.thivien.net | Nghĩa gốc Hán Việt (cứu cánh, yếu điểm…) | Không thấy | [HIGH CONFIDENCE] |
| vdict, vtudien, rung.vn, tratu.soha.vn | **Không dùng làm căn cứ**: không ghi nguồn, rung.vn nghi sinh tự động, soha lỗi SSL | | [HIGH CONFIDENCE] |

### 5.4 Công cụ tự động

| Công cụ | Làm được | Không làm được | Tag |
|---|---|---|---|
| LanguageTool | | **Không hỗ trợ tiếng Việt** (API trả "'vi' is not a language code known") | [CONFIRMED] |
| hunspell-vi (6.641 âm tiết) | Bắt âm tiết gõ sai: *nghành*, *chĩ*, *qui* | Bỏ lọt *xử dụng*, *dành được*; báo oan *hóa* (bản DauMoi ưa *hoá*, cần dùng bản `vi-DauCu`) | [HIGH CONFIDENCE] |
| underthesea | Chuẩn hóa văn bản, khôi phục dấu | Không có kiểm chính tả, ngữ pháp | [HIGH CONFIDENCE] |
| VietAIDetector (MIT) | Đoán văn có phải AI viết | Chưa chạy thử | [LOW CONFIDENCE] |
| Phép đo trong packet này (script ở nhật ký, mục B) | Đo lại tật AI theo quý, theo mô hình mới | Cần chạy tay | [HIGH CONFIDENCE] |

---

## 6. Bảng claim đã kiểm

Claim chi tiết của agent: A01–A45 (nhóm A), T01–T31 (nhóm B), W01–W22 và H01–H06 (nhóm C), R01–R40 (nhóm D) ở 4 báo cáo `researcher-261004-2340-*`. Bảng dưới là claim trọng yếu dùng trong packet.

| ID | Claim | Tag | Nguyên văn / số | URL | primary_origin | source_type |
|---|---|---|---|---|---|---|
| X01 | Chưa có nghiên cứu đếm cụm AI trong tiếng Việt | [HIGH CONFIDENCE] | 52 query Việt + Anh không ra (A, mục 6) | | | bằng chứng phủ định |
| X02 | ViDetect, VietBinoculars không nêu cụm làm lộ | [HIGH CONFIDENCE] | ViDetect xóa dấu câu, stop word trước khi học (A28); accuracy 0,8580 | arxiv.org/abs/2405.03206; arxiv.org/abs/2509.26189 | UIT; TH Nguyen | preprint |
| X03 | Kobak: từ dư ở PubMed | [CONFIRMED] | "delves (r=28.0), underscores (r=13.8), and showcasing (r=10.7)"; "at least 13.5% of 2024 abstracts"; 454 từ năm 2024 | pmc.ncbi.nlm.nih.gov/articles/PMC12219543/ | Kobak et al., Sci. Adv. 2025 | tạp chí, tiếng Anh |
| X04 | Người dùng LLM nhiều nhận ra văn AI tốt | [HIGH CONFIDENCE] | TPR 92,7%, FPR 3,3% (5 người, 300 bài tiếng Anh) | arxiv.org/abs/2501.15654 | Russell, Karpinska, Iyyer | preprint |
| X05 | BrandsVietnam: *Trong bối cảnh… phát triển không ngừng*, *không chỉ… mà còn*; phương pháp 1 prompt, 1 chủ đề | [CONFIRMED] | "“Trong bối cảnh ngành [XYZ] đang phát triển không ngừng…”"; "bài blog khoảng 2.000 chữ về chủ đề Ambient Advertising" | help.brandsvietnam.com (A01) | Brands Vietnam | blog cộng đồng |
| M01 | Bài báo AI dư *góp phần*, *mà còn*, *không chỉ*, *đồng thời*, *thay vì* | [HIGH CONFIDENCE] | Bảng 3.2 | phép đo (nhật ký B) | | thực nghiệm |
| M02 | Bài blog AI dư *hành trình*, *mà là*, *quan trọng nhất*, *thay vì*, *điều quan trọng*, *bí quyết*, *hãy*, *dưới đây là* | [HIGH CONFIDENCE] | Bảng 3.2 | phép đo | | thực nghiệm |
| M03 | *một cách*, *có thể*, *điều này*, *bởi* không dư; *bởi* thiếu | [HIGH CONFIDENCE] | Bảng 3.3 | phép đo | | thực nghiệm |
| M04 | 15 cụm đồn là AI không xuất hiện ở mô hình 2026 | [ASSESSED] | 0/120 bài lô 2 | phép đo | | thực nghiệm |
| M05 | Gạch dài gần như biến mất | [HIGH CONFIDENCE] | 0–3,18 trên 1.000 chữ; văn người 0,00 | phép đo; A12 (VnExpress 15/11/2025) | | thực nghiệm + báo |
| M06 | Dấu hiệu tụ ở kết bài | [ASSESSED] | Bảng 3.5; thiếu mốc văn người | phép đo | | thực nghiệm |
| M07 | Claude: Title Case ở giao diện, *điều quan trọng không phải là… mà là…* | [HIGH CONFIDENCE] / [ASSESSED] | Mục 3.6 | phép đo | | thực nghiệm |
| T11 | 65,8% câu bị động Anh dịch thành bị động Việt | [CONFIRMED] | "Câu bị động 427 65,8 … Câu chủ động 184 28,4 … Tổng cộng 649" | vci.vnu.edu.vn/upload/15022/pdf/5763a1817f8b9aa7b58b45d2.pdf | Hoàng Công Bình, Ngôn ngữ & Đời sống 2015 | tạp chí |
| T09 | Mozilla: chủ động, bỏ số nhiều thừa | [CONFIRMED] | "Cố gắng chuyển câu bị động tiếng Anh thành câu chủ động tiếng Việt"; "“Thiết lập” chứ không phải “Những thiết lập”" | mozilla-l10n.github.io/styleguides/vi/ | Mozilla L10n | hướng dẫn cộng đồng |
| T19 | Thừa đã thành đúng | [CONFIRMED] | "nay đã thành “đúng”: cây đại thụ, đường quốc lộ, người nông dân" | thvl.vn/de-lau-cau-sai-hoa…-dung.html | Nguyễn Đức Dân | báo |
| T28 | Danh sách từ thừa trong văn bản quản lý | [CONFIRMED] | "Tái tạo lại, chưa vị thành niên, hoàn thành xong, đáp ứng theo, căn cứ theo…" | std.vnuhcmjournal.com.vn/…/1012/1421/2590 | Đỗ Văn Học 2015 | tạp chí |
| T21 | *tái … lại* | [CONFIRMED] | "Tái sinh lại, tái hiện lại, tái diễn lại, tái bản lại, phục chế lại" | tienphong.vn/chu-thua-post699411.tpo | Hồ Anh Thái | báo (ý kiến) |
| W01 | *sát nhập* có trong HP2003 như dạng trỏ | [CONFIRMED] | "sát nhập x. sáp nhập." | archive.org/details/tudientiengviet_vnnh_2003 | Viện Ngôn ngữ học | từ điển (OCR) |
| W06 | *yếu điểm* = điểm quan trọng | [CONFIRMED] | "yếu điểm d. (id.), Điểm quan trọng nhất"; An Chi: "điểm yếu … đồng nghĩa với nhược điểm" | archive.org; thanhnien.vn/diem-yeu-va-yeu-diem-185794175.htm | Viện Ngôn ngữ học; An Chi | từ điển + báo |
| H02 | *cứu cánh* = mục đích cuối cùng | [CONFIRMED] | "cứu cánh d. Mục đích cuối cùng. Nghệ thuật là…" | archive.org; dhtn.ttxvn.org.vn | Viện Ngôn ngữ học; TTXVN | từ điển + báo |
| W36 | Luật Thương mại dùng *khuyến mại* | [CONFIRMED] | "Khuyến mại là hoạt động xúc tiến thương mại của thương nhân…" | vcci.com.vn (Luật 36/2005/QH11) | Quốc hội | luật, bản sao |
| R26 | LanguageTool không hỗ trợ tiếng Việt | [CONFIRMED] | "'vi' is not a language code known to LanguageTool" | api.languagetool.org/v2/check | LanguageTool | API, chạy trực tiếp |
| R01 | binhvq news-corpus ngừng phân phối | [HIGH CONFIDENCE] | README repo | github.com/binhvq/news-corpus | binhvq | repo |
| R04 | FineWeb-2 vi ~28% thuộc 2023–2024 | [ASSESSED] | 800/2.900 dòng mẫu | datasets-server.huggingface.co | agent tự lấy mẫu | thực nghiệm thô |

Claim bị loại hoặc hạ mức: xem nhật ký, mục X.

---

## 7. Quy tắc dùng kho cho agent

1. **Cờ, không phải lệnh cấm.** Một cờ đơn lẻ giữ nguyên nếu có lý do. Viết lại khi **một đoạn có ≥ 3 cờ** của mục 4.1–4.2 (theo ngưỡng 3 dấu hiệu trong `development/style-audit.md` của skill viet-chuyen-nghiep), hoặc **cả bài có ≥ 4 cờ của thể loại đó trên mỗi 300 chữ** (bạn chốt Q12). Thử trên mẫu (bài AI lô 2; văn người ghép từ câu ngẫu nhiên thành đoạn dài tương đương):

   | Luật | Bài blog AI bị bắt | Bài báo AI bị bắt | Văn người bị bắt oan |
   |---|---|---|---|
   | ≥ 3 cờ trong một đoạn | 20/60 | 4/60 | 3/2.000 đoạn báo; 2/2.000 đoạn web |
   | Cả bài ≥ 3 cờ / 300 chữ | 46/60 | 19/60 | 2,4% (báo); 0,8% (web) |
   | **Cả bài ≥ 4 cờ / 300 chữ** | **34/60** | **13/60** | **0,2% (báo); 0,4% (web)** |
   | Cả bài ≥ 5 cờ / 300 chữ | 29/60 | 7/60 | 0% |

   Tỷ lệ bắt được là lạc quan, vì cờ được rút ra từ chính mẫu này `[ASSESSED]`. Bài báo AI ít bị bắt bằng từ ngữ, nên phải soát thêm độ cụ thể (số, tên, ngày) và mẫu cấu trúc.
2. **Theo thể loại.** Áp cột đúng thể loại ở 4.1. Không áp cờ blog (*hãy*) cho hướng dẫn từng bước, nơi câu mệnh lệnh là đúng thể loại.
3. **Soát đoạn kết trước.** Đây là nơi cờ tụ dày nhất (3.5).
4. **Sửa bằng nội dung, không bằng từ đồng nghĩa.** Đổi *hành trình* thành *chặng đường* vẫn là giọng AI. Phải thay bằng việc cụ thể, con số, tên riêng. Bouchard: "you can’t just delete delve; you have to change the skeleton" (A20).
5. **Không sửa danh sách 4.3** với lý do "giống AI".
6. **Lỗi từ (4.6) và từ thừa (4.5) là lỗi thật:** sửa luôn, trừ khi trích nguyên văn.
7. **Ghi ngày cho kho.** Tật đổi theo đời mô hình: gạch dài đã hết, *bức tranh* không còn. Đo lại mỗi quý bằng script ở nhật ký, mục B.

---

## 8. Điểm mù và câu còn mở

1. **Mẫu AI nhỏ:** 120 bài lô 2, khoảng 40.000 âm tiết. Mỗi họ mô hình chỉ khoảng 7.000 âm tiết, nên con số của từng họ dao động mạnh. Kết luận dựa trên số gộp và độ phủ theo họ.
2. **Kiểm định Poisson** giả định các lần xuất hiện độc lập. Một bài lặp cùng cụm sẽ làm p trông chắc hơn thực tế. Đã kèm cột "bài có cụm" để bù.
3. **Không có mốc văn người cho mở bài, kết bài:** kho Leipzig chỉ có câu rời.
4. **Mô hình:** Claude Sonnet 5 (qua cursor), không phải Opus hay Fable mà agent của bạn có thể dùng. GLM-4.6 chạy với system prompt "expert programmer" của glm CLI, có chèn câu ghi đè. Giọng có thể lệch.
5. **Thể loại mốc:** web 2015 không thuần blog. Văn người năm 2015 và 2019 có thể khác văn người năm 2026.
6. **Văn dịch:** chưa mở sách gốc của Cao Xuân Hạo, Nguyễn Đức Dân, Nguyễn Hiến Lê. Các trích Hạo đều gián tiếp (T12, T15, T16).
7. **Từ điển:** chỉ HP2003. Bản Vietlex 2007+ và Hồng Đức 2016 chưa kiểm. OCR lỗi dấu hỏi/ngã (*dè bỉu*, *chia sẻ*).
8. **Chưa đo:** hợp đồng và công văn do AI viết có lỗi gì riêng (lô 1 chỉ 1 đề mỗi loại); giọng AI khi đã có chỉ dẫn văn phong (agent thật của bạn luôn có skill).
9. **Chưa kiểm:** giấy phép Leipzig; độ chính xác VietAIDetector; mức nhiễm AI web tiếng Việt.
10. **Agent nhóm C** chưa tìm được bài đúng chủ đề của Lê Trung Hoa, Phạm Văn Tình, Đào Tiến Thi, Lê Xuân Mậu. Không gán ý kiến cho họ.

## 9. Cờ human-review (3 câu cho chuyên gia ngôn ngữ)

1. *khuyến mại* và *khuyến mãi*: trong văn thường (không phải văn bản pháp luật), dạng nào nên coi là chuẩn khi Luật Thương mại và Từ điển Hoàng Phê 2003 chọn khác nhau?
2. Các cụm đo được là dư trong văn AI (*góp phần*, *hành trình*, *không chỉ… mà còn*) có được giới biên tập Việt coi là sáo từ trước khi có AI không? Nếu có, có nguồn in nào?
3. Ngoài Cao Xuân Hạo và Nguyễn Đức Dân, có giáo trình hay sách chữa lỗi nào (Lê A, Nguyễn Minh Thuyết, Bùi Minh Toán) liệt kê cấu trúc văn dịch như *một cách + tính từ*, lạm dụng *việc/sự* không?

## 10. Chỗ trống cần điền

Q1–Q5 đã trả lời đầu phiên (mục 1). Q6–Q11 hỏi theo skill grill-everything, hai vòng, ngày 05/10/2026.

| Câu | Lựa chọn | Đề xuất | Quyết định (05/10/2026) |
|---|---|---|---|
| Q6. Nơi đặt kho | A. Skill viet-chuyen-nghiep: file mới `review/tu-ngu.md`, cập nhật `review/anti-ai.md` · B. Chỉ để trong báo cáo · C. Skill riêng mới | A | **A** |
| Q7. Cách áp | A. Cờ theo mật độ (lỗi từ sửa luôn) · B. Cấm cứng | A | **A** |
| Q12. Ngưỡng cả bài (hỏi sau khi thử luật trên mẫu) | A. ≥ 4 cờ / 300 chữ · B. ≥ 5 cờ cùng loại / bài · C. ≥ 3 cờ / 300 chữ | A | **A** |
| Q8. *khuyến mại* hay *khuyến mãi* ở văn thường | A. *khuyến mại* mọi nơi (Luật Thương mại 2005) · B. *khuyến mãi* ở văn thường | A | **A**. Cùng nguyên tắc với Q4, Q5: theo cách viết chiếm ưu thế trong luật |
| Q9. Script đo | A. Chỉ để trong nhật ký · B. Lưu vào skill viet-chuyen-nghiep · C. Lưu vào repo này | A | **A** |
| Q10. Thuật ngữ giao diện | A. Microsoft · B. Apple · C. Mozilla | A | **A** |
| Q11. Ý kiến nhà văn, nhà báo cho luật từ thừa | A. Được, ghi mức "mềm"; mục tranh cãi chỉ là gợi ý · B. Chỉ nhận nguồn học thuật | A | **A** |
