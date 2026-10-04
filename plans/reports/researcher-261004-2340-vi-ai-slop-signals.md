# Nhóm A: dấu hiệu văn AI trong tiếng Việt

Ngày thu: 04/10/2026 (Asia/Saigon). Người thu: agent desk research nhóm A. Chỉ nguồn công khai.

## 0. Kết luận ngắn

- Không thấy nghiên cứu nào có tên tác giả đếm tần suất cụm từ AI trong TIẾNG VIỆT. Đây vẫn là điểm mù thật. Query đã thử ở mục 5.
- Bằng chứng tiếng Việt chỉ có 4 loại: (a) bài kinh nghiệm của cộng đồng/biên tập (BrandsVietnam), (b) blog thương mại, (c) báo dịch từ nguồn Anh/Mỹ, (d) repo của một cá nhân (GitHub). Không loại nào là số liệu đếm.
- Bằng chứng số liệu mạnh chỉ có ở TIẾNG ANH (Kobak, Liang, Russell). Không suy thẳng sang tiếng Việt.
- Hai bài phát hiện văn AI tiếng Việt (ViDetect, VietBinoculars/VietAIDetector) dùng bộ phân loại học máy hoặc thống kê perplexity. Họ không báo cáo cụm từ hay cấu trúc nào làm "lộ".
- Cụm có ≥3 nguồn tiếng Việt khá độc lập: "không chỉ… mà còn…" và dấu gạch ngang dài (em dash). Cụm "trong bối cảnh…" có 2 nguồn. Phần lớn cụm trong danh sách nghi vấn của đề bài KHÔNG có nguồn (xem mục 2).
- Bằng chứng nói tell nằm ở cả từ vựng lẫn cấu trúc. Chỉ đổi từ chưa đủ (Bouchard, Wikipedia, Juzek).
- Con người nhận diện: người dùng LLM nhiều đạt ~93% (tiếng Anh, 300 bài), người ít dùng gần ngẫu nhiên. Mẫu nhỏ, tiếng Anh.

## 1. Bảng claim

Ghi chú cột "Mở": GỐC = đã mở trang gốc bằng jina-read; WF = mở bằng WebFetch (bản tóm tắt do công cụ trả, nguyên văn chưa kiểm); SNIP = chỉ thấy snippet trong kết quả tìm; CHẶN = bị chặn/paywall.

### 1.1 Nguồn tiếng Việt

