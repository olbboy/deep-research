# WebMCP & nekuda — Báo cáo tổng hợp toàn hệ sinh thái

**Ngày:** 2026-09-10 · **Tổng hợp từ 3 báo cáo** + 3 kiểm chứng bổ sung làm riêng cho bản này
**Nguồn gốc:**
- `research-260910-0148-webmcp-domain-services.md` — khảo sát 15 tên miền `webmcp.<TLD>`
- `research-260910-1126-webmcp-com-features.md` — mổ xẻ 11 khối tính năng webmcp.com
- `research-260910-1156-agentlane-app-hands-on.md` — dùng thật AgentLane trong tài khoản Leo

**Ba việc làm thêm cho bản tổng hợp này** (không có trong 3 báo cáo trước):
1. Tải và đọc mã `cdn.agentlane.com/v1/snippet.js` (41.322 byte) → **đóng được câu hỏi treo về polyfill**
2. Lấy mẫu 45 site trong danh bạ, quét dấu vết nhà cung cấp → **đo được thị phần thật của AgentLane**
3. Đọc mã `check_inverter_compatibility` + đối chiếu trang thật → **bác bỏ một phỏng đoán tôi đã nêu**

---

## 0. Đính chính trước

Lượt trước tôi đoán `check_inverter_compatibility` "khả năng cao cũng có bảng tương thích do AI tự đặt". **Sai.** Tôi đã đọc mã: nó tải `/inverter-compatibility` và **bóc chính bảng thật trên trang** — không bịa gì. Chi tiết ở §7. Việc kiểm này còn hé ra một quy luật hữu ích hơn cả kết luận ban đầu.

---

## 1. Bản đồ ba tầng

Toàn bộ những gì đã khảo sát xếp vào ba tầng. Nhầm lẫn giữa các tầng là nguồn gốc của hầu hết hiểu sai về WebMCP.

```
TẦNG 1 — CHUẨN (không ai sở hữu)
   W3C Community Group · webmachinelearning/webmcp · 3.905 ⭐
   API: document.modelContext.registerTool()
   Trạng thái: DỰ THẢO. Safari phản đối · Firefox không làm · Chrome origin trial
        │
TẦNG 2 — HẠ TẦNG CHUNG (mã nguồn mở, ai dùng cũng được)
   @mcp-b/webmcp-polyfill  →  211.351 tải/tháng   ← nơi hệ sinh thái thật chạy
   Stagehand · Vercel agent-browser · Chrome DevTools MCP · Puppeteer
        │
TẦNG 3 — SẢN PHẨM THƯƠNG MẠI (nekuda / OpenCommerce Network, Inc.)
   webmcp.com (danh bạ) · AgentLane (SaaS) · WebMCP Kit · SDK ·
   WindTunnel (benchmark) · Chrome extension · Protocol Scout
   @nekuda/webmcp-sdk → 2.196 tải/tháng          ← nhỏ hơn tầng 2 gấp 96 lần
```

**Điều quan trọng nhất rút ra khi ghép ba báo cáo:** nekuda **không sở hữu WebMCP**. Họ là người quảng bá năng nổ nhất và xây bộ công cụ thương mại quanh nó. Chuẩn thuộc W3C; hạ tầng thật là polyfill của MCP-B. Đọc sai chỗ này sẽ dẫn tới quyết định sai về mức phụ thuộc.

---

## 2. Ai là ai — dọn sạch nhầm lẫn tên miền

Từ báo cáo khảo sát 15 tên miền, chỉ 3 cái có nội dung thật, và chúng **không liên quan nhau**:

