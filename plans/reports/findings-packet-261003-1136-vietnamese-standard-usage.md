---
title: "Findings packet — Dùng tiếng Việt đúng chuẩn: ai quy định gì, bắt buộc với ai, agent nên viết thế nào"
generated: "2026-10-03"
timezone: "UTC+7"
tools: "runtime-web (collect.py: serper, brave, jina-read, jina-search), pdftotext, tesseract OCR (agent), Node Intl (ICU 78.3 / CLDR 48.0), dữ liệu cldr-json 48.2.3; 4 agent thu thập song song; controller tự mở lại nguồn gốc"
verifier_engine: "none (không có `mr`); vòng 4 theo skill kiem-chung-thong-tin, domain LAW"
---

# Findings packet — Dùng tiếng Việt đúng chuẩn

Nhật ký kiểm từng claim: [verification-log-261003-1136-vietnamese-standard-usage.md](verification-log-261003-1136-vietnamese-standard-usage.md)

## 0. Tóm tắt 60 giây

1. **Không có một "chuẩn tiếng Việt" chung có giá trị pháp lý cho mọi người.**
   - Hiến pháp chỉ nói "Ngôn ngữ quốc gia là tiếng Việt" (L01). Chưa có luật ngôn ngữ (L02).
   - Mỗi phạm vi có văn bản riêng:
     - sách giáo khoa: QĐ 1989/QĐ-BGDĐT;
     - văn bản hành chính nhà nước: NĐ 30/2020;
     - văn bản pháp luật: NĐ 78/2025, Phụ lục I thay bằng NĐ 187/2025;
     - văn bản Đảng: HD 05-HD/VPTW năm 2026;
     - đơn vị đo: NĐ 86/2012;
     - kế toán: Luật Kế toán;
     - quảng cáo, nhãn hàng, tên doanh nghiệp: luật chuyên ngành.
   - Xem bảng ở mục 3.
2. **Với cá nhân hay doanh nghiệp tư nhân viết báo cáo, tài liệu, slide: gần như không có gì bắt buộc.**
   - Bộ Nội vụ trả lời: NĐ 30 "không xác định các tổ chức kinh tế là đối tượng bắt buộc áp dụng", nhưng có thể căn cứ vào đó (L08).
   - Bắt buộc thật chỉ khi bạn viết một trong các loại sau (N01–N09): quảng cáo; nhãn hàng; tên doanh nghiệp; hợp đồng với người tiêu dùng; chứng từ, sổ kế toán; hồ sơ đấu thầu trong nước.
3. **Chỉ có hai điểm tranh cãi thật: dấu thanh ("hòa" hay "hoà") và i/y ("kỹ" hay "kĩ").**
   - Văn bản duy nhất có quy định là QĐ 1989, chỉ ràng buộc người làm sách giáo khoa. Văn bản này chọn "hoà" và "kĩ" (C01, C02).
   - Luật, nghị định 2020–2025 phần lớn viết "hòa" và "kỹ". Văn bản Đảng 2026 viết "hoà" và "kỹ" (C05).
   - Báo cáo trong repo này đang viết "hoà" và "kỹ" (T01).
4. **Số: dấu phẩy thập phân là điểm duy nhất mọi nguồn cùng đồng ý.** NĐ 86/2012 bắt buộc dấu phẩy thập phân trong văn bản nhà nước (S01). Riêng phân cách hàng nghìn có 3 kiểu (S02):
   - dấu chấm: Luật Kế toán, dữ liệu chuẩn Unicode CLDR, Microsoft;
   - khoảng trắng: sách giáo khoa, chuẩn SI quốc tế;
   - dấu phẩy: thói quen, không có văn bản nào ủng hộ.
5. **Tiền: luật ghi "Đồng", ký hiệu quốc gia "đ", ký hiệu quốc tế "VND"** (S05). Chữ "VNĐ" không xuất hiện trong các luật đã đọc (S06).
6. **Mới trong 2025–2026, cần biết:**
   - NĐ 87/2026 phạt cá nhân 5.000.000 đến 10.000.000 đồng khi tiếng Việt trong quảng cáo "không bảo đảm giữ gìn sự trong sáng" (N03).
   - NĐ 37/2026 thay NĐ 43/2017 về nhãn hàng (N04).
   - Luật Báo chí 126/2025 thay luật 2016 (N05).
   - HD 05-HD/VPTW thay HD 36 (L11).
7. **Quy ước cho agent (mục 6):** 15 luật ngắn, mỗi luật có căn cứ. Bạn đã chốt 4 điểm (mục 10):
   - dấu thanh kiểu cũ (*hòa*);
   - dùng y (*kỹ*);
   - dấu chấm hàng nghìn;
   - *đồng / đ / VND*.
8. **Skill viet-chuyen-nghiep (chỉ báo cáo, không sửa):**
   - Phần lớn quy tắc viết hoa và dấu câu có căn cứ.
   - Một quy tắc trái với cách viết của văn bản nhà nước: dạy viết "kinh tế-xã hội" liền, trong khi luật viết "kinh tế - xã hội" (D04).
   - Thiếu luật về dấu thanh, i/y, số, ngày, tiền, mã hóa.
   - Skill viết kiểu "hòa", ngược với các báo cáo của bạn (mục 7).

---

## 1. Objective, phạm vi, cách làm

- **Câu hỏi chủ:** khi agent viết báo cáo, tài liệu, văn bản, slide bằng tiếng Việt cho bạn, "đúng chuẩn" do văn bản nào quy định, bắt buộc tới đâu, quy tắc cụ thể là gì; điểm nào chưa ngã ngũ thì nên chọn quy ước nào.
- **Mục đích sử dụng (bạn trả lời Q1):** hướng dẫn agent viết tiếng Việt cho báo cáo, tài liệu, văn bản, slide.
- **Thị trường, ngôn ngữ nguồn:** Việt Nam. Nguồn chính bằng tiếng Việt. Thêm nguồn quốc tế cho chuẩn kỹ thuật (Unicode, W3C, BIPM, Microsoft).
- **Thời điểm cắt:** 03/10/2026, 11:36 (UTC+7).
- **Cách làm:**
  - Dùng skill essential-questions dựng bộ câu hỏi: 1 câu chủ, 9 câu thiết yếu, 4 câu phụ, 2 câu bên lề (chuẩn phát âm, ngữ pháp "trong sáng": để ngoài phạm vi).
  - 4 agent thu thập song song: (A) pháp lý và chính tả; (B) văn bản hành chính và mã hóa; (C) số, tiền, dấu câu, lĩnh vực luật bắt buộc; (D) chuẩn ngành số và bản địa hóa.
  - Tôi tự mở lại khoảng 20 nguồn gốc cho các claim tác động lớn. Đọc bằng jina-read, tải PDF gốc, chạy Node Intl.
  - Vòng 4 chạy theo skill kiem-chung-thong-tin, với bộ câu hỏi pháp lý: văn bản còn hiệu lực không, áp dụng cho ai, cấp văn bản nào, đọc bản gốc hay bản sao.
  - Vòng 5 bù lỗ hổng chạy 1 lượt: tìm dự thảo sửa NĐ 30 và văn bản thay NĐ 86. Không thấy.
  - Skill grill-everything dùng để hỏi bạn các quyết định: Q1–Q9 đã trả lời (mục 10).
- **Giới hạn nguồn:**
  - thuvienphapluat.vn chặn truy cập tự động.
  - Nhiều văn bản chỉ đọc được qua bản sao toàn văn (luatvietnam.vn, trang tin của Chính phủ, trang trường học). Cột `source_type` ghi rõ.
- **Thẻ tin cậy trong packet này:**
  - `[CONFIRMED]`: tôi tự mở nguồn có thẩm quyền (hoặc bản sao toàn văn), **và** có thêm ít nhất một lần kiểm độc lập (agent khác hoặc bản sao khác).
  - `[HIGH CONFIDENCE]`: một lần mở nguồn gốc hoặc bản sao toàn văn.
  - `[ASSESSED]`: tổng hợp, suy luận, hoặc các nguồn mâu thuẫn nhau (giữ range).
  - `[LOW CONFIDENCE]`: chỉ có nguồn thứ cấp hoặc snippet.
  - `[BLIND SPOT]`: chưa kiểm được.

## 2. Từ điển (định nghĩa một lần, sau đó dùng lời thường)

