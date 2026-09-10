# webmcp.com — Nghiên cứu sâu toàn bộ tính năng

**Ngày kiểm:** 2026-09-10, 04:27–05:05 UTC (11:27–12:05 giờ Sài Gòn)
**Đối tượng:** `https://webmcp.com` — WebMCP Directory
**Chủ sở hữu:** OpenCommerce Network, Inc. — kinh doanh dưới tên **nekuda** (nekuda.ai)
**Cách kiểm:** đọc sitemap + OpenAPI spec → gọi thật 10 endpoint API (kể cả ca lỗi) → tải và bóc text 12 trang → phân tích thống kê toàn bộ `directory.json` (3,78 MB / 564 site) → điều khiển trình duyệt thật, **gọi thật tool WebMCP của chính webmcp.com** → chạy lại scanner → tra npm/GitHub.
**Nguyên tắc:** mọi con số dưới đây đều tự mở/tự gọi. Chỗ nào chỉ đọc lại tuyên bố của họ mà chưa tự dựng lại thì ghi rõ **"chưa tự kiểm"**.

---

## 0. Từ điển (định nghĩa một lần, sau đó dùng lời thường)

| Từ | Nghĩa |
|---|---|
| **WebMCP** | Đề xuất chuẩn web (W3C Community Group) cho phép trang web **tự khai báo "công cụ" (tool)** để AI agent gọi trực tiếp, thay vì agent nhìn ảnh màn hình và đoán nút. API: `document.modelContext.registerTool()`. |
| **tool** | Một hành động trang web mở ra cho agent: có `name`, `description`, `inputSchema` (JSON Schema — bản mô tả tham số, giống "chữ ký hàm"). |
| **imperative / declarative** | Hai cách khai báo tool: gọi hàm JS (`registerTool`) hay đánh dấu thẳng trong HTML (thẻ `<tool>` / thuộc tính trên `<form>`). |
| **polyfill** | Đoạn JS "vá" API còn thiếu, để trang chạy được ở trình duyệt chưa hỗ trợ. |
| **origin trial** | Chế độ Chrome cho phép site bật tính năng thử nghiệm cho người dùng thật, có thời hạn. |
| **CORS** | Cơ chế cho phép trang web khác gọi API của mình. `Access-Control-Allow-Origin: *` = ai gọi cũng được. |
| **JSON-LD / schema.org** | Dữ liệu có cấu trúc nhúng trong HTML để máy tìm kiếm và AI đọc hiểu trang. |

---

## 1. TL;DR — webmcp.com là cái gì

**Không phải một danh bạ.** Là **7 sản phẩm ghép lại thành một phễu bán hàng** cho nekuda:

```
Danh bạ (miễn phí, SEO)  →  API cho agent (miễn phí, giữ chân dev)
        ↓
Benchmark WindTunnel (bằng chứng "WebMCP tốt hơn")
        ↓
Ecosystem tracker (bằng chứng "sắp tới lúc rồi")
        ↓
Scanner quét site bạn  →  đăng nhập AgentLane (SaaS trả phí)
        ↓
WebMCP Kit + SDK (dev tự cài, SDK gửi telemetry về nekuda)
```

Chất lượng thực thi **cao bất thường** cho một sản phẩm marketing: API có OpenAPI 3.1 đầy đủ, có changelog phá vỡ tương thích ghi rõ ngày, có 3 tầng file máy-đọc, benchmark mở mã nguồn Apache-2.0, ecosystem tracker ghi rõ chỗ nào "tự chúng tôi chạy thử" và chỗ nào "chỉ đọc tài liệu".

---

## 2. Bản đồ tính năng (11 khối)

| # | Khối | Trạng thái kiểm | Miễn phí? |
|---|---|---|---|
| 1 | **Directory UI** — duyệt/lọc/tìm 532 site | ✅ đã thao tác thật | Có |
| 2 | **Site detail + Tool Tree** — cây tool, xem JSON, Rescan | ✅ đã mở | Có |
| 3 | **Shopify index** — 833.707 store, toolkit dùng chung | ✅ đã tìm thật | Có |
| 4 | **API for Agents** — 10 endpoint, không cần khoá | ✅ gọi hết, kể cả ca lỗi | Có |
| 5 | **File máy-đọc** — llms.txt, llms-full.txt, directory.json, openapi.json, JSON-LD | ✅ tải hết | Có |
| 6 | **Scanner + Scorecard** — quét site, đề xuất tool, chấm điểm A+…C | ✅ chạy 1 lần end-to-end | Miễn phí đến bước đăng nhập |
| 7 | **Build path** — WebMCP Kit plugin, SDK, prompt cho coding agent | ✅ lấy được lệnh + prompt | Có (SDK MIT) |
| 8 | **WindTunnel benchmark** — 19 cấu hình, 49 task | ✅ đọc hết bảng | Có, mã Apache-2.0 |
| 9 | **Ecosystem tracker** — ~90 sản phẩm, 3 nhóm | ✅ đọc hết | Có |
| 10 | **Resources + Blog** — 20 tài nguyên, 5 bài | ✅ liệt kê hết | Có |
| 11 | **Demo riêng** — webmcp.com tự chạy WebMCP + `computer.webmcp.com` | ✅ **gọi thật tool** | Có |

---

## 3. Directory UI — chi tiết

### 3.1 Ba chỉ số ở đầu trang (và cách chúng khớp với API)

Đây là chỗ dễ nhầm nhất, nên tôi đối soát bằng số:

| Hiển thị trên trang | Giá trị | API tương ứng | Giải thích chênh lệch |
|---|---|---|---|
| VERIFIED SITES | **532** | `/stats` → `sites: 564` | 564 − 32 site Shopify tuyển chọn = 532. Shopify tách sang tab riêng. |
| VERIFIED SHOPIFY SITES | **833K+** | `platforms.shopify: 833707` | Khớp |
| TOOLS INDEXED | **3.434** | `/stats` → `tools: 3763` | 3763 − 329 tool của 32 site Shopify = 3434 |

Tôi tự tính lại từ `directory.json`: 532 site non-Shopify với **đúng 3.434** tool, 32 site Shopify với **đúng 329** tool. **Ba con số khớp tuyệt đối** — không có số làm đẹp.

### 3.2 Thanh "TOOL MIX"

Hiển thị **Answer 44% · Action 51% · Sensitive Action 5%**.
Đối chiếu API: 1.649 / 3.763 = 43,8% · 1.934 / 3.763 = 51,4% · 180 / 3.763 = 4,8%. **Khớp.**

### 3.3 Bộ lọc và điều khiển (đã bấm thật)

- **Loại:** All / Live / Demo
- **Bố cục:** Grid / List
- **Danh mục** (kèm số đếm, tổng 494 + 38 demo = 532):
  Developer Tools 102 · Productivity & Business 94 · Media & Personal 82 · AI & Agents 77 · Commerce 43 · Finance & Crypto 38 · Health & Education 32 · Travel & Events 26 · Demos 38 · Shopify 833K+
- **Ô tìm kiếm** `#dir-search-input` — lọc tức thì, không gọi mạng
- **Nạp dần:** "Show 517 more sites"

> **Chi tiết kỹ thuật đáng chú ý:** trang tải `directory-data.js` nặng **4,6 MB** — **toàn bộ danh bạ được nhúng sẵn phía client**. Vì thế tìm kiếm nhanh tức thì, nhưng lần tải đầu rất nặng. File tự khai trong comment: *"AUTO-GENERATED by scripts/scrape-tools.js… nguồn sự thật là public/directory.json"*.

