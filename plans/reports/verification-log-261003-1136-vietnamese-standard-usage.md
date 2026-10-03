# Verification log — Dùng tiếng Việt đúng chuẩn

Ngày: 03/10/2026, 11:00–11:36 (UTC+7).
Phương pháp: kiem-chung-thong-tin (TKC × ACV), domain chính LAW, kit phụ STATISTICS cho phần đếm. Không có `mr`, nên vòng 1–3 chấm tay.

- **Vòng 1 — Coverage:** 9 câu thiết yếu.
  - Đủ: khung pháp lý, chính tả, viết hoa, số, tiền, mã hóa, nghĩa vụ chuyên ngành.
  - Thiếu: dấu câu (không có quy phạm), lỗi do AI sinh (không có nguồn).
- **Vòng 2 — Usability:** chỉ giữ claim có URL, ngày và trích nguyên văn.
- **Vòng 3 — Independence:** gom origin theo cơ quan ban hành.
  - Bản sao toàn văn trên luatvietnam.vn, trang tin của Chính phủ hay trang trường học vẫn quy về cùng origin là cơ quan ban hành.
  - Không có nguồn AI-search nào được dùng làm bằng chứng.
- **Vòng 4 — Truth:** chạy cho từng claim. Câu hỏi pháp lý cố định cho mọi claim: còn hiệu lực không, áp dụng cho ai, cấp văn bản nào, đọc bản gốc hay bản sao.
- **Vòng 5 — Gap:** chạy 1 lượt, gồm (a) dự thảo sửa NĐ 30, (b) văn bản thay NĐ 86/2012. Cả hai: không thấy. Dừng vì đã `sufficient`.

Packet: [findings-packet-261003-1136-vietnamese-standard-usage.md](findings-packet-261003-1136-vietnamese-standard-usage.md)

**Ký hiệu người kiểm:**
- **CTL** = controller tự mở.
- **AG-A / AG-B / AG-C / AG-D** = agent cụm pháp lý-chính tả / hành chính-mã hóa / số-tiền-dấu câu-nghĩa vụ / bản địa hóa.
- **S** = chỉ qua kết quả tìm kiếm.

---

Claim L01: "Hiến pháp 2013, Điều 5.3: Ngôn ngữ quốc gia là tiếng Việt."
Kết luận: Đúng · Mức tin cậy: Cao · Tính đến: 03/10/2026
→ Tag: [CONFIRMED]
Bằng chứng:
- AG-A đọc toàn văn trên xaydungchinhsach.chinhphu.vn.
- AG-C đọc VBHN 52/VBHN-VPQH (PDF trên datafiles.chinhphu.vn).
- NQ 203/2025/QH15 chỉ sửa Điều 9, 10, 84, 110, 111; không đụng Điều 5.
Diễn giải thay thế: Điều 5 nói ngôn ngữ nào, không nói cách viết. Không được dùng làm căn cứ cho quy tắc chính tả.
Yếu tố bất định: Chưa đọc hết phần cuối NQ 203.
Nguồn: chinhphu.vn · non-AI · primary_origin: Quốc hội
Independence: max_tag=[CONFIRMED] · origins: Quốc hội (2 bản độc lập)
---

Claim L02: "Việt Nam chưa có luật ngôn ngữ hay luật tiếng Việt (đến 10/2026)."
Kết luận: Đúng · Mức tin cậy: Vừa · Tính đến: 03/10/2026
→ Tag: [HIGH CONFIDENCE]
Bằng chứng:
- daibieunhandan.vn (2021): "vẫn chưa có văn bản luật nào…".
- GS Nguyễn Văn Hiệp (2020) gọi luật này là "mơ ước".
- Chương trình lập pháp 2026, qua bản tóm tắt NQ 105/2025/UBTVQH15 và bản điều chỉnh: 0 lần chữ "ngôn ngữ".
- Bộ VHTTDL trả lời cử tri (08/2024) không nhắc luật.
Diễn giải thay thế: Có thể có dự thảo trong nội bộ mà chưa công bố.
Yếu tố bất định: Đây là bằng chứng phủ định. Chưa đọc bản gốc NQ 105.
Nguồn: daibieunhandan.vn · baohaiphong.vn · luatvietnam.vn · bvhttdl.gov.vn · non-AI
Independence: max_tag=[HIGH CONFIDENCE] · origins: báo Quốc hội, Viện Ngôn ngữ học, UBTVQH (qua tóm tắt)
---

Claim L03: "Luật Giáo dục 2019, Điều 11.1: Tiếng Việt là ngôn ngữ chính thức dùng trong cơ sở giáo dục."
Kết luận: Đúng · Mức tin cậy: Cao · Tính đến: 03/10/2026
→ Tag: [CONFIRMED]
Bằng chứng: AG-A đọc bản luatvietnam.vn; AG-C đọc VBHN 72/VBHN-VPQH (03/2026, chinhphu.vn). Câu chữ khớp nhau.
Diễn giải thay thế: Chính phủ quy định ngoại lệ dạy bằng tiếng nước ngoài.
Yếu tố bất định: Chế tài chưa kiểm.
Nguồn: datafiles.chinhphu.vn · luatvietnam.vn · non-AI
Independence: max_tag=[CONFIRMED] · origins: Quốc hội
---

Claim L04: "Luật 64/2025/QH15, Điều 7.1: ngôn ngữ trong VBQPPL là tiếng Việt, chính xác, phổ thông, thống nhất."
Kết luận: Đúng · Mức tin cậy: Cao · Tính đến: 03/10/2026
→ Tag: [CONFIRMED]
Bằng chứng: AG-A và AG-B đọc độc lập toàn văn trên xaydungchinhsach.chinhphu.vn. Hiệu lực 01/04/2025 (Điều 71).
Diễn giải thay thế: Luật chỉ nêu nguyên tắc; chi tiết nằm ở NĐ 78/2025.
Yếu tố bất định: Luật 87/2025/QH15 (sửa đổi) chưa mở.
Nguồn: chinhphu.vn · non-AI
Independence: max_tag=[CONFIRMED] · origins: Quốc hội
---

Claim L05: "QĐ 1989/QĐ-BGDĐT (25/05/2018) chỉ áp dụng cho người làm chương trình, sách giáo khoa phổ thông và tổ chức, cá nhân liên quan."
Kết luận: Đúng · Mức tin cậy: Cao · Tính đến: 03/10/2026
→ Tag: [CONFIRMED]
Bằng chứng: CTL đọc Điều 1.2 trên luatvietnam.vn; AG-A đối chiếu bản scribd, khớp.
Diễn giải thay thế: Cụm "tổ chức, cá nhân liên quan" có thể hiểu rộng. Nhưng tên văn bản giới hạn ở "chương trình, sách giáo khoa giáo dục phổ thông".
Yếu tố bất định: Không tìm thấy bản gốc trên vbpl.vn, moet.gov.vn, chinhphu.vn.
Nguồn: luatvietnam.vn · scribd.com · non-AI (bản sao)
Independence: max_tag=[CONFIRMED] · origins: Bộ GD&ĐT (2 bản sao)
---

Claim L06: "QĐ 240/1984, QĐ 07/2003, QĐ 1989/2018 còn hiệu lực."
Kết luận: Phức tạp hơn claim · Mức tin cậy: Thấp–Vừa · Tính đến: 03/10/2026
→ Tag: [ASSESSED]
Bằng chứng:
- QĐ 07/2003: vbpl.vn ghi "Còn hiệu lực" (cập nhật 01/04/2026).
- QĐ 240 và QĐ 1989: luatvietnam.vn ghi "Đang cập nhật".
- TT 47/2026/TT-BGDĐT bãi bỏ 11 văn bản; cả ba không có trong danh sách.
- Bộ GD&ĐT (2020) vẫn liệt kê cả ba văn bản.
Diễn giải thay thế: QĐ 1989 có thể đã thay ngầm QĐ 07/2003 về tên nước ngoài (hai văn bản mâu thuẫn).
Yếu tố bất định: Trạng thái hiệu lực trên thuvienphapluat bị chặn.
Nguồn: vbpl.vn · luatvietnam.vn · suckhoedoisong.vn · giaoducthoidai.vn · non-AI
Independence: max_tag=[ASSESSED] · origins: Bộ GD&ĐT, CSDL quốc gia
---