| Từ | Nghĩa |
|---|---|
| **Văn bản quy phạm pháp luật (VBQPPL)** | Luật, nghị định, thông tư… có quy tắc chung, bắt buộc. Thể thức theo NĐ 78/2025. |
| **Văn bản hành chính** | Công văn, tờ trình, báo cáo, quyết định cá biệt… của cơ quan. Thể thức theo NĐ 30/2020. |
| **Thể thức** | Bộ khung trình bày: phông chữ, lề, cỡ chữ, cách ghi ngày, số hiệu. |
| **Dấu thanh** | Huyền, sắc, hỏi, ngã, nặng. |
| **Âm chính / âm đệm** | Trong "hòa", "a" là âm chính, "o" là âm đệm (âm lướt). |
| **Kiểu cũ / kiểu mới** | Kiểu cũ đặt dấu lên chữ đứng trước cho cân đối: *hòa, thủy, khỏe*. Kiểu mới đặt dấu lên âm chính: *hoà, thuỷ, khoẻ*. Tên gọi theo sổ tay UniKey. |
| **i ngắn / y dài** | Cặp viết khác nhau cho cùng một âm: *kĩ/kỹ, lí/lý, mĩ/mỹ*. |
| **Title Case / viết hoa kiểu câu** | Title Case viết hoa đầu mọi từ: *Hướng Dẫn Sử Dụng*. Viết hoa kiểu câu chỉ viết hoa chữ đầu và tên riêng: *Hướng dẫn sử dụng*. |
| **Unicode dựng sẵn (NFC) / tổ hợp (NFD)** | Dựng sẵn: "ề" là 1 ký tự. Tổ hợp: "e" + dấu mũ + dấu huyền = 3 ký tự. Mắt nhìn giống nhau, máy so khác nhau. |
| **TCVN** | Tiêu chuẩn Việt Nam. Tự nguyện, trừ khi văn bản pháp luật viện dẫn. |
| **CLDR** | Kho dữ liệu chuẩn của Unicode Consortium về cách viết số, ngày, tiền theo từng ngôn ngữ. Windows, macOS, Android, trình duyệt đều dùng. |
| **Style guide** | Sổ tay văn phong của một hãng hoặc tòa soạn. Không có giá trị pháp lý. |
| **Bản sao toàn văn** | Văn bản chép lại trên trang thứ ba (luatvietnam.vn…), không phải file ký số gốc. |
| **VBHN** | Văn bản hợp nhất: bản gộp luật gốc với các lần sửa. |

## 3. Bản đồ chuẩn: ai quy định gì, bắt buộc với ai

| Phạm vi | Văn bản (hiện hành đến 03/10/2026) | Quy định gì về tiếng Việt | Bắt buộc với | Với báo cáo, tài liệu của bạn | Claim |
|---|---|---|---|---|---|
| Nguyên tắc quốc gia | Hiến pháp 2013, Điều 5.3 | "Ngôn ngữ quốc gia là tiếng Việt." Không nói cách viết | Mọi người | Không có quy tắc để theo | L01, L02 |
| Sách giáo khoa phổ thông | QĐ 1989/QĐ-BGDĐT (25/05/2018) | Chính tả đầy đủ nhất: dấu thanh, i/y, tên nước ngoài, thuật ngữ, ngày, số | Người làm chương trình, sách giáo khoa và "tổ chức, cá nhân liên quan" | Không bắt buộc. Là văn bản chính tả mới nhất của Nhà nước, tham chiếu tốt | L05, L06, C01–C09 |
| Sách giáo khoa (cũ hơn) | QĐ 240/QĐ (05/03/1984); QĐ 07/2003/QĐ-BGDĐT | Nguyên tắc chính tả, viết hoa tên riêng | Ngành giáo dục; người biên soạn sách giáo khoa | Không bắt buộc | L06, L07, V05 |
| Văn bản hành chính | NĐ 30/2020/NĐ-CP (05/03/2020) | Thể thức; viết hoa (Phụ lục II); viết tắt tên loại; ngày tháng | Cơ quan, tổ chức nhà nước, doanh nghiệp nhà nước | Không bắt buộc. Theo khi gửi văn bản cho cơ quan nhà nước | L08, L09, V01–V03 |
| Văn bản pháp luật | Luật 64/2025/QH15, Điều 7; NĐ 78/2025, Phụ lục I thay bởi NĐ 187/2025 | Tiếng Việt "chính xác, phổ thông, thống nhất"; thể thức, viết hoa, viết tắt | Cơ quan soạn văn bản pháp luật | Không áp dụng | L04, L10, V04 |
| Văn bản Đảng | HD 05-HD/VPTW (27/05/2026) | Thể thức, phông chữ, ngày tháng | Cấp ủy, cơ quan đảng. Loại trừ doanh nghiệp | Không áp dụng | L11 |
| Mã hóa chữ | TCVN 6909:2001; QĐ 72/2002/QĐ-TTg | Bộ mã Unicode cho chữ Việt | Trao đổi điện tử giữa tổ chức Đảng và Nhà nước | Nên theo (Unicode dựng sẵn) | L12, M01–M04 |
| Đo lường | Luật Đo lường 2011, Điều 9; NĐ 86/2012, Phụ lục V | Dấu phẩy thập phân; số cách ký hiệu đơn vị; °C | Văn bản do cơ quan nhà nước ban hành (và các trường hợp khác ở Điều 9) | Nên theo | S01, S03 |
| Kế toán | Luật Kế toán (VBHN 41/VBHN-VPQH, 16/03/2026), Điều 10–11 | Chữ viết tiếng Việt; dấu chấm hàng nghìn, dấu phẩy thập phân; "đ", "VND" | Đơn vị kế toán | **Bắt buộc** cho sổ sách, báo cáo tài chính | N08, S02, S05 |
| Tiền tệ | Luật Ngân hàng Nhà nước 2010, Điều 16 | "Đồng", "đ", "VND" | Mọi văn bản pháp luật về tiền | Nên theo | S05 |
| Quảng cáo | Luật Quảng cáo, Điều 18 (sửa bởi Luật 75/2025); NĐ 87/2026 xử phạt | Phải có tiếng Việt; chữ nước ngoài ≤ 3/4 khổ chữ Việt; "trong sáng" | Người quảng cáo | **Bắt buộc**, có phạt | N01–N03 |
| Nhãn hàng hóa | NĐ 37/2026/NĐ-CP, Điều 39 | Nội dung bắt buộc ghi tiếng Việt; chữ nước ngoài không lớn hơn chữ Việt | Hàng lưu thông ở Việt Nam | **Bắt buộc** | N04 |
| Tên doanh nghiệp | Luật Doanh nghiệp 2020, Điều 37, 39 | Chữ cái tiếng Việt và F, J, Z, W; tên nước ngoài khổ chữ nhỏ hơn | Doanh nghiệp | **Bắt buộc** | N06 |
| Hợp đồng với người tiêu dùng | Luật 19/2023/QH15, Điều 23.2 | Ngôn ngữ hợp đồng là tiếng Việt | Bên bán | **Bắt buộc** | N07 |
| Báo chí | Luật Báo chí 126/2025/QH15 (hiệu lực 01/07/2026), Điều 8, khoản 7 | Cấm "sử dụng ngôn ngữ làm biến dạng tiếng Việt dẫn đến hiểu sai nội dung tuyên truyền" | Cơ quan báo chí | Không áp dụng | N05 |
| Giáo dục | Luật Giáo dục 2019, Điều 11.1 | Tiếng Việt là ngôn ngữ chính thức trong cơ sở giáo dục | Cơ sở giáo dục | Không áp dụng | L03 |
| Đấu thầu trong nước | Luật Đấu thầu 22/2023, Điều 12.1 | Ngôn ngữ là tiếng Việt | Bên mời thầu, nhà thầu | **Bắt buộc** nếu làm hồ sơ thầu | N09 |
| Tên cơ quan sang tiếng Anh | TT 05/2026/TT-BNG (30/06/2026) | Cách dịch Quốc hiệu, tên cơ quan, chức danh | Hệ thống chính trị | Dùng khi báo cáo song ngữ có tên cơ quan nhà nước | L13 |
| Chuẩn ngành (không pháp lý) | Unicode CLDR 48.2.3; Microsoft Vietnamese Style Guide; Mozilla; Netflix | Số, ngày, tiền trên phần mềm; văn phong; dấu câu | Không ai | Tham chiếu cho slide, tài liệu số | B01–B03, D02, D03 |
| Học thuật | Từ điển tiếng Việt (Hoàng Phê chủ biên); Viện Ngôn ngữ học | Nghĩa, chính tả từ | Không ai. Viện không có thẩm quyền ban hành chuẩn | Tra khi phân vân | C10, L14 |

