# Nhóm D: kho văn bản, từ điển, công cụ tiếng Việt

Ngày 04/10/2026. Desk research, nguồn công khai. Thư mục: worktree tv-selection-research-a75206.

Định nghĩa một lần:
- **Corpus** = kho văn bản lớn, gom sẵn để nghiên cứu.
- **Crawl** = robot đi gom trang web hàng loạt. Common Crawl là nguồn crawl công cộng.
- **Dump** = bản chụp toàn bộ một site (vd Wikipedia) ở một ngày.
- **TBX** = định dạng chuẩn trao đổi bảng thuật ngữ.
- **Hunspell** = bộ kiểm chính tả mã nguồn mở, so từng từ với danh sách.

Mức xác nhận dùng trong bảng:
- **[mở]** = mở trang/README/API và đọc.
- **[gh]** = `gh api`.
- **[HEAD]** = `curl -I` lấy kích thước/ngày.
- **[snippet]** = chỉ thấy đoạn trích tìm kiếm.
- **[test]** = tự chạy thử.

---

## 1. Bảng claim

| ID | Claim | Nguồn / xác nhận | Độ tin |
|---|---|---|---|
| R01 | binhvq/news-corpus **đã ngừng phân phối từ 08/2026**. Link tải gỡ, file Drive xóa, repo archive. Thu thập khoảng 2018-2021. Cũ: ~14,9 triệu bài, 150+ báo, ~18,6 GB, ~111 triệu câu. Ngoài ra ~10 triệu bình luận Facebook đến 10/2020. MIT chỉ áp cho mã, không áp cho dữ liệu. | README repo [gh], đã đọc. https://github.com/binhvq/news-corpus | Cao |
| R02 | Bản re-upload trên HF `vietgpt/binhvq_news_vi` vẫn hiện (tạo 21/02/2023, sửa 30/03/2023, thẻ giấy phép trống). Quyền bản quyền báo vẫn thuộc các tòa soạn. | HF API, chỉ metadata. Chưa mở nội dung, chưa kiểm còn tải được không | Trung bình |
| R03 | FineWeb-2 tiếng Việt (`vie_Latn`): 61.064.248 tài liệu, 50,89 tỷ từ, 319,83 GB thô / 121,19 GB nén. Giấy phép ODC-By. Từ 96 snapshot Common Crawl, **mùa hè 2013 đến 04/2024**. | Thẻ dataset [mở] `HuggingFaceFW/fineweb-2`, HF API | Cao |
| R04 | Tôi lấy mẫu ngẫu nhiên FineWeb-2 vi qua datasets-server: 29 khối × 100 dòng. Năm thu thập: 2015=97, 2016=103, 2017=120, 2018=280, 2019=200, 2020=200, 2021=514, 2022=586, 2023=600, 2024=200. **~28% (800/2900) có ngày crawl 2023-2024.** Khối liền nhau cùng đợt crawl nên sai số lớn (khoảng ±8 điểm). Chỉ là ước lượng thô. | [test] tự chạy, https://datasets-server.huggingface.co/rows | Trung bình-thấp |
| R05 | HPLT v2.0 `vie_Latn`: 1,01e8 tài liệu (~101 triệu), 8,32e10 từ (~83,2 tỷ), 3,8e11 ký tự, 3,02e9 đoạn. CC0 cho phần đóng gói. Nguồn chủ yếu Internet Archive, thêm Common Crawl. Khoảng thời gian crawl: **không thấy** trong thẻ. | Thẻ HF `HPLT/HPLT2.0_cleaned` [mở], trang hplt-project.org/datasets/v2.0 [mở] | Cao (kích thước), thấp (thời gian) |
| R06 | OSCAR 23.01 vi: 33.933.994 / 22.424.984.210 / 140,8 GB. Thứ tự cột ước đoán là tài liệu / từ / dung lượng, chưa kiểm chắc. Lấy từ **snapshot Common Crawl 11-12/2022**. Chỉ metadata và chú thích là CC0. Nội dung thuộc chủ trang gốc. Bị khóa (gated), phải khai form. | Thẻ HF `oscar-corpus/OSCAR-2301` [mở] | Cao (nguồn, ngày), trung bình (cột) |
| R07 | CulturaX vi: 57.606.341 tài liệu, 55.380.123.774 token (0,88% toàn bộ). Gộp mC4 v3.1.0 + OSCAR 20.19, 21.09, 22.01, 23.01. Giấy phép theo mC4 và OSCAR. Bị khóa. Phạm vi ngày của mC4 3.1.0: chưa kiểm. | Thẻ HF `uonlp/CulturaX` [mở] | Cao (số), thấp (ngày mC4) |
| R08 | CC-100 vi: file `vi.txt.xz` 29.508.806.944 byte (~29,5 GB nén), sửa 23/10/2020. Dựng từ **các snapshot Common Crawl 01-12/2018**. "Không tuyên bố quyền sở hữu trí tuệ" cho phần chuẩn bị. | [HEAD], trang data.statmt.org/cc-100 [mở] | Cao |
| R09 | Wikipedia vi: 1.304.833 bài, 396.154.064 từ (theo CirrusSearch), 4.605.815 trang. Dump mới nhất `viwiki-latest-pages-articles.xml.bz2` = 1.158.035.363 byte (~1,16 GB), 01/10/2026. Giấy phép CC BY-SA 4.0. Thư mục dump công khai chỉ còn từ 2026 trở đi, **không thấy** dump trước 11/2022. | MediaWiki API (siteinfo, rightsinfo) + [HEAD] + liệt kê dumps.wikimedia.org/viwiki | Cao |
| R10 | Wikipedia trên HF `wikimedia/wikipedia`, cấu hình `20231101.vi`. Thẻ ghi CC BY-SA 3.0 + GFDL (bản chụp cũ). | HF API [mở] | Cao |
| R11 | viTenTen (Sketch Engine): 6+ tỷ từ, 7+ tỷ token, 138+ triệu câu, 24+ triệu trang. Tải về web **tháng 5-7, 11/2017 và 01/2018**. Dịch vụ trả phí (có bản thử miễn phí). Không tải được thô. | Trang sketchengine.eu [mở] | Cao |
| R12 | Leipzig Corpora: tồn tại vài gói tiếng Việt, `vie_mixed_2014_1M` (306 MB), `vie_wikipedia_2021_1M` (217 MB), `vie_wikipedia_2016_1M` (227 MB). Mỗi gói ~1 triệu câu (theo tên). Trang web chính bị Anubis chặn bot nên giấy phép chưa đọc được. | [HEAD] trên downloads.wortschatz-leipzig.de. Mẫu tên tôi đoán, 3/6 tên cho 200 OK | Trung bình |
| R13 | VLSP: dữ liệu **phải ký form và gửi email** mới được cấp. Không tải tự do. Danh mục từ VLSP 2013 đến 2022. Vietnamese WordNet: "chưa có sẵn". | Trang vlsp.org.vn/resources [mở] | Cao |
| R14 | NIIVTB (Vietnamese Treebank): 20.588 câu, chia NIIVTB-1 (10.431) và NIIVTB-2 (10.157). Repo không khai giấy phép (spdx trống). VTB gốc 10.433 câu, 274.266 token. | [gh] mynlp/niivtb + snippet | Trung bình |
| R15 | **Chưa thấy ai đo mức nhiễm văn AI/dịch máy riêng cho web tiếng Việt.** Có ba thứ gần nhất: (a) Thompson 2024 đo dịch máy đa chiều trên web nhiều ngôn ngữ, văn bản không nhắc "Vietnamese"; (b) Pew 08/2026 đo văn AI nhưng **chỉ trang tiếng Anh** (10.000 trang/đợt × 49 đợt, 01/2021-07/2026); (c) VietAIDetector (arXiv 26/08/2026) là công cụ phát hiện, không phải số đo web. | Thompson: arxiv 2401.05749v1 [mở, tìm "Vietnam" không có kết quả]. Pew: trang methodology [mở]. VietAIDetector: arxiv 2608.25478 [mở abstract] | Cao (cho phát biểu "không thấy") |
| R16 | Thompson 2024: 57,1% câu trong mẫu đa ngôn ngữ nằm trong bộ câu dịch song song nhiều chiều. Ngôn ngữ ít tài nguyên bị nhiễm nặng hơn. Tác giả kết luận đó là dấu hiệu dịch máy. | arxiv 2401.05749v1 [mở] | Cao |
| R17 | Pew snippet: "35% of newly published websites contained AI-generated or AI-assisted text". Chỉ là snippet, chưa mở trang kết quả. Phương pháp xác nhận ở R15 (b). | Serper snippet + methodology [mở] | Thấp (cho con số 35%) |
| R18 | Hồ Ngọc Đức (Free Vietnamese Dictionary Project): trang gốc ở Leipzig **không còn** (404). Từng công khai 1999-2024. Có bản lưu re-host bởi Huy Nguyen (06/04/2026), định dạng DICT. | informatik.uni-leipzig.de/~duc/Dict/ trả 404 [test]. Bài everyhue.me [mở] | Cao |
| R19 | Giấy phép từ điển Hồ Ngọc Đức: **GPL**. Wiktionary vi nói nhập phần lớn mục từ từ FVDP, xin phép phát hành kép cùng GFDL. | Wiktionary:Nguồn gốc/FVDP [mở] | Cao |
| R20 | undertheseanlp/dictionary tổng hợp 79.226 từ. Phân theo nguồn: hongocduc 73.172, tudientv 36.533, wiktionary 32.484. GPL-3.0, push cuối 10/12/2018. | [gh] + README [mở] | Cao |
| R21 | duyet/vietnamese-wordlist: danh sách Viet11K / 22K / 39K / 74K. GPL-2.0. Push cuối 01/01/2024. | [gh] contents | Cao |
| R22 | Wiktionary vi: 348.841 "bài" (mục từ), 401.949 trang, 18.225.651 từ. Dump `viwiktionary-latest-pages-articles.xml.bz2` = 65.037.654 byte (~65 MB, hơi trên ngưỡng 50 MB, không tải). Giấy phép CC BY-SA. | MediaWiki API + [HEAD] | Cao |
| R23 | Từ điển Hán Nôm (hvdic.thivien.net): 393.660 mục. Nguồn gồm Thiều Chửu 1942, Trần Văn Chánh 1999, Nguyễn Quốc Hùng 1975, Hồ Lê 1976, Unihan… Trang điều khoản trả 404 ở đường dẫn tôi thử. Giấy phép tải: **không thấy**. | Trang chủ [mở] | Cao (nội dung), không thấy (giấy phép) |
| R24 | hunspell-vi (1ec5): có hai bộ dấu. `vi-DauCu` (xóa, kiểu truyền thống/hải ngoại) và `vi-DauMoi` (xoá, kiểu cải cách trong nước). Không có file LICENSE trên GitHub, nhưng README gốc Aspell ghi **GPLv2**, và file LICENSES của LibreOffice ghi "released with GPLv2". Chỉ chứa **âm tiết đơn**, **không có từ ghép**. | README [gh], README-en.txt [gh], LibreOffice LICENSES-en.txt [gh] | Cao |
| R25 | `vi-DauMoi.dic` có 6.641 dòng (6.642 dòng trừ dòng đầu). Tôi chạy thử bằng cách tách âm tiết (không có binary hunspell). Kết quả ở mục 4. | [test] | Cao (cho phép thử), trung bình (cho suy rộng) |
| R26 | LanguageTool **không hỗ trợ tiếng Việt**. API công khai `language=vi` trả lỗi "not a language code known". Danh sách 62 biến thể không có `vi`. Thư mục `languagetool-language-modules` không có `vi`. | API trực tiếp [test], trang /languages [mở], [gh] | Cao |
| R27 | underthesea v9.5.0 (17/05/2026), Apache-2.0, hoạt động (push 03/10/2026). Có `text_normalize`, `restore_diacritics`, `word_tokenize`, `pos_tag`, `ner`… **Không thấy** hàm kiểm chính tả/ngữ pháp riêng trong bảng chức năng README. | [gh] + README [mở] | Cao |
| R28 | VnCoreNLP: NOASSERTION, push cuối 12/02/2023, cần Java 1.8+. Chức năng: tách từ, POS, NER, dependency. Không phải công cụ sửa lỗi. | [gh] + README [mở] | Cao |
| R29 | VSEC (sửa lỗi chính tả): 9.341 câu, 11.202 lỗi. Repo không khai giấy phép, push cuối 31/05/2021. Bản mirror HF ghi `license: other`. | [gh] + README [mở] + HF API | Cao |
| R30 | ViLexNorm (chuẩn hóa từ MXH): 10.467 cặp bình luận. **CC BY-NC-SA 4.0 (cấm thương mại).** | README [gh] + HF API | Cao |
| R31 | Mô hình sửa lỗi `bmd1905/vietnamese-correction-v2`: dựa trên BARTpho, Apache-2.0, sửa 17/04/2024. Dữ liệu huấn luyện tạo từ VNTC (lỗi gây ra nhân tạo). Chưa chạy thử. | HF API + README [gh] | Trung bình |
| R32 | Microsoft Terminology: **Language Portal đã đóng 30/06/2023** (Slator, snippet). Nay có hai nơi: bản TBX trọn bộ (zip **176.156.561 byte** ≈ 176 MB, sửa 06/02/2025, ~100 ngôn ngữ) và trang "Terminology Search" / "UI String Search" dạng báo cáo Power BI. Style guide lấy ở "Microsoft Style Guides". Giấy phép: **không thấy** trên trang. | learn.microsoft.com [mở] + [HEAD] zip. Ngày đóng từ snippet, chưa mở bài | Cao (vị trí mới), trung bình (ngày đóng) |
| R33 | Pontoon (Mozilla) vi: 51.578 chuỗi, dịch 50.662, còn thiếu 916. Có link "Download Terminology" (TBX, ~109 KB) và "Download Translation Memory". Dự án Terminology vi: 211 chuỗi, 116 đã dịch. Style guide Mozilla l10n: repo `mozilla-l10n/styleguides` CC-BY-4.0. | Trang Pontoon [mở], `vi.tbx` [HEAD/tải 108.847 byte], [gh] | Cao |
| R34 | applelocalization.com: **không chính thức**. Tra chuỗi chuẩn của iOS 15-26, macOS 12-26. 16.339.749 chuỗi toàn bộ ngôn ngữ. Mã nguồn web 203 sao. Quyền sở hữu chuỗi thuộc Apple. | Trang [mở], [gh] kishikawakatsumi/applelocalization-web | Cao |
| R35 | GNOME: nhóm dịch vi có trang trên l10n.gnome.org (điều phối viên Trần Ngọc Quân, wiki GnomeVi). Repo `Teams/Translation/vi` trên GitLab **trống**, bản dịch nằm ở từng module. KDE: nhóm vi có svn `l10n-kf6/vi`. Giấy phép chuỗi dịch: chưa kiểm. | l10n.gnome.org [mở], gitlab.gnome.org [mở], l10n.kde.org [mở] | Trung bình |
| R36 | Android/AOSP: file `core/res/res/values-vi/strings.xml` 353.543 byte trong mirror `aosp-mirror/platform_frameworks_base`. **Mirror đã archive** (push cuối 12/11/2025). Giấy phép repo: GitHub không nhận ra (NOASSERTION). AOSP dùng Apache-2.0 theo hiểu biết chung, chưa kiểm trong repo. | [gh] | Trung bình |
| R37 | Không thấy style guide công khai của Tuổi Trẻ hay VnExpress. Tuổi Trẻ có bài luận (Hải Thụy) nêu ví dụ AP Stylebook, Guardian, BBC, Economist, và nói ở Việt Nam các cơ quan nên gặp nhau thống nhất dần quy định. Ngụ ý chưa có tài liệu chung. Bài chưa rõ năm đăng. | Tuổi Trẻ [mở], tìm kiếm VnExpress/Tuổi Trẻ không ra | Trung bình |
| R38 | Quy định chính tả duy nhất có văn bản chính thức rõ: **Quyết định 240/QĐ ngày 05/03/1984 của Bộ Giáo dục** về chính tả và thuật ngữ tiếng Việt (áp dụng cho sách giáo khoa, báo, văn bản ngành giáo dục). | luatvietnam.vn [mở], nhiều nguồn trùng | Cao (tồn tại), chưa kiểm còn hiệu lực |
| R39 | Thông tư 02/2023/TT-BXD (ban hành 03/03/2023, hiệu lực 20/04/2023) có kèm mẫu hợp đồng thi công, tư vấn xây dựng. Thông tư 09/2016/TT-BXD là bản cũ. | vanban.chinhphu.vn [mở] | Cao (ngày), chưa kiểm còn hiệu lực 2026 |
| R40 | NSO (Cục Thống kê) đăng báo cáo kinh tế xã hội và thông cáo báo chí đều kỳ. Mới nhất: quý III và 9 tháng 2026, ngày đăng 03/10/2026. World Bank có bản tiếng Việt "Điểm lại: Cập nhật Tình hình Kinh tế Việt Nam" (03/2025, 09/2025) và "Cập Nhật Kinh Tế Vĩ Mô Việt Nam" trên kho tài liệu. VEPR có Báo cáo Thường niên Kinh tế Việt Nam nhiều năm, bản 2025 đã đăng toàn văn. | nso.gov.vn [mở trang liệt kê qua Serper], worldbank.org snippet, vepr.org.vn snippet | Trung bình (chỉ snippet cho WB/VEPR) |

