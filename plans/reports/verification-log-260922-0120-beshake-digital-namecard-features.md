# Verification log — Tính năng danh thiếp điện tử cho BeShake

Ngày: 22/09/2026, 00:44–01:20 (UTC+7).

Phương pháp: claim-gate chạy ngay trong phiên.
- **Vòng thu thập:** workflow `deep-research` (5 góc tìm kiếm, 23 nguồn, 110 claim, kiểm 25 claim bằng 3 verifier mỗi claim, cần 2/3 bác mới loại).
- **Vòng 5 (Gap), 1 lượt:** 4 agent bù lỗ hổng — kỹ thuật, pháp lý Việt Nam, đối thủ quốc tế, đối thủ Việt Nam.
- **Vòng Independence:** controller tự mở lại nguồn gốc các claim có tác động lớn.

Packet: [findings-packet-260922-0120-beshake-digital-namecard-features.md](findings-packet-260922-0120-beshake-digital-namecard-features.md)

Ký hiệu người kiểm: **CTL** = controller (tôi) tự mở · **WF** = verifier của workflow (phiếu x–y) · **AG** = agent bù lỗ hổng tự mở · **S** = chỉ qua search.

---

Claim C01: "becard.me chuyển 302 sang becard.uk; chủ là Behires Services GmbH (Vienna)"
Kết luận: Đúng · Mức tin cậy: Cao · Tính đến: 22/09/2026
→ Tag: [CONFIRMED]
Bằng chứng: CTL `curl -sIL` thấy 302 → becard.uk; CTL đọc trang imprint (cập nhật 02/07/2026, FN 547461s, VAT ATU76323514); CTL whois becard.me (tạo 2019-10-16, InterNetX GmbH); WF 3–0.
Diễn giải thay thế: becard.me có thể là một thương hiệu khác trùng tên. Loại trừ: imprint, app iOS (seller cùng tên) và footer "© 2019 - 2026 Behires Services GmbH" khớp nhau.
Yếu tố bất định: Domain `.me` hết hạn 16/10/2026; đích chuyển hướng có thể đổi.
Nguồn: becard.uk/resources/legal/imprint · non-AI · primary_origin: vendor; whois.nic.me · registry
Independence: max_tag=[CONFIRMED] · origins: vendor + registry + quan sát HTTP
---

Claim C02: "Becard: Business 1,19 € / Teams 1,96 € / Enterprise 2,76 € mỗi người dùng/tháng; tối thiểu 10 giấy phép; không có gói miễn phí; dùng thử 14 ngày"
Kết luận: Đúng · Mức tin cậy: Cao · Tính đến: 22/09/2026
→ Tag: [CONFIRMED]
Bằng chứng: CTL đọc HTML trang pricing và bóc bảng bằng trình duyệt. Các câu FAQ gồm "Becard is a paid service" và "The first 14 days are free of charge". WF 3–0 (URL gốc), WF 2–1 (tối thiểu 10 giấy phép).
Diễn giải thay thế: Giá hiển thị cho mốc 1–10 người, trả năm. Mốc đông người hơn có thể rẻ hơn (chưa bấm thử dropdown).
Yếu tố bất định: Giá chưa gồm thuế.
Nguồn: https://becard.uk/pricing · non-AI · primary_origin: vendor
Independence: max_tag=[CONFIRMED] · origins: vendor (CTL + WF quan sát độc lập)
---

Claim C03: "Bảng chia gói Becard: Wallet, thống kê, PIN, hình nền họp, thu liên hệ, quét danh thiếp, SSO SAML, Entra mở từ Teams; file, đa ngôn ngữ, email chào nhân viên mới, hỗ trợ điện thoại chỉ ở Enterprise; chữ ký email chưa có"
Kết luận: Đúng · Mức tin cậy: Vừa · Tính đến: 22/09/2026
→ Tag: [HIGH CONFIDENCE]
Bằng chứng: CTL bóc bảng bằng JS: mỗi ô là icon `circle-check` / `minus` (lucide), map ra Y/-. WF 3–0 cho riêng "Wallet + Statistics mở từ Teams".
Diễn giải thay thế: Icon có thể bị hiểu sai. Đã đối chiếu với tiêu đề cột; thứ tự Business | Teams | Enterprise khớp với thứ tự 3 thẻ giá.
Yếu tố bất định: Mục "Integration with Salesforce, Google" ghi "Limited availability".
Nguồn: https://becard.uk/pricing · non-AI · vendor
Independence: max_tag=[HIGH CONFIDENCE] · origins: vendor
---

