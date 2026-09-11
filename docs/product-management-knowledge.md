# Kiến thức Product Management chắt lọc

Tài liệu này chắt lọc nội dung thực chất từ các nguồn đã kiểm chứng trong [báo cáo danh mục](../plans/reports/deep-research-260908-0214-product-management-ebooks-catalog.md). Mọi khung và định nghĩa đều dẫn về nguồn gốc. Chỗ nào là suy luận của người viết sẽ ghi rõ.

Ngày biên soạn: 2026-09-08.

## Từ vựng định nghĩa một lần

| Từ | Nghĩa dùng trong tài liệu |
|---|---|
| **Output** | Thứ team làm ra: tính năng, màn hình, dòng code. Đếm được ngay. |
| **Outcome** | Thay đổi hành vi người dùng hoặc kết quả kinh doanh do output tạo ra. Ví dụ: tỷ lệ hoàn tất đăng ký tăng từ 40% lên 60%. |
| **Discovery** | Giai đoạn tìm hiểu nên làm gì và giải pháp nào đúng, trước khi viết code sản xuất. |
| **Delivery** | Giai đoạn xây, kiểm thử, phát hành giải pháp đã chọn. |
| **PRD** | Product Requirements Document, tài liệu mô tả sản phẩm hoặc tính năng cần xây: vấn đề, mục tiêu, phạm vi, yêu cầu. |
| **Roadmap** | Bản trình bày hướng đi của sản phẩm theo thời gian, cho người khác biết ta đang giải bài toán nào và sắp giải bài toán nào. |
| **Backlog** | Danh sách hạng mục chờ làm, chi tiết ở mức thực thi. Không phải roadmap. |
| **Stakeholder** | Người có quyền lợi hoặc tiếng nói với sản phẩm: ban lãnh đạo, kinh doanh, chăm sóc khách hàng, pháp chế. |
| **Product trio** | Bộ ba product manager, designer, tech lead cùng làm discovery. |
| **PMF** | Product-Market Fit, mức độ sản phẩm khớp với nhu cầu thị trường. |
| **MVP** | Minimum Viable Product, phiên bản nhỏ nhất đủ để kiểm chứng một giả định. |

## 1. Sáu khung nền tảng, từ nguồn gốc

### 1.1 Build trap: bẫy chỉ lo sản xuất

Melissa Perri định nghĩa build trap là tình trạng team "định nghĩa và phát hành phần mềm mà không có thước đo thành công, quá bận quản lý backlog, và chỉ chăm chăm đẩy tính năng ra cửa". Gốc của vấn đề là tổ chức coi trọng output hơn outcome, tức là xây bất cứ thứ gì thay vì xây đúng thứ cần.

Perri chỉ ra ba yếu tố bên trong quyết định việc thoát bẫy: quy trình, chiến lược, văn hóa.

