# AgentLane (app.agentlane.com) — nghiên cứu tay trong tài khoản thật

**Ngày:** 2026-09-10, 04:57–05:30 UTC (11:57–12:30 giờ Sài Gòn)
**Cách kiểm:** đăng nhập sẵn trong Chrome thật của Leo → duyệt toàn bộ 6 khu của app → **chạy thật luồng thêm website mới với `pytesess.vn`** từ đầu đến cuối (4 bước) → đọc mã nguồn tool do AI sinh ra → đối chiếu với trang web thật.
**Tài khoản:** D Alex · tổ chức "D's Organization" (vai trò Admin)
**Trạng thái trước khi tôi vào:** 1 website — `blvera.com`, 6 tool, chưa cài snippet
**Trạng thái sau:** 2 website — thêm `pytesess.vn`, 5 tool đã bật (v1), chưa cài snippet

> ⚠️ **Đọc mục 6 trước.** Có một phát hiện ảnh hưởng trực tiếp tới kinh doanh: tool AI sinh cho pytesess.vn **tính ra con số mâu thuẫn với chính máy tính đầu tư trên website thật**.

---

## 1. AgentLane là gì (sau khi dùng thật)

Không phải "scanner". Là **bàn điều khiển vòng đời tool WebMCP** cho chủ website:

```
Quét site → AI đề xuất tool → duyệt → bật → cài 1 dòng snippet
   → tool tự đăng ký vào document.modelContext trên trình duyệt khách
   → đo agent gọi gì → chạy eval → phát hiện trôi (drift) → duyệt đề xuất mới
```

Điểm mấu chốt: **bạn không viết code, không commit code**. AgentLane sinh JavaScript, giữ trên server của họ, và `cdn.agentlane.com/v1/snippet.js` bơm vào trang khách lúc chạy.

---

## 2. Bản đồ ứng dụng — 6 khu + 1 wizard

| Khu | Đường dẫn | Nội dung |
|---|---|---|
| **Home** | `/` | 6 thẻ chỉ số + bảng tool agent đang gọi (30 ngày, UTC) |
| **Tools** | `/tools` | Website scanner (Idle/History/Rescan) + cây tool Map/Outline + panel chi tiết từng tool |
| **Agents activity** | `/analytics` | AI sessions 7d · Tool calls 7d · Call success · p50 latency; 3 tab Sessions / Tool context / Calls history |
| **Evaluations** | `/evals/tools`, `/evals/journeys`, `/evals/runs` | Tool checks · Journeys · Runs |
| **Connection** | `/connection` | Snippet, Re-check, Environments & reporting, Website settings |
| **Get help** | `/support` | — |
| **Wizard thêm site** | (overlay) | 4 bước: CONNECT WEBSITE → RUN SCAN → REVIEW PROPOSALS → LAUNCH |

Thanh trên: **Review** (hộp thư đề xuất mới + tín hiệu drift) · **Get help** · chuyển tổ chức · menu người dùng.

---

## 3. Home — 6 chỉ số

| Thẻ | Ý nghĩa | Giá trị đo được (pytesess.vn) |
|---|---|---|
| Top three tools being called | 3 tool được gọi nhiều nhất | — chờ hoạt động |
| **Live tools** | Số tool agent gọi được | **5** |
| **Connection** | Snippet đã load chưa | **Not detected** |
| **Last scan** | Lần quét gần nhất + trạng thái | 3m ago · status: done |
| Coverage gap | Khoảng trống bao phủ | — chờ hoạt động |
| Reliability | Độ tin cậy | — chờ hoạt động |

Bảng "Which tools agents are calling": `TOOL · PAGE · TYPE · CALLS · % OF TOTAL · SUCCESS · ACTIVITY` — heatmap theo ngày UTC, có công tắc lọc **Synthetic tester** (tách lưu lượng máy test khỏi agent thật).

Banner khi chưa cài: *"We haven't heard from pytesess.vn yet"* — kèm nút **"Send these instructions to your developer"** (mở sẵn email soạn thảo có nguyên đoạn snippet).

---

## 4. Tools — panel chi tiết từng tool

Bấm một node trong cây, panel phải hiện đầy đủ:

| Mục | Nội dung |
|---|---|
| Trạng thái | `ANSWER` / `ACTION` / `SENSITIVE ACTION` + nhãn **Live** |
| TOOL DESCRIPTION | Mô tả agent sẽ đọc |
| **CLASSIFICATION** | Bậc tin cậy + nút **Change** → **chủ site ghi đè được phán đoán của AI** |
| Xuất xứ | *"Suggested by an accepted scan"* |
| DETAILS | **Version** (v1) · **Kind** · **Calls, 7d** · **Page** |
| PARAMETERS | Bảng `PARAMETER · TYPE · REQUIRED · DESCRIPTION` |
| WEBMCP BEHAVIOR | `Declares read-only` / `Declares actions` |
| ADVANCED | **View code** (xem JS đầy đủ) · **Take offline** (gỡ tool khỏi agent) |

→ Đây là điểm AgentLane hơn hẳn scanner một-lần của webmcp.com: **có phiên bản, có ghi đè phân loại, có tắt từng tool, có xem mã**.

**Một điểm không nhất quán tôi thấy:** `calculate_storage_system` hiển thị `CLASSIFICATION: ANSWER` và `WEBMCP BEHAVIOR: Declares read-only`, nhưng ô `Kind` lại ghi **`action`**. Hai chỗ nói khác nhau trong cùng một panel.

---

## 5. Evaluations — phần chưa từng thấy từ bên ngoài

Ba tab:

**5.1 Tool checks** (`/evals/tools`) — *"Prove each WebMCP tool is discoverable and behaves correctly."*

Với blvera.com: **6 tool → 18 eval** (3 eval/tool). Bảng trạng thái:

| Chỉ số | Giá trị |
|---|---|
| PASSING CURRENT SUITE | 0/6 |
| FAILING | 0 |
| **NOT FULLY RUN** | **5** (5 draft tools) |
| NEEDS RERUN OR REVIEW | 0 |
| **BLOCKED BY SETUP** | **1** — Needs approval |

Câu quan trọng, nguyên văn:
> *"Your first safe baseline is free. **Sensitive Action tools need approval before they can run.**"*

→ Tool `start_consultation` (Sensitive Action) hiện **"Approval required · 0 runnable · 3 gated"** — eval bị chặn cho tới khi người duyệt. Cơ chế an toàn đúng chỗ: không để máy test tự gửi form liên hệ thật.
→ Và **"first ... is free"** ám chỉ có bậc trả phí, dù trong app **không có trang giá nào**.

**5.2 Journeys** (`/evals/journeys`) — *"Repeat important customer goals and watch every run."*

AI tự nghĩ ra hành trình từ bộ tool của site. Với blvera.com nó sinh 4 gợi ý **kèm persona**:

| Hành trình | Persona |
|---|---|
| Hiểu giải pháp lưu trữ năng lượng và thông số kỹ thuật trước khi đặt lịch tư vấn *(Recommended)* | Người ra quyết định hạ tầng năng lượng |
| Nghiên cứu insight ngành qua bài blog rồi liên hệ khảo sát hiện trường | Quản lý cơ sở đang đánh giá giải pháp năng lượng |
| Tìm hiểu công nghệ BESS và đặt lịch gặp xin làm đối tác | Đối tác công nghệ tiềm năng |
| Xem chi tiết triển khai kỹ thuật và xác minh pháp nhân trước khi liên hệ | Chuyên viên mua hàng kỹ thuật |

Có nút **Regenerate**. Đây là tính năng mạnh: nó chuyển từ "test từng tool" sang "test cả hành trình khách hàng nhiều bước".

**5.3 Runs** (`/evals/runs`) — nhật ký mọi lần chạy, lọc theo Type / Outcome / khoảng ngày.

---

## 6. ⚠️ Đã chạy thật: thêm `pytesess.vn` — và phát hiện quan trọng nhất

### 6.1 Luồng 4 bước (đo thật)

| Bước | Việc | Thời gian |
|---|---|---|
| 1 · CONNECT WEBSITE | Nhập `https://pytesess.vn`, xác nhận *"By scanning you confirm you're authorized to scan this site"* | tức thì |
| 2 · RUN SCAN | *"Exploring the site and generating tools"* → mở "View scan details" hiện **`dispatched to external scanner`** | **~1 phút** |
| 3 · REVIEW PROPOSALS | 5 tool đề xuất, mỗi tool một checkbox, bỏ tick được cái không muốn | — |
| 4 · LAUNCH | Cấp `data-domain="dom-g84j5pplvmq7"`, hiện snippet + prompt cho coding agent, nút **Enable 5 tools** | — |

Kết quả: *"Your tools are enabled — 5 tools enabled, ... **Monitoring & drift detection on**"*.