**Hình dung cụ thể:**
- Chị Hà làm ở một công ty phần mềm tư nhân. Chị viết báo cáo thị trường bằng "hòa", "kĩ", "1,000,000 VNĐ". Không luật nào phạt chị. Báo cáo vẫn trông thiếu chuẩn vì lệch hết các văn bản tham chiếu.
- Cùng câu đó in lên băng-rôn quảng cáo. Nếu chữ tiếng Anh to hơn 3/4 chữ Việt, hoặc tiếng Việt "không rõ ràng, không dễ hiểu", công ty chị có thể bị phạt theo NĐ 87/2026. Mức phạt tổ chức gấp đôi mức cá nhân.

---

## 4. Quy tắc cụ thể đã kiểm, theo chủ đề

### 4.1 Viết hoa (NĐ 30/2020, Phụ lục II)

Ví dụ trong bảng là nguyên văn nghị định.

| Trường hợp | Viết | Không viết | Claim |
|---|---|---|---|
| Đầu câu | Sau `.` `?` `!` và khi xuống dòng | | V01 |
| Đơn vị hành chính: danh từ chung + tên riêng | thành phố Thái Nguyên, tỉnh Nam Định | Thành Phố Thái Nguyên | V01 |
| Đơn vị hành chính có số, tên người | Quận 1, Phường Điện Biên Phủ | quận 1 | V01 |
| Viết hoa đặc biệt | Thủ đô Hà Nội, Thành phố Hồ Chí Minh | | V01 |
| Địa hình + tên một âm tiết thành tên riêng | Vũng Tàu, Cửa Lò, Cầu Giấy | | V02 |
| Địa hình đi trước tên riêng | biển Cửa Lò, chợ Bến Thành, sông Vàm Cỏ, vịnh Hạ Long | Sông Vàm Cỏ | V02 |
| Cơ quan, tổ chức | Bộ Tài nguyên và Môi trường, Văn phòng Chủ tịch nước, Sở Tài chính | Bộ Tài Nguyên Và Môi Trường | V01 |
| Tổ chức nước ngoài | Liên hợp quốc (UN), Tổ chức Y tế thế giới (WHO) | | V01 |
| Chức vụ | "Viết hoa tên chức vụ, học vị nếu đi liền với tên người cụ thể": Chủ tịch Quốc hội, Thủ tướng Chính phủ, Giáo sư Tôn Thất Tùng | | V03 |
| Danh từ đặc biệt | Nhân dân, Nhà nước | | V01 |
| Tên văn bản; điều khoản | Bộ luật Hình sự; "điểm a khoản 2 Điều 103 Mục 5 Chương XII Phần I" | Bộ Luật Hình Sự | V01 |
| Ngày, tháng bằng chữ | thứ Hai, thứ Tư, tháng Năm, tháng Tám | Thứ hai, Tháng năm | V01 |
| Tết, ngày lễ | tết Nguyên đán, ngày Quốc khánh 2-9 | | V01 |

**Lưu ý khi áp dụng:**
- Quy tắc chức vụ trong NĐ 30 lệch với chính ví dụ của nó. Quy tắc nói "đi liền với tên người cụ thể", nhưng hai ví dụ đầu không kèm tên người (V03).
- Văn bản pháp luật theo NĐ 78/187 hơi khác (V04):
  - viết hoa sau dấu hai chấm khi mở ngoặc kép, và đầu mỗi khoản, điểm;
  - "Nhà nước" chỉ viết hoa khi dùng như danh từ riêng;
  - ví dụ đã đổi theo mô hình chính quyền 2 cấp: "tỉnh Ninh Bình; phường Ba Đình".

### 4.2 Tiêu đề, heading, slide, nút bấm

- **NĐ 30:** không có điều riêng cho tiêu đề. Nhưng quy tắc gốc là chỉ viết hoa đầu câu và tên riêng.
- **Microsoft (tr. 24):** "In Vietnamese, only the first character in a sentence is capitalized." Có bảng đúng/sai: *Chọn tất cả* đúng, *Chọn Tất Cả* sai.
- **Mozilla:** cấm Title Case kiểu Anh.
- **Phản chứng (giữ nguyên, V06):**
  - Microsoft trang 28 "accept title capitalization".
  - Thanh điều hướng của Apple tiếng Việt viết "Mua Hàng".
  - Netflix có tên phim viết Title Case.

**Kết luận:** viết hoa kiểu câu là chuẩn có nhiều căn cứ nhất. Title Case là thói quen dịch từ tiếng Anh.

### 4.3 Dấu thanh: "hòa" hay "hoà"? (đã chốt Q4: kiểu cũ "hòa")

**Câu hỏi thật sự:** khi một âm tiết có âm đệm o/u (oa, oe, uy), dấu đặt lên chữ nào?

**Hai phương án:**
- **A. Kiểu mới (dấu trên âm chính):** *hoà, hoá, khoẻ, thuỷ, tuỳ, uỷ, xoá, khoá.*
- **B. Kiểu cũ (dấu trên chữ đứng trước):** *hòa, hóa, khỏe, thủy, tùy, ủy, xóa, khóa.*

**Bằng chứng đã kiểm:**
- QĐ 1989, Điều 8: "dấu thanh được đặt trên hoặc dưới chữ cái ghi âm chính… ví dụ: *hoà nhạc, quý hoá, thuỷ thủ, mạnh khoẻ*". Đây là văn bản Nhà nước duy nhất có quy định (C01).
- Đếm trên bản sao văn bản, tức kiểu cũ / kiểu mới (C05):
  - Luật 64/2025: 116 / 0
  - NĐ 187/2025: 134 / 1
  - NĐ 78/2025: 35 / 6
  - NĐ 30/2020: 44 / 9
  - HD 05-HD/VPTW 2026: 0 / 142
  - Chính QĐ 1989: 9 / 5 (tự viết lẫn, ví dụ "tùy ngữ cảnh", "hóa học")
- Ngành số (C05, M05):
  - Microsoft và Apple dùng kiểu cũ; Google dùng chủ yếu kiểu mới.
  - Bộ gõ OpenKey và UniKey bản Linux mặc định kiểu cũ.
  - Sổ tay UniKey ghi: "Theo nhiều nhà ngôn ngữ học thì 'kiểu mới' được coi là đúng chính tả".
- Repo của bạn (T01, T02):
  - báo cáo: kiểu mới 198 / kiểu cũ 48;
  - skill viet-chuyen-nghiep: kiểu mới 6 / kiểu cũ 92.

**Điều gì đổi nếu chọn:**
- Chọn A: khớp văn bản quy định duy nhất và khớp báo cáo cũ của bạn. Nhưng lệch với bộ gõ mặc định, nên văn bản bạn tự gõ sẽ lẫn kiểu nếu không chỉnh bộ gõ.
- Chọn B: khớp luật, nghị định và bộ gõ. Nhưng phải sửa khoảng 200 từ trong báo cáo cũ để thống nhất.
- Cả hai đều **không sai về pháp lý**, trừ khi viết sách giáo khoa.
- Hai kiểu là hai chuỗi ký tự khác nhau (*hòa* = `68 f2 61`, *hoà* = `68 6f e0`), nên tìm kiếm phải khớp được cả hai (M04).

**Khuyến nghị lúc đầu:** A (kiểu mới).

**Quyết định của bạn (Q4, 03/10/2026):** B (kiểu cũ). Lý do hợp lệ: khớp phần lớn luật, nghị định, bộ gõ mặc định và skill viet-chuyen-nghiep.

**Hệ quả:**
- Khoảng 200 từ kiểu mới trong các báo cáo cũ sẽ lệch quy ước (T01). Có sửa hay không: xem Q9.
- Packet này đã chuyển sang kiểu cũ, trừ trích dẫn và ví dụ của phương án A.

### 4.4 i hay y: "kỹ" hay "kĩ"? (đã chốt Q5: "kỹ")

**Câu hỏi thật sự:** âm /i/ đứng ngay sau phụ âm đầu, không có âm cuối (h, k, l, m, s, t + i), viết i hay y?

**Hai phương án:**
- **A. y theo thói quen:** *kỹ thuật, lý do, nước Mỹ, tỷ lệ, hy vọng, kỷ niệm.*
- **B. i theo QĐ 1989, Điều 9:** *kĩ thuật, lí do, mĩ thuật, tỉ lệ, hi vọng, kỉ niệm.*