Claim L07: "QĐ 240/QĐ (05/03/1984) áp dụng cho sách giáo khoa, báo và văn bản của ngành giáo dục; toàn văn không có quy tắc i/y."
Kết luận: Đúng · Mức tin cậy: Vừa · Tính đến: 03/10/2026
→ Tag: [HIGH CONFIDENCE]
Bằng chứng: AG-A đọc toàn văn trên luatvietnam.vn; tìm "kỹ", "hòa", "dấu thanh": 0 kết quả.
Diễn giải thay thế: Tuổi Trẻ (2020) nói QĐ 240 có quy định i/y. Xem C03.
Yếu tố bất định: Bản sao có thể thiếu phụ lục.
Nguồn: luatvietnam.vn · non-AI
Independence: max_tag=[HIGH CONFIDENCE] · origins: Bộ Giáo dục
---

Claim L08: "NĐ 30/2020 bắt buộc với cơ quan, tổ chức nhà nước và doanh nghiệp nhà nước; tổ chức kinh tế không bắt buộc nhưng có thể căn cứ."
Kết luận: Đúng · Mức tin cậy: Cao · Tính đến: 03/10/2026
→ Tag: [CONFIRMED]
Bằng chứng:
- AG-B đọc Điều 2 trên bản ký số (OCR, đối chiếu ảnh trang 1).
- CTL đọc bài Bộ Nội vụ trả lời trên baochinhphu.vn (22/12/2020): "không xác định các tổ chức kinh tế là đối tượng bắt buộc áp dụng".
Diễn giải thay thế: Đối tác nhà nước có thể yêu cầu theo thể thức NĐ 30 qua hợp đồng.
Yếu tố bất định: Không có.
Nguồn: datafiles.chinhphu.vn · baochinhphu.vn · non-AI
Independence: max_tag=[CONFIRMED] · origins: Chính phủ, Bộ Nội vụ
---

Claim L09: "NĐ 30/2020 còn hiệu lực đến 10/2026; chưa bị sửa hay thay."
Kết luận: Đúng · Mức tin cậy: Vừa · Tính đến: 03/10/2026
→ Tag: [HIGH CONFIDENCE]
Bằng chứng:
- vbpl.vn: "Còn hiệu lực" (S, cập nhật 01/04/2026).
- QĐ 144/QĐ-BNV (02/2026): NĐ 30 không có trong danh mục văn bản hết hiệu lực năm 2025.
- VTV (29/07/2026): Bộ Nội vụ vẫn dẫn NĐ 30.
- CTL: trang xaydungchinhsach.chinhphu.vn (09/2026) dẫn NĐ 30 trong mục "Tham khảo thêm"; NĐ 347/2026 không sửa NĐ 30.
Diễn giải thay thế: CV 1826/BNV (03/03/2026) có thể báo hiệu kế hoạch sửa (chưa mở được).
Yếu tố bất định: Danh mục "hết hiệu lực một phần" chưa mở.
Nguồn: vbpl.vn · ninhbinh.gov.vn · vtv.vn · chinhphu.vn · non-AI
Independence: max_tag=[HIGH CONFIDENCE] · origins: CSDL quốc gia, Bộ Nội vụ, báo
---

Claim L10: "NĐ 78/2025 (01/04/2025) thay NĐ 34/2016, 154/2020, 59/2024; NĐ 187/2025 (01/07/2025) thay Phụ lục I của NĐ 78."
Kết luận: Đúng · Mức tin cậy: Vừa · Tính đến: 03/10/2026
→ Tag: [HIGH CONFIDENCE]
Bằng chứng: AG-B đọc Điều 78.2 của NĐ 78 (bản xaydungchinhsach) và Điều 3.3.a của NĐ 187 (bản luatvietnam).
Diễn giải thay thế: Không có.
Yếu tố bất định: Chưa đọc bản ký số NĐ 187.
Nguồn: chinhphu.vn · luatvietnam.vn · non-AI (bản sao)
Independence: max_tag=[HIGH CONFIDENCE] · origins: Chính phủ
---

Claim L11: "HD 05-HD/VPTW (27/05/2026) thay HD 36-HD/VPTW; loại trừ doanh nghiệp; Times New Roman + TCVN 6909:2001; ngày dưới 10 và tháng dưới 3 thêm số 0."
Kết luận: Đúng · Mức tin cậy: Cao · Tính đến: 03/10/2026
→ Tag: [CONFIRMED]
Bằng chứng: CTL đọc bài tóm tắt trên chinhphu.vn và tải PDF toàn văn 36 trang (pdftotext).
- Mục 4.2.2: "Ngày dưới 10 và tháng dưới 3 phải thêm số không (0) phía trước", ví dụ "Hà Nội, ngày 03 tháng 02 năm 2026".
- Mục IV.1: phông chữ.
- Mục 6.1.3: viết tắt.
- Không có phần viết hoa (tìm "viết hoa": 0).
AG-B xác nhận qua bài tóm tắt.
Diễn giải thay thế: Bài báo ghi HD 36 "ngày 04/3/2018"; các bản khác ghi 03/04/2018. Coi là lỗi gõ của báo.
Yếu tố bất định: Không có.
Nguồn: xdcs.cdnchinhphu.vn (PDF) · non-AI
Independence: max_tag=[CONFIRMED] · origins: Văn phòng Trung ương Đảng
---

Claim L12: "QĐ 72/2002/QĐ-TTg: từ 01/01/2003 dùng TCVN 6909:2001 trong trao đổi thông tin điện tử giữa tổ chức Đảng và Nhà nước."
Kết luận: Đúng · Mức tin cậy: Vừa · Tính đến: 03/10/2026
→ Tag: [HIGH CONFIDENCE]
Bằng chứng: AG-B đọc Điều 1 (luatvietnam.vn, bản sao).
Diễn giải thay thế: Không có.
Yếu tố bất định: Hiệu lực hiện tại chưa kiểm.
Nguồn: luatvietnam.vn · non-AI
Independence: max_tag=[HIGH CONFIDENCE] · origins: Thủ tướng
---

Claim L13: "TT 05/2026/TT-BNG (30/06/2026) hướng dẫn dịch Quốc hiệu, tên cơ quan, chức danh sang tiếng Anh."
Kết luận: Đúng · Mức tin cậy: Vừa · Tính đến: 03/10/2026
→ Tag: [HIGH CONFIDENCE]
Bằng chứng: CTL đọc phần đầu và Điều 1–2 trên luatvietnam.vn.
Diễn giải thay thế: Có thể thay TT 03/2009/TT-BNG (chưa đọc điều khoản thay thế).
Yếu tố bất định: Chưa đọc phụ lục.
Nguồn: luatvietnam.vn · non-AI
Independence: max_tag=[HIGH CONFIDENCE] · origins: Bộ Ngoại giao
---

Claim L14: "Viện Ngôn ngữ học không có thẩm quyền ban hành chuẩn; chỉ nghiên cứu, làm từ điển, tư vấn."
Kết luận: Đúng · Mức tin cậy: Vừa · Tính đến: 03/10/2026
→ Tag: [HIGH CONFIDENCE]
Bằng chứng: AG-A đọc trang chức năng nhiệm vụ (tóm tắt QĐ 576/QĐ-KHXH, 17/04/2025).
Diễn giải thay thế: Không có.
Yếu tố bất định: Ảnh hưởng của QĐ 12-QĐ/TW (30/03/2026) chưa kiểm.
Nguồn: vienngonnguhoc.vass.gov.vn · non-AI
Independence: max_tag=[HIGH CONFIDENCE] · origins: Viện Hàn lâm KHXH
---

Claim L15: "2017: Bộ GD&ĐT và Chính phủ không có chủ trương cải tiến chữ viết (đề xuất của PGS Bùi Hiền)."
Kết luận: Đúng · Mức tin cậy: Vừa · Tính đến: 03/10/2026
→ Tag: [HIGH CONFIDENCE]
Bằng chứng: AG-A đọc daibieunhandan.vn (01/12/2017) và dantri.com.vn (01/12/2017). GS Nguyễn Văn Lợi phản biện trên vietnamnet.vn.
Diễn giải thay thế: Không có.
Yếu tố bất định: Không có.
Nguồn: daibieunhandan.vn · dantri.com.vn · vietnamnet.vn · non-AI
Independence: max_tag=[HIGH CONFIDENCE] · origins: báo (trích phát ngôn chính thức)
---