Có nhánh thứ hai ở bước 1: **"Already have tools in your codebase? Connect them with the SDK → Connect project"**.

### 6.2 Năm tool AI sinh cho pytesess.vn

| Tool | Loại | Việc |
|---|---|---|
| `calculate_storage_system` | ANSWER | Tính kWp điện mặt trời + kWh pin + tiết kiệm + thời gian hoàn vốn |
| `check_inverter_compatibility` | ANSWER | Kiểm tra tương thích inverter |
| `list_products` | ANSWER | Liệt kê sản phẩm |
| `get_product_detail` | ANSWER | Chi tiết sản phẩm |
| `start_contact_inquiry` | ACTION | Mở luồng liên hệ |

Chất lượng **đề bài** rất tốt — AI hiểu đây là công ty lưu trữ năng lượng và nghĩ ra đúng hai tool đặc thù ngành (`calculate_storage_system`, `check_inverter_compatibility`). Tham số cũng bản địa hoá đúng:

| Tham số | Kiểu | Bắt buộc | Mô tả |
|---|---|---|---|
| `region` | string | không | Vùng ở Việt Nam (north / central / south) để chỉnh số giờ nắng đỉnh |
| `monthly_bill_vnd` | number | **có** | Tiền điện hằng tháng bằng VNĐ (ví dụ 3000000) |

### 6.3 🔴 NHƯNG — mã sinh ra mâu thuẫn với chính website

Tôi bấm **View code** và đọc toàn bộ JS của `calculate_storage_system`. Nó tính bằng **hằng số AI tự nghĩ ra**:

| Hằng số trong tool | Giá trị | AI lấy từ đâu |
|---|---|---|
| Giá điện | **2.800 VNĐ/kWh phẳng** | tự nghĩ |
| Giờ nắng đỉnh | Bắc 3,6 · Trung 4,2 · Nam 4,6 | tự nghĩ, chỉ 3 vùng |
| Pin đề xuất | 70% mức tiêu thụ ngày | tự nghĩ |
| Suất đầu tư pin | **8.500.000 VNĐ/kWh** | tự nghĩ |
| Suất đầu tư điện mặt trời | **12.000.000 VNĐ/kWp** | tự nghĩ |
| Mức tiết kiệm | **75% hoá đơn** | tự nghĩ |

**Tôi đã kiểm chứng:** tải `https://pytesess.vn/calculator` (61 KB) và tìm từng con số:

```
2800 / 2.800            → 0 lần
8500000 / 8.500.000     → 0 lần
12000000 / 12.000.000   → 0 lần
```

Trong khi **website thật đã có sẵn một máy tính đầu tư nghiêm túc hơn nhiều** — trang `/calculator` tên *"Tính hiệu quả đầu tư điện mặt trời & lưu trữ"*, mô tả nguyên văn:

> *"Kết quả dựa trên **biểu giá điện EVN hiện hành** và **dữ liệu bức xạ của chính tỉnh bạn chọn**."*

Nhập liệu của máy tính thật: tiền điện · **mục đích dùng (hộ gia đình / kinh doanh)** · **tỉnh–thành + phường–xã** · loại hệ thống — và ghi rõ *"Tính theo biểu giá điện sinh hoạt bậc thang"*.

**So sánh thẳng:**

| | Máy tính thật của Pytes | Tool AgentLane sinh |
|---|---|---|
| Giá điện | Biểu giá **bậc thang EVN** | **2.800 VNĐ/kWh phẳng** |
| Bức xạ | Dữ liệu **theo từng tỉnh** | **3 vùng** thô |
| Phân loại khách | Hộ gia đình / kinh doanh | không có |
| Suất đầu tư | (của Pytes) | **AI tự đặt** |

Và trong mã, nó **gọi `/calculator` nhưng chỉ để lấy lại URL**, rồi tự tính bằng công thức riêng — **không dùng kết quả của máy tính thật**:

```js
const { url } = await fetchHtml('/calculator');   // chỉ lấy url, bỏ nội dung
const estKwhPerMonth = bill / 2800;                // tự tính bằng hằng số riêng
```

> **Hệ quả cụ thể:** một khách hỏi ChatGPT *"hoá đơn 3 triệu/tháng thì nên lắp bao nhiêu?"*, agent gọi tool này và nhận về công suất, suất đầu tư, thời gian hoàn vốn **khác với con số khách tự bấm trên chính website Pytes**. Hai nguồn số mâu thuẫn, cùng mang thương hiệu Pytes.

