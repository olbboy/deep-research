# Kiến thức thực chất về Product Roadmap — tổng hợp từ 3 nguồn miễn phí

Nguồn đã đọc trực tiếp (tải PDF về, extract bằng pdftotext, đọc toàn văn):
1. **[ProductPlan]** Jim Semick, "Product Roadmaps: Your Guide to Planning and Selling Your Strategy" (2016) — https://assets.productplan.com/content/Product-Roadmap-Guide-by-ProductPlan.pdf — đọc toàn bộ 68 trang.
2. **[Tempo/Roadmunk]** "The Tempo Way" / tên gốc trong file "The Roadmunk Way" (2021) — https://assets.ctfassets.net/99u0kepfatsy/2yrEH1WKZXlYUGdJ3dGtLT/3eb675b824e68ae418f4714ece7977c0/-Tempo-_The_Tempo_Way.pdf — đọc toàn bộ 39 trang.
3. **[ProdPad blog]** "Who invented the Now-Next-Later roadmap?" — https://www.prodpad.com/blog/invented-now-next-later-roadmap/
4. **[ProdPad glossary]** "Now-Next-Later Roadmap" — https://www.prodpad.com/glossary/now-next-later-roadmap/

Ghi chú kỹ thuật: WebFetch không đọc được PDF (binary/FlateDecode) → đã tải file về scratchpad và dùng `pdftotext -layout` để trích văn bản thật, sau đó đọc toàn văn bằng Read. Không đoán nội dung.

---

## 1. Roadmap là gì / không phải là gì

**[ProductPlan]**
> "A roadmap communicates the 'why' behind what you're building. It's a plan for your strategy. A roadmap is a high-level visual summary that maps out the vision and direction of your product, often over time."

Không phải: "A roadmap is not simply a list of features arranged in a somewhat prioritized order, nor is it the product backlog." Roadmap KHÔNG chứa resource requirements, man-hours, story points cụ thể — các chi tiết đó thuộc project management tool, không thuộc roadmap.

Phân biệt rõ trong hình "top-down" (Fig.2): **Product Vision → Product Goals → Product Roadmap → Release Plan & Backlog**. Roadmap là tầng chiến lược, nằm giữa vision/goal (cao nhất) và release plan/backlog (chi tiết thực thi, thấp nhất). "The backlog in itself is not the roadmap." Backlog nói ngôn ngữ feature/task chi tiết; roadmap nói ngôn ngữ epic/theme.

**[Tempo Way]**
> "It's important to remember that a roadmap is not, and should not be, a list of tasks or deliverables. Roadmaps are strategy-focused, not tactic-focused."

Belief cốt lõi: "Your roadmap should be your North Star, **not a release plan**." Sai lầm phổ biến #1 họ liệt kê: "Using Your Roadmap as a Release Plan" — roadmap lý tưởng không chứa chi tiết resource management và ngày ship; nó tập trung vào outcome kinh doanh/người dùng sẽ tạo ra trong một khoảng thời gian.

**Gantt chart**: không nguồn nào định nghĩa Gantt trực tiếp, nhưng ProductPlan mô tả "Timeline-based roadmap" (dạng bar-chart trên lưới thời gian, giống Gantt) và cảnh báo: "a common pitfall for timeline-based roadmaps is to focus on deadlines rather than emphasizing strategic priorities" — tức khi roadmap bị kéo về dạng Gantt/timeline chi tiết, nó mất tính chiến lược. (Phân biệt Gantt vs roadmap cụ thể hơn: suy luận, không có trong nguồn — nguồn chỉ nói timeline roadmap là 1 trong 3 style, không dùng từ "Gantt".)

Bảng so sánh (tổng hợp có trích dẫn):