Claim C04: "Trang sản phẩm NFC, thu liên hệ, quét danh thiếp, chữ ký email của Becard đang 'đang xây dựng'; docs.becard.me trả 404"
Kết luận: Đúng (tại thời điểm kiểm) · Mức tin cậy: Vừa
→ Tag: [HIGH CONFIDENCE]
Bằng chứng: CTL trình duyệt thấy "Anscheined befindet sich diese Seite im Aufbau!" trên becard.uk và becard.de. CTL `curl` docs.becard.me trả 404 "This organization does not have any default site content".
Yếu tố bất định: Tình trạng tạm thời, có thể được sửa bất cứ lúc nào.
Independence: max_tag=[HIGH CONFIDENCE] · origins: vendor
---

Claim C05: "App iOS Becard ra 11/02/2025, 2 lượt đánh giá, chỉ cho doanh nghiệp"
Kết luận: Đúng · Mức tin cậy: Vừa
→ Tag: [HIGH CONFIDENCE]
Bằng chứng: CTL gọi iTunes lookup id=6741759589, country=at: 5,0/2, v4.4.10 ngày 12/09/2026. Mô tả app: "nicht für die Einzelanwender gedacht" (không dành cho người dùng cá nhân).
Yếu tố bất định: Số lượt đánh giá chỉ tính App Store Áo.
Independence: origins: Apple
---

Claim C06: "Blinq: gói Free $0; Premium $9,99/tháng ($7,33 trả năm); Business $6,99/người ($4,99 trả năm); Enterprise có SSO, SCIM, SOC 2"
Kết luận: Đúng · Mức tin cậy: Cao
→ Tag: [CONFIRMED]
Bằng chứng: AG đọc trang pricing. CTL `curl` bóc chuỗi giá {$4.99, $6.99, $7.33, $9.99} và đoạn "Enforced SSO SCIM user provisioning SOC 2 Type II & GDPR compliance".
Independence: max_tag=[CONFIRMED] · origins: vendor (AG + CTL)
---

Claim C07: "HiHello: Professional $6/tháng hoặc $72/năm; Business $5/người/tháng ($60/năm), 5–100 người; Free 4 thẻ; không bán thẻ NFC"
Kết luận: Đúng một phần · Mức tin cậy: Vừa
→ Tag: [HIGH CONFIDENCE]
Bằng chứng: CTL bóc được {$5, $6, $60, $72}. Chi tiết "4 thẻ", "16 thẻ", "5–100 người" chỉ có AG thấy; CTL grep không ra (có thể nằm trong phần render bằng JS).
Yếu tố bất định: Giới hạn số thẻ chưa có kiểm thứ hai.
---

Claim C08–C13: "Giá Mobilo, Wave, Haystack, Uniqode, V1CE, Tapni"
Kết luận: Đúng theo trang chính chủ agent đã mở · Mức tin cậy: Vừa
→ Tag: [HIGH CONFIDENCE]
Bằng chứng: AG tự mở từng trang pricing (Uniqode dùng jina-read đọc sâu). CTL chưa mở lại.
Diễn giải thay thế: Giá khuyến mãi có thể khác giá niêm yết.
Yếu tố bất định: Wave có tối thiểu 3 người hay không: chưa thấy nguyên văn. V1CE: giá thẻ £60 mâu thuẫn với số liệu nguồn thứ ba (thẻ nhựa $36–kim loại $140).
---

Claim C14: "Popl không công bố bảng giá công khai"
Kết luận: Đúng · Mức tin cậy: Vừa
→ Tag: [HIGH CONFIDENCE]
Bằng chứng: AG mở 2 URL pricing, không thấy bảng giá. Giá $7,99/$14,99 từ digitalbusinesscard.com là nguồn thứ ba → không đưa vào packet như sự thật.
---

