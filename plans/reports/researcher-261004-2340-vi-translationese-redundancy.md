# Nhóm B: văn dịch (translationese) và từ thừa trong tiếng Việt

Ngày thu thập: 04/10/2026 (Asia/Saigon). Người thu: agent desk research. Chỉ nguồn công khai.
Quy ước cột "Mở gốc": **Mở** = đã đọc trang/PDF gốc bằng jina-read. **Snippet** = chỉ thấy đoạn trích trong kết quả tìm kiếm. **Gián tiếp** = trích lại từ bài khác, chưa mở sách gốc.
Ví dụ sai → sửa lấy từ nguồn. Chỗ nào agent tự đề xuất đều ghi "đề xuất của agent".

## 0. Tóm tắt (10 dòng)

1. Không tìm được bài nào của Cao Xuân Hạo, Nguyễn Đức Dân, Nguyễn Hiến Lê nói thẳng "lối nói dịch" cho từng cấu trúc (được…bởi, một cách, việc/sự…). Sách gốc không mở được (Scribd khóa, Studocu 404, ResearchGate chặn bot). Không vượt chặn.
2. Hạo phê phán **ngữ pháp trường học chép từ tiếng Pháp**, không phải văn dịch. Trích qua Wikipedia và Thanh Niên (gián tiếp).
3. Lời khuyên "chuyển bị động tiếng Anh sang chủ động tiếng Việt" có nhiều nguồn: Mozilla, Wikipedia tiếng Việt (trích Nguyễn Quốc Hùng 2007), khảo sát Hoàng Công Bình 2015. Nhưng chính khảo sát đó cho thấy 65,8% câu bị động Anh vẫn được dịch thành bị động Việt (đa số với "được"). Không nguồn nào cấm hẳn "được".
4. Từ thừa/lặp nghĩa có nguồn có tên: Hồ Anh Thái (Tiền Phong 2014), Đỗ Văn Học (2015), Đặng Minh Phương (Nhân Dân 2011), Nguyễn Đức Dân. "Các quý vị" có 3 nguồn.
5. **Không tìm được nguồn có tên tác giả** cho: một cách, việc/sự, nó chỉ vật, là một trong những, đóng vai trò, "có thể" thừa, "Có một…", "Điều này", "của" thừa, với/cho, quá ư là, cùng chung, đầu tiên…trước hết, giai đoạn hiện nay. Ghi "chưa kiểm". Đừng đưa các mục này vào luật cứng của agent khi chưa có nguồn.
6. Microsoft Vietnamese Style Guide (mở bản gốc PDF) vừa ủng hộ "tránh dịch từng chữ" vừa **giữ** "sẽ được gửi", "Điều này sẽ được giải thích", "của tôi". Đây là phản chứng quan trọng cho UI.

---

## 1. Bảng claim