### 3.4 Tiêu chí vào danh bạ (trích nguyên văn từ trang)

> *"Stub-only sites (modelContext present but no registered tools) are excluded."*

Nghĩa là: chỉ có API mà không đăng ký tool nào thì **không** được liệt kê. Đây là tiêu chí lọc rõ ràng — hiếm với loại directory này.

---

## 4. Site detail + Tool Tree

URL dạng `webmcp.com/sites/{host}` — **526 trang**, đều có trong sitemap (539 URL tổng).

Đã mở `render.com` và `aloyoga.com`. Các thành phần:

| Thành phần | Nội dung |
|---|---|
| **EXPLORE CAPABILITIES** | Đếm theo 3 loại: Answer / Action / Sensitive Action |
| **Tool Tree** | Hai chế độ **⌘ Map** (đồ thị toả tia theo trang) và **☷ Outline** (danh sách), có zoom − / + |
| **SELECTED TOOL** | Chọn 1 node → panel phải hiện: OVERVIEW, **PAGE** (trang tool chạy), **IMPLEMENTATION** (imperative/declarative), **API SURFACE** (spec/polyfill/mixed), **TOOL JSON** đầy đủ |
| **Tools verified** | Ngày quét gần nhất, **theo từng site** |
| **Rescan** | Quét lại, yêu cầu email để gửi báo cáo (POST `/api/scan`) |

**Kiểm độ tươi dữ liệu** — tôi so ngày "Tools verified" của 6 site:

| Site | Ngày verified |
|---|---|
| aloyoga.com | Sep 9, 2026 |
| render.com | Sep 7, 2026 |
| attio.com · eworker.ca · formswrite.com · webmcp.com | Sep 2, 2026 |

→ Ngày **khác nhau theo từng site**, mới nhất cách thời điểm kiểm 1 ngày, cũ nhất 8 ngày. Đây là dữ liệu quét thật, không phải một mốc chung dán cho tất cả.

---

## 5. Shopify index — khối lớn nhất về số lượng

Đã thao tác thật: bấm tab Shopify → gõ "hanoi" → **"Showing 9 of 9 matching stores"**: `aishanoir.com`, `hanoi-art.com`, `hanoi-bookworm-2.myshopify.com`, `hanoison.com`, `hanoistreetbites.com`, `karkhanoimportedcollection.com`, `matchanoire.de`, `passionnement-stephanois.fr`, `thundershop.concordiahanoi.org`.

### 5.1 Bộ tool dùng chung — 10 tool (Answer 4 / Action 6 / Sensitive 0)

| Tool | Loại | Việc |
|---|---|---|
| `search_catalog` | answer | Tìm sản phẩm/bộ sưu tập/bài viết/trang |
| `get_product` | answer | Chi tiết sản phẩm hoặc điều hướng tới trang sản phẩm |
| `get_cart` | answer | Đọc giỏ hàng |
| `search_shop_policies_and_faqs` | answer | Chính sách, FAQ, liên hệ |
| `browse_store` | act | Duyệt / điều hướng bộ sưu tập |
| `show_variant` | act | Mở trang sản phẩm ở một biến thể cụ thể |
| `update_cart` | act | Thêm / sửa số lượng / xoá dòng hàng |
| `cancel_cart` | act | Xoá sạch giỏ |
| `proceed_to_checkout` | act | Kiểm tra giỏ khác rỗng rồi **chuyển trình duyệt** sang trang thanh toán |
| `manage_orders` | act | Mở lịch sử đơn hàng |

> **Điểm tinh tế đáng khen:** `proceed_to_checkout` được xếp **Action**, không phải Sensitive Action — vì nó chỉ *điều hướng đến* trang thanh toán, **không tự trả tiền**. Cách phân loại này chính xác về mặt an toàn.

### 5.2 Nguồn gốc dữ liệu (họ ghi rõ, đáng tin)

```
source.file        : shopify_webmcp_enabled_ALL_20260803.csv
source.sha256      : e7f78f83c594919fb822403eeb50166c7dae76fb6ea271f81aac2af3ba4279c8
sourceRows         : 833.690
evidence.static_confirmed : 814.365   ← chỉ xác nhận tĩnh
evidence.tools_live       :  19.325   ← thật sự thấy tool chạy
updatedAt (index)  : 2026-09-09  |  toolsUpdatedAt : 2026-09-09
sentinelHost       : aloyoga.com     ← store tham chiếu để lấy bộ tool
```

**Cảnh báo họ tự viết** (nguyên văn): *"Index membership is not a live verification."* — tức 833K store chỉ là **thành viên danh sách nhập vào**, không phải mỗi cái đều đã được kiểm trực tiếp. Chỉ **19.325** store (2,3%) có bằng chứng tool chạy thật.

→ **Đọc đúng con số:** đừng nói "833.707 store hỗ trợ WebMCP đã kiểm chứng". Nói: "833.707 store nằm trong index nhập từ CSV ngày 03/08/2026; 19.325 có bằng chứng tool chạy".

---

## 6. API for Agents — mổ xẻ đầy đủ

**Base:** `https://webmcp.com` · **Không cần khoá** · **CORS `*`** (preflight OPTIONS trả 204) · **`Cache-Control: public, max-age=60`** · Spec: `/api/openapi.json` (OpenAPI **3.1.0**, 12,3 KB).

### 6.1 Bảng 10 endpoint (đã gọi thật toàn bộ)

| Endpoint | Tham số | Kết quả kiểm |
|---|---|---|
| `GET /api/v1/lookup` | `url` **hoặc** `host` | ✅ `render.com`→supported true; `example.com`→false; thiếu tham số→**400** có thông báo rõ |
| `GET /api/v1/sites` | `type`, `q`, `tool`, `kind`, `impl`, `apiSurface`, `fields`, `limit`, `offset` | ✅ mọi bộ lọc hoạt động, `total` đổi đúng |
| `GET /api/v1/sites/{host}` | — | ✅ ; host lạ → **404** `{"ok":false,"error":"site not found"}` |
| `GET /api/v1/sites/{host}/tools` | — | ✅ trả `{ok, host, url, count, tools}` |
| `GET /api/v1/sites/{host}/tools/{tool}` | — | ✅ ; tool lạ → **404** có `host` + `tool` trong body |
| `GET /api/v1/tools` | `q`, `kind`, `impl`, `limit`, `offset` | ✅ `q=checkout` → **total 114** |
| `GET /api/v1/stats` | — | ✅ (xem §6.4) |
| `GET /api/v1/platforms/shopify` | — | ✅ |
| `GET /api/v1/platforms/shopify/stores` | `q` (3–100 ký tự) | ✅ `q=al` (2 ký tự) → **400** `{"error":"query must be 3–100 characters","minLength":3}` ; `q=coffee` → matchCount **4.803**, trả tối đa **20** |
| `GET /api/directory.json` | — | ✅ Legacy, dump toàn bộ **3,78 MB** |

### 6.2 Ba mức `fields` — tiết kiệm băng thông thế nào

Tôi so trực tiếp key của một tool:

| `fields` | Key trong mỗi tool |
|---|---|
| `full` (mặc định) | `name, kind, impl, description, inputSchema, executable, handlerField, page` |
| `summary` | như trên **trừ `inputSchema`** |
| `minimal` | chỉ `name, kind, impl, description` |

Key của site không đổi giữa 3 mức: `host, url, desc, type, category, apiSurface, prominence, favicon, toolCount, tools`.