| Tên miền | Chủ | Là gì | Đáng tin? |
|---|---|---|---|
| **webmcp.com** | nekuda | Danh bạ + API + benchmark + scanner | ✅ Nghiêm túc, số liệu tự khớp |
| **webmcp.dev** | Jason McGhee (cá nhân) | Nguyên mẫu WebMCP đầu tiên, 03/2025, 820⭐ | ⚠️ Đã ngừng phát triển; chính tác giả trỏ sang W3C |
| **webmcp.xyz** | không rõ | "Registry" dựng bằng Lovable | ❌ **Dữ liệu bịa** — gắn nhãn `verified: true` cho Expedia/Stripe/Notion vốn không có WebMCP; dạy sai spec (manifest `webmcp.json` không tồn tại) |
| 12 tên còn lại | — | Parking / rao bán / bỏ hoang | — |

→ **Hệ sinh thái WebMCP hiện chỉ có đúng MỘT danh bạ đáng tin: webmcp.com.** Đây là lợi thế cạnh tranh thật của nekuda, không phải marketing.

---

## 3. Toàn bộ danh mục nekuda — 8 sản phẩm

Ghép từ báo cáo 2 (bên ngoài) và báo cáo 3 (bên trong tài khoản):

| # | Sản phẩm | Làm gì | Giá | Tôi đã kiểm |
|---|---|---|---|---|
| 1 | **webmcp.com** | Danh bạ 564 site · 3.763 tool · 833.707 store Shopify | Miễn phí | ✅ Gọi hết 10 endpoint API, phân tích 3,78 MB dữ liệu |
| 2 | **API for Agents** | 10 endpoint đọc, không khoá, CORS mở, OpenAPI 3.1 | Miễn phí | ✅ Cả ca lỗi |
| 3 | **Scanner** | Quét site → AI đề xuất tool | Miễn phí tới bước đăng nhập | ✅ Chạy 2 lần (render.com, pytesess.vn) |
| 4 | **AgentLane** | Bàn điều khiển vòng đời tool: version, phân loại, eval, drift, analytics | **Không có trang giá.** Chỉ ám chỉ *"first safe baseline is free"* | ✅ Dùng thật trong tài khoản Leo |
| 5 | **WebMCP Kit** | Plugin cho Claude Code / Codex / Cursor | Mã nguồn mở MIT · 30⭐ | ⚠️ Lấy được lệnh cài, chưa chạy |
| 6 | **@nekuda/webmcp-sdk** | SDK bọc `document.modelContext` | npm, 2.196 tải/tháng | ⚠️ Chưa chạy |
| 7 | **WindTunnel** | Benchmark 19 cấu hình × 49 task | Apache-2.0 · 43⭐ | ⚠️ Đọc bảng, **chưa tự chạy lại** |
| 8 | **Chrome extension** | "nekuda WebMCP Workbench" / "Ask nekuda" | Chrome Web Store | ❌ Chưa cài |

Kèm hai demo tự làm: `computer.webmcp.com` (máy tính trong trình duyệt, 30 tool) và `store.nekuda.ai`.

---

## 4. Sợi chỉ xuyên suốt: bậc tin cậy 3 mức

Đây là điểm nối quan trọng nhất giữa hai báo cáo. Cùng một phân loại chạy qua **toàn bộ** chồng sản phẩm, và tôi đã kiểm được từng mắt xích:

```
[1] Scanner đọc tên + mô tả + schema của tool
        ↓  SUY LUẬN, không phải site khai
[2] Gán nhãn: answer (đọc) / act (đổi trạng thái, hoàn tác được) / transact (tiền, cam kết)
        ↓
[3] webmcp.com hiển thị: Answer 44% · Action 51% · Sensitive Action 5%
        ↓
[4] AgentLane cho chủ site GHI ĐÈ nhãn (nút "Change")
        ↓
[5] Nhãn transact CHẶN eval tự chạy → "Approval required · 0 runnable · 3 gated"
```

**Bằng chứng cho mắt xích [1]–[2]:** tôi gọi `getTools()` ngay trên webmcp.com, mọi tool trả về `kind: null` — site không khai gì. Nhưng API danh bạ vẫn gán `about → act`. Vậy nhãn là **phán đoán của máy quét**.