| ID | Claim (nguyên văn ngắn, ≤25 từ) | Tác giả / nơi | Ngày | source_type | URL | Mở gốc |
|---|---|---|---|---|---|---|
| T01 | "To achieve a fluent translation, avoid word-to-word translation." Ví dụ đúng: "Image save failed." → "Không lưu được hình ảnh." Sai: "Lưu hình ảnh thất bại." | Microsoft, Vietnamese Localization Style Guide, mục 2.1.3 | chưa thấy ngày (tham khảo từ điển 2003–2008); đọc 04/10/2026 | hướng dẫn doanh nghiệp | https://download.microsoft.com/download/b/f/e/bfecb1b4-21ab-48fd-a48c-c2471b026f8f/vie-vnm-StyleGuide.pdf (qua https://aka.ms/vietnamese-styleguide) | Mở |
| T02 | Cùng mục: "Feel free to reply this email if you have further questions." Đúng: "Vui lòng trả lời email này nếu bạn có bất kỳ thắc mắc nào khác." Sai: "Cứ thoải mái trả lời email này nếu bạn có các câu hỏi khác." | như T01 | như T01 | như T01 | như T01 | Mở |
| T03 | "Many translators, influenced by the English language, omit them or change the word order." (nói về giới từ). Ví dụ: "A bird flies in the sky" → "Con chim bay trên trời", không phải "trong trời" (bản ChatsControl). | như T01, mục 4.1.12 | như T01 | như T01 | như T01 | Mở (ví dụ chim bay: chỉ thấy ở bản ChatsControl, chưa thấy trong PDF gốc) |
| T04 | Cũ → hiện đại: "Tải về không thành công" → "Không tải được"; "File cannot be found" → "Không tìm được tệp"; "Failed to connect" → "Kết nối hỏng". | như T01, mục 2.1.4 và 6 | như T01 | như T01 | như T01 | Mở |
| T05 | "The Microsoft voice avoids an unnecessarily formal tone." Cũ: "Xác định hành động mà máy chủ sẽ thực hiện khi gặp các loại lỗi…" → mới: "Chỉ rõ thao tác cho máy chủ khi gặp các dạng lỗi…" (bỏ "mà…sẽ thực hiện"). | như T01, mục 2.1.4 | như T01 | như T01 | như T01 | Mở |
| T06 | Phản chứng: "Website addresses will be sent to Microsoft" → "Địa chỉ website sẽ được gửi cho Microsoft" (đánh dấu đúng, ký hiệu +). | như T01, mục Articles | như T01 | như T01 | như T01 | Mở |
| T07 | Chủ ngữ giả: "It is raining" → "Trời đang mưa" hoặc "đang mưa"; "It is difficult to do…" → "Khó làm…". Dangling modifier: "Not applicable for Vietnamese", dùng "trong lúc, trong khi, vừa … vừa". | như T01, mục Pronouns, Modifiers | như T01 | như T01 | như T01 | Mở |
| T08 | "The frequent use of possessives is a feature of the English language." Nhưng hướng dẫn vẫn là thêm "của" trước đại từ ("của tôi", "của bạn"). | như T01, mục Possessives | như T01 | như T01 | như T01 | Mở |
| T09 | "Cố gắng chuyển câu bị động tiếng Anh thành câu chủ động tiếng Việt." Và: "Thận trọng khi sử dụng số nhiều." Ví dụ: "Settings" → "Thiết lập", không phải "Những thiết lập" hay "Các thiết lập". | Mozilla L10n, Style Guide Vietnamese (vi), mục "Chú ý chung" | chưa thấy ngày | hướng dẫn cộng đồng bản địa hóa | https://mozilla-l10n.github.io/styleguides/vi/ | Mở |
| T10 | "Chuyển những câu bị động về chủ động cho thích hợp với văn phong tiếng Việt." Cùng mục: cắt câu dài thành câu ngắn; chuyển chỗ mệnh đề quan hệ dài. Dẫn nguồn: Nguyễn Quốc Hùng (2007), *Hướng dẫn kỹ thuật phiên dịch Anh-Việt, Việt-Anh*, NXB Tổng hợp TP.HCM, tr.132–133. | Wikipedia tiếng Việt, "Cẩm nang biên soạn/Dịch thuật" | chưa thấy ngày | wiki cộng đồng trích giáo trình | https://vi.wikipedia.org/wiki/Wikipedia:Cẩm_nang_biên_soạn/Dịch_thuật | Mở trang wiki; **chưa mở sách của Nguyễn Quốc Hùng** |
| T11 | Khảo sát 649 câu bị động Anh (hành chính-công vụ, khoa học, văn học): 427 (65,8%) dịch thành bị động Việt; 184 (28,4%) thành chủ động; 38 (5,9%) thành câu trung gian. Tác giả: "người dịch có xu hướng đưa về câu chủ động", và "câu bị động trong tiếng Anh đều mang ý nghĩa trung tính" (tiếng Việt thường mang sắc thái được/bị). | Hoàng Công Bình, "Các phương thức dịch câu bị động tiếng Anh sang tiếng Việt", *Ngôn ngữ & Đời sống* số 2 (232), 2015 | 2015 | bài khoa học (tạp chí ngành) | http://vci.vnu.edu.vn/upload/15022/pdf/5763a1817f8b9aa7b58b45d2.pdf | Mở (PDF lỗi dấu cách, số liệu đã đối chiếu) |
| T12 | Hạo (2003, tr.145): "những ý nghĩa 'bị động' được diễn đạt bằng những câu 'chủ động'". Hạo (2001): trong mọi công dụng của "được/bị", chỉ có "một tỉ lệ không đến 3,5%" trùng thái bị động châu Âu. | Lâm Minh Hoa, "'Bị' và câu bị động trong tiếng Việt", Việt Nam học – Kỷ yếu Hội thảo quốc tế lần thứ tư (sau 2012) | sau 2012 (bài trích Mi An 2012) | bài khoa học, trích Hạo | https://dulieu.itrithuc.vn/media/dataset/2020_08/ky_05740.pdf | Mở bài của Lâm; **Hạo: gián tiếp** |
| T13 | Nguyễn Kim Thản (1999, qua Lâm Minh Hoa): cấu trúc bị động tiếng Việt "thường không có thành phần phụ biểu thị chủ thể của hoạt động". | như T12 | như T12 | như T12 | như T12 | Gián tiếp |
| T14 | Phía khẳng định có câu bị động: Trương Văn Chình–Nguyễn Hiến Lê, Hoàng Trọng Phiến, Diệp Quang Ban, Nguyễn Minh Thuyết và Nguyễn Văn Hiệp. Ví dụ của Thuyết–Hiệp: "Công nhân xây dựng nhà máy" → "Nhà máy được công nhân xây dựng". | như T12, mục 3.3–3.4 | như T12 | như T12 | như T12 | Gián tiếp |
| T15 | Hạo: "Ngữ pháp sao chép từ tiếng Pháp trở thành một thứ tôn giáo nghiệt ngã". Cũng nói khoảng 75% kiểu câu thật của tiếng Việt không được dạy. | Cao Xuân Hạo (trích trong trang Wikipedia, chú thích [7]) | chưa rõ năm bài gốc | trích gián tiếp | https://vi.wikipedia.org/wiki/Cao_Xuân_Hạo | Gián tiếp (chưa mở chú thích [7]) |
| T16 | Hạo (trích): "nhiều khi người ta thường viết ra những câu mà thường ngày người ta không bao giờ nói". | Báo Thanh Niên, loạt "40 năm Báo Thanh Niên – Hành trình: Viết tiếng Việt cho người Việt đọc" (thẻ tác giả "Hoàng Hải Vân", chưa xác nhận byline) | 28/11/2025 (suy từ URL và ảnh) | báo chí, trích Hạo *Tiếng Việt – Văn Việt – Người Việt* | https://thanhnien.vn/40-nam-bao-thanh-nien-hanh-trinh-viet-tieng-viet-cho-nguoi-viet-doc-185251127153959586.htm | Mở bài báo; Hạo: gián tiếp |
| T17 | Nguyễn Đức Dân: lỗi "Qua thực tế, cho thấy…" (Nguyễn Kim Thản, bút danh Vương Thịnh, báo Nhân Dân 1975) "không được … lên án mạnh mẽ nên nó tiếp tục được duy trì". Ví dụ báo: "Theo khảo sát mới đây của các nhà nghiên cứu, cho thấy nạn tự tử…". | Nguyễn Đức Dân, "Để lâu câu sai hóa… đúng", Sài Gòn Tiếp Thị, đăng lại trên thvl.vn | khoảng 10/2010 (suy từ đường dẫn ảnh) | báo chí, chuyên gia ngôn ngữ | https://thvl.vn/de-lau-cau-sai-hoa%E2%80%A6-dung.html | Mở |
| T18 | Cùng bài: "Trong hầu hết các trường hợp, có thể thay 'tham gia giao thông' bằng 'đi lại'." | Nguyễn Đức Dân | như T17 | như T17 | như T17 | Mở |
| T19 | Cùng bài: "Ông là một cây đại thụ trong giới sử học" là dư, "nhưng cách nói này hiện nay được coi là đúng". Tương tự "người nông dân", "đường quốc lộ". | Nguyễn Đức Dân | như T17 | như T17 | như T17 | Mở |
| T20 | Cùng bài: "Khi một lỗi sai, một lỗi dư thừa nào đó trở nên phổ biến thì chúng ta hãy dè chừng". Cuối bài: cách dùng sai đã thành đúng thì nhà ngôn ngữ "không thể áp đặt"; vì vậy phải phê phán ngay từ đầu. | Nguyễn Đức Dân | như T17 | như T17 | như T17 | Mở |
| T21 | "Tái sinh lại, tái hiện lại, tái diễn lại, tái bản lại, phục chế lại…"; "khi đã hồi phục lại, bà đi xuống" (sách dịch *Kẻ trộm sách*, tr.330). | Hồ Anh Thái (nhà văn), "Chữ thừa", báo Tiền Phong | 22/06/2014 | báo chí, ý kiến nhà văn (kể lại sửa chữa của một người làm đối ngoại, không nêu tên) | https://tienphong.vn/chu-thua-post699411.tpo | Mở |
| T22 | Cùng bài: "Tối ưu nhất, tối đa nhất, tối kỵ nhất, cực kỳ tối mật…"; "Đặc thù riêng"; "đặc trưng riêng của nó" (sách dịch *Tên của khí trời*, tr.40). | Hồ Anh Thái | như T21 | như T21 | như T21 | Mở |
| T23 | Cùng bài: "người họa sĩ", "nhà họa sĩ", "nhà học giả", "nhà triết gia", "nhà doanh nhân"… "đều thừa chữ nhà hoặc chữ người"; "cô gái trẻ", "chàng trai trẻ" giống "young girl, young boy". Ví dụ lấy từ nhiều sách dịch. | Hồ Anh Thái | như T21 | như T21 | như T21 | Mở |
| T24 | Cùng bài, sách *Những mối tình nực cười* (Cao Việt Dũng dịch): "Nhưng mặc dù vậy" (tr.271), "Nhưng tuy nhiên" (tr.271), "Ở bên trong nội tâm" (tr.287); thêm "Lính bộ binh", "Đạo giáo". | Hồ Anh Thái | như T21 | như T21 | như T21 | Mở |
| T25 | "Những từ trùng lắp như bước tiến bộ thì chỉ viết tiến bộ hoặc bước tiến, các quý vị viết quý vị hoặc các vị (vì quý là các rồi)." Và: "Ngày mai trên địa bàn Hà Nội có mưa" → "Ngày mai Hà Nội có mưa". | Đặng Minh Phương, "Viết hay đi đôi với viết đúng", báo Nhân Dân (kể lại thông lệ Ban Biên tập báo Nhân Dân thời trước) | 19/06/2011 | báo chí, hồi ký nghề; không phải văn bản quy định | https://nhandan.vn/viet-hay-di-doi-voi-viet-dung-post543961.html | Mở |
| T26 | "Nói 'các quý vị' là thừa ra chữ 'các'." Cũng chê "những quý vị" và "nhiều những / rất nhiều những" (ví dụ: "Có rất nhiều những khán giả gọi vào."). | Lê Hữu, "Tiếng Việt, yêu & ghét", t-van.net | khoảng 10/2022 (suy từ đường dẫn ảnh) | blog tạp văn hải ngoại | https://t-van.net/le-huu-tieng-viet-yeu-ghet/ | Mở |
| T27 | "cụm từ 'các quý vị' thì chữ 'các' ở đây là thừa". Dẫn *Từ điển tiếng Việt* (Trung tâm KHXH&NV Quốc gia, 2005): "quý" dùng gọi lịch sự một số người. Cũng nói cách này "ngày càng phổ biến" trên báo, truyền hình. | Tác giả chưa rõ trong bản đọc, đăng trên tgpsaigon.net | chưa rõ | bài trên trang giáo phận, không rõ tác giả | https://tgpsaigon.net/bai-viet/thua-cac-quy-vi-40842 | Mở |
| T28 | "Một số tổ hợp sau cũng bị coi là dùng thừa từ: Tái tạo lại, chưa vị thành niên, hoàn thành xong, đáp ứng theo, căn cứ theo, đại quy mô lớn, cấm không được, tối ưu nhất, hoàn toàn rất, đề xuất kiến nghị, nhu cầu đòi hỏi…" Cũng: "Xét theo đề nghị của…" → "Xét đề nghị của…" hoặc "Theo đề nghị của…". | Đỗ Văn Học, "Một số vấn đề về sử dụng ngôn ngữ, văn phong trong văn bản quản lý nhà nước", Tạp chí Phát triển KH&CN (ĐHQG-HCM), tập 18, số X1, 2015 | 2015 | bài khoa học | https://std.vnuhcmjournal.com.vn/index.php/std/article/download/1012/1421/2590 | Mở |
| T29 | Cùng bài, về văn bản nhà nước: "tuyệt đối tránh việc dùng thừa từ"; thừa từ là chọn nhiều đơn vị đồng nghĩa trong khi "chỉ cần một đơn vị từ là đủ". | Đỗ Văn Học | 2015 | như T28 | như T28 | Mở |
| T30 | Tiếp xúc với tiếng Pháp: "tiếng Pháp ảnh hưởng vào tiếng Việt trước tiên và rõ rệt nhất là về mặt cú pháp". Nếu không có báo chí và văn xuôi quốc ngữ đầu thế kỷ XX "thì sẽ không có cú pháp tiếng Việt bây giờ". Văn phong mới thời đó có lúc bị chê "tây hoá". | Lê Tú Anh (tên theo đường dẫn file), "Ngôn ngữ trong tiểu thuyết Việt Nam giai đoạn giao thời", Khoa Văn học và Ngôn ngữ, ĐH KHXH&NV TP.HCM | chưa rõ | bài nghiên cứu văn học-ngôn ngữ | https://khoavanhoc-ngonngu.edu.vn/nghien-cuu/văn-học-việt-nam/3663-ngon-ng-trong-tiu-thuyt-vit-nam-giai-on-giao-thi.html | Mở |
| T31 | Ví dụ "mot à mot": "Rất ít xã hội ngày nay tin vào tôn giáo hơn 40-50 trước" (trích BBC tiếng Việt). Blogger sửa: "Khác với 40, 50 năm trước, ngày nay xã hội tin vào tôn giáo ngày càng ít hơn." | Blog hoamunich (tác giả chưa rõ) | 20/09/2014 (từ URL) | blog cá nhân, độ tin thấp | https://hoamunich.wordpress.com/2014/09/20/noi-buon-tieng-viet/ | Mở; chưa tự đối chiếu bản BBC |