---

## 2. Bảng kho văn bản

Cột "Lẫn AI?" nhìn theo ngày crawl: trước 11/2022 coi sạch. Sau đó không chắc.

| Kho | Link | Giấy phép | Kích thước (vi) | Năm thu thập | Nguồn văn bản | Lẫn AI? | Xác nhận |
|---|---|---|---|---|---|---|---|
| CC-100 vi | https://data.statmt.org/cc-100/ (`vi.txt.xz`) | Không tuyên bố quyền cho phần chuẩn bị. Nội dung gốc thuộc chủ trang | ~29,5 GB nén | 2018 (CC 01-12/2018) | Web | **Sạch** | [mở] + [HEAD] |
| viTenTen | https://www.sketchengine.eu/vitenten-vietnamese-corpus/ | Dịch vụ trả phí | 6+ tỷ từ, 24+ triệu trang | 2017-01/2018 | Web (đã lọc spam tay trên domain lớn) | **Sạch** | [mở] |
| Leipzig vie_mixed_2014 | https://downloads.wortschatz-leipzig.de/corpora/vie_mixed_2014_1M.tar.gz | Chưa đọc được (site chặn bot) | 306 MB | 2014 (theo tên) | Hỗn hợp (theo tên) | **Sạch** | [HEAD] |
| Leipzig vie_wikipedia_2016 / 2021 | cùng thư mục, `vie_wikipedia_2016_1M`, `vie_wikipedia_2021_1M` | Chưa đọc được | 227 MB / 217 MB | 2016 / 2021 | Wikipedia | **Sạch** | [HEAD] |
| binhvq news (đã gỡ) | https://github.com/binhvq/news-corpus | Không có cho dữ liệu | cũ ~18,6 GB | 2018-2021 | 150+ báo | Sạch nhưng **không còn tải chính thức** | [gh] |
| Wikipedia vi dump | https://dumps.wikimedia.org/viwiki/latest/ | CC BY-SA 4.0 | ~1,16 GB nén, 1,30 triệu bài | Liên tục đến 10/2026 | Bách khoa mở | Có thể lẫn (chỉnh sửa gần đây). Dump cũ trước 11/2022 **không thấy** | API + [HEAD] |
| Wikipedia HF 20231101.vi | https://huggingface.co/datasets/wikimedia/wikipedia | CC BY-SA 3.0 + GFDL | chưa kiểm cỡ | 11/2023 | Bách khoa | Ranh giới mờ | HF API |
| OSCAR 23.01 vi | https://huggingface.co/datasets/oscar-corpus/OSCAR-2301 | Metadata CC0, nội dung không | 140,8 GB | CC 11-12/2022 | Web | **Sát ngưỡng** (giữa 11/2022) | [mở] |
| CulturaX vi | https://huggingface.co/datasets/uonlp/CulturaX | Theo mC4 + OSCAR | 55,4 tỷ token | mC4 3.1.0 + OSCAR đến 23.01 | Web | Chủ yếu trước 2023, mC4 ngày chưa kiểm | [mở] |
| FineWeb-2 vie | https://huggingface.co/datasets/HuggingFaceFW/fineweb-2 | ODC-By | 319,83 GB thô, 61 triệu tài liệu | 2013-04/2024 | Web | **Có lẫn** (~28% mẫu thuộc 2023-24, ước thô) | [mở] + [test] |
| HPLT v2.0 vie | https://huggingface.co/datasets/HPLT/HPLT2.0_cleaned | CC0 (phần đóng gói) | ~101 triệu tài liệu, ~83 tỷ từ | Không thấy | Internet Archive + CC | Không rõ | [mở] |
| VLSP | https://vlsp.org.vn/resources | Ký form, xin email | thay đổi theo bộ | 2013-2022 | Tác vụ nhỏ (NER, WSD, ASR…) | Sạch | [mở] |
| NIIVTB Treebank | https://github.com/mynlp/niivtb | Không khai | 20.588 câu | ~2016-2019 | Báo | Sạch | [gh] |
| UIT datasets (ViQuAD, VSFC, ViNewsQA…) | https://nlp.uit.edu.vn/datasets , https://huggingface.co/datasets/uitnlp/vietnamese_students_feedback | Từng bộ khác nhau, chưa kiểm hết | UIT-VSFC >16.000 câu | Trước 2023 | Wikipedia, phản hồi sinh viên, tin y tế | Sạch | snippet |

