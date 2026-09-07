# Đối chiếu khung "PRD world-class" với nguồn đã kiểm, và khung PRD tổng hợp cuối

Ngày: 2026-09-08. Đầu vào: khung "PRD world-class" gồm 5 đặc điểm và 7 phần cấu trúc do Leo đưa vào, chưa rõ tác giả gốc. Chuẩn đối chiếu: 5 template PRD đã kiểm ở [báo cáo PRD](researcher-260908-0238-prd-knowledge.md) cộng 2 nguồn chính chủ của Marty Cagan mở thêm trong vòng này.

## Từ vựng định nghĩa một lần

| Từ | Nghĩa |
|---|---|
| **Non-goal** | Thứ cố ý không làm trong phạm vi này, ghi ra để không ai hiểu nhầm là sẽ làm. |
| **Guardrail metric** | Chỉ số bảo vệ: thứ không được xấu đi dù chỉ số chính có tăng, ví dụ độ trễ, tỷ lệ lỗi. |
| **Release criteria / NFR** | Yêu cầu phi chức năng để được phép phát hành: hiệu năng, khả năng mở rộng, độ tin cậy, hỗ trợ được, bản địa hóa được. |
| **P95 latency** | Độ trễ mà 95% yêu cầu nằm dưới mức đó. Đo đuôi chậm thay vì trung bình. |
| **Canary** | Phát hành cho một phần nhỏ người dùng trước, ví dụ 5%, để bắt lỗi sớm. |
| **Kill switch** | Công tắc tắt tính năng tức thì mà không cần triển khai lại mã. |
| **Given-When-Then** | Cách viết tiêu chí nghiệm thu: cho trước bối cảnh, khi hành động xảy ra, thì kết quả mong đợi. |
| **Acceptance criteria** | Tiêu chí để nói một yêu cầu đã xong. |
| **Tracking plan** | Bảng liệt kê sự kiện cần đo: tên sự kiện, lúc nào bắn, mang tham số gì. |
| **Requirements traceability** | Ghi rõ mỗi yêu cầu phục vụ mục tiêu nào, để khi cắt yêu cầu biết mất gì. |
| **High-fidelity prototype** | Nguyên mẫu đủ giống thật để đưa cho người dùng thử. |

## Kết luận một đoạn

Khung được đưa vào là khung **tốt và thiên về kỹ thuật**. Về nguyên tắc nó không sai chỗ nào và có tổ tiên rõ ràng: mục "ràng buộc kỹ thuật" của nó chính là "Release Criteria" mà Cagan đã đặt vào PRD từ năm 2005. Nhưng có bốn điểm cần sửa trước khi coi nó là chuẩn. Một, ba con số 40%, 90% và nhãn "world-class" không có nguồn. Hai, nó thiếu bốn mục mà các nguồn đã kiểm coi là cốt lõi: câu hỏi mở, giả định, luồng chính kèm mockup, và xếp hạng ưu tiên từng yêu cầu. Ba, ba khái niệm kỹ thuật của nó là mượn từ ba truyền thống khác, hợp lệ nhưng không phải chuẩn PRD, cần ghi nguồn đúng. Bốn, nó chỉ mô tả **tài liệu**, không mô tả **việc phải làm trước khi viết tài liệu**, trong khi Cagan coi bước nguyên mẫu và kiểm thử trước khi viết là quan trọng nhất, và đến năm 2006 đã kết luận nguyên mẫu độ trung thực cao mới là bản spec chính, văn bản chỉ là chú giải.

## 1. Nguồn dùng để đối chiếu