**Vì sao điều này quan trọng với Leo:** khi bạn đọc danh bạ và thấy một site có tool `transact`, đó là **webmcp.com đoán**, không phải chủ site cam kết. Và ngược lại — nhãn `answer` không đảm bảo tool đó thật sự không có tác dụng phụ. Chính tool `calculate_storage_system` của bạn là ví dụ: nhãn `ANSWER` + `Declares read-only`, nhưng trường `Kind` ghi `action` và mã có `fetch`. Ba chỗ nói ba kiểu.

**Điểm cộng thật sự:** mắt xích [5] là thiết kế an toàn đúng chỗ — không để máy test tự bấm nút gửi form liên hệ thật của bạn.

---

## 5. Hai mô hình phân phối cạnh tranh — và số đo mới

Ghép hai báo cáo lộ ra một điều không báo cáo nào tự nói được:

| | **Mô hình chuẩn** (tự làm) | **Mô hình nekuda** (AgentLane) |
|---|---|---|
| Mã tool ở đâu | Trong repo của bạn | Trên máy chủ nekuda |
| Cài thế nào | Viết code, deploy | Dán 1 dòng `<script>` |
| Duyệt code | Qua pull request | Qua giao diện web của nekuda |
| Đổi tool | Commit + deploy | Đổi trên dashboard, có hiệu lực ngay |
| Lịch sử | Git | "Version v1" trong AgentLane |
| Rủi ro | Chậm hơn | Script bên thứ ba chạy JS tuỳ ý trên site bạn |

**Đo thật thị phần** — tôi lấy mẫu ngẫu nhiên 45 site live (không Shopify) trong chính danh bạ của nekuda và quét HTML tìm dấu vết nhà cung cấp:

| Dấu vết | Số site |
|---|---|
| `cdn.agentlane.com` | **1** (marketingmanagerjobs.com) + nekuda.ai |
| `@mcp-b` polyfill trong HTML | 0 |
| Không dấu vết (tự cài) | 42 |

*Giới hạn phép đo: tôi chỉ grep HTML thô, site nào nạp qua bundle JS sẽ lọt lưới. Nhưng snippet AgentLane vốn thiết kế để nằm trong `<head>` nên phép đo này hợp lý.*

Đối chiếu với thống kê `apiSurface` từ báo cáo 2: **spec 532 · polyfill 28 · mixed 4** — tức 94% site trong danh bạ dùng API chuẩn trực tiếp.

→ **Kết luận:** ngay trong danh bạ do chính nekuda vận hành, khách hàng AgentLane là thiểu số rất nhỏ (~2%). Tuyệt đại đa số site tự triển khai. Điều này **không có nghĩa AgentLane tệ** — nó có nghĩa là bạn đang cân nhắc một sản phẩm còn rất sớm, chứ không phải chuẩn mực ngành.

---

## 6. 🔴 Câu hỏi treo đã đóng: snippet AgentLane **không** polyfill

Báo cáo 3 để treo câu hỏi: *"Snippet có chạy được ở trình duyệt chưa có WebMCP không?"* Tôi tải mã về đọc.

`cdn.agentlane.com/v1/snippet.js` — 41.322 byte, tự chứa, chỉ gọi ra hai nơi: `api.agentlane.com` (lấy cấu hình + tool) và `ingest.agentlane.com` (telemetry). Đoạn phát hiện API:

```js
// Nếu không tìm thấy modelContext, trả về "không khả dụng" và DỪNG.
// Không tự nạp polyfill.
if (!J) return { available: false, provenance: "none" };
// Có thì ghi nhận nguồn gốc: polyfill / extension / native
provenance: ["polyfill","extension"].find(X => X === q) ?? "native"
```

**Nghĩa là:** snippet chỉ **đăng ký tool khi trình duyệt đã có sẵn** `document.modelContext` (gốc, hoặc do polyfill/extension khác cung cấp). Nó không tự tạo ra.