| | Roadmap | Release plan | Backlog | Timeline/Gantt-style roadmap |
|---|---|---|---|---|
| Nội dung | Theme/epic, chiến lược, "why" | Ngày ship, phân bổ resource, ownership (ProductPlan: "allocate resources... assign ownership... designate release dates") | Feature/task chi tiết, 200+ items (ProductPlan) | Sáng kiến xếp theo trục thời gian, dễ lệch thành cam kết ngày |
| Đối tượng | Toàn tổ chức, exec | Team thực thi, PM | Dev team, sprint | Exec cần trả lời "khi nào xong" |
| Nguồn | ProductPlan Fig.2 | ProductPlan ch.5 "Execution" | ProductPlan ch.2 | ProductPlan ch.4 |

---

## 2. Thành phần bắt buộc của roadmap tốt (theo từng nguồn)

**[ProductPlan]** — mục tiêu roadmap phải đạt (6 gạch đầu dòng, nguyên văn ý):
- Describe vision & strategy
- Guiding document để thực thi chiến lược
- Đưa stakeholder nội bộ vào cùng một hướng (alignment)
- Facilitate thảo luận option/scenario planning
- Communicate progress/status
- Communicate strategy ra ngoài (kể cả khách hàng)

Cố ý KHÔNG bao gồm: resource requirements, man-hours, story points.

**[Tempo Way]** — 5 mục tiêu của "guiding document":
1. Clearly communicate product vision
2. Gain buy-in & alignment từ stakeholder nội bộ
3. Outline kế hoạch thực thi vision
4. Organize resource cần thiết
5. Tie back tới business outcomes của công ty

6 câu hỏi cần trả lời khi build roadmap (Chapter 1, "What Goes Into a Roadmap"):
- Sản phẩm trông như thế nào ở cuối giai đoạn này?
- Vì sao xây cái này quan trọng?
- Sẽ xây như thế nào?
- Cần gì để xây?
- Ngày nào cần đạt?
- Khi nào biết là đã thành công?

→ Điểm chung 2 nguồn: roadmap phải nối được vision ↔ strategy ↔ outcome kinh doanh, và phải là công cụ alignment, không phải danh sách việc.
→ Điểm khác: ProductPlan nhấn use case "getting exec buy-in / selling strategy"; Tempo Way nhấn "consensus giữa mọi stakeholder" + coi PM là "facilitator/conductor" hơn là người quyết một mình.

---

## 3. Khung Now-Next-Later

**Nguồn gốc lịch sử [ProdPad blog]**: sáng tạo bởi **Janna Bastow và Simon Cast, năm 2012**. Tên gốc: **Current / Near Term / Future** (sau đổi thành Now-Next-Later theo gợi ý của một khách hàng sớm — nguồn không nêu tên khách hàng). Lý do ra đời: roadmap theo timeline cố định deadline khiến team bị trói buộc; Bastow cần "something a stakeholder could understand in about ten seconds" — thứ cho thấy priorities mà không giả vờ biết chính xác tuần nào sẽ ship. Nguyên văn:
> "I needed something... that showed what we were working on, what was coming up next, and what we were still thinking about, without pretending I knew the exact week any of it would ship."

**Định nghĩa 3 cột** (gộp cả blog + glossary, có khác biệt nhỏ về cách diễn đạt giữa 2 trang ProdPad — đã ghi rõ):

| Cột | Theo blog (lịch sử) | Theo glossary (định nghĩa hiện hành) |
|---|---|---|
| **Now** | Đang làm chủ động; "clearly defined, fully detailed, and spec'd out", chia nhỏ thành work item cụ thể | "the problem is well understood" — team tập trung solution discovery và đo outcome |
| **Next** | Sau khi Now xong; ít chi tiết hơn, phụ thuộc kết quả của Now | Cơ hội đang được validate qua "customer conversations, problem framing, and early experiments" |
| **Later** | Việc tương lai chưa định hình; "hazy" — vấn đề lớn nhìn thấy ở đường chân trời, giữ trên radar nhưng chưa cần spec | "Strategic bets" — discovery rộng và mang tính khám phá, vấn đề còn đang được định hình |

Tiêu chí đưa item vào từng cột (glossary): dựa trên **mức độ tự tin (confidence)**, không phải ngày tháng — "organizes work by levels of confidence instead of fixed dates."