Claim N01: "Quảng cáo: khổ chữ nước ngoài không quá 3/4 khổ chữ tiếng Việt, đặt bên dưới."
Kết luận: Đúng · Mức tin cậy: Cao · Tính đến: 03/10/2026
→ Tag: [CONFIRMED]
Bằng chứng:
- AG-C đọc Luật 16/2012, Điều 18.2 (vanban.chinhphu.vn).
- CTL thấy chế tài khớp ở NĐ 87/2026, Điều 52.1.c: "khổ chữ nước ngoài vượt quá ba phần tư khổ chữ tiếng Việt".
Diễn giải thay thế: Khoản 1 có ngoại lệ (nhãn hiệu, khẩu hiệu, tên riêng…).
Yếu tố bất định: Chưa đọc được VBHN 88/2025 (PDF quét).
Nguồn: vanban.chinhphu.vn · luatvietnam.vn · non-AI
Independence: max_tag=[CONFIRMED] · origins: Quốc hội, Chính phủ
---

Claim N02: "Luật 75/2025/QH15 bổ sung: từ ngữ tiếng Việt trong quảng cáo phải giữ gìn sự trong sáng, rõ ràng, dễ hiểu (hiệu lực 01/01/2026)."
Kết luận: Đúng · Mức tin cậy: Vừa · Tính đến: 03/10/2026
→ Tag: [HIGH CONFIDENCE]
Bằng chứng: AG-A và AG-C đọc độc lập trên luatvietnam.vn (bài phân tích, toàn văn). CTL thấy chế tài khớp ở NĐ 87/2026, điểm b.
Diễn giải thay thế: Pháp luật "không quy định theo hướng liệt kê 'cấm dùng từ lóng' hay 'cấm sai chính tả'" (luatvietnam). Tiêu chí "trong sáng" do cơ quan xử phạt diễn giải.
Yếu tố bất định: Cách cơ quan xử phạt áp dụng thực tế.
Nguồn: luatvietnam.vn · non-AI (bản sao)
Independence: max_tag=[HIGH CONFIDENCE] · origins: Quốc hội
---

Claim N03: "NĐ 87/2026/NĐ-CP: phạt 5.000.000–10.000.000 đồng khi tiếng Việt trong quảng cáo không bảo đảm trong sáng; thay NĐ 38/2021; hiệu lực 15/05/2026."
Kết luận: Đúng · Mức tin cậy: Cao (nội dung) / Vừa (ngày hiệu lực) · Tính đến: 03/10/2026
→ Tag: [CONFIRMED]
Bằng chứng: CTL đọc điểm b khoản 1 và điều khoản bãi bỏ NĐ 38/2021 trên luatvietnam.vn; AG-C đọc cùng điều.
Diễn giải thay thế:
- Mức phạt cho cá nhân; tổ chức gấp đôi theo Điều 6.3 (chỉ AG-C đọc).
- Ngày hiệu lực lấy từ lamdong.dms.gov.vn (AG-C).
Yếu tố bất định: Chưa đọc bản ký số.
Nguồn: luatvietnam.vn · lamdong.dms.gov.vn · non-AI
Independence: max_tag=[CONFIRMED] · origins: Chính phủ
---

Claim N04: "NĐ 37/2026/NĐ-CP, Điều 39: nội dung bắt buộc trên nhãn phải ghi tiếng Việt; chữ ngôn ngữ khác không lớn hơn chữ tiếng Việt; NĐ 43/2017 và 111/2021 hết hiệu lực."
Kết luận: Đúng · Mức tin cậy: Cao · Tính đến: 03/10/2026
→ Tag: [CONFIRMED]
Bằng chứng: CTL và AG-C đọc Điều 39.1–2 và Điều 97.4 trên luatvietnam.vn.
- CTL kiểm thêm Điều 97.4: điều này bãi bỏ NĐ 13/2022 (văn bản sửa NĐ 86/2012), **không** bãi bỏ NĐ 86/2012.
Diễn giải thay thế: Không có.
Yếu tố bất định: Chế tài vi phạm nhãn chưa kiểm.
Nguồn: luatvietnam.vn · vanban.chinhphu.vn · non-AI
Independence: max_tag=[CONFIRMED] · origins: Chính phủ
---

Claim N05: "Luật Báo chí 126/2025/QH15 (hiệu lực 01/07/2026) cấm sử dụng ngôn ngữ làm biến dạng tiếng Việt dẫn đến hiểu sai; thay Luật 103/2016."
Kết luận: Đúng · Mức tin cậy: Cao · Tính đến: 03/10/2026
→ Tag: [CONFIRMED]
Bằng chứng:
- CTL đọc trên luatvietnam.vn: câu cấm nằm ở cuối khoản 7 Điều 8, ngay trước khoản 8 "Kích động bạo lực…".
- CTL đọc điều khoản hiệu lực có nhắc Luật 103/2016.
- AG-C đọc cùng văn bản.
Diễn giải thay thế: Điều cấm gắn với "nội dung tuyên truyền", không cấm lỗi chính tả nói chung.
Yếu tố bất định: NĐ 367/2026 (xử phạt báo chí) mới chỉ quét chữ, chưa đọc từng điều.
Nguồn: luatvietnam.vn · non-AI
Independence: max_tag=[CONFIRMED] · origins: Quốc hội
---

Claim N06: "Luật Doanh nghiệp, Điều 37.3: tên riêng dùng chữ cái tiếng Việt, F, J, Z, W, chữ số, ký hiệu; Điều 39.2: tên nước ngoài khổ chữ nhỏ hơn."
Kết luận: Đúng · Mức tin cậy: Vừa · Tính đến: 03/10/2026
→ Tag: [HIGH CONFIDENCE]
Bằng chứng: AG-C đọc VBHN 67/VBHN-VPQH (luatvietnam.vn).
Diễn giải thay thế: Không có.
Yếu tố bất định: Chế tài chưa kiểm.
Nguồn: luatvietnam.vn · non-AI
Independence: max_tag=[HIGH CONFIDENCE] · origins: Quốc hội
---

Claim N07: "Luật 19/2023/QH15, Điều 23.2: ngôn ngữ hợp đồng với người tiêu dùng là tiếng Việt."
Kết luận: Đúng · Mức tin cậy: Vừa · Tính đến: 03/10/2026
→ Tag: [HIGH CONFIDENCE]
Bằng chứng: AG-C đọc trên luatvietnam.vn.
Diễn giải thay thế: Có thể thỏa thuận thêm ngôn ngữ khác.
Yếu tố bất định: Luật sửa đổi dự kiến trình Quốc hội 10/2026.
Nguồn: luatvietnam.vn · tapchicongthuong.vn · non-AI
Independence: max_tag=[HIGH CONFIDENCE] · origins: Quốc hội
---

Claim N08: "Luật Kế toán (VBHN 41/VBHN-VPQH, 16/03/2026): chữ viết là tiếng Việt; dấu chấm sau hàng nghìn, triệu, tỷ; dấu phẩy sau hàng đơn vị; đơn vị tiền 'đ', 'VND'."
Kết luận: Đúng · Mức tin cậy: Cao · Tính đến: 03/10/2026
→ Tag: [CONFIRMED]
Bằng chứng: CTL đọc Điều 10.1 và 11.2 trên vbpl.vn; AG-C đọc cùng văn bản.
Diễn giải thay thế: Khoản 3 cho doanh nghiệp có công ty mẹ nước ngoài dùng kiểu ngược nếu có chú thích.
Yếu tố bất định: Không có.
Nguồn: vbpl.vn · non-AI (văn bản hợp nhất chính thức)
Independence: max_tag=[CONFIRMED] · origins: Văn phòng Quốc hội
---

Claim N09: "Luật Đấu thầu, Điều 12.1: ngôn ngữ đấu thầu trong nước là tiếng Việt."
Kết luận: Chưa đủ chứng cứ · Mức tin cậy: Thấp · Tính đến: 03/10/2026
→ Tag: [LOW CONFIDENCE]
Bằng chứng: AG-C đọc bản tổng hợp trên dauthau.gxd.vn (trang thương mại).
Diễn giải thay thế: Không có.
Yếu tố bất định: Chưa đối chiếu bản gốc và các lần sửa 2024–2025.
Nguồn: dauthau.gxd.vn · non-AI, thứ cấp
Independence: max_tag=[LOW CONFIDENCE] · origins: 1 bản tổng hợp
---