| ID | Claim | Nguyên văn ngắn | URL | Ngày | Tác giả / tổ chức | Loại | Mở |
|---|---|---|---|---|---|---|---|
| A01 | Câu mở "Trong bối cảnh ngành … phát triển không ngừng" là kiểu AI ưa dùng | "Trong bối cảnh ngành [XYZ] đang phát triển không ngừng…" | https://help.brandsvietnam.com/vi/article/dau-hieu-nhan-biet-noi-dung-duoc-viet-boi-ai-3zy07d/ | cập nhật 23/09/2025 | Admin Brands Vietnam (cộng đồng Marketing) | blog/hướng dẫn cộng đồng (gốc) | GỐC |
| A02 | Cấu trúc và từ nối máy móc: "không chỉ… mà còn", "tưởng chừng… nhưng", "Hơn nữa", "Thêm vào đó", kết bằng "Tóm lại", "Kết luận là" | "‘không chỉ… mà còn…’, ‘tưởng chừng… nhưng…’" | như A01 | như A01 | như A01 | như A01 | GỐC |
| A03 | Thuật ngữ sáo rỗng "tạo giá trị", "đồng bộ hoá mục tiêu" | "‘tạo giá trị’, ‘đồng bộ hoá mục tiêu’" | như A01 | như A01 | như A01 | như A01 | GỐC |
| A04 | Dấu gạch ngang dài xuất hiện 2-3 lần trong đoạn ngắn là tín hiệu | "xuất hiện đến 2-3 lần trong một đoạn văn ngắn thì khả năng cao đó là nội dung AI" | như A01 | như A01 | như A01 | như A01 | GỐC |
| A05 | Chia bullet, mở bằng "Dưới đây là một số gợi ý…"; ý nông, trùng | "‘Dưới đây là một số gợi ý…’" | như A01 | như A01 | như A01 | như A01 | GỐC |
| A06 | Bịa ví dụ/chiến dịch không có thật; để sót prompt; giọng không nhất quán giữa các đoạn | "phần lớn ví dụ đều do chatbot này bịa ra" | như A01 | như A01 | như A01 | như A01 | GỐC |
| A07 | Phương pháp A01-A06: 1 prompt, 1 chủ đề (Ambient Advertising), 2 mô hình (ChatGPT, Gemini), bài ~2.000 chữ. Không phải đếm tần suất | "một bài blog khoảng 2.000 chữ về chủ đề Ambient Advertising" | như A01 | như A01 | như A01 | như A01 | GỐC |
| A08 | Hai trang ai-hay.vn chép lại A01-A06, có dẫn link BrandsVietnam. KHÔNG độc lập | (không trích) | https://ai-hay.vn/cac-dau-hieu-nhan-biet-noi-dung-do-ai-tao-ra-pN1UmIYCY04 ; https://ai-hay.vn/lam-the-nao-de-phan-biet-van-ban-ai-va-van-ban-nguoi-viet-pN1UmHFx8xC | không rõ | AI Hay (hỏi-đáp tổng hợp) | bản sao | GỐC |
| A09 | Bài Facebook của chính Brands Vietnam: "phiên bản tiếng Việt của not only… but also", đặt dấu phẩy trước "và", nhiều khởi ngữ, gạch ngang chú thích | "Các version tiếng Việt của not only... but also..." | https://www.facebook.com/BrandsVietnam/posts/m%E1%BB%99t-d%E1%BA%A5u-hi%E1%BB%87u-khi%E1%BA%BFn-b%E1%BA%A1n-d%E1%BB%85-d%C3%A0ng-nh%E1%BA%ADn-bi%E1%BA%BFt-c%C3%A1i-n%C3%A0y-chatgpt-vi%E1%BA%BFt-ch%E1%BA%AFc-lu%C3%B4n-/1183554327130202/ | không rõ | Brands Vietnam | cùng tổ chức A01 (không độc lập), mạng xã hội | SNIP (jina-read ra rỗng) |
| A10 | Mẫu "phủ định rồi khẳng định" có 3 biến thể tiếng Việt; tần suất mới là vấn đề, vì Shakespeare/Churchill cũng dùng | "‘không chỉ... mà còn...’, ‘điều quan trọng không phải là... mà là...’, ‘đây không đơn thuần là...’" | https://congdankhuyenhoc.vn/khi-ai-co-giong-van-rieng-va-con-nguoi-bat-dau-viet-giong-may-179260713181911472.htm | 13/07/2026 | Đỗ Tho, báo Công dân & Khuyến học | báo (tổng hợp lại từ Pangram/The Atlantic, không phải khảo sát tiếng Việt) | GỐC |
| A11 | Cùng bài A10 nêu: theo Pangram, cấu trúc này xuất hiện ở văn AI "gấp khoảng ba lần" văn người | "với tần suất gấp khoảng ba lần so với văn bản do con người viết" | như A10 | 13/07/2026 | như A10, dẫn Pangram | báo, thứ cấp. Số 3x là TIẾNG ANH | GỐC (chưa thấy nguồn gốc Pangram, xem A33) |
| A12 | Em dash bị coi là dấu hiệu AI; OpenAI sửa để ChatGPT tôn trọng yêu cầu không dùng | "dấu hiệu nhận biết văn bản AI vì chatbot thường sử dụng chúng" (bản tóm tắt WF) | https://vnexpress.net/chatgpt-khac-phuc-dau-gach-ngang-dai-4964281.html | 15/11/2025 | Thu Thảo (dịch Business Insider, TechCrunch) | báo, bản dịch | WF |
| A13 | Dấu hiệu độc giả "truyền tai": nhiều gạch ngang, cụm sáo rỗng; Guardian lưu ý đây cũng là đặc điểm viết của người, AI học lại. Nghiên cứu 2025: AI nhiều danh từ, ít đại từ và tính từ làm vị ngữ | "Nội dung có nhiều dấu gạch ngang, cụm từ sáo rỗng." (WF) | https://vnexpress.net/ai-tac-dong-len-ngon-ngu-the-nao-5103242.html | 31/07/2026 | Thảo Uyên (dịch Guardian, Scientific American) | báo, bản dịch, nói về tiếng Anh | WF |
| A14 | Văn AI: nhiều gạch ngang dài, lặp cụm, "không phải X, mà là Y", ngữ pháp chuẩn xác bất thường | "nhiều dấu gạch ngang dài, lặp lại cụm từ" (WF) | https://vnexpress.net/cong-cu-nhan-hoa-van-ban-giup-che-dau-vet-ai-len-ngoi-5094235.html | không lấy được | VnExpress (nguồn dịch không rõ) | báo | WF |
| A15 | Cụm sáo rỗng "Trong thế giới ngày nay", "Không thể phủ nhận rằng", "Nhìn chung"; câu đều độ dài (burstiness). Không có số liệu | "Những cụm từ sáo rỗng như “Trong thế giới ngày nay”, “Không thể phủ nhận rằng”, “Nhìn chung”" | https://www.finhay.com.vn/meo-dung-chatgpt-khong-bi-van-mau-robotic | khoảng 05/2026 (theo đường dẫn ảnh, chưa kiểm ngày đăng) | Finhay (công ty fintech) | blog thương mại | GỐC |
| A16 | Repo cá nhân có catalog mẫu tiếng Việt: (L01) "đóng vai trò … trong việc"; (L03) lời khen "đột phá/vượt trội/đẳng cấp/ấn tượng/tuyệt vời"; (D02) "hy vọng những thông tin trên sẽ hữu ích"; (S02) "không chỉ … mà còn" lặp; (S03) "đồng thời/qua đó/từ đó" dày. Tự gắn nhãn heuristic, độ tin cậy medium, S02 false_positive_risk high | "Lạm dụng cấu trúc "đóng vai trò ... trong việc" khi một động từ trực tiếp rõ hơn." | https://github.com/longhang2004/vietnamese-humanizer (patterns/humanizer.yml) | bài giới thiệu 21/07/2026 | Hàng Nhựt Long (cá nhân) | repo cá nhân, không kiểm chứng bằng corpus (chưa thấy) | GỐC (raw file) |
| A17 | Cùng repo: "Pattern là gợi ý review, không phải danh sách từ cấm"; một tín hiệu đơn lẻ không đủ kết luận | "Pattern là gợi ý review, không phải danh sách từ cấm." | https://raw.githubusercontent.com/longhang2004/vietnamese-humanizer/main/skills/humanizer-vi/references/patterns.md | 2026 | như A16 | repo | GỐC |
| A18 | Cùng tác giả (bài Facebook): lỗi AI tiếng Việt "đúng thì đúng, nhưng nghe vẫn cứ sai sai, cứ bị google dịch" (giả thuyết văn dịch) | "nghe vẫn cứ sai sai, cứ bị google dịch thế nào đó" | https://www.facebook.com/groups/aiartworksvn/posts/4474821566064026/ | 21/07/2026 | Hàng Nhựt Long, nhóm Nghiện AI | forum/Facebook | GỐC |
| A19 | Bài dịch: văn AI theo "bài luận hình thức" 5 đoạn, kết "Khi trí tuệ nhân tạo tiếp tục phát triển…", điều hướng "như đã đề cập trước đó"; đổi vài từ chỉ là giải pháp tạm | "việc chỉ thay đổi từ vựng chỉ là giải pháp tạm thời" | https://vnreview.vn/threads/chuyen-gia-ai-tiet-lo-bi-quyet-loai-bo-mui-ai-viet-bang-ngon-ngu-don-gian-tu-nhien-nhu-con-nguoi.79367/ | không rõ | VnReview (dịch lại, ảnh từ gtimg, nguyên bản Towards AI/Bouchard) | bản dịch của bản dịch | GỐC |
| A20 | Bản gốc tiếng Anh của A19: sửa cấu trúc trước từ | "you can’t just delete delve; you have to change the skeleton" | https://www.louisbouchard.ai/ai-editing/ | 15/01/2026 | Louis-François Bouchard (Towards AI) | blog tác giả | GỐC |
| A21 | Bài hướng dẫn nhận diện: dịch từ guide tiếng Anh ("bước tiến đúng hướng", "tảng băng chìm"); nói chưa có công cụ nào tin cậy cho tiếng Việt | "chưa có công cụ nào hoàn toàn đáng tin cậy khi kiểm tra các văn bản bằng tiếng Việt" | https://tex.vn/ai-infor/lam-the-nao-de-nhan-dien-noi-dung-do-ai-viet-muc-do-tin-cay-den-dau-1021 | không rõ (ảnh T9/2024) | tex.vn | blog giáo dục, văn dịch từ tiếng Anh | GỐC |
| A22 | Dạy học sinh phân tích đoạn văn AI để nhận "chi tiết sáo rỗng, thông tin thiếu chính xác"; không nêu cụm cụ thể | "nhận diện chi tiết sáo rỗng, thông tin thiếu chính xác" | https://dantri.com.vn/tam-diem/khi-thay-co-cam-hoc-sinh-dung-ai-viet-bai-20260512134852075.htm | 12/05/2026 | Dân trí | báo | GỐC |
| A23 | Em dash không phải dấu gõ tự nhiên của tiếng Việt: dài gạch ngang (–) quy chuẩn bằng hai gạch nối | "dấu gạch ngang (–) dài bằng hai dấu gạch nối (-)" | https://www.facebook.com/TGVConfession/posts/tgv4623t%E1%BA%A1i-sao-c%C3%B3-ng%C6%B0%E1%BB%9Di-c%E1%BB%A9-th%E1%BA%A5y-l%C3%A0-m%E1%BA%B7c-%C4%91%E1%BB%8Bnh-cho-r%E1%BA%B1ng-l%C3%A0-s%E1%BB%AD-d%E1%BB%A5ng-ai-chat-gpt-v%E1%BA%ADy-/743985188260449/ | không rõ | TGV Confession (trang confession) | mạng xã hội | SNIP |
| A24 | Bình luận Voz/Reddit: "văn AI" bị chê; một người cho rằng người có chuyên môn "nhận ra ngay". Không nêu cụm | "Người có chuyên môn sẽ nhận ra ngay và không thích văn AI đâu." | https://www.reddit.com/r/vozforums/comments/1ebkdj2/qu%C3%A1_l%E1%BA%A1m_d%E1%BB%A5ng_ai/ | không rõ | người dùng r/vozforums | forum | SNIP (Reddit CHẶN jina) |
| A25 | Bình luận Voz Party: "Văn AI nó chỉn chu hơn… lặp đi lặp lại"; chê giọng báo bợ trên YouTube. Ý kiến, không cụm | "Văn AI nó chỉn chu hơn khối thằng có đều nó 1 tuồng lặp đi lặp lại." | https://voz.party/d/794648-dung-ai-lam-bao-cao-cau-tha-nhieu-loi-khong-the-chap-nhan-so-cong-thuong-bi-chu-tich-tinh-nhac-nho | không rõ | người dùng voz.party | forum | SNIP |