**Mức chi tiết giảm dần**: nguyên tắc cốt lõi (blog): "Detail decreases over time because 'you can't make decisions far off in the distance... you can't see it clearly yet.'" Càng xa hiện tại, càng ít chi tiết, càng nhiều khám phá.

**Vì sao bỏ ngày tháng cố định** (glossary): "dated columns 'turn every date into a commitment, and when priorities shift, those commitments break.'" → cột theo confidence horizon giữ được sự linh hoạt, tránh promise gãy.

**Outcome-based framing** (glossary, nhấn mạnh): entries nên viết dưới dạng **problem cần giải** chứ không phải feature cần ship — giữ linh hoạt khi ưu tiên đổi, tránh cam kết giải pháp quá sớm.

**Sai lầm thường gặp khi dùng Now-Next-Later** (glossary, nguyên văn ý): coi 3 cột như "Q1, Q2, Q3" (biến tướng lại thành timeline); nhồi feature thay vì problem; nhồi quá tải cột Now; thêm deadline giả tạo phá vỡ tính linh hoạt của khung.

Lưu ý: cả 2 trang ProdPad tự nhận đây là "outcome-focused roadmap" nhưng cách mô tả tiêu chí cột hơi khác nhau (blog thiên về "mức độ đã spec hóa", glossary thiên về "mức độ hiểu vấn đề/confidence") — cả hai không mâu thuẫn nhau, chỉ là 2 góc diễn đạt của cùng nguyên tắc giảm chi tiết theo khoảng cách thời gian.

---

## 4. Roadmap theo outcome vs theo feature

**[Tempo Way]**, belief cốt lõi:
> "Unfortunately, many roadmaps put too much of a focus on the specific features that need to get built as opposed to the outcome it should be producing for the business and its customers. This creates a gap between the product and the reason for the product existing in the first place."

Câu hỏi test roadmap outcome-based: "how is the roadmapped product vision driving us towards our business goals?" — bất kỳ ai trong công ty mở roadmap ra phải trả lời được câu này.

**[ProdPad glossary]**: outcome-based = viết dòng roadmap là **problem to solve**, không phải feature to ship. Ví dụ cách viết dòng roadmap outcome-based (glossary không cho ví dụ cụ thể bằng câu — đây là **suy luận từ định nghĩa, không có câu ví dụ nguyên văn trong nguồn**): thay vì "Xây dashboard báo cáo mới" → viết "Khách hàng doanh nghiệp không tự tra được lịch sử giao dịch → cần giải pháp tự phục vụ" (tên feature để trống, chỉ nêu vấn đề + đối tượng bị ảnh hưởng).

**[ProductPlan]** không dùng thuật ngữ "outcome-based roadmap" nhưng có khái niệm tương đương: **theme**. "Themes should be goal-driven... ideally describe customer value — what customers are going to be receiving or the job that you'll help them accomplish." Ví dụ theme: "Customers Complete First Purchase Faster" — đây là dạng phát biểu theo outcome/value, các feature (Mobile Support, Credit Card API...) là con nằm dưới theme đó. Về bản chất, "theme" của ProductPlan và "problem to solve" của ProdPad là cùng một cơ chế: nhóm feature dưới một mục tiêu customer value, để có thể đổi feature con mà không phá vỡ roadmap tổng.

So sánh nhanh:

| | Feature-based | Outcome-based (ProdPad) / Theme-based (ProductPlan) |
|---|---|---|
| Đơn vị dòng roadmap | Tên feature cụ thể | Vấn đề/mục tiêu khách hàng-kinh doanh |
| Rủi ro | Cam kết giải pháp sớm, vỡ khi đổi hướng | Giữ linh hoạt, dễ đổi giải pháp con |
| Nguồn | (ngầm định, phần đối lập trong cả 2 nguồn) | ProdPad glossary + ProductPlan ch. "Organizing Initiatives Into Themes" |

---

## 5. Quy trình xây roadmap — ProductPlan vs Tempo Way