Claim C01: "QĐ 1989, Điều 8: dấu thanh đặt trên hoặc dưới chữ cái ghi âm chính (hoà, quý hoá, thuỷ, khoẻ); ia/ua/ưa dấu trên chữ thứ nhất; iê/yê/uô/uơ dấu trên chữ thứ hai."
Kết luận: Đúng · Mức tin cậy: Cao · Tính đến: 03/10/2026
→ Tag: [CONFIRMED]
Bằng chứng: CTL đọc nguyên văn Điều 8 (luatvietnam.vn); AG-A đối chiếu bản scribd, khớp; GS Nguyễn Minh Thuyết (Dân trí 2018) mô tả cùng nội dung lúc còn dự thảo.
Diễn giải thay thế: Chỉ ràng buộc sách giáo khoa (L05).
Yếu tố bất định: Chính văn bản viết lẫn kiểu ("tùy ngữ cảnh", "hóa học") nếu bản sao chép đúng.
Nguồn: luatvietnam.vn · scribd.com · dantri.com.vn · non-AI
Independence: max_tag=[CONFIRMED] · origins: Bộ GD&ĐT
---

Claim C02: "QĐ 1989, Điều 9: âm i đứng ngay sau phụ âm đầu viết bằng i (hi vọng, kỉ niệm, lí luận, mĩ thuật, bác sĩ, tỉ lệ); tên riêng viết theo đúng tên."
Kết luận: Đúng · Mức tin cậy: Cao · Tính đến: 03/10/2026
→ Tag: [CONFIRMED]
Bằng chứng: CTL đọc nguyên văn Điều 9; AG-A đọc cùng điều.
Diễn giải thay thế: Âm "uy" nằm ngoài Điều 9, vẫn viết y (Điều 8: "quý hoá, thuỷ thủ").
Yếu tố bất định: Tên nước "Mỹ" không được nêu trực tiếp.
Nguồn: luatvietnam.vn · non-AI
Independence: max_tag=[CONFIRMED] · origins: Bộ GD&ĐT
---

Claim C03: "Quy tắc viết i của sách giáo khoa bắt nguồn từ QĐ 240/1984."
Kết luận: Phức tạp hơn claim · Mức tin cậy: Thấp · Tính đến: 03/10/2026
→ Tag: [ASSESSED]
Bằng chứng (mâu thuẫn, giữ cả hai):
- Đào Tiến Thi (ngonnguhoc.org, 2011): gốc từ Quy định 30/11/1980; QĐ 240 "không đề cập cụ thể".
- Thanh Niên (2017): kết luận tương tự, nhưng ghi nhầm số văn bản.
- GS Thuyết (Dân trí 2018): theo "quy định đã có từ năm 1980".
- Tuổi Trẻ (2020): "Quyết định số 240 quy định về viết chữ 'i' hay 'y'".
- AG-A tìm trong toàn văn QĐ 240: không có quy tắc i/y.
Diễn giải thay thế: Phụ lục của QĐ 240 có thể khác bản sao.
Yếu tố bất định: Không ảnh hưởng quy ước đề xuất.
Nguồn: ngonnguhoc.org · dantri.com.vn · tuoitre.vn · thanhnien.vn · non-AI
Independence: max_tag=[ASSESSED] · origins: học giả, báo
---

Claim C04: "Ngoài sách giáo khoa, thói quen chiếm ưu thế là y (kỹ, lý, Mỹ)."
Kết luận: Đúng · Mức tin cậy: Vừa · Tính đến: 03/10/2026
→ Tag: [ASSESSED]
Bằng chứng:
- CTL đếm trên bản sao: NĐ 30 (kỹ 15, lý 65, kĩ/lí 0); Luật 64/2025 (kỹ 6, lý 67); NĐ 78 (kỹ 18, lý 84); NĐ 187 (kỹ 5, lý 67); HD 05/2026 (kỹ 10, lý 4).
- AG-D: trang hỗ trợ Microsoft, Apple, Google dùng "lý", "kỹ". Microsoft Style Guide có lẫn ("Xử lí" 1 lần).
- Đào Tiến Thi (2011): 46/49 nhà xuất bản phân biệt i/y.
Diễn giải thay thế: Báo chí sau 2020 có thể đã chuyển sang i. Chưa có khảo sát.
Yếu tố bất định: Đếm trên bản sao, mẫu văn bản nhỏ.
Nguồn: bản sao văn bản (chinhphu.vn, luatvietnam.vn, dap.ctu.edu.vn) · ngonnguhoc.org · support.apple/microsoft/google
Independence: max_tag=[ASSESSED] · origins: nhiều
---

Claim C05: "Vị trí dấu thanh trên thực tế chia đôi."
Kết luận: Đúng · Mức tin cậy: Vừa · Tính đến: 03/10/2026
→ Tag: [ASSESSED]
Bằng chứng (CTL đếm cục bộ, cú pháp: kiểu cũ / kiểu mới):
- Luật 64/2025: 116 / 0. NĐ 187/2025: 134 / 1. NĐ 78/2025: 35 / 6. NĐ 30/2020 (bản OCR ctu.edu.vn): 44 / 9. HD 05 (PDF gốc): 0 / 142. QĐ 1989 (bản sao): 9 / 5.
- TT 05/2026/TT-BNG: thấy "khoá".
- AG-D: Microsoft 7 / 0; Apple 9 / 0; Google Chrome 4 / 31.
Diễn giải thay thế:
- Bản sao có thể gõ lại theo kiểu của trang đăng.
- Riêng HD 05 là PDF gốc, chắc chắn kiểu mới.
Yếu tố bất định: Chưa đếm trên bản ký số của luật và nghị định.
Nguồn: như trên
Independence: max_tag=[ASSESSED] · origins: Quốc hội, Chính phủ, Đảng, 3 hãng
---

Claim C06: "Chuyên gia ngôn ngữ chưa thống nhất về i/y và dấu thanh."
Kết luận: Đúng · Mức tin cậy: Vừa · Tính đến: 03/10/2026
→ Tag: [HIGH CONFIDENCE]
Bằng chứng: AG-A đọc:
- Dân trí 2018 (Nguyễn Minh Thuyết);
- Tuổi Trẻ 2020 (Phạm Văn Tình, Nguyễn Văn Hiệp, Hoàng Dũng);
- khoavanhoc-ngonngu.edu.vn (Trần Trí Dõi);
- qdnd.vn 2022: Hoàng Phê "không nên xác định chuẩn một cách vội vàng".
AG-D đọc sổ tay UniKey: "Theo nhiều nhà ngôn ngữ học thì 'kiểu mới' được coi là đúng chính tả".
Diễn giải thay thế: Không có.
Yếu tố bất định: Chưa đọc tham luận gốc của Hoàng Phê, Cao Xuân Hạo.
Nguồn: dantri.com.vn · tuoitre.vn · qdnd.vn · unikey.org · non-AI
Independence: max_tag=[HIGH CONFIDENCE] · origins: nhiều chuyên gia độc lập
---

Claim C07: "QĐ 1989, Điều 5: tên chữ Latin viết nguyên dạng (lược dấu phụ); tên không Latin viết như tiếng Anh; Hán Việt quen dùng giữ nguyên; tiểu học phiên âm có gạch nối."
Kết luận: Đúng · Mức tin cậy: Cao · Tính đến: 03/10/2026
→ Tag: [CONFIRMED]
Bằng chứng: CTL đọc Điều 5 (luatvietnam.vn); AG-A đọc cùng điều.
Diễn giải thay thế: Mâu thuẫn với QĐ 07/2003 và NĐ 30 (C08).
Yếu tố bất định: Không có.
Nguồn: luatvietnam.vn · non-AI
Independence: max_tag=[CONFIRMED] · origins: Bộ GD&ĐT
---

Claim C08: "NĐ 30, Phụ lục II: tên người, địa danh nước ngoài phiên âm trực tiếp có gạch nối (Vla-đi-mia I-lích Lê-nin; Mát-xcơ-va)."
Kết luận: Đúng · Mức tin cậy: Vừa · Tính đến: 03/10/2026
→ Tag: [HIGH CONFIDENCE]
Bằng chứng: AG-B đọc trang 37–39 của bản ký số (OCR, đối chiếu ảnh).
Diễn giải thay thế: NĐ 30 cũng chấp nhận phiên âm Hán Việt (Mao Trạch Đông, Bắc Kinh).
Yếu tố bất định: Không có.
Nguồn: datafiles.chinhphu.vn · non-AI
Independence: max_tag=[HIGH CONFIDENCE] · origins: Chính phủ
---