**Ghép với ecosystem tracker** (báo cáo 2), ta có câu trả lời thực tế cho câu hỏi *"hôm nay ai gọi được tool của tôi?"*:

| Agent | Đọc được tool của bạn? | Điều kiện |
|---|---|---|
| **ChatGPT desktop app** | ✅ **Có, mặc định bật** | Cần GPT-5.6 Sol/Terra. Không có ở Enterprise/Edu |
| **ChatGPT Work** (cloud browser) | ✅ Có | nekuda thấy trong thực tế; OpenAI chưa ghi tài liệu |
| Brave Leo | ⚠️ Có, sau cờ | Chỉ Nightly |
| Chrome + Gemini | ❌ Không | Chrome có API (origin trial) nhưng Gemini không đọc tool |
| **Claude for Chrome** | ❌ **Không** | *"Invocation works; discovery doesn't exist."* Claude Code / Cowork / Desktop dùng chung extension này |
| Perplexity Comet, Sider, Monica, HARPA | ❌ Không | Extension chưa có cách chuẩn để đọc |

→ **Tổng kết thẳng: hôm nay, cài WebMCP nghĩa là phục vụ người dùng ChatGPT desktop và ChatGPT Work. Hết.** Đó là một cược sớm có cơ sở (ChatGPT là agent lớn nhất bật mặc định), nhưng đừng kỳ vọng lưu lượng rộng trong 2026.

---

## 7. 🔑 Quy luật quan trọng nhất: khi nào AI sinh tool đáng tin

Đây là phát hiện có giá trị thực tiễn cao nhất của cả ba báo cáo, và nó **chỉ hiện ra khi so ba tool cạnh nhau**:

| Tool | Site | Cách lấy dữ liệu | Kết luận |
|---|---|---|---|
| `check_inverter_compatibility` | pytesess.vn | Tải `/inverter-compatibility`, **bóc 3 bảng HTML thật** | ✅ **Đúng** |
| `start_consultation` | blvera.com | **Trích** email, hotline, URL thật từ trang | ✅ **Đúng** |
| `calculate_storage_system` | pytesess.vn | **Tự bịa 6 hằng số** kinh doanh | ❌ **Sai** |

**Kiểm chứng `check_inverter_compatibility`** — tôi đọc mã rồi mở trang thật đối chiếu:

| Giả định trong mã | Thực tế trên `/inverter-compatibility` |
|---|---|
| 3 bảng, thứ tự low → high → 12V | ✅ Đúng 3 `<table>` |
| Nhận diện tiêu đề chứa "thấp"/"cao"/"12v" | ✅ Đúng: *Điện áp thấp · Điện áp cao · 12V* |
| Bảng 4 cột → cột 3 là mã DIP, cột 4 là giao tiếp | ✅ `Hãng \| Dòng inverter \| Mã DIP \| Giao tiếp` (33 và 15 dòng) |
| Bảng 3 cột → không có mã DIP | ✅ Bảng 12V đúng 3 cột |

Mã chạy đúng trên dữ liệu thật. **Giữ được.**

### Quy luật rút ra

> **AI đọc dữ liệu thật khi site phơi dữ liệu đó ra dạng đọc được (bảng, khối liên hệ, danh sách).
> AI bịa số khi logic của site nằm sau một biểu mẫu tương tác.**

`/calculator` của Pytes là ứng dụng JavaScript — nhập tiền điện, chọn tỉnh, chọn loại hệ thống rồi mới tính. Không có đáp án nào nằm sẵn trong HTML để bóc. Máy quét gặp bức tường đó, và thay vì báo "không làm được", nó **tự chế một công thức**:

| Hằng số bịa | Giá trị | Có trên `/calculator`? |
|---|---|---|
| Giá điện | 2.800 VNĐ/kWh **phẳng** | **0 lần** |
| Suất đầu tư pin | 8.500.000 VNĐ/kWh | **0 lần** |
| Suất đầu tư PV | 12.000.000 VNĐ/kWp | **0 lần** |
| Tiết kiệm | 75% hoá đơn | tự đặt |
| Giờ nắng | 3 vùng thô | tự đặt |
| Pin đề xuất | 70% tiêu thụ ngày | tự đặt |