Claim C15: "Linq One $29/người/tháng hoặc $249/năm"
Kết luận: Chưa đủ chứng cứ · Mức tin cậy: Thấp
→ Tag: [LOW CONFIDENCE]
Bằng chứng: S. Trang linqapp.com/pricing render bằng JS, cả WebFetch lẫn jina-read chỉ lấy được khung trang. Review App Store có câu "now they want $30/month", phù hợp nhưng không phải bằng chứng giá.
---

Claim C16: "CRM là tính năng trả phí/team; SCIM ở Enterprise; SSO có nơi mở từ gói team"
Kết luận: Phức tạp hơn claim · Mức tin cậy: Vừa
→ Tag: [ASSESSED]
Bằng chứng: WF 3–0 / 3–0 / 2–1 / 2–1 (Blinq, HiHello, Kado: CRM ở gói trả phí). WF claim gốc "SSO + SCIM chỉ ở Enterprise" không đúng với mọi vendor: Blinq có SSO ở Business, SCIM ở Enterprise (ma trận AG); Becard có SSO SAML ở Teams (CTL); Mobilo có SSO ở Business. → Viết lại: **SCIM** thuộc Enterprise; **SSO** từ gói team trở lên.
Nguồn: blinq.me/pricing, blinq.me/enterprise, hihello.com/enterprise, kadonetworks.com/business, kadonetworks.com/integrations · primary
Independence: 3 vendor không liên quan, cấu trúc lặp lại.
---

Claim C17: "Apple/Google Wallet miễn phí ở phần lớn app quốc tế; Becard là ngoại lệ"
Kết luận: Phức tạp hơn claim · Mức tin cậy: Vừa
→ Tag: [ASSESSED]
Bằng chứng: Tổng kết của workflow ghi "Wallet và analytics bị khoá ở gói giữa" — dữ kiện đúng **với Becard** (WF 3–0). Nhưng ma trận AG cho thấy Wallet là F ở Blinq, HiHello, Mobilo, V1CE, Wave. → Không khái quát hoá từ Becard.
---

Claim C19: "SOC 2 của Blinq/HiHello chỉ là tự công bố; tuyên bố SOC 2 Type I của Kado bị bác"
Kết luận: Phức tạp hơn claim · Mức tin cậy: Vừa
→ Tag: [ASSESSED]
Bằng chứng: WF 3–0 (Blinq, HiHello tự công bố, báo cáo "available on request"). WF 1–2 bác claim SOC 2 Type I của Kado.
Yếu tố bất định: Không ai đọc được báo cáo kiểm toán gốc.
---

Claim C20/C21: "Số lượt đánh giá App Store ở Mỹ và ở Việt Nam"
Kết luận: Đúng tại thời điểm lấy · Mức tin cậy: Vừa
→ Tag: [HIGH CONFIDENCE]
Bằng chứng: AG lấy bộ số Mỹ qua itunes search (01:05–01:10). CTL lấy bộ số Việt Nam qua lookup id=… country=vn: Blinq 4,89/82, HiHello 4,92/83, Popl 4,77/47, Linq 5/3.
Diễn giải thay thế: Số lượt đánh giá không phải số người dùng. Người Việt cũng có thể dùng tài khoản App Store Mỹ.
Ghi chú: Các số ở blog so sánh của Blinq (4,9/92.300, v.v.) bị WF bác 0–3. Số thật hiện nay khác hẳn, nên là số **lỗi thời**, không hẳn là bịa.
---

Claim C22: "Chủ đề phàn nàn trong 50 review mới nhất: Linq 18/50 ≤3★ (khó huỷ 5), Popl ép người nhận tải app (3), Blinq trừ tiền bất ngờ (3)"
Kết luận: Đúng với mẫu đã lấy · Mức tin cậy: Vừa (mẫu nhỏ)
→ Tag: [HIGH CONFIDENCE]
Bằng chứng: AG đọc RSS customerreviews mostRecent.
Yếu tố bất định: Review mới nhất nghiêng về trải nghiệm tiêu cực. 50 review không đại diện cho toàn bộ người dùng.
---