Claim C09: "QĐ 1989, Điều 7: thuật ngữ có khả năng tạo nhiều thuật ngữ cùng gốc thì viết nguyên dạng (hydrogen, concerto)."
Kết luận: Đúng · Mức tin cậy: Cao · Tính đến: 03/10/2026
→ Tag: [CONFIRMED]
Bằng chứng: CTL đọc nguyên văn Điều 7; AG-A đọc cùng điều.
Diễn giải thay thế: Không có.
Yếu tố bất định: Không có.
Nguồn: luatvietnam.vn · non-AI
Independence: max_tag=[CONFIRMED] · origins: Bộ GD&ĐT
---

Claim C10: "Từ điển tiếng Việt (Hoàng Phê) là tham chiếu de facto, nhưng đang tranh cãi bản nào chính thống."
Kết luận: Phức tạp hơn claim · Mức tin cậy: Vừa · Tính đến: 03/10/2026
→ Tag: [ASSESSED]
Bằng chứng:
- AG-D: Microsoft Style Guide liệt kê "Từ điển Tiếng Việt 2008", "Từ điển Chính tả (Hoàng Phê, 2006)" làm normative references.
- AG-A: báo Thanh Hóa (09 và 13/02/2026) nói có 3 bản "Hoàng Phê"; đồng tác giả Phạm Hùng Việt nói không biết việc sửa chữa bản 2016.
- AG-A: qdnd.vn (2022) nói từ điển "tái bản… tới hàng chục lần".
Diễn giải thay thế: Mỗi nhà xuất bản có thể có bản riêng.
Yếu tố bất định: Chưa hỏi Vietlex hay nhà xuất bản.
Nguồn: download.microsoft.com · baothanhhoa.vn · ct.qdnd.vn · non-AI
Independence: max_tag=[ASSESSED] · origins: hãng, báo
---

Claim V01: "NĐ 30, Phụ lục II: các nhóm viết hoa như bảng 4.1 của packet."
Kết luận: Đúng · Mức tin cậy: Cao · Tính đến: 03/10/2026
→ Tag: [CONFIRMED]
Bằng chứng:
- AG-B đọc bản ký số (OCR + ảnh trang 37–39), liệt kê 23 nhóm.
- CTL tải bản thứ hai (PDF trên dap.ctu.edu.vn) và khớp các câu: "Thủ đô Hà Nội, Thành phố Hồ Chí Minh"; "thứ Hai, thứ Tư, tháng Năm, tháng Tám"; "Nhân dân, Nhà nước"; quy tắc chức vụ; quy tắc phông chữ.
Diễn giải thay thế: Không có.
Yếu tố bất định: Bản ctu.edu.vn là bản OCR, có lỗi chữ ("Đỉều").
Nguồn: datafiles.chinhphu.vn · dap.ctu.edu.vn · non-AI
Independence: max_tag=[CONFIRMED] · origins: Chính phủ (2 bản)
---

Claim V02: "Địa hình + tên riêng: 'biển Cửa Lò, chợ Bến Thành, sông Vàm Cỏ, vịnh Hạ Long'; ghép thành tên riêng: 'Cửa Lò, Vũng Tàu, Lạch Trường, Vàm Cỏ, Cầu Giấy'."
Kết luận: Đúng · Mức tin cậy: Vừa · Tính đến: 03/10/2026
→ Tag: [HIGH CONFIDENCE]
Bằng chứng: AG-B đọc bản ký số. CTL thấy quy tắc ghép ("…trở thành…") trên bản ctu.edu.vn; câu ví dụ "sông Vàm Cỏ" không bắt được trên bản OCR này.
Diễn giải thay thế: Không có.
Yếu tố bất định: Không có.
Nguồn: datafiles.chinhphu.vn · dap.ctu.edu.vn · non-AI
Independence: max_tag=[HIGH CONFIDENCE] · origins: Chính phủ
---

Claim V03: "NĐ 30: 'Viết hoa tên chức vụ, học vị nếu đi liền với tên người cụ thể', nhưng ví dụ 'Chủ tịch Quốc hội, Thủ tướng Chính phủ' không kèm tên người."
Kết luận: Đúng (quy tắc lệch ví dụ) · Mức tin cậy: Cao · Tính đến: 03/10/2026
→ Tag: [CONFIRMED]
Bằng chứng: CTL đọc trên bản ctu.edu.vn; AG-B đọc bản ký số và ghi nhận cùng điểm lệch.
Diễn giải thay thế: Ví dụ có thể hiểu là chức vụ gắn với tên cơ quan, coi như danh từ riêng.
Yếu tố bất định: Không có.
Nguồn: dap.ctu.edu.vn · datafiles.chinhphu.vn · non-AI
Independence: max_tag=[CONFIRMED] · origins: Chính phủ
---

Claim V04: "Quy tắc viết hoa trong văn bản pháp luật (NĐ 78/2025, Phụ lục I thay bởi NĐ 187/2025) khác NĐ 30."
Kết luận: Đúng · Mức tin cậy: Vừa · Tính đến: 03/10/2026
→ Tag: [HIGH CONFIDENCE]
Bằng chứng: AG-B đọc bản sao NĐ 78 (xaydungchinhsach) và NĐ 187 (luatvietnam). Các điểm khác:
- viết hoa sau dấu hai chấm khi mở ngoặc kép, và đầu khoản, điểm;
- "Nhà nước" chỉ khi là tên riêng;
- ví dụ "Giàng A Pao, Kơ Pa Kơ Lơng";
- ví dụ hai cấp hành chính.
Diễn giải thay thế: Không có.
Yếu tố bất định: Chưa đọc bản ký số NĐ 187.
Nguồn: chinhphu.vn · luatvietnam.vn · non-AI
Independence: max_tag=[HIGH CONFIDENCE] · origins: Chính phủ
---

Claim V05: "QĐ 07/2003: tên dân tộc thiểu số nhiều âm tiết có gạch nối (Ê-đê, Ba-na); QĐ 1989: viết hoa tên thiên thể (Mặt Trời, Trái Đất), viết liền (Sêrêpôk)."
Kết luận: Đúng · Mức tin cậy: Vừa · Tính đến: 03/10/2026
→ Tag: [HIGH CONFIDENCE]
Bằng chứng: AG-A đọc QĐ 07/2003 trên vbpl.vn và QĐ 1989, Điều 4 trên luatvietnam.vn.
Diễn giải thay thế: Hai văn bản khác nhau về gạch nối cho tên dân tộc thiểu số.
Yếu tố bất định: Quan hệ hiệu lực giữa hai văn bản (L06).
Nguồn: vbpl.vn · luatvietnam.vn · non-AI
Independence: max_tag=[HIGH CONFIDENCE] · origins: Bộ GD&ĐT
---

Claim V06: "Tiêu đề tiếng Việt viết hoa kiểu câu, không Title Case."
Kết luận: Phức tạp hơn claim · Mức tin cậy: Vừa · Tính đến: 03/10/2026
→ Tag: [ASSESSED]
Bằng chứng:
- CTL đọc Microsoft trang 24 ("only the first character in a sentence is capitalized") và trang 28 ("But we accept title capitalization…").
- AG-D: Mozilla cấm Title Case; thanh điều hướng Apple vi-vn viết "Mua Hàng"; Netflix có tên phim viết Title Case.
- NĐ 30 không nói trực tiếp về tiêu đề.
Diễn giải thay thế: Title Case được chấp nhận cho tên sản phẩm, tên tác phẩm dịch.
Yếu tố bất định: Không có.
Nguồn: download.microsoft.com · mozilla-l10n.github.io · support.apple.com · netflixstudios.com
Independence: max_tag=[ASSESSED] · origins: 4 hãng (mâu thuẫn)
---