| Nguồn | Năm | Loại | Đã kiểm |
|---|---|---|---|
| Cagan, [How To Write a Good PRD](https://www.svpg.com/wp-content/uploads/2024/07/How-To-Write-a-Good-PRD.pdf), SVPG | 2005 | PDF 26 trang, miễn phí, dựa một phần trên ghi chú của Ben Horowitz | ✅ tải về, trích văn bản, đọc toàn văn |
| Cagan, [Revisiting the Product Spec](https://www.svpg.com/revisiting-the-product-spec/), SVPG | 2006 | bài web | ✅ |
| Atlassian, Product School, Square (Kevin Yien), Figma, Aha! | 2020 trở đi | template | ✅ vòng trước |
| Kohavi, Tang, Xu, *Trustworthy Online Controlled Experiments*, Cambridge | 2020 | sách | ✅ tra cứu nguồn gốc guardrail metric |
| Dan North, [Introducing BDD](https://dannorth.net/introducing-bdd/) | 2006 | bài | ✅ tra cứu nguồn gốc Given-When-Then |

## 2. Đối chiếu 5 đặc điểm cốt lõi

| Đặc điểm trong khung | Nguồn đã kiểm nói gì | Kết luận |
|---|---|---|
| **Problem-first, không solution-first.** Dành ít nhất 40% cho Why và What | Cagan 2005: PRD phải nêu "vấn đề muốn giải, không phải giải pháp", yêu cầu "nêu nhu cầu thay vì giải pháp, để lại tối đa linh hoạt cho kỹ thuật". Square: mô tả vấn đề trong 1 tới 2 câu kèm bằng chứng | **Trùng** về nguyên tắc. Con số **40% không có nguồn**, là số bịa cho dễ nhớ |
| **Tôn sùng non-goals.** Bảo vệ phạm vi là thước đo năng lực PM | Square: non-goals "quan trọng và làm rõ ngang goals", và phải **giải thích vì sao** không làm. Atlassian, Aha!, Product School đều có mục tương đương | **Trùng**, nhưng khung được đưa vào **yếu hơn nguồn** ở một điểm: chỉ nói "từ chối thẳng thừng", không yêu cầu ghi lý do. Câu "thước đo năng lực PM" là ý kiến, không có nguồn |
| **Metrics có guardrail** | 5 template PRD: đều có success metrics, **không template nào có guardrail**. Cagan 2005: mục tiêu phải được xếp ưu tiên và nêu cách đo. Guardrail metric là khái niệm của Kohavi, Tang, Xu 2020 trong sách về thực nghiệm A/B: chỉ số không được thay đổi giữa nhóm đối chứng và nhóm thử, như độ trễ, tỷ lệ crash | **Không có trong chuẩn PRD, nhưng hợp lệ.** Mượn từ truyền thống thực nghiệm. Đáng đưa vào khung tổng hợp, ghi đúng nguồn |
| **Edge case và failure state** | Square: luồng chính phải gồm cả "edgy use cases". Cagan 2005: mô tả từng tính năng "ở mức thiết kế tương tác và use case". Ma trận trạng thái zero, loading, error, limit không có trong nguồn PRD nào, là thực hành của thiết kế giao diện | **Trùng một phần.** Nguyên tắc có, ma trận trạng thái là bổ sung từ thiết kế. Con số "giảm 90% bug" **không có nguồn**, và không kiểm chứng được |
| **Living document, có trạng thái** | Product School: PRD là tài liệu sống. Cagan 2005: "PRD là tài liệu sống, theo dõi mọi tính năng tới lúc ra mắt", và "nếu chưa có trong PRD thì đưa vào PRD". Atlassian có mục trạng thái | **Trùng hoàn toàn.** Trạng thái Deprecated là bổ sung hợp lý, không nguồn nào nêu |

## 3. Đối chiếu 7 phần cấu trúc

| Phần trong khung | Có trong nguồn nào | Nhận xét |
|---|---|---|
| 1. Overview và context: problem statement có số, persona, gắn OKR | Atlassian (Objective gắn mục tiêu tổ chức), Product School (Personas), Aha! (Context), Cagan 2005 (Product Purpose: vấn đề, sản phẩm cho ai, kịch bản) | Trùng. Cagan 2005 thêm "phép thử thang máy": nói được giá trị sản phẩm trước khi thang máy tới tầng |
| 2. Goals và non-goals | Square, Atlassian, Product School, Aha! | Trùng. Thiếu "kèm lý do" của Square |
| 3. Success metrics: primary và guardrail | Metrics có ở cả 5 nguồn. Guardrail không có | Xem mục 2 |
| 4. User stories và acceptance criteria Given-When-Then | User story: Atlassian, Product School. Given-When-Then: **không có trong nguồn PRD nào**, là của Dan North, bài Introducing BDD năm 2006, gốc từ Chris Matts và North năm 2004 | Mượn từ truyền thống kiểm thử hành vi. Hợp lệ, phục vụ đúng bước 9 của Cagan: "QA có đủ thông tin để viết test plan không" |
| 5. Scenarios và edge cases | Square (edgy use cases), Cagan 2005 (use case từng tính năng) | Trùng nguyên tắc, chi tiết là bổ sung |
| 6. Tech và data constraints: SLA, P95, bảo mật, tracking plan | **Cagan 2005, mục Release Criteria**: performance, scalability, reliability, usability, supportability, localizability. Cagan 2006: chú giải nguyên mẫu bằng "release requirements: reliability, performance, scalability". Figma launch checklist có Security và Growth & Data | **Trùng, và có tổ tiên xa hơn khung tự nhận.** Tracking plan là bổ sung từ thực hành phân tích sản phẩm, không nguồn PRD nào nêu |
| 7. Rollout và rollback | Square: Launch Plan theo giai đoạn pilot, beta, early access, launch, mỗi giai đoạn có **tiêu chí chuyển giai đoạn**. Figma: milestones dogfood, beta, launch. Cagan 2005 mục Schedule: nêu bối cảnh và cửa sổ mục tiêu, không phải ngày ngẫu nhiên | Trùng phần rollout. **Rollback và kill switch không có trong nguồn PRD nào**, là thực hành phát hành phần mềm. Nguồn gốc cụ thể chưa kiểm |

## 4. Bốn mục khung này thiếu so với nguồn

| Mục thiếu | Ai có | Vì sao quan trọng |
|---|---|---|
| **Câu hỏi mở** | 5 trên 5 template. Cagan 2005 bước 10: mọi câu hỏi phát sinh phải được giải quyết và ghi vào PRD | Thiếu mục này thì quyết định phát sinh trong lúc xây rơi vào email và chat, không ai tìm lại được |
| **Giả định** | Atlassian, Aha!, Cagan 2005 bước 6 "Nhận diện và chất vấn giả định của bạn", với ví dụ "đừng đặc tả cây nến trong PRD rồi tự chặn mình khỏi bóng đèn" | Giả định không ghi ra là giả định không ai kiểm |
| **Luồng chính kèm mockup hoặc nguyên mẫu** | 4 trên 5 template. Cagan 2006: nguyên mẫu là bản spec chính | Khung đưa vào có ma trận trạng thái nhưng không có chỗ cho luồng chính và bản vẽ |
| **Xếp hạng ưu tiên từng yêu cầu** | Atlassian có cột ưu tiên. Cagan 2005 bước 8: phân loại must-have, high-want, nice-to-have, **rồi xếp hạng 1 tới n trong từng loại**. Must-have nghĩa là thiếu một cái thì không được ship | Không xếp hạng thì khi lịch trượt, đội sẽ làm cái dễ trước và cắt cái quan trọng |

Hai mục nữa chỉ Cagan 2005 có, đáng cân nhắc:

- **Nguyên tắc sản phẩm** (bước 4): vài câu la bàn cho mọi đánh đổi. Ví dụ TiVo: "mọi thứ phải mượt và nhẹ nhàng", "không có chế độ, không có cây phân cấp sâu". eBay: dễ dùng, an toàn, vui.
- **Truy vết yêu cầu tới mục tiêu**: mỗi yêu cầu ghi nó phục vụ mục tiêu nào. Cắt yêu cầu là thấy ngay mất mục tiêu nào.

## 5. Ba con số không có nguồn

| Con số | Tình trạng |
|---|---|
| "Ít nhất 40% trọng tâm cho Why và What" | Không nguồn. Là số ước lệ |
| "Giảm thiểu 90% bug phát sinh" | Không nguồn, không kiểm chứng được. Nên bỏ |
| Nhãn "world-class" | Không nguồn. Khung này là một tổng hợp có chất lượng, không phải chuẩn được công nhận |

## 6. Mâu thuẫn lớn nhất: chính Cagan đã đổi ý về PRD

Năm 2005 Cagan viết tài liệu 10 bước để làm PRD tốt. Năm 2006 ông viết lại: spec phải giải bảy việc, gồm mô tả trọn trải nghiệm người dùng, thể hiện đúng hành vi phần mềm, phục vụ nhiều đối tượng đọc, chịu được thay đổi, có một bản duy nhất, kiểm thử được, và không mơ hồ. Ông kết luận văn bản thất bại ở hầu hết bảy việc đó vì "mất quá lâu để viết, hiếm khi được đọc, không đủ chi tiết", và "chữ với hình đẹp quá hạn chế để mô tả hành vi phần mềm". Nguy hiểm hơn, sự tồn tại của một PRD dày tạo cảm giác tự tin giả mà không chứng minh được sản phẩm dùng được hay đáng mua.

Đề xuất của ông: **nguyên mẫu độ trung thực cao là bản spec chính**, vì nó kiểm thử được với người dùng thật trước khi kỹ thuật bắt đầu. Văn bản chỉ còn là chú giải trên wiki cho những gì nguyên mẫu không thể hiện được: yêu cầu phát hành về độ tin cậy, hiệu năng, khả năng mở rộng, và mô tả use case quan trọng.

Hệ quả cho khung được đưa vào: nó mô tả một **văn bản**, nên đúng nhất là coi nó là phần chú giải đi kèm nguyên mẫu, không phải bản spec đứng một mình. Điều này cũng nhất quán với bước 5 của chính tài liệu 2005: "nguyên mẫu và kiểm thử ý tưởng sản phẩm" phải xảy ra **trước** bước 7 "viết ra".

Cả hai tài liệu của Cagan không mâu thuẫn với nhau nếu đọc theo trình tự: làm bài tập về nhà, dựng nguyên mẫu, thử với người dùng, rồi mới viết. Cái sai là viết trước, thử sau.

## 7. Tình huống cụ thể

Chị Lan là PM ở một công ty phần mềm quản lý cửa hàng. Sáng thứ hai 14/09/2026, chị nhận yêu cầu từ trưởng phòng kinh doanh: "khách doanh nghiệp than phải mời từng nhân viên vào hệ thống, mất cả buổi, làm tính năng nhập từ tệp CSV đi".

**Nếu chị viết theo khung được đưa vào**, tài liệu sẽ có problem statement, persona, non-goals, chỉ số chính kèm guardrail, user story với Given-When-Then, ma trận trạng thái, ràng buộc P95 và kế hoạch canary. Đọc rất chắc tay. Nhưng ba tuần sau, khi kỹ sư hỏi "tệp có 51 dòng thì sao, tệp có email trùng thì sao", câu trả lời nằm trong chat vì tài liệu không có bảng câu hỏi mở. Khi lịch trượt, đội cắt phần "gửi email mời" vì không ai xếp hạng nó là must-have. Và không ai từng cho một khách hàng thử màn hình nhập tệp trước khi viết, vì khung không có bước đó.

**Nếu chị viết theo khung tối thiểu từ nguồn**, tài liệu có vấn đề, chỉ số, yêu cầu, non-goals, câu hỏi mở. Đủ để đồng thuận, nhưng kỹ sư sẽ tự đoán độ trễ chấp nhận được và tự quyết cách phát hành.

**Nếu chị làm theo khung tổng hợp ở mục 8**, trình tự là: nói chuyện với ba khách doanh nghiệp đã than phiền; dựng nguyên mẫu màn hình nhập tệp trong Figma và cho hai người trong số họ thử; phát hiện họ không có tệp CSV mà có danh sách trong Google Sheets, nên non-goal "không hỗ trợ Sheets" phải ghi kèm lý do và ngày xét lại. Rồi mới viết văn bản, ngắn, với bảng câu hỏi mở có người phụ trách và hạn.

## 8. Khung PRD tổng hợp cuối

### 8.1 Việc phải làm trước khi viết, theo Cagan 2005

1. Làm bài tập về nhà: khách hàng, đối thủ, năng lực đội, công nghệ sẵn có.
2. Xác định mục đích: giá trị sản phẩm nói được trong một chuyến thang máy.
3. Hồ sơ người dùng, mục tiêu, tác vụ. Chọn vài persona chính, không chiều tất cả.
4. Nguyên tắc sản phẩm: vài câu la bàn cho đánh đổi.
5. Nguyên mẫu và thử: ba loại kiểm thử là khả thi, dùng được, và có muốn mua không.
6. Nhận diện và chất vấn giả định.

Chỉ sau đó mới đến bước 7, viết ra.

### 8.2 Cấu trúc văn bản, 10 mục, ghi nguồn từng mục

| # | Mục | Nội dung | Lấy từ |
|---|---|---|---|
| 0 | Thông tin chung | Trạng thái Draft, In review, Approved, Deprecated. Vai trò. Changelog | Atlassian, Square, khung đưa vào |
| 1 | Vấn đề và bối cảnh | Vấn đề trong 1 tới 2 câu có số. Persona chính. Gắn mục tiêu quý hoặc OKR nào | Square, Product School, Atlassian, Cagan 2005 |
| 2 | Mục tiêu và non-goals | Mục tiêu xếp ưu tiên. Non-goal **kèm lý do và ngày xét lại** | Square, Cagan 2005 |
| 3 | Nguyên tắc sản phẩm | 3 tới 7 câu la bàn | Cagan 2005 |
| 4 | Chỉ số | Chỉ số chính có mốc hiện tại, mốc đích, hạn đo. Chỉ số bảo vệ không được xấu đi | Atlassian, Square, Kohavi 2020 cho guardrail |
| 5 | Giả định | Về người dùng, kỹ thuật, kinh doanh. Cái nào đã kiểm, cái nào chưa | Atlassian, Aha!, Cagan 2005 |
| 6 | Yêu cầu | Mỗi dòng: user story, tiêu chí nghiệm thu Given-When-Then, loại must-have hoặc high-want hoặc nice-to-have, **hạng 1 tới n trong loại**, phục vụ mục tiêu số mấy | Atlassian, Cagan 2005, Dan North 2006 |
| 7 | Luồng chính và trạng thái biên | Link nguyên mẫu đã thử với người dùng. Luồng chính và 1 tới 2 luồng biên. Ma trận trạng thái: rỗng, đang tải, lỗi, vượt giới hạn, thiếu quyền, mất mạng | Square, Figma, Cagan 2006, khung đưa vào |
| 8 | Tiêu chí phát hành | Hiệu năng, khả năng mở rộng, độ tin cậy, dùng được, hỗ trợ được, bản địa hóa được. Bảo mật dữ liệu. Tracking plan: sự kiện, lúc bắn, tham số | Cagan 2005, khung đưa vào |
| 9 | Kế hoạch ra mắt và rút lui | Giai đoạn nội bộ, beta hoặc canary, toàn bộ. Mỗi giai đoạn có tiêu chí chuyển tiếp. Điều kiện rút lui cụ thể. Cửa sổ thời gian kèm lý do, không phải ngày ngẫu nhiên | Square, Figma, Cagan 2005, khung đưa vào |
| 10 | Câu hỏi mở | Câu hỏi, người phụ trách, hạn, trạng thái | 5 template, Cagan 2005 |

### 8.3 Phép thử hoàn chỉnh, theo Cagan 2005 bước 9

Trước khi duyệt, hỏi hai câu: kỹ sư đọc xong có đủ hiểu đích để đưa sản phẩm tới đó không, và QA có đủ thông tin để viết test plan không. Given-When-Then ở mục 6 là để trả lời câu thứ hai.

### 8.4 Quy mô nào dùng bao nhiêu

(Đề xuất của người viết, không nguồn nào quy định.) Tính năng nhỏ, một đội, dưới hai tuần: dùng mục 0, 1, 2, 4, 6, 10, tức one-pager. Tính năng liên đội hoặc có rủi ro hạ tầng: dùng đủ 10 mục. Sản phẩm mới: nguyên mẫu đã thử là bản chính, văn bản 10 mục là chú giải.

## 9. Chỗ trống cần điền

Chọn một phương án cho mỗi câu.

1. **Vai trò của văn bản PRD trong đội bạn.** (a) PRD là bản spec chính, nguyên mẫu đi kèm. (b) Nguyên mẫu đã thử là bản chính, PRD là chú giải ngắn theo Cagan 2006. (c) Tùy quy mô như mục 8.4.
2. **Guardrail metric.** (a) Bắt buộc cho mọi PRD. (b) Chỉ khi có A/B test. (c) Bỏ, chỉ giữ chỉ số chính.
3. **Ai viết Given-When-Then.** (a) PM viết cùng user story. (b) PM viết user story, QA hoặc kỹ sư viết tiêu chí nghiệm thu rồi PM duyệt. (c) Chỉ viết cho luồng chính.
4. **Kế hoạch rút lui.** (a) Nằm trong PRD. (b) Tách sang tài liệu phát hành riêng của kỹ thuật, PRD chỉ link tới.
5. **Nguyên tắc sản phẩm.** (a) Viết một lần ở cấp sản phẩm, PRD chỉ tham chiếu. (b) Viết lại trong từng PRD. (c) Bỏ.

## Câu hỏi chưa giải quyết

1. Không biết khung "PRD world-class" lấy từ đâu, nên không kiểm được ý định gốc của tác giả và không biết ba con số có được giải thích ở nguồn gốc hay không.
2. Nguồn gốc cụ thể của canary và kill switch trong phát hành phần mềm chưa kiểm, mới chỉ xác nhận chúng không có trong nguồn PRD nào.
3. Chưa kiểm SVPG hiện nay còn khuyến nghị dạng PRD nào không, hay đã bỏ hẳn sang nguyên mẫu. Tài liệu 2005 vẫn được đăng lại trên svpg.com với đường dẫn năm 2024, nên có thể vẫn được coi là tham khảo.
4. Phần FAQ của mô hình PR-FAQ Amazon vẫn chưa đọc được, chưa so sánh được với khung này.