Ghi chú dùng:
- Để **đọc giọng văn thật** (mục tiêu của dự án), nên bốc mẫu từ CC-100, viTenTen (nếu có tài khoản), Leipzig 2014/2016. Đây là các kho **chắc chắn trước 11/2022**.
- FineWeb-2 và HPLT quá lớn để đọc, lại có phần sau 2023. Muốn dùng phải lọc theo trường `date` (FineWeb-2 có trường này, [mở]).
- Cả hai nhóm đều là web, không phải văn bản chọn lọc. Có rất nhiều rác, spam, văn dịch.

---

## 3. Bảng từ điển

| Từ điển | Link | Giấy phép | Kích thước | Cập nhật cuối | Nguồn | Xác nhận |
|---|---|---|---|---|---|---|
| Hồ Ngọc Đức (FVDP), bản lưu | https://everyhue.me/posts/preservering-ho-ngoc-duc-vietnamese-dictionary-dataset/ | GPL (nguồn gốc) | Việt-Việt, Anh-Việt, Việt-Anh, Nga-Việt, Việt-Pháp, Pháp-Việt, Đức-Việt, Việt-Đức, Na Uy-Việt… (định dạng DICT) | Trang gốc sống 1999-2024, bản lưu 04/2026 | Cộng đồng | [mở] |
| undertheseanlp/dictionary | https://github.com/undertheseanlp/dictionary | GPL-3.0 | 79.226 từ gộp | 12/2018 | Hồ Ngọc Đức + tudientv + Wiktionary | [gh] |
| duyet/vietnamese-wordlist | https://github.com/duyet/vietnamese-wordlist | GPL-2.0 | 11K / 22K / 39K / 74K từ | 01/2024 | Chưa kiểm nguồn gốc | [gh] |
| Wiktionary vi | https://dumps.wikimedia.org/viwiktionary/latest/ | CC BY-SA | 348.841 mục, dump ~65 MB | Dump 01/10/2026 | Cộng đồng, nhiều mục nhập từ FVDP | API + [HEAD] |
| hunspell-vi (1ec5) | https://github.com/1ec5/hunspell-vi | GPLv2 (qua README gốc) | 6.641 dòng (âm tiết) | push 03/08/2024 | Hồ Ngọc Đức qua Aspell | [gh] + [test] |
| Từ điển Hán Nôm (Thiều Chửu và nhiều nguồn) | https://hvdic.thivien.net/ | **Không thấy** | 393.660 mục | Có tin 02/08/2026 | Thiều Chửu 1942, Trần Văn Chánh, Unihan… | [mở] |
| Từ điển tiếng Việt (Hoàng Phê, Viện Ngôn ngữ học) | https://archive.org/details/tu-dien-tieng-viet-vien-ngon-ngu-hoc | **Còn bản quyền**, bản scan do người dùng đăng, không phải mở | ~36.000 từ theo mô tả trang | — | In 1988, tái bản nhiều lần | snippet. **Không khuyến nghị dùng làm dữ liệu** |
| VietLex | **Không thấy** nguồn đáng tin sau khi tìm | — | — | — | — | Không xác nhận được |