**Bằng chứng đã kiểm:**
- QĐ 1989, Điều 9: "Trường hợp âm i đứng ngay sau phụ âm đầu thì được viết bằng chữ i". Tên riêng giữ đúng tên: *Nguyễn Vỹ, Thy Ngọc* (C02).
- Văn bản Chính phủ, Quốc hội và văn bản Đảng 2026 đều viết "kỹ", "lý" (C04).
- Microsoft, Apple, Google đều viết "lý", "kỹ" (C04).
- Khảo sát năm 2011: 46 trên 49 nhà xuất bản vẫn phân biệt i/y theo kiểu cũ (C04). Chưa có khảo sát mới hơn.
- Báo cáo của bạn: "kỹ" 58, "lý" 119, "Mỹ" 32, "kĩ" và "lí" 0 lần. Nhưng "tỷ" và "tỉ" cùng 11 lần, tức đang lẫn (T01).
- Gốc của quy tắc "i" còn tranh cãi (C03): nguồn thì nói từ Quy định 1980, nguồn thì nói từ QĐ 240/1984.

**Điều gì đổi nếu chọn:**
- Chọn A: khớp văn bản nhà nước ngoài ngành giáo dục, khớp báo chí và báo cáo cũ của bạn. Lệch sách giáo khoa.
- Chọn B: khớp sách giáo khoa. Lệch gần như mọi văn bản bạn sẽ đọc và trích.

**Khuyến nghị:** A (y), trừ khi tài liệu dành cho trường phổ thông. Sửa "tỉ" thành "tỷ" cho thống nhất.

**Nguyên tắc chung sau quyết định Q4 và Q5:** theo thói quen chiếm ưu thế trong luật, nghị định của Quốc hội và Chính phủ, tức *hòa* và *kỹ*. QĐ 1989 chỉ áp dụng khi viết cho trường phổ thông. Nguyên tắc này nhất quán cho cả hai điểm.

### 4.5 Tên riêng và thuật ngữ nước ngoài

Hai hệ đang cùng tồn tại:
- **NĐ 30 (hành chính, C08):** phiên âm có gạch nối, ví dụ *Vla-đi-mia I-lích Lê-nin, Mát-xcơ-va, Men-bon*. Phiên âm Hán Việt quen dùng: *Mao Trạch Đông, Bắc Kinh*.
- **QĐ 1989, Điều 5 (sách giáo khoa từ trung học cơ sở, C07):**
  - Tên chữ Latin viết nguyên dạng: *Victor Hugo, Paris, New York*. Dấu phụ thì lược: *Petõfi* thành *Petofi*.
  - Tên không dùng chữ Latin thì viết như tiếng Anh: *Moscow, Tokyo, Zhejiang*.
  - Tên Hán Việt đã quen giữ nguyên: *Ba Lan, Hy Lạp, Thổ Nhĩ Kỳ*.
  - Riêng tiểu học vẫn phiên âm có gạch nối.
- **Thuật ngữ, QĐ 1989, Điều 7 (C09):** viết nguyên dạng tiếng Anh. Ví dụ "Không phiên âm hydrogen thành hyđrô, hiđrô…".
- **Microsoft (B02):** giữ nguyên các từ viết tắt tiếng Anh và các từ như "OK", "tab".

### 4.6 Số, đơn vị, tiền, ngày, giờ

| Mục | Văn bản nhà nước | Sách giáo khoa (QĐ 1989) | Kế toán | Phần mềm (CLDR, Microsoft) | Claim |
|---|---|---|---|---|---|
| Thập phân | dấu phẩy, `245,12 mm` (NĐ 86, bắt buộc) | dấu phẩy, `5,21` | dấu phẩy | dấu phẩy, `1.234,5` | S01 |
| Hàng nghìn | **không quy định** | khoảng trắng, `1 234 567` | dấu chấm, `1.234.567` (bắt buộc) | dấu chấm, `1.234.567` | S02 |
| Số với ký hiệu đơn vị | cách 1 dấu cách, `22 m`, `15 °C`; góc viết liền | | | NBSP, `250 GB` | S03 |
| % | không quy định | | | viết liền, `80%`, `25,6%` (BIPM thì cách) | S04 |
| Tiền | "Đồng", "đ", "VND" (Luật Ngân hàng Nhà nước) | | "đ", "VND" | `1.234.567 ₫`, ký hiệu sau, NBSP | S05, S06 |
| Ngày đầy đủ | `ngày 05 tháng 3 năm 2020` (số 0 trước ngày < 10 và tháng 1, 2) | | | `3 tháng 10, 2026` | S07 |
| Ngày rút gọn | | `20-11-2017` hoặc `20/11/2017`, một tài liệu một kiểu | | `3/10/26` | S07 |
| Khoảng ngày | | `15/10/2017 - 20/11/2017` | | | S07 |
| Giờ | (chưa kiểm: "14 giờ 30") | | | `11:05` (24 giờ) | S08 |

**Hình dung:** viết "doanh thu 1,234 tỷ" là mơ hồ. Người theo kiểu Việt đọc thành 1 phẩy 234 tỷ; người quen kiểu Anh đọc thành một nghìn hai trăm ba mươi tư tỷ. Đây là lý do phải chốt một kiểu (Q6).

### 4.7 Dấu câu và khoảng trắng

- **Không có văn bản quy phạm nào** quy định cách dùng dấu câu hay khoảng trắng. QĐ 1989 không có điều nào về dấu câu (D01).
- **Microsoft (D02):**
  - không cách trước `. ? !`, cách sau;
  - không cách sau `(`, cách trước `(`;
  - "Please do not use comma before 'và' and 'hoặc'";
  - NBSP (khoảng trắng không ngắt dòng) giữa số và đơn vị;
  - không cách giữa số và `%`.
- **Mozilla (D03):** dấu ba chấm là một ký tự (U+2026); câu bị động tiếng Anh nên chuyển sang chủ động.
- **Văn bản luật dùng gạch nối có cách giữa hai danh từ ngang hàng (D04):**
  - "kinh tế - xã hội": Luật 64/2025 viết có cách 14 lần, liền 0 lần;
  - "chính trị - xã hội" (NĐ 30);
  - "Độc lập - Tự do - Hạnh phúc".

### 4.8 Mã hóa (cho file, tìm kiếm, xử lý)

- **TCVN 6909:2001** là bộ mã 16 bit, khớp Unicode 3.0. Tiêu chuẩn có cả dạng dựng sẵn lẫn dạng tổ hợp, không chọn dạng nào (M01).
- **NĐ 30, NĐ 78, HD 05** đều ghi: phông Times New Roman, "bộ mã ký tự Unicode theo Tiêu chuẩn Việt Nam TCVN 6909:2001" (M02).
- **W3C và Unicode** khuyến nghị dạng dựng sẵn (NFC) cho nội dung. Tác giả UniKey cũng khuyên người dùng thường ưu tiên dựng sẵn (M03).
- **Thực nghiệm (M04):**
  - "Việt" ở dạng NFC dài 4 ký tự, ở dạng NFD dài 6.
  - Tìm một chuỗi NFD trong văn bản NFC sẽ không thấy. Chuẩn hóa cả hai về NFC thì thấy.

### 4.9 Văn phong (khi viết hoặc dịch)

- **Microsoft (B02, B03):**
  - giọng "clear, friendly and concise";
  - tránh dịch từng chữ, vì sẽ "stiff and unnatural";
  - ưu tiên *Không lưu được hình ảnh.* hơn *Lưu hình ảnh thất bại.*;
  - xưng "bạn", tránh đại từ có giới tính khi nói chung.
- **Sắc thái "được/bị" (B04, nguồn yếu):** "được" mang nghĩa thuận, "bị" mang nghĩa nghịch. Khi dịch câu bị động trung tính, nên đổi sang câu chủ động.

---

## 5. Bảng claim đã kiểm

Số và trích dẫn giữ nguyên như nguồn. URL đầy đủ, ngày, nguồn phụ ở nhật ký.