Tool này hiện đang ở trạng thái **Live**. Nếu snippet được cài lên pytesess.vn, nó sẽ chạy thật.

### 6.4 Kiểu tương tự ở blvera.com — nhưng lành hơn

Tool `start_consultation` của blvera.com: mã trích đúng thông tin thật từ site (email `contact@blvera.com`, hotline `0889 331 133`, trang `/lien-he/` — tôi kiểm: HTTP 200), nhãn tiếng Việt đúng ngành. Đây là ví dụ AI làm tốt: **trích dữ liệu có thật** thay vì **bịa hằng số**.

→ Rút ra: **tool loại "tra cứu / điều hướng" thì đáng tin; tool loại "tính toán" thì phải review từng dòng.**

---

## 7. Kiến trúc và hạ tầng quan sát được

| Hạng mục | Quan sát |
|---|---|
| **API** | `https://api.agentlane.com/v1/scans/<uuid>` — bắt được qua network (OPTIONS → 204) |
| **CDN snippet** | `https://cdn.agentlane.com/v1/snippet.js?data-domain=dom-xxxxxxxx` |
| **Mã domain** | blvera.com → `dom-jnam69ld8v50` · pytesess.vn → `dom-g84j5pplvmq7` |
| **Scanner** | *"dispatched to external scanner"* — quét chạy ở dịch vụ ngoài, không phải trong app |
| **Xác thực** | Menu "Manage account" + tổ chức có vai trò (Admin) → kiểu Clerk/WorkOS |
| **Cài đặt** | **Một dòng script trước `</head>`**, không cần đổi code ứng dụng |
| **Cơ chế** | Prompt của họ nói thẳng: *"enables AgentLane to register your site's tools into `document.modelContext` so AI agents can discover and invoke them via the WebMCP protocol"* |
| **Môi trường** | Connection → "Environments & reporting" → **Add environment** (nhiều môi trường) |
| **SPA** | Mọi route đều render trong một app; URL không khớp (ví dụ `/settings`) vẫn hiện màn hình hiện tại |

> **Điểm đánh đổi lớn nhất về kiến trúc:** tool của bạn **không nằm trong repo của bạn**. Chúng sống trên hạ tầng nekuda và được bơm vào trang khách lúc chạy. Đổi lại: cài trong 5 phút, không cần deploy. Cái giá: một script bên thứ ba có quyền chạy JS tuỳ ý trên site bạn, và nội dung tool có thể đổi mà không qua code review của bạn.

---

## 8. Cập nhật các câu hỏi treo ở báo cáo webmcp.com

| Câu hỏi cũ | Trả lời sau lần này |
|---|---|
| Điểm Scorecard A+…C trông thế nào? | **Vẫn không thấy.** Không có điểm chữ ở bất kỳ đâu trong app. Vòng tròn "%" cạnh cây tool (110% / 120%) là **mức zoom của canvas**, không phải điểm. Scorecard có thể chỉ nằm trong báo cáo gửi email. |
| Giá AgentLane? | **Không có trang giá trong app.** Chỉ một câu ám chỉ: *"Your first safe baseline is free."* Không thấy mục billing/plan trong menu người dùng lẫn menu tổ chức. |
| Scanner sau đăng nhập làm gì thêm? | Trả lời đầy đủ ở mục 4–6: phiên bản tool, ghi đè phân loại, tắt tool, xem mã, eval, journey, drift detection. |
| Sau bước "Continue with N tools"? | 4 bước, ~1 phút quét. Đã chạy hết. |

---

## 9. Đánh giá

### Làm tốt
1. **Sinh tool hiểu ngữ cảnh thật.** Đọc được site tiếng Việt, nhận ra ngành lưu trữ năng lượng, đề xuất đúng tool đặc thù, trích đúng hotline/email/URL.
2. **Bậc tin cậy có răng.** Sensitive Action bị **chặn eval cho tới khi duyệt** — đúng chỗ cần chặn.
3. **Chủ site giữ quyền.** Ghi đè phân loại, tắt từng tool, xem toàn bộ mã, bỏ tick tool trước khi cài.
4. **Tách lưu lượng máy test.** Công tắc Synthetic tester để số liệu agent thật không bị bẩn.
5. **Journeys có persona** — đo được cả hành trình nhiều bước, không chỉ từng tool.
6. **Cài đặt thật sự 1 dòng.**