Ghi chú: danh sách từ Hồ Ngọc Đức là gốc của hunspell-vi, undertheseanlp, Wiktionary. Ba bộ này **chồng lấn nhiều**, không độc lập. Theo thống kê undertheseanlp: trong 79.226 từ, 18.833 có đủ ba nguồn, 29.140 chỉ có hongocduc.

---

## 4. Bảng công cụ kiểm lỗi, kèm đánh giá

### 4.1. Phép thử tôi tự chạy (hunspell-vi, `vi-DauMoi.dic`)

Cách chạy: tách âm tiết, đối chiếu với 6.641 mục (không chạy binary hunspell vì máy chưa cài; không mở rộng luật `.aff`). Chỉ là mô phỏng gần, không thay thế hunspell thật.

| Câu thử | Từ bị đánh dấu | Nhận xét |
|---|---|---|
| Câu đúng, "tối ưu hóa" | `hóa` | Báo oan. Từ điển DauMoi ưa "hoá". Là khác phong cách đặt dấu, không phải lỗi |
| Sai dấu: "tôi ưu", "qui trình", "chính xát" | `hóa`, `qui` | Bắt "qui" (chính tả cũ). **Không bắt** "tôi ưu" (tôi là từ hợp lệ) và "xát" (âm tiết hợp lệ) |
| "xử dụng", "dành được", "nghành", "chăm chĩ" | `nghành`, `chĩ` | Bắt hai lỗi thuần chính tả. **Bỏ lọt** "xử dụng" (đúng là "sử dụng") và "dành được" (đúng là "giành được") |
| Viết không dấu: "Toi dang lam bao cao ve ket qua…" | `ket` | Chỉ bắt 1 từ. Phần lớn âm tiết không dấu vẫn là âm tiết hợp lệ |
| Văn kiểu AI: "Trong bối cảnh chuyển đổi số mạnh mẽ…" | không | Không có khả năng bắt giọng văn |
| Lỗi ngữ pháp: "Tôi đã sẽ gửi…" | không | Không có khả năng ngữ pháp |