### 1.2 Nghiên cứu phát hiện văn AI tiếng Việt

| ID | Claim | Nguyên văn / số | URL | Ngày | Tác giả | Loại | Mở |
|---|---|---|---|---|---|---|---|
| A26 | ViDetect: 6.800 bài văn (3.400 người, 3.400 AI). Người: bài văn mẫu trên trang giáo dục, đăng trước 2021, ≥256 từ. AI: ChatGPT 3.5/4.0 VIẾT LẠI chính các bài đó | "ChatGPT 3.5 and ChatGPT 4.0… rewrites" (đoạn 3.1) | https://arxiv.org/abs/2405.03206 | 06/05/2024 | Quang-Dan Tran, Van-Quan Nguyen, Quang-Huy Pham, K. B. Thang Nguyen, Trong-Hop Do (UIT, ĐHQG TP.HCM) | preprint arXiv, chưa thấy dấu phản biện | GỐC (pdf) |
| A27 | ViDetect, thống kê: độ dài TB người 323 vs AI 301 từ; câu TB 13,69 vs 12,18; đoạn TB 2,71 vs 3,84 (bảng in). Văn bản bài nói AI "longer paragraphs" nhưng bảng cho AI NHIỀU đoạn hơn: mâu thuẫn trong bài, bảng 2 bị lỗi cột Min/Max | "Avg. Length 323 301" | như A26 | 2024 | như A26 | như A26 | GỐC |
| A28 | ViDetect tiền xử lý xóa dấu câu, số, stop word, hạ chữ thường. Nên mô hình KHÔNG học được tell về dấu câu/từ nối | "We remove punctuation, special characters, numbers…" | như A26 | 2024 | như A26 | như A26 | GỐC |
| A29 | ViDetect kết quả: accuracy TB 0,8580 / 0,8721 / 0,8437 tại 64/128/256 token (5 mô hình: ViT5, BARTpho, PhoBERT, mDeBERTa-v3, mBERT). Không có phân tích đặc trưng ngôn ngữ nào "lộ" | "average accuracy is recorded as 0.8580 for 64 tokens" | như A26 | 2024 | như A26 | như A26 | GỐC |
| A30 | VietBinoculars: zero-shot, dựa perplexity; >99% accuracy/F1/AUC trên tập ngoài miền. Người: tin tức Kaggle (đến 07/2022) và tác phẩm Vũ Trọng Phụng; AI: mô hình mở (Gemma-3-12B-it…). Không nêu tell đọc được | "achieves over 99% in all two domains of accuracy, F1-score, and AUC" | https://arxiv.org/abs/2509.26189 | 2025 | TH Nguyen | preprint | GỐC (abs + pdf) |
| A31 | VietAIDetector: công cụ mã mở, PhoGPT-4B, chia cửa sổ cho văn dài; so với GPTZero trên 3 tập tin tức do mô hình mới sinh. Giới hạn: hiệu năng phụ thuộc mô hình nền, thay đổi theo miền | "Detection performance depends on the quality of the underlying language models and may vary across domains." | https://arxiv.org/abs/2608.25478 | 26/08/2026 | Trieu Hai Nguyen (ĐH Nha Trang), Van-Dung Hoang (ĐH SPKT TP.HCM) | preprint gửi Elsevier | GỐC (html). Số kết quả trong hình, chưa đọc |