**[ProductPlan]** — quy trình vòng lặp (Fig.1): **Set Strategic Goals → Gather Initiatives and Organize → Prioritize Initiatives → Roadmap Proposal → Stakeholder Engagement → Roadmap Communication** (rồi lặp lại). Trước đó còn có bước tiền đề: xác định **Product Vision** (top-down: Vision → Goal → Roadmap → Release/Backlog).

Chi tiết theo chương:
1. Tying strategy: viết vision statement (ví dụ IKEA, Google), suy ra product goals đo được (KPI).
2. Planning & prioritizing: thu thập business intelligence từ customer feedback, competitive landscape, sales/CS, analyst research, analytics — rồi nhóm initiative thành **theme**, áp prioritization framework, biết nói "no".
3. Building: chọn 1 trong 3 style (Timeline / Roadmap without Dates / Kanban), áp dụng visual best practice (color, large font, high-level).
4. Communicating: lặp lại theo 4 giai đoạn lifecycle — Planning (roadmap không ngày, nói chuyện với exec) → Prioritization (làm việc với dept heads) → Execution (roadmap chi tiết hơn cho eng) → Release (roadmap cao cấp, không ngày, cho sales/marketing/CS).

**[Tempo Way]** — quy trình 6 bước tuyến tính, đặt tên rõ:
1. Understand Your Role as a PM — PM là facilitator/conductor, không phải người ra mọi quyết định; nhiệm vụ là "welcome and nurture productive debate."
2. Put the Problem First and Solution Last — dùng Geoffrey Moore's product vision template hoặc **The Five Whys** để tránh yêu-giải-pháp-quá-sớm.
3. Gather and Manage Stakeholders — liệt kê stakeholder nội bộ chính và mối quan tâm riêng: CEO ("ảnh hưởng đội khác thế nào"), Sales Exec ("bán được gì cho khách"), Marketing Exec ("khi nào go-to-market"), Product Exec ("lợi thế cạnh tranh từ đâu"). Nói chuyện 1-1 và theo nhóm quanh 3 chủ đề: Company Vision, Understanding of Customers, Priorities.
4. Collect and Prioritize Ideas — 2 pha **Diverge (Create choices) → Converge (Make choices)**; PM tạm gác vai trò gatekeeper ở pha diverge, chỉ nói "no" ở pha converge. Sau đó áp 1 trong 9 prioritization framework (mục 6).
5. Polish and Present the Roadmap — 5 bước: Frame the Big Picture, Mark Milestones/Key Dates, Tell Stories by Pivoting Data (group theo nhiều lát cắt), Leverage Color, Clean Labels. Trước khi present: phải nắm rõ (a) high-level strategy, (b) stakeholders (động cơ, deadline, áp lực), (c) resource constraints. Roadmap trình bày nên đạt tiêu chí: Flexibility (phân biệt planned vs TBD, ví dụ nhãn In Progress/Scheduled/Proposed), Personalization (theo phòng ban/owner), Collaboration (chỉnh sửa live trong buổi họp), Clarity+Attractiveness.
6. Evolve Your Roadmap — coi roadmap là living document; update ngắn hạn 2 tuần/lần (team nhỏ, đào sâu chi tiết), update dài hạn tối thiểu hàng tháng (với senior leader, khớp lại business strategy); 3 input liên tục cần thu thập: Feedback, Progress, Major Changes.

**So sánh 2 quy trình:**

| Điểm | ProductPlan | Tempo Way |
|---|---|---|
| Hình dạng | Vòng lặp 6 khối quanh 1 vòng tròn | Chuỗi tuyến tính 6 bước có thứ tự rõ |
| Điểm bắt đầu | Set Strategic Goals (vision trước) | Understand vai trò PM → rồi problem-first |
| Trọng tâm khác biệt | Nhấn mạnh metrics/KPI ngay từ đầu, nhấn "say no", 3 style trình bày | Nhấn mạnh kỹ thuật khai vấn đề (5 Whys), vai trò facilitator, kỹ thuật diverge/converge, tiêu chí trình bày (flexibility/personalization/collaboration) |
| Điểm chung | Cả hai: (1) chiến lược/vision phải có trước khi liệt kê initiative; (2) roadmap phải là living document, update định kỳ (ProductPlan: tháng/tuần theo khảo sát 2015; Tempo: ngắn hạn 2 tuần, dài hạn tháng); (3) phải nói "no"/converge có chọn lọc; (4) phải tailor theo từng nhóm stakeholder, không dùng 1 bản cho tất cả |