### 4.2. Đánh giá từng công cụ

| Công cụ | Link | Giấy phép | Chạy ở đâu | Làm được | **Hữu dụng thật cho rà bản thảo** |
|---|---|---|---|---|---|
| hunspell-vi (DauCu/DauMoi) | https://github.com/1ec5/hunspell-vi | GPLv2 | Máy cục bộ, LibreOffice, Firefox | Phát hiện âm tiết không tồn tại ("nghành") | **Thấp-trung bình.** Bắt gõ sai âm tiết. Không bắt sai từ đúng-âm-tiết (xử/sử, giành/dành). Báo oan do phong cách dấu. Vô dụng cho giọng văn |
| LibreOffice vi_VN | https://github.com/LibreOffice/dictionaries/tree/master/vi | GPLv2 | Cục bộ | Cùng gốc với hunspell-vi, `vi_VN.dic` 39.852 byte | Như trên. Không thêm giá trị |
| LanguageTool | https://languagetool.org/languages/ | LGPL-2.1 | — | **Không hỗ trợ tiếng Việt** | Không dùng được [R26] |
| underthesea | https://github.com/undertheseanlp/underthesea | Apache-2.0 | Python (`pip install underthesea`) | Chuẩn hóa văn bản, khôi phục dấu, tách từ, POS, NER | **Trung bình cho tiền xử lý.** `text_normalize`/`restore_diacritics` hữu ích sửa bản thiếu dấu. Không có bộ kiểm chính tả/ngữ pháp trong bảng chức năng |
| VnCoreNLP | https://github.com/vncorenlp/VnCoreNLP | NOASSERTION | Java 1.8+ | Tách từ, POS, NER, dependency | Không phải công cụ sửa lỗi. Dùng để phân tích câu |
| VNTK | `vntk/vntk-core` không còn, `vntk/vntk-cli` push cuối 03/2018 | MIT (cli) | Node | Không thấy chức năng sửa lỗi | **Không khuyến nghị**, bỏ hoang |
| pyvi | https://github.com/trungtv/pyvi | MIT | Python | Tách từ, gán nhãn | Không phải công cụ sửa lỗi |
| bmd1905/vietnamese-correction-v2 | https://huggingface.co/bmd1905/vietnamese-correction-v2 | Apache-2.0 | HF, cần GPU/CPU chậm | Sinh lại câu đúng từ câu sai | **Chưa chạy thử.** Huấn luyện trên lỗi nhân tạo từ báo (VNTC). Có thể "sửa quá tay" như mô hình sinh. Cần thử trên mẫu thật trước khi tin |
| VSEC (bộ dữ liệu) | https://github.com/VSEC2021/VSEC | Không khai | Dữ liệu, không phải công cụ | 9.341 câu, 11.202 lỗi thật do người | Dùng làm **bộ đo** (benchmark) hay làm bộ lỗi mẫu. Giấy phép chưa rõ |
| ViLexNorm | https://github.com/ngxtnhi/vilexnorm | CC BY-NC-SA 4.0 | Dữ liệu | 10.467 cặp bình luận MXH, chuẩn hóa tiếng lóng, viết tắt | Hữu ích để **biết kiểu viết MXH**. Cấm dùng thương mại |
| VietAIDetector | https://github.com/trieuntu/VietAIDetector | MIT | Python + Gradio | Đoán văn có phải do AI viết (zero-shot) | Phù hợp **đo văn bản của agent** có "lộ AI" không. Chưa chạy, chưa biết độ chính xác (có công bố trong paper, tôi chỉ đọc abstract) |