---

## 2. Bảng cấu trúc văn dịch

Mức đồng thuận: **nhiều nguồn** (≥3 nguồn độc lập), **ít nguồn** (2), **một nguồn**, **tranh cãi**, **chưa kiểm** (không tìm được nguồn có tên).

| # | Dạng | Ví dụ sai | Ví dụ sửa | Nguồn | Mức đồng thuận |
|---|---|---|---|---|---|
| S1 | Bị động Anh giữ nguyên "được/bị + V", nhất là khi không có người làm | EN: "No Title of Nobility shall be granted by the United States." Bản gượng (đề xuất của agent, không có trong nguồn): "Danh hiệu quý tộc không được ban tặng bởi Hợp chủng quốc." | "Hợp chủng quốc không ban tặng bất cứ danh hiệu quý tộc nào." (bản dịch trong khảo sát của Hoàng Công Bình). Ví dụ 2: EN "More than 70,000 metric tons of button mushroom are harvested…" → "Mỗi năm, các trang trại trồng nấm ở Mĩ thu hoạch hơn 70000 tấn nấm cúc." | T09, T10, T11 | **Nhiều nguồn** khuyên chuyển chủ động. **Tranh cãi** ở mức "cấm": T11 cho thấy 65,8% vẫn dịch bị động (xem mục 4) |
| S2 | "được … bởi + tác nhân" | Chưa có câu sai nguyên văn từ nguồn. Gợi ý (đề xuất của agent): "Báo cáo được thực hiện bởi nhóm A." | Đề xuất của agent: "Nhóm A thực hiện báo cáo." hoặc "Báo cáo do nhóm A thực hiện." Nguồn chỉ nói gián tiếp: bị động tiếng Việt "thường không có thành phần phụ biểu thị chủ thể" (Thản), và T11: đa số bị động Việt không nêu tác nhân (80,5% theo tác giả) | T13, T11 | **Một nguồn gián tiếp**. Không nguồn nào chê "bởi" trực tiếp. Giữ ở mức khuyến nghị nhẹ |
| S3 | "được/bị" dùng như nhãn trung tính | Chưa có câu sai nguồn. Nguồn nói: tiếng Việt "được" mang sắc thái lợi, "bị" mang sắc thái hại | Không có sửa từ nguồn. Gợi ý (đề xuất của agent): tránh "bị" cho việc trung tính ("tệp bị lưu") | T11 ("trung tính" vs "tình thái"), T12 | **Một nguồn** (T11). Hạo thì đi xa hơn: "được/bị" phần lớn không phải bị động châu Âu |
| S4 | Chủ ngữ giả "It is…", "While/Dangling" | EN "It is raining", "It is difficult to do…" | "Trời đang mưa" / "đang mưa"; "Khó làm…"; "while" → "trong lúc, trong khi, vừa … vừa" | T07 | **Một nguồn** (Microsoft, cho UI) |
| S5 | Trạng ngữ "Qua … cho thấy" thiếu chủ ngữ | "Theo khảo sát mới đây của các nhà nghiên cứu, cho thấy nạn tự tử ở Nhật Bản ngày càng…" (VTV1, 14/9/2010) | Nguồn không đưa bản sửa. Đề xuất của agent: bỏ dấu phẩy và "cho thấy" làm vị ngữ: "Khảo sát … cho thấy…". Lưu ý: nguồn **không** gán lỗi này cho dịch thuật | T17 | **Một nguồn** (Dân, dẫn Thản 1975). Là lỗi cú pháp, chưa chứng minh là văn dịch |
| S6 | Chuỗi Hán-Việt dài thay cho từ thường | "xe cộ tham gia giao thông", "những phương tiện tham gia giao thông trên đường" | "xe cộ đi lại", "những phương tiện đi lại trên đường" | T18 | **Một nguồn** |
| S7 | Câu dịch dài, tuyến tính theo gốc | "Rất ít xã hội ngày nay tin vào tôn giáo hơn 40-50 trước" | "Khác với 40, 50 năm trước, ngày nay xã hội tin vào tôn giáo ngày càng ít hơn." | T31 (blog, độ tin thấp); T10 (cắt câu dài, chuyển mệnh đề quan hệ) | **Ít nguồn**; ví dụ cụ thể chỉ từ blog |
| S8 | Giới từ theo tiếng Anh (in/on/to) | "Con chim bay trong trời" (theo chữ "in") | "Con chim bay trên trời"; "migrate to" → "di chuyển đến/tới/vào/với", không dùng "sang" | T03 | **Một nguồn** (Microsoft) |
| S9 | Số nhiều "các/những" theo Anh | "Những thiết lập", "Các thiết lập" cho "Settings"; "các câu hỏi khác" cho "further questions" | "Thiết lập"; "bất kỳ thắc mắc nào khác" | T09, T02, T26 | **Ít nguồn** (Mozilla, Microsoft, Lê Hữu "nhiều những") |
| S10 | "một cách + tính từ" | Chưa kiểm | Chưa kiểm | Không tìm được nguồn phê phán có tên | **Chưa kiểm** |
| S11 | Lạm dụng "việc/sự/điều" | Chưa kiểm | Chưa kiểm | Không tìm được nguồn | **Chưa kiểm** |
| S12 | Danh từ hóa "tiến hành thực hiện việc kiểm tra" | Không có câu nguồn. Gần nhất (T05): "Xác định hành động mà máy chủ sẽ thực hiện khi gặp…" | "Chỉ rõ thao tác cho máy chủ khi gặp…" | T05 | **Một nguồn gián tiếp** (Microsoft, về văn phong trang trọng thừa). Chưa có nguồn về "tiến hành" |
| S13 | "nó" chỉ vật, "là một trong những", "đóng vai trò", "có thể" thừa, "Có một…", "Điều này", "Trong khi đó" | Chưa kiểm | Chưa kiểm. Ghi chú: Microsoft dùng "Điều này sẽ được giải thích…" làm ví dụ đúng và "Nó" cho "It" (xem T06, T08) | Không tìm được nguồn phê phán | **Chưa kiểm** |
| S14 | Sở hữu "của" thừa ("bạn của tôi" vs "bạn tôi") | Chưa kiểm | Chưa kiểm. Microsoft bảo "thêm của trước đại từ" (T08) | Không tìm được nguồn phê phán có tên | **Chưa kiểm**; nguồn có sẵn đi ngược |
| S15 | "với" dịch "with", "cho" dịch "for" | Chưa kiểm | Chưa kiểm. Microsoft vẫn dùng "kết nối với" (T03) | — | **Chưa kiểm** |