Claim C23: "ecard.vn: ECard VIP 185.000đ/3 năm; ECard NFC 285.000đ/3 năm; 'không cần cài đặt ứng dụng'"
Kết luận: Đúng · Mức tin cậy: Cao
→ Tag: [CONFIRMED]
Bằng chứng: WF 3–0 (hai claim); AG mở trang; CTL `curl` bóc nguyên văn "285.000 đ (3 năm)", "185.000 đ (3 năm)", "không cần cài đặt ứng dụng".
Independence: vendor (3 lần quan sát độc lập)
---

Claim C24: "ECard Pro (gói doanh nghiệp) từ khoảng 1.500.000đ"
Kết luận: Chưa đủ chứng cứ · Mức tin cậy: Thấp
→ Tag: [LOW CONFIDENCE]
Bằng chứng: WF 1–2 (bác). AG ghi "từ 1.500.000đ" (nguồn ecard.vn/vip). CTL grep trang chủ không thấy.
Xung đột: giữ **range**. WF: không thấy số này trên trang WF mở. AG: thấy "từ 1.500.000đ" ở trang con.
---

Claim C25–C27: "vcard.vn cùng chủ ecard.vn; mặt bằng giá Việt Nam 99.000–350.000đ; hoa hồng cộng tác viên 30–50%; giá BizMot"
Kết luận: Đúng theo trang chính chủ agent mở · Mức tin cậy: Vừa
→ Tag: [HIGH CONFIDENCE]
Bằng chứng: AG mở vcard.vn (thong-tin-phap-ly), ncv.vn, gud.vn, icardpro.vn/bang-gia, mycard.asia, bizmot.com/pricing. Pháp nhân kèm MST: VSTAR GROUP 0601282535, Nhơn Mỹ 0305684347, GUD E&C 0313656093, BizMot 0315988305.
Yếu tố bất định: Số khách hàng (ecard "gần 4000 KH cá nhân, 200+ DN"; BizMot "2000+ chuyên gia") là **tự công bố**, không dùng làm dữ kiện.
---

Claim C28: "11 thương hiệu web bán thẻ ở Việt Nam không có app iOS; nhưng có vài app Việt nhỏ"
Kết luận: Phức tạp hơn claim ban đầu · Mức tin cậy: Cao
→ Tag: [CONFIRMED] (dạng đã sửa)
Bằng chứng: Claim ban đầu của AG là "**Không đối thủ nào** có app iOS; toàn thị trường VN là web-only". CTL tìm App Store VN theo từ khoá ("danh thiếp điện tử", "namecard"…) và ra InCard (INAPPS COMPANY LIMITED, 4,89/131, ra 10/07/2023), MeU (NTIOT, 5,0/7, ra 25/06/2022), EnsCard (EINSLIGHT JSC, 5,0/1, ra 17/09/2025), MK Widget Card (Tran Minh Khoi, ra 14/05/2026).
→ Sửa thành: "Không thương hiệu nào trong 11 thương hiệu web có app iOS. App Việt có tồn tại nhưng rất nhỏ (tối đa 131 lượt đánh giá)."
---

Claim C29: "Chưa đối thủ Việt nào có nút VietQR/chuyển khoản trên danh thiếp"
Kết luận: Chưa đủ chứng cứ (mệnh đề phủ định) · Mức tin cậy: Vừa
→ Tag: [ASSESSED]
Bằng chứng: AG đọc trang chủ và trang giá của 11 thương hiệu, không thấy. Có thể nằm ở trang con chưa đọc.
---

Claim C30: "Zalo 81,3 triệu người dùng/tháng, quý 2/2026"
Kết luận: Đúng · Mức tin cậy: Vừa
→ Tag: [HIGH CONFIDENCE]
Bằng chứng: CTL mở CafeF: tiêu đề "VNG lãi gấp 32 lần trong Q2.26: 81,3 triệu người dùng Zalo…". Search cho thấy VietnamPlus, Báo Đầu tư, Baomoi đưa cùng số. Trang VietnamPlus CTL grep không thấy chuỗi "81,3 triệu" (có thể do định dạng).
Yếu tố bất định: Chưa đọc báo cáo gốc của VNG. Các bài báo cùng dẫn một nguồn gốc (VNG), nên chỉ tính là 1 origin.
Independence: max_tag=[HIGH CONFIDENCE] · origins: VNG (qua báo chí)
---

