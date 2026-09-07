# Kiến thức thực chất về PRD (Product Requirements Document) — chắt lọc từ nguồn miễn phí đã xác minh

Ngày nghiên cứu: 2026-09-08. Phương pháp: WebFetch trực tiếp từng URL, đọc nguyên văn, không suy diễn ngoài nội dung đã đọc được.

---

## 1. PRD là gì, giải quyết vấn đề gì, ai đọc, khi nào cần / không cần

**Định nghĩa** (nguồn: Product School — https://productschool.com/blog/product-strategy/product-template-requirements-document-prd):
PRD là "a guide that defines a particular product's requirements, including its purpose, features, functionality, and behavior" — tài liệu định nghĩa yêu cầu của một sản phẩm: mục đích, tính năng, chức năng, hành vi.

**Vấn đề PRD giải quyết** (tổng hợp từ các nguồn):
- Atlassian: PRD giúp team giải thích "how this project supports your organization's larger goals" — căn chỉnh lý do tồn tại của tính năng/sản phẩm với mục tiêu tổ chức, đồng thời chống trôi phạm vi qua mục Out of Scope.
- Aha! (https://www.aha.io/roadmapping/guide/requirements-management/what-is-a-good-product-requirements-document-template): PRD "mô tả những gì sản phẩm sẽ bao gồm và cách hoạt động", dịch MRD (Market Requirements Document — tài liệu yêu cầu thị trường) thành "các tính năng và kế hoạch phát triển cụ thể".
- Kevin Yien/Square (PRD template, Google Docs): PRD dùng để "squint your eyes and see the same shape" — giúp cả team hình dung cùng một giải pháp trước khi build, và ghi rõ Non-Goals để tránh hiểu lầm phạm vi.

**Ai đọc PRD**: Aha! ghi rõ template "được xây dựng chủ yếu cho product manager, UX designer, và development team, dù cũng hữu ích cho bất kỳ ai trong tổ chức muốn hiểu mục tiêu sản phẩm, nhu cầu người dùng và tính năng cốt lõi". Atlassian nêu PRD có phần "team roles" (vai trò các thành viên chủ chốt tham gia) — ngụ ý đối tượng đọc gồm PM, kỹ sư, thiết kế, QA, và stakeholder liên quan.

**Khi nào cần / không cần viết PRD**: (suy luận, không có trong nguồn) — không nguồn nào trong 5 nguồn đọc được nêu tiêu chí rõ ràng "khi nào cần / không cần viết PRD". Product School có nêu PRD "are living documents" cần cập nhật liên tục, và là "sản phẩm của teamwork" — ngụ ý PRD phù hợp cho tính năng/sản phẩm đủ lớn cần nhiều bên liên quan phối hợp, nhưng đây là suy luận của người viết báo cáo, không phải câu trích trực tiếp về "khi nào không cần".

---

## 2. Bảng so sánh cấu trúc PRD giữa các nguồn

Nguồn dùng: Atlassian (https://www.atlassian.com/software/confluence/templates/product-requirements), Product School (https://productschool.com/blog/product-strategy/product-template-requirements-document-prd), Square/Kevin Yien (qua Lenny's Newsletter, https://www.lennysnewsletter.com/p/my-favorite-templates-issue-37 → Google Doc gốc), Figma (qua Lenny's Newsletter → Coda doc gốc), Aha! (https://www.aha.io/roadmapping/guide/requirements-management/what-is-a-good-product-requirements-document-template, mở rộng từ trang templates gốc theo yêu cầu vì trang templates chỉ liệt kê link không mô tả nội dung).

| Nhóm mục (canonical) | Atlassian | Product School | Square (Kevin Yien) | Figma | Aha! |
|---|---|---|---|---|---|
| Thông tin cơ bản / team roles / status | ✅ (PRD Basics & Team Roles) | ✅ (Title, Change History) | — | — | ✅ (Overview) |
| Objective / vấn đề cần giải quyết | ✅ (Objective) | ✅ (Overview) | ✅ (The Problem, High Level Approach) | ✅ (The Problem, High-level Approach) | ✅ (Objective) |
| Context / personas / narrative / thị trường | — | ✅ (Personas, User Scenarios) | ✅ (Narrative) | — | ✅ (Context) |
| Success metrics | ✅ (Success Metrics) | ✅ (Success Metrics) | ✅ (Goals — có "measurable metrics") | ✅ (Goals & Success) | ✅ (Performance) |
| Assumptions | ✅ (Assumptions) | — | — | — | ✅ (Assumptions) |
| Scope / Non-Goals / Out-of-Scope / Features Out | ✅ (Out of Scope) | ✅ (Features Out) | ✅ (Non-Goals — nhấn mạnh riêng) | — (không có mục riêng, gần nhất là Open Issues & Key Decisions) | ✅ (Scope) |
| Requirements / Features / User Stories | ✅ (Options — bảng requirement + user story + priority) | ✅ (User Stories/Features/Requirements) | ✅ (Key Features, Key Logic) | ✅ (Key Features) | ✅ (Requirements) |
| Supporting docs / mockup / flows / design | ✅ (Supporting Documentation) | ✅ (Designs) | ✅ (Key Flows) | ✅ (Key Flows) | — (không nêu riêng trong bài; template gốc chỉ nói "note-style area") |
| Timeline / Launch plan / Milestones | — | ✅ (Timeline/Release Planning) | ✅ (Launch Plan, Key Milestones) | ✅ (Key Milestones, Launch Checklist) | — |
| Open Questions | ✅ (Open Questions) | ✅ (Open Issues, Q&A) | ✅ (Appendix: Open Questions, FAQs) | ✅ (Open Issues & Key Decisions) | ✅ (Open questions) |
| Khác (Changelog, Messaging, Impact Checklist, Other Considerations) | — | ✅ (Messaging, Other Considerations) | ✅ (Appendix: Changelog, Impact Checklist) | — | — |

**Bộ khung tối thiểu (xuất hiện ở ≥4/5 nguồn)**: Objective/Problem, Success Metrics, Requirements/Features, Scope hoặc Non-Goals/Out-of-Scope, Open Questions. Gần đủ (3-4/5): thông tin cơ bản, context/narrative, supporting docs/flows, timeline/milestones.

Ghi chú: trang Aha! templates gốc (https://www.aha.io/roadmapping/guide/templates) mà đề bài chỉ định KHÔNG mô tả cấu trúc PRD cụ thể — chỉ liệt kê link. Cấu trúc 8 mục ở trên lấy từ trang con sâu hơn của Aha! (what-is-a-good-product-requirements-document-template) để đáp ứng yêu cầu "giải thích từng mục cốt lõi". Trang https://www.aha.io/roadmapping/guide/templates/create/prd mô tả PRD template Aha! theo hướng khác: 4 cấp Product/Release/Epic/Feature requirements, không trùng khớp hoàn toàn với 8 mục trên — hai trang Aha! không nhất quán về cấu trúc "PRD" (ghi nhận khác biệt, không tự ý chọn một bên là đúng).

---

## 3. Giải thích từng mục cốt lõi: viết gì, viết bao nhiêu, ví dụ câu tốt/tệ

### Objective / The Problem
- Nguồn: Atlassian — giải thích "how this project supports your organization's larger goals". Kevin Yien/Square — "Describe the problem we are trying to solve in 1-2 sentences" (nguyên văn từ template), kèm bằng chứng vì sao vấn đề quan trọng với khách hàng và doanh nghiệp. Figma — tương tự "The Problem" mô tả vấn đề/cơ hội, tầm quan trọng với người dùng và kinh doanh.
- Viết bao nhiêu: 1-2 câu (theo hướng dẫn nguyên văn Kevin Yien).
- Câu mẫu tốt (theo tinh thần nguồn, có bằng chứng, cụ thể): "23% khách hàng doanh nghiệp rời bỏ trong tháng đầu vì không tìm được cách mời thành viên team vào workspace (theo phỏng vấn 15 khách hàng churned, tháng 8/2026)."
- Câu mẫu tệ (mơ hồ, không có bằng chứng, không đo được): "Trải nghiệm onboarding của chúng ta chưa tốt lắm."

### Success Metrics / Goals & Success / Performance
- Nguồn: Atlassian — bảng liệt kê "product or feature-specific goals" và metrics theo dõi, ví dụ nêu trong trang: "tăng điểm hài lòng khách hàng 15%". Kevin Yien/Square — Goals gồm cả "measurable (metrics) and immeasurable (feelings) goals", ưu tiên theo thứ tự. Aha! — mục Performance là "metrics for success" để đo giá trị.
- Xem chi tiết cách viết định lượng ở mục 4.

### Assumptions
- Nguồn: Atlassian — "assumptions you have about your users, technical constraints, and business goals" (giả định về người dùng, ràng buộc kỹ thuật, mục tiêu kinh doanh). Aha! cũng có mục Assumptions riêng nhưng không mô tả chi tiết nội dung.
- Câu mẫu tốt: "Giả định: 80% khách hàng mục tiêu dùng Chrome/Safari trên desktop; nếu sai, cần audit lại ưu tiên mobile."
- Câu mẫu tệ: "Giả định người dùng sẽ thích tính năng này."

### Requirements / Options / Key Features
- Nguồn: Atlassian — bảng "Options" ánh xạ requirement với user story, mức độ quan trọng (priority), Jira issue liên kết, ghi chú. Product School — "User Stories/Features/Requirements". Kevin Yien/Square — Key Features là danh sách tính năng có ưu tiên, mô tả như "drawing the perimeter of the solution space" (vẽ ranh giới không gian giải pháp). Figma — tương tự, "tổng quan những gì sẽ xây dựng, danh sách tính năng có ưu tiên".
- Viết bao nhiêu: mỗi requirement nên gắn 1 user story + mức ưu tiên (must/should/could), không viết đặc tả kỹ thuật chi tiết trong PRD (PRD nêu "cái gì/tại sao", spec kỹ thuật để tài liệu riêng — suy luận từ cách các template tách Key Features khỏi Key Logic/technical scoping).
- Câu mẫu tốt: "Là một admin, tôi muốn mời tối đa 50 thành viên cùng lúc bằng CSV import, để không phải mời từng người (Must-have)."
- Câu mẫu tệ: "Cải thiện tính năng mời thành viên."

### Non-Goals / Out of Scope / Features Out / Scope
- Xem chi tiết ở mục 5.

### Supporting Documentation / Key Flows
- Nguồn: Atlassian — thêm mockup, diagram, visual design liên quan. Figma/Square — Key Flows "show what the end-to-end experience will be" qua story, diagram, hoặc design, đại diện các hành trình người dùng chính (bao gồm cả "edgy use cases" theo Square).
- Viết bao nhiêu: không cần vẽ toàn bộ UI, chỉ đủ để người đọc hình dung luồng chính + 1-2 luồng biên (edge case).

### Open Questions
- Nguồn: Atlassian — bảng theo dõi câu hỏi, câu trả lời, ngày hoàn thành. Product School — tách hai mục Open Issues và Q&A. Square — đưa vào Appendix cùng FAQs.
- Câu mẫu tốt: "Chưa quyết: có cho phép import CSV >50 dòng không? Cần feedback từ Eng lead trước 15/09. Owner: @minh."
- Câu mẫu tệ: "Còn vài vấn đề cần bàn thêm."

### Timeline / Launch Plan / Key Milestones
- Nguồn: Product School — "Timeline/Release Planning". Square — Launch Plan định nghĩa các giai đoạn (pilot, beta, early access, launch) kèm mục đích, tiêu chí chuyển giai đoạn (exit criteria), rủi ro; Key Milestones là bảng mốc thời gian + mô tả + exit criteria. Figma — Key Milestones (Dogfood, Beta, Launch) + Launch Checklist bao quát Support, Growth & Data, Marketing, Enterprise, Platform, Security & Privacy.

---

## 4. Cách viết Success Metrics trong PRD (định lượng, baseline, target)

Từ nguồn trực tiếp:
- Atlassian: ví dụ cụ thể nêu trong trang — mục tiêu dạng "tăng điểm hài lòng khách hàng 15%" (một con số % thay đổi, ngụ ý cần biết baseline hiện tại để tính % tăng).
- Kevin Yien/Square: phân biệt rõ 2 loại — "measurable (metrics)" và "immeasurable (feelings) goals" — tức PRD chấp nhận cả mục tiêu định tính (cảm nhận) miễn phân loại rõ ràng, không lẫn lộn với mục tiêu đo được.
- Aha!: Performance = "metrics for success để đo lường giá trị" (không chi tiết công thức).

Khuôn mẫu suy ra để viết success metric tốt (kết hợp 3 nguồn trên, phần công thức baseline/target là tổng hợp thực hành phổ biến — đánh dấu **(suy luận, không có trong nguồn)** vì không nguồn nào nêu công thức chi tiết "baseline → target → deadline"):
- Tên metric + baseline hiện tại + target mong muốn + thời hạn đo. Ví dụ: "Tỷ lệ hoàn tất onboarding trong 24h: baseline 42% (tháng 8/2026) → target 60% trong 6 tuần sau launch."

Câu mẫu tốt: "Giảm thời gian trung bình để mời xong 1 team từ 8 phút (hiện tại, đo qua Mixpanel) xuống dưới 2 phút, đo trong 30 ngày đầu sau launch."
Câu mẫu tệ: "Tăng sự hài lòng của người dùng."

---

## 5. Cách viết Out of Scope / Non-Goals và vì sao quan trọng

Nguồn trực tiếp:
- Atlassian: mục Out of Scope yêu cầu liệt kê cụ thể "what's out of scope for this feature or release" — không giải thích lý do "vì sao quan trọng" trong đoạn đọc được.
- Kevin Yien/Square (nguyên văn): "List explicit areas we do not plan to address" và "Explain why they are not goals" — Non-Goals "are as important and clarifying as the goals" (quan trọng và làm rõ ngang với goals). Đây là câu trả lời trực tiếp nhất về "vì sao quan trọng": Non-Goals giúp làm rõ ranh giới ngang mức với Goals, tránh hiểu lầm rằng "không nói tới nghĩa là sẽ làm".
- Aha!: Scope định nghĩa là "điều gì không được bao gồm trong bản phát hành này".

Cách viết: liệt kê từng mục out-of-scope kèm lý do (theo yêu cầu nguyên văn của Square: "Explain why"), không chỉ liệt kê suông.

Câu mẫu tốt: "Không hỗ trợ import từ Google Sheets trong bản này — vì <5% khách hàng khảo sát dùng Sheets làm nguồn danh sách mời; sẽ xét lại ở Q1/2027 nếu nhu cầu tăng."
Câu mẫu tệ: "Không làm tích hợp Google Sheets."

Vì sao chống scope creep (suy luận trực tiếp từ câu trích Square ở trên): khi Non-Goals được viết tường minh và có lý do, mọi yêu cầu bổ sung giữa chừng phải được so chiếu lại với lý do đã ghi — nếu ai đó muốn thêm tính năng đã bị liệt là non-goal, họ phải phản biện lại lý do cũ thay vì âm thầm mở rộng phạm vi.

---

## 6. Amazon Working Backwards / PR-FAQ

Nguồn: Ian McAllister, LinkedIn — "Working Backwards Press Release Template & Example" (https://www.lennysnewsletter.com/p/my-favorite-templates-issue-37 dẫn tới https://www.linkedin.com/pulse/working-backwards-press-release-template-example-ian-mcallister/).

Cấu trúc Press Release (PR) trong PR-FAQ:
1. **Title & Subtitle**: dạng "[COMPANY] ANNOUNCES [SERVICE|TECHNOLOGY|TOOL] TO ENABLE [CUSTOMER SEGMENT] TO [BENEFIT]", subtitle diễn giải lại thông báo.
2. **Date and Location**: [Thành phố, Bang]–[Ngày dự kiến ra mắt].
3. **Problem**: tối đa 3-4 pain point của khách hàng, xếp theo mức độ nghiêm trọng, KHÔNG nhắc tới giải pháp ở đây.
4. **Solution**: mô tả sản phẩm giải quyết từng vấn đề ra sao, kèm tổng quan cách triển khai.
5. **Executive Quote**: lãnh đạo giải thích vì sao công ty giải quyết vấn đề này và giải pháp hoạt động ở tầm cao ra sao.
6. **Product Details**: khách hàng cần làm gì để tiếp cận dịch vụ, sản phẩm vận hành thế nào trong thực tế.
7. **Customer Quote**: lời chứng thực từ khách hàng — "giả định nhưng thực tế" (fictional but realistic).
8. **Call-to-Action**: URL hoặc thông tin để bắt đầu dùng.
9. Kết thúc bằng ký hiệu "# # #" đánh dấu hết thông cáo báo chí.
Ghi chú thêm từ tác giả: đặt ngày ra mắt cụ thể có thể khiến lãnh đạo hiểu nhầm là mốc ship thật — cần chọn ngày mang tính thực tế.

**Khác biệt so với PRD truyền thống** (đối chiếu cấu trúc trên với các PRD mục 2-3 ở trên; đây là suy luận từ so sánh cấu trúc, không phải câu trích trực tiếp nói "khác PRD ở điểm nào"):
- PR-FAQ viết bằng giọng văn thông cáo báo chí hướng tới khách hàng cuối, PRD viết bằng giọng nội bộ hướng tới team build (requirements, flows, milestones).
- PR-FAQ bắt đầu từ "trải nghiệm khách hàng đã hoàn thành" (viết như sản phẩm đã ra mắt) rồi làm ngược lại yêu cầu kỹ thuật — PRD bắt đầu từ vấn đề/Objective rồi đi tới requirements cụ thể, mốc launch.
- PR-FAQ không có mục Key Features/Requirements dạng bảng, không có Success Metrics dạng bảng như PRD Atlassian/Square/Aha!.
- (Lưu ý: bài chỉ mô tả phần Press Release; phần "FAQ" đi kèm PR-FAQ đầy đủ — nội dung "FAQ" là gì — KHÔNG được đọc thấy chi tiết trong đoạn trích WebFetch trả về; không bịa thêm nội dung FAQ.)

---

## 7. PRD Template tiếng Việt hoàn chỉnh (copy dùng ngay)

Tổng hợp bộ khung tối thiểu (mục 2) + các mục hay của Square/Figma (Non-Goals, Key Flows, Launch Milestones).

```markdown
# PRD: [Tên tính năng/sản phẩm]

## 0. Thông tin chung
| Trường | Giá trị |
|---|---|
| Trạng thái | Draft / In Review / Approved |
| Tác giả (PM) | |
| Ngày cập nhật | |
| Kỹ sư phụ trách | |
| Thiết kế phụ trách | |
<!-- Hướng dẫn: điền vai trò để mọi người biết hỏi ai. Nguồn: Atlassian "PRD Basics and Team Roles". -->

## 1. Vấn đề (Objective / The Problem)
[Mô tả vấn đề trong 1-2 câu, kèm bằng chứng số liệu.]
<!-- Hướng dẫn: 1-2 câu, có bằng chứng vì sao quan trọng với khách hàng và doanh nghiệp. Nguồn: Kevin Yien/Square, Figma. -->

## 2. Bối cảnh (Context)
- Đối tượng người dùng (persona):
- Kịch bản sử dụng chính (user scenario):
<!-- Hướng dẫn: mô tả ai gặp vấn đề, trong tình huống nào. Nguồn: Product School (Personas, User Scenarios), Aha! (Context). -->

## 3. Mục tiêu & Success Metrics
| Metric | Baseline | Target | Thời hạn đo |
|---|---|---|---|
| | | | |
<!-- Hướng dẫn: mỗi metric có baseline + target + deadline, tránh mục tiêu mơ hồ. Nguồn: Atlassian, Kevin Yien/Square, Aha!. -->

## 4. Giả định (Assumptions)
- [Giả định về người dùng/kỹ thuật/kinh doanh]
<!-- Hướng dẫn: ghi rõ điều gì đang được coi là đúng mà chưa kiểm chứng. Nguồn: Atlassian. -->

## 5. Phạm vi & Non-Goals (Out of Scope)
| Không làm | Lý do |
|---|---|
| | |
<!-- Hướng dẫn: liệt kê + giải thích lý do, không chỉ liệt kê suông. Nguồn nguyên văn Kevin Yien/Square: "List explicit areas we do not plan to address" + "Explain why they are not goals". -->

## 6. Yêu cầu / Tính năng chính (Key Features / Requirements)
| Requirement | User story | Ưu tiên (Must/Should/Could) | Ghi chú |
|---|---|---|---|
| | | | |
<!-- Hướng dẫn: mỗi dòng gắn với 1 user story cụ thể. Nguồn: Atlassian (Options table), Product School, Kevin Yien/Square (Key Features). -->

## 7. Luồng chính (Key Flows) & Tài liệu hỗ trợ
[Link mockup/wireframe/diagram cho luồng chính + 1-2 luồng biên]
<!-- Hướng dẫn: đủ để người đọc hình dung trải nghiệm end-to-end. Nguồn: Atlassian (Supporting Documentation), Kevin Yien/Square & Figma (Key Flows). -->

## 8. Kế hoạch ra mắt (Launch Plan / Key Milestones)
| Giai đoạn | Mục đích | Tiêu chí chuyển giai đoạn | Thời gian |
|---|---|---|---|
| Dogfood/Pilot | | | |
| Beta | | | |
| Launch | | | |
<!-- Hướng dẫn: Nguồn: Kevin Yien/Square (Launch Plan, Key Milestones), Figma (Key Milestones, Launch Checklist), Product School (Timeline/Release Planning). -->

## 9. Câu hỏi mở (Open Questions)
| Câu hỏi | Người phụ trách | Hạn trả lời | Trạng thái |
|---|---|---|---|
| | | | |
<!-- Hướng dẫn: theo dõi để không rơi vào quên lãng. Nguồn: Atlassian, Product School, Kevin Yien/Square (Appendix). -->

## 10. Phụ lục (Changelog, FAQ)
- Changelog: [ngày — thay đổi — người sửa]
- FAQ: [nếu có]
<!-- Hướng dẫn tuỳ chọn. Nguồn: Kevin Yien/Square (Appendix: Changelog, FAQs). -->
```

---

## 8. Sai lầm thường gặp khi viết PRD

Nguồn: Product School (Common Mistakes, 4 điểm nêu trong bài):
1. Viết PRD chỉ để "hoàn thành nhiệm vụ" (viết cho có, không dùng thật).
2. Không lấy ý kiến từ stakeholders trước khi chốt.
3. Mất cân bằng giữa yêu cầu kỹ thuật và nhu cầu khách hàng.
4. Thiếu mục tiêu rõ ràng.

Bổ sung từ Square/Kevin Yien (suy luận từ cách template nhấn mạnh, không phải liệt kê "common mistakes" trực tiếp): không viết Non-Goals rõ ràng dẫn tới hiểu lầm phạm vi — Non-Goals "quan trọng ngang goals" theo nguyên văn, ngụ ý bỏ qua mục này là một lỗi phổ biến trong thực hành PM dù bài không liệt kê thành danh sách lỗi tường minh.

Best Practices đối lập (Product School, nguyên văn ý): PRD là "living document" cần cập nhật liên tục; chấp nhận TBD/placeholder ở bản nháp; cân bằng giữa chính xác và súc tích; là sản phẩm của teamwork; là công cụ giao tiếp.

---

## 9. Ghi chú về nguồn không mở được / mở được nhưng hạn chế

- https://www.aha.io/roadmapping/guide/templates (URL đề bài chỉ định): mở được nhưng KHÔNG có mô tả cấu trúc PRD cụ thể — chỉ liệt kê "Product requirements document (PRD) templates" và "Market requirements document (MRD) templates" dưới dạng link, không mô tả nội dung bên trong, không giải thích khác biệt PRD/MRD. Để đáp ứng yêu cầu đề bài (giải thích từng mục, PRD vs MRD), báo cáo đã mở thêm 2 trang con của Aha! (what-is-a-good-product-requirements-document-template và templates/create/prd) — cả hai đọc được đầy đủ, nhưng KHÔNG khớp nhau về danh sách mục (xem ghi chú ở cuối mục 2).
- Product School: đã xác nhận bài viết liệt kê **14 mục** (Title, Change History, Overview, Success Metrics, Messaging, Timeline/Release Planning, Personas, User Scenarios, User Stories/Features/Requirements, Features Out, Designs, Open Issues, Q&A, Other Considerations) — KHÔNG phải "13 thành phần" như nhận định trước đó bị bác bỏ; đã tự đọc lại và ghi đúng số 14 kèm danh sách nguyên văn.
- hellopm.co: bài liệt kê link tới ProductHunt/AirPods/Airbnb PRD examples nhưng KHÔNG ghi rõ các ví dụ này là chính thức hay tái dựng lại — bản thân trang hellopm không làm rõ. (Không tự suy đoán thay nguồn.)
- Kevin Yien/Square PRD: đọc được đầy đủ qua export text của Google Doc (không phải trang HTML preview vốn không tải được nội dung).
- Figma PRD (Coda): URL gốc redirect sang docs.superhuman.com — đã đọc được nội dung tại URL redirect.
- Amazon PR-FAQ (LinkedIn, Ian McAllister): đọc được phần Press Release đầy đủ; phần "FAQ" đi kèm mô hình PR-FAQ không thấy nội dung chi tiết trong đoạn WebFetch trả về — không bịa thêm.

---

## Câu hỏi chưa giải quyết

1. Aha! có hai mô tả PRD khác nhau ở hai trang (8 mục kiểu Objective/Context/Scope... vs 4 cấp Product/Release/Epic/Feature requirements) — chưa rõ trang nào là "PRD template chính thức hiện hành" của Aha!, cần người dùng xác nhận nếu cần trích dẫn chính xác.
2. Nội dung phần "FAQ" trong mô hình PR-FAQ của Amazon (câu hỏi nội bộ + câu hỏi khách hàng thường đi kèm) chưa đọc được chi tiết từ nguồn LinkedIn đã fetch — nếu cần đầy đủ, nên mở thêm nguồn khác (vd. bài gốc của Ian McAllister trên Medium/trang cá nhân) để bổ sung.
3. hellopm.co không xác nhận tính chính thức của ví dụ ProductHunt/AirPods/Airbnb — nếu tài liệu tổng hợp muốn dùng các ví dụ này, nên ghi rõ "minh hoạ tái dựng, không phải PRD gốc của công ty" khi trích dẫn.