### 1.3 Nghiên cứu tiếng Anh (không suy sang tiếng Việt)

| ID | Claim | Nguyên văn / số | URL | Ngày | Tác giả | Loại | Mở |
|---|---|---|---|---|---|---|---|
| A32 | Kobak: 15,1 triệu abstract PubMed 2010-2024 (tiếng Anh). Từ "dư" (excess) 2024: 454 từ (so 190 năm 2021 thời COVID); 343 lemma độc nhất. Từ nội dung chiếm 51,3%, từ phong cách 45,2% trong 900 từ dư 2013-2024. 2024: 379 từ phong cách, 66% động từ, 14% tính từ | "at least 13.5% of 2024 abstracts were processed with LLMs" | https://arxiv.org/abs/2406.07016 ; https://pmc.ncbi.nlm.nih.gov/articles/PMC12219543/ | 06/2024; Sci. Adv. 11(27), 02/07/2025 | Dmitry Kobak et al. | tạp chí (bản gốc) | GỐC |
| A33 | Kobak, tỷ lệ tần suất r (từ ít gặp): delves 28,0; underscores 13,8; showcasing 10,7. Khoảng cách δ (từ thường): potential 0,052; findings 0,041; crucial 0,037. Cận dưới dùng LLM ≥13,5%, có tập con tới 40% | "delves (r=28.0), underscores (r=13.8), and showcasing (r=10.7)" | như A32 | như A32 | như A32 | như A32 | GỐC |
| A34 | Liang et al. (ICML 2024): trong review ICLR 2024, "commendable", "meticulous", "intricate" tăng 9,8 / 34,7 / 11,2 lần xác suất trong câu. 6,5%-16,9% review có thể bị LLM sửa đáng kể | "9.8, 34.7, and 11.2-fold increases" | https://arxiv.org/abs/2403.07183 | 03/2024 | Weixin Liang et al. | hội nghị | GỐC (pdf) |
| A35 | Liang et al. (Nature Human Behaviour 2025): 950.965 bài 01/2020-02/2024; khoa học máy tính tăng đến 17,5%, toán và Nature đến 6,3% | "up to 17.5%" | https://arxiv.org/abs/2404.01268 | 2024-2025 | Weixin Liang et al. | tạp chí | GỐC (abs). Con số 22,5% từ phys.org: SNIP, chưa kiểm |
| A36 | Juzek & Ward (COLING 2025): 21 "focal words"; chưa chứng minh nguyên nhân; RLHF có thể góp phần | "We fail to find evidence that lexical overrepresentation is caused by model architecture" | https://arxiv.org/abs/2412.11385 | 12/2024 | Tom Juzek, Zina Ward | hội nghị | GỐC (abs) |
| A37 | Yakura et al.: từ ChatGPT ưa dùng (delve, comprehend, boast, swift, meticulous) tăng đột ngột trong lời nói tự nhiên: 737.083 giờ, 824.634 tập podcast; thí nghiệm N=496. Người đang bắt chước LLM | "humans internalize the lexical choices of large language models" | https://arxiv.org/abs/2409.01754 | 09/2024 | Hiromu Yakura et al. | preprint | GỐC (abs) |
| A38 | Reinhart et al. (PNAS 2025): dùng đặc trưng ngữ pháp/tu từ của Biber; mô hình tinh chỉnh theo hướng dẫn khác người rõ hơn mô hình nền; khác biệt không mất khi mô hình lớn hơn | "LLMs struggle to match human stylistic variation" | https://arxiv.org/abs/2410.16107 | 10/2024; v2 21/08/2025 | Alex Reinhart et al. | tạp chí | GỐC (abs). Chi tiết (mệnh đề phân từ hiện tại) từ snippet PNAS |
| A39 | Russell et al.: 5 người "chuyên gia" (hay dùng LLM để viết), 300 bài báo tiếng Anh: đa số phiếu sai 1/300; TPR 92,7%, FPR 3,3% (thí nghiệm 1). Người ít dùng LLM gần ngẫu nhiên | "annotators who frequently use LLMs for writing tasks excel at detecting AI-generated text" | https://arxiv.org/abs/2501.15654 | 26/01/2025; v2 19/05/2025 | Jenna Russell, Marzena Karpinska, Mohit Iyyer | preprint | GỐC (html) |
| A40 | Russell: lời giải thích của chuyên gia nhắc từ vựng ("AI vocabulary": vibrant, crucial, significantly) nhiều nhất (bảng 3: 53,1%), sau đó cấu trúc câu (35,9%): "not only … but also", liệt kê ba ý. Từ vựng ít được nhắc hơn khi bài đã "humanize". Người ít dùng LLM hay gán nhầm từ "sang", giọng trung tính là AI; chuyên gia biết người viết mắc lỗi ngữ pháp nhiều hơn AI | "AI-generated sentences follow predictable patterns (e.g., high frequency of “not only … but also …”" | như A39 | 2025 | như A39 | như A39 | GỐC. Cách tính % (GPT-4o mã hóa lời giải thích) chưa kiểm sâu |
| A41 | Cheng et al.: 30 phần mở đầu bài báo y khoa mô phỏng, 5 điều kiện, 5 người chấm mù: độ chính xác chung 19% ("không khác ngẫu nhiên"); người viết 17%, AI hoàn toàn 10%. 3 công cụ phát hiện phân biệt được điều kiện nhưng điểm lệch nhau (ICC 0,57-0,95) | "overall accuracy of 19%, indistinguishable from chance" | https://pmc.ncbi.nlm.nih.gov/articles/PMC12752165/ | 2025 | A. Cheng et al. | tạp chí | GỐC |
| A42 | Penn State (Dongwon Lee): người phân biệt AI chỉ ~53% khi đoán mò là 50%. Điều kiện thí nghiệm không nêu trong bài phỏng vấn | "can distinguish AI-generated text only about 53% of the time" | https://www.psu.edu/news/information-sciences-and-technology/story/qa-increasing-difficulty-detecting-ai-versus-human | không rõ | Dongwon Lee (Penn State) | phỏng vấn trường | GỐC |
| A43 | Wikipedia (trang hướng dẫn, không phải nghiên cứu): chia nhóm dấu hiệu; "words to watch" (pivotal, underscore, serves as, tapestry…); tránh "is/are" dùng "serves as"; negative parallelism "not just X, but Y"; AI "hồi quy về trung bình": thay chi tiết cụ thể bằng khen chung | "Humans are notoriously bad at distinguishing human and LLM-generated text." | https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing | sửa đến ít nhất 11/2025 | cộng đồng biên tập Wikipedia | tài liệu cộng đồng | GỐC |
| A44 | Pangram (hãng phát hiện AI): trang liệt kê từ/cụm (delve, tapestry, testament, in conclusion…); không có số tần suất trên trang. Nói "AI Names": 60-70% tên trong bài ChatGPT/Claude là Emily hoặc Sarah | "60-70% of names in AI-generated articles… are either “Emily” or “Sarah”" | https://www.pangram.com/blog/comprehensive-guide-to-spotting-ai-writing-patterns | không rõ | Pangram Labs | blog hãng, có lợi ích thương mại | GỐC |
| A45 | The Atlantic dẫn Pangram: "Not just X but Y" xuất hiện ~3 lần dày hơn ở văn AI | "appear three times as often in AI writing" | https://www.theatlantic.com/technology/2026/07/ai-chatbot-writing-tic-negative-parallelism/687892/ | 12/07/2026 | The Atlantic | báo | SNIP (paywall, jina ra 402 ký tự). Số liệu gốc Pangram chưa thấy |

