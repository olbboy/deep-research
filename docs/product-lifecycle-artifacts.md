# Vòng đời tài liệu sản phẩm: pha nào cần gì

Lát cắt theo **pha** của [tài liệu kiến thức Product Management](product-management-knowledge.md), vốn được tổ chức theo **khung lý thuyết**. Không thêm khung mới; mọi dòng dẫn về một nguồn đã kiểm trong tài liệu đó. Chỗ nào là suy luận thì ghi rõ.

Ngày biên soạn 2026-09-11.

## Từ vựng định nghĩa một lần

| Từ | Nghĩa dùng trong tài liệu |
|---|---|
| **Outcome** | Thay đổi đo được ở hành vi người dùng hoặc kết quả kinh doanh |
| **Output** | Thứ đội làm ra: tính năng, màn hình, dòng code |
| **Discovery** | Giai đoạn tìm xem nên xây gì và giải pháp nào đúng |
| **Delivery** | Giai đoạn xây, kiểm thử, phát hành |
| **Baseline** | Mốc hiện tại của một chỉ số, **đã đo**, có nguồn đo và ngày đo |
| **Guardrail** | Chỉ số bảo vệ, không được xấu đi dù chỉ số chính có tăng |
| **Non-goal** | Thứ cố ý không làm, ghi kèm lý do và ngày xét lại |
| **Tracking plan** | Bảng sự kiện cần đo: tên sự kiện, lúc bắn, tham số |

## 1. Thứ bậc bốn tầng

Nguyên văn ProductPlan: **tầm nhìn sản phẩm → mục tiêu sản phẩm → roadmap → kế hoạch phát hành và backlog**.

| Tầng | Trả lời câu gì | Công cụ điền vào nó |
|---|---|---|
| 1. Tầm nhìn sản phẩm | Ta đi về đâu | Kim tự tháp PMF của **Olsen** trả lời ba tầng dưới: phục vụ ai, nhu cầu nào đang bị phục vụ kém, giá trị ta hứa là gì. Nguyên tắc sản phẩm của **Cagan** là la bàn cho đánh đổi |
| 2. Mục tiêu sản phẩm | Đổi được hành vi hay chỉ số nào | **Product Kata** của Perri biến mục tiêu mơ hồ thành chuỗi target condition đo được |
| 3. Roadmap | Đang giải bài toán nào, sắp giải bài nào | **Now-Next-Later** của Bastow và Cast, xếp theo mức tự tin |
| 4. Kế hoạch phát hành và backlog | Ship cái gì, khi nào, ai làm | Release plan, backlog, story map |

Lưu ý gán nhãn: ProductPlan chỉ nêu **tên** bốn tầng, không định nghĩa tầng 1 gồm những gì. Việc dùng kim tự tháp PMF và nguyên tắc sản phẩm để điền vào tầng 1 là **ghép của người biên soạn**, hợp lệ vì cả hai đều nằm trong tài liệu kiến thức, nhưng đừng trích như thể ProductPlan nói vậy.

## 2. Bảng vòng đời

Discovery và delivery chạy **song song**, không nối đuôi (Cagan, dual-track).

### Pha hướng và chẩn đoán

| Tài liệu | Nội dung bắt buộc | Nguồn |
|---|---|---|
| Kata một trang | **Bảy bước**: Direction → Current condition đo bằng số → Target condition → Obstacle → Experiment → **Expected outcome** → Learning | Perri |
| Bảng bốn rủi ro | Bốn dòng value, usability, feasibility, business viability; mỗi dòng ghi đã có bằng chứng gì, còn thiếu gì | Cagan, SVPG |

Bước **Expected outcome** hay bị bỏ, và đó chính là bước làm cho vòng lặp có nghĩa: nó buộc ghi ra ta *tin* kết quả sẽ ra sao **trước khi** đo. Ví dụ của Perri: đội đoán người bán gọi lên văn phòng khoảng 4 lần một tuần, đếm thật ra 7 lần, gấp đôi giả định. Bỏ bước này thì vẫn đo được, nhưng không biết mình đã sai bao xa, nên không học được gì.

Perri nhấn thêm: những vòng lặp đầu thường chỉ để **đo current condition**, và đây là bước hầu hết bỏ qua khi lao thẳng vào làm.

### Pha discovery

| Tài liệu | Nội dung bắt buộc | Nguồn |
|---|---|---|
| Opportunity Solution Tree | Bốn tầng outcome → opportunity → solution → assumption test. Bốn quy tắc: cơ hội đến từ **phỏng vấn thật**; phép thử "có nhiều hơn một cách giải không"; so sánh **ít nhất ba giải pháp**; mỗi giải pháp gắn **đúng một** cơ hội | Torres |
| Ghi chú phỏng vấn | Ai, ngày, trích dẫn nguyên văn | Torres |
| Nguyên mẫu **và kết quả thử** | Thử về khả thi, dùng được, có muốn mua. Ghi ai thử, ngày nào, đổi gì sau khi thử | Cagan 2005 bước 5 |
| PR-FAQ, tuỳ chọn | Thông cáo báo chí viết ngược | Amazon, McAllister |

Nhịp cập nhật cây cơ hội: **sau mỗi 3 tới 4 cuộc phỏng vấn**, không đợi hết một đợt nghiên cứu.