Trong khi máy tính thật ghi rõ: *"dựa trên **biểu giá điện EVN hiện hành** và **dữ liệu bức xạ của chính tỉnh bạn chọn**"*, có phân biệt hộ gia đình / kinh doanh, chọn tới cấp phường–xã.

Và mã **có gọi `/calculator` nhưng vứt nội dung đi**, chỉ giữ lại URL:
```js
const { url } = await fetchHtml('/calculator');  // lấy url rồi bỏ doc
const estKwhPerMonth = bill / 2800;               // tự tính bằng hằng số riêng
```

**Áp dụng quy luật này thành quy trình duyệt:**

| Loại tool | Cách duyệt |
|---|---|
| Tra cứu / liệt kê / điều hướng | Duyệt nhanh — kiểm URL đích còn sống là đủ |
| Bóc dữ liệu có cấu trúc (bảng, danh mục) | Kiểm cấu trúc trang khớp giả định của mã; lưu ý **giòn** khi đổi layout |
| **Tính toán / báo giá / cam kết** | **Đọc từng dòng.** Nếu thấy hằng số kinh doanh trong mã → gỡ hoặc viết lại |

---

## 8. Lỗ hổng lớn nhất của cả hệ sinh thái

Ghép Scorecard (báo cáo 2) với Evaluations (báo cáo 3) lộ ra một khoảng trống mà **không sản phẩm nào trong chồng này lấp**:

| Lớp kiểm | Kiểm cái gì | Có kiểm tính ĐÚNG của số liệu không? |
|---|---|---|
| **Scorecard** của webmcp.com | Usability 60% + Coverage 20% + Quality 20%. "Quality" = vệ sinh cơ học: có mô tả thật không, có input schema không, tên có snake_case không | ❌ **Không** |
| **Tool checks** của AgentLane | *"Prove each WebMCP tool is discoverable and behaves correctly"* — tool có gọi được không, có trả về đúng hình dạng không | ❌ **Không** |
| **Journeys** | Agent hoàn thành được mục tiêu nhiều bước không | ❌ **Không** |
| **WindTunnel** | Agent giải xong task nhanh/rẻ hơn bao nhiêu | ❌ **Không** |

Cả bốn lớp đều đo **tool có chạy được không**. **Không lớp nào hỏi: con số nó trả về có đúng không.**

`calculate_storage_system` sẽ **qua sạch** mọi lớp: mô tả đầy đủ, schema chuẩn, tên snake_case, gọi được, trả về JSON đúng hình dạng, agent hoàn thành journey. Nó chỉ sai ở chỗ duy nhất không ai đo — **nội dung**.

> **Hệ quả cho bất kỳ ai dùng AgentLane:** khâu kiểm tính đúng đắn của logic nghiệp vụ **là việc của bạn**, không có công cụ nào trong chồng này gánh hộ. Đây không phải lỗi của nekuda — đó là giới hạn bản chất của việc để AI sinh code nghiệp vụ. Nhưng giao diện của họ không nói điều đó ra, và nút "Enable N tools" thì rất dễ bấm.

---

## 9. Đánh giá tổng — mạnh, yếu, rủi ro