Nguồn: [Mind the Product – Escaping the Build Trap](https://www.mindtheproduct.com/escaping-build-trap-melissa-perri/); sách gốc *Escaping the Build Trap* (O'Reilly, 2018), bản Việt *Quản Lý Sản Phẩm Trong Thời Đại 4.0* (NXB Đại học Kinh tế Quốc dân, 2019).

**Dấu hiệu nhận biết bạn đang trong bẫy** (suy luận từ định nghĩa trên, không phải danh sách nguyên văn của Perri): roadmap là danh sách tính năng kèm ngày; họp ưu tiên xoay quanh "ai xin trước"; không ai trả lời được tính năng phát hành quý trước đã thay đổi chỉ số nào.

### 1.2 Product Kata: vòng lặp đi từ mục tiêu tới thực nghiệm

Perri mượn khái niệm kata của Toyota để biến chiến lược thành hành động. Vòng lặp gồm bảy bước, lặp lại tới khi đạt target condition.

| Bước | Câu hỏi | Ví dụ của Perri |
|---|---|---|
| 1. Direction / Challenge | Lãnh đạo muốn đi đâu? | "Làm cho người bán tự vận hành cửa hàng hoàn toàn" |
| 2. Current condition | Hiện tại đang ở đâu, đo bằng số? | Người bán gọi lên văn phòng 7 lần một tuần |
| 3. Target condition | Bước kế tiếp cụ thể, đo được là gì? | Người bán gọi ít hơn 2 lần một tuần |
| 4. Obstacle | Cái gì đang cản? | "Chưa biết hiện họ gọi bao nhiêu lần" |
| 5. Next step / Experiment | Thí nghiệm nhỏ nào gỡ được cản trở đó? | Đếm số cuộc gọi trong một tuần |
| 6. Expected outcome | Ta tin kết quả sẽ ra sao? | "Chắc khoảng 4 lần một tuần" |
| 7. Learning | Thực tế ra sao? | 7 lần một tuần, gấp đôi giả định |

Điểm mấu chốt mà Perri nhấn mạnh: những vòng lặp đầu tiên thường chỉ để đo current condition, và đây là bước hầu hết mọi người bỏ qua khi lao thẳng vào làm.

Nguồn: [Melissa Perri – The Product Kata](https://melissaperri.com/blog/2015/07/22/the-product-kata).

### 1.3 Bốn rủi ro lớn: bộ lọc trước khi xây

Marty Cagan nêu bốn rủi ro mọi ý tưởng sản phẩm phải vượt qua, kèm người chịu trách nhiệm từng loại.

| Rủi ro | Câu hỏi | Ai chịu trách nhiệm |
|---|---|---|
| **Value** | Khách hàng có mua, người dùng có chọn dùng không? | Product manager |
| **Usability** | Người dùng có tự hiểu cách dùng không? | Product designer |
| **Feasibility** | Kỹ sư có xây được với thời gian, kỹ năng, công nghệ đang có không? | Tech lead |
| **Business viability** | Giải pháp có chạy được với phần còn lại của doanh nghiệp không (pháp chế, tài chính, bán hàng, thương hiệu)? | Product manager |

Nguyên tắc Cagan nêu: xử lý rủi ro lớn **sớm**, và tìm giải pháp theo cách **cộng tác** chứ không phải chuyền tay theo thứ tự.

Nguồn: [SVPG – The Four Big Risks](https://www.svpg.com/four-big-risks/).

**Cách dùng thực tế** (suy luận): trước khi mở PRD, viết bốn dòng, mỗi dòng một rủi ro, ghi rõ ta đã có bằng chứng gì và còn thiếu bằng chứng gì. Rủi ro nào chưa có bằng chứng thì đó chính là việc discovery tiếp theo.

### 1.4 Product operating model: cách tổ chức vận hành

Cagan mô tả mô hình vận hành sản phẩm qua ba chiều và năm khái niệm.

Ba chiều: cách sản phẩm được xây (phát hành nhỏ, thường xuyên, đáng tin cậy, tối thiểu hai tuần một lần); cách vấn đề được giải (team tự tìm giải pháp vừa valuable, usable, feasible, viable thay vì nhận tính năng đặt sẵn); cách quyết định giải vấn đề nào (lãnh đạo đặt hướng bằng tầm nhìn hướng khách hàng và chiến lược dựa trên insight).

Năm khái niệm và nguyên tắc đi kèm:

| Khái niệm | Nguyên tắc Cagan nêu |
|---|---|
| Product culture | Nguyên tắc hơn quy trình; tin tưởng hơn kiểm soát; đổi mới hơn dự đoán được; học hơn là thất bại |
| Product strategy | Tập trung, insight, minh bạch, đặt cược có chủ đích |
| Product teams | Trao quyền, outcome hơn output, sở hữu, cộng tác |
| Product discovery | Giảm lãng phí, đánh giá rủi ro, thực nghiệm nhanh, kiểm thử có trách nhiệm |
| Product delivery | Phát hành nhỏ, đo đạc, giám sát, hạ tầng triển khai |

Cagan tóm chuyển dịch văn hóa thành một câu: chuyển từ cấp vốn, xây và phát hành **tính năng và dự án theo ngày cụ thể**, sang cấp vốn, xây và phát hành **sản phẩm để đạt outcome cần thiết**.

Nguồn: [SVPG – The Product Operating Model](https://www.svpg.com/the-product-operating-model-an-introduction/), [SVPG – Product Model Concepts](https://www.svpg.com/product-model-concepts/). Sách: *Inspired* (Wiley, 2017) và *Empowered* (Wiley, 2020), cả hai đã có bản Việt.

### 1.5 Discovery và delivery chạy song song

Cagan mô tả dual-track: discovery, tức việc tìm ra nên xây gì và liệu nó có chạy không, diễn ra **song song** với delivery, không phải hai giai đoạn nối đuôi. Bản thân Cagan đã bỏ cụm "Dual-track Agile" và chuyển sang gọi là continuous discovery và continuous delivery.

Định nghĩa team được trao quyền: team được giao **một vấn đề để giải**, không phải một giải pháp để xây, và không phải người nhận lệnh.

Nguồn: [SVPG – Dual-Track Agile](https://www.svpg.com/dual-track-agile/), [SVPG – Empowered Product Teams](https://www.svpg.com/empowered-product-teams/).

### 1.6 Kim tự tháp Product-Market Fit và tiến trình Lean Product

Dan Olsen chia sản phẩm thành năm tầng, xếp chồng từ dưới lên. PMF là mức độ ba tầng trên cộng hưởng với hai tầng dưới.

| Tầng (dưới lên) | Thuộc về | Nội dung |
|---|---|---|
| 1. Target customer | Problem space | Chọn phục vụ nhóm khách hàng nào |
| 2. Underserved needs | Problem space | Nhu cầu nào của họ đang bị phục vụ kém |
| 3. Value proposition | Solution space | Ta đáp ứng nhu cầu nào, tốt hơn đối thủ ra sao |
| 4. Feature set | Solution space | Chức năng nào hiện thực hóa lời hứa đó |
| 5. User experience | Solution space | Người dùng chạm vào giá trị đó qua giao diện nào |

Phân biệt cốt lõi: **problem space là thị trường, bạn không kiểm soát được**. Olsen nói bạn có thể chọn nhắm vào khách hàng nào và nhu cầu nào, nhưng không đổi được nhu cầu đó. **Solution space là phần bạn quyết định**. Sai lầm phổ biến là dồn sức cho ba tầng trên trong khi bỏ mặc nền móng ở hai tầng dưới.

Tiến trình Lean Product, 7 bước theo trang chính thức của sách:

1. Xác định khách hàng mục tiêu.
2. Tìm nhu cầu đang bị phục vụ kém.
3. Dựng chiến lược sản phẩm thắng cuộc.
4. Định nghĩa MVP.
5. Thiết kế nguyên mẫu MVP.
6. Kiểm thử MVP với khách hàng.
7. Lặp nhanh để đạt product-market fit.

Nguồn: [leanproductplaybook.com](https://leanproductplaybook.com/), [Mind the Product – Mastering the Problem Space](https://www.mindtheproduct.com/mastering-the-problem-space-for-product-market-fit-by-dan-olsen/). Sách: *The Lean Product Playbook* (Wiley, 2015), chưa có bản Việt.

### 1.7 Sáu khung này ghép với nhau thế nào

(Phần này là suy luận tổng hợp của người viết, không phải nội dung nguyên văn của nguồn nào.)

Đọc riêng lẻ thì sáu khung trên nghe như sáu trường phái. Thực ra chúng nằm ở sáu tầng khác nhau của cùng một việc:

- **Tầng tổ chức**: product operating model của Cagan trả lời câu hỏi công ty nên vận hành ra sao.
- **Tầng chẩn đoán**: build trap của Perri trả lời câu hỏi công ty đang hỏng ở đâu.
- **Tầng chiến lược**: Product Kata biến mục tiêu mơ hồ thành chuỗi target condition đo được.
- **Tầng thị trường**: kim tự tháp PMF của Olsen trả lời ta phục vụ ai và giải nhu cầu nào.
- **Tầng ý tưởng**: bốn rủi ro lớn lọc từng giải pháp trước khi tiêu tiền xây.
- **Tầng nhịp làm việc**: dual-track cho discovery chạy song song delivery.


## 2. Product Roadmap

Chi tiết đầy đủ kèm trích dẫn nguyên văn: [báo cáo roadmap](../plans/reports/researcher-260908-0238-roadmap-knowledge.md). Phần dưới là bản chắt lọc.

### 2.1 Roadmap là gì và không phải là gì

ProductPlan định nghĩa roadmap truyền đạt cái "vì sao" đằng sau thứ ta đang xây, là bản tóm tắt trực quan ở mức cao về tầm nhìn và hướng đi của sản phẩm. Và nói rõ nó **không phải** một danh sách tính năng xếp theo thứ tự ưu tiên, cũng không phải backlog.

Tempo Way nói cùng ý theo cách khác: roadmap nên là **sao Bắc Đẩu, không phải kế hoạch phát hành**. Roadmap tập trung vào chiến lược, không phải chiến thuật.

Thứ bậc bốn tầng theo ProductPlan: **tầm nhìn sản phẩm → mục tiêu sản phẩm → roadmap → kế hoạch phát hành và backlog**. Roadmap nằm ở tầng chiến lược, giữa tầm nhìn ở trên và chi tiết thực thi ở dưới.

| | Roadmap | Kế hoạch phát hành | Backlog |
|---|---|---|---|
| Đơn vị | Theme, vấn đề, cái "vì sao" | Ngày ship, phân bổ người, ai sở hữu | Task và tính năng chi tiết |
| Người đọc | Cả tổ chức, ban lãnh đạo | Team thực thi | Đội phát triển |
| Có ngày cứng | Không nên | Có | Theo sprint |

Roadmap cố ý **không** chứa: yêu cầu nguồn lực, giờ công, story point.

### 2.2 Now-Next-Later

Khung do **Janna Bastow và Simon Cast tạo năm 2012**, tên gốc là Current / Near Term / Future, sau đổi theo gợi ý của một khách hàng sớm. Lý do ra đời: Bastow cần thứ mà stakeholder hiểu trong khoảng mười giây, cho thấy ưu tiên mà không giả vờ biết chính xác tuần nào sẽ ship.

| Cột | Mức hiểu vấn đề | Mức chi tiết | Việc đang làm |
|---|---|---|---|
| **Now** | Vấn đề đã hiểu rõ | Đã spec đầy đủ, chia thành hạng mục cụ thể | Tìm giải pháp và đo outcome |
| **Next** | Đang xác thực | Ít chi tiết hơn, phụ thuộc kết quả của Now | Phỏng vấn khách hàng, đóng khung vấn đề, thử nghiệm sớm |
| **Later** | Còn mơ hồ | Chỉ là vấn đề lớn nhìn thấy ở đường chân trời | Khám phá rộng, đặt cược chiến lược |

Ba nguyên tắc:

1. **Xếp theo mức độ tự tin, không theo ngày.** ProdPad nói cột có ngày biến mọi ngày thành lời cam kết, và khi ưu tiên đổi thì cam kết vỡ.
2. **Chi tiết giảm dần theo khoảng cách.** Bạn không ra quyết định được cho thứ ở xa vì chưa nhìn rõ nó.
3. **Mỗi dòng là một vấn đề cần giải, không phải tính năng cần ship.**

Bốn cách dùng sai: biến ba cột thành Q1, Q2, Q3; nhồi tính năng thay vì vấn đề; nhồi quá tải cột Now; thêm deadline giả.

### 2.3 Roadmap theo outcome

Tempo Way chỉ ra khoảng trống: nhiều roadmap dồn quá nhiều chú ý vào tính năng cụ thể phải xây, thay vì outcome mà nó phải tạo ra cho doanh nghiệp và khách hàng. Điều này tạo ra khoảng cách giữa sản phẩm và lý do sản phẩm tồn tại.

Câu hỏi kiểm tra: bất kỳ ai trong công ty mở roadmap ra có trả lời được **tầm nhìn trong roadmap này đang đẩy chúng ta tới mục tiêu kinh doanh nào** hay không.

ProductPlan gọi cùng cơ chế đó là **theme**: theme nên hướng mục tiêu, mô tả giá trị khách hàng nhận được hoặc công việc ta giúp họ hoàn thành. Ví dụ theme của họ: "Khách hàng hoàn tất đơn hàng đầu tiên nhanh hơn". Các tính năng con nằm dưới theme, nên đổi tính năng con không phá vỡ roadmap tổng.

Cách viết một dòng roadmap theo outcome (suy luận từ định nghĩa, nguồn không cho câu ví dụ): thay vì viết "Xây dashboard báo cáo mới", viết "Khách hàng doanh nghiệp không tự tra được lịch sử giao dịch nên phải gọi hỗ trợ", để trống tên giải pháp.

### 2.4 Quy trình xây roadmap

ProductPlan dùng vòng lặp sáu khối: đặt mục tiêu chiến lược, thu thập và nhóm sáng kiến, ưu tiên, đề xuất roadmap, làm việc với stakeholder, truyền thông, rồi quay lại.

Tempo Way dùng chuỗi sáu bước: hiểu vai trò PM là người điều phối chứ không phải người quyết mọi thứ; đặt vấn đề trước, giải pháp sau (dùng Five Whys); tập hợp và quản lý stakeholder; thu thập rồi ưu tiên ý tưởng theo hai pha phân kỳ rồi hội tụ; trau chuốt và trình bày; tiến hóa roadmap.

Bốn điểm chung của cả hai:

- Chiến lược và tầm nhìn phải có **trước** khi liệt kê sáng kiến.
- Roadmap là tài liệu sống. ProductPlan cập nhật theo tuần hoặc tháng; Tempo cập nhật ngắn hạn hai tuần một lần và dài hạn tối thiểu hàng tháng.
- Phải biết nói không, phải hội tụ có chọn lọc.
- Phải tùy biến theo từng nhóm stakeholder, không dùng một bản cho tất cả.

Khác biệt đáng chú ý: ProductPlan nhấn KPI ngay từ đầu và ba kiểu trình bày; Tempo nhấn kỹ thuật khai vấn đề và vai trò điều phối của PM.

### 2.5 Khung ưu tiên

Cả hai nguồn cộng lại cho 13 khung. Năm khung xuất hiện ở cả hai: Value vs Effort, Kano, Buy a Feature, Opportunity Scoring, Story Mapping.

| Khung | Cách chấm | Khi nào dùng |
|---|---|---|
| **RICE** | Reach, Impact, Confidence chia Effort | Khi lượng hóa được chỉ số theo mục tiêu SMART |
| **Value vs Effort** | Ma trận hai trục giá trị và công sức | Khi cần nhanh và trực quan |
| **Weighted Scoring** | Chấm điểm nhiều tiêu chí lợi ích và chi phí | Khi cần thảo luận có cấu trúc, nhiều tiêu chí |
| **Kano** | Phân loại phải có, tỉ lệ thuận, gây thích thú | Khi có thời gian thu thập phản hồi khách hàng |
| **Opportunity Scoring** | Điểm quan trọng 1-10 trừ điểm hài lòng 1-10 | Khi có khảo sát theo từng nhu cầu, tìm quick win |
| **MoSCoW** | Must, Should, Could, Won't | Khi làm việc với stakeholder không rành kỹ thuật |
| **Cost of Delay** | Quy giá trị chậm trễ ra tiền | Khi muốn lượng hóa backlog bằng tài chính |
| **Buy a Feature** | Phát tiền giả cho nhóm để "mua" tính năng | Khi cần lấy ưu tiên từ nhóm đông |
| **Story Mapping** | Xếp story theo luồng công việc rồi kẻ lằn ranh phát hành | Khi cần xác định MVP và phạm vi từng bản phát hành |
| **Affinity Grouping** | Sticky note, nhóm theo tương đồng, bỏ phiếu | Khi khởi động ý tưởng theo nhóm |
| **Product Tree** | Cắt tỉa cây tính năng | Khi brainstorm phân kỳ |
| **Buckets of Features** | Phân bổ phần trăm công sức theo nhóm | Khi cần cân đối core, yêu cầu khách, sửa lỗi, đột phá |
| **T-shirt sizing** | S, M, L | Ước lượng công sức thô trước khi ưu tiên |

Mục đích thật của việc chấm điểm, theo Tempo Way: để **làm im tiếng người nói to nhất trong phòng**, dùng dữ liệu thay cho giai thoại.

### 2.6 Trình bày cho từng nhóm

| Nhóm | Mức chi tiết | Có ngày | Thông điệp chính |
|---|---|---|---|
| Ban lãnh đạo | Cao, theo theme | Không, ở giai đoạn hoạch định | Không gian thị trường, dữ liệu khách hàng, ROI tiềm năng. Bắt đầu bằng "vì sao" |
| Kỹ thuật | Chi tiết, có yêu cầu và mốc | Có, ở giai đoạn thực thi | Cần thấy bức tranh lớn để không mắc kẹt trong ốc đảo phát triển |
| Kinh doanh, hỗ trợ, marketing | Cao | Không, phải bỏ ngày cụ thể | Định vị sản phẩm mới, nó giải vấn đề gì để họ bán và hỗ trợ được |
| Khách hàng | Rất cao | Không | Chỉ nêu thứ đã duyệt và sắp thành hiện thực. Thứ còn bàn thì để mơ hồ hoặc bỏ hẳn |

Mối quan tâm riêng của từng lãnh đạo theo Tempo Way: tổng giám đốc hỏi việc này ảnh hưởng các đội khác ra sao; lãnh đạo kinh doanh hỏi tôi sẽ chào được gì cho khách; lãnh đạo marketing hỏi khi nào ra thị trường; lãnh đạo sản phẩm hỏi lợi thế cạnh tranh đến từ đâu.

### 2.7 Mười bốn sai lầm hay gặp

Từ Tempo Way: dùng roadmap như kế hoạch phát hành; nói với một nhóm khán giả duy nhất; không lượng hóa được phản hồi định tính thành sáng kiến có căn cứ.

Từ ProdPad: biến ba cột thành ba quý; nhồi tính năng thay vì vấn đề; nhồi quá tải cột Now; thêm deadline giả.

Từ ProductPlan: khóa cứng kế hoạch quá dài hạn; để kinh doanh dẫn dắt roadmap thay vì chiến lược; bỏ kỹ sư ngoài bức tranh lớn; chia sẻ quá nhiều chi tiết với khách rồi phải rút lại; chỉ nghe khách hàng hiện có vì đó là tập dữ liệu bị lệch; ưu tiên theo cảm hứng từng lúc không có khung; để roadmap ở dạng bảng tính chữ nhỏ khó cập nhật.

## 3. PRD, tài liệu yêu cầu sản phẩm

Chi tiết đầy đủ kèm trích dẫn: [báo cáo PRD](../plans/reports/researcher-260908-0238-prd-knowledge.md).

### 3.1 PRD là gì và ai đọc

Product School định nghĩa PRD là bản hướng dẫn xác định yêu cầu của một sản phẩm cụ thể, gồm mục đích, tính năng, chức năng và hành vi.

Kevin Yien, tác giả template PRD của Square, mô tả mục đích thực dụng hơn: PRD giúp cả team **nheo mắt lại và cùng nhìn thấy một hình dạng** trước khi bắt tay xây.

Aha! nói template PRD của họ dành chủ yếu cho product manager, UX designer và đội phát triển. Atlassian có hẳn mục ghi vai trò từng thành viên, tức người đọc còn gồm cả QA và các stakeholder liên quan.

Không nguồn nào trong năm nguồn đã đọc nêu tiêu chí rõ ràng khi nào **không** cần viết PRD.

### 3.2 Bộ khung tối thiểu, rút ra từ 5 nguồn

So sánh cấu trúc PRD của Atlassian, Product School, Square, Figma và Aha!, năm mục xuất hiện ở ít nhất bốn trên năm nguồn:

1. **Vấn đề hoặc mục tiêu.**
2. **Success metrics.**
3. **Yêu cầu và tính năng chính.**
4. **Phạm vi hoặc non-goals.**
5. **Câu hỏi mở.**

Xuất hiện ở ba tới bốn nguồn: thông tin cơ bản và vai trò team, bối cảnh và persona, tài liệu hỗ trợ và luồng chính, mốc thời gian.

Danh sách đầy đủ của Product School gồm **14 mục**: title, change history, overview, success metrics, messaging, timeline và release planning, personas, user scenarios, user stories và requirements, features out, designs, open issues, Q&A, other considerations.

### 3.3 Viết từng mục ra sao

**Vấn đề.** Template của Square yêu cầu mô tả trong **1 tới 2 câu**, kèm bằng chứng vì sao vấn đề quan trọng với khách hàng và doanh nghiệp.

| Tốt | Tệ |
|---|---|
| "23% khách hàng doanh nghiệp rời bỏ trong tháng đầu vì không tìm được cách mời thành viên vào workspace, theo phỏng vấn 15 khách hàng đã rời, tháng 8/2026." | "Trải nghiệm onboarding của chúng ta chưa tốt lắm." |

**Success metrics.** Atlassian ví dụ dạng "tăng điểm hài lòng khách hàng 15%". Square phân biệt rõ hai loại mục tiêu: **đo được** và **không đo được** tức cảm nhận, miễn là phân loại rành mạch, không lẫn lộn.

Khuôn viết đề xuất (tổng hợp thực hành, không nguồn nào cho công thức này): tên chỉ số, mốc hiện tại, mốc mong muốn, thời hạn đo.

| Tốt | Tệ |
|---|---|
| "Thời gian trung bình mời xong một team: từ 8 phút hiện tại, đo qua công cụ phân tích, xuống dưới 2 phút, đo trong 30 ngày sau ra mắt." | "Tăng sự hài lòng của người dùng." |

**Non-goals.** Đây là mục bị bỏ nhiều nhất và cũng là mục Square nhấn mạnh nhất. Nguyên văn hướng dẫn: liệt kê rõ những vùng ta **không** định đụng tới, và **giải thích vì sao chúng không phải mục tiêu**. Square nói non-goals quan trọng và làm rõ ngang với goals.

| Tốt | Tệ |
|---|---|
| "Không hỗ trợ nhập từ Google Sheets ở bản này, vì dưới 5% khách khảo sát dùng Sheets làm nguồn danh sách. Sẽ xét lại quý 1/2027 nếu nhu cầu tăng." | "Không làm tích hợp Google Sheets." |

Cơ chế chống phình phạm vi: khi non-goal có kèm lý do, ai muốn thêm hạng mục đó vào giữa chừng phải phản biện lại lý do đã ghi, thay vì âm thầm mở rộng phạm vi.

**Câu hỏi mở.** Atlassian dùng bảng gồm câu hỏi, câu trả lời, ngày hoàn thành. Viết tốt là "Chưa quyết: có cho phép nhập tệp trên 50 dòng không? Cần ý kiến trưởng nhóm kỹ thuật trước 15/09, người phụ trách ghi rõ". Viết tệ là "Còn vài vấn đề cần bàn thêm".

### 3.4 Amazon Working Backwards và PR-FAQ

Cấu trúc thông cáo báo chí viết ngược, theo template của Ian McAllister:

1. Tiêu đề theo mẫu "[Công ty] công bố [dịch vụ] cho phép [nhóm khách hàng] [lợi ích]", kèm tiêu đề phụ diễn giải.
2. Ngày và địa điểm, dùng ngày ra mắt dự kiến.
3. **Vấn đề**: tối đa 3 tới 4 điểm đau, xếp theo mức nghiêm trọng, **không nhắc giải pháp ở đây**.
4. **Giải pháp**: giải quyết từng vấn đề ra sao.
5. Trích lời lãnh đạo giải thích vì sao công ty làm việc này.
6. Chi tiết sản phẩm: khách hàng cần làm gì để dùng.
7. Trích lời khách hàng, là lời giả định nhưng phải thực tế.
8. Lời kêu gọi hành động.

Khác biệt so với PRD (đối chiếu cấu trúc, không phải trích dẫn trực tiếp): PR-FAQ viết bằng giọng thông cáo hướng khách hàng cuối và bắt đầu từ trải nghiệm đã hoàn thành rồi lần ngược về yêu cầu. PRD viết bằng giọng nội bộ, bắt đầu từ vấn đề rồi đi tới bảng yêu cầu và mốc ra mắt.

Lưu ý: phần FAQ trong mô hình PR-FAQ chưa đọc được chi tiết từ nguồn, nên không mô tả ở đây.

### 3.5 Bốn sai lầm hay gặp

Theo Product School: viết PRD chỉ để cho có; không hỏi ý kiến stakeholder trước khi chốt; mất cân bằng giữa yêu cầu kỹ thuật và nhu cầu khách hàng; thiếu mục tiêu rõ ràng.

Ngược lại, thực hành tốt mà Product School nêu: PRD là tài liệu sống cần cập nhật liên tục; chấp nhận để trống ở bản nháp; cân bằng giữa chính xác và súc tích; là sản phẩm của làm việc nhóm chứ không phải của một người.

### 3.6 Khung PRD tổng hợp cuối

Sau khi đối chiếu năm template với tài liệu gốc của Cagan và với một khung "PRD world-class" thiên kỹ thuật, khung tổng hợp cuối gồm 11 mục, đánh số 0 tới 10, kèm nguồn từng mục, nằm ở [mục 8 của báo cáo đối chiếu](../plans/reports/prd-synthesis-260908-0254-world-class-prd-vs-verified-sources.md). Tóm tắt: thông tin chung và trạng thái; vấn đề và bối cảnh; mục tiêu và non-goals kèm lý do; nguyên tắc sản phẩm; chỉ số chính và chỉ số bảo vệ; giả định; yêu cầu có tiêu chí nghiệm thu, phân loại và xếp hạng; luồng chính và ma trận trạng thái biên; tiêu chí phát hành và tracking plan; kế hoạch ra mắt và rút lui; câu hỏi mở.

Bản template markdown gốc từ năm nguồn vẫn ở [mục 7 của báo cáo PRD](../plans/reports/researcher-260908-0238-prd-knowledge.md).

### 3.7 Việc phải làm trước khi viết, theo Cagan

Tài liệu [How To Write a Good PRD](https://www.svpg.com/wp-content/uploads/2024/07/How-To-Write-a-Good-PRD.pdf) của Marty Cagan năm 2005, PDF miễn phí 26 trang trên SVPG, đặt bước "viết ra" ở vị trí thứ 7 trong 10 bước. Sáu bước trước đó: làm bài tập về nhà về khách hàng, đối thủ và công nghệ; xác định mục đích nói được trong một chuyến thang máy; hồ sơ người dùng, mục tiêu, tác vụ; nguyên tắc sản phẩm; **dựng nguyên mẫu và thử** về khả thi, dùng được và có muốn mua; chất vấn giả định. Ba bước sau: xếp hạng ưu tiên 1 tới n trong từng loại must-have, high-want, nice-to-have; kiểm tra hoàn chỉnh bằng câu hỏi kỹ sư có xây được và QA có viết test được không; quản lý PRD như tài liệu sống tới lúc ra mắt.

Bốn khu vực của văn bản theo Cagan 2005: mục đích sản phẩm, tính năng, **tiêu chí phát hành** gồm hiệu năng, khả năng mở rộng, độ tin cậy, dùng được, hỗ trợ được, bản địa hóa được, và lịch dưới dạng cửa sổ có lý do.

Một năm sau, trong bài [Revisiting the Product Spec](https://www.svpg.com/revisiting-the-product-spec/), Cagan kết luận văn bản thất bại vì mất quá lâu để viết, hiếm khi được đọc, không đủ chi tiết, và tạo tự tin giả. Ông đề xuất **nguyên mẫu độ trung thực cao là bản spec chính**, văn bản chỉ là chú giải cho những gì nguyên mẫu không thể hiện được. Hai tài liệu không mâu thuẫn nếu đọc theo trình tự: thử trước, viết sau.

### 3.8 Cảnh báo về các "PRD thật" trên mạng

Mọi ví dụ được quảng cáo là PRD thật của Mercury, Spotify, Product Hunt, AirPods, Airbnb đều là **bản dựng lại hoặc mẫu minh họa do bên thứ ba viết**, không phải tài liệu chính thức công ty phát hành. Dùng chúng để học cấu trúc thì được, trích dẫn như bằng chứng về cách công ty đó làm việc thì không.

## 4. Discovery: tìm đúng thứ cần làm

Chi tiết đầy đủ: [báo cáo discovery và chỉ số](../plans/reports/researcher-260908-0240-discovery-metrics-knowledge.md).

### 4.1 Opportunity Solution Tree

Công cụ của Teresa Torres, gắn với sách *Continuous Discovery Habits*. Template Miro, Mural và FigJam miễn phí trên [producttalk.org](https://www.producttalk.org/opportunity-solution-trees/).

Cây có bốn tầng, từ đỉnh xuống:

| Tầng | Nội dung |
|---|---|
| **Outcome** | Nhu cầu kinh doanh phản ánh cách team tạo ra giá trị. Torres khuyên dùng **product outcome**, không phải business outcome quá rộng |
| **Opportunity** | Nhu cầu chưa được đáp ứng, điểm đau, mong muốn của khách hàng. Nếu giải quyết được thì sẽ đẩy outcome ở trên |
| **Solution** | Sản phẩm, tính năng, dịch vụ, quy trình, tài liệu, bất cứ thứ gì ta đưa cho khách hàng |
| **Assumption test** | Cách đánh giá giải pháp nào giúp tạo giá trị khách hàng tốt nhất |

Bốn quy tắc Torres nêu:

1. Opportunity phải đến từ **phỏng vấn khách hàng thật**, không được bịa ra từ suy đoán nội bộ.
2. Phép thử phân biệt opportunity với solution: **có nhiều hơn một cách giải quyết nó không?** Nếu chỉ có đúng một cách thì đó là giải pháp, không phải cơ hội.
3. Ở tầng giải pháp, so sánh **ít nhất ba giải pháp** cho cùng một cơ hội trước khi chọn.
4. Mỗi giải pháp gắn với **đúng một cơ hội**.

Nhịp cập nhật: xem lại bản đồ cơ hội **sau mỗi 3 tới 4 cuộc phỏng vấn khách hàng**, không đợi hết một đợt nghiên cứu.

Quy trình chín bước: đáp ứng điều kiện tiên quyết, đặt outcome ở đỉnh, vẽ bản đồ cơ hội, chọn cơ hội mục tiêu, brainstorm giải pháp, chọn ba giải pháp để khám phá, phân tích giả định của từng giải pháp, kiểm chứng giả định rủi ro nhất, đánh giá và quyết định bước tiếp.

Cây không phải bản kế hoạch cố định. Torres mô tả nó là công cụ giúp team **đưa suy nghĩ ra ngoài đầu và nhìn thấy được**, để dễ đồng thuận về việc làm gì vào lúc nào.

### 4.2 Kết hợp định lượng với định tính

Thực hành mà Pendo ghi lại từ một trưởng nhóm vận hành sản phẩm: dùng phân tích sản phẩm ở pha học hỏi để tìm lỗ hổng và hiểu luồng công việc của người dùng, sau đó phỏng vấn người dùng để đồng cảm với trải nghiệm của họ.

Trình tự: **dữ liệu định lượng chỉ ra chỗ cần xem, phỏng vấn định tính giải thích vì sao**.

## 5. Chỉ số sản phẩm

### 5.1 Retention, chỉ số có công thức rõ nhất

Pendo định nghĩa: so sánh số khách hàng đầu kỳ với cuối kỳ, **loại trừ khách hàng mới có được trong kỳ**.

```
Retention = (khách cuối kỳ − khách mới trong kỳ) / khách đầu kỳ
```

Ví dụ trong tài liệu: bắt đầu 100 khách, thêm 10 mới, mất 10 khách cũ, cuối kỳ vẫn 100 khách nên tăng trưởng nhìn có vẻ phẳng, nhưng retention chỉ **90%**. Kết luận: thu hút khách mạnh không che được retention thấp.

### 5.2 Feature adoption theo bốn chiều

Tài liệu Pendo 2020 nêu bốn chiều. Bản 2022 chỉ còn ba, bỏ chiều Depth. Giữ nguyên cả hai thay vì gộp.

| Chiều | Câu hỏi | Tín hiệu |
|---|---|---|
| **Breadth** | Tính năng được dùng rộng tới đâu trong tệp người dùng | Sức hấp dẫn ban đầu |
| **Depth** (chỉ có ở bản 2020) | Nhóm người dùng chính chạm vào nó thường xuyên thế nào | Nhu cầu thường trực, hoặc khó dùng |
| **Time to adopt** | Mất bao lâu để khách bắt đầu dùng | Adopt càng nhanh càng khớp điểm đau có thật |
| **Duration** | Người dùng tiếp tục dùng bao lâu sau khi biết | Gắn với retention. Duration thấp là dấu hiệu cần làm mới |

Cách chọn tính năng đáng theo dõi: tìm nhóm tính năng tạo ra **80% tổng lượng click** của sản phẩm.

Ứng viên loại bỏ: tính năng hoặc trang **không hoạt động trên 90 ngày**. Nhưng phải kiểm nguyên nhân trước, vì có thể người dùng không tìm thấy nó chứ không phải không cần nó.

### 5.3 NPS, hai cấp và một cái bẫy

Pendo phân biệt **NPS cấp tài khoản** và **NPS cấp người dùng**. Điểm của người dùng thường cao hơn điểm tài khoản, vì điểm tài khoản bị kéo xuống bởi những góc nhìn ít hiểu sản phẩm hơn.

Cái bẫy: khảo sát trong ứng dụng cho điểm **cao hơn** khảo sát qua email, vì nó bắt đúng nhóm người dùng đang tích cực. Muốn so sánh theo thời gian thì phải giữ nguyên một phương pháp.

Công thức NPS chuẩn không có trong các tài liệu Pendo, nên không ghi ở đây.

### 5.4 Đo hiệu quả onboarding

Ba tầng đo:

1. **Tương tác với nội dung**: số lượt xem hướng dẫn, tỷ lệ hoàn tất từng bước, thời gian ở trong hướng dẫn.
2. **Tác động lên sử dụng sản phẩm**: theo dõi các tính năng đã đưa vào onboarding, dùng phễu để tìm bước rơi rụng.
3. **Tác động lên kết quả kinh doanh**: khách đã qua onboarding có tạo ít phiếu hỗ trợ hơn không, hoàn tất onboarding có tương quan với gắn bó dài hạn và ít rời bỏ hơn không.

Nguyên tắc thiết kế: onboarding riêng theo từng nhóm; phân biệt **người dùng mới trong tài khoản đã có** với **tài khoản hoàn toàn mới**, vì nhóm đầu chỉ cần cập nhật nhanh chứ không cần thiết lập lại từ đầu.

Liên hệ trực tiếp mà Pendo nêu: rút ngắn thời gian tới giá trị là mấu chốt để chống rời bỏ, vì chi phí chuyển đổi của phần mềm dịch vụ rất thấp.

### 5.5 Ba nguyên tắc cho vòng phản hồi

1. **Làm cho dễ.** Thu thập theo điều kiện của khách, không bắt họ đi tìm form liên hệ. Khảo sát định kỳ đơn lẻ là không đủ.
2. **Làm cho thông minh.** Cho khách tự xếp mức ưu tiên phản hồi của họ.
3. **Đóng vòng lặp.** Phải có tầm nhìn, quy trình và công cụ xử lý **trước khi** bắt đầu thu thập, nếu không phản hồi rơi vào hố đen.

Khi nối phản hồi vào roadmap: nhắm đúng người có ý kiến giá trị nhất, phân nhóm phản hồi theo quy mô công ty, doanh thu, vai trò, ngành. Ghép phản hồi với dữ liệu sử dụng để ưu tiên, nhưng nhớ rằng tính năng ít dùng chưa chắc vô dụng, có thể người dùng đang kẹt ở một bước trong luồng.

### 5.6 Product operations

Pendo mô tả đây là đội chuyên trách tối ưu vận hành cho team sản phẩm, giống vai trò của vận hành bán hàng với đội bán hàng. Năm nhiệm vụ: quản lý bộ công cụ; thu thập và phân tích dữ liệu; điều phối thử nghiệm; thúc đẩy hợp tác liên phòng ban quanh chiến lược; làm cố vấn tin cậy cho lãnh đạo sản phẩm.

Không có ngưỡng cụ thể về quy mô để biết khi nào cần lập đội này.

## 6. AI trong quản lý sản phẩm

Pendo chia vòng đời thành sáu pha, tất cả hướng tới kết quả kinh doanh.

| Pha | AI làm được gì |
|---|---|
| **Discover** | Tổng hợp dữ liệu từ hỗ trợ khách hàng, phỏng vấn, khảo sát, cuộc gọi bán hàng và dữ liệu sử dụng. Nhận diện mẫu hình xuyên nguồn. Đưa khuyến nghị kèm bằng chứng để biện minh cho đề xuất đầu tư |
| **Validate** | Phân tích nhanh dữ liệu xác thực nhiều kênh. Tạo nguyên mẫu nhanh hơn từ mô tả. Thử nhiều nguyên mẫu **cùng lúc** |
| **Build** | Lập bản đồ mã nguồn, gợi ý tác động của thay đổi lên toàn sản phẩm. Soạn user story và tiêu chí chấp nhận từ mô tả ngắn để người viết chỉnh lại |
| **Launch** | Triển khai có kiểm soát dựa trên dữ liệu sử dụng. Tự tạo bảng theo dõi mức độ tiếp nhận và tác động kinh doanh. Gợi ý đúng tính năng cho đúng người dùng |
| **Evaluate** | Tự xác định cái gì đang chạy và không chạy, phân tích toàn bộ dữ liệu ở quy mô con người không tự làm nổi |
| **Iterate** | Hỗ trợ ưu tiên cải tiến tiếp theo, khởi động lại vòng lặp |

Ranh giới mà Pendo nêu rõ: AI **bổ trợ** chứ không thay thế vai trò PM. Thứ còn lại thuộc về con người là tư duy chiến lược, sự đồng cảm, khả năng thích ứng và hiểu biết thực tế. Hệ quả kèm theo: PM sẽ ngày càng bị đo bằng **kết quả đạt được**, không phải số tính năng đã ship.

## 7. Lộ trình học đề xuất

(Phần này là đề xuất của người viết, không phải nội dung của nguồn nào.)

**Tuần 1 tới 2, hiểu bức tranh.** Đọc Inspired bản Việt. Đọc miễn phí các bài nền tảng của SVPG về bốn rủi ro lớn, team được trao quyền, mô hình vận hành sản phẩm.

**Tuần 3 tới 4, chẩn đoán chỗ đang hỏng.** Đọc Escaping the Build Trap, tên tiếng Việt là *Quản Lý Sản Phẩm Trong Thời Đại 4.0*. Chạy thử một vòng Product Kata cho một mục tiêu thật của bạn.

**Tuần 5 tới 6, làm PRD cho tử tế.** Dựng lại một PRD cũ theo khung 11 mục ở mục 3.6. Bắt buộc viết đủ phần non-goals kèm lý do và success metrics có mốc hiện tại lẫn mốc mong muốn.

**Tuần 7 tới 8, roadmap.** Đọc ebook roadmap miễn phí của ProductPlan. Chuyển roadmap hiện tại sang Now-Next-Later, mỗi dòng viết là một vấn đề chứ không phải tính năng. Chọn một khung ưu tiên và dùng nhất quán.

**Tuần 9 tới 12, discovery.** Đọc Continuous Discovery Habits, chưa có bản Việt. Dựng một Opportunity Solution Tree bằng template Miro miễn phí. Đặt lịch phỏng vấn khách hàng hàng tuần, cập nhật cây sau mỗi 3 tới 4 cuộc.

**Song song suốt quá trình.** Đọc bốn PDF miễn phí của Pendo để dựng bộ chỉ số. Bắt đầu với retention, breadth và time to adopt của các tính năng chiếm 80% lượng click, cùng ba chỉ số onboarding.

## 8. Nguồn và mức độ tin cậy

| Loại | Nguồn |
|---|---|
| **Chính chủ, tin cậy cao** | SVPG (Cagan, gồm PDF How To Write a Good PRD 2005 và bài Revisiting the Product Spec 2006), Product Talk (Torres), melissaperri.com, leanproductplaybook.com, trang Wiley và O'Reilly của từng sách |
| **Nguồn gốc khái niệm mượn** | Guardrail metric: Kohavi, Tang, Xu 2020. Given-When-Then: Dan North 2006 |
| **Vendor, miễn phí, đã kiểm mở được** | ProductPlan (PDF roadmap), Pendo (4 PDF), Tempo Way, ProdPad (Now-Next-Later), Atlassian (PRD template), Aha! (guides và template), Product School (ebook và PRD template), Productboard (12 ebook sau form), Amplitude |
| **Tổng hợp bên thứ ba, cần kiểm lại** | Bài liệt kê sách của Amplitude, Dovetail, Pragmatic Institute; ví dụ PRD của Figr, ChatPRD, HelloPM |

Ba báo cáo chi tiết kèm trích dẫn nguyên văn:

- [Kiến thức roadmap](../plans/reports/researcher-260908-0238-roadmap-knowledge.md)
- [Kiến thức PRD](../plans/reports/researcher-260908-0238-prd-knowledge.md)
- [Đối chiếu khung PRD world-class với nguồn, và khung tổng hợp cuối](../plans/reports/prd-synthesis-260908-0254-world-class-prd-vs-verified-sources.md)
- [Kiến thức discovery và chỉ số](../plans/reports/researcher-260908-0240-discovery-metrics-knowledge.md)
- [Danh mục sách và tài liệu kèm trạng thái kiểm chứng](../plans/reports/deep-research-260908-0214-product-management-ebooks-catalog.md)

## Câu hỏi chưa giải quyết

1. Thành phần cụ thể của product trio ngoài PM không có trong trang Product Talk đã đọc, cần chính cuốn sách để xác nhận.
2. Không nguồn nào so sánh trực tiếp discovery liên tục với nghiên cứu theo đợt.
3. Công thức NPS chuẩn không có trong tài liệu Pendo, nếu cần thì phải lấy từ nguồn khác và ghi nguồn riêng.
4. Aha! có hai mô tả cấu trúc PRD khác nhau ở hai trang, chưa rõ trang nào là bản chính thức hiện hành.
5. Phần FAQ trong mô hình PR-FAQ của Amazon chưa đọc được chi tiết.
6. Không nguồn nào nêu tiêu chí khi nào **không** cần viết PRD.