---

## 6. Khung ưu tiên (prioritization frameworks)

**[ProductPlan]** liệt kê 7 "strategies for weighing roadmap initiatives" + giải thích:
- **Value vs. Complexity**: ma trận 2 trục business value / complexity-effort; item value cao, effort thấp = low-hanging fruit. Dùng khi cần cách nhìn nhanh, trực quan.
- **Weighted Scoring**: nâng cấp Value vs Complexity bằng cách gán điểm số cho nhiều category benefit/cost để có kết quả khách quan hơn — dùng khi cần thảo luận có cấu trúc, nhiều tiêu chí.
- **Kano Model**: đánh giá feature theo "customer delight" vs "investment" — 3 loại feature: threshold (phải có), performance (đầu tư tỉ lệ thuận với hài lòng), excitement (đầu tư tạo delight bất ngờ). Dùng khi muốn cân bằng chi tiêu giữa "phải có" và "gây wow".
- **Buy a Feature**: hoạt động group với khách hàng/stakeholder — gán "giá" cho mỗi feature theo effort, phát tiền giả, để người tham gia "mua" feature họ muốn. Dùng khi cần lấy ý kiến ưu tiên từ nhóm đông một cách vui/nhanh.
- **Opportunity Scoring** (từ Outcome-Driven Innovation, gắn với "Jobs to Be Done"): đo điểm Importance (1-10) và Satisfaction hiện tại (1-10) của mỗi outcome; opportunity cao = important cao + satisfaction thấp. Dùng khi có dữ liệu khảo sát khách hàng theo từng job/outcome.
- **Affinity Grouping**: brainstorm trên sticky note → nhóm theo tương đồng → đặt tên nhóm → team vote/rank nhóm. Dùng cho hoạt động nhóm, khởi động ý tưởng.
- **Story Mapping**: tạo story card theo workflow, sắp priority order, kẻ line chia thành release/sprint. Dùng để xác định MVP và scope từng release cho user story.
- Ngoài ra còn nhắc **Buckets of Features**: phân bổ % effort theo nhóm (core enhancement, feature khách yêu cầu, bug fix/UI, feature đột phá, sáng kiến nội bộ) — không phải scoring model mà là cách phân bổ resource theo category.
- Và **T-shirt sizing** (S/M/L hoặc "big/medium/simple") cho ước lượng effort thô ở bước tiền-ưu tiên.

**[Tempo Way]** liệt kê **9 prioritization framework** kèm "khi nào dùng":
| Framework | Khi nào dùng (nguyên văn ý) |
|---|---|
| RICE | Khi lượng hóa được metric theo SMART goal |
| Value vs. Effort | Khi cần framework nhanh, đơn giản để lượng hóa priority |
| Kano Model | Khi có nhiều thời gian thu thập/đánh giá feedback khách hàng |
| Story Mapping | Khi có thể gạt bỏ ý kiến nội bộ để tập trung vào UX |
| MoSCoW Method | Khi làm việc với stakeholder không có nền tảng kỹ thuật |
| Opportunity Scoring | Khi muốn quick-win bằng cách giải quyết nhanh vấn đề khách hàng |
| The Product Tree | Khi tập hợp team cho phiên brainstorm phân kỳ (divergent) |
| Cost of Delay | Khi muốn lượng hóa backlog bằng giá trị tài chính |
| Buy a Feature | Khi muốn hiểu giá trị của feature cụ thể đối với khách hàng |

Tempo Way nói rõ họ chỉ build sẵn 2 framework trong sản phẩm: **RICE và Value vs. Effort**. Nguyên tắc chọn framework (Tempo Way): "The Roadmunk Way... looks to data over anecdotes to drive decisions" — mục đích dùng scoring là để "silence the voice of the loudest person in the room."