### Mạnh (đã kiểm bằng số)
1. **Số liệu webmcp.com tự khớp tuyệt đối.** 532 site + 3.434 tool + 833K Shopify — tôi tính lại độc lập từ 3,78 MB dữ liệu thô, khớp từng con số. Không làm đẹp.
2. **API chất lượng sản phẩm thật.** OpenAPI 3.1, 3 mức `fields`, lỗi có cấu trúc, changelog ghi rõ ngày phá vỡ tương thích. Miễn phí, không khoá.
3. **Ecosystem tracker trung thực bất thường.** Trích nguyên văn phản đối của WebKit/Mozilla, tự nêu rủi ro đối tác, phân biệt "tự chạy thử" với "chỉ đọc thông cáo".
4. **Benchmark mở mã** Apache-2.0, tự công bố lỗi phiên bản trước.
5. **AgentLane giữ quyền cho chủ site:** ghi đè phân loại, tắt từng tool, xem toàn bộ mã, bỏ tick trước khi cài. Sensitive Action bị chặn eval.
6. **AI hiểu ngữ cảnh bản địa tốt.** Đọc site tiếng Việt, nhận ra ngành lưu trữ năng lượng, sinh đúng tool đặc thù, bóc đúng bảng tương thích inverter.

### Yếu
1. **Không lớp nào kiểm tính đúng của nội dung** (§8) — lỗ hổng lớn nhất.
2. **Bịa hằng số nghiệp vụ khi gặp form tương tác** (§7), phát hành thẳng ở trạng thái Live.
3. **Bẫy enum im lặng ở API:** `kind=read` (giá trị đã bỏ) trả 200 + rỗng thay vì 400 → client cũ hỏng âm thầm.
4. **833K store Shopify gây hiểu nhầm:** chỉ 19.325 (2,3%) có bằng chứng tool chạy thật.
5. **Không có trang giá ở bất kỳ đâu**, kể cả trong app sau đăng nhập.
6. **Scorecard A+…C được tài liệu hoá kỹ nhưng không hiển thị ở đâu** — không trên danh bạ, không trong AgentLane.
7. **Panel tự mâu thuẫn:** `ANSWER` + `read-only` nhưng `Kind: action` và mã có `fetch`.

### Rủi ro khi phụ thuộc
1. **Xung đột lợi ích cấu trúc.** Cùng một công ty vận hành danh bạ, viết benchmark, làm ecosystem tracker và bán SaaS. Không cái nào sai, nhưng "WebMCP thắng 8/8 hạng đầu" là do bên bán WebMCP đo.
2. **Chuẩn chưa chốt.** Safari phản đối · Firefox không làm · Playwright (78 triệu tải/tuần) từ chối · Chrome 157 mới là *mục tiêu*.
3. **Khán giả thực tế hôm nay rất hẹp** (§6): ChatGPT desktop + ChatGPT Work.
4. **Mã tool ngoài tầm kiểm soát repo** — không pull request, không git history bên bạn.
5. **Telemetry SDK bật mặc định**; kênh theo dõi đầy đủ (URL, input, output của tool) tắt mặc định nhưng bật được.

---

## 10. Khuyến nghị cho Leo — theo thứ tự làm

| # | Việc | Vì sao | Trạng thái |
|---|---|---|---|
| 1 | Gỡ `calculate_storage_system` | Số mâu thuẫn với máy tính EVN thật của chính Pytes | ✅ **Đã làm** — Live → Disabled, Live tools 5→4 |
| 2 | Giữ `check_inverter_compatibility` | Đã kiểm: bóc bảng thật, chạy đúng | ✅ Không cần làm gì |
| 3 | Giữ 3 tool tra cứu/liên hệ còn lại | Nhóm rủi ro thấp | ✅ Không cần làm gì |
| 4 | **Trước khi cài snippet:** xác nhận `contact@blvera.com` + `0889 331 133` còn dùng | `start_consultation` của blvera.com dùng hai kênh này | ⬜ Cần Leo |
| 5 | Quyết định về `calculate_storage_system` | 3 lựa chọn ở dưới | ⬜ Cần Leo |
| 6 | Đặt quy trình duyệt theo §7 cho mọi tool tương lai | Rescan có thể sinh tool mới bất cứ lúc nào | ⬜ Cần Leo |

**Ba lựa chọn cho `calculate_storage_system`, theo thứ tự tôi khuyên:**

