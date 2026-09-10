# Báo cáo: 15 tên miền `webmcp.<TLD>` — dịch vụ gì, thật hay giả, đã test thử

**Ngày:** 2026-09-10 · **Phạm vi:** `webmcp` trên 15 đuôi: `.com .net .org .ai .dev .me .co .app .xyz .cloud .online .site .info .biz .us`
**Phương pháp:** DNS/WHOIS/RDAP → tải HTML → mở trình duyệt thật → gọi API → chạy thử gói npm → đối chiếu chéo với spec W3C.
**Tất cả số liệu dưới đây đều do tôi tự mở/gọi và kiểm tại thời điểm 2026-09-09 18:50–19:05 UTC.**

---

## 0. Từ điển nhanh (định nghĩa 1 lần, sau đó dùng lời thường)

| Từ | Nghĩa trong báo cáo này |
|---|---|
| **MCP** (Model Context Protocol) | Chuẩn để ứng dụng AI gọi "công cụ" từ server bên ngoài. |
| **WebMCP** | Đưa ý tưởng đó vào *trong trình duyệt*: trang web tự khai báo công cụ (`tool`) cho AI gọi, thay vì AI phải nhìn màn hình đoán nút bấm. |
| **Spec chính thức** | Bản dự thảo W3C Community Group: `github.com/webmachinelearning/webmcp` (3.905 sao, cập nhật 2026-09-04). API là JavaScript: `document.modelContext.registerTool()`. |
| **Origin trial** | Chế độ Chrome cho phép site chạy tính năng thử nghiệm trên người dùng thật trước khi ra mắt chính thức. |
| **Domain parking** | Tên miền đã mua nhưng không có sản phẩm — chỉ hiện trang quảng cáo/rao bán. |

---

## 1. Kết luận 1 dòng

Trong 15 tên miền, **chỉ 3 cái là dịch vụ thật** (`.com`, `.dev`, `.xyz`), **1 cái là mã demo bỏ hoang** (`.org`), **1 cái là ghi chú thử nghiệm 3 chữ** (`.us`), **8 cái là đất trống/rao bán**, **2 cái không phân giải được**. Và trong 3 cái "thật", **chỉ `.com` là sản phẩm nghiêm túc có backend thực**; `.xyz` là vỏ marketing chứa **dữ liệu bịa và tài liệu kỹ thuật sai spec**.

---

## 2. Bảng tổng hợp 15 tên miền