---

## 3. Bảng từ thừa / lặp nghĩa

| Dạng | Ví dụ thừa | Gọn hơn | Nguồn (tác giả hoặc tòa soạn) | Mức đồng thuận |
|---|---|---|---|---|
| tái … lại | tái sinh lại, tái hiện lại, tái diễn lại, tái bản lại, tái tạo lại | bỏ "lại" | Hồ Anh Thái, Tiền Phong 22/06/2014 (T21); Đỗ Văn Học 2015 (T28, "tái tạo lại") | **Ít nguồn (2)** |
| hồi phục lại, phục chế lại | "khi đã hồi phục lại, bà đi xuống" (sách dịch) | "khi đã hồi phục" | Hồ Anh Thái (T21) | **Một nguồn** |
| tối ưu nhất, tối đa nhất | cũng "tối kỵ nhất", "hoàn toàn rất" | "tối ưu", "tối đa" | Hồ Anh Thái (T22); Đỗ Văn Học (T28, "tối ưu nhất", "hoàn toàn rất") | **Ít nguồn (2)** |
| "các quý vị" | "Thưa các quý vị" | "Thưa quý vị" / "các vị" | Đặng Minh Phương, Nhân Dân 19/06/2011 (T25); Lê Hữu (T26); tgpsaigon.net (T27, dẫn Từ điển TV 2005) | **Nhiều nguồn (3)** |
| "những/các" kép | "nhiều những", "rất nhiều những", "những quý vị" | "nhiều", "quý vị" | Lê Hữu (T26); Mozilla (T09, "Những thiết lập") | **Ít nguồn (2)** |
| đặc thù riêng | "đặc trưng riêng của nó" (sách dịch) | "đặc trưng của nó" | Hồ Anh Thái (T22) | **Một nguồn** |
| nhà/người + nghề | người họa sĩ, nhà họa sĩ, nhà triết gia, nhà doanh nhân | "họa sĩ", "triết gia"… | Hồ Anh Thái (T23). Chính tác giả nhận cách này "đã thành quen" | **Một nguồn; tranh cãi** (xem mục 4) |
| tính từ "trẻ" thừa | cô gái trẻ, chàng trai trẻ, anh thanh niên trẻ | "cô gái", "chàng trai" | Hồ Anh Thái (T23), liên hệ "young girl/boy" | **Một nguồn** |
| nhưng + tuy/mặc dù | "Nhưng mặc dù vậy", "Nhưng tuy nhiên" | "Nhưng"/"Tuy nhiên"/"Mặc dù vậy" | Hồ Anh Thái (T24) | **Một nguồn** |
| ở bên trong nội tâm | "Ở bên trong nội tâm" | "Trong nội tâm" | Hồ Anh Thái (T24) | **Một nguồn** |
| Hán-Việt + thuần Việt chồng nhau | lính bộ binh, đạo giáo | "bộ binh", "đạo" (nếu không cần phân biệt) | Hồ Anh Thái (T24) | **Một nguồn** |
| chồng nghĩa trong văn bản nhà nước | "Xét theo đề nghị", hoàn thành xong, căn cứ theo, đáp ứng theo, cấm không được, đại quy mô lớn, đề xuất kiến nghị, nhu cầu đòi hỏi, chưa vị thành niên | "Xét đề nghị"/"Theo đề nghị"; "hoàn thành"; "căn cứ"… | Đỗ Văn Học 2015 (T28) | **Một nguồn** (bài khoa học có tên) |
| trùng lắp "bước tiến bộ" | "bước tiến bộ" | "tiến bộ" hoặc "bước tiến" | Đặng Minh Phương, Nhân Dân (T25) | **Một nguồn** |
| từ địa điểm thừa | "trên địa bàn Hà Nội" | "Hà Nội" | Đặng Minh Phương, Nhân Dân (T25) | **Một nguồn** |
| Hán-Việt thừa đã thành quen | cây đại thụ, người nông dân, đường quốc lộ | — | Nguyễn Đức Dân (T19): nay "được coi là đúng" | **Tranh cãi** |
| tham gia giao thông | "xe cộ tham gia giao thông" | "đi lại" | Nguyễn Đức Dân (T18) | **Một nguồn** |
| cùng chung | — | — | Không tìm được nguồn có tên | **Chưa kiểm** |
| quá ư là | — | — | Không tìm được nguồn có tên | **Chưa kiểm** |
| đầu tiên … trước hết | — | — | Không tìm được nguồn có tên | **Chưa kiểm** |
| giai đoạn hiện nay | — | — | Không tìm được nguồn có tên | **Chưa kiểm** |