- **(a) Để offline luôn.** Website đã có máy tính tốt hơn ở `/calculator`. Thay vào đó thêm một tool `answer` đơn giản chỉ **dẫn agent tới trang máy tính thật** — vừa đúng, vừa kéo khách về site.
- **(b) Viết lại** để gọi API thật đằng sau `/calculator` (nếu có endpoint) và trả nguyên kết quả của nó.
- **(c) Giữ nhưng thay hằng số** bằng số thật của Pytes + thêm miễn trừ rõ ràng. Rủi ro: mỗi lần Pytes đổi giá, tool lệch trở lại mà không ai biết.

**Về việc có nên cài snippet lên hai site không** — cân nhắc thẳng:

| Ủng hộ cài | Chống lại cài |
|---|---|
| ChatGPT desktop bật mặc định, là agent lớn nhất | Khán giả hôm nay chỉ có ChatGPT; Claude/Gemini chưa đọc |
| Cài 5 phút, gỡ cũng 5 phút | Script bên thứ ba chạy JS tuỳ ý trên site thương hiệu |
| Có analytics agent gọi gì — dữ liệu chưa ai khác có | Nội dung tool đổi được từ dashboard, không qua code review |
| Đi trước đối thủ ngành năng lượng VN | Chuẩn chưa chốt, Safari phản đối |

**Gợi ý:** cài lên **một site trước** (blvera.com — tool an toàn hơn), chạy 4–6 tuần, xem `Agents activity` có lưu lượng thật không rồi mới quyết cho pytesess.vn. Không mất gì nếu bỏ.

---

## 11. Trạng thái tài khoản AgentLane hiện tại

| Site | Domain ID | Tool | Snippet | Ghi chú |
|---|---|---|---|---|
| blvera.com | `dom-jnam69ld8v50` | 6 (5 Answer + 1 Sensitive Action) | ❌ Chưa cài | Có sẵn trước khi tôi vào |
| pytesess.vn | `dom-g84j5pplvmq7` | **4 Live** + 1 Disabled | ❌ Chưa cài | Tôi thêm hôm nay |

**Vì chưa cài snippet, chưa có tool nào thực sự chạy trên website.** Mọi thứ còn hoàn tác được.

---

## 12. Câu hỏi treo — đã đóng bao nhiêu

| Câu hỏi | Trạng thái |
|---|---|
| Snippet có tự polyfill không? | ✅ **ĐÓNG** — Không. Chỉ đăng ký khi trình duyệt đã có `modelContext` (§6) |
| `check_inverter_compatibility` có bịa số không? | ✅ **ĐÓNG** — Không. Bóc bảng thật, đã đối chiếu trang (§7) |
| AgentLane chiếm bao nhiêu thị phần trong danh bạ? | ✅ **ĐÓNG** — ~2% (1/45 mẫu) (§5) |
| **Giá AgentLane** | ❌ Vẫn treo. Không có trang giá ở bất kỳ đâu, kể cả sau đăng nhập |
| **Scorecard A+…C hiện ở đâu** | ❌ Vẫn treo. Không thấy trên danh bạ lẫn trong app. Có thể chỉ trong báo cáo email |
| Ngưỡng rate limit API | ❌ Vẫn treo. 15 request liên tiếp đều 200 |
| WindTunnel chạy lại | ❌ Vẫn treo. Tốn tiền API thật để tái lập 19 cấu hình × 49 task × 3 lần |
| Ai chạy "external scanner" | ❌ Vẫn treo. Scan ghi *"dispatched to external scanner"*, không rõ dịch vụ nào |
| Rescan có ghi đè tool đã sửa tay không | ❌ Vẫn treo. Có drift detection nhưng không rõ cách giải quyết xung đột — **đáng hỏi trước khi sửa tay bất kỳ tool nào** |
| Xoá website khỏi tài khoản ở đâu | ❌ Vẫn treo. Chưa tìm thấy nút; có thể trong Connection → Website settings |
| 19.325 store Shopify "tools_live" là những store nào | ❌ Vẫn treo. API không cho lọc theo bằng chứng |