| ID | Claim | Tag | Nguyên văn / số | URL chính | primary_origin | source_type |
|---|---|---|---|---|---|---|
| L01 | Hiến pháp: ngôn ngữ quốc gia | [CONFIRMED] | "Ngôn ngữ quốc gia là tiếng Việt." | xaydungchinhsach.chinhphu.vn (toàn văn Hiến pháp); datafiles.chinhphu.vn VBHN 52 | Quốc hội | non-AI, bản sao chính thức |
| L02 | Chưa có luật ngôn ngữ, luật tiếng Việt | [HIGH CONFIDENCE] | "vẫn chưa có văn bản luật nào xác định tiếng Việt là ngôn ngữ chính thức" (2021); Chương trình lập pháp 2026: 0 lần "ngôn ngữ" | daibieunhandan.vn; luatvietnam.vn (tóm tắt NQ 105/2025) | báo Quốc hội; UBTVQH | non-AI; bằng chứng phủ định |
| L03 | Luật Giáo dục, Điều 11.1 | [CONFIRMED] | "Tiếng Việt là ngôn ngữ chính thức dùng trong cơ sở giáo dục." | datafiles.chinhphu.vn VBHN 72; luatvietnam.vn | Quốc hội | non-AI |
| L04 | Luật 64/2025, Điều 7.1 | [CONFIRMED] | "…là tiếng Việt, bảo đảm chính xác, phổ thông, thống nhất, diễn đạt rõ ràng, dễ hiểu." | xaydungchinhsach.chinhphu.vn | Quốc hội | non-AI, bản sao |
| L05 | Phạm vi QĐ 1989 | [CONFIRMED] | "áp dụng đối với tổ chức, cá nhân xây dựng chương trình, biên soạn sách giáo khoa giáo dục phổ thông và tổ chức, cá nhân liên quan" | luatvietnam.vn; scribd.com | Bộ GD&ĐT | non-AI, 2 bản sao |
| L06 | Hiệu lực QĐ 240, 07/2003, 1989 | [ASSESSED] | 07/2003: "Còn hiệu lực" (vbpl.vn, 01/04/2026). 240, 1989: chưa thấy văn bản bãi bỏ; không có trong 11 văn bản hết hiệu lực theo TT 47/2026 | vbpl.vn; suckhoedoisong.vn | Bộ GD&ĐT | non-AI; phủ định |
| L07 | QĐ 240: phạm vi; không có quy tắc i/y | [HIGH CONFIDENCE] | "…áp dụng cho các sách giáo khoa, báo và văn bản của ngành giáo dục." | luatvietnam.vn | Bộ Giáo dục | non-AI, bản sao |
| L08 | NĐ 30 bắt buộc với ai | [CONFIRMED] | "áp dụng đối với cơ quan, tổ chức nhà nước và doanh nghiệp nhà nước"; Bộ Nội vụ: "không xác định các tổ chức kinh tế là đối tượng bắt buộc áp dụng" | datafiles.chinhphu.vn (bản ký số); baochinhphu.vn 22/12/2020 | Chính phủ; Bộ Nội vụ | non-AI, gốc |
| L09 | NĐ 30 còn hiệu lực | [HIGH CONFIDENCE] | vbpl.vn "Còn hiệu lực" (cập nhật 01/04/2026); Bộ Nội vụ vẫn dẫn (29/07/2026); không thấy văn bản sửa đến 09/2026 | vbpl.vn; vtv.vn | Chính phủ | non-AI |
| L10 | NĐ 78/2025 thay NĐ 34/2016, 154/2020, 59/2024; NĐ 187/2025 thay Phụ lục I | [HIGH CONFIDENCE] | "Thay thế Phụ lục I ban hành kèm theo Nghị định số 78/2025/NĐ-CP…" | xaydungchinhsach.chinhphu.vn; luatvietnam.vn | Chính phủ | non-AI, bản sao |
| L11 | HD 05-HD/VPTW (27/05/2026) | [CONFIRMED] | Thay HD 36-HD/VPTW; "Các tổ chức, cơ quan hoạt động theo Luật Doanh nghiệp không thuộc đối tượng áp dụng"; "Ngày dưới 10 và tháng dưới 3 phải thêm số không (0)" | xdcs.cdnchinhphu.vn (PDF) | Văn phòng Trung ương Đảng | non-AI, gốc |
| L12 | QĐ 72/2002/QĐ-TTg | [HIGH CONFIDENCE] | "Kể từ ngày 01 tháng 01 năm 2003, thống nhất dùng bộ mã… TCVN 6909:2001… trong trao đổi thông tin điện tử giữa các tổ chức của Đảng và Nhà nước." | luatvietnam.vn | Thủ tướng | non-AI, bản sao; hiệu lực chưa kiểm |
| L13 | TT 05/2026/TT-BNG | [HIGH CONFIDENCE] | Ngày 30/06/2026; dịch Quốc hiệu, tên cơ quan, chức danh sang tiếng Anh | luatvietnam.vn | Bộ Ngoại giao | non-AI, bản sao |
| L14 | Viện Ngôn ngữ học chỉ nghiên cứu, tư vấn | [HIGH CONFIDENCE] | "Tham gia góp ý và phản biện khoa học…" | vienngonnguhoc.vass.gov.vn | Viện Hàn lâm KHXH | non-AI |
| L15 | Không cải tiến chữ viết (2017) | [HIGH CONFIDENCE] | Bộ GD&ĐT "không đủ thẩm quyền và không có dự kiến áp dụng bất cứ một phương án nào về cải tiến chữ viết quốc gia" | daibieunhandan.vn; dantri.com.vn | Bộ GD&ĐT | non-AI, báo |
| N01 | Quảng cáo: chữ nước ngoài ≤ 3/4 | [CONFIRMED] | "khổ chữ nước ngoài không được quá ba phần tư khổ chữ tiếng Việt và phải đặt bên dưới chữ tiếng Việt" | vanban.chinhphu.vn (Luật 16/2012); luatvietnam.vn (NĐ 87/2026, điểm c) | Quốc hội; Chính phủ | non-AI |
| N02 | Quảng cáo: "trong sáng" (từ 01/01/2026) | [HIGH CONFIDENCE] | "Từ ngữ bằng tiếng Việt trong sản phẩm quảng cáo phải bảo đảm giữ gìn sự trong sáng của tiếng Việt, rõ ràng, dễ hiểu…" | luatvietnam.vn (Luật 75/2025) | Quốc hội | non-AI, bản sao |
| N03 | NĐ 87/2026: mức phạt | [CONFIRMED] | "Phạt tiền từ 5.000.000 đồng đến 10.000.000 đồng…"; NĐ 38/2021 hết hiệu lực; hiệu lực 15/05/2026 (chỉ agent kiểm) | luatvietnam.vn | Chính phủ | non-AI, bản sao |
| N04 | NĐ 37/2026: nhãn hàng | [CONFIRMED] | "…phải ghi bằng tiếng Việt…"; "kích thước chữ của ngôn ngữ khác không được lớn hơn kích thước chữ tiếng Việt"; NĐ 43/2017, 111/2021 hết hiệu lực | luatvietnam.vn; vanban.chinhphu.vn | Chính phủ | non-AI, bản sao |
| N05 | Luật Báo chí 126/2025 | [CONFIRMED] | Điều cấm "sử dụng ngôn ngữ làm biến dạng tiếng Việt dẫn đến hiểu sai nội dung tuyên truyền"; Luật 103/2016 hết hiệu lực | luatvietnam.vn | Quốc hội | non-AI, bản sao |
| N06 | Tên doanh nghiệp | [HIGH CONFIDENCE] | "Tên riêng được viết bằng các chữ cái trong bảng chữ cái tiếng Việt, các chữ F, J, Z, W, chữ số và ký hiệu." | luatvietnam.vn (VBHN 67/2025) | Quốc hội | non-AI, bản sao |
| N07 | Hợp đồng với người tiêu dùng | [HIGH CONFIDENCE] | "Ngôn ngữ sử dụng trong hợp đồng giao kết với người tiêu dùng… là tiếng Việt." | luatvietnam.vn | Quốc hội | non-AI, bản sao |
| N08 | Kế toán | [CONFIRMED] | "Chữ viết sử dụng trong kế toán là tiếng Việt."; dấu chấm hàng nghìn, dấu phẩy thập phân | vbpl.vn (VBHN 41, 16/03/2026) | Quốc hội | non-AI, gốc hợp nhất |
| N09 | Đấu thầu trong nước | [LOW CONFIDENCE] | "Ngôn ngữ sử dụng đối với đấu thầu trong nước là tiếng Việt." | dauthau.gxd.vn | (Quốc hội) | bản tổng hợp, chưa đối chiếu gốc |
| C01 | QĐ 1989: dấu thanh trên âm chính | [CONFIRMED] | "dấu thanh được đặt trên hoặc dưới chữ cái ghi âm chính… *hoà nhạc, quý hoá, thuỷ thủ, mạnh khoẻ*"; ia/ua/ưa: dấu trên chữ thứ nhất; iê/yê/uô/uơ: chữ thứ hai | luatvietnam.vn; scribd.com | Bộ GD&ĐT | non-AI, 2 bản sao |
| C02 | QĐ 1989: i sau phụ âm đầu | [CONFIRMED] | "*hi vọng, kỉ niệm, lí luận, mĩ thuật, bác sĩ, tỉ lệ*"; tên riêng: "*Nguyễn Vỹ, Thy Ngọc*" | luatvietnam.vn | Bộ GD&ĐT | non-AI, bản sao |
| C03 | Gốc quy tắc i | [ASSESSED] | Đào Tiến Thi (2011): từ Quy định 30/11/1980, QĐ 240 "không đề cập". Tuổi Trẻ (2020): QĐ 240 có quy định i/y | ngonnguhoc.org; tuoitre.vn | học giả; báo | non-AI, mâu thuẫn |
| C04 | Ngoài sách giáo khoa dùng y | [ASSESSED] | 46/49 NXB phân biệt i/y (2011); văn bản Chính phủ/Quốc hội, Đảng 2026, Microsoft/Apple/Google: kỹ, lý | ngonnguhoc.org; đếm trên bản sao | nhiều | non-AI + đếm cục bộ |
| C05 | Dấu thanh trên thực tế chia đôi | [ASSESSED] | Bảng đếm ở 4.3 | bản sao văn bản; trang hỗ trợ của hãng | nhiều | đếm cục bộ trên bản sao |
| C06 | Chuyên gia bất đồng | [HIGH CONFIDENCE] | GS Nguyễn Minh Thuyết (2018): "Dự thảo quy định đặt dấu thanh vào âm chính"; i/y giữ theo 1980. PGS Phạm Văn Tình: "uy" phải là y dài. Hoàng Dũng: i và y đều được | dantri.com.vn; tuoitre.vn | chuyên gia | non-AI, báo |
| C07 | QĐ 1989: tên nước ngoài | [CONFIRMED] | "Trường hợp tên được viết bằng chữ Latin thì viết nguyên dạng chữ Latin"; non-Latin "viết như cách viết trong tiếng Anh" | luatvietnam.vn | Bộ GD&ĐT | non-AI, bản sao |
| C08 | NĐ 30: phiên âm có gạch nối | [HIGH CONFIDENCE] | "Vla-đi-mia I-lích Lê-nin"; "Mát-xcơ-va, Men-bon" | datafiles.chinhphu.vn (OCR bản ký số) | Chính phủ | non-AI, gốc |
| C09 | QĐ 1989: thuật ngữ nguyên dạng | [CONFIRMED] | "Không phiên âm hydrogen thành hyđrô, hiđrô, hy-đrô, hi-đrô, mà viết nguyên dạng tiếng Anh" | luatvietnam.vn | Bộ GD&ĐT | non-AI, bản sao |
| C10 | Từ điển Hoàng Phê là tham chiếu de facto, đang tranh cãi bản | [ASSESSED] | Microsoft liệt kê làm "normative references"; báo Thanh Hóa (02/2026): có 3 bản "Hoàng Phê" | download.microsoft.com; baothanhhoa.vn | hãng; báo | non-AI |
| V01 | NĐ 30, Phụ lục II: các nhóm viết hoa | [CONFIRMED] | Xem bảng 4.1 | datafiles.chinhphu.vn; dap.ctu.edu.vn (bản thứ 2) | Chính phủ | non-AI, 2 bản |
| V02 | Địa hình + tên riêng | [HIGH CONFIDENCE] | "biển Cửa Lò, chợ Bến Thành, sông Vàm Cỏ, vịnh Hạ Long" / "Cửa Lò, Vũng Tàu…" | datafiles.chinhphu.vn | Chính phủ | non-AI, gốc |
| V03 | Chức vụ: quy tắc lệch ví dụ | [CONFIRMED] | "Viết hoa tên chức vụ, học vị nếu đi liền với tên người cụ thể. Ví dụ: Chủ tịch Quốc hội, Thủ tướng Chính phủ…" | dap.ctu.edu.vn; datafiles.chinhphu.vn | Chính phủ | non-AI |
| V04 | NĐ 78/187 khác NĐ 30 | [HIGH CONFIDENCE] | Viết hoa "sau dấu hai chấm trong ngoặc kép", đầu khoản, điểm; "Nhà nước (chỉ tên riêng…)"; "tỉnh Ninh Bình…; phường Ba Đình" | xaydungchinhsach.chinhphu.vn; luatvietnam.vn | Chính phủ | non-AI, bản sao |
| V05 | Sách giáo khoa: tên dân tộc, thiên thể | [HIGH CONFIDENCE] | QĐ 07/2003: Ê-đê, Ba-na (gạch nối); QĐ 1989: Mặt Trời, Trái Đất; Sêrêpôk | vbpl.vn; luatvietnam.vn | Bộ GD&ĐT | non-AI |
| V06 | Tiêu đề: viết hoa kiểu câu hay Title Case | [ASSESSED] | Microsoft tr. 24 so với tr. 28; Mozilla cấm; Apple, Netflix có Title Case | download.microsoft.com; mozilla-l10n.github.io; support.apple.com | hãng | non-AI, mâu thuẫn |
| S01 | Dấu phẩy thập phân | [CONFIRMED] | "phải sử dụng dấu phẩy (,) không sử dụng dấu chấm (.) Ví dụ: 245,12 mm" | luatvietnam.vn (NĐ 86/2012, Phụ lục V); QĐ 1989, Điều 11; VBHN 41 | Chính phủ; Quốc hội | non-AI |
| S02 | Hàng nghìn: 3 kiểu | [ASSESSED] | Kế toán `.` (bắt buộc); QĐ 1989 `1 000; 34 456`; BIPM "Neither dots nor commas…"; CLDR `group "."`; VSQI "216,000 VNĐ" | vbpl.vn; luatvietnam.vn; bipm.org; cldr-json; vsqi.gov.vn | nhiều | non-AI, range |
| S03 | Số cách ký hiệu đơn vị; °C | [CONFIRMED] | "giữa hai thành phần này phải cách nhau một dấu cách. Ví dụ: 22 m"; "15 °C (không viết là 15°C…)"; tên đơn vị chữ thường | luatvietnam.vn (NĐ 86/2012) | Chính phủ | non-AI, bản sao |
| S04 | % | [ASSESSED] | CLDR `#,##0%`; Microsoft "no space between number and %"; BIPM "a space separates the number and the symbol %" | cldr-json; microsoft; bipm.org | nhiều | non-AI, mâu thuẫn |
| S05 | Đơn vị tiền | [CONFIRMED] | "là "Đồng", ký hiệu quốc gia là "đ", ký hiệu quốc tế là "VND"" | vanban.chinhphu.vn (Luật 46/2010, Điều 16); vbpl.vn (VBHN 41, Điều 10) | Quốc hội | non-AI, gốc |
| S06 | "VNĐ" không có trong luật; ₫ là ký tự kỹ thuật | [ASSESSED] | Hai luật trên chỉ ghi "đ", "VND"; ₫ = U+20AB; CLDR `1.234.567 ₫` | unicode.org; cldr-json; Node Intl | nhiều | suy luận + dữ liệu |
| S07 | Ngày | [CONFIRMED] | NĐ 30: "ngày nhỏ hơn 10 và tháng 1, 2 phải ghi thêm số 0"; QĐ 1989: "20-11-2017" / "20/11/2017", "mỗi bài viết và tài liệu phải sử dụng một cách viết thống nhất"; CLDR `d/M/yy` | dap.ctu.edu.vn; luatvietnam.vn; Node Intl | nhiều | non-AI |
| S08 | Giờ | [LOW CONFIDENCE] | CLDR `HH:mm`; "14 giờ 30 phút" trong văn bản pháp luật chỉ thấy qua snippet | cldr-json; vi.wikipedia.org | | thứ cấp |
| S09 | Số đếm bằng chữ | [HIGH CONFIDENCE] | Microsoft: "There is no specific rule…"; Netflix: 1–10 viết chữ (riêng phụ đề) | microsoft; netflixstudios.com | hãng | non-AI |
| D01 | Không có quy phạm về dấu câu | [HIGH CONFIDENCE] | QĐ 1989 Điều 1–11: 0 lần "dấu câu"; không thấy văn bản khác | luatvietnam.vn | | phủ định |
| D02 | Microsoft: dấu câu, khoảng trắng | [CONFIRMED] | "Please do not use comma before "và" and "hoặc"."; "There is a non-breaking space between number and unit."; "The hyphen should not be used when translating into Vietnamese." | download.microsoft.com (vie-vnm-StyleGuide.pdf) | Microsoft | non-AI, gốc |
| D03 | Mozilla | [HIGH CONFIDENCE] | "Dấu ba chấm là một ký tự (… U+2026)"; "Cố gắng chuyển câu bị động tiếng Anh thành câu chủ động tiếng Việt." | mozilla-l10n.github.io | cộng đồng Mozilla (2019) | non-AI |
| D04 | Gạch nối có cách trong văn bản luật | [HIGH CONFIDENCE] | Luật 64/2025: "kinh tế - xã hội" 14 lần có cách, 0 lần liền; NĐ 187: 2/0; NĐ 30: "chính trị - xã hội" | bản sao chinhphu.vn, luatvietnam.vn | Quốc hội; Chính phủ | đếm cục bộ |
| M01 | TCVN 6909:2001 | [HIGH CONFIDENCE] | "phù hợp với ISO/IEC 10646-1:2000 và UNICODE 3.0"; có cả 2 dạng; không chọn | vietunicode.sourceforge.net (bản quét) | Bộ KH&CN | non-AI, bản quét không chính thức |
| M02 | Phông chữ + bộ mã trong thể thức | [CONFIRMED] | "Phông chữ tiếng Việt Times New Roman, bộ mã ký tự Unicode theo Tiêu chuẩn Việt Nam TCVN 6909:2001, màu đen." | NĐ 30 (2 bản); NĐ 78; HD 05 PDF | Chính phủ; Đảng | non-AI |
| M03 | Khuyến nghị NFC | [CONFIRMED] | W3C: "Content authors SHOULD use Unicode Normalization Form C (NFC)…"; UAX #15 nhắc lại | w3.org; unicode.org | W3C; Unicode | non-AI (W3C là bản nháp) |
| M04 | Hai kiểu dấu, hai dạng mã là chuỗi khác nhau | [CONFIRMED] | `hòa` = 68 f2 61 ≠ `hoà` = 68 6f e0; "Việt": NFC 4 ký tự, NFD 6 ký tự | chạy cục bộ (Python, 2 agent + controller) | | thực nghiệm |
| M05 | Bộ gõ mặc định kiểu cũ | [HIGH CONFIDENCE] | OpenKey `vUseModernOrthography = 0`; fcitx-unikey `ModernStyle DefaultValue=False`; sổ tay UniKey: "kiểu mới được coi là đúng chính tả" | github.com/tuyenvm/OpenKey; github.com/fcitx; unikey.org | tác giả bộ gõ | non-AI, mã nguồn |
| B01 | CLDR locale vi | [CONFIRMED] | `"decimal": ","`, `"group": "."`; `#,##0.00 ¤` (NBSP); VND 0 chữ số lẻ | raw.githubusercontent.com/unicode-org/cldr-json; Node Intl | Unicode | non-AI, dữ liệu gốc |
| B02 | Microsoft: giọng văn, xưng hô, thuật ngữ | [HIGH CONFIDENCE] | "clear, friendly and concise"; "You: Bạn, anh, chị"; giữ OK, tab, từ viết tắt | download.microsoft.com | Microsoft | non-AI |
| B03 | Microsoft: tránh dịch từng chữ | [CONFIRMED] | "To achieve a fluent translation, avoid word-to-word translation." | download.microsoft.com | Microsoft | non-AI |
| B04 | Sắc thái được/bị | [LOW CONFIDENCE] | "được" [+positive], "bị" [+negative] | i-jte.org (2022) | học thuật, tác giả sinh viên | non-AI |
| B05 | Lỗi tiếng Việt do AI sinh | [BLIND SPOT] | Không có nghiên cứu có tên tác giả | | | |
| T01 | Thói quen trong báo cáo của repo | [CONFIRMED] | 31 file: kiểu mới 198 / cũ 48; kỹ 58, lý 119, Mỹ 32; kĩ, lí 0; tỷ 11 / tỉ 11 | đếm cục bộ | repo | dữ liệu nội bộ |
| T02 | Thói quen trong skill viet-chuyen-nghiep | [CONFIRMED] | 44 file: kiểu cũ 92 / mới 6; kỹ 53, lý 76 | đếm cục bộ | skill | dữ liệu nội bộ |