> **`prominence` không có trong OpenAPI spec** — một trường ẩn. Tôi giải mã được ý nghĩa (xem §6.5).

### 6.3 Thay đổi phá vỡ tương thích — họ ghi rõ ngày

Trích changelog trong `info.description` của OpenAPI:

> **2026-07-03:** đổi tên `kind`: `read`/`write`/`action` → **`answer`/`act`/`transact`**. Giá trị cũ **không còn được phát ra và không còn được chấp nhận** ở bộ lọc `kind`.

Hiển thị trên web: `answer` = **Answer**, `act` = **Action**, `transact` = **Sensitive Action**.

### 6.4 `/api/v1/stats` — số thật lúc 2026-09-10T04:27Z

```json
{
  "totalSites": 834240, "sites": 564, "liveSites": 526, "demoSites": 38,
  "tools": 3763,
  "byKind": { "answer": 1649, "act": 1934, "transact": 180 },
  "byImpl": { "imperative": 3640, "declarative": 123 },
  "platforms": { "shopify": 833707 }
}
```

### 6.5 Phân tích thống kê toàn bộ 564 site (tôi tự tính từ `directory.json`)

**Phân bố tool trên mỗi site**

| Chỉ số | Giá trị |
|---|---|
| min / p25 / trung vị / p75 / p90 / max | 1 / 3 / **5** / 8 / 12 / **73** |
| trung bình | 6,67 tool/site |
| site có ≥ 10 tool | 120 (21%) |
| site có 0 tool | 0 (đúng tiêu chí lọc stub) |

**Top 10 site nhiều tool nhất**

| Tool | Site | Danh mục |
|---|---|---|
| 73 | eworker.ca | Productivity & Business |
| 61 | cesium-browser-agent.pages.dev | AI & Agents |
| 54 | neohack.dev | Developer Tools |
| 47 | hunchbank.com | AI & Agents |
| 44 | birmakine.com | Commerce |
| 42 | persona-chat.dev | Developer Tools |
| 40 | lectern.click | Health & Education |
| 37 | vaanzari.com | Commerce |
| 35 | sssnack.com | AI & Agents |
| 31 | fiveminutebrief.ai | Media & Personal |

**`apiSurface`** — cách site đăng ký tool: `spec` **532** · `polyfill` **28** · `mixed` **4**
→ 94% đã dùng API chuẩn, không phải polyfill. Tín hiệu chuẩn đang thắng.

**`impl`**: imperative **3.640** (96,7%) · declarative **123** (3,3%)
→ Cách khai báo bằng HTML thuần gần như chưa ai dùng, dù nekuda có hẳn một bài blog quảng bá nó.

**`handlerField`** (tên hàm xử lý): `execute` 3.598 · `handler` 11 · `invoke` 2 · không có 152
**`executable`**: true 3.722 · false 14 · không có 27

**`prominence` — trường ẩn, là thứ tự ưu tiên hiển thị:**

| Giá trị | Số site | Ai |
|---|---|---|
| 0 | 1 | `openai.com` |
| 1 | 14 | aloyoga, reebok, redbus.in, forter, attio, telnyx, monday.com, render.com, ziprecruiter, quicknode, feverup, netgear, awaytravel, crewai |
| 2 | 14 | ai.simplepdf.com, store.nekuda.ai, **webmcp.com**, openfort.io, attention.com, nodecraft.com… |
| 3 | 56 | phần còn lại được đẩy lên |
| (không có) | 479 | mặc định |

→ Danh bạ **có xếp hạng biên tập**, không phải thứ tự trung lập. Không sai, nhưng nên biết.

**20 tên tool phổ biến nhất** (2.983 tên khác nhau trên 3.763 tool):
`get_product` 43 · `search_catalog` 39 · `get_cart` 39 · `update_cart` 34 · `proceed_to_checkout` 32 · `cancel_cart` 31 · `search_shop_policies_and_faqs` 31 · `browse_store` 30 · `show_variant` 30 · `manage_orders` 30 · `get_pricing` 24 · `add_to_cart` 14 · `search_docs` 13 · `search_products` 12 · `scan_images_c2pa` 11 · `inspect_image_c2pa` 11 · `navigate` 10 · `list_services` 10 · `book_demo` 9 · `get_page` 8
→ 10 tên đầu đều là bộ Shopify — chứng tỏ **thương mại điện tử đang dẫn dắt việc áp dụng WebMCP**.

**125 site có tool `transact`** (tiền/cam kết): ví dụ `baerskintactical.com` → `start_checkout`, `qrcodecrafter.com` → `create_blik_payment_link_qr_code`, `forter.com` → `contact_sales`, `persona-chat.dev` → `delete_event`/`delete_slide`.

### 6.6 Ba lỗi API đáng lưu ý (dành cho người sẽ tích hợp)

1. **Enum sai không báo lỗi.** `?kind=read` (giá trị đã bỏ từ 2026-07-03) trả **HTTP 200** với `total: 0` và `filters.kinds:["read"]` — **không phải 400**.
   → Code cũ pin giá trị cũ sẽ **âm thầm trả rỗng** thay vì nổ lỗi. Đây là cái bẫy nguy hiểm nhất của API này.
2. **`limit` bị chặn ở 500.** Gửi `limit=9999` → trả `limit: 500`, `count: 500`. Không báo là đã bị cắt.
3. **Khớp theo tiền tố đường dẫn cho demo.** `lookup?url=…/demos/coffee-shop/menu?x=1` → khớp, trả `host: "coffee-shop"`, `matchedHost: "googlechromelabs.github.io"`. Nhưng `…/demos/todo/` (không tồn tại) → `supported: false`. Tức khớp theo **đúng thư mục demo**, không phải cả host.

### 6.7 Rate limit — thử thật, không chạm trần

15 request liên tiếp tới `/platforms/shopify/stores` (tài liệu ghi "rate limited") → **15/15 đều 200**. 12 request tới `/api/v1/sites` → **12/12 đều 200**. Ngưỡng cụ thể **chưa xác định**; tôi dừng ở mức thăm dò lịch sự.

### 6.8 Công thức dùng ngay

```bash
curl -s "https://webmcp.com/api/v1/lookup?url=https://render.com" | jq '.supported'
```

```bash
curl -s "https://webmcp.com/api/v1/sites/render.com/tools/render.docs.search" | jq '.tool.inputSchema'
```

```bash
curl -s "https://webmcp.com/api/v1/sites?fields=minimal&limit=500&offset=0" | jq '{total, count, next: (.offset + .count)}'
```

> **Bẫy thường gặp:** đừng chỉ đọc `count` rồi dừng — phải so `offset + count` với `total`. Và đừng pin `kind=read/write/action` (đã bỏ), vì API trả 200 rỗng chứ không báo lỗi. Dùng `fields=minimal` khi không cần JSON Schema — nhẹ hơn nhiều lần.

---

## 7. Các file máy-đọc — 3 tầng

| File | Kích thước | Nội dung | Dùng khi nào |
|---|---|---|---|
| `/llms.txt` | 120,7 KB / 614 dòng | FAQ + Product + Research + hướng dẫn API + **danh sách 564 site 1 dòng/site** | Nạp context cho LLM, nhẹ |
| `/llms-full.txt` | **1,07 MB** / 6.592 dòng / 564 mục `##` | Mỗi site một mục, liệt kê **từng tool kèm loại và mô tả** | Cần chi tiết tool nhưng không cần JSON Schema |
| `/api/directory.json` | **3,78 MB** | Dump đầy đủ (legacy), có `inputSchema` | Phân tích offline |
| `/api/openapi.json` | 12,3 KB | Hợp đồng API 3.1.0 + changelog + 7 schema | Sinh client tự động |
| `/sitemap.xml` | 100,3 KB | **539 URL** | Crawler |
| `/robots.txt` | 2,6 KB | **Content Signals** của Cloudflare | (xem dưới) |