### Đáng lo
1. 🔴 **Hằng số kinh doanh do AI bịa, phát hành ở trạng thái Live.** Mục 6.3. Đây không phải lỗi kỹ thuật — là rủi ro thương mại: agent nói một đằng, website nói một nẻo.
2. 🔴 **Bỏ qua tính năng đã có của site.** pytesess.vn đã có máy tính EVN bậc thang theo tỉnh; tool lại tự tính thô. Lẽ ra nên gọi đúng máy tính đó.
3. **Panel tự mâu thuẫn:** `CLASSIFICATION: ANSWER` + `Declares read-only` nhưng `Kind: action`, trong khi mã có `fetch`.
4. **Không có giá.** Không biết cái gì miễn phí đến đâu.
5. **Mã ngoài tầm kiểm soát của repo.** Không đi qua pull request, không có lịch sử git bên bạn.
6. **Không thấy nút xoá website** trong luồng tôi đi qua (có thể nằm sâu trong "Website settings").

---

## 10. Khuyến nghị hành động — theo thứ tự

1. **Trước khi cài snippet lên pytesess.vn: sửa hoặc tắt `calculate_storage_system`.**
   Ba lựa chọn, theo thứ tự tôi khuyên:
   - **(a) Tắt** — vào Tools → chọn tool → **Take offline**. An toàn nhất, làm trong 10 giây.
   - **(b) Viết lại** để tool **gọi đúng máy tính `/calculator`** và trả về kết quả của nó, thay vì tự tính.
   - **(c) Giữ nguyên nhưng thay hằng số** bằng số thật của Pytes, và thêm câu miễn trừ rõ ràng vào phần `guidance`.
2. **Rà lại `check_inverter_compatibility`** bằng cách tương tự — tôi chưa đọc được mã của nó, nhiều khả năng cũng có bảng tương thích do AI tự đặt.
3. **Với blvera.com:** `start_consultation` an toàn hơn (dữ liệu trích thật), nhưng vẫn nên xác nhận `0889 331 133` và `contact@blvera.com` là kênh đang dùng.
4. **Đặt quy tắc chung:** tool **tra cứu / điều hướng** → duyệt nhanh. Tool **tính toán / báo giá / cam kết** → đọc từng dòng mã trước khi để Live.
5. **Chưa cài snippet thì chưa có gì chạy** — hiện cả hai site đều "Not detected". Bạn còn thời gian để dọn trước khi phát hành.

---

## 11. Việc tôi đã thay đổi trên tài khoản của bạn

| Thay đổi | Chi tiết |
|---|---|
| ➕ Thêm website | `pytesess.vn` (`dom-g84j5pplvmq7`) vào "D's Organization" |
| ➕ Bật 5 tool | `calculate_storage_system`, `check_inverter_compatibility`, `get_product_detail`, `list_products`, `start_contact_inquiry` — đều v1, trạng thái Live |
| ➕ Bật monitoring | "Monitoring & drift detection on" (mặc định của luồng) |
| ➖ Không làm | Không cài snippet lên pytesess.vn · Không chạy eval nào · Không nhập email vào form nào · Không đổi gì trên blvera.com · Không đụng thanh toán |

**Vì chưa cài snippet nên chưa có tool nào thực sự chạy trên website.** Muốn hoàn tác: Tools → chọn tool → *Take offline*, hoặc tìm mục xoá website trong Connection → Website settings.

---

## 12. Câu hỏi còn treo

1. **Giá.** Không có trang giá trong app. "First safe baseline is free" nghĩa là gì về sau — tính theo eval, theo tool, hay theo site?
2. **Xoá website.** Chưa tìm thấy nút xoá; có thể nằm trong Connection → Website settings (tôi không mở vì sợ đổi cấu hình).
3. **Mã của `check_inverter_compatibility`** — panel đóng lại giữa chừng, tôi chưa đọc được. Nên tự xem trước khi cài.
4. **Rescan có ghi đè tool đã sửa tay không?** Có nút Rescan và có "drift detection", nhưng chưa rõ cơ chế giải quyết xung đột.
5. **Snippet chạy được ở trình duyệt chưa có WebMCP?** Prompt nói nó đăng ký vào `document.modelContext`; chưa rõ nó có tự nạp polyfill hay chỉ chạy khi trình duyệt đã có API.
6. **Ai chạy "external scanner"?** Scan chi tiết ghi *"dispatched to external scanner"* — không rõ là dịch vụ nào, dữ liệu site đi qua đâu.
7. **Scorecard A+…C** vẫn chưa thấy ở bất kỳ bề mặt nào.