Claim C31: "Mỗi người dùng Zalo có mã QR cá nhân"
Kết luận: Đúng · Mức tin cậy: Cao
→ Tag: [HIGH CONFIDENCE]
Bằng chứng: CTL WebFetch trang help.zalo.me: "Mỗi người dùng Zalo sẽ đều có cho riêng mình một mã QR". Trang này **không** nhắc tính năng gửi "danh thiếp" trong chat. Tính năng gửi danh thiếp chỉ thấy ở trang hướng dẫn bên thứ ba (thegioididong, cellphones) → [LOW CONFIDENCE], không đưa vào packet như sự thật.
---

Claim C33: "NFC nền trên iPhone XS+; cần bản ghi NDEF URI; không hỗ trợ scheme riêng; không đọc được khi Wallet/Camera đang mở, chế độ máy bay, hoặc máy chưa mở khoá từ lúc khởi động"
Kết luận: Đúng · Mức tin cậy: Cao
→ Tag: [CONFIRMED]
Bằng chứng: AG đọc tài liệu Apple. CTL tải JSON của chính trang tài liệu đó và thấy nguyên văn: "iPhone XS and later support background tag reading." / "Background tag reading doesn't support custom URL schemes. Use universal links instead." / "Airplane mode is enabled." / "The camera is in use."
---

Claim C35: "iPhone không cho app bên thứ ba giả làm thẻ NFC (HCE)"
Kết luận: Phức tạp hơn claim · Mức tin cậy: Vừa
→ Tag: [ASSESSED]
Bằng chứng: AG: phạm vi framework Core NFC chỉ có lớp đọc/ghi, không có lớp giả lập thẻ. Ngoại lệ là Apple Wallet VAS (nguồn thứ cấp).
Yếu tố bất định: Kết luận dựa trên việc không thấy API, không có câu phủ định trực tiếp. Chưa kiểm các chính sách mở NFC theo khu vực (ví dụ EEA).
---

Claim C39: "App Clip: 15 MB (iOS 16+) khi mở bằng NFC/QR; 100 MB chỉ cho App Clip mở từ web/Spotlight, iOS 17+; 10 MB dưới iOS 16"
Kết luận: Đúng · Mức tin cậy: Cao
→ Tag: [CONFIRMED]
Bằng chứng: AG đọc trang. CTL `curl` bóc nguyên văn: "iOS 17 and later 100 MB … only supports digital invocations … not from physical invocations like App Clip Codes, QR codes, or NFC tags", "iOS 16 and later 15 MB", "Earlier than iOS 16 10 MB".
---

Claim C40: "Google Play Instant khai tử từ 12/2025"
Kết luận: Đúng · Mức tin cậy: Cao
→ Tag: [CONFIRMED]
Bằng chứng: CTL `curl` developer.android.com/topic/google-play-instant thấy nguyên văn: "Starting December 2025, Instant Apps cannot be published through Google Play, and all Google Play services Instant APIs will no longer work."
---

Claim C41: "vCard 4.0 bắt buộc UTF-8; FN bắt buộc; N = Family;Given;Additional;Prefix;Suffix"
Kết luận: Đúng · Mức tin cậy: Vừa
→ Tag: [HIGH CONFIDENCE]
Bằng chứng: AG đọc RFC 6350 (file .txt). CTL chưa mở lại.
---

Claim C44: "Luật 91/2025/QH15 ban hành 26/06/2025, hiệu lực 01/01/2026"
Kết luận: Đúng · Mức tin cậy: Cao
→ Tag: [CONFIRMED]
Bằng chứng: CTL mở congbao.chinhphu.vn: "Ban hành: 26/06/2025 - Hiệu lực: 01/01/2026". AG thấy khớp ở thuvienphapluat và luatvietnam.
Independence: Công báo (nguồn gốc) + 2 bản đăng lại.
---

Claim C45: "Nghị định 356/2025/NĐ-CP hướng dẫn luật, hiệu lực 01/01/2026; Nghị định 13/2023 hết hiệu lực"
Kết luận: Chưa đủ chứng cứ · Mức tin cậy: Thấp
→ Tag: [LOW CONFIDENCE]
Bằng chứng: S (thuvienphapluat). Chưa ai mở văn bản gốc. → Cờ human-review.
---