## 2. Cụm / cấu trúc ứng viên cho kho

Quy ước "nguồn độc lập": đếm theo tổ chức/tác giả khác nhau, không tính bản sao (A08), cùng tổ chức (A09), bản dịch từ nguồn Anh (A12-A14, A19, A21).
Mức bằng chứng: M = có nguồn tiếng Việt (có thể quá ít); E = chỉ có analog tiếng Anh; P = phỏng đoán, KHÔNG nguồn.

### 2.1 Có nguồn tiếng Việt

| Cụm / cấu trúc | Nguồn độc lập (tiếng Việt) | Nguồn tiếng Anh tương ứng | Mức | Đề xuất viết thay |
|---|---|---|---|---|
| "không chỉ … mà còn …" lặp | 3: BrandsVietnam (A02), Công dân & Khuyến học (A10), repo GitHub (A16). Finhay, VnExpress dịch không nêu đúng cụm | Russell (A40), Wikipedia (A43), Pangram 3x (A45, thứ cấp) | M mạnh nhất | Nêu thẳng hai ý bằng "và"; nếu ý thứ hai mới là điểm chính, chỉ viết ý đó. Nguồn đều nói tần suất mới là lỗi, 1 lần dùng có lý do thì giữ |
| "điều quan trọng không phải là … mà là …", "đây không đơn thuần là …" | 1 (A10); VnExpress A14 nêu dạng "không phải X, mà là Y" (bản dịch) | như trên | M yếu | Nói luôn điều khẳng định, bỏ vế phủ định tự dựng |
| dấu gạch ngang dài (—) | BrandsVietnam (A04), TGV (A23, nói em dash lạ với cách gõ tiếng Việt), VnExpress 3 bài dịch (A12-A14) | Wikipedia (A43); OpenAI đã thêm tùy chọn giảm em dash 11/2025 (A12) | M | Dùng dấu phẩy, dấu chấm hoặc ngoặc đơn; dùng gạch ngang ngắn có khoảng trắng nếu cần. Tell đang yếu đi vì mô hình mới giảm em dash (một bài Medium nói "đã chết", chỉ snippet, blog) |
| "Trong bối cảnh … (đang) phát triển (không ngừng)" | 2: BrandsVietnam (A01), repo GitHub (A16, mẫu L02: chỉ ghi nhận khi chính câu đó không nêu thay đổi cụ thể) | Wikipedia "evolving landscape" (A43) | M | Mở bằng sự kiện, con số, quyết định cụ thể. Nếu cần bối cảnh thì nêu thay đổi thật: "Từ 07/2026, …" |
| "Tóm lại", "Kết luận là…" mở đoạn kết | 1 (A02) | tiếng Anh "In conclusion/In summary" (Wikipedia words-to-watch, A43; A44) | M yếu | Kết bằng thông tin cuối hoặc việc cần làm tiếp |
| "Nhìn chung", "Không thể phủ nhận rằng", "Trong thế giới ngày nay" | 1 (Finhay A15, blog thương mại) | tương tự | M yếu | Bỏ; nói thẳng nhận định |
| "Hơn nữa", "Thêm vào đó" | 1 (A02) | tiếng Anh "Furthermore/Moreover" | M yếu | Bỏ hoặc thay bằng "Ngoài ra" chỉ khi có quan hệ thêm ý thật. Xét theo mật độ cả đoạn |
| "đồng thời", "qua đó", "từ đó" dày | 1 (repo GitHub A16, S03; nói ít nhất 3 lần/đoạn mới tính) | – | M yếu | Tách câu; chỉ giữ từ nối khi có quan hệ nhân quả đã chứng minh |
| "đóng vai trò (quan trọng/then chốt) trong việc …" | 1 (repo GitHub A16, L01, cần ≥2 lần). Đề bài nghi vấn "đóng vai trò quan trọng": ngoài repo này KHÔNG thấy nguồn nào gắn cụm với AI | Wikipedia "a crucial/pivotal … role" (A43); Kobak "crucial" δ=0,037 (A33) | M yếu | Dùng động từ cụ thể: "Quản lý giữ tiến độ bằng cách…" |
| lời khen rỗng "đột phá, vượt trội, đẳng cấp, ấn tượng, tuyệt vời" | 1 (repo GitHub A16, L03) | Kobak style words, Russell (vibrant, crucial) | M yếu | Thay bằng số đo, tính năng, kết quả kiểm chứng được |
| mở bài báo trước nội dung: "Trong bài viết này, chúng ta sẽ cùng tìm hiểu…" | 1 (repo GitHub A16, ví dụ trong README) | – | M yếu | Vào thẳng nội dung |
| kết xã giao "Hy vọng những thông tin trên sẽ hữu ích" | 1 (repo GitHub A16, D02) | – | M yếu | Xóa |
| "tạo giá trị", "đồng bộ hoá mục tiêu" | 1 (A03) | – | M yếu | Nêu việc cụ thể làm ra giá trị gì cho ai |
| mở danh sách "Dưới đây là một số gợi ý…" + bullet nông | 1 (A05; A08 bản sao) | Russell (liệt kê ba ý), vnreview/Bouchard (A19-A20) | M | Viết đoạn văn; chỉ dùng bullet khi là bước hay mục rời |
| bài 5 đoạn đều độ dài; kết "khi AI tiếp tục phát triển…"; nhắc lại "như đã đề cập" | 0 bản gốc tiếng Việt (A19 là dịch Bouchard) | Bouchard (A20), Russell "optimistically vague conclusions" (A39) | E | Bỏ báo hiệu; để độ dài đoạn theo nội dung |
| ví dụ/chiến dịch/nguồn bịa | 1 (A06) | – | M (kiểm sự thật, không phải từ) | Mọi ví dụ phải có nguồn mở được; không có thì bỏ |
| sót prompt trong bài ("Dưới đây là phiên bản…") | 1 (A06) | – | M | Soát trước khi gửi |
| câu đều độ dài, nhịp đều | Finhay (A15), Facebook chuyên gia marketing (SNIP, 1 cá nhân), repo GitHub (S04, confidence low) | Russell "short choppy" (A40) | M yếu, chưa có số đo | Xen câu ngắn/dài; đây là chỉ dấu mật độ chứ không phải cụm |