**`robots.txt` — điểm đáng chú ý về pháp lý:**
```
User-agent: *
Content-Signal: search=yes, ai-train=no, use=reference
```
Nghĩa: cho lập chỉ mục tìm kiếm, **cấm dùng để huấn luyện model**, cho phép dùng làm tài liệu tham chiếu. Kèm tuyên bố bảo lưu quyền theo **Điều 4 Chỉ thị EU 2019/790**. → Một directory khuyến khích agent đọc mình, nhưng chặn việc lấy nội dung đi train. Nhất quán, không mâu thuẫn.

**JSON-LD trên trang chủ:** `WebSite` · `Organization` (id `https://nekuda.ai/#org`) · **`ItemList`** (id `#directory`) · `FAQPage` · `VideoObject`.

**Không có:** `/ai.txt`, `/agents.json`, `/manifest.json`, `/feed.xml`, `/rss.xml`, `/.well-known/security.txt` — tất cả 404.

---

## 8. Scanner + Scorecard

### 8.1 Luồng đã chạy thật (`render.com`)

1. Trang chủ → chip **"No tools yet — Build WebMCP tools"** → ô nhập `#build-scan-site`
2. Bấm **"Scan my site"** → **chuyển hẳn sang `app.agentlane.com/scan/<token>?al_src=webmcp_com&al_did=<uuid>`**
3. Hai pha, ~2 phút: *"Exploring the site and generating tools"* → *"Verifying generated tools in a fresh browser"*
4. Kết quả: **"✓ 9 tools found"**
   - **5 tool `Built-in`** — tool render.com đã có sẵn: `render.docs.search`, `render.docs.get-markdown`, `render.llms.get-index`, `render.blog.get-index`, `render.articles.get-index`
   - **4 tool đề xuất mới**: `list_templates`, `get_template`, `start_template_deploy`, `start_free_account`
   - Vòng tiến độ hiện **100%**
5. **Chặn ở "Sign in to add them to your workspace"** → phễu vào AgentLane. Tôi dừng, không tạo tài khoản.

> **Điểm quan trọng:** scanner của webmcp.com **chính là AgentLane**. Đánh giá scanner = đánh giá AgentLane, không phải đánh giá webmcp.com. `build-handoff.js` xác nhận: nó gắn `?site=<url>&ref=webmcp.com` để AgentLane đo được kênh nào chuyển đổi.

### 8.2 Scorecard — cách chấm điểm (trang `/methodology`)

**Trọng số điểm cuối:** Usability **60%** + Coverage **20%** + Quality **20%**

| Tham số | Chấm cái gì |
|---|---|
| **Usability** | Một agent chấm bộ tool trên thang **1–5 nghiêm ngặt**. 5 = "Genuinely rare"; 3 = "usable, but with real gaps — bộ tốt điển hình"; 1 = "agent sẽ chật vật" |
| **Coverage** | Bao nhiêu phần site mở cho agent. 1 trang có tool = mức nền; mỗi trang thêm nâng điểm |
| **Quality** | Vệ sinh cơ học từng tool: có **mô tả thật** (không phải 1 từ), có **input schema** agent điền được, tên **snake_case** rõ ràng |

**Bậc điểm:** A+ Exceptional ★★★★★ → A → A− → B+ → B → B− → C Early ★★☆☆☆ ("WebMCP detected — vạch xuất phát")

**Bốn trạng thái không có điểm:**

| Mã | Nghĩa |
|---|---|
| `api-absent` | Không thấy `document.modelContext`, `navigator.modelContext`, hay thẻ tool declarative |
| `api-empty` | Có API nhưng **không tool nào đăng ký lúc quét** → khuyến nghị: đăng ký tool ngay khi load, đừng đợi user bấm |
| `blocked` | Site chặn quét tự động → *"That can hide your tools from agents and from this scorecard alike"* |
| `load-error` | Không tải được trang |

**Phân loại 3 bậc tin cậy** (trích nguyên văn):
> *"The category is assigned automatically by classifying each tool's name, description, and input schema during the scan, so it's **inferred, not declared** by the site."*

Tôi **xác nhận điều này bằng thực nghiệm**: gọi `getTools()` trực tiếp trên webmcp.com, mọi tool đều có `kind: null` (§13.3). Vậy `answer/act/transact` là **suy luận của webmcp.com**, không phải site tự khai.

### 8.3 Hạn chế phát hiện được: Scorecard **không** hiển thị trong danh bạ công khai

Tôi grep 6 trang site (`render.com`, `attio.com`, `aloyoga.com`, `developers.openai.com`, `forter.com`, `eworker.ca`) → **không trang nào có điểm chữ**. Grep 4,6 MB `directory-data.js` → 18 lần xuất hiện từ "grade" đều nằm trong **mô tả tool của site khác** (isitagentready.com, glama…), không phải trường điểm.

→ **Kết luận:** `/methodology` mô tả cách chấm, nhưng điểm chỉ xuất hiện trong **báo cáo quét** (gửi qua email, hoặc trong AgentLane sau đăng nhập). Danh bạ công khai không xếp hạng chất lượng. Ai đọc `/methodology` rồi đi tìm điểm trong danh bạ sẽ không thấy.

`POST /api/scan` với body rỗng → **400** `{"ok":false,"error":"invalid url or email"}` → xác nhận cần cả URL lẫn email.

---

## 9. Build path — cho lập trình viên

### 9.1 Lệnh cài (lấy trực tiếp từ `build-handoff.js`)

```bash
claude plugin marketplace add nekuda-ai/webmcp-kit && claude plugin install webmcp-kit@nekuda
```

```bash
codex plugin marketplace add nekuda-ai/webmcp-kit && codex plugin add webmcp-kit
```

```bash
npx skills add nekuda-ai/webmcp-kit --skill '*' --agent cursor
```

GitHub Copilot: hiển thị **"soon"**.

### 9.2 Prompt "Copy a prompt for your agent" — bắt được nguyên văn

Tôi hook `navigator.clipboard.writeText` rồi bấm nút Copy:

> *"Install the webmcp-kit plugin (command: `claude plugin marketplace add nekuda-ai/webmcp-kit && claude plugin install webmcp-kit@nekuda`), then use it to make this site agent-ready: implement WebMCP tools for its key user actions and keep the diff minimal."*

### 9.3 Kho và gói (số liệu tra thật)

| Thứ | Số liệu |
|---|---|
| `nekuda-ai/webmcp-kit` | ⭐**30**, 3 fork, MIT, tạo 2026-08-13, push cuối 2026-09-04 |
| `nekuda-ai/WindTunnel` | ⭐**43**, 1 fork, **Apache-2.0**, tạo 2026-07-27, push cuối **2026-09-09** |
| npm `@nekuda/webmcp-sdk` | latest **0.5.0**, chỉ **3 phiên bản**, sửa cuối 2026-08-25, **2.196 lượt tải/tháng** |
| npm `@mcp-b/webmcp-polyfill` | latest **5.1.0**, sửa 2026-08-31, **211.351 lượt tải/tháng** |
| So chiếu W3C `webmachinelearning/webmcp` | ⭐**3.905**, push cuối 2026-09-04 |