Kết luận mục 4: không có công cụ tự động đủ tốt để rà **giọng văn** hay **ngữ pháp** tiếng Việt. Hunspell chỉ bắt lỗi gõ nhầm âm tiết. Phần còn lại (từ dùng sai, diễn đạt máy móc, tính tự nhiên) phải dùng luật tay hoặc người đọc.

---

## 5. Glossary thuật ngữ giao diện

| Nguồn | Nay ở đâu | Cách tải / tra | Giấy phép | Ghi chú |
|---|---|---|---|---|
| Microsoft Terminology | https://learn.microsoft.com/en-us/globalization/reference/microsoft-terminology | Tải TBX trọn bộ: https://download.microsoft.com/download/b/2/d/b2db7a7c-8d33-47f3-b2c1-ee5e6445cf45/MicrosoftTermCollection.zip (~176 MB, ~100 ngôn ngữ). Hoặc tra qua "Terminology Search" (báo cáo Power BI) trong trang Microsoft language resources | **Không thấy** trên trang | Language Portal cũ đóng 30/06/2023. Link cũ microsoft.com/language trả 403 khi truy cập tự động |
| Microsoft UI Strings | https://learn.microsoft.com/en-us/globalization/reference/microsoft-language-resources | Tra qua "UI String Search" (Power BI). Không thấy file tải riêng | Không thấy | Chuỗi giao diện thật của sản phẩm |
| Microsoft Style Guide vi | Trang "Microsoft Style Guides" cùng mục | PDF (đã có sẵn theo yêu cầu, không tìm lại) | — | — |
| Mozilla Pontoon vi | https://pontoon.mozilla.org/vi/ | "Download Terminology" (TBX 108.847 byte): https://pontoon.mozilla.org/terminology/vi.tbx . Có thêm "Download Translation Memory" | Chưa đọc điều khoản. Style guide repo là CC-BY-4.0 | 51.578 chuỗi, 20 dự án. Chuỗi Mozilla l10n cũng có trên GitHub (chưa kiểm) |
| Apple localization terms | https://applelocalization.com/ | Tra web, chọn iOS 15-26 / macOS 12-26, tìm tiếng Việt. Mã nguồn: github.com/kishikawakatsumi/applelocalization-web | Không chính thức. Chuỗi thuộc Apple | Không thấy API tải bulk trong phiên này |
| Android / AOSP | https://github.com/aosp-mirror/platform_frameworks_base/blob/main/core/res/res/values-vi/strings.xml | Tải file XML trực tiếp (353 KB) | Apache-2.0 theo AOSP (chưa kiểm trong repo) | Mirror đã archive. Chưa kiểm repo chính android.googlesource.com |
| GNOME vi | https://l10n.gnome.org/teams/vi/ , wiki https://wiki.gnome.org/GnomeVi | Bản dịch theo module, không có glossary riêng tìm thấy | Thường GPL (chưa kiểm) | Repo nhóm trống |
| KDE vi | https://l10n.kde.org/team-infos.php?teamcode=vi | `svn co svn://anonsvn.kde.org/home/kde/branches/stable/l10n-kf6/vi/messages` (lệnh lấy từ trang) | Chưa kiểm | Dạng file `.po` |
| Google (Android style guide, Material) | **Không thấy** glossary tiếng Việt công khai | — | — | Không tìm thấy trong phiên này |

Gợi ý: đối chiếu cả Microsoft + Apple + Pontoon cho cùng một thuật ngữ (ví dụ "Settings", "Sign in"). Ba hãng thường **dịch khác nhau**. Cần chọn một nhà làm chuẩn cho agent.

---

## 6. Văn bản mẫu theo thể loại

Chỉ liệt kê nguồn thật, đã thấy link.