### 2.2 Không thấy nguồn: đừng đưa vào kho như "cụm cấm"

Đề bài nghi vấn các cụm này. Tìm bằng query ở mục 5, KHÔNG thấy nguồn nào (ngoài snippet nhiễu) gắn chúng với văn AI tiếng Việt:

- "hãy cùng khám phá" (gần nhất: "chúng ta sẽ cùng tìm hiểu", A16)
- "hành trình"
- "bức tranh" / "bức tranh toàn cảnh"
- "góp phần"
- "một cách" (nghĩ là phó từ hóa, không ai nêu)
- "điều này cho thấy"
- "đa dạng và phong phú"
- "thế giới đầy màu sắc"

Có thể đúng. Hiện ở mức P (phỏng đoán). Cách kiểm đề xuất ngoài phạm vi nhóm A: đếm tần suất trên bài tiếng Việt viết trước 2022 so với đầu ra mô hình, theo phương pháp "excess word" của Kobak (A32).

## 3. Phản chứng: danh sách từ cấm vô ích hoặc phản tác dụng

| ID | Ai nói | Nội dung | URL |
|---|---|---|---|
| C01 | Bouchard (A20), VnReview dịch (A19) | Xóa "delve" vẫn còn cảm giác AI vì cấu trúc không đổi; phải sửa khung bài trước | A20 |
| C02 | Wikipedia (A43) | Dấu hiệu chỉ là "potential signs"; con người "notoriously bad"; AI thay chi tiết bằng khen chung → vấn đề là độ cụ thể | A43 |
| C03 | Juzek trong Reuters Institute | "Causality is really hard to show": các từ "delve…" cũng tăng ở podcast không do LLM; có thể là thay đổi ngôn ngữ tự nhiên. Trang có thể vừa dẫn Yakura (người bắt chước AI, A37) | https://reutersinstitute.politics.ox.ac.uk/news/how-ai-generated-prose-diverges-human-writing-and-why-it-matters (mở GỐC; ngày không lấy được, sau 10/2025) |
| C04 | Yakura et al. (A37) | Người đang dùng đúng các từ này trong lời nói → từ đơn lẻ làm chứng cứ AI ngày càng yếu | A37 |
| C05 | Công dân & Khuyến học (A10) | "không chỉ… mà còn…" là thủ pháp tu từ hợp lệ hàng thế kỷ; vấn đề là mật độ | A10 |
| C06 | VnExpress dịch Guardian (A13) | Gạch ngang và sáo rỗng cũng là đặc điểm viết của người, AI học lại | A13 |
| C07 | Repo GitHub (A16-A17) | Gắn false_positive_risk "high" cho "không chỉ… mà còn"; "một tín hiệu đơn lẻ không đủ"; không sửa cụm chỉ vì có trong catalog | A17 |
| C08 | Russell (A40) | Người ít kinh nghiệm hay gán nhầm từ "sang" và giọng trung tính là AI → nhiều dương tính giả; chuyên gia biết người mắc lỗi ngữ pháp nhiều hơn AI | A39 |
| C09 | Salvaggio, blog (31/05/2026) | Grammarly đánh dấu "align with" là "43x more likely to be AI"; người viết nói mình phải viết lại để khỏi bị nghi; sợ bị nghi khiến người né cách viết bình thường | https://mail.cyberneticforests.com/its-not-just-data-its-post-training/ (GỐC) |
| C10 | Cheng et al. (A41), Wikipedia (A43) | Con người và cả công cụ không đáng tin riêng lẻ; không dùng làm bằng chứng duy nhất | A41 |
| C11 | Mô hình mới thay đổi: OpenAI thêm giảm em dash (A12); Thanh Niên 06/05/2026 nói ChatGPT bị "chấn chỉnh" lối nói dài dòng (tiêu đề đã đọc, nội dung chưa kiểm) https://thanhnien.vn/loi-kho-chiu-nhat-tren-chatgpt-da-duoc-khac-phuc-185260506214650393.htm | Tell cụ thể hết hạn nhanh; danh sách phải có ngày | A12 |
| C12 | tex.vn (A21), ViDetect/VietBinoculars (A26-A31) | Chưa có công cụ phát hiện tin cậy tuyệt đối cho tiếng Việt; chính các bài viết nói phụ thuộc miền và mô hình | A21 |