> **Ba điều rút ra:**
> 1. Hệ sinh thái thật chạy trên **`@mcp-b/webmcp-polyfill` (211K tải/tháng)**, gấp **96 lần** SDK của nekuda (2,2K). nekuda là người *quảng bá* chuẩn, không phải người *sở hữu* hạ tầng.
> 2. SDK nekuda mới 3 phiên bản, tự mô tả là **"Phase-1"** — còn rất sớm.
> 3. **webmcp.com tự dùng polyfill `@3.0.0`** trong khi bản mới nhất là **5.1.0** — chậm 2 phiên bản chính so với chính hệ sinh thái họ theo dõi.

---

## 10. WindTunnel — benchmark

**Thiết kế:** 8 website thật · **49 task** · **3 lần thử/task** · **19 cấu hình** · 4 cách điều khiển trang:

| Cách | Agent nhìn gì |
|---|---|
| **WebMCP** | Trang tự đưa hành động ra để gọi |
| **Computer use** | Ảnh chụp màn hình, thao tác theo toạ độ |
| **DOM / Accessibility tree** | Cấu trúc trang |
| **Code execution** | Model viết code, agent chạy để đọc và lái trang |

**Công thức điểm cuối** (họ công bố): tỉ lệ thành công **60%** + chi phí trung vị **20%** + thời gian trung vị **20%**; chi phí và thời gian **chuẩn hoá log** để giá trị cực đoan không lấn át. Token thống kê riêng, không tính điểm hai lần.

### Bảng xếp hạng đầy đủ (19 cấu hình, board v1.1)

| # | Cấu hình | Giao diện | Điểm | Task giải | Tỉ lệ thử | Chi phí/task | Token/task | Thời gian/task |
|---|---|---|---|---|---|---|---|---|
| 1 | GPT-5.6 Luna · native | **WebMCP** | 99,6 | 49/49 | 99,3% | $0,002 | 2.596 | 5,7s |
| 2 | Gemini 3.6 Flash · native | **WebMCP** | 95,4 | 49/49 | 100% | $0,004 | 4.453 | 7,2s |
| 3 | Gemini 3.6 Flash · Stagehand v4 | **WebMCP** | 94,0 | 49/49 | 99,3% | $0,004 | 4.371 | 8,0s |
| 4 | Sonnet 5 · native | **WebMCP** | 92,7 | 49/49 | 100% | $0,009 | 5.172 | 6,8s |
| 5 | Sonnet 5 · Stagehand v4 | **WebMCP** | 91,0 | 49/49 | 100% | $0,010 | 5.161 | 8,1s |
| 6 | GPT-6 Astra · native | **WebMCP** | 90,3 | 49/49 | 99,3% | $0,017 | 2.575 | 6,3s |
| 7 | GPT-5.6 SOL · native | **WebMCP** | 87,9 | 49/49 | 98,6% | $0,012 | 2.573 | 9,3s |
| 8 | Claude Opus 5 · native | **WebMCP** | 87,6 | 49/49 | 100% | $0,014 | 4.770 | 9,8s |
| 9 | GPT-5.6 Luna | Computer use | 75,6 | 45/49 | 91,2% | $0,017 | 20.914 | 18,3s |
| 10 | GPT-6 Astra | Code execution | 73,7 | 49/49 | 100% | $0,119 | 10.982 | 16,4s |
| 11 | GPT-5.6 Luna | DOM + vision | 70,5 | 43/49 | 88,4% | $0,033 | 29.561 | 19,8s |
| 12 | GPT-5.6 Luna | Accessibility tree | 70,2 | 40/49 | 81,0% | $0,020 | 18.517 | 16,0s |
| 13 | Gemini 3.6 Flash | Computer use | 67,7 | 43/49 | 88,4% | $0,020 | 23.857 | 33,7s |
| 14 | GPT-5.6 SOL | Computer use | 66,4 | 46/49 | 91,2% | $0,063 | 16.235 | 27,3s |
| 15 | Sonnet 5 | DOM + vision | 65,1 | 48/49 | 98,6% | $0,210 | 64.424 | 29,3s |
| 16 | GPT-6 Astra | Computer use | 63,2 | 45/49 | 91,8% | $0,261 | 20.560 | 20,8s |
| 17 | Sonnet 5 | Accessibility tree | 63,2 | 42/49 | 87,1% | $0,038 | 10.762 | 37,5s |
| 18 | Sonnet 5 | Computer use | 58,5 | 39/49 | 81,0% | $0,070 | 57.701 | 31,7s |
| 19 | Claude Opus 5 | Computer use | 57,4 | 45/49 | 91,2% | $0,139 | 47.141 | 50,4s |

**Đọc bảng:** **8 cấu hình WebMCP chiếm trọn 8 hạng đầu**, tất cả đều giải 49/49. Cấu hình không-WebMCP tốt nhất xếp hạng 9. Khoảng cách rõ nhất là **token**: WebMCP 2.573–5.172 token/task, computer-use 16.235–57.701 — **chênh 3–22 lần**.

**Changelog (họ tự công bố):**
- **v1.1 — 06/09/2026:** thêm tool `complete_checkout`, sửa task thanh toán; đo lại cả 8 cấu hình WebMCP — checkout từ **0/3 → 3/3** mỗi cấu hình. Thêm GPT-6 Astra.
- **v1.0 — 20/08/2026:** 16 cấu hình, 2.352 lượt thử.

> **Đánh giá của tôi:** benchmark này **minh bạch hơn mức trung bình của ngành** — mã nguồn, định nghĩa task và transcript đầy đủ đều ở `github.com/nekuda-ai/WindTunnel` (Apache-2.0), và họ **tự khai** rằng v1.0 làm hỏng task checkout rồi sửa ở v1.1.
> **Nhưng** đây vẫn là benchmark do **bên bán WebMCP** thiết kế: họ chọn 8 site, chọn 49 task, chọn công thức trọng số. Việc WebMCP thắng gần như là tất yếu về mặt kiến trúc (gọi hàm luôn rẻ hơn đọc ảnh). **Tôi chưa tự chạy lại.**

---

## 11. Ecosystem Tracker — phần giá trị nhất

"Verified 6 Sep 2026", **~90 sản phẩm được kiểm**, chia 3 nhóm + 1 đuôi dài.

### 11.1 Trình duyệt

| Trình duyệt | Trạng thái | Chi tiết |
|---|---|---|
| **Chrome** | Origin trial | Chrome Status nhắm **Chrome 157 (03/11/2026)** — *mục tiêu, chưa cam kết*. Trial phủ đến Chrome 156 (ra 20/10/2026). Cờ test: `chrome://flags/#enable-webmcp-testing` |
| **Edge** | Origin trial | Mở đến **17/11/2026**. Microsoft chưa công bố phiên bản Edge khởi điểm |
| **Brave** | Sau cờ | Desktop + Android. **Trình duyệt duy nhất có cả hai nửa**: API có, và trợ lý Leo của họ đọc được. Đồng sáng lập Brian Bondy demo công khai 19/08. Bật: `--enable-blink-features=WebMCP` |
| **Lightpanda** | Một phần | Engine headless cho agent. Có WebMCP từ **0.3.6 (7/2026)**, nhưng đặt ở **`navigator`** (địa chỉ cũ) chứ không phải `document` → trang theo spec hiện tại **không được nhìn thấy** |
| **Firefox** | Không hỗ trợ | Mozilla **trung lập**. Lo ngại: site có thể đưa agent chỉ dẫn mà người không nhìn thấy; thu thập dữ liệu qua thứ người dùng nhập vào tool |
| **Safari** | **Phản đối** | WebKit lập luận: agent hành động thay người **gần với công nghệ trợ năng** (như screen reader), site **không nên phát hiện được** và đối xử khác. Đề nghị lập working group mới, bắt đầu bằng workshop tại **TPAC tháng 10** |
| Comet, Dia, Sigma, Fellou | Không tín hiệu | Đều nền Chromium, API *có thể* có sau cờ — nhưng đó không phải là sản phẩm hỗ trợ |