| # | Tên miền | HTTP | Là cái gì | Hạ tầng | Đăng ký | Xếp loại |
|---|---|---|---|---|---|---|
| 1 | **webmcp.com** | 200 | **WebMCP Directory** — danh bạ site có WebMCP + API công khai + benchmark + scanner. Của **nekuda** (nekuda.ai) | Cloudflare | 2020-11-17, GoDaddy, hết hạn 2028 | 🟢 **Sản phẩm thật, đầy đủ** |
| 2 | **webmcp.dev** | 200 | **Thư viện JS gốc** `@jason.today/webmcp` — nguyên mẫu WebMCP đầu tiên (03/2025) của Jason McGhee | GitHub Pages, NS Porkbun | 2025-03-08, Porkbun | 🟢 **Thật, nhưng đã ngừng phát triển** |
| 3 | **webmcp.xyz** | 200 | **"WebMCP Registry"** — danh bạ không chính thức, 11 site, có bán "Featured Listing" | Lovable + Supabase | 2026-02-10, NameCheap | 🟡 **Vỏ thật, ruột bịa** |
| 4 | **webmcp.org** | 200 | **Trang test JSON-RPC 1 file** trỏ `localhost:4333`. Không phải sản phẩm | GitHub Pages | 2025-02-02, NameCheap, hết hạn **2035** | ⚪ Mã demo bỏ hoang |
| 5 | **webmcp.us** | 200 | Trả về đúng 27 byte text: `homestar deep-linking spike` | Cloudflare Worker | 2026-03-07, GoDaddy | ⚪ Ghi chú thử nghiệm cá nhân |
| 6 | **webmcp.net** | → www | Trang **parking Namecheap** ("recently registered") | Namecheap | 2025-04-06 | 🔴 Đất trống |
| 7 | **webmcp.co** | 200 | Trang **"This domain is for sale"** tự dựng, có form liên hệ chủ | Angie/Hetzner, rDNS `1push.io` | hết hạn 2027-06-25, Virtualia LLC | 🔴 Đang rao bán |
| 8 | **webmcp.cloud** | 200 | Parking GoDaddy — "Get This Domain" | GoDaddy (3.33.130.190) | 2026-02-11 | 🔴 Đất trống |
| 9 | **webmcp.online** | 200 | Parking GoDaddy (cùng IP #8) | GoDaddy | 2025-07-28 | 🔴 Đất trống |
| 10 | **webmcp.site** | 200 | Parking GoDaddy (cùng IP) | GoDaddy | 2026-02-10 | 🔴 Đất trống |
| 11 | **webmcp.info** | 200 | Parking GoDaddy (cùng IP) | GoDaddy | 2025-07-28 | 🔴 Đất trống |
| 12 | **webmcp.biz** | 200 | Parking GoDaddy (cùng IP) | GoDaddy | 2026-04-07 | 🔴 Đất trống |
| 13 | **webmcp.me** | 404 | Trỏ GitHub Pages nhưng **chưa gắn repo** → "Site not found" | GitHub Pages | 2025-09-24, NameCheap, **hết hạn 2026-09-24** | 🔴 Hỏng/bỏ |
| 14 | **webmcp.ai** | — | **Không có bản ghi DNS nào** — đã mua, chưa dựng | không NS | **2025-03-04**, GoDaddy, hết hạn 2029 | 🔴 Giữ chỗ |
| 15 | **webmcp.app** | — | Có NS Cloudflare nhưng **không có bản ghi A** | Cloudflare NS | 2025-07-10, Porkbun | 🔴 Giữ chỗ |

> 5 tên miền `.cloud .online .site .info .biz` **trỏ chung một IP GoDaddy `3.33.130.190`** → cùng một kho parking, nhiều khả năng cùng một người/nhóm gom tên miền để đầu cơ (suy luận từ hạ tầng chung + cùng registrar GoDaddy; **chưa xác minh chủ sở hữu** vì WHOIS đã ẩn danh).

---

## 3. Ba dịch vụ thật — mô tả chi tiết + kết quả test

### 3.1 `webmcp.com` — WebMCP Directory (của nekuda) 🟢

**Bán/cho gì:** danh bạ trực tiếp các website đã gắn công cụ WebMCP, cộng bộ công cụ để bạn tự gắn.

**Các mảng sản phẩm quan sát được:**

| Mảng | Nội dung |
|---|---|
| `/directory` | Danh bạ site + xem từng `tool` và input schema |
| `/api/v1/*` | **API công khai, không cần khoá, CORS mở** — dành cho agent đọc máy |
| `/benchmark` | **WindTunnel** — benchmark mở so WebMCP với agent điều khiển màn hình |
| `/ecosystem-tracker` | Theo dõi trình duyệt/agent/framework nào đã hỗ trợ WebMCP |
| `/resources`, `/blog` | Tài liệu, spec, bài viết kỹ thuật |
| Scanner "Scan my site" | Quét site của bạn, đề xuất bộ tool nên làm |

**Test 1 — API (đã gọi thật, tất cả đều trả 200 + JSON hợp lệ):**

```bash
curl "https://webmcp.com/api/v1/stats"
curl "https://webmcp.com/api/v1/sites?limit=2"
curl "https://webmcp.com/api/v1/lookup?url=https://render.com"
curl "https://webmcp.com/api/v1/tools?q=checkout&limit=3"
curl "https://webmcp.com/api/v1/platforms/shopify"
```

Kết quả `/stats` lúc 2026-09-09T18:50Z:

| Chỉ số | Giá trị |
|---|---|
| Site trong danh bạ | **564** (526 live, 38 demo) |
| Tool đã lập chỉ mục | **3.763** |
| Phân loại tool | `answer` 1.649 · `act` 1.934 · `transact` 180 |
| Cách cài | `imperative` 3.640 · `declarative` 123 |
| Cửa hàng Shopify | **833.707** (814.365 xác nhận tĩnh, 19.325 tool chạy thật) |
| Site nhiều tool nhất | `eworker.ca` (73 tool) |

`lookup` phân biệt đúng: `render.com` → `supported: true` (5 tool); `example.com` → `supported: false`.

**Test 2 — Scanner (chạy end-to-end với `render.com`):**
Bấm "Scan my site" → **chuyển sang `app.agentlane.com`** → chạy ~2 phút qua 2 pha ("Exploring the site and generating tools" → "Verifying generated tools in a fresh browser") → trả **9 tool**: 5 tool `Built-in` mà render.com đã có sẵn (`render.docs.search`, `render.docs.get-markdown`, `render.llms.get-index`, `render.blog.get-index`, `render.articles.get-index`) + **4 tool mới đề xuất** (`list_templates`, `get_template`, `start_template_deploy`, `start_free_account`), độ tin cậy hiển thị 95%.
→ **Muốn dùng tiếp phải đăng nhập** ("Sign in to add them to your workspace"). Tôi dừng ở đây — không tạo tài khoản, không nhập email của bạn.

**Test 3 — kiểm chứng độc lập rằng danh bạ nói thật.** Tôi tải HTML `render.com` và tìm dấu vết WebMCP:
```html
<script id="webmcp" type="application/json">{"spec":"webmcp/0.1","tools":[...]}</script>
```
kèm đoạn JS `const modelContext = navigator.modelContext; if (!modelContext) return;` rồi `modelContext.registerTool(tool)` / `modelContext.provideContext(...)`.
→ **Đúng như danh bạ mô tả.** `attio.com` cũng có component `WebMcpTools`. Cơ chế "guard `if (!modelContext) return`" giải thích vì sao khi tôi chạy JS trong trình duyệt thường thì `navigator.modelContext` = `undefined`: **API chưa bật trong Chrome bản thường**, phải qua origin trial hoặc `chrome://flags/#enable-webmcp-testing`.

**Ai đứng sau:** `agentlane.com` và `nekuda.ai` trả về **cùng một trang** → cùng công ty **nekuda**. Danh mục của họ: AgentLane (quản lý WebMCP trên site), WebMCP Kit (plugin cho coding agent), tiện ích Chrome, SDK `@nekuda/webmcp-sdk`, webmcp.com, Protocol Scout, WindTunnel.
→ **Mô hình kinh doanh:** danh bạ + benchmark + scanner miễn phí là phễu, tiền nằm ở AgentLane (SaaS quản lý tool WebMCP).

**Số liệu benchmark WindTunnel họ công bố** (49 task, board v1.1, 19 cấu hình — *tôi đọc được nhưng chưa tự chạy lại*): WebMCP giải 49/49 task, nhanh **3–5×** (7,4s vs 26,1s/task), rẻ **4–23×** (0,8 xu vs 7,1 xu/task), điểm cuối cao hơn **38%** (91,9 vs 66,4) so với agent điều khiển màn hình.

---

### 3.2 `webmcp.dev` — thư viện JS gốc của Jason McGhee 🟢 (nhưng đã "về hưu")

**Là gì:** thư viện JavaScript mã nguồn mở nhét 1 widget vuông xanh vào góc trang; người dùng dán "connection token" để nối trang web với MCP client (Claude Desktop…). Đây là **nguyên mẫu WebMCP đầu tiên**, ra 03/2025.

Repo `github.com/jasonjmcghee/WebMCP`: **820 sao**, 52 fork, MIT, push cuối 2026-02-15. Mô tả repo tự nói: *"Early WebMCP proposal / implementation — since evolved and worked on by much more capable folks"* và trỏ sang W3C.
npm `@jason.today/webmcp`: bản mới nhất **0.1.13**, publish cuối **2025-03-23**, **1.518 lượt tải/tháng**.

**Test thật — chạy được, có 1 giới hạn môi trường:**

1. `npx -y @jason.today/webmcp@latest --help` → in đúng bảng tuỳ chọn (port mặc định 4797, `-n` tạo token, `--mcp` chạy chế độ MCP server). ✅
2. `npx ... -n` → tạo token, server chạy daemon PID 4923 nghe cổng 4797. ✅
3. **Nối MCP qua stdio** — tôi gửi `initialize` + `tools/list` thật:
   → server trả `serverInfo: {name: "WebMCP", version: "0.1.12"}`, capabilities `tools/prompts/resources/sampling`, và 2 tool cầu nối `_webmcp_get-token`, `_webmcp_define-mcp-tool`. ✅ **Nửa MCP hoạt động tốt.**
4. **Nối widget trên trang** → dán token vào widget ở `webmcp.dev` → hiện **"Disconnected"**. Nguyên nhân: trình duyệt trong sandbox của tôi **không truy cập được `localhost:4797` của máy host** (`fetch('http://localhost:4797/')` → `Failed to fetch`). Đây là **giới hạn môi trường test, không phải lỗi thư viện** — console trang vẫn log `Tool registered: calculator`, `Tool registered: echo`, chứng tỏ phía trang chạy đúng.
5. Đã dọn: `--quit` → "Server stopped successfully", cổng 4797 giải phóng. ✅

**Đánh giá:** dùng được, nhưng **đừng chọn cho dự án mới** — chính tác giả đã chuyển tiếp sang bản W3C, và npm 6 tháng không có bản mới.

---

### 3.3 `webmcp.xyz` — "WebMCP Registry" 🟡 CẢNH BÁO

**Tự nhận:** "The Unofficial Web Model Context Protocol Directory". Dựng bằng **Lovable** (ảnh OG còn nguyên link `lovable.app`), backend Supabase (URL chi tiết dạng `/site/<uuid>`). Đăng ký 2026-02-10.

**Có:** danh bạ 11 site, blog 12 bài, trang `/submit` có ô "✨ Scan with AI" và **gói trả phí "Featured Listing" — huy hiệu vàng, nổi bật 30 ngày**.

**Ba vấn đề tôi kiểm chứng được:**

**(a) Dữ liệu danh bạ phần lớn là bịa.** 10/11 mục "featured" là thương hiệu lớn: Expedia, Shopify, GitHub, Twilio, OpenWeather, Airbnb, Stripe, Notion, Reuters, Figma. Trang chi tiết Expedia in ra JSON `{"protocol": "webmcp/1.0", ..., "verified": true}`.
- Đối chiếu `webmcp.com/api/v1/lookup`: **cả 10 đều `supported: false`**.
- Kiểm trực tiếp: tôi tải HTML `expedia.com` và grep `modelcontext|webmcp|registerTool|provideContext` → **0 kết quả** (cùng lệnh grep tìm ra dấu vết rõ ràng ở `render.com`).
- Thêm nữa, chuỗi `"protocol": "webmcp/1.0"` không tồn tại trong spec; `render.com` thật dùng `"spec":"webmcp/0.1"`.
→ **Nhãn `verified: true` là sai sự thật.**

**(b) Tài liệu kỹ thuật sai spec.** Bài "What is WebMCP?" dạy rằng WebMCP hoạt động qua file manifest `/.well-known/webmcp.json` với `webmcp_version: "1.0"` và các REST endpoint.
Đối chiếu README chính thức của `webmachinelearning/webmcp` mà tôi tải về: spec dùng **JavaScript API `document.modelContext.registerTool()`**, và mục "Alternatives considered → 2. Static Declarative Manifests" **nêu rõ lý do bác bỏ** cách dùng manifest tĩnh làm cơ chế duy nhất.
→ Ai làm theo hướng dẫn của webmcp.xyz sẽ **cài ra thứ không có agent nào gọi được**.

**(c) Blog gần như là vỏ rỗng.** 12 bài liệt kê nhưng chỉ **1 bài** (`/blog/what-is-webmcp-protocol`) mở được; 11 nút "Read more" còn lại không dẫn đi đâu.

**Kết luận:** site làm ra để hứng SEO từ khoá "webmcp" rồi bán chỗ hiển thị. **Không nên dùng làm nguồn tham khảo, càng không nên trả tiền Featured Listing.**

---

## 4. Hai "gần như trống" đáng ghi nhận

- **`webmcp.org`** — 1 file HTML dùng Preact qua unpkg, dựng form JSON-RPC (Server URL mặc định `http://localhost:4333`, method `initialize`/`echo`). Tôi bấm "Send Request" thật → **`Error: Failed to fetch`**. Không có backend. Đáng chú ý: đăng ký từ 2025-02-02 và **trả tiền tới 2035** — giữ tên miền dài hạn nhưng bỏ hoang nội dung.
- **`webmcp.us`** — Cloudflare Worker trả duy nhất chuỗi `homestar deep-linking spike`. Tôi dò `/mcp`, `/sse`, `/.well-known/mcp.json`, `/api`, `/health` → tất cả **404**. Là ghi chú/spike cá nhân, không phải dịch vụ.

---

## 5. Bối cảnh chuẩn (để bạn biết mình đang đứng ở đâu)

Từ `webmcp.com/ecosystem-tracker` (họ ghi "Verified 6 Sep 2026") + đối chiếu repo W3C:

- **Spec chính thức:** `webmachinelearning/webmcp`, 3.905 sao, cập nhật 2026-09-04. Trạng thái: dự thảo Community Group, **chưa phải chuẩn cuối**.
- **Chrome:** đang origin trial, nhắm mốc **Chrome 157 (dự kiến 03/11/2026)** — mới là *mục tiêu*, chưa phải cam kết ra mắt. Chrome 156 (20/10/2026) là bản cuối được origin trial bao phủ. Test cục bộ: `chrome://flags/#enable-webmcp-testing`.
- **Edge:** origin trial mở đến 17/11/2026.

→ Nghĩa là: **WebMCP đang ở giai đoạn thử nghiệm sắp chín.** Site nào gắn tool bây giờ là đặt cược sớm, và code phải tự bảo vệ bằng `if (!modelContext) return`.

---

## 6. Khuyến nghị (1 dòng mỗi mục)

1. **Muốn theo dõi/khai thác hệ sinh thái WebMCP:** dùng `webmcp.com` + API `/api/v1/*` — miễn phí, không cần khoá, dữ liệu có kiểm chứng.
2. **Muốn tự triển khai WebMCP:** bám **spec W3C `webmachinelearning/webmcp`** và tài liệu Chrome for Developers. Đừng bám `webmcp.xyz`.
3. **Đừng dùng `@jason.today/webmcp` cho dự án mới** — chỉ đọc để hiểu lịch sử; chính tác giả đã trỏ sang W3C.
4. **Nếu bạn định mua tên miền `webmcp.*`:** `.co` đang rao bán tự do, 5 tên `.cloud/.online/.site/.info/.biz` đang parking GoDaddy, `.me` **hết hạn 24/09/2026** (có thể rớt ra thị trường). `.com`, `.dev`, `.xyz`, `.org`, `.ai` đều đã có chủ giữ chắc.
5. **Nếu định trả tiền cho scanner:** biết rằng scanner của `webmcp.com` thực chất là **AgentLane** — đánh giá AgentLane, không phải đánh giá "webmcp.com".

---

## 7. Câu hỏi còn treo

1. **Chủ sở hữu thật của nhóm 5 tên miền parking GoDaddy cùng IP** — WHOIS ẩn danh, tôi chỉ suy ra "cùng kho" từ hạ tầng chung, chưa xác minh được là một chủ.
2. **`webmcp.ai` (mua 2025-03-04, cùng ngày repo của Jason McGhee ra đời) và `webmcp.app`** — cùng thuộc Jason hay người khác đón đầu? Chưa xác minh; `.dev` và `.app` cùng registrar Porkbun nhưng khác nhà DNS.
3. **Số liệu WindTunnel** — tôi đọc từ trang của nekuda, **chưa tự chạy lại benchmark**. Đây là số của bên bán WebMCP, nên đọc với thái độ dè dặt.
4. **Scanner AgentLane sau bước đăng nhập** — giá, giới hạn, chất lượng tool sinh ra: chưa kiểm vì tôi không tạo tài khoản. Bạn muốn tôi test tiếp thì cần bạn tự đăng ký rồi cho biết kết quả.
5. **Widget `webmcp.dev` nối token end-to-end** — chưa chứng minh được do sandbox chặn `localhost`; cần chạy trên Chrome máy bạn để xác nhận.