Claim bị loại vì sai hoặc không có căn cứ (chi tiết ở nhật ký, mục X):
- "NĐ 30 đã bị sửa bởi NĐ 05/2025";
- "CV 4168/BNV ngày 23/6/2026";
- "TCVN 6909 thừa nhận hai phương pháp… giá trị pháp lý kỹ thuật như nhau";
- "Quyết định 241/QĐ";
- nhận định trong phiên này rằng văn bản nhà nước 2026 viết kiểu "khóa, cấp ủy" (đúng với văn bản Đảng, sai khi khái quát cho văn bản Chính phủ).

---

## 6. Quy ước cho agent viết tiếng Việt (đã chốt Q4–Q7 ngày 03/10/2026)

Phạm vi áp dụng: báo cáo, tài liệu, văn bản, slide do agent viết cho bạn. Mỗi luật ghi căn cứ.

1. **Mã hóa:** lưu và xử lý ở Unicode dựng sẵn (NFC). Chuẩn hóa NFC trước khi so khớp hay tìm kiếm. (M01–M04)
2. **Viết hoa:**
   - Theo NĐ 30, Phụ lục II (bảng 4.1).
   - Tiêu đề, heading, tiêu đề slide, nút: chỉ viết hoa chữ đầu và tên riêng. Viết *Kế hoạch triển khai quý 4*, không viết *Kế Hoạch Triển Khai Quý 4*. (V01, V06)