Ghi chú loại nguồn: Hồ Anh Thái là nhà văn, bài ý kiến, không phải nhà ngôn ngữ học. Ông kể sửa chữa của một người bạn không nêu tên. Đặng Minh Phương kể lại thông lệ nội bộ, không có văn bản quy định. Hai nguồn này là bằng chứng "có người trong nghề chê", chưa phải chuẩn.

---

## 4. Phản chứng: hai phía

**Phía "nên tránh / cải" (giữ gìn)**
- Nguyễn Đức Dân: lỗi và từ dư phải phê phán sớm, nếu không "sai hóa đúng" (T19, T20).
- Mozilla, Wikipedia tiếng Việt (trích Nguyễn Quốc Hùng), Microsoft: tránh dịch từng chữ, chuyển bị động sang chủ động, bỏ "Những/Các" thừa (T01, T09, T10).
- Hạo (trích): người Việt viết ra những câu mà nói thường ngày thì không bao giờ nói (T16). Lưu ý đây là phê phán **ngữ pháp trường học**, không nêu "văn dịch" (T15).

**Phía "đã là tiếng Việt bình thường / không nên cấm"**
- Hoàng Công Bình 2015: 65,8% câu bị động Anh trong ngữ liệu dịch (hành chính, khoa học, văn học) vẫn thành bị động Việt, trong đó "được" chiếm tỉ lệ cao nhất (theo tác giả 69,3%). Tỉ lệ bị động Việt cao nhất ở văn bản khoa học (81,3%, theo thứ tự cột trong bảng; thứ tự cột chưa tự kiểm với bản gốc) (T11). Đây là mô tả thực tế dịch, chưa phải khuyến nghị.
- Nguyễn Minh Thuyết và Nguyễn Văn Hiệp, Diệp Quang Ban, Hoàng Trọng Phiến, Trương Văn Chình–Nguyễn Hiến Lê: tiếng Việt **có** câu bị động, ví dụ "Nhà máy được công nhân xây dựng" (T14, gián tiếp).
- Lâm Minh Hoa: khác biệt giữa tiếng Việt và ngôn ngữ Ấn-Âu "không nằm ở chỗ có hay không có câu bị động" mà ở cách diễn đạt (T12, mục 3.1).
- Microsoft giữ "sẽ được gửi cho Microsoft" và "Điều này sẽ được giải thích…" làm ví dụ đúng; vẫn dùng "của tôi/của bạn" (T06, T08).
- Lê Tú Anh: cú pháp chịu ảnh hưởng tiếng Pháp là nền của văn xuôi hiện đại; văn phong mới từng bị gọi "tây hoá" (T30).
- Nguyễn Đức Dân (T19): "cây đại thụ" nay "được coi là đúng"; "đại thụ" trơn lại bị coi là không bình thường.
- Hồ Anh Thái (T23): chính tác giả cho rằng "nhà họa sĩ", "người nghệ sĩ" sẽ "có ngày được vào từ điển". Chưa trích nguyên văn vì dài; xem bài gốc.