Claim C46/C47: "Điều 9, 20, 21; mức phạt 5% doanh thu và 3 tỷ đồng"
Kết luận: Đúng · Mức tin cậy: Vừa
→ Tag: [HIGH CONFIDENCE]
Bằng chứng: AG mở bản luật trên luatvietnam.vn và bài trên xaydungchinhsach.chinhphu.vn. CTL chưa mở lại.
Yếu tố bất định: Số hiệu điều khoản được trích từ bản đăng lại, chưa đối chiếu với Công báo.
---

Claim C49: "Apple 3.1.1 / 3.1.3(c) / 3.1.3(e); hoa hồng 15% cho doanh nghiệp nhỏ"
Kết luận: Đúng (3.1.x) · Mức tin cậy: Vừa
→ Tag: [HIGH CONFIDENCE]; riêng mức 15% là [LOW CONFIDENCE] (chỉ qua search trang chính chủ)
Bằng chứng: AG mở Review Guidelines, trích "Consumer, single user, or family sales must use in-app purchase".
---

Claim C51: "Nghị định 254/2026/NĐ-CP ban hành 30/06/2026, hiệu lực 01/07/2026, thay Nghị định 123/2020"
Kết luận: Đúng · Mức tin cậy: Vừa
→ Tag: [HIGH CONFIDENCE]
Bằng chứng: CTL mở MeInvoice (MISA), trang trích nguyên văn điều khoản thi hành: "Nghị định này có hiệu lực thi hành từ ngày 01 tháng 7 năm 2026… Nghị định số 123/2020/NĐ-CP… hết hiệu lực". Search thấy thêm 8 trang (MISA AMIS, einvoice, FTS, MAN…) cùng nội dung.
Yếu tố bất định: Chưa mở Công báo. Các trang đều là nhà cung cấp hoá đơn điện tử dẫn cùng một văn bản.
---

Claim C52: "VietQR là chuẩn của NAPAS; vietqr.io là của Công ty CASSO"
Kết luận: Đúng · Mức tin cậy: Cao
→ Tag: [CONFIRMED]
Bằng chứng: CTL `curl` vietqr.io/intro: "VietQR™ là của NAPAS - CTCP Thanh toán Quốc gia VN. VietQR.io là của CTY CASSO". AG mở cùng trang.
---

Claim C55/C56: "beshake.me chưa ai đăng ký; beshake.com đã có chủ"
Kết luận: Đúng tại thời điểm kiểm · Mức tin cậy: Vừa
→ Tag: [HIGH CONFIDENCE]
Bằng chứng: CTL `whois beshake.me` → whois.nic.me trả "Domain not found." (DB 2026-09-21T17:45:37Z). **Phép thử đối chứng:** `whois becard.me` ra đủ bản ghi, nên đường truy vấn hoạt động. `whois beshake.com`: tạo 2018-10-20, NameBright, hết hạn 2026-10-20.
Diễn giải thay thế: Tên miền đang trong trạng thái chờ xoá hoặc bị registry giữ lại. whois không phân biệt được. RDAP cho `.me` không có dịch vụ (rdap.org 404).
Yếu tố bất định: Có thể có người đăng ký sau thời điểm kiểm.
---

Claim C57: "Không có app tên BeShake; app 'be' của Be Group có 531.895 lượt đánh giá ở Việt Nam"
Kết luận: Đúng · Mức tin cậy: Vừa
→ Tag: [HIGH CONFIDENCE]
Bằng chứng: CTL gọi iTunes search term=beshake (VN: 0 kết quả; US: 1 kết quả không liên quan) và term="be group" (VN: "be - Multi-Service Platform | be Group JSC | 531895"). Search cho thấy Be Group dùng họ tên beBike, beCar, beFood…
Yếu tố bất định: Rủi ro nhãn hiệu thật sự **chưa kiểm** tại Cục Sở hữu trí tuệ.
---

## Claim bác bỏ / điều chỉnh