### 11.2 Agent

| Agent | Trạng thái | Chi tiết |
|---|---|---|
| **ChatGPT desktop app** | ✅ **Chạy hôm nay** | Từ **25/08** bật **"site tools"** — tên OpenAI gọi WebMCP — trong trình duyệt tích hợp, **mặc định bật**, tắt ở Settings → Browser → Permissions. Yêu cầu **GPT-5.6 Sol hoặc Terra** (*"GPT-5.6 Luna currently has WebMCP disabled"*), không có ở workspace Enterprise/Edu. Mỗi lần gọi đều qua **safety review**. nekuda ghi *"We tested this one ourselves"* |
| **ChatGPT Work** | ✅ Chạy hôm nay | Trình duyệt đám mây phía OpenAI. Tài liệu OpenAI **không nói tới** bề mặt này nhưng nekuda thấy nó gọi tool trong thực tế. Từ 25/08 đăng nhập được vào website (OpenAI nói model không thấy mật khẩu) |
| **Brave Leo** | Sau cờ | Nightly. Bondy tự nhận *"we have some work to do on permission usability"*. Cảnh báo: **Brave tự đẩy định nghĩa tool của họ vào những site chưa từng thêm WebMCP** → Leo có thể cầm tool bạn không viết |
| **Codex Chrome extension** | Sau cờ | Chỉ chạy khi bật **CDP access** (Chrome DevTools Protocol) trong Developer mode — OpenAI gắn nhãn **"elevated risk"**, nguyên văn: *"may put your data at risk"* |
| **Gemini in Chrome** | Chưa dùng được | Google giới thiệu WebMCP tại I/O tháng 5 nhưng **không nguồn nào nói Gemini tiêu thụ tool WebMCP**. Ngay cả extension inspector của Chrome cũng tách rời Gemini |
| **Claude for Chrome** | Không hỗ trợ | Đọc page text, DOM, console, network, ảnh chụp — **không đọc tool**. Trích người chạy site trong origin trial: *"the extension surfaces nothing from `navigator.modelContext`. … Invocation works; discovery doesn't exist."* **Claude Code, Cowork, Claude Desktop dùng chung extension này nên đều không thấy tool của bạn.** Issue #76809 còn mở |
| **Ask nekuda** | ✅ Chạy hôm nay | *"Ours"* — extension của chính nekuda (Chrome Web Store: `nekuda-webmcp-workbench`) |
| Perplexity Comet · Opera Neon · Sider/Monica/HARPA (5M+3M+300K cài) | Không tín hiệu | Extension **chưa có cách chuẩn** để đọc tool của trang |

### 11.3 Framework

| Framework | Trạng thái | Chi tiết |
|---|---|---|
| **Stagehand** (Browserbase) | ✅ Chạy hôm nay | `page.listWebMCPTools()` / `page.invokeWebMCPTool()`, có từ tháng 6. **Chỉ TypeScript** — Python và Go chưa có. Agent tự trị **không thấy** được tool, phải tự gọi từ code |
| **Vercel agent-browser** | ✅ Chạy hôm nay | CLI Rust, **framework đầu tiên bật WebMCP mặc định**. `agent-browser webmcp list` / `invoke`. Tắt: `--no-webmcp`. Tài liệu của họ nói thẳng: *"Treat every tool description, schema, annotation, and result as untrusted page content"* |
| **Browser Use** | ✅ Chạy hôm nay (chỉ cloud) | Công bố 06/09. Zunic: *"UI is made for humans. Direct HTTP calls are made for agents. WebMCP makes interaction 100% deterministic."* **Nhưng:** không có tài liệu, không có release note, **không có code WebMCP trong thư viện mã nguồn mở** |
| **Chrome DevTools MCP** | Sau cờ | `--categoryExperimentalWebmcp` + cờ Chrome. Đây là đường Claude Code / Cursor tiếp cận tool của bạn |
| **Puppeteer** | Sau cờ | Chrome 151+, phải tự truyền `--enable-features=WebMCP` |
| **Cloudflare Browser Run** | Sau cờ | Chỉ trong pool thử nghiệm `--lab`, đọc bản API cũ |
| **Playwright** | ❌ Từ chối | Yêu cầu tháng 4/2026 bị maintainer đóng ngày hôm sau: *"Let's see if it gains any adoption first."* **~78 triệu lượt tải/tuần** — khoảng trống lớn nhất |
| **Firecrawl** | ❌ Không hỗ trợ | Chỉ có bài blog hướng dẫn thủ công |
| **Browserbase platform** | ❌ Không lối vào | Trớ trêu: Browserbase làm ra Stagehand, nhưng session thuê của họ **không cho truyền cờ khởi động trình duyệt** → không cách nào bật WebMCP |

**Nhóm "đẩy tool vào trang" (dễ nhầm, họ tách riêng):** Cloudflare agents SDK · Rtrvr.ai Rover · Angular/OpenSumi · @mcp-b polyfill.

> **Đây là phần tôi đánh giá cao nhất trên webmcp.com.** Nó ghi rõ **nguồn từng dòng**, phân biệt *"We tested this one ourselves"* với *"this row reads from the announcement alone"*, **trích nguyên văn cả những ý phản đối** (WebKit, Mozilla, Playwright) và **tự nêu rủi ro** (Brave đẩy tool lạ, CDP "elevated risk"). Với một trang do bên bán WebMCP dựng, mức tự phản biện này là hiếm.

---

## 12. Resources + Blog

**`/resources` — 20 mục, 6 nhóm:**

| Nhóm | Mục |
|---|---|
| Spec & Standards (3) | W3C Draft Spec · `webmachinelearning/webmcp` · Awesome WebMCP |
| Official Docs (5) | Chrome for Developers: WebMCP · Build WebMCP Tools · Origin Trial (Chrome 149) · **WebMCP Tool Security** · **Agent Security Considerations** |
| Frameworks (1) | Angular WebMCP (v22+) |
| Tools (4) | **nekuda WebMCP Workbench** (extension của họ) · Model Context Tool Inspector (Google) · Cloudflare Browser Run · GoogleChromeLabs/webmcp-tools |
| Videos & Talks (3) | BlinkOn 21 — Dominic Farolino (Google), 4/2026 · "Don't Let AI Agents Push Your Buttons" — Khushal Sagar (Google), 11/2025 · Alex Nahas (tác giả MCP-B) |
| Community (3) | Chrome AI Early Preview · Google Groups · **r/webmcp** |

**`/blog` — 5 bài:**