**Hai phía bất đồng về Hạo**
- Hạo: ý nghĩa bị động tiếng Việt thường diễn đạt bằng câu chủ động; "được/bị" phần lớn không phải thái bị động châu Âu (<3,5%) (T12).
- Thuyết–Hiệp, Ban và những người khác: có cấu trúc bị động tiếng Việt với "được/bị" (T14).
- Lâm Minh Hoa tổng kết: đa số ý kiến phủ nhận chỉ là "phủ nhận tương đối". Chưa ai trong nguồn đã mở nói thẳng "cấm được/bởi".

**Gợi ý cho luật agent (đề xuất của agent, dựa trên bằng chứng ở trên):**
- Mức khuyến nghị (có nguồn nhiều): ưu tiên chủ động; bỏ "những/các" thừa; bỏ "lại" trong "tái … lại"; "quý vị" không thêm "các".
- Mức "cân nhắc": "được … bởi", "một cách", "việc/sự", "của". Không nguồn phê phán, hoặc nguồn có sẵn chấp nhận. Không nên cấm cứng.

---

## 5. Điểm mù

1. **Chưa mở sách gốc** của Cao Xuân Hạo (*Tiếng Việt – Văn Việt – Người Việt* 2003; *Tiếng Việt – Mấy vấn đề…* 1998), Nguyễn Đức Dân (*Lôgích và tiếng Việt*, *Từ câu sai đến câu hay*), Nguyễn Hiến Lê (*Luyện văn*, *Tôi tập viết tiếng Việt*). Scribd chỉ hiện bản xem trước; Studocu trả 404; ResearchGate chặn bot (không vượt).
2. Các trích Hạo (T12, T15, T16) đều gián tiếp. Chưa có nguồn nào cho thấy Hạo chê "được…bởi" hay "một cách".
3. Hoàng Dũng, Phan Ngọc, Nguyễn Văn Tu: không tìm được bài liên quan tới văn dịch. Chưa kiểm.
4. Sách "chữa lỗi" kiểu Lê A, Hoàng Trọng Phiến, Nguyễn Minh Thuyết, Bùi Minh Toán: chưa mở. Có thể chứa danh sách từ thừa có nguồn tốt hơn.
5. Giáo trình biên dịch Anh–Việt: mới chạm Nguyễn Quốc Hùng 2007 và Lưu Trọng Huấn 2008 qua Wikipedia (chưa mở sách). Không tìm được danh sách "lỗi dịch điển hình" có số liệu ngoài T11. Các trang dịch thuật thương mại (achautrans, dichthuathoasen…) bị loại vì không có tác giả và không nguồn.
6. Các mục "chưa kiểm" ở mục 2 và 3: một cách, việc/sự, nó, là một trong những, đóng vai trò, "có thể", "Có một…", "Điều này", "Trong khi đó", "của", với/cho, cùng chung, quá ư là, đầu tiên…trước hết, giai đoạn hiện nay.
7. Ngày đăng thiếu: thvl.vn (T17–T20), t-van.net (T26), tgpsaigon.net (T27), Mozilla, Wikipedia, Lê Tú Anh. Ngày ghi "suy từ URL/ảnh" là ước lượng, không phải ngày đăng đã xác nhận.
8. Microsoft T03: ví dụ "chim bay trên trời" chỉ thấy ở bản ChatsControl (bản chuyển thể của bên thứ ba), chưa thấy trong PDF gốc. Các claim còn lại của Microsoft đã đối chiếu PDF gốc.
9. Không có nghiên cứu đo tần suất các cấu trúc này trong văn bản do LLM sinh ra. Mọi "slop" ở đây là phê phán văn dịch của người, chưa chứng minh áp dụng cho LLM.
10. Kết quả tìm kiếm tiếng Việt cho cụm chính xác (dấu ngoặc kép) hầu như trả rỗng; phần lớn nguồn tìm được qua truy vấn tự nhiên. Có thể còn nguồn tốt chưa lộ.

