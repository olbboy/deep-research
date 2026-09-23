---
title: "Findings packet — Toàn bộ tính năng danh thiếp điện tử, cho BeShake (app) + beshake.me (web)"
generated: "2026-09-22"
timezone: "UTC+7"
tools: "runtime-web (WebSearch/WebFetch, curl, Apple iTunes API, whois, trình duyệt thật) + workflow deep-research (105 agent) + 4 agent bù lỗ hổng"
verifier_engine: "sampling (bỏ phiếu 3 verifier/claim trong workflow) + tự mở lại nguồn gốc"
---

# Findings packet — Danh thiếp điện tử: bộ tính năng đầy đủ cho BeShake

Nhật ký kiểm từng claim: [verification-log-260922-0120-beshake-digital-namecard-features.md](verification-log-260922-0120-beshake-digital-namecard-features.md)

## 0. Tóm tắt 60 giây

1. **becard.me không phải mẫu cho sản phẩm cá nhân ở Việt Nam.** Đó là Becard của công ty Áo (Behires Services GmbH, Vienna), chỉ bán cho doanh nghiệp, tối thiểu 10 giấy phép, không có gói miễn phí. Nhiều trang tính năng của họ đang "đang xây dựng" (C01–C05). Dùng Becard làm **mẫu cho gói doanh nghiệp**, không làm mẫu cho sản phẩm cá nhân.
2. **Bộ bắt buộc (ai cũng có, thường miễn phí):** hồ sơ + link + QR + tương thích NFC + người nhận xem trên web và lưu danh bạ **không cần cài app** + cập nhật tức thì. Ở các app quốc tế hướng cá nhân, **Apple/Google Wallet cũng miễn phí** (Blinq, HiHello, Mobilo, V1CE, Wave). Chỉ Becard khoá Wallet ở gói giữa (C06–C09, C17).
3. **Thứ bị khoá trả phí ở mọi nơi:** đồng bộ CRM, SSO/SCIM, quản trị đội, mẫu khoá thương hiệu, phân tích chi tiết (C16).
4. **Thị trường Việt Nam gần như chưa có app thật.** Có 11 thương hiệu bán thẻ NFC chạy trên web, bán trọn gói **99.000–350.000đ cho 3–5 năm hoặc trọn đời**. Chỉ BizMot là phần mềm thuê bao đúng nghĩa. App Việt có nhiều lượt đánh giá nhất là InCard, chỉ 131 lượt. Blinq/HiHello có hơn 131.000/44.000 lượt ở Mỹ nhưng chỉ 82/83 lượt trên App Store Việt Nam (C21, C23–C28).
5. **Đối thủ thật sự là Zalo:** 81,3 triệu người dùng/tháng, mỗi người đã có sẵn mã QR cá nhân (C30, C31). BeShake phải hơn "quét Zalo" ở chỗ: lưu thẳng vào danh bạ, thông tin nghề nghiệp, nhận chuyển khoản, quản lý khách.
6. **Chưa đối thủ Việt nào gắn QR chuyển khoản VietQR lên danh thiếp.** Đây là khoảng trống khác biệt rẻ để làm (C29, C52).
7. **Pháp lý đã đổi:** Nghị định 13/2023 hết hiệu lực. Nay áp dụng **Luật Bảo vệ dữ liệu cá nhân 91/2025/QH15** (hiệu lực 01/01/2026). Hoá đơn điện tử theo **Nghị định 254/2026** (hiệu lực 01/07/2026) (C44–C51).
8. **Việc làm ngay:** `beshake.me` hiện **chưa ai đăng ký** (whois 21/09/2026). `beshake.com` đã có chủ. Tên "BeShake" trùng họ tên sản phẩm "be…" của Be Group (app "be" có 531.895 lượt đánh giá ở Việt Nam), nên cần kiểm nhãn hiệu (C55–C57).

---

## 1. Objective và phạm vi

- **Câu hỏi chủ:** một danh thiếp điện tử đầy đủ gồm những tính năng nào? Cái nào bắt buộc, cái nào tạo khác biệt, cái nào nằm ở gói trả phí hay gói doanh nghiệp? Mục đích: làm app **BeShake** (iOS + Android) và web **beshake.me**, thị trường Việt Nam, phục vụ cả cá nhân lẫn doanh nghiệp.
- **Thị trường:** Việt Nam là chính; quốc tế dùng làm tham chiếu.
- **Thời điểm cắt:** 22/09/2026, 01:20 (UTC+7).
- **Cách làm:**
  - Workflow `deep-research`: 5 góc tìm kiếm, 23 nguồn, 110 claim. Kiểm 25 claim bằng 3 verifier mỗi claim: 17 giữ, 8 bác.
  - 4 agent bù lỗ hổng: kỹ thuật, pháp lý Việt Nam, bảng tính năng quốc tế, đối thủ Việt Nam.
  - Tôi tự mở lại các claim có tác động lớn: trình duyệt thật trên becard.uk, Apple iTunes API, whois, Công báo, tài liệu Apple/Google.
- **Quy ước thẻ tin cậy trong packet này:**
  - `[CONFIRMED]`: tôi tự mở nguồn gốc có thẩm quyền, **và** có thêm một lần kiểm độc lập (verifier khác hoặc nguồn khác).
  - `[HIGH CONFIDENCE]`: một lần mở nguồn gốc (của agent hoặc của tôi).
  - `[ASSESSED]`: tổng hợp hoặc suy luận từ nhiều dữ kiện.
  - `[LOW CONFIDENCE]`: chỉ qua kết quả tìm kiếm hoặc nguồn thứ cấp.
  - `[BLIND SPOT]`: chưa kiểm.

## 2. Từ điển (định nghĩa một lần, sau đó dùng lời thường)