Hàm ý cho kho: dùng cụm như cờ cần xem lại theo mật độ trong đoạn, không như danh sách cấm. Ưu tiên quy tắc về độ cụ thể, cấu trúc, kiểm sự thật.

## 4. Trả lời 5 câu hỏi

1. Có bài có tên tác giả liệt kê cụm AI tiếng Việt? Có, nhưng yếu: BrandsVietnam (admin, 1 prompt, 1 chủ đề), Đỗ Tho (báo, thứ cấp), Finhay (blog), Hàng Nhựt Long (repo). Không có đếm tần suất. Cụm có nguồn xem 2.1; cụm không nguồn xem 2.2.
2. Nghiên cứu phát hiện tiếng Việt thấy gì? ViDetect: AI hơi ngắn hơn (301 vs 323 từ), ít câu hơn (12,18 vs 13,69); bảng đoạn mâu thuẫn với lời văn; AI tạo bằng cách viết lại nên có thể thiên lệch. VietBinoculars: >99% bằng perplexity trên tập ngoài miền, không nêu tell đọc được. Không có nghiên cứu nào nêu từ/cụm.
3. Số liệu "từ thừa" tiếng Anh: xem A32-A36. Kobak: 454 từ dư 2024; delves r=28,0. Liang: meticulous ×34,7. Lưu ý: bài VnReview/Bouchard nêu "delve +400%" và "3.900%" cho một cụm khác; tôi chưa kiểm hai số này và chúng không khớp với r=28,0 của Kobak (đo khác nhau). Không dùng.
4. Tell ở từ vựng hay cấu trúc? Cả hai. Chuyên gia (Russell): từ vựng nhiều nhất, cấu trúc câu và cấu trúc bài kế tiếp; khi bài đã qua humanize thì từ vựng ít lộ hơn. Bouchard/VnReview, Wikipedia: xóa từ chưa đủ. Con người: chuyên gia 92,7% TPR/3,3% FPR (n=5, 300 bài tiếng Anh); người ít dùng gần ngẫu nhiên; Cheng 19% (5 nhóm, 5 người, 30 bài y khoa); Penn State ~53% (điều kiện không nêu). Không có số liệu cho người đọc tiếng Việt.
5. Cộng đồng Việt: Voz/Reddit chỉ snippet ("văn AI" như lời chê, không nêu cụm); Reddit bị chặn khi mở. Tinhte, Spiderum, Zing, Tuổi Trẻ, Thanh Niên: không thấy bài nào nêu cụm cụ thể. Dân trí chỉ nêu "sáo rỗng". Cụm lặp ở nhiều nguồn độc lập: "không chỉ… mà còn" và em dash. Mọi thứ khác 1-2 nguồn.

## 5. Điểm mù

- Không có nghiên cứu đếm tần suất cụm AI trong tiếng Việt (đã thử scholar + Việt + Anh). Mọi "mức độ độc lập" trong 2.1 là số nguồn, không phải số liệu.
- Nhiều nguồn tiếng Việt thực chất là bản dịch/chép từ nguồn Anh (A08, A12-A14, A19, A21) hoặc cùng gốc BrandsVietnam. Số nguồn thật rất thấp.
- Reddit (r/vozforums, r/VietNam, r/TroChuyenLinhTinh) bị chặn khi mở trang; chỉ có snippet. Facebook cần đăng nhập, chỉ mở được 1 bài nhóm công khai. Scribd "13 dấu hiệu VisionEdu" chỉ thấy mô tả (không mở được nội dung). Voz.vn: tìm có nhưng không thấy chủ đề đúng nội dung; chưa đọc thread nào đầy đủ.
- The Atlantic bị paywall: số liệu Pangram "3 lần" chỉ thấy qua snippet và qua A10. Chưa thấy nghiên cứu gốc của Pangram. Pangram có lợi ích thương mại.
- Ngày đăng nhiều nguồn không lấy được (A08, A14, A19, A21, A23-A25, Reuters).
- Em dash: tell đang yếu đi vì mô hình mới đổi (A12); danh sách phải ghi mốc ngày.
- ViDetect: nhãn AI từ việc viết lại; bảng thống kê đoạn mâu thuẫn; chưa đọc kết quả VietAIDetector.
- Kobak, Liang, Russell, Cheng đều tiếng Anh, văn học thuật hoặc bài báo; thể loại báo cáo công sở, hợp đồng, chuỗi giao diện tiếng Việt chưa có nghiên cứu nào.
- Chưa kiểm sâu cách tính "53,1% / 35,9%" trong Russell (mã hóa bằng GPT-4o).
- Chưa kiểm số "22,5% abstract khoa học máy tính" (phys.org, chỉ snippet) và "delve +400%" / "3.900%" trong bài Bouchard/VnReview.
- WebFetch trả bản tóm tắt cho A12-A14, Wikipedia, nên "nguyên văn" ở đó là theo công cụ, chưa đối chiếu từng chữ.
- Khả năng hai nguồn Việt (A01 và A16) ảnh hưởng nhau không loại trừ được.