| Ngày | Bài | Độ dài |
|---|---|---|
| 2026-09-05 | 6 Reasons to Implement WebMCP on Your Website or Web App | ~1.016 từ |
| 2026-08-31 | Bring Your Own Agent (BYOA). What Does the Website Bring? *(bài khách)* | ~2.012 từ |
| 2026-08-13 | WindTunnel: Benchmarking WebMCP Against Browser Agents | ~1.598 từ |
| 2026-07-09 | Building Awesome User (and Agent) Journeys with WebMCP | ~1.481 từ |
| 2026-07-09 | Making Your Website Agent-Ready: The Easy Way *(API declarative)* | ~931 từ |

---

## 13. webmcp.com tự dùng WebMCP — và tôi đã gọi thật

### 13.1 Trang chủ đăng ký 6 tool sống

Trang nạp polyfill `@mcp-b/webmcp-polyfill@3.0.0` từ jsDelivr. Tôi kiểm trong trình duyệt:

```js
// navigator.modelContext tồn tại nhờ polyfill, không phải API gốc của trình duyệt
navigator.modelContext.__isWebMCPPolyfill  // → true

// Xem trình duyệt đang có những phương thức WebMCP nào
Object.getOwnPropertyNames(Object.getPrototypeOf(navigator.modelContext))
// → registerTool, unregisterTool, getTools, executeTool,
//   executeToolByName, getTestingShim, notifyToolsChanged, …
```

`getTools()` trả **6 tool**: `about`, `request_listing`, `surprise_me`, `share_on_x`, `share_on_linkedin`, `record_unsupported_request`.

> **Directory ghi webmcp.com có 7 tool, trang chủ chỉ đăng ký 6.** Tool thứ 7 (`suggest_resource`) gần như chắc chỉ đăng ký trên `/resources` → **tool là theo từng trang, không phải theo cả site.** Đây là điều quan trọng khi bạn tự triển khai.

### 13.2 Gọi thật 2 tool

```js
// LƯU Ý QUAN TRỌNG: executeToolByName nhận CHUỖI JSON, không phải object.
// Truyền một object sẽ ném "UnknownError: Failed to parse input arguments"
await navigator.modelContext.executeToolByName('about', '{}')
```

Kết quả — đúng định dạng MCP `{content:[{type:'text', text:…}]}`:
> *"The WebMCP Directory — webmcp.com. A live directory of WebMCP-enabled sites and tools. WebMCP is a web platform proposal (W3C webmachinelearning) that lets a page expose tools via `document.modelContext`…"* rồi liệt kê site.

Gọi tiếp `surprise_me` → trang **thật sự vẽ ra một con thú pixel**: *"Nekudoraptor primus — Class: Mosalithia · Period: Late Webcene"*.
→ **Bằng chứng trực tiếp rằng tool WebMCP điều khiển được giao diện thật, không chỉ trả text.**

### 13.3 Một phát hiện quan trọng: `kind` do webmcp.com suy luận, không phải site khai

Mọi tool `getTools()` trả về đều có **`kind: null`**. Nhưng API danh bạ gán `about → act`, `request_listing → act`… → xác nhận đúng như `/methodology` nói: **phân loại 3 bậc tin cậy là suy luận của scanner**, site không tự khai. Người dùng danh bạ nên hiểu: `transact` là *phán đoán của webmcp.com*, không phải cam kết của chủ site.

### 13.4 `computer.webmcp.com` — demo hoành tráng nhất

Một **"máy tính" chạy trong trình duyệt**, khẩu hiệu *"one machine, two users"* — người và agent dùng chung. 30 tool: 17 act, 11 answer, **2 transact** (`os_publish`, `fs_delete`).

| Nhóm | Tool |
|---|---|
| Cửa sổ | `app_open`, `app_close`, `app_list`, `window_focus/move/resize` |
| Hệ thống | `sys_status`, `screensaver_wake`, `os_manual`, `os_search`, `settings_get/set`, `ps`, `kill` |
| Tệp | `fs_read`, `fs_write`, `fs_edit`, `fs_search`, `fs_list`, `fs_mkdir`, `fs_delete`, `fs_move` |
| Terminal | `term_exec` (shell `just-bash`), `term_read`, `term_state`, `term_history` |
| Bên ngoài | `browser_open` (Chrome đám mây Cloudflare), `cloud_exec` (container), `os_publish` (xuất bản ra URL công khai), `ui_open` |

Tôi mở thật: hiện màn hình chờ → bấm → desktop có `brief.md`, `pizza-demo.md`, dock ứng dụng, thanh trạng thái **`CLOUD · LEASE 14:33`** (container thuê tạm) và **`AGENT SURFACE: NONE`**.

Nội dung `brief.md` (đọc thật) là một đề bài gửi cho agent: dựng landing page cho công ty leo núi đêm "Aurora Trails" ở Bắc Na Uy — đặt ở `~/site/`, chạy `serve site/`, hero + 3 thẻ tour giá 89/129/189 EUR, form đặt chỗ, bảng màu navy-teal-tím.

> **Giới hạn tôi xác minh được:** `navigator.modelContext` và `document.modelContext` đều **undefined** trên trang này — nó **không nạp polyfill**. Trang tự báo **`AGENT SURFACE: NONE`**. Nghĩa là demo này **chỉ chạy được trong trình duyệt có WebMCP thật** (Chrome origin trial, hoặc ChatGPT desktop). Trình duyệt thường mở ra chỉ xem được vỏ, không điều khiển được bằng agent.

---

## 14. Kiến trúc và vận hành (quan sát từ bên ngoài)

| Hạng mục | Quan sát |
|---|---|
| **Hosting** | Header `x-render-origin-server: Render` → chạy trên **Render.com**, đứng sau **Cloudflare** (`cf-ray`, `cf-cache-status: DYNAMIC`) |
| **Cache API** | `Cache-Control: public, max-age=60` — dữ liệu tươi trong vòng 1 phút |
| **Bảo mật header** | `x-content-type-options: nosniff`; có `report-to` / `nel` của Cloudflare |
| **Render** | Server-side rendering (tool và mô tả có trong HTML thô: `<p class="ssr-tools">`) — tốt cho SEO và cho agent không chạy JS |
| **Nguồn sự thật** | `public/directory.json` → script `scripts/scrape-tools.js` sinh ra `directory-data.js` (client) — comment trong file tự khai |
| **Phân tích** | Google Analytics 4 (`G-NXC6VRB0NV`) + `analytics.js` + `attribution.js` (giữ UTM/gclid qua các panel) |
| **Đồng ý cookie** | Có banner; **trang lõi chạy bình thường khi từ chối** (tôi đã bấm Decline và mọi thứ vẫn hoạt động) |
| **Điều hướng** | Nhãn nav kiểu `/directory`, `/about` chỉ là **trang trí** — `/directory` trỏ về `/`, `/about` là nút cuộn. Gõ thẳng URL đó ra **404**, nhưng **không phải lỗi liên kết** |
| **Chiến dịch** | `?path=build` / `?path=register` mở panel tương ứng; banner workshop Luma (16/09/2026) có thể tắt, lưu ở `localStorage` |

---

## 15. Pháp nhân, quyền riêng tư, dữ liệu (từ `/privacy`, cập nhật 13/08/2026)