---

## 6. Query đã chạy (tóm tắt)

Công cụ: `collect.py serper` (gl vn, hl vi), `brave` (search-lang vi), `jina-search` (có/không `--site`), `jina-read`. Không dùng searxng (không cần stop).

Nhóm query chính (đã có kết quả đọc được):
- Cao Xuân Hạo + câu bị động / "được" "bị" / lối nói dịch / Tây hóa / "Một số biểu hiện của cách nhìn Âu châu".
- Nguyễn Đức Dân + lỗi logic / chuyên mục tiếng Việt / "để lâu câu sai hóa đúng".
- Nguyễn Kim Thản "Qua thực tế cho thấy".
- Nguyễn Hiến Lê + Luyện văn / Tôi tập viết tiếng Việt / "mot à mot" / bị động "bởi".
- "được thực hiện bởi", "một cách", "là một trong những", "đóng vai trò", "nó chỉ vật", "danh hóa việc sự", "tiến hành", "Có một", "có thể thừa", "nhằm mục đích".
- "tái … lại", "hồi phục lại", "cùng chung", "các quý vị", "những các", "quá ư là", "giai đoạn hiện nay", "tối ưu nhất".
- Microsoft Vietnamese Style Guide, Mozilla l10n Vietnamese, Gengo style guide, Wikipedia Cẩm nang dịch thuật.
- Dịch Anh–Việt: lỗi thường gặp, giáo trình biên dịch, câu bị động Anh–Việt, khảo sát lỗi biên dịch.
- Văn bản hành chính: lỗi dùng từ, từ thừa.