3. **Dấu thanh:** kiểu cũ (*hòa, hóa, khỏe, thủy, tùy, ủy, xóa, khóa*), theo quyết định của bạn ở Q4.
   - Trích nguyên văn và tên riêng thì giữ như nguồn.
   - Khi tìm kiếm, phải khớp cả hai kiểu.
   - Lưu ý: "quý", "quỹ", "quỳ" không đổi, vì "qu" là phụ âm đầu.
   - (C01, C05, M04, M05; Q4)
4. **i/y:** dùng y (*kỹ, lý, Mỹ, tỷ, hy vọng, kỷ niệm*); viết "quy", không viết "qui". Tên riêng giữ đúng cách chủ nhân viết. Tài liệu cho trường phổ thông thì theo QĐ 1989 (*kĩ, lí*). (C02, C04; Q5)
5. **Số:**
   - Thập phân dùng dấu phẩy: *81,3 triệu*.
   - Hàng nghìn dùng dấu chấm: *1.234.567*.
   - Không dùng dấu phẩy cho hàng nghìn.
   - (S01, S02; Q6)
6. **Đơn vị:**
   - Ký hiệu đặt sau số, cách một dấu cách: *22 m, 250 GB, 15 °C*. Độ góc viết liền: *30°*.
   - Phần trăm viết liền: *26%*.
   - Tên đơn vị viết thường; không trộn tên với ký hiệu (không viết *km/giờ*).
   - (S03, S04)
7. **Tiền:**
   - Văn xuôi: *1.234.567 đồng*, *3,5 tỷ đồng*.
   - Bảng: *đ* hoặc *VND*.
   - Không dùng *VNĐ*. Chỉ để *₫* khi hệ thống tự sinh.
   - (S05, S06; Q7)
8. **Ngày:**
   - Văn xuôi và bảng: *03/10/2026*.
   - Văn bản gửi cơ quan nhà nước: *ngày 03 tháng 10 năm 2026* (số 0 trước ngày < 10 và tháng 1, 2).
   - Khoảng ngày: *15/10/2017 - 20/11/2017*.
   - Một tài liệu chỉ dùng một kiểu.
   - (S07)
9. **Giờ:** 24 giờ: *14:30*. (S08, độ tin thấp)
10. **Tên nước ngoài và thuật ngữ:**
    - Tên chữ Latin giữ nguyên dạng: *New York, Victor Hugo*. Tên Hán Việt đã quen giữ nguyên: *Hy Lạp*.
    - Thuật ngữ quốc tế giữ nguyên dạng, định nghĩa ở lần đầu.
    - Văn bản theo NĐ 30 có thể dùng phiên âm có gạch nối.
    - (C07–C09)