Claim S01: "Dấu thập phân là dấu phẩy."
Kết luận: Đúng · Mức tin cậy: Cao · Tính đến: 03/10/2026
→ Tag: [CONFIRMED]
Bằng chứng:
- CTL đọc NĐ 86/2012, Phụ lục V, Chú ý 4: "245,12 mm (không viết là 245.12 mm)".
- CTL đọc QĐ 1989, Điều 11.1 và Luật Kế toán, Điều 11.2.
- CTL chạy Node Intl: `1.234.567,891`.
- AG-C đọc NĐ 86 trên vbpl.vn.
Diễn giải thay thế: Không có.
Yếu tố bất định: NĐ 86 "hết hiệu lực một phần" theo vbpl (S). NĐ 37/2026 chỉ bãi bỏ NĐ 13/2022. Luật Đo lường đang sửa.
Nguồn: luatvietnam.vn · vbpl.vn · Node ICU 78.3 · non-AI
Independence: max_tag=[CONFIRMED] · origins: Chính phủ, Quốc hội, Bộ GD&ĐT, Unicode
---

Claim S02: "Phân cách hàng nghìn không thống nhất."
Kết luận: Đúng · Mức tin cậy: Cao · Tính đến: 03/10/2026
→ Tag: [ASSESSED] (range, giữ từng nguồn)
Bằng chứng:
- Dấu chấm: Luật Kế toán, Điều 11.2 (CTL; bắt buộc trong kế toán); CLDR `"group": "."` (CTL, AG-D); Microsoft trang 34 (AG-D); Netflix (AG-C).
- Khoảng trắng: QĐ 1989, Điều 11.2 "1 000; 34 456; 3 809 008" (CTL; bắt buộc trong sách giáo khoa); BIPM SI Brochure: "Neither dots nor commas are ever inserted in the spaces between groups." (AG-C).
- Dấu phẩy: VSQI "216,000 VNĐ" (AG-C; thói quen).
- NĐ 86/2012: không quy định.
Diễn giải thay thế: Không có quy định chung cho văn bản ngoài kế toán và sách giáo khoa.
Yếu tố bất định: TCVN 7870-1 chưa đọc (trả phí).
Nguồn: vbpl.vn · luatvietnam.vn · bipm.org · cldr-json · vsqi.gov.vn
Independence: max_tag=[ASSESSED] · origins: nhiều
---

Claim S03: "Ký hiệu đơn vị đặt sau trị số, cách một dấu cách; °C viết '15 °C'; góc phẳng viết liền; tên đơn vị chữ thường."
Kết luận: Đúng · Mức tin cậy: Cao · Tính đến: 03/10/2026
→ Tag: [CONFIRMED]
Bằng chứng: CTL đọc NĐ 86/2012, Phụ lục V (luatvietnam.vn), mục 7 và Chú ý 1, 2; AG-C đọc cùng phụ lục và mục 1–2 về tên đơn vị.
Diễn giải thay thế: Phạm vi bắt buộc là văn bản do cơ quan nhà nước ban hành (Luật Đo lường, Điều 9).
Yếu tố bất định: Bản sao có lỗi OCR ở ví dụ "22 m".
Nguồn: luatvietnam.vn · vanban.chinhphu.vn (Luật 04/2011) · non-AI
Independence: max_tag=[CONFIRMED] · origins: Chính phủ, Quốc hội
---

Claim S04: "Giữa số và % không có khoảng trắng."
Kết luận: Phức tạp hơn claim · Mức tin cậy: Vừa · Tính đến: 03/10/2026
→ Tag: [ASSESSED]
Bằng chứng:
- CTL đọc Microsoft trang 40: "There is no space between number and %."
- CTL chạy Node: `25,6%`.
- AG-C đọc BIPM: "a space separates the number and the symbol %".
- Chưa thấy văn bản Việt Nam nào quy định.
Diễn giải thay thế: Theo chuẩn SI thì phải có dấu cách.
Yếu tố bất định: Không có.
Nguồn: download.microsoft.com · bipm.org · cldr-json
Independence: max_tag=[ASSESSED] · origins: hãng, BIPM, Unicode
---

Claim S05: "Đơn vị tiền là 'Đồng', ký hiệu quốc gia 'đ', ký hiệu quốc tế 'VND'."
Kết luận: Đúng · Mức tin cậy: Cao · Tính đến: 03/10/2026
→ Tag: [CONFIRMED]
Bằng chứng: CTL đọc Luật 46/2010/QH12, Điều 16 (vanban.chinhphu.vn) và Luật Kế toán, Điều 10.1 (vbpl.vn). AG-C xác nhận VBHN 25 vẫn giữ Điều 16, và Luật 23/2026/QH16 không sửa điều này.
Diễn giải thay thế: Không có.
Yếu tố bất định: Không có.
Nguồn: vanban.chinhphu.vn · vbpl.vn · quochoi.vn · non-AI
Independence: max_tag=[CONFIRMED] · origins: Quốc hội
---

Claim S06: "'VNĐ' không phải ký hiệu chính thức; ₫ (U+20AB) là ký tự kỹ thuật mà CLDR dùng."
Kết luận: Đúng (trong các văn bản đã đọc) · Mức tin cậy: Vừa · Tính đến: 03/10/2026
→ Tag: [ASSESSED]
Bằng chứng:
- Hai luật ở S05 chỉ ghi "đ", "VND".
- AG-C: UnicodeData `20AB;DONG SIGN`.
- CTL chạy Node: `1.234.567 ₫`, ký tự trước ₫ là `a0` (NBSP).
- Thói quen "VNĐ" (VSQI) vẫn phổ biến.
Diễn giải thay thế: Có thể có văn bản khác dùng "VNĐ".
Yếu tố bất định: Chưa quét toàn bộ cơ sở dữ liệu văn bản.
Nguồn: unicode.org · cldr-json · Node Intl
Independence: max_tag=[ASSESSED] · origins: Quốc hội, Unicode
---

Claim S07: "Cách ghi ngày theo từng phạm vi."
Kết luận: Đúng · Mức tin cậy: Cao · Tính đến: 03/10/2026
→ Tag: [CONFIRMED]
Bằng chứng (CTL đọc tất cả):
- NĐ 30 (bản ctu.edu.vn): "đối với những số thể hiện ngày nhỏ hơn 10 và tháng 1, 2 phải ghi thêm số 0 phía trước".
- HD 05: "tháng dưới 3".
- QĐ 1989, Điều 10: "ngày 20-11-2017", "ngày 20/11/2017", "15/10/2017 - 20/11/2017", "mỗi bài viết và tài liệu phải sử dụng một cách viết thống nhất".
- Node Intl: `3/10/26`, `3 thg 10, 2026`, `3 tháng 10, 2026`.
Diễn giải thay thế: Không có.
Yếu tố bất định: Không có.
Nguồn: dap.ctu.edu.vn · xdcs.cdnchinhphu.vn · luatvietnam.vn · Node
Independence: max_tag=[CONFIRMED] · origins: Chính phủ, Đảng, Bộ GD&ĐT, Unicode
---

Claim S08: "Văn bản trang trọng ghi giờ kiểu '14 giờ 30'."
Kết luận: Chưa đủ chứng cứ · Mức tin cậy: Thấp · Tính đến: 03/10/2026
→ Tag: [LOW CONFIDENCE]
Bằng chứng: AG-C chỉ thấy trích đoạn tìm kiếm (TT 111/2018/TT-BTC) và Wikipedia. CLDR dùng `HH:mm` (CTL kiểm).
Diễn giải thay thế: Không có.
Yếu tố bất định: Không có quy phạm chung.
Nguồn: vi.wikipedia.org (S) · cldr-json
Independence: max_tag=[LOW CONFIDENCE] · origins: thứ cấp
---

Claim S09: "Không có quy tắc chung về viết số bằng chữ hay chữ số."
Kết luận: Đúng · Mức tin cậy: Vừa · Tính đến: 03/10/2026
→ Tag: [HIGH CONFIDENCE]
Bằng chứng: AG-D đọc Microsoft trang 31: "There is no specific rule to write numbers as numbers or letters in Vietnamese." Netflix: 1–10 viết chữ, chỉ cho phụ đề.
Diễn giải thay thế: Không có.
Yếu tố bất định: Không có.
Nguồn: download.microsoft.com · netflixstudios.com
Independence: max_tag=[HIGH CONFIDENCE] · origins: 2 hãng
---