Trùng lặp giữa 2 nguồn: Value vs Complexity/Effort, Kano Model, Buy a Feature, Opportunity Scoring, Story Mapping — cả 2 nguồn đều liệt kê. ProductPlan có thêm Weighted Scoring, Affinity Grouping, Buckets of Features (không có trong Tempo Way). Tempo Way có thêm RICE, MoSCoW, The Product Tree, Cost of Delay (không có trong ProductPlan — cuốn ProductPlan xuất bản 2016, RICE/MoSCoW phổ biến hơn sau này).

---

## 7. Trình bày roadmap theo từng nhóm stakeholder

**[ProductPlan]**, theo giai đoạn lifecycle (Planning/Prioritize/Execute/Release) và theo "Know Your Audience":

| Nhóm | Mức chi tiết | Có ngày không | Nội dung/thông điệp |
|---|---|---|---|
| Ban lãnh đạo (exec) | Cao (high-level themes, strategic goals) | Không nên có ngày cụ thể ở giai đoạn planning — dùng "roadmap without dates" | Market space, customer data, ROI tiềm năng; theo "why, how, what" — bắt đầu bằng "why" |
| Kỹ thuật/engineering | Chi tiết, actionable, task/requirement/deadline cụ thể | Có, ở giai đoạn Execution | Cần hiểu big picture để không "stuck in development silo"; nên có custom roadmap riêng, granular hơn |
| Sales/CS/marketing (giai đoạn Release) | Cao-level, loại bỏ ngày cụ thể | Không — "be sure to exclude specific dates when presenting to customer-facing teams" | Positioning sản phẩm mới, cách nó giải quyết vấn đề khách hàng để họ bán/support được |
| Khách hàng/bên ngoài | Rất cao-level | Không, tránh over-committing | Chỉ gồm feature đã approved và gần thành hiện thực; item còn bàn thì để vague hoặc bỏ hẳn |

Nguyên tắc chung ProductPlan: dùng ngôn ngữ phù hợp — non-technical audience thì "layman's terms", tránh jargon/acronym khi roadmap phân phối rộng.

**[Tempo Way]**, khác biệt về stakeholder quan tâm gì (Chapter 3, bước 3):
- CEO: "How will product development affect other teams?"
- Sales Executive: "What will this allow me to offer our customers?"
- Marketing Executive: "When will this feature go to market?"
- Product Executive: "Where is our competitive advantage coming from?"

Sai lầm liệt kê rõ (Tempo Way, Common Mistakes): **"Speaking Only to One Audience"** — dùng 1 bản roadmap cho mọi nhóm là sai; mỗi phòng ban quan tâm khác nhau (ví dụ có nhóm quan tâm scalability/performance hơn nhóm khác) nên phải giải thích riêng initiative đóng góp gì cho business goal theo góc nhìn của họ.

Tiêu chí trình bày chung (Tempo Way, phần "How to Actually Present"): Flexibility, Personalization (theo phòng ban/owner), Collaboration, Clarity+Attractiveness — áp dụng khi build bản trình bày cho từng nhóm.

---

## 8. Sai lầm thường gặp (tổng hợp có nguồn)

**[Tempo Way]** — mục "Common Mistakes" liệt kê trực tiếp:
1. **Using Your Roadmap as a Release Plan** — nhồi chi tiết resource/ngày ship vào roadmap.
2. **Speaking Only to One Audience** — dùng 1 bản cho tất cả stakeholder.
3. **Failing to Quantify the Qualitative** — không biến feedback định tính (khảo sát, phỏng vấn) thành initiative có căn cứ trên roadmap.

**[ProdPad glossary]** — sai lầm khi dùng Now-Next-Later cụ thể:
4. Biến 3 cột thành "Q1, Q2, Q3" (quay lại timeline trá hình).
5. Nhồi feature thay vì problem vào từng cột.
6. Nhồi quá tải cột Now.
7. Thêm deadline giả tạo, phá vỡ tính linh hoạt của khung.