11. **Viết tắt:** lần đầu ghi đầy đủ, chữ tắt trong ngoặc đơn ngay sau. Không viết tắt trong tiêu đề. (L10: NĐ 78, Điều 60.4; L11: HD 05, mục 6.1.3)
12. **Dấu câu:**
    - Sát chữ trước, cách chữ sau.
    - Ngoặc mở: cách trước, sát sau.
    - Không đặt dấu phẩy trước *và*, *hoặc*.
    - Gạch nối giữa hai danh từ ngang hàng có cách: *kinh tế - xã hội*.
    - (D02, D04)
13. **Văn phong:**
    - Không dịch từng chữ.
    - Ưu tiên câu chủ động; dùng *được/bị* đúng sắc thái.
    - Tài liệu hướng tới người dùng thì xưng *bạn*. Báo cáo trang trọng thì không xưng hô.
    - (B02–B04)
14. **Văn bản gửi cơ quan nhà nước:** áp dụng đủ NĐ 30: Times New Roman, cỡ 13–14, lề trái 30–35 mm, ngày tháng có số 0, viết hoa theo Phụ lục II. (L08, M02, S07)
15. **Quảng cáo, nhãn, tên doanh nghiệp:**
    - Agent gắn cờ cho người duyệt: tỷ lệ chữ nước ngoài (quảng cáo ≤ 3/4; nhãn không lớn hơn; tên doanh nghiệp nhỏ hơn) và yêu cầu "trong sáng".
    - Vi phạm có phạt. (N01–N06)

## 7. Đối chiếu skill viet-chuyen-nghiep (chỉ báo cáo, không sửa)

| Quy tắc trong skill | Căn cứ tìm được | Kết luận |
|---|---|---|
| Không Title Case, "Tham chiếu NĐ 30/2020" (`review/capitalization.md`) | NĐ 30 chỉ viết hoa đầu câu và tên riêng; Microsoft tr. 24, Mozilla | Có căn cứ. Nên ghi rõ NĐ 30 không nói trực tiếp về tiêu đề |
| "sông Hồng", không "Sông Hồng" | NĐ 30: "sông Vàm Cỏ, vịnh Hạ Long" | Đúng |
| "Thủ đô Hà Nội", "Thành phố Hồ Chí Minh" | NĐ 30: "Trường hợp viết hoa đặc biệt" | Đúng |
| Chức danh viết thường khi đứng một mình, viết hoa khi kèm tên người hoặc tổ chức | NĐ 30: "nếu đi liền với tên người cụ thể", ví dụ lại kèm tên tổ chức | Khớp ví dụ của NĐ 30. Vế "viết thường khi đứng một mình" là suy luận |
| Viết hoa sau dấu hai chấm khi trích dẫn | NĐ 78/187: viết hoa "sau dấu hai chấm trong ngoặc kép" | Có căn cứ (văn bản pháp luật) |
| Dấu câu sát trước, cách sau; quy tắc ngoặc đơn | Microsoft tr. 34, 40 | Có căn cứ (chuẩn ngành) |
| Không dấu phẩy Oxford | Microsoft tr. 34 | Có căn cứ |
| **Gạch nối không cách: "kinh tế-xã hội"** | Luật 64/2025 viết "kinh tế - xã hội" 14/14 lần có cách; NĐ 30 "chính trị - xã hội" | **Lệch** cách viết của văn bản nhà nước |
| Không dùng em-dash (đã ghi là quy ước nội bộ) | Không có quy phạm; Microsoft tr. 36 vẫn bàn về en dash, em dash | Đúng là quy ước nội bộ |
| "TP. HCM" trong ví dụ | HD 05 cho viết tắt "TP (thành phố)" ở địa danh văn bản Đảng; NĐ 78: viết tắt phải ghi đầy đủ ở lần đầu | Nên ghi đầy đủ lần đầu |
| **Thiếu luật:** dấu thanh, i/y, số, đơn vị, tiền, ngày, Unicode | Mục 6, luật 1, 3–9 | Khoảng trống |
| **Kiểu dấu trong chính skill:** cũ 92 / mới 6 | Quyết định Q4: kiểu cũ. Báo cáo của bạn: mới 198 / cũ 48 | Skill đã khớp quyết định. Báo cáo cũ thì lệch (Q9) |

## 8. Điểm mù và câu còn mở

1. **QĐ 1989:** không tìm thấy bản gốc trên vbpl.vn, moet.gov.vn, chinhphu.vn; chỉ có bản sao. Hiệu lực QĐ 240 và QĐ 1989: chưa kiểm (L06).
2. **Quan hệ QĐ 07/2003 và QĐ 1989 về tên nước ngoài:** QĐ 07/2003 phiên âm có gạch nối ở mọi cấp, QĐ 1989 chỉ ở tiểu học. QĐ 1989 không có điều khoản bãi bỏ. Chưa có nguồn phân định.
3. **NĐ 30 sau 29/07/2026:** không thấy văn bản sửa. CV 1826/BNV-CVT&LTNN (03/03/2026) trả lời kiến nghị về NĐ 30 chưa mở được (thuvienphapluat chặn).
4. **Đếm dấu thanh và i/y:** làm trên bản sao, có thể khác bản ký số. Chưa có khảo sát báo chí sau 2020.
5. **Tiêu chuẩn:** TCVN 5712:1993 không có nguồn đọc được. TCVN 7870-1 phải trả phí, chưa đọc.
6. **Dấu câu:** chưa đọc giáo trình ngữ pháp (Diệp Quang Ban) và chương trình Ngữ văn 2018.
7. **Bộ gõ:** chưa biết mặc định của UniKey Windows, EVKey và bộ gõ Telex có sẵn trên macOS. Cách tự kiểm: gõ `hoaf` trong TextEdit.
8. **Lỗi tiếng Việt do AI sinh:** không có nghiên cứu có tên tác giả (B05).
9. **Sắp đổi:** Luật Đo lường đang sửa (Chính phủ thống nhất dự án ngày 23/06/2026); Luật Bảo vệ quyền lợi người tiêu dùng dự kiến trình Quốc hội 10/2026.
10. **Chế tài chưa kiểm:** nhãn hàng, tên doanh nghiệp, đấu thầu (N09 chưa đối chiếu bản gốc).
11. **"bác sĩ" hay "bác sỹ":** luật 4 chưa quyết vì chưa đếm tần suất.

## 9. Cờ human-review (3 câu cho chuyên gia pháp lý hoặc ngôn ngữ)

1. QĐ 1989/QĐ-BGDĐT và QĐ 240/QĐ còn hiệu lực không? QĐ 1989 có thay QĐ 07/2003 về cách viết tên nước ngoài trong sách giáo khoa không?
2. Ngoài kế toán và sách giáo khoa, có quy định nào về dấu phân cách hàng nghìn cho văn bản của cơ quan nhà nước không?
3. Có văn bản nào quy định cách ghi giờ trong văn bản hành chính ("14:30" hay "14 giờ 30") không? Luật 9 ở mục 6 hiện chỉ dựa trên chuẩn kỹ thuật (S08).

## 10. Chỗ trống cần điền

Q1–Q3 đã trả lời ở đầu phiên: mục đích là hướng dẫn agent; điểm tranh cãi thì đề xuất một quy ước; skill chỉ đối chiếu, không sửa.

| Câu | Lựa chọn | Đề xuất | Quyết định (03/10/2026) |
|---|---|---|---|
| Q4. Dấu thanh | A. *hoà, thuỷ, khoẻ* · B. *hòa, thủy, khỏe* | A | **B** |
| Q5. i/y | A. *kỹ, lý, Mỹ, tỷ* · B. *kĩ, lí, Mĩ, tỉ* (QĐ 1989) | A | **A** |
| Q6. Hàng nghìn | A. dấu chấm *1.234.567* · B. khoảng trắng *1 234 567* | A | **A** |
| Q7. Tiền | A. *đồng / đ / VND*, bỏ *VNĐ* · B. giữ *VNĐ* | A | **A** |
| Q8. Bước tiếp | A. Chuyển mục 6 thành file quy tắc cho agent (nơi đặt do bạn chọn) · B. Dừng ở báo cáo | A | **A**: thêm vào skill viet-chuyen-nghiep, file `review/standards.md` |
| Q9. Báo cáo cũ (khoảng 200 từ kiểu mới, 11 chữ "tỉ") | A. Để nguyên, chỉ áp quy ước cho tài liệu mới · B. Chuyển hết sang kiểu cũ và "tỷ" | A (báo cáo là bản ghi theo thời điểm) | **A** |