| Claim | Phiếu WF | Xử lý | Lý do |
|---|---|---|---|
| "SSO (Entra) và đồng bộ CRM của Becard chỉ có ở Enterprise 2,76 €" | 1–2 bác | **Giữ bác bỏ** | Bảng giá CTL bóc cho thấy SSO SAML và Entra có ở **Teams**; Salesforce/Google ở Enterprise ghi "Limited availability" |
| "Becard định vị cho SME và doanh nghiệp lớn, không cho cá nhân" | 1–2 bác | **Khôi phục thành [HIGH CONFIDENCE]** | Bằng chứng mới của CTL: trang chủ becard.uk ghi "Optimized for SMEs and large companies… specifically for teams and companies"; app iOS ghi không dành cho người dùng cá nhân. Nhiều khả năng verifier đã đọc trang cũ `becard.me/en-US` (khẩu hiệu "for everyone") |
| "ECard Pro từ khoảng 1.500.000đ" | 1–2 bác | **Giữ ở [LOW CONFIDENCE]**, ghi range | AG thấy ở trang con, CTL không thấy trên trang chủ |
| "Blinq Enterprise dùng SCIM qua Entra ID/Okta/AD, tự cấp thẻ cho người mới" | 1–2 bác | **Tách claim** | Phần "Blinq có SCIM ở Enterprise" đúng (CTL thấy "SCIM user provisioning" trên trang pricing). Phần danh sách nhà cung cấp định danh và tự cấp thẻ: chưa kiểm |
| "Kado đạt SOC 2 Type I, tuân thủ GDPR" | 1–2 bác | **Loại** | Không có bằng chứng mới |
| "Blinq 4,9/92.300 review; 2,5 triệu người dùng" (blog Blinq) | 0–3 bác | **Loại** | Số thật hiện nay là 131.424 lượt đánh giá (Mỹ). Số trên blog đã lỗi thời |
| "HiHello 'nền tảng an toàn nhất', 4,85/32.900" (blog Blinq) | 0–3 bác | **Loại** | Tuyên bố tiếp thị; số lỗi thời (thật: 44.268) |
| "Popl 4,3/94.000; '#1 event lead capture app'" (blog Blinq) | 0–3 bác | **Loại** | Số lỗi thời (thật: 4,82/102.289) |
| "Toàn thị trường Việt Nam chỉ có web, không app nào" (AG) | — | **Sửa** thành C28 | CTL tìm thấy InCard, MeU, EnsCard |
| "Wallet + analytics bị khoá ở gói giữa (chuẩn ngành)" (tổng kết WF) | — | **Thu hẹp** thành C17 | Chỉ đúng với Becard |

## Nguồn đã loại (trọng số < 0,3)

- Blog so sánh do chính vendor viết (blinq.me/blog/top-digital-business-cards-compared, v1ce.co/blog/…, mobilocard.com/post/…) **không dùng làm nguồn số liệu** về đối thủ, chỉ dùng để gợi ý hướng tìm.
- digitalbusinesscard.com (giá Popl, Dot): nguồn thứ ba, không dùng.
- Tuyên bố "95% người vẫn dùng danh thiếp giấy" của ncv.vn: tiếp thị, không có nguồn.

## Điểm mù (nhắc lại từ packet)

1. Vai trò "bên kiểm soát" dữ liệu người nhận và danh thiếp giấy bị quét: luật chưa nói rõ.
2. Toàn văn Nghị định 356/2025 và Điều 38 (miễn trừ): chưa đọc văn bản gốc.
3. Nhãn hiệu "BeShake" và nguy cơ trùng họ tên sản phẩm "be…" của Be Group: chưa kiểm.
4. `beshake.vn`: chưa kiểm.
5. Hành vi trao đổi liên hệ của người Việt (Zalo QR / lưu số / danh thiếp giấy): chưa có số liệu khảo sát; cần hỏi trực tiếp.
6. Mức sẵn lòng trả tiền (thuê bao so với trọn gói): cần hỏi trực tiếp.
7. Ngoại lệ bán trực tiếp cho doanh nghiệp trên Google Play: chưa thấy.
8. Apple Watch, yêu cầu tự xoá tài khoản trên App Store, mã vạch Google Wallet: chưa kiểm.
9. Giá Linq và Popl: chỉ có nguồn thứ ba.
10. Điểm đánh giá trên Google Play: chưa kiểm.