| Thể loại | Nguồn | Link | Ghi chú | Xác nhận |
|---|---|---|---|---|
| Văn bản hành chính | NĐ 30/2020/NĐ-CP, Phụ lục III (đã có sẵn) | — | Không tìm lại | theo yêu cầu |
| Chính tả, thuật ngữ | Quyết định 240/QĐ ngày 05/03/1984, Bộ Giáo dục | https://luatvietnam.vn/giao-duc/quyet-dinh-240-qd-1984-ve-chinh-ta-tieng-viet-va-ve-thuat-ngu-tieng-viet-160366-d1.html | Quy định chính tả duy nhất có văn bản chính thức. Chưa kiểm còn hiệu lực. Có bài phản biện "không bảo đảm nguyên tắc tên riêng" | [mở] |
| Hợp đồng xây dựng | Thông tư 02/2023/TT-BXD (kèm mẫu hợp đồng thi công, tư vấn…) | https://vanban.chinhphu.vn/?pageid=27160&docid=207653 | Hiệu lực 20/04/2023. Bản cũ 09/2016 (https://congbao.chinhphu.vn/van-ban/thong-tu-so-09-2016-tt-bxd-19374.htm) | [mở] cho ngày |
| Hợp đồng lao động | Mẫu kèm Nghị định 145/2020/NĐ-CP, Thông tư 10/2020/TT-BLĐTBXH | https://luatvietnam.vn/lao-dong/nghi-dinh-145-2020-huong-dan-thi-hanh-dieu-kien-lao-dong-va-quan-he-lao-dong-195612-d1.html | Chưa kiểm còn hiệu lực 2026 (có Bộ luật Lao động mới có thể thay) | snippet |
| Hợp đồng theo mẫu | Thông tư 42/2025/TT-BCT về danh mục phải đăng ký hợp đồng theo mẫu | https://baochinhphu.vn/danh-muc-san-pham-hang-hoa-dich-vu-phai-dang-ky-hop-dong-theo-mau-dieu-kien-giao-dich-chung-102250626144222617.htm | Là danh mục, không phải văn mẫu. Hữu ích để biết nhóm hàng phải có hợp đồng mẫu | snippet |
| Đấu thầu | Thông tư 22/2024/TT-BKHĐT (mẫu hồ sơ đấu thầu) | https://thuvienphapluat.vn/van-ban/Dau-tu/Thong-tu-22-2024-TT-BKHDT-cung-cap-thong-tin-ve-lua-chon-nha-thau-tren-He-thong-mang-dau-thau-quoc-gia-619403.aspx | Chưa kiểm hiệu lực hiện hành | snippet |
| Báo cáo thống kê (giọng hành chính, số liệu) | NSO: Báo cáo tình hình kinh tế - xã hội quý III và 9 tháng 2026 | https://www.nso.gov.vn/bai-top/2026/10/bao-cao-tinh-hinh-kinh-te-xa-hoi-quy-iii-va-9-thang-nam-2026/ | Đăng 03/10/2026. Văn bản **mới**, có thể kiểm giọng hiện hành. Thông cáo báo chí cùng kỳ: https://www.nso.gov.vn/du-lieu-va-so-lieu-thong-ke/2026/10/thong-cao-bao-chi-tinh-hinh-kinh-te-xa-hoi-quy-iii-va-9-thang-nam-2026/ | trang tìm kiếm |
| Báo cáo kinh tế | World Bank, "Điểm lại: Cập nhật Tình hình Kinh tế Việt Nam" | https://www.worldbank.org/vi/country/vietnam/publication/taking-stock-viet-nam-economic-update-march-2025 | Bản 03/2025 và 09/2025. Bản tiếng Việt khả năng dịch từ tiếng Anh, giọng dịch cần kiểm. Giấy phép: chưa kiểm (WB thường CC BY 3.0 IGO, chưa mở trang) | snippet |
| Báo cáo kinh tế | World Bank, "Cập Nhật Kinh Tế Vĩ Mô Việt Nam" (Vietnamese) | https://documents.worldbank.org/en/publication/documents-reports/documentdetail/099629501262657260 | Trang tải chỉ hiện khung, chưa đọc nội dung PDF | snippet |
| Báo cáo kinh tế | VEPR, Báo cáo Thường niên Kinh tế Việt Nam | http://vepr.org.vn/533/ebooks/1440260/bao-cao-thuong-nien-kinh-te-viet-nam.html | Nhiều năm, tác giả học thuật viết gốc tiếng Việt. Bản 2025 do VEPR giới thiệu toàn văn trên Facebook | snippet |
| Sổ tay phong cách tòa soạn | Tuổi Trẻ, VnExpress | **Không thấy** công bố | Tuổi Trẻ có bài luận bàn về việc cần chuẩn văn phong chung (https://tuoitre.vn/cau-chuyen-tieng-viet-co-the-chuan-hoa-tieng-viet-181459.htm) | [mở] |
| Sổ tay biên tập VTV | Chỉ thấy bản đăng trên Studocu, không phải nguồn gốc | — | **Không khuyến nghị**, chưa xác thực | snippet |
| Đạo đức nghề báo | Hội Nhà báo Việt Nam, Quyết định 483/QĐ-HNBVN (16/12/2016), 10 điều | https://nhandan.vn/10-dieu-quy-dinh-dao-duc-nghe-nghiep-nguoi-lam-bao-viet-nam-post885757.html | Không phải style guide ngôn ngữ | snippet |
| MXH / blog | Không có "giọng chuẩn". Dùng ViLexNorm để biết dạng viết tắt, tiếng lóng | https://github.com/ngxtnhi/vilexnorm | CC BY-NC-SA | [gh] |
| Chuỗi giao diện | Microsoft/Apple/Mozilla (mục 5) | — | — | — |

---

## 7. Điểm mù

1. **Không có số đo nhiễm AI/dịch máy riêng cho web tiếng Việt.** Tìm ba hướng đều không ra (R15). Số nhiễm tiếng Anh của Pew (R17) không áp dụng được.
2. Ước tính ~28% FineWeb-2 vi thuộc 2023-24 (R04) dựa trên 29 khối mẫu. Cần mẫu lớn hơn nếu muốn cố định con số.
3. Dump Wikipedia vi **trước 11/2022** chưa thấy. Có thể tìm trên archive.org hoặc HF cũ. Chưa kiểm.
4. Ngày crawl của HPLT v2.0 và mC4 3.1.0 chưa kiểm.
5. Giấy phép Leipzig, Hán Nôm (hvdic), Microsoft Terminology, Pontoon chưa đọc được hoặc không thấy trên trang.
6. Chưa chạy hunspell thật, LanguageTool-ngoài, mô hình sửa lỗi bmd1905, VietAIDetector.
7. Phép thử hunspell dùng 6 câu tự soạn, độc lập với các bộ VSEC. Chưa đo precision/recall chuẩn trên VSEC.
8. Nhiều văn bản pháp luật chưa kiểm còn hiệu lực 2026 (Quyết định 240/QĐ 1984, Thông tư 02/2023/TT-BXD, NĐ 145/2020).
9. World Bank, VEPR chỉ thấy qua snippet, chưa đọc PDF để chấm giọng văn. World Bank bản Việt khả năng là dịch từ tiếng Anh.
10. Không có VietLex tìm thấy. Không có glossary Google tiếng Việt.
11. Tuổi Trẻ bài luận không rõ năm đăng. Không kiểm xem VnExpress/Tuổi Trẻ có tài liệu nội bộ chưa công bố.
12. Trang Microsoft Terminology Search là Power BI, chưa xác nhận có export hàng loạt.

---

## 8. Query đã chạy

Serper (gl=vn, hl=vi nếu tiếng Việt):
- AI-generated text contamination web corpus FineWeb multilingual machine translated content share
- machine-translated web content multilingual low-resource languages share … Shocking Amount …
- Vietnamese web AI-generated content proportion detection
- viTenTen Vietnamese corpus Sketch Engine tokens
- VLSP resources Vietnamese corpus download license vlsp.org.vn
- Vietnamese Treebank VTB size sentences license
- UIT-ViQuAD UIT-VSFC UIT-ViNewsQA dataset license UIT NLP group
- VSEC Vietnamese spelling error correction dataset
- ViLexNorm Vietnamese lexical normalization dataset
- Free Vietnamese Dictionary Project Hồ Ngọc Đức download license
- Từ điển Hồ Ngọc Đức tải về giấy phép GPL stardict
- Thiều Chửu từ điển Hán Việt điều khoản sử dụng hvdic thivien
- Wiktionary tiếng Việt mục từ dump giấy phép CC BY-SA
- danh sách từ tiếng Việt wordlist github âm tiết từ ghép 74000 từ
- Microsoft Terminology Service API download terminology localization glossaries Vietnamese
- Microsoft Language Portal retired terminology search replaced
- applelocalization.com Vietnamese terms
- Pontoon Mozilla Vietnamese vi locale terminology
- GNOME Vietnamese translation team glossary
- KDE Vietnamese translation vi glossary l10n
- sổ tay phong cách báo chí tòa soạn quy định về chính tả thuật ngữ Tuổi Trẻ
- VnExpress cẩm nang cách viết quy chuẩn ngôn ngữ tòa soạn
- Quy tắc đạo đức nghề nghiệp nhà báo sổ tay phóng viên biên tập viên tiếng Việt PDF
- mẫu hợp đồng Thông tư Bộ Kế hoạch và Đầu tư mẫu hợp đồng xây dựng Thông tư 09/2016 Phụ lục
- World Bank Vietnam Economic Update bản tiếng Việt
- VEPR báo cáo thường niên kinh tế Việt Nam tải về pdf
- Tổng cục Thống kê báo cáo tình hình kinh tế - xã hội quý họp báo pdf
- Cục Thống kê Thông cáo báo chí tình hình kinh tế xã hội Quý III năm 2026
- Thông tư 02/2023/TT-BXD hợp đồng xây dựng mẫu hợp đồng
- Thông tư 05/2024/TT-BKHĐT mẫu hồ sơ mời thầu hợp đồng
- mẫu hợp đồng lao động Nghị định 145/2020 …
- Bộ Tư pháp hợp đồng mẫu hợp đồng theo mẫu điều kiện giao dịch chung …
- Vietnam news agency VNA style guide … ; VTV quy định về cách đọc viết số liệu …
- Từ điển tiếng Việt Viện Ngôn ngữ học Hoàng Phê bản số hóa tải
- Quyết định 240/QĐ 1984 chính tả tiếng Việt thuật ngữ …
- Tuổi Trẻ Online quy chuẩn ngôn ngữ …
- Leipzig Corpora Collection Vietnamese vie corpus download wortschatz

Khác:
- `gh api repos/<owner>/<repo>` cho: binhvq/news-corpus, 1ec5/hunspell-vi, undertheseanlp/underthesea, undertheseanlp/dictionary, VinAIResearch/PhoBERT, duyvuleo/VNTC, vncorenlp/VnCoreNLP, languagetool-org/languagetool, LibreOffice/dictionaries, duyet/vietnamese-wordlist, VSEC2021/VSEC, ngxtnhi/vilexnorm, mynlp/niivtb, trieuntu/VietAIDetector, bmd1905/vietnamese-correction, trungtv/pyvi, vntk/vntk-cli, mozilla-l10n/styleguides, aosp-mirror/platform_frameworks_base, kishikawakatsumi/applelocalization-web. Nhiều tên repo tôi đoán trả 404, bỏ qua.
- HF API: HuggingFaceFW/fineweb-2, uonlp/CulturaX, oscar-corpus/OSCAR-2301, HPLT/HPLT2.0_cleaned, wikimedia/wikipedia, vietgpt/binhvq_news_vi, bmd1905/*, SEACrowd/vilexnorm, statmt/cc100.
- datasets-server `/rows` lấy mẫu FineWeb-2 vie_Latn (30 lần gọi, 29 khối hợp lệ).
- MediaWiki API: siteinfo vi.wikipedia, vi.wiktionary; rightsinfo.
- `curl -I`: Wikipedia dump, Wiktionary dump, CC-100 vi, Microsoft TBX zip, Leipzig tar.gz.
- Mở trang: Sketch Engine viTenTen, VLSP resources, Microsoft Terminology/Language resources, Pontoon vi, applelocalization, KDE vi, GNOME l10n, languagetool.org/languages, LanguageTool API (`language=vi` thử trực tiếp), arXiv 2401.05749, arXiv 2608.25478, Pew methodology, Tuổi Trẻ bài luận, everyhue.me, hvdic.thivien.net, Wiktionary:Nguồn gốc/FVDP, data.statmt.org/cc-100.
- Công cụ: jina-read thử với arXiv trả nội dung rỗng/sai, đổi sang `curl` trực tiếp. SearXNG không dùng. Không cần `--stop`.

Câu hỏi còn mở:
1. Có cần tôi lấy mẫu lớn hơn FineWeb-2 vi theo trường `date` để có tỷ lệ 2023-24 chắc hơn không?
2. Có cần tìm dump Wikipedia vi trước 11/2022 trên archive.org không?
3. Có muốn chạy thử `bmd1905/vietnamese-correction-v2` và VietAIDetector để đo hữu dụng thật không?