Claim D01: "Không có văn bản quy phạm nào quy định cách dùng dấu câu, khoảng trắng."
Kết luận: Đúng (bằng chứng phủ định) · Mức tin cậy: Vừa · Tính đến: 03/10/2026
→ Tag: [HIGH CONFIDENCE]
Bằng chứng:
- AG-C: QĐ 1989, Điều 1–11 có 0 lần "dấu câu".
- CTL đọc danh sách điều của QĐ 1989: không có điều về dấu câu.
- monkey.edu.vn (nguồn yếu): "chưa có quy định chính thức và đồng bộ".
- Cao Tự Thanh (2021): tòa báo, nhà xuất bản tự đặt quy ước.
Diễn giải thay thế: Chương trình Ngữ văn 2018 hoặc sách giáo khoa có thể có nội dung dạy dấu câu, nhưng đó không phải quy phạm.
Yếu tố bất định: Chưa đọc giáo trình.
Nguồn: luatvietnam.vn · khoavanhoc-ngonngu.edu.vn · monkey.edu.vn
Independence: max_tag=[HIGH CONFIDENCE] · origins: Bộ GD&ĐT, học giả
---

Claim D02: "Microsoft Vietnamese Style Guide: không cách trước dấu câu; không dấu phẩy trước 'và/hoặc'; NBSP giữa số và đơn vị; không cách trước %; không dùng hyphen khi dịch."
Kết luận: Đúng · Mức tin cậy: Cao · Tính đến: 03/10/2026
→ Tag: [CONFIRMED]
Bằng chứng: CTL đọc bản trích PDF (trang 8, 24, 28, 34, 36, 40); AG-D tải PDF gốc từ download.microsoft.com (metadata sửa 2024-09-05).
Diễn giải thay thế: Đây là sổ tay bản địa hóa phần mềm, không phải chuẩn quốc gia.
Yếu tố bất định: Tài liệu có mâu thuẫn nội bộ: `5,25 cm` so với `2.34 cm`; `$ 1.526,75` so với `2.400VND`.
Nguồn: download.microsoft.com · non-AI
Independence: max_tag=[CONFIRMED] · origins: Microsoft
---

Claim D03: "Mozilla: dấu ba chấm là một ký tự (U+2026); chuyển câu bị động sang chủ động; cấm Title Case."
Kết luận: Đúng · Mức tin cậy: Vừa · Tính đến: 03/10/2026
→ Tag: [HIGH CONFIDENCE]
Bằng chứng: AG-D đọc README trên GitHub (commit 2019-07-03).
Diễn giải thay thế: Tài liệu cũ, thời Firefox OS.
Yếu tố bất định: Không có.
Nguồn: mozilla-l10n.github.io · non-AI
Independence: max_tag=[HIGH CONFIDENCE] · origins: cộng đồng Mozilla
---

Claim D04: "Văn bản luật viết gạch nối có cách giữa hai danh từ ngang hàng ('kinh tế - xã hội')."
Kết luận: Đúng · Mức tin cậy: Vừa · Tính đến: 03/10/2026
→ Tag: [HIGH CONFIDENCE]
Bằng chứng:
- CTL đếm: Luật 64/2025 (bản chinhphu.vn) có 14 lần có cách, 0 lần liền; NĐ 187 (luatvietnam) có 2 lần có cách, 0 lần liền.
- AG-B: NĐ 30, Điều 2.2 viết "tổ chức chính trị - xã hội".
- Quốc hiệu "Độc lập - Tự do - Hạnh phúc" xuất hiện ở các bản.
Diễn giải thay thế: Bản sao có thể chuẩn hóa khoảng trắng.
Yếu tố bất định: Chưa đếm trên bản ký số.
Nguồn: bản sao chinhphu.vn, luatvietnam.vn
Independence: max_tag=[HIGH CONFIDENCE] · origins: Quốc hội, Chính phủ
---

Claim M01: "TCVN 6909:2001 là bộ mã 16 bit phù hợp ISO/IEC 10646-1:2000 và Unicode 3.0; có cả dạng dựng sẵn và tổ hợp; không chọn dạng nào."
Kết luận: Đúng · Mức tin cậy: Vừa · Tính đến: 03/10/2026
→ Tag: [HIGH CONFIDENCE]
Bằng chứng: AG-B OCR bản quét trên vietunicode.sourceforge.net (mục 1.1, 2.1, 5.1, 5.2); tìm "dựng sẵn", "tổ hợp" chỉ ra 2 định nghĩa.
Diễn giải thay thế: Có thể có văn bản hướng dẫn khác chọn dạng. Chưa thấy.
Yếu tố bất định: Bản quét không chính thức. Hiệu lực TCVN 6909 chưa kiểm.
Nguồn: vietunicode.sourceforge.net · non-AI
Independence: max_tag=[HIGH CONFIDENCE] · origins: Bộ KH&CN (qua bản quét)
---

Claim M02: "Thể thức NĐ 30, NĐ 78, HD 05: phông Times New Roman, bộ mã Unicode theo TCVN 6909:2001, màu đen."
Kết luận: Đúng · Mức tin cậy: Cao · Tính đến: 03/10/2026
→ Tag: [CONFIRMED]
Bằng chứng: CTL đọc câu này ở NĐ 30 (bản ctu.edu.vn) và HD 05 (PDF gốc). AG-B đọc NĐ 30 (bản ký số) và NĐ 78.
Diễn giải thay thế: Không có.
Yếu tố bất định: Không có.
Nguồn: dap.ctu.edu.vn · xdcs.cdnchinhphu.vn · datafiles.chinhphu.vn · non-AI
Independence: max_tag=[CONFIRMED] · origins: Chính phủ, Đảng
---

Claim M03: "W3C và Unicode khuyến nghị dạng NFC cho nội dung."
Kết luận: Đúng · Mức tin cậy: Cao · Tính đến: 03/10/2026
→ Tag: [CONFIRMED]
Bằng chứng:
- AG-B và AG-D đọc độc lập w3.org/TR/charmod-norm: "Content authors SHOULD use… NFC".
- AG-D đọc UAX #15, Unicode 18.0.0, §1.2.
- AG-D đọc W3C Q&A (2010) có ví dụ "ề".
- AG-D đọc sổ tay UniKey: ưu tiên dựng sẵn.
Diễn giải thay thế: Charmod-norm vẫn là bản nháp.
Yếu tố bất định: Không có.
Nguồn: w3.org · unicode.org · unikey.org · non-AI
Independence: max_tag=[CONFIRMED] · origins: W3C, Unicode, tác giả UniKey
---

Claim M04: "'hòa' và 'hoà' là hai chuỗi khác nhau; NFC và NFD khác độ dài; tìm kiếm thô sẽ trượt."
Kết luận: Đúng · Mức tin cậy: Cao · Tính đến: 03/10/2026
→ Tag: [CONFIRMED]
Bằng chứng:
- CTL chạy Python: `hòa` = `0x68 0xf2 0x61`, `hoà` = `0x68 0x6f 0xe0`; "Việt" NFD dài 6, NFC dài 4.
- AG-B, AG-D tự chạy trên APFS: tạo file tên NFC, mở bằng tên NFD vẫn được.
- Tài liệu Apple APFS FAQ: "preserves… normalization".
Diễn giải thay thế: Không có.
Yếu tố bất định: Lỗi khi chia sẻ file qua SMB/NFS chỉ có nguồn blog với ví dụ tiếng Hàn, không có ví dụ tiếng Việt.
Nguồn: thực nghiệm · developer.apple.com · eclecticlight.co
Independence: max_tag=[CONFIRMED] · origins: thực nghiệm độc lập 3 lần + Apple
---

Claim M05: "Bộ gõ OpenKey và fcitx-unikey mặc định kiểu cũ; sổ tay UniKey nói kiểu mới được nhiều nhà ngôn ngữ học coi là đúng."
Kết luận: Đúng · Mức tin cậy: Vừa · Tính đến: 03/10/2026
→ Tag: [HIGH CONFIDENCE]
Bằng chứng: AG-D đọc mã nguồn OpenKey (`vUseModernOrthography = 0`), file cấu hình fcitx-unikey (`DefaultValue=False`) và sổ tay UniKey 3.5.
Diễn giải thay thế: Mặc định của UniKey bản Windows có thể khác.
Yếu tố bất định: Chưa biết mặc định của UniKey Windows, EVKey, bộ gõ Telex macOS.
Nguồn: github.com · unikey.org · non-AI
Independence: max_tag=[HIGH CONFIDENCE] · origins: tác giả bộ gõ
---