Trang đã mở bằng jina-read (đọc nội dung): Lâm Minh Hoa (itrithuc.vn), Nguyễn Đức Dân (thvl.vn), Hồ Anh Thái (tienphong.vn), Đặng Minh Phương (nhandan.vn), Lê Hữu (t-van.net), tgpsaigon.net, Microsoft PDF, Mozilla vi, Wikipedia (Cẩm nang Dịch thuật; Cao Xuân Hạo), Hoàng Công Bình (vci.vnu.edu.vn), Đỗ Văn Học (std.vnuhcmjournal.com.vn), Lê Tú Anh (khoavanhoc-ngonngu.edu.vn), Thanh Niên 2025, blog hoamunich, bản ChatsControl của Microsoft guide, Nhân Dân "Đừng biến văn học dịch thành thảm họa" (không dùng làm claim), Tuổi Trẻ "Học dùng tiếng Việt với Nguyễn Hiến Lê" (không dùng), jst-ud (bị/được → tiếng Hàn, không dùng).

Không mở được: studocu (404), ResearchGate (bị chặn), Facebook (rỗng), Scribd (chỉ xem trước).

Thứ tự trình bày theo yêu cầu: bảng claim, bảng cấu trúc, bảng từ thừa, phản chứng, điểm mù, query.

---

## Câu hỏi chưa giải quyết

1. Có muốn mở rộng sang sách giấy (Hạo 2003, Dân, Nguyễn Hiến Lê) qua thư viện hoặc bản PDF hợp pháp để có trích nguyên văn trực tiếp không?
2. Với các mục "chưa kiểm" (một cách, việc/sự, nó, của…), agent nên bỏ khỏi luật cứng hay cần thêm một vòng tìm nguồn (đề xuất: sách chữa lỗi của Lê A, Nguyễn Minh Thuyết, Bùi Minh Toán)?
3. Có chấp nhận nguồn "ý kiến nhà báo/nhà văn" (Hồ Anh Thái, Đặng Minh Phương) làm căn cứ cho luật mềm, hay chỉ nhận nguồn học thuật?