## 6. Query đã chạy

Serper (gl vn, hl vi, trừ khi ghi "EN"):
1. dấu hiệu văn bản do ChatGPT viết tiếng Việt cụm từ hay dùng
2. nhận biết văn ChatGPT "đóng vai trò quan trọng" "không chỉ" "mà còn" văn AI
3. phát hiện văn bản do AI sinh tiếng Việt bộ dữ liệu human vs machine-generated Vietnamese
4. (EN) Vietnamese AI-generated text detection dataset ChatGPT human written
5. (EN) Kobak excess vocabulary LLM PubMed delve
6. (EN) Liang monitoring AI-modified content peer reviews ICLR commendable meticulous
7. "văn AI" "giọng AI" nhận diện bài viết ChatGPT báo (type news): 0 kết quả
8. voz văn ChatGPT nhận ra ngay cụm từ
9. (EN) humans ability detect AI-generated text accuracy study
10. AI slop Vietnamese tiếng Việt văn sáo rỗng do AI viết spiderum
11. "văn ChatGPT" nhận ra "không chỉ" "mà còn" "trong bối cảnh" sáo rỗng: 0
12. tinhte nhận biết bài viết do AI viết "mùi AI"
13. reddit r/VietNam văn ChatGPT dấu hiệu bài viết AI "hành trình" "bức tranh"
14. vnexpress văn phong AI dấu hiệu nhận biết bài viết ChatGPT từ ngữ lặp
15. "văn mẫu" AI "hãy cùng khám phá" ChatGPT tiếng Việt sáo rỗng
16. dấu gạch ngang em dash ChatGPT tiếng Việt nhận biết văn AI
17. (EN, scholar) Vietnamese ChatGPT-generated text linguistic features stylometric analysis
18. phát hiện văn bản do ChatGPT sinh ra tiếng Việt đặc trưng ngôn ngữ nghiên cứu (scholar)
19. (EN) LLM overused phrases list study "tapestry" "in conclusion" structural patterns
20. danh sách từ cấm khi viết prompt tránh văn AI phản tác dụng
21. tuoitre.vn văn AI dấu hiệu nhận biết bài viết do ChatGPT viết "mùi AI" cụm từ
22. thanhnien.vn văn phong ChatGPT nhận ra bài viết AI sáo rỗng
23. dantri.com.vn viết văn bằng AI giáo viên nhận ra bài văn ChatGPT đặc điểm
24. zingnews văn AI "hoa mỹ" "sáo rỗng" học sinh bài văn ChatGPT giáo viên phát hiện: 0
25. spiderum cách nhận biết bài viết do AI viết dấu hiệu
26. vietcetera OR tinhte "giọng văn" AI "không chỉ" "mà còn" lặp cấu trúc dấu hiệu
27. bài văn ChatGPT đặc điểm "trong bối cảnh" "đóng vai trò" "tóm lại" giáo viên ngữ văn nhận diện: 0
28. (mix) Vietnamese ChatGPT writing sounds translated English calque "văn dịch": 0
29. Vietnamese Writing Skills giúp văn AI tự nhiên hơn danh sách cụm từ AI hay dùng tiếng Việt
30. github vietnamese humanizer anti AI slop tiếng Việt skill cụm từ cấm: 0
31. AI slop tiếng Việt danh sách cụm từ "bức tranh toàn cảnh" "hành trình" "đóng vai trò then chốt" văn ChatGPT: 0
32. voz.vn văn ChatGPT đọc là biết "văn AI" cụm từ
33. tinhte.vn thread viết bằng ChatGPT đọc "là biết" văn AI dấu hiệu gạch ngang "không chỉ"
34. "văn AI" nhận ra ngay "Không chỉ" "mà còn" "Trong thời đại" comment mạng xã hội
35. (EN) linguist Vietnamese ChatGPT style … translationese
36. ngôn ngữ học AI tiếng Việt văn phong ChatGPT "văn dịch" Hán Việt hóa nhận xét nhà ngôn ngữ
37. (EN) Reinhart Do LLMs write like humans PNAS
38. (EN) Liang Mapping the increasing use of LLMs Nature Human Behaviour 2025
39. (EN) Juzek Ward Why does ChatGPT delve so much RLHF
40. (EN) Vietnamese LLM generated text detection VLSP shared task OR benchmark 2025 ViDetect VietAIDetector
41. dấu hiệu văn AI "13 dấu hiệu" VisionEdu OR "đa dạng và phong phú" OR "đóng vai trò quan trọng"
42. reddit VietNam "viết như ChatGPT" OR "văn như ChatGPT" OR "văn AI" nhận ra
43. (EN) VietBinoculars Vietnamese zero-shot
44. (EN) Pangram negative parallelism "not just" …
45. (EN) Pangram "not just" negative parallelism three times as often Atlantic
46. (EN) Towards AI Bouchard remove AI smell writing guide …
47. (EN) Yakura Empirical evidence of LLM's influence on human spoken communication

Brave (search-lang vi):
48. văn ChatGPT đặc trưng cụm từ "không chỉ" "mà còn" nhận biết AI viết
49. "giọng văn AI" tiếng Việt dấu hiệu sáo rỗng bài đăng Facebook ChatGPT viết: 1 kết quả (A18-liên quan)
50. văn phong AI tiếng Việt "đóng vai trò quan trọng" "trong bối cảnh" sáo rỗng dấu hiệu bài viết ChatGPT: 1 kết quả không liên quan
51. cách nhận biết bài viết ChatGPT: dấu gạch ngang, gạch đầu dòng, emoji, "Tóm lại" Tinh tế OR Genk OR Zing: 0

Jina-search (no-content):
52. dấu hiệu nhận biết văn bản do ChatGPT viết tiếng Việt cụm từ mở bài kết bài sáo rỗng

Mở trang bằng jina-read: các URL "GỐC" ở mục 1. WebFetch: A12, A13, A14, Wikipedia (A43).

SearXNG: không dùng (không cần dừng).