- **Pháp nhân:** **OpenCommerce Network, Inc.**, kinh doanh dưới tên **nekuda**.
- **Xác nhận AgentLane = nekuda:** chính sách nói áp dụng cho *"packages currently or previously published under nekuda or **AgentLane** names"*.
- **WebMCP Kit plugin:** chạy trong máy dev, **không tải mã nguồn lên nekuda**. Tạo thư mục cục bộ `.webmcp` chứa kế hoạch tool, bản sao code sinh ra, trạng thái, phê duyệt.
- **SDK telemetry — BẬT MẶC ĐỊNH.** Gửi sự kiện khi load, khi đăng ký tool, khi tool chạy xong. Gồm: phiên bản SDK, có bề mặt WebMCP hay không, **session id ngẫu nhiên trong bộ nhớ** (không định danh lâu dài), mẫu route rút gọn, tên trình duyệt, **tên tool và schema fingerprint**, kết quả, thời lượng, kích thước phản hồi, loại lỗi.
- **Theo dõi đầy đủ tool-call — TẮT MẶC ĐỊNH, do chủ site bật.** Khi bật **có thể gồm URL đầy đủ, đầu vào và kết quả của tool, nội dung lỗi, và định danh giả danh lâu dài**. Chủ site chịu trách nhiệm thông báo/xin phép người dùng cuối.
- **Khi bạn dùng scanner:** nekuda xử lý URL, email, prompt hành trình, nội dung công khai của site, đầu ra tool, thông tin chẩn đoán. Cảnh báo nguyên văn: *"Do not submit a website you are not authorized to test or include personal information or secrets in a journey prompt."*

---

## 16. Đánh giá — mạnh, yếu, rủi ro

### Mạnh
1. **Số liệu tự khớp.** Ba con số trang chủ khớp tuyệt đối với API và với phép tính độc lập của tôi trên 3,78 MB dữ liệu thô. Không có số làm đẹp.
2. **API chất lượng sản phẩm thật.** OpenAPI 3.1 đầy đủ, ba mức `fields`, mã lỗi có cấu trúc, changelog ghi rõ ngày phá vỡ tương thích. Miễn phí, không khoá, CORS mở.
3. **Ba tầng file máy-đọc** (120 KB → 1 MB → 3,8 MB) cho ba mức nhu cầu — thiết kế chu đáo hiếm thấy.
4. **Ecosystem tracker trung thực.** Trích nguyên văn phản đối của WebKit và Mozilla, tự nêu rủi ro của các đối tác, phân biệt rõ "tự chạy thử" và "chỉ đọc thông cáo".
5. **Benchmark mở mã.** Apache-2.0, có transcript, tự công bố lỗi v1.0.
6. **Tự ăn món mình nấu.** webmcp.com tự chạy WebMCP; `computer.webmcp.com` là demo tham vọng thật.

### Yếu / cần biết trước
1. **Bẫy enum im lặng.** `kind=read` (giá trị đã bỏ) trả **200 + rỗng** thay vì 400 → client cũ hỏng âm thầm.
2. **833K store gây hiểu nhầm.** Chỉ **19.325 (2,3%)** có bằng chứng tool chạy; phần còn lại là "static_confirmed" từ CSV ngày 03/08/2026. Họ có ghi chú, nhưng con số 833K thì nằm chình ình ở tiêu đề.
3. **Scorecard được tài liệu hoá nhưng không công bố.** `/methodology` mô tả kỹ thang A+…C, nhưng danh bạ công khai **không hiển thị điểm nào**. Muốn có điểm phải quét và để lại email.
4. **`prominence` không có trong spec.** Danh bạ có xếp hạng biên tập ẩn (openai.com hạng 0), không phải trung lập, và không tài liệu hoá.
5. **Trang chủ nặng 4,6 MB JS** vì nhúng cả danh bạ phía client.
6. **Chậm chính hệ sinh thái mình theo dõi:** dùng polyfill `@3.0.0` trong khi bản mới nhất là `5.1.0`.
7. **`limit` bị cắt ở 500 mà không báo.**

### Rủi ro nếu phụ thuộc
1. **Xung đột lợi ích cấu trúc.** Bên vận hành danh bạ, viết benchmark, làm ecosystem tracker và bán SaaS là **cùng một công ty**. Không có cái nào sai, nhưng "WebMCP thắng 8/8 hạng đầu" là kết quả do bên bán WebMCP đo.
2. **Chuẩn chưa chốt.** Safari **phản đối**, Firefox **không làm**, Chrome mới ở origin trial với mốc 157 là *mục tiêu*. Playwright (78 triệu tải/tuần) đã từ chối. Đặt cược lớn lúc này là đặt cược sớm.
3. **Telemetry SDK bật mặc định** — nếu dùng `@nekuda/webmcp-sdk`, hãy đọc kỹ và quyết định có tắt không.
4. **Danh bạ là ảnh chụp, không phải kiểm tra sống.** `lookup` trả kết quả từ bản ghi đã lưu; tài liệu nói rõ *"this is not a live check"*.

---

## 17. Khuyến nghị theo vai

| Bạn là | Nên làm |
|---|---|
| **Muốn theo dõi hệ sinh thái WebMCP** | Đọc `/ecosystem-tracker` (cập nhật, có nguồn) và dùng `/api/v1/*`. Đây là nguồn tổng hợp tốt nhất công khai hiện có. |
| **Xây agent cần biết trang có tool không** | Gọi `/api/v1/lookup?url=…` **trước**, nhưng **đừng tin tuyệt đối** — vẫn phải kiểm `document.modelContext` tại chỗ vì đây là ảnh chụp. |
| **Chủ website muốn thử WebMCP** | Bám **spec W3C** + tài liệu Chrome for Developers. Dùng `@mcp-b/webmcp-polyfill` (211K tải/tháng) thay vì SDK nekuda (2,2K, mới Phase-1). Chạy scanner miễn phí để lấy gợi ý tool, nhưng **cân nhắc trước khi vào AgentLane**. |
| **Cần dữ liệu để phân tích** | Tải `/api/directory.json` (3,78 MB) một lần, phân tích offline. Đừng gọi 564 lần `/sites/{host}`. |
| **Đang đánh giá có nên đầu tư WebMCP** | Đọc bảng WindTunnel để hiểu **hướng**, nhưng lấy quyết định từ §11.2: **ChatGPT desktop bật mặc định** là tín hiệu thật lớn nhất; Claude/Gemini chưa đọc tool; Safari phản đối. |

---

## 18. Câu hỏi còn treo

1. **Điểm Scorecard trông thế nào trong thực tế?** Tôi dừng trước bước đăng nhập AgentLane và không để lại email, nên chưa thấy báo cáo có điểm chữ. Cần một tài khoản để biết.
2. **Giá AgentLane.** Không có trang giá công khai nào tôi tìm được; chỉ có "Schedule a call". Chưa kiểm.
3. **Ngưỡng rate limit của API.** Tài liệu nói `/platforms/shopify/stores` có giới hạn, nhưng 15 request liên tiếp đều 200. Ngưỡng thật chưa xác định.
4. **WindTunnel chưa tự chạy lại.** Mã Apache-2.0 có sẵn nhưng chạy lại 19 cấu hình × 49 task × 3 lần tốn tiền API thật. Số liệu trong §10 là **của nekuda công bố**, tôi chỉ đối chiếu nội tại (bảng khớp với công thức họ nêu).
5. **`computer.webmcp.com` khi có agent thật.** Tôi chỉ xem được vỏ vì trình duyệt không có API WebMCP. Cần Chrome origin trial hoặc ChatGPT desktop mới đánh giá được demo này.
6. **Vì sao webmcp.com dùng polyfill `3.0.0` mà không phải `5.1.0`?** Có thể là cố ý (ổn định) hoặc bỏ quên. Không có tài liệu giải thích.
7. **19.325 store Shopify "tools_live" là những store nào?** API không cho lọc theo bằng chứng, và index không có xuất hàng loạt.