Claim B01: "CLDR locale vi: thập phân ',', nhóm '.', % viết liền, tiền '#,##0.00 ¤' với NBSP, VND 0 chữ số lẻ, ngày 'd/M/yy', giờ 'HH:mm'."
Kết luận: Đúng · Mức tin cậy: Cao · Tính đến: 03/10/2026
→ Tag: [CONFIRMED]
Bằng chứng: AG-D tải dữ liệu gốc cldr-json 48.2.3; CTL chạy Node 24 (ICU 78.3, CLDR 48.0), kết quả khớp.
Diễn giải thay thế: Không có.
Yếu tố bất định: Không có.
Nguồn: raw.githubusercontent.com/unicode-org/cldr-json · Node
Independence: max_tag=[CONFIRMED] · origins: Unicode (2 cách đọc)
---

Claim B02: "Microsoft: giọng 'clear, friendly and concise'; xưng 'bạn'; tránh đại từ có giới tính khi nói chung; giữ OK, tab, từ viết tắt."
Kết luận: Đúng · Mức tin cậy: Vừa · Tính đến: 03/10/2026
→ Tag: [HIGH CONFIDENCE]
Bằng chứng: AG-D đọc trang 6, 8, 16, 20, 23, 29.
Diễn giải thay thế: Viết cho giao diện phần mềm, không viết cho báo cáo trang trọng.
Yếu tố bất định: Không có.
Nguồn: download.microsoft.com · non-AI
Independence: max_tag=[HIGH CONFIDENCE] · origins: Microsoft
---

Claim B03: "Microsoft: tránh dịch từng chữ."
Kết luận: Đúng · Mức tin cậy: Cao · Tính đến: 03/10/2026
→ Tag: [CONFIRMED]
Bằng chứng: CTL đọc trang 8; AG-D đọc cùng trang.
Diễn giải thay thế: Không có.
Yếu tố bất định: Không có.
Nguồn: download.microsoft.com · non-AI
Independence: max_tag=[CONFIRMED] · origins: Microsoft
---

Claim B04: "'được' mang nghĩa thuận, 'bị' mang nghĩa nghịch; câu bị động trung tính nên dịch sang chủ động."
Kết luận: Chưa đủ chứng cứ · Mức tin cậy: Thấp · Tính đến: 03/10/2026
→ Tag: [LOW CONFIDENCE]
Bằng chứng: AG-D đọc i-jte.org (2022, tác giả là sinh viên).
- Bài jst-ud.vn (2025) cho thấy máy dịch còn sai theo chiều ngược lại: thiếu bị động.
Diễn giải thay thế: Đây là quan sát ngôn ngữ học quen thuộc, nhưng nguồn tìm được còn yếu.
Yếu tố bất định: Chưa có nguồn mạnh hơn.
Nguồn: i-jte.org · jst-ud.vn · non-AI
Independence: max_tag=[LOW CONFIDENCE] · origins: 2 bài tạp chí
---

Claim B05: "Có nghiên cứu về lỗi tiếng Việt do AI sinh (Title Case, dấu câu kiểu Anh)."
Kết luận: Chưa đủ chứng cứ · Mức tin cậy: Thấp · Tính đến: 03/10/2026
→ Tag: [BLIND SPOT]
Bằng chứng: AG-D tìm bằng serper và brave; chỉ thấy style guide của hãng và một bài ACL 2025 về translationese, không có ví dụ tiếng Việt.
Diễn giải thay thế: Không có.
Yếu tố bất định: Không có.
Nguồn: aclanthology.org (gián tiếp)
Independence: max_tag=[BLIND SPOT]
---

Claim T01: "Báo cáo trong repo dùng kiểu mới và y."
Kết luận: Đúng · Mức tin cậy: Cao · Tính đến: 03/10/2026
→ Tag: [CONFIRMED]
Bằng chứng: CTL đếm 31 file (plans/, docs/, SKILL.md, references/), sau khi chuẩn hóa NFC: kiểu mới 198, kiểu cũ 48; kỹ 58, lý 119, Mỹ 32, kĩ 0, lí 0; tỷ 11, tỉ 11; quy 46, qui 0.
Diễn giải thay thế: Regex chỉ bắt âm tiết kết thúc bằng oa/oe/uy có dấu, không bắt "oan, oai…" (hai kiểu giống nhau ở đó).
Yếu tố bất định: Chưa tính file viết sau 11:36.
Nguồn: repo · dữ liệu nội bộ
Independence: max_tag=[CONFIRMED] · origins: đếm trực tiếp
---

Claim T02: "Skill viet-chuyen-nghiep dùng kiểu cũ và y."
Kết luận: Đúng · Mức tin cậy: Cao · Tính đến: 03/10/2026
→ Tag: [CONFIRMED]
Bằng chứng: CTL đếm 44 file trong ~/.claude/skills/viet-chuyen-nghiep: kiểu cũ 92, mới 6; kỹ 53, lý 76, kĩ/lí 0.
Diễn giải thay thế: Không có.
Yếu tố bất định: Không có.
Nguồn: skill · dữ liệu nội bộ
Independence: max_tag=[CONFIRMED] · origins: đếm trực tiếp
---

## X. Claim bị loại (Sai, hoặc không có căn cứ trong văn bản gốc) — không có trong packet

Claim X1: "NĐ 30/2020 đã bị sửa bởi NĐ 05/2025/NĐ-CP." (bài Facebook hieuluat.vn, AG-B gặp)
Kết luận: Sai · Mức tin cậy: Vừa
Bằng chứng: Snippet hue.gov.vn, hanoi.gov.vn cho thấy NĐ 05/2025 sửa NĐ 08/2022 về môi trường. Không văn bản nào xác nhận việc sửa NĐ 30.
→ Loại khỏi packet.
---

Claim X2: "CV 4168/BNV-CQĐP ngày 23/6/2026." (VTV, 29/07/2026)
Kết luận: Sai (ngày) · Mức tin cậy: Cao
Bằng chứng: dangcongsan.vn, tcnnld.vn và mã URL Báo Chính phủ (20250623) đều ghi 23/06/2025.
→ Dùng ngày 23/06/2025.
---

Claim X3: "TCVN 6909 thừa nhận hai phương pháp (dựng sẵn, tổ hợp) có giá trị pháp lý kỹ thuật như nhau." (tóm tắt trên hethongphapluat.com)
Kết luận: Chưa đủ chứng cứ (không có trong văn bản tiêu chuẩn) · Mức tin cậy: Vừa
Bằng chứng: AG-B đọc mục 1–6 của tiêu chuẩn, không thấy câu này.
→ Loại. M01 chỉ giữ: tiêu chuẩn có cả hai dạng và không chọn.
---

Claim X4: "Quyết định 241/QĐ quy định chính tả." (Thanh Niên, 2017)
Kết luận: Sai (số văn bản) · Mức tin cậy: Cao
Bằng chứng: Toàn văn là QĐ 240/QĐ ngày 05/03/1984.
→ Loại.
---

Claim X5: "Văn bản nhà nước năm 2026 viết kiểu mới ('khoá', 'cấp uỷ')." (nhận định của controller trong phiên này, trước khi đếm)
Kết luận: Phức tạp hơn claim → khái quát sai · Mức tin cậy: Cao
Bằng chứng: Đúng với HD 05-HD/VPTW (0 / 142) và một từ trong TT 05/2026/TT-BNG. Sai khi khái quát cho văn bản Chính phủ, Quốc hội 2025 (Luật 64: 116 / 0; NĐ 187: 134 / 1).
→ Thay bằng C05.
---

## Điểm mù (nhắc lại từ packet, mục 8)

1. Bản gốc QĐ 1989 trên cổng chính thức; hiệu lực QĐ 240 và QĐ 1989.
2. Quan hệ QĐ 07/2003 và QĐ 1989 về tên nước ngoài.
3. NĐ 30 sau 29/07/2026; CV 1826/BNV chưa mở.
4. Đếm dấu thanh và i/y trên bản ký số; khảo sát báo chí sau 2020.
5. TCVN 5712:1993; nội dung TCVN 7870-1.
6. Giáo trình về dấu câu.
7. Mặc định bộ gõ UniKey Windows, EVKey, Telex macOS.
8. Nghiên cứu lỗi tiếng Việt do AI sinh.
9. Luật Đo lường và Luật Bảo vệ quyền lợi người tiêu dùng đang sửa.
10. Chế tài nhãn hàng, tên doanh nghiệp, đấu thầu.
11. Tần suất "bác sĩ" so với "bác sỹ".