| Từ | Nghĩa |
|---|---|
| **NFC** | Sóng tầm rất gần (vài cm). Chạm thẻ vào điện thoại là điện thoại đọc được link. |
| **Thẻ NFC / chip NTAG** | Thẻ nhựa có chip nhỏ. NTAG213/215/216 chứa được 144/504/888 byte. |
| **QR** | Mã vuông để camera quét. "QR trực tuyến" chứa link; "QR ngoại tuyến" chứa luôn thông tin liên hệ, không cần mạng. |
| **vCard (.vcf)** | Định dạng chuẩn của "một mục danh bạ". Bấm vào là điện thoại hỏi "Lưu liên hệ?". |
| **Wallet pass** | "Tấm thẻ" nằm trong ví Apple Wallet / Google Wallet, mở nhanh từ màn hình khoá. |
| **App Clip** | Bản app thu nhỏ của iPhone, chạy ngay khi quét/chạm mà không cần cài app đầy đủ. |
| **Universal link** | Link web thường (https://beshake.me/...). App đã cài thì mở app, chưa cài thì mở web. |
| **Lead capture / trao đổi ngược** | Người nhận điền lại tên, số điện thoại của họ cho chủ thẻ. |
| **CRM** | Phần mềm quản lý khách hàng của doanh nghiệp (HubSpot, Salesforce…). |
| **SSO** | Đăng nhập bằng tài khoản công ty (Microsoft, Google), không tạo mật khẩu riêng. |
| **SCIM** | Tự động tạo hoặc khoá tài khoản khi phòng nhân sự thêm hoặc cho nghỉ nhân viên. |
| **OCR** | Máy đọc chữ từ ảnh chụp danh thiếp giấy. |
| **Seat / giấy phép** | Đơn vị tính tiền theo đầu người dùng. |
| **Gói F / P / T / E** | Miễn phí / Pro cá nhân / Team / Enterprise. |
| **IAP** | Thanh toán trong app qua Apple/Google. Họ thu hoa hồng 15–30%. |
| **VietQR** | Chuẩn QR chuyển khoản liên ngân hàng của NAPAS. |
| **Bên kiểm soát dữ liệu** | Bên quyết định mục đích và phương tiện xử lý dữ liệu cá nhân (Điều 2, Luật 91/2025). |

## 3. Dàn nhân vật (kịch bản minh hoạ — tên và số trong kịch bản là giả định, không phải dữ liệu)

| Nhân vật | Vai | Điện thoại | Điều họ cần |
|---|---|---|---|
| **Chị Lan**, 34 tuổi | Môi giới bất động sản ở Thủ Đức, gặp khách hằng ngày ở dự án | iPhone 15 | Đưa thông tin trong 3 giây, biết ai đã lưu mình, nhớ ai là ai |
| **Anh Tuấn** | Khách của chị Lan | Samsung Android đời 2021, chỉ dùng Zalo | Không muốn cài app lạ |
| **Anh Minh** | Trưởng phòng kinh doanh công ty phân phối thiết bị y tế, 40 nhân viên sales | — | Cả đội dùng một mẫu logo; nhân viên nghỉ thì khoá thẻ; lead đi thẳng vào CRM; có hoá đơn VAT |
| **Chị Mai** | Chủ tiệm bánh ở Đà Nẵng, bán qua Facebook/Zalo | Android | Khách quét là chuyển khoản được luôn |
| **Hà** | Nhân viên vận hành BeShake | — | Xử lý thẻ hỏng, gia hạn, hoá đơn, yêu cầu xoá dữ liệu |

---

## 4. Becard (becard.me) thật ra là gì — tự kiểm trên trình duyệt

| Điều thấy | Căn cứ |
|---|---|
| `becard.me` chuyển 302 sang `becard.uk`. Chủ là **Behires Services GmbH**, Vienna, Áo. Domain `.me` đăng ký 16/10/2019 | C01 |
| Có 3 gói **Business 1,19 € · Teams 1,96 € · Enterprise 2,76 €** mỗi người dùng/tháng (1–10 người, trả năm). **Tối thiểu 10 giấy phép.** Không có gói miễn phí, dùng thử 14 ngày. Không bán đứt. Không giảm giá cho giáo dục hay phi lợi nhuận | C02 |
| Tên miền riêng 15 €/tháng; hợp đồng dữ liệu riêng 250 € (miễn phí từ 500 người dùng) | C02 |
| Gói Business rẻ nhất **không có** Wallet, thống kê, khoá PIN, hình nền họp, thu thập liên hệ, quét danh thiếp giấy. Các thứ này mở từ gói Teams. SSO SAML và Microsoft Entra cũng mở từ Teams | C03 |
| Chỉ gói Enterprise có: đa ngôn ngữ, đính kèm file, email chào nhân viên mới, hỗ trợ qua điện thoại. Chữ ký email ghi "có từ mùa đông 2026", tức là **chưa có** | C03 |
| Các trang NFC, thu thập liên hệ, quét danh thiếp giấy, chữ ký email báo "đang xây dựng". Trang tài liệu API `docs.becard.me` trả **404** | C04 |
| App iOS phát hành 11/02/2025, **2 lượt đánh giá** (App Store Áo). Mô tả app ghi rõ không dành cho người dùng cá nhân | C05 |

**Nên học gì từ Becard:** cách chia 3 gói doanh nghiệp, mô hình "Spaces" (nhóm thẻ theo chi nhánh), QR ngoại tuyến có ở mọi gói, SSO đặt ở gói giữa, hợp đồng dữ liệu là dịch vụ tính phí. **Không nên học:** bắt tối thiểu 10 giấy phép (loại luôn cá nhân và hộ kinh doanh), quảng cáo tính năng chưa có.

---

## 5. Bản đồ đối thủ

### 5.1 Quốc tế — giá (USD/tháng trừ khi ghi khác)

| Vendor | Miễn phí có gì | Cá nhân trả phí | Team / DN | Thẻ NFC rẻ nhất | Thẻ |
|---|---|---|---|---|---|
| Blinq | 2 thẻ, Wallet, chữ ký email cá nhân, hình nền họp | $9,99 ($7,33 nếu trả năm) | $6,99/người ($4,99 trả năm); Enterprise có SSO, SCIM, SOC 2 | $14,99 sticker / $19,99 thẻ | C06 `[CONFIRMED]` |
| HiHello | 4 thẻ, 5 lượt quét danh thiếp/tháng | $6 hoặc $72/năm | $5/người, 5–100 người | Không bán, khách tự mua thẻ | C07 |
| Mobilo | Thẻ số miễn phí | $3 | $4–$5/người | $5 | C08 |
| Wave | Có cả **form thu liên hệ** và Wallet | $7 | $5/người | chưa kiểm | C09 |
| Haystack | **Quét danh thiếp AI không giới hạn** | $4,50/người trả năm | $2,50/người (từ 10 người) | Không bán | C10 |
| Uniqode | 1 thẻ | — | $6/người, chỉ trả năm | Không bán | C11 |
| V1CE | Có (trang riêng, chưa tự mở) | £49 | chưa rõ | £60, mua một lần | C12 |
| Tapni | ? | Thẻ $29,90 mua một lần | $59,90/người/năm | $29,90 | C13 |
| Popl | Không công bố giá | — | — | — | C14 |
| Linq | ? | $29/người (chỉ qua search) | — | ? | C15 `[LOW]` |

**Khoảng giá quốc tế:** cá nhân **$3–$10/tháng**; team **$2,50–$6,99/người/tháng**; thẻ NFC **$5–$30** (kim loại cao hơn).

### 5.2 Việt Nam

| Tên | Mô hình | Giá | Điểm đáng chú ý | Thẻ |
|---|---|---|---|---|
| ecard.vn (VSTAR GROUP) | Trọn gói | Chỉ hồ sơ online **185.000đ/3 năm**; kèm thẻ NFC **285.000đ/3 năm** | "không cần cài đặt ứng dụng", nút Zalo, thống kê truy cập | C23 `[CONFIRMED]` |
| vcard.vn (cùng chủ ecard) | Miễn phí + trọn gói | Plus 285.000đ/5 năm; Pro từ 500.000đ/năm | Đa ngôn ngữ, cộng tác viên hoa hồng đến 50% | C25 |
| ncv.vn | Bán thẻ | 120.000–230.000đ/thẻ | Nút Zalo, **xuất hoá đơn VAT**, cộng tác viên 45% | C26 |
| gud.vn | Bán sản phẩm | 150.000–350.000đ | Mở rộng sang "menu QR" cho quán ăn | C26 |
| icardpro.vn | Bán đứt | 200.000–300.000đ/thẻ, **dùng vĩnh viễn** | Chiết khấu sỉ 5–15% | C26 |
| mycard.asia | Bán thẻ | 99.000đ | Cộng tác viên 30–50%; tự nhận có cả ERP/CRM (chưa kiểm) | C26 |
| mksmart.com.vn (MK Group) | Doanh nghiệp lớn | Báo giá riêng | Có năng lực sản xuất thẻ chip | C26 |
| **bizmot.com** | **Thuê bao phần mềm** | Miễn phí; 199.000–249.000đ/tháng; nhóm 59.000–99.000đ/người/tháng (từ 5 người) | Thu thập liên hệ, CRM, phân tích — **thuê bao đúng nghĩa duy nhất** | C27 |
| nfccard.vn, proid.vn, xanhlenvn.com | Web bán thẻ | chưa kiểm | Quy mô nhỏ | C26 |
| App Việt trên App Store | App | Miễn phí | InCard (INAPPS) 4,89★/**131** lượt; MeU 7 lượt; EnsCard 1 lượt | C28 |

**Mô hình chiếm ưu thế ở Việt Nam:** bán **thẻ + hồ sơ trọn gói 99.000–350.000đ** cho 3–5 năm hoặc trọn đời, phân phối qua cộng tác viên ăn hoa hồng 30–50%. Thuê bao hằng tháng là ngoại lệ (C26, C27).

### 5.3 Tín hiệu mức dùng app (số lượt đánh giá trên App Store, 22/09/2026)

| App | Ở Mỹ | Ở Việt Nam |
|---|---|---|
| Blinq | 131.424 | **82** |
| HiHello | 44.268 | **83** |
| Popl | 102.289 | **47** |
| Linq | 12.288 | **3** |
| InCard (app Việt) | — | **131** |

Diễn giải `[ASSESSED]`: người Việt gần như chưa dùng app danh thiếp. Số lượt đánh giá chỉ là chỉ báo gián tiếp, không phải số người dùng (C20, C21).

---

## 6. Danh mục tính năng đầy đủ

Ký hiệu cột "Ai có": vendor và **gói thấp nhất** có tính năng đó (F/P/T/E). Cột "BeShake": **MVP** (bản đầu, miễn phí) · **Pro** (cá nhân trả phí) · **DN** (gói doanh nghiệp) · **Sau** (để sau) · **Không**.

### A. Hồ sơ và thẻ

| # | Tính năng | Ai có | BeShake | Căn cứ |
|---|---|---|---|---|
| 1 | Tên, chức danh, công ty, ảnh, logo | Mọi vendor, F | MVP | C06–C13, C23 |
| 2 | Nhiều số điện thoại, email, địa chỉ + bản đồ | Phổ biến | MVP | C03 |
| 3 | Nút mạng xã hội, website (Facebook, TikTok, LinkedIn…) | F ở 7/9 vendor quốc tế; ecard.vn | MVP | C18, C23 |
| 4 | Nhiều thẻ cho một người (công việc / cá nhân) | Blinq F2→P5; HiHello F4→P16; Haystack F không giới hạn; Becard "Spaces" | MVP 2 thẻ, Pro nhiều hơn | C06, C07, C10 |
| 5 | Video YouTube/Vimeo, file PDF (catalogue, bảng giá) | Becard Teams (video), Enterprise (file) | Pro | C03 |
| 6 | Tuỳ biến màu, mẫu giao diện | Cơ bản F (HiHello, Becard); nâng cao P (Blinq, Mobilo, Wave) | MVP cơ bản, Pro nâng cao | C03, C18 |
| 7 | Bỏ nhãn BeShake / tên miền riêng | Becard add-on 15 €/tháng; Mobilo Business | DN | C02, C08 |
| 8 | Song ngữ Việt–Anh trên cùng thẻ | Becard Enterprise; vcard.vn | Pro | C03, C25 |
| 9 | Ẩn/hiện từng trường; khoá thẻ bằng PIN | vcard.vn (ẩn/hiện); Becard Teams (PIN) | MVP ẩn/hiện, Pro PIN | C03, C25 |
| 10 | Tên tiếng Việt lưu đúng thứ tự Họ–Đệm–Tên trong danh bạ | Chưa vendor nào nói tới — yêu cầu kỹ thuật | MVP (bắt buộc) | C41 |

### B. Kênh chia sẻ

| # | Tính năng | Ai có | BeShake | Căn cứ |
|---|---|---|---|---|
| 11 | Link cá nhân `beshake.me/<tên>` | Mọi vendor, F | MVP | C06–C13 |
| 12 | QR trực tuyến | Mọi vendor, F | MVP | C06–C13 |
| 13 | **QR ngoại tuyến** (chứa luôn vCard, không cần mạng) | Becard mọi gói; EnsCard | MVP — hơn các đối thủ Việt chỉ có web | C03, C28 |
| 14 | NFC: thẻ hoặc sticker ghi link | Hầu hết; HiHello để khách tự mua thẻ; Uniqode/Haystack chỉ có QR | MVP tương thích; bán thẻ hay không → Q2 | C33, C36 |
| 15 | Apple Wallet / Google Wallet | **F** ở Blinq, HiHello, Mobilo, V1CE, Wave; Becard Teams | MVP — chưa đối thủ Việt nào công bố | C17, C37, C38 |
| 16 | Widget màn hình chính / màn hình khoá | HiHello F; app Becard; MK Widget Card (Việt) | MVP (app) | C05, C28 |
| 17 | Gửi qua Zalo, SMS, email, Messenger | ecard.vn (Zalo); Blinq/HiHello (SMS, email) | MVP | C23 |
| 18 | Chữ ký email | Blinq F cá nhân; Mobilo, V1CE F; Becard chưa có | Pro | C03, C06 |
| 19 | Hình nền họp video (Zoom/Teams/Meet) | Blinq F; Becard Teams | Pro | C03, C06 |
| 20 | Apple Watch | Chưa kiểm | Sau | `[BLIND SPOT]` |
| 21 | Chạm điện thoại vào điện thoại | iPhone không cho app bên thứ ba làm; NameDrop chỉ dành cho danh bạ của Apple | **Không** | C35, C43 |
| 22 | App Clip (iPhone) | Giới hạn 15 MB khi mở bằng NFC/QR | Sau (web đã đủ) | C39 |
| 23 | Google Play Instant (Android) | Khai tử từ 12/2025 | **Không** | C40 |

### C. Trải nghiệm người nhận (anh Tuấn)

| # | Tính năng | Ai có | BeShake | Căn cứ |
|---|---|---|---|---|
| 24 | Xem trên trình duyệt, **không cần cài app** | Mọi vendor; ecard.vn lấy làm điểm bán chính | MVP (bắt buộc) | C23, C28 |
| 25 | Nút "Lưu vào danh bạ" (vCard 4.0, có bản 3.0 dự phòng) | Mọi vendor | MVP | C41, C42 |
| 26 | **Không bật cửa sổ ép tải app** | Popl bị phàn nàn vì làm vậy | Nguyên tắc MVP | C22 |
| 27 | Hiển thị đúng trên Android và trình duyệt cũ | HiHello bị phàn nàn lỗi hiển thị | Kiểm thử MVP | C22 |

### D. Nhận liên hệ ngược và quản lý danh bạ

| # | Tính năng | Ai có | BeShake | Căn cứ |
|---|---|---|---|---|
| 28 | Form trao đổi liên hệ hai chiều | **F** ở Wave, Mobilo, V1CE (cơ bản); T ở Blinq, HiHello, Uniqode; Becard Teams; BizMot | MVP, kèm ô đồng ý riêng → Q4 | C18, C46 |
| 29 | Quét danh thiếp giấy (OCR/AI) | HiHello F 5 lượt/tháng; Haystack F không giới hạn; Blinq P; Becard Teams | Miễn phí có hạn mức, Pro nhiều hơn | C07, C10 |
| 30 | Quét thẻ đeo ở sự kiện, hội chợ | Blinq E; HiHello T/E; Popl | DN | C18 |
| 31 | Ghi chú, gắn nhãn, nhắc gọi lại | Blinq P (AI ghi chú); V1CE T; app Becard | Pro | C05, C18 |
| 32 | Xuất CSV / đồng bộ danh bạ điện thoại | Becard Teams; Popl bị chê vì **bỏ** xuất CSV | MVP — và không rút lại về sau | C22 |
| 33 | AI: làm giàu thông tin, soạn email chăm sóc, ghi âm cuộc gặp | Blinq P, HiHello T, Mobilo P, V1CE T, InCard | Pro | C18, C28 |

### E. Phân tích

| # | Tính năng | Ai có | BeShake | Căn cứ |
|---|---|---|---|---|
| 34 | Tổng lượt xem | Mobilo F; V1CE F cơ bản; ecard.vn "thống kê truy cập" | MVP | C18, C23 |
| 35 | Nguồn truy cập (QR/NFC/link), lượt lưu, lượt bấm, theo ngày/tuần | Blinq P, HiHello P, Wave P; Becard Teams | Pro | C03, C18 |
| 36 | Phân tích cả đội, phễu khách (mới → đã liên hệ → chốt) | NFC.cool; Becard; Blinq | DN | C16 |

### F. Doanh nghiệp (anh Minh)

| # | Tính năng | Ai có | BeShake | Căn cứ |
|---|---|---|---|---|
| 37 | Bảng quản trị tập trung | Becard mọi gói; Blinq/HiHello/Mobilo T | DN | C03, C16 |
| 38 | Mẫu khoá theo thương hiệu (nhân viên không sửa được logo, màu) | Blinq T, Mobilo Business, Wave T, Uniqode T | DN | C18 |
| 39 | Tạo hàng loạt từ danh sách Excel | Becard "directories" | DN | C03 (chi tiết `[BLIND SPOT]`) |
| 40 | Nhân viên nghỉ việc → khoá hoặc chuyển thẻ NFC | Mobilo T | DN | C18 |
| 41 | Phân quyền | Becard mọi gói; Haystack P | DN | C03 |
| 42 | Đăng nhập bằng tài khoản công ty (Microsoft Entra, Google) | Becard Teams; Blinq T; Mobilo Business | DN | C03, C16 |
| 43 | SCIM tự cấp/thu hồi tài khoản | Blinq E, HiHello E, Uniqode Business+, Tapni E | Sau (DN lớn) | C16 |
| 44 | Tích hợp CRM (HubSpot, Salesforce, Dynamics) | Blinq T, HiHello T, Kado; Becard Enterprise ("hạn chế") | DN | C16 |
| 45 | Zapier / API / webhook | Blinq T; Mobilo F (Zapier); Becard "theo yêu cầu" (tài liệu 404) | DN | C04, C18 |
| 46 | Danh bạ công ty dùng chung | Becard Teams | DN | C03 |
| 47 | Nhóm theo chi nhánh / phòng ban | Becard "Spaces" | DN | C03 |
| 48 | **Hoá đơn VAT điện tử** | ncv.vn | DN (bắt buộc ở VN) | C26, C51 |
| 49 | Hợp đồng xử lý dữ liệu cho khách doanh nghiệp | Becard (riêng 250 €) | DN | C02, C46 |

### G. Phần cứng NFC

| # | Tính năng | Ai có | BeShake | Căn cứ |
|---|---|---|---|---|
| 50 | Thẻ nhựa / gỗ / kim loại | Mobilo $5–$20; Blinq $19,99; Tapni $29,90; V1CE £60; Việt Nam 99.000–350.000đ trọn gói | → Q2 | C08, C12, C13, C26 |
| 51 | Sticker NFC dán lưng điện thoại | Blinq $14,99; gud.vn | → Q2 | C06, C26 |
| 52 | In logo doanh nghiệp theo lô | MK Smart; iCardPro chiết khấu 5–15% | DN | C26 |
| 53 | Khoá ghi thẻ bằng mật khẩu (chống bị ghi đè link) | Có sẵn trên chip NTAG | Bắt buộc nếu bán thẻ | C36 |
| 54 | Chọn chip: NTAG213 đủ cho link; 215/216 mới chứa được vCard | Kỹ thuật | Bắt buộc nếu bán thẻ | C36 |

### H. Bảo mật, quyền riêng tư, tuân thủ

| # | Tính năng | Căn cứ pháp lý / thị trường | BeShake | Căn cứ |
|---|---|---|---|---|
| 55 | Xin đồng ý **riêng cho từng mục đích** khi người nhận để lại thông tin, hoặc khi quét danh thiếp giấy | Điều 9, Luật 91/2025 | MVP (bắt buộc) | C46 |
| 56 | Hồ sơ đánh giá tác động xử lý dữ liệu trong 60 ngày kể từ ngày đầu xử lý | Điều 21 | Trước khi ra mắt | C46 |
| 57 | Nơi lưu dữ liệu (trong hay ngoài Việt Nam) | Điều 20; chuyển ra nước ngoài trái phép bị phạt tới 5% doanh thu năm trước | → Q3 | C47 |
| 58 | Tự xoá tài khoản và dữ liệu | Quyền của chủ thể dữ liệu; yêu cầu của App Store (chưa kiểm trong phiên này) | MVP | `[BLIND SPOT]` |
| 59 | SOC 2 / ISO 27001 | Blinq, HiHello tự công bố SOC 2; Becard lưu dữ liệu trên hạ tầng đạt ISO 27001 | Sau (khi bán DN lớn) | C19 |

### I. Đặc thù Việt Nam

| # | Tính năng | Ai có | BeShake | Căn cứ |
|---|---|---|---|---|
| 60 | Nút Zalo (`zalo.me/<sđt>`) + nút "Sao chép số" dự phòng | ecard.vn, ncv.vn | MVP | C29, C53 |
| 61 | **QR chuyển khoản VietQR trên thẻ** | Chưa thấy đối thủ Việt nào | MVP — điểm khác biệt | C29, C52 |
| 62 | Link Shopee / TikTok Shop / Facebook Page | ecard.vn có TikTok | MVP (nằm trong #3) | C23 |
| 63 | Thanh toán: IAP cho gói cá nhân; chuyển khoản/VietQR cho thẻ vật lý và gói DN | Apple 3.1.1 / 3.1.3(c)(e); Google Play | MVP | C49, C50 |
| 64 | Kênh cộng tác viên ăn hoa hồng | vcard.vn, ncv.vn, mycard.asia | Quyết định kênh bán, không phải tính năng | C26 |

### J. Vận hành (Hà)

| # | Tính năng | Ai có / bài học | BeShake | Căn cứ |
|---|---|---|---|---|
| 65 | Huỷ gói dễ; báo rõ trước khi gia hạn | Linq: 5/50 review than không huỷ được; Blinq: 3/50 than bị trừ tiền bất ngờ | MVP (nguyên tắc) | C22 |
| 66 | Không rút tính năng miễn phí sau khi đã cho | Popl bị chê "keep taking features away" | Nguyên tắc | C22 |
| 67 | Trang trạng thái hệ thống | Becard `status.becard.me` | Sau | C01 |

---

## 7. Ràng buộc kỹ thuật — kể bằng tình huống

- **Chị Lan chạm thẻ vào iPhone của khách.** Điện thoại đọc nền không cần mở app, nhưng chỉ từ **iPhone XS trở lên**. Thẻ phải chứa link web thật (`https://beshake.me/...`). Kiểu `beshake://` thì iPhone im lặng, không báo gì (C33).
- **Khách đang mở Camera hoặc Apple Pay đúng lúc chạm**, hoặc máy bật chế độ máy bay, hoặc máy chưa mở khoá lần nào từ khi khởi động lại: thẻ **không được đọc**. → Mặt thẻ vật lý **luôn in thêm QR** (C33).
- **Anh Tuấn dùng Android:** máy chỉ đọc NFC khi màn hình đã mở khoá **và** NFC đang bật trong Cài đặt (C34). Android không còn "app chạy tức thì" vì Google Play Instant đã khai tử từ 12/2025. Người dùng Android chỉ còn đường web (C40).
- **Chị Lan muốn chạm iPhone của mình vào iPhone của khách như chạm thẻ:** không làm được. iPhone không cho app bên thứ ba giả làm thẻ NFC. NameDrop là tính năng riêng của danh bạ Apple (C35, C43).
- **Thẻ in sẵn:** NTAG213 có 144 byte, đủ cho một link ngắn. Muốn thẻ tự chứa cả danh bạ tiếng Việt có dấu thì cần NTAG215/216 (504/888 byte). Chip có khoá mật khẩu 32-bit để chống người khác ghi đè link (C36).
- **Tên "Nguyễn Thị Lan" lưu vào danh bạ:** dùng vCard 4.0 (mặc định UTF-8, không lỗi dấu). Ghép trường N theo thứ tự Họ=Nguyễn, Đệm=Thị, Tên=Lan; trường FN hiển thị đầy đủ "Nguyễn Thị Lan" (C41). Với máy cũ chỉ đọc vCard 3.0, phải khai báo mã hoá UTF-8 thủ công `[LOW]` (C42).
- **Thẻ trong Apple Wallet:** cần tài khoản Apple Developer, mã "Pass Type ID" và chứng chỉ ký. Thẻ tự cập nhật khi chị Lan đổi chức danh (máy chủ gửi thông báo đẩy). Trên thẻ hiển thị được QR (C37). Google Wallet: tài khoản phát hành mới ở **chế độ thử**, phải xin quyền phát hành, nên nộp sớm (C38).
- **App Clip:** tối đa 15 MB nếu mở bằng NFC/QR. Mức 100 MB chỉ dành cho App Clip mở từ web hoặc ô tìm kiếm Spotlight (C39).

## 8. Pháp lý và thanh toán ở Việt Nam

| Chủ đề | Nội dung | Hệ quả cho BeShake | Căn cứ |
|---|---|---|---|
| Luật nền | Luật Bảo vệ dữ liệu cá nhân **91/2025/QH15**, ban hành 26/06/2025, hiệu lực 01/01/2026. Nghị định hướng dẫn 356/2025 `[LOW]`. Nghị định 13/2023 hết hiệu lực `[LOW]` | Dùng bộ luật mới làm chuẩn, không dẫn Nghị định 13/2023 | C44, C45 |
| Đồng ý | Tự nguyện, rõ ràng, **riêng cho từng mục đích** (Điều 9) | Form trao đổi ngược và quét danh thiếp giấy cần ô đồng ý riêng, không đánh dấu sẵn | C46 |
| Đánh giá tác động | Lập hồ sơ trong 60 ngày kể từ ngày đầu xử lý (Điều 21). Chuyển dữ liệu ra nước ngoài thì thêm hồ sơ riêng, gửi cơ quan chuyên trách (Điều 20) | Server đặt ở nước ngoài làm tăng thủ tục và rủi ro phạt | C46, C47 |
| Phạt | Chuyển dữ liệu ra nước ngoài trái phép: tới **5% doanh thu năm trước** (tối thiểu 3 tỷ đồng). Vi phạm khác: tối đa 3 tỷ đồng | — | C47 |
| Miễn trừ | Doanh nghiệp nhỏ/khởi nghiệp được miễn một số nghĩa vụ, **trừ** khi kinh doanh dịch vụ xử lý dữ liệu cá nhân `[LOW]` | BeShake có thể **không** thuộc diện miễn → cần luật sư xác nhận | C48 |
| Ai kiểm soát dữ liệu của anh Tuấn | Luật chưa nói rõ trường hợp app trung gian. Có thể BeShake và chị Lan **cùng** là bên kiểm soát | Ghi rõ vai trò trong điều khoản sử dụng; cần luật sư | `[BLIND SPOT]` |
| Thu tiền trong app | Gói số cho cá nhân **bắt buộc** qua IAP (Apple 3.1.1), hoa hồng 15% nếu doanh thu dưới 1 triệu USD/năm. Thẻ vật lý **không** qua IAP (3.1.3(e)). Bán trực tiếp cho tổ chức được ngoài IAP (3.1.3(c)). Google Play miễn cho hàng vật lý | Gói Pro cá nhân mất 15–30%. Thẻ NFC và gói DN thu trực tiếp | C49, C50 |
| Hoá đơn | **Nghị định 254/2026**: ban hành 30/06/2026, hiệu lực 01/07/2026, thay Nghị định 123/2020 | Luồng thanh toán gói DN phải xuất hoá đơn điện tử theo Nghị định 254 | C51 |
| VietQR | Chuẩn của NAPAS; `vietqr.io` là của Công ty CASSO (bên thứ ba), có API | Tự sinh QR chuyển khoản theo chuẩn mở. Chưa kiểm được có cần giấy phép riêng không `[LOW]` | C52 |
| Zalo | Mỗi người dùng có mã QR riêng (trang hướng dẫn chính thức). Link `zalo.me/<sđt>` dùng phổ biến nhưng không thấy tài liệu chính thức cam kết | Luôn có nút "Sao chép số" dự phòng | C31, C53 |

## 9. Phản biện — vì sao BeShake có thể thất bại

1. **"Tôi quét Zalo là xong."** Zalo có 81,3 triệu người dùng/tháng, ai cũng có sẵn mã QR (C30, C31). Nếu BeShake chỉ làm "một trang thông tin có QR" thì không ai đổi thói quen. → Phải cho thứ Zalo không có: lưu đúng vào danh bạ điện thoại, thông tin nghề nghiệp, nhận chuyển khoản, danh sách ai đã gặp, dùng cho cả đội.
2. **Người Việt còn nghi ngờ NFC.** Một bài hỏi trên cộng đồng Tinh Tế (2026) đặt câu "có thật không" về thẻ chạm (C32 `[LOW]`, một giai thoại). App quốc tế chỉ có vài chục lượt đánh giá ở Việt Nam (C21). → QR là kênh chính, NFC là "điểm cộng".
3. **Thị trường cá nhân đang đua giá rẻ và bán qua cộng tác viên.** 99.000–350.000đ cho 3–5 năm, hoa hồng 30–50% (C26). Nếu BeShake bán thuê bao hằng tháng cho cá nhân thì vừa đắt hơn mặt bằng, vừa mất 15–30% cho Apple/Google (C49).
4. **Những lỗi làm app quốc tế bị ghét** (50 review mới nhất mỗi app, C22):
   - Trừ tiền bất ngờ, khó huỷ gói (Linq 5/50, Blinq 3/50).
   - Ép người nhận tải app (Popl 3/50).
   - Rút dần tính năng miễn phí (Popl).
   - QR lỗi đúng lúc đang ở sự kiện (Blinq).
5. **Rủi ro tên:** Be Group đặt tên sản phẩm kiểu "be" + từ (beBike, beCar, beFood…). App "be" có 531.895 lượt đánh giá ở Việt Nam. "BeShake" có thể bị cho là cùng họ, hoặc bị phản đối khi đăng ký nhãn hiệu (C57, `[BLIND SPOT]` về pháp lý nhãn hiệu).

## 10. Đề xuất phân tầng cho BeShake — kể bằng tình huống

### MVP miễn phí (app + web) — "sáng thứ Hai chị Lan gặp anh Tuấn"
Chị Lan mở widget trên màn hình khoá. Anh Tuấn quét QR bằng camera Android. Trình duyệt mở `beshake.me/lan-nguyen`, không có cửa sổ ép cài app. Trang có ảnh, chức danh, nút **Zalo**, nút **Gọi**, nút **Lưu danh bạ**. Anh Tuấn bấm lưu, danh bạ hiện đúng "Nguyễn Thị Lan". Anh điền số điện thoại vào form "Gửi lại thông tin của bạn", có ô đồng ý riêng. Tối đó chị Lan thấy "3 người xem, 1 người để lại số".
**Gồm:** tính năng #1–4, 6, 9–17, 24–28, 32, 34, 55, 58, 60–63, 65–66.

### Pro cá nhân — "hai tuần sau, chị Lan đi sự kiện mở bán"
Chị chụp 30 danh thiếp giấy, máy tự đọc thành danh bạ. Chị xem được bao nhiêu người đến từ QR ở quầy, bao nhiêu từ link Zalo. Chị gắn nhãn "khách nóng" và đặt nhắc gọi lại. Chị dùng thêm thẻ tiếng Anh cho khách nước ngoài, và chữ ký email có QR.
**Gồm:** #5, 8, 18–19, 29 (vượt hạn mức), 31, 33, 35.

### Gói doanh nghiệp — "anh Minh trang bị cho 40 nhân viên trước hội chợ"
Hà nhập danh sách Excel 40 người. Mọi thẻ dùng chung mẫu logo, nhân viên không sửa được. Thẻ NFC in logo được gửi theo lô. Một nhân viên nghỉ: anh Minh bấm khoá, thẻ cũ chuyển cho người mới. Lead ở hội chợ tự vào CRM, có báo cáo cả đội. Công ty đăng nhập bằng Microsoft. Cuối tháng nhận hoá đơn VAT điện tử.
**Gồm:** #7, 30, 36–49, 52.

### Chị Mai (hộ kinh doanh) — "khách quét là trả tiền"
Thẻ của chị Mai có nút **"Chuyển khoản"**, mở QR VietQR đã điền sẵn số tài khoản. Chưa đối thủ Việt nào công bố tính năng này (C29). Gợi ý để trong MVP, vì đây là lý do để hộ kinh doanh cài app.

---

## 11. Bảng claim đã kiểm (tóm tắt — chi tiết từng khối ở verification log)

| ID | Claim | Tag | Số liệu nguyên văn | URL | primary_origin | source_type |
|---|---|---|---|---|---|---|
| C01 | becard.me → becard.uk; chủ Behires Services GmbH, Vienna | `[CONFIRMED]` | "302"; domain tạo 2019-10-16 | https://becard.uk/resources/legal/imprint | vendor + whois | primary |
| C02 | Giá Becard, tối thiểu 10 giấy phép, không có gói free, dùng thử 14 ngày | `[CONFIRMED]` | 1,19 € / 1,96 € / 2,76 €; "Minimum number of licences 10" | https://becard.uk/pricing | vendor | primary |
| C03 | Bảng chia gói của Becard (Wallet/thống kê/SSO ở Teams; file/đa ngôn ngữ ở Enterprise) | `[HIGH CONFIDENCE]` | "Available from winter 2026" (chữ ký email) | https://becard.uk/pricing | vendor | primary |
| C04 | Trang sản phẩm Becard "đang xây dựng"; docs.becard.me 404 | `[HIGH CONFIDENCE]` | HTTP 404 | https://becard.uk/products/lead-capturing | vendor | primary |
| C05 | App Becard: ra 11/02/2025, 2 lượt đánh giá, chỉ cho doanh nghiệp | `[HIGH CONFIDENCE]` | 5,0/2 | https://itunes.apple.com/lookup?id=6741759589&country=at | Apple | primary |
| C06 | Giá và gói miễn phí của Blinq | `[CONFIRMED]` | $9,99 · $7,33 · $6,99 · $4,99 | https://blinq.me/pricing | vendor | primary |
| C07 | Giá HiHello; không bán thẻ NFC | `[HIGH CONFIDENCE]` | $6 · $72 · $5 · $60 | https://www.hihello.com/pricing | vendor | primary |
| C08 | Giá Mobilo; thẻ từ $5 | `[HIGH CONFIDENCE]` | $3 · $4 · $5 | https://www.mobilocard.com/pricing-2 | vendor | primary |
| C09 | Wave: form thu liên hệ ngay ở gói Free; Pro $7 | `[HIGH CONFIDENCE]` | $7 · $5/người | https://wavecnct.com/pages/pricing | vendor | primary |
| C10 | Haystack: quét danh thiếp AI không giới hạn ở gói Free | `[HIGH CONFIDENCE]` | $4,50 · $2,50 (10+ người) | https://thehaystackapp.com/pricing | vendor | primary |
| C11 | Uniqode: 1 thẻ miễn phí; Team $6/người trả năm | `[HIGH CONFIDENCE]` | $6 | https://www.uniqode.com/pricing | vendor | primary |
| C12 | V1CE £49/tháng; thẻ £60 mua một lần | `[HIGH CONFIDENCE]` | £49 · £60 | https://v1ce.co/pricing | vendor | primary |
| C13 | Tapni: thẻ $29,90; Business $59,90/người/năm | `[HIGH CONFIDENCE]` | $29,90 · $59,90 | https://tapni.com/pages/pricing | vendor | primary |
| C14 | Popl không công bố bảng giá | `[HIGH CONFIDENCE]` | — | https://popl.co/pricing | vendor | primary |
| C15 | Linq One $29/người/tháng | `[LOW CONFIDENCE]` | $29 · $249/năm | (chỉ qua search) | search | secondary |
| C16 | CRM ở gói trả phí/team; SCIM ở Enterprise (Blinq, HiHello, Kado); SSO có nơi mở từ gói team | `[ASSESSED]` | "Enforced SSO SCIM user provisioning" (Blinq) | https://blinq.me/pricing ; https://www.hihello.com/enterprise ; https://www.kadonetworks.com/business | 3 vendor | primary |
| C17 | Wallet miễn phí ở phần lớn app quốc tế; Becard là ngoại lệ | `[ASSESSED]` | — | C06–C09 + C03 | nhiều vendor | primary |
| C18 | Ma trận tính năng 9 vendor (agent đọc trang chính chủ) | `[HIGH CONFIDENCE]` (từng ô) | — | trang pricing của từng vendor | vendor | primary |
| C19 | SOC 2 chỉ là tự công bố (Blinq, HiHello); tuyên bố SOC 2 của Kado bị bác | `[ASSESSED]` | — | https://blinq.me/security ; https://www.hihello.com/security | vendor | primary |
| C20 | Số lượt đánh giá ở Mỹ (22/09/2026) | `[HIGH CONFIDENCE]` | Blinq 4,87/131.424 · HiHello 4,87/44.268 · Popl 4,82/102.289 · Linq 4,85/12.288 · Mobilo 4,65/738 · Wave 4,77/1.492 · Uniqode 4,93/128 · Haystack 4,28/169 | https://itunes.apple.com/search | Apple | primary |
| C21 | Số lượt đánh giá ở Việt Nam | `[HIGH CONFIDENCE]` | Blinq 82 · HiHello 83 · Popl 47 · Linq 3 | https://itunes.apple.com/lookup?country=vn | Apple | primary |
| C22 | Chủ đề phàn nàn (50 review mới nhất/app) | `[HIGH CONFIDENCE]` (mẫu nhỏ) | Linq 18/50 ≤3★ | Apple RSS customerreviews | Apple | primary |
| C23 | ecard.vn: 185.000đ và 285.000đ/3 năm; "không cần cài đặt ứng dụng" | `[CONFIRMED]` | 185.000 đ (3 năm) · 285.000 đ (3 năm) | https://ecard.vn/ | vendor | primary |
| C24 | ECard Pro "từ 1.500.000đ" | `[LOW CONFIDENCE]` | Không có trên trang chủ; workflow bác 1–2 | https://ecard.vn/vip | vendor | primary |
| C25 | ecard.vn và vcard.vn cùng chủ; bảng giá vcard.vn | `[HIGH CONFIDENCE]` | 285.000đ/5 năm · từ 500.000đ/năm | https://vcard.vn/ | vendor | primary |
| C26 | Mặt bằng giá Việt Nam; hoa hồng cộng tác viên | `[HIGH CONFIDENCE]` | 99.000–350.000đ; 30–50% | ncv.vn, gud.vn, icardpro.vn/bang-gia, mycard.asia, mksmart.com.vn | vendor | primary |
| C27 | Giá BizMot | `[HIGH CONFIDENCE]` | 199.000/249.000đ/tháng; 59.000–99.000đ/người | https://bizmot.com/pricing | vendor | primary |
| C28 | 11 thương hiệu web không có app iOS; vài app Việt nhỏ có tồn tại | `[CONFIRMED]` | InCard 4,89/131 · MeU 5,0/7 · EnsCard 5,0/1 | https://itunes.apple.com/search?country=vn | Apple | primary |
| C29 | Nút Zalo có ở ecard/ncv; chưa thấy đối thủ Việt nào có nút VietQR | `[ASSESSED]` | — | ecard.vn, ncv.vn | vendor | primary |
| C30 | Zalo 81,3 triệu người dùng/tháng, quý 2/2026 | `[HIGH CONFIDENCE]` | "81,3 triệu người dùng Zalo" | https://cafef.vn/vng-lai-gap-32-lan-trong-q226-813-trieu-nguoi-dung-zalo-gan-62-trieu-nguoi-choi-game-va-24-trieu-nguoi-su-dung-ai-188260803114510411.chn | báo chí dẫn báo cáo VNG | secondary |
| C31 | Mỗi người dùng Zalo có mã QR riêng | `[HIGH CONFIDENCE]` | "Mỗi người dùng Zalo sẽ đều có cho riêng mình một mã QR" | https://help.zalo.me/huong-dan/chuyen-muc/nguoi-dung-moi/su-dung-ma-qr-tren-zalo/ | Zalo | primary |
| C32 | Người dùng phổ thông còn nghi ngờ NFC | `[LOW CONFIDENCE]` | một bài hỏi trên Tinh Tế | (nhóm Tinh Tế, agent mở) | diễn đàn | forum |
| C33 | NFC nền trên iPhone XS+; cần NDEF URI; không dùng scheme riêng; các trường hợp không đọc được | `[CONFIRMED]` | "iPhone XS and later support background tag reading" | https://developer.apple.com/documentation/corenfc/adding-support-for-background-tag-reading | Apple | primary |
| C34 | Android đọc NFC khi màn hình mở khoá và NFC đang bật | `[HIGH CONFIDENCE]` | "when the screen is unlocked, unless NFC is disabled" | https://developer.android.com/develop/connectivity/nfc/nfc | Google | primary |
| C35 | iPhone không cho app bên thứ ba giả làm thẻ NFC | `[ASSESSED]` | (không có API giả lập thẻ trong Core NFC) | https://developer.apple.com/documentation/corenfc | Apple | primary |
| C36 | NTAG213/215/216 = 144/504/888 byte; khoá mật khẩu 32-bit | `[HIGH CONFIDENCE]` | "144 bytes user programmable read/write memory" | https://www.nxp.com/docs/en/data-sheet/NTAG213_215_216.pdf | NXP | primary |
| C37 | Apple Wallet generic pass: điều kiện, cập nhật đẩy, QR | `[HIGH CONFIDENCE]` | — | https://developer.apple.com/documentation/walletpasses/adding-a-web-service-to-update-passes | Apple | primary |
| C38 | Google Wallet: tài khoản mới ở chế độ thử | `[HIGH CONFIDENCE]` | "you won't have publishing access" | https://developers.google.com/wallet/generic/getting-started/issuer-onboarding | Google | primary |
| C39 | App Clip: 15 MB khi mở bằng NFC/QR; 100 MB chỉ khi mở từ web/Spotlight, iOS 17+ | `[CONFIRMED]` | "iOS 16 and later 15 MB"; "iOS 17 and later 100 MB" | https://developer.apple.com/help/app-store-connect/reference/maximum-build-file-sizes/ | Apple | primary |
| C40 | Google Play Instant khai tử từ 12/2025 | `[CONFIRMED]` | "Starting December 2025, Instant Apps cannot be published" | https://developer.android.com/topic/google-play-instant | Google | primary |
| C41 | vCard 4.0 bắt buộc UTF-8; bắt buộc có FN; cấu trúc trường N | `[HIGH CONFIDENCE]` | "the charset for vCard is UTF-8" | https://www.rfc-editor.org/rfc/rfc6350 | IETF | primary |
| C42 | vCard 2.1/3.0 lỗi dấu nếu thiếu khai báo UTF-8 | `[LOW CONFIDENCE]` | — | (nguồn thứ cấp) | search | secondary |
| C43 | NameDrop không mở cho app bên thứ ba | `[LOW CONFIDENCE]` | — | (suy từ việc không có API) | search | secondary |
| C44 | Luật 91/2025/QH15: ban hành 26/06/2025, hiệu lực 01/01/2026 | `[CONFIRMED]` | "Ban hành: 26/06/2025 - Hiệu lực: 01/01/2026" | https://congbao.chinhphu.vn/van-ban/luat-so-91-2025-qh15-45578.htm | Công báo | primary |
| C45 | Nghị định 356/2025 hướng dẫn luật; Nghị định 13/2023 hết hiệu lực | `[LOW CONFIDENCE]` | — | (thuvienphapluat qua search) | search | secondary |
| C46 | Điều 9 (đồng ý), Điều 20 (chuyển ra nước ngoài), Điều 21 (hồ sơ trong 60 ngày) | `[HIGH CONFIDENCE]` | "trong vòng 60 ngày kể từ ngày đầu tiên xử lý" | https://luatvietnam.vn (bản luật) | văn bản luật (bản đăng lại) | primary-copy |
| C47 | Mức phạt: tới 5% doanh thu (chuyển ra nước ngoài), tối đa 3 tỷ đồng (vi phạm khác) | `[HIGH CONFIDENCE]` | "5% tổng doanh thu... tối thiểu 3 tỷ đồng" | https://xaydungchinhsach.chinhphu.vn | Chính phủ | primary |
| C48 | Miễn trừ cho DN nhỏ/khởi nghiệp, trừ DN kinh doanh dịch vụ xử lý dữ liệu | `[LOW CONFIDENCE]` | — | baovedlcn.vn (bài luật sư) | search | secondary |
| C49 | Apple 3.1.1 / 3.1.3(c) / 3.1.3(e); hoa hồng 15% cho doanh nghiệp nhỏ | `[HIGH CONFIDENCE]` (15% `[LOW]`) | "Consumer, single user, or family sales must use in-app purchase" | https://developer.apple.com/app-store/review/guidelines/ | Apple | primary |
| C50 | Google Play: hàng vật lý được miễn; phí mới từ 30/06/2026 chỉ áp dụng US/UK/EEA | `[HIGH CONFIDENCE]` | "Purchases or rentals of physical goods" | https://support.google.com/googleplay/android-developer/answer/10281818 | Google | primary |
| C51 | Nghị định 254/2026: ban hành 30/06/2026, hiệu lực 01/07/2026, thay Nghị định 123/2020 | `[HIGH CONFIDENCE]` | "Nghị định số 123/2020/NĐ-CP… hết hiệu lực thi hành" | https://www.meinvoice.vn/tin-tuc/48311/nghi-dinh-254-2026-nd-cp-thay-the-nghi-dinh-123/ | trích văn bản (MISA) | secondary-quote |
| C52 | VietQR của NAPAS; vietqr.io của CASSO | `[CONFIRMED]` | "VietQR.io là của CTY CASSO" | https://vietqr.io/intro/ | CASSO | primary |
| C53 | Link `zalo.me/<sđt>` không có tài liệu chính thức cam kết | `[LOW CONFIDENCE]` | — | (không tìm thấy trên developers.zalo.me) | search | secondary |
| C54 | Nhà cung cấp nước ngoài bán cho người Việt phải đăng ký thuế qua etaxvn | `[LOW CONFIDENCE]` | — | gdt.gov.vn (qua search) | search | secondary |
| C55 | `beshake.me` chưa ai đăng ký | `[HIGH CONFIDENCE]` | "Domain not found." (DB 2026-09-21T17:45:37Z) | whois.nic.me | registry | primary |
| C56 | `beshake.com` đã có chủ từ 20/10/2018, hết hạn 20/10/2026 | `[HIGH CONFIDENCE]` | Registrar NameBright | whois | registry | primary |
| C57 | Không có app tên BeShake (App Store VN/US). App "be" của Be Group có 531.895 lượt đánh giá ở VN | `[HIGH CONFIDENCE]` | 531.895 | https://itunes.apple.com/search?term=be%20group&country=vn | Apple | primary |

Claim bị loại (Sai), claim được khôi phục, và lý do: xem mục "Claim bác bỏ / điều chỉnh" trong verification log.

## 12. Điểm mù / câu mở

1. **Ai là bên kiểm soát dữ liệu** của người nhận (anh Tuấn) và của danh thiếp giấy bị quét: BeShake, chủ thẻ, hay cả hai. Luật chưa nói rõ.
2. Toàn văn **Nghị định 356/2025** và **Điều 38** (miễn trừ cho DN nhỏ): mới đọc qua bài phân tích, chưa đọc văn bản gốc.
3. **Kiểm tra nhãn hiệu "BeShake"** tại Cục Sở hữu trí tuệ, và nguy cơ trùng họ sản phẩm "be…" của Be Group: **chưa kiểm**.
4. `beshake.vn`: chưa kiểm (whois VNNIC không truy vấn được bằng dòng lệnh).
5. **Người Việt đang trao đổi liên hệ bằng gì, tỷ lệ bao nhiêu** (Zalo QR / lưu số / danh thiếp giấy): **chưa có số liệu khảo sát** nào đáng tin. Đây là câu hỏi cần hỏi trực tiếp người dùng.
6. **Mức sẵn lòng trả tiền** của cá nhân và SME Việt Nam cho gói thuê bao so với gói trọn đời: chưa kiểm, cần hỏi trực tiếp.
7. Google Play có ngoại lệ bán trực tiếp cho doanh nghiệp giống Apple 3.1.3(c) không: chưa tìm thấy văn bản.
8. Apple Watch, yêu cầu tự xoá tài khoản trong app của App Store, định dạng mã vạch của Google Wallet: chưa kiểm.
9. Giá Linq và Popl: chỉ có qua nguồn thứ ba.
10. Điểm đánh giá trên Google Play: chưa kiểm cho vendor nào.

## 13. Cờ human-review

- Cần luật sư xác nhận: BeShake có phải "bên kiểm soát" dữ liệu người nhận và danh thiếp giấy bị quét không, và có thuộc diện miễn trừ Điều 38 không.
- Cần tra cứu nhãn hiệu "BeShake" (nhóm 9 phần mềm, nhóm 42 dịch vụ) tại Cục Sở hữu trí tuệ trước khi in thẻ và làm logo.
- Cần kế toán xác nhận luồng hoá đơn điện tử theo Nghị định 254/2026 cho gói doanh nghiệp và cho thẻ vật lý bán lẻ.

---

## 14. Chỗ trống cần điền — vòng hỏi 1 (theo kiểu grill: mỗi câu kèm khuyến nghị; các câu trong vòng này độc lập với nhau)

❓ **Q1 — Ai là người trả tiền đầu tiên?**
- (A) Cá nhân làm sales/môi giới như chị Lan. Thị trường đông, đua giá 99.000–350.000đ, mất 15–30% nếu thu thuê bao qua IAP (C26, C49).
- (B) Doanh nghiệp 10–200 nhân viên như công ty anh Minh. Ít đối thủ Việt làm phần mềm thật, chỉ có BizMot và MK Smart. Được thu tiền ngoài IAP. Becard chứng minh mô hình tính theo đầu người (C02, C27, C49).
- (C) Cả hai ngay từ ngày đầu.

➡️ Khuyến nghị: **(B) thu tiền, (A) miễn phí làm phễu.** Cá nhân dùng miễn phí để lan truyền. Tiền đến từ gói doanh nghiệp và thẻ NFC in logo.

---

❓ **Q2 — Có tự bán thẻ NFC vật lý không?**
- (A) Không, chỉ QR và app.
- (B) Tự nhập chip, tự in, tự giữ kho.
- (C) Hợp tác xưởng in thẻ; BeShake chỉ ghi link và khoá thẻ.

➡️ Khuyến nghị: **(C).** Khách Việt quen mua "thẻ + hồ sơ" (cả 11 đối thủ Việt đều bán thẻ). Nhưng giữ kho là rủi ro. Chip NTAG213 đủ cho link (C26, C36).

---

❓ **Q3 — Dữ liệu người dùng đặt ở đâu?**
- (A) Máy chủ tại Việt Nam.
- (B) Nước ngoài (ví dụ Singapore), chấp nhận thêm hồ sơ chuyển dữ liệu ra nước ngoài và rủi ro phạt tới 5% doanh thu (C46, C47).

➡️ Khuyến nghị: **(A) từ đầu.** Bớt một hồ sơ pháp lý, và là điểm bán với khách doanh nghiệp.

---

❓ **Q4 — Bản đầu tiên có cho người nhận "gửi lại thông tin" không?**
- (A) Có ngay, kèm ô đồng ý riêng cho từng mục đích. Wave, Mobilo cho miễn phí; đây là lý do chị Lan dùng app (C18, C46).
- (B) Để sau, khi luật sư đã xác nhận vai trò bên kiểm soát.

➡️ Khuyến nghị: **(A)**, làm song song với việc hỏi luật sư. Chốt nội dung ô đồng ý trước khi ra mắt.

---

❓ **Q5 — Nút QR chuyển khoản VietQR vào bản đầu tiên hay để sau?**
- (A) Bản đầu, miễn phí. Đây là khác biệt mà chưa đối thủ Việt nào công bố; nhắm hộ kinh doanh như chị Mai (C29, C52).
- (B) Để sau.

➡️ Khuyến nghị: **(A).**

**Vòng 2 (chỉ mở sau khi chốt Q1):**
- Gói cá nhân Pro: thuê bao tháng qua IAP, hay trọn gói kèm thẻ như thị trường Việt?
- Tích hợp CRM nào trước?
- SSO Microsoft trước hay Google trước?
- Có dùng kênh cộng tác viên không?

## 15. Việc làm ngay (không cần quyết định)

1. Đăng ký **beshake.me** (C55). Kiểm thêm `beshake.vn`.
2. Tra nhãn hiệu "BeShake" tại Cục Sở hữu trí tuệ (cờ human-review 2).
3. Mở tài khoản Apple Developer và nộp hồ sơ phát hành Google Wallet sớm, vì cả hai cần thời gian duyệt (C37, C38).