**[ProductPlan]** — sai lầm/pitfall (rải trong chương Communication + Prioritizing):
8. **Attempting to lock in plans too long-term** — khóa cứng deliverable dài hạn trong thị trường agile.
9. **Letting Sales Drive the Conversation** — để sales quyết định roadmap thay vì chiến lược; nguyên văn Matt Feldman: "That's not strategic and it does nothing to help you prioritize."
10. **Engineering Missing the Bigger Picture** — kỹ sư bị bỏ ngoài lề, không hiểu "why".
11. **Oversharing Roadmap Details with Sales or Customers** — hé lộ ngày/feature cho khách quá sớm rồi phải rút lại → mất uy tín.
12. Xây feature dựa hoàn toàn theo yêu cầu khách hàng hiện tại (existing customer base là "skewed set of data") — không nghe cả thị trường/đối thủ.
13. Prioritizing in the moment — xử lý từng request ngẫu hứng, không có framework, 23% PM (khảo sát ProductPlan 2015) coi đây là thách thức #1.
14. Roadmap không visual, để dạng spreadsheet 8-point font/PowerPoint tĩnh — khó update, khó truyền cảm hứng ("Only 13% of B2B PM rất hài lòng với tool họ dùng" — SiriusDecisions 2015, trích trong ProductPlan).

---

## 9. Mẫu roadmap tối giản (Now-Next-Later) — copy dùng ngay

Format dựa trên định nghĩa 3 cột đã kiểm chứng ở mục 3 (ProdPad blog + glossary). Nội dung ví dụ là minh họa cấu trúc, không phải trích nguyên văn từ nguồn.

| | **NOW** (đang làm, đã hiểu rõ vấn đề, chi tiết đầy đủ) | **NEXT** (đang xác thực, ít chi tiết hơn) | **LATER** (bet chiến lược, còn mơ hồ, chỉ để trên radar) |
|---|---|---|---|
| Theme/Problem | Khách hàng SME không tự đối soát được hóa đơn → mất time support | Tệp khách doanh nghiệp lớn cần multi-user permission, chưa rõ mô hình | Mở rộng sang thị trường mới — vấn đề compliance địa phương chưa được frame rõ |
| Trạng thái | Spec'd out, đang build, đo outcome cụ thể (VD: giảm 30% ticket support) | Đang phỏng vấn khách hàng, chạy thử nghiệm nhỏ | Chỉ có giả thuyết, chưa customer conversation |
| Ngày tháng | Không ghi ngày cứng — chỉ ghi "đang làm" | Không ghi ngày | Không ghi ngày |
| Ai xem | Toàn công ty (exec, sales, eng, CS) — bản base | Tuỳ stakeholder, có thể thêm chi tiết riêng cho eng (ProductPlan: "custom roadmaps for technical audiences") | Chỉ nội bộ leadership/strategy |

Quy tắc dùng bảng: mỗi dòng viết theo **problem/outcome**, không viết tên feature cứng (mục 4); khi 1 problem ở Later "đủ hiểu" thì chuyển nó lên Next, không sáng tạo thêm cột theo quý (tránh sai lầm #4 ở mục 8).

---

## Câu hỏi chưa giải quyết

- ProdPad không nêu tên "khách hàng sớm" đã đổi tên Current/Near Term/Future thành Now/Next/Later — nguồn không có, không suy luận thêm.
- Không có case study định lượng (ví dụ % công ty dùng Now-Next-Later thành công) trong 3 nguồn — chỉ có tuyên bố định tính.
- ProductPlan (2016) không có RICE/MoSCoW/Cost of Delay/Product Tree — không rõ có được cập nhật trong version mới hơn của ebook hay không (bản tải về là bản có watermark "2016 ProductPlan").
- Chưa có nguồn nào trong 3 tài liệu này giải thích khác biệt Gantt chart vs roadmap một cách tường minh bằng từ "Gantt" — phần so sánh ở mục 1 dựa trên suy luận từ mô tả "timeline roadmap".