### Pha roadmap

| Tài liệu | Nội dung bắt buộc | Nguồn |
|---|---|---|
| Now-Next-Later | Mỗi dòng là một **vấn đề**, không phải tên tính năng. Xếp theo mức tự tin, không theo ngày. Chi tiết giảm dần theo khoảng cách | ProdPad |
| Bản theo nhóm người đọc | Lãnh đạo xem theme không ngày; kỹ thuật xem chi tiết; kinh doanh, hỗ trợ, khách hàng **không được thấy ngày** | ProductPlan, Tempo Way |

Bốn cách dùng sai: biến ba cột thành Q1/Q2/Q3; nhồi tính năng thay vì vấn đề; nhồi quá tải cột Now; thêm deadline giả.

### Pha delivery

| Tài liệu | Nội dung bắt buộc | Nguồn |
|---|---|---|
| **PRD 11 mục, đánh số 0 tới 10** | 0 thông tin chung và trạng thái · 1 vấn đề có nguồn · 2 mục tiêu và non-goal kèm lý do · 3 nguyên tắc sản phẩm · 4 chỉ số có baseline và guardrail · 5 giả định · 6 yêu cầu có tiêu chí nghiệm thu và hạng · 7 luồng chính và ma trận trạng thái biên · 8 tiêu chí phát hành **và tracking plan** · 9 ra mắt và rút lui · 10 câu hỏi mở có chủ và hạn | Tổng hợp Cagan, Square, Atlassian, Product School, Figma, Aha! |
| Nguyên mẫu có chú giải | Cagan 2006: nguyên mẫu độ trung thực cao **là bản spec chính**, văn bản chỉ chú giải cho thứ nguyên mẫu không thể hiện được | Cagan 2006 |
| Thiết kế kỹ thuật | Tài liệu riêng, không nhét vào PRD | Suy luận từ cách các template tách Key Features khỏi Key Logic |
| Release plan và backlog | Ngày ship, phân bổ người, task chi tiết | ProductPlan |

**Tracking plan thuộc mục 8 của PRD**, tức viết **trước khi ship**, không phải việc làm sau ship. Lý do: không có tracking plan từ trước thì chỉ số ở mục 4 không đo được lúc ra mắt, và phải chờ một đợt phát hành nữa mới biết tính năng có tác dụng không.

One-pager cho tính năng nhỏ, một đội, dưới hai tuần: chỉ mục 0, 1, 2, 4, 6, 10.

### Pha sau ship

| Tài liệu | Nội dung bắt buộc | Nguồn |
|---|---|---|
| Đối chiếu outcome với target condition | Chỉ số chính đạt chưa, guardrail có xấu đi không | Perri, Pendo |
| Learning của vòng Kata | Thực tế khác giả định bao nhiêu, vòng kế tiếp làm gì | Perri |
| Đo feature adoption | Breadth, time to adopt, duration. Chọn tính năng đáng theo dõi: nhóm tạo 80% tổng click | Pendo |

## 3. Bộ tối thiểu "đủ sống"

*(Suy luận của người biên soạn, không nguồn nào quy định bộ này.)*

Tầm nhìn · Kata kèm bảng bốn rủi ro · Now-Next-Later viết bằng vấn đề · Nguyên mẫu và ghi chú phỏng vấn · PRD sống · Release plan và tracking plan · Backlog.

## 4. Bốn chỗ dễ ghi sai

| Chỗ | Ghi sai thường gặp | Đúng |
|---|---|---|
| Kata | Liệt kê sáu bước, bỏ Expected outcome | Bảy bước; Expected outcome nằm giữa Experiment và Learning |
| Đếm mục PRD | Gọi "10 mục" vì đánh số 0 tới 10 | **11 mục**, đánh số 0 tới 10. Giữ nguyên số hiệu vì phạm vi one-pager và mã kiểm của skill phụ thuộc vào nó |
| Tracking plan | Xếp vào pha sau ship | Mục 8 của PRD, viết trước khi ship |
| Tầng 1 thứ bậc | Trích như thể ProductPlan định nghĩa tầm nhìn gồm persona và value proposition | ProductPlan chỉ nêu tên tầng; nội dung lấy từ Olsen và Cagan, phải ghi rõ là ghép |

## 5. Kiểm tự động

Skill `prd-validate` chạy 65 phép kiểm có mã trên PRD và roadmap, xuất phán quyết ĐẠT / ĐẠT CÓ ĐIỀU KIỆN / CHƯA ĐẠT. Kết quả kiểm thử ở [báo cáo lặp bảy vòng](../plans/reports/skill-test-260908-1426-prd-validate-iterations.md).

## Nguồn

Mọi dòng trong tài liệu này dẫn về [tài liệu kiến thức](product-management-knowledge.md) mục 1 tới 5, và qua đó về năm báo cáo nghiên cứu kèm trích dẫn nguyên văn trong `plans/reports/`.

## Câu hỏi chưa giải quyết

1. Không nguồn nào nêu tiêu chí khi nào **không** cần viết PRD.
2. Bộ tối thiểu "đủ sống" là suy luận, chưa có nguồn hay dữ liệu kiểm chứng.
3. ProductPlan không định nghĩa nội dung tầng 1; cách ghép Olsen và Cagan vào đó chưa được nguồn nào xác nhận.
