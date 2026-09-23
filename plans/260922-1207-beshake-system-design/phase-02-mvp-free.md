---
phase: 2
title: "Phase 2: MVP miễn phí"
status: todo
priority: P1
effort: "4-6 tuần"
dependencies: [1]
---

# Phase 2: MVP miễn phí
<!-- Updated: Validation Session 1 - API tách riêng (Hono); mốc ra mắt 2a web trước, 2b app -->
<!-- Updated: Validation Session 2 - URL /c/<id> ngẫu nhiên, đổi link, chống cào, bộ trường ngang danh thiếp giấy -->

## Overview

Bản dùng được đầu tiên cho chị Lan và anh Tuấn: tạo thẻ trong app, chia sẻ bằng link/QR, người nhận xem trên web và lưu danh bạ đúng tên tiếng Việt, để lại liên hệ; nút Zalo và nút chuyển khoản VietQR; thống kê lượt xem; xuất CSV; xoá tài khoản; widget. Tính năng packet: #1–4, 6, 9–13, 17, 24–28, 32, 34, 55, 58, 60–63, 65–66.

## Requirements

- Functional:
  - Thẻ (ngang danh thiếp giấy): tên (họ/đệm/tên riêng ô), chức danh, công ty + phòng ban, logo công ty, ảnh chân dung, ảnh bìa, câu giới thiệu ngắn, nhiều số điện thoại (di động, bàn), email, website, địa chỉ + nút chỉ đường, nút mạng xã hội (Facebook, TikTok, LinkedIn, Shopee), nút Zalo, nút chuyển khoản (BIN + số tài khoản + tên chủ), ẩn/hiện từng trường, tạm khoá thẻ, 2 thẻ/người, màu và mẫu cơ bản.
  - Chia sẻ: link duy nhất không đoán được `beshake.me/c/<id>` (12 ký tự base58 ngẫu nhiên — Q11), QR trực tuyến (`?s=qr`), QR ngoại tuyến (chứa vCard, sinh trên máy), gửi qua Zalo/SMS/email bằng share sheet hệ điều hành.
  - Đổi link (Q12): sinh mã mới, link cũ 404 ngay; app/web cảnh báo "QR đã in sẽ hỏng" trước khi xác nhận; thẻ NFC không ảnh hưởng.
  - Trang công khai: SSR, không ép cài app, nút Gọi / Zalo / Lưu danh bạ / Chuyển khoản; form trao đổi ngược có ô đồng ý; chạy trên Android 10 Chrome và iOS Safari.
  - Nhận liên hệ: danh sách lead trong app, push khi có lead mới, xuất CSV.
  - Thống kê: tổng lượt xem theo thẻ.
  - Tài khoản: xoá tài khoản và toàn bộ dữ liệu (xoá thật sau 7 ngày).
  - Widget: iOS (màn hình khoá + màn hình chính) và Android hiện QR thẻ mặc định.
  - Web (**chính**): trang giới thiệu; dashboard đầy đủ — trình sửa thẻ, tải QR PNG/SVG, danh sách lead, thống kê, xuất CSV, xoá tài khoản. App: cùng trình sửa (dùng chung schema zod và API) + chia sẻ, QR ngoại tuyến, lead + push, widget.
- Non-functional: LCP < 1,5 s trên 4G; JS trang công khai < 60 KB gzip; `.vcf` p95 < 100 ms. Chống cào (system-design §7): giới hạn tần suất `/c/*`, `.vcf`, `/t/*`, form lead theo IP và dải /24, vượt ngưỡng trả trang trống + Turnstile; không trang liệt kê thẻ, không sitemap thẻ, `noindex` mặc định; 404 đồng nhất về nội dung và thời gian.

## Architecture

system-design §7 (URL), §8.1 (chia sẻ → lưu), §8.3 (form), §10 (vCard), §11 (VietQR), §12 (bảo mật). Trang công khai cache 60 s theo slug, xoá cache khi thẻ sửa (`revalidateTag('card:'+slug)`).

## Related Code Files

- Create: `packages/core/src/{vcard,vietqr,qr-offline}.ts` + test; `packages/core/data/banks.json` (`public-id.ts` đã có từ phase 1)
- Create: `packages/core/src/schemas/card.ts` (zod, dùng chung web + mobile + API)
- Create: `apps/web/src/app/c/[id]/page.tsx`, `apps/web/src/app/c/[id].vcf/route.ts`, `apps/web/src/app/c/[id]/pay/page.tsx`, `apps/web/src/app/not-found.tsx` (404 đồng nhất)
- Create: `apps/api/src/routes/{cards,contacts,events,exports,account,public}.ts`
- Create: `apps/web/src/app/(marketing)/page.tsx`, `apps/web/src/app/(dashboard)/...`
- Create: `apps/api/src/lib/{rate-limit,turnstile,visitor-hash}.ts`
- Create: `apps/mobile/src/screens/{CardEditor,ShareSheet,QrOffline,Leads,Analytics,Settings}.tsx`
- Create: `apps/mobile/targets/widget/` (config plugin iOS WidgetKit) và `android/.../CardWidgetProvider.kt`
- Create: `apps/worker/src/jobs/{push-lead,account-purge}.ts`
- Modify: `packages/db/src/schema/{cards,contacts,events}.ts` (chỉ khi thiếu cột)

## Implementation Steps

1. **Trình sửa thẻ trên web** (dashboard Next.js, `packages/ui`; schema zod ở `packages/core` dùng chung với app; upload ảnh presigned, nén ảnh 240px cho vCard). Tham khảo luồng UI danh thiếp số qua Mobbin (connector đã nối) trước khi vẽ màn.
2. **Trang công khai SSR** `/c/[id]`: component server gọi `GET /v1/public/cards/:id` (API nội bộ), thẻ `paused`/không tồn tại → cùng một trang 404, OG tags, nút hành động; `?s=` ghi vào `events` qua API sau khi trả HTML; nút bấm ghi bằng `sendBeacon` tới `api.beshake.me/v1/public/events`.
3. **vCard** `/c/[id].vcf`: Next.js lấy JSON thẻ từ API rồi dựng bằng `packages/core/vcard.ts` (không chạm DB); nhánh 3.0 + `CHARSET=UTF-8` cho UA Android cũ; test thiết bị theo ma trận §14.
4. **QR**: trực tuyến (PNG/SVG tải từ dashboard, hiện trong app); ngoại tuyến sinh trên máy từ vCard 3.0 rút gọn (< 500 byte) — kiểm iOS Camera và Google Lens đều đề nghị "Thêm liên hệ".
5. **Nút Zalo** `https://zalo.me/<sđt>` + nút "Sao chép số" ngay cạnh (link Zalo không có cam kết chính thức, packet C53). **Nút chuyển khoản** → `/c/[id]/pay` hiện VietQR từ `packages/core/vietqr.ts`; test 3 app ngân hàng.
6. **Form trao đổi ngược**: Turnstile, giới hạn 5/IP/giờ, ô đồng ý không đánh dấu sẵn → `POST /v1/public/leads` → `contacts` + `event(lead)` + job `push-lead` (Expo Push).
7. **Lead + thống kê** (web dashboard trước, app sau): danh sách lead, chi tiết, gọi/Zalo từ lead; màn thống kê tổng lượt xem 7/30 ngày (`GET /v1/analytics/summary`, truy vấn `events` gộp theo ngày).
8. **Xuất CSV** `GET /v1/exports/contacts.csv` (UTF-8 có BOM để Excel hiện dấu). **Xoá tài khoản**: đánh dấu `deleted_at`, job `account-purge` sau 7 ngày xoá hàng + file.
9. **Trình sửa thẻ trong app** (form React Native, cùng schema zod và API với web) + trang giới thiệu web. App còn cần cho: QR ngoại tuyến, lead + push, nhận thẻ NFC (phase 3), widget.
10. **Widget**: iOS WidgetKit qua config plugin (target riêng, đọc QR từ App Group); Android AppWidgetProvider. Làm cuối phase vì nhiều rủi ro native nhất.
11. Playwright: trang công khai (emulation Android Chrome, iOS Safari), lưu vCard, gửi lead. Ma trận thiết bị thật.
12. **Đổi link + chống cào (Q11, Q12):** `POST /v1/cards/:id/rotate-link` (sinh `public_id` mới, `link_rotated_at`, xoá cache, đẩy lại pass nếu có); màn xác nhận có cảnh báo QR in giấy; rate limit theo IP và dải /24 trên `/c/*`, `.vcf`, `/t/*` (`apps/api/src/lib/rate-limit.ts`), vượt ngưỡng → trang trống + Turnstile; `robots.txt` + `noindex` mặc định, bật theo `cards.seo_indexable`; **kịch bản kiểm**: script thử 100.000 URL ngẫu nhiên trong 10 phút → 0 thẻ trúng, bị chặn sau ngưỡng, thời gian phản hồi 404 ≈ trang thẻ.

**Mốc ra mắt (Q9):** **2a — web trước:** bước 1, 2, 3, 4 (QR trực tuyến), 5, 6, 7 (web), 8, 9 (trang giới thiệu), 11, 12 → phát hành `beshake.me` công khai. **2b — app theo sau, cùng phase:** bước 4 (QR ngoại tuyến), 7 (app), 9 (editor app), 10 (widget) → phát hành App Store / Google Play.

## Todo

- [ ] Mốc 2a: web ra mắt công khai trước app
- [ ] Script đoán 100.000 URL ngẫu nhiên trong 10 phút: 0 trúng, bị chặn sau ngưỡng; đổi link → link cũ 404 ngay, thẻ NFC (phase 3) vẫn mở
- [ ] Editor thẻ + upload ảnh chạy trên web (Chrome, Safari) trước, rồi trên iOS và Android
- [ ] Trang công khai đạt LCP < 1,5 s (Lighthouse mobile, throttling 4G)
- [ ] vCard đúng tên trên iOS 17, Android 12, Android 10
- [ ] QR ngoại tuyến được iOS Camera và Google Lens nhận là liên hệ
- [ ] VietQR quét đúng ở 3 app ngân hàng
- [ ] Lead → push ≤ 5 s
- [ ] CSV mở bằng Excel không lỗi dấu
- [ ] Widget iOS + Android hiện QR
- [ ] Playwright xanh trong CI

## Success Criteria

- [ ] Tiêu chí "Chị Lan → anh Tuấn", "Form trao đổi ngược" và "Chống cào" trong `plan.md` đạt trên thiết bị thật
- [ ] 10 người dùng thử ngoài nhóm tạo được thẻ và chia sẻ trong < 5 phút không cần hướng dẫn
- [ ] Không có màn hình nào ép cài app trên trang công khai (review chéo)

## Risk Assessment

- **Trang công khai nặng dần** vì thêm thư viện. Tín hiệu: bundle > 60 KB hoặc LCP > 1,5 s trong CI Lighthouse. Phản ứng: chặn merge, tách phần tương tác thành island nhỏ.
- **vCard trên trình duyệt Android cũ** không mở Danh bạ. Tín hiệu: test thiết bị Android 10 thất bại. Phản ứng: nhánh 3.0 + nút "Tải file .vcf" hướng dẫn mở; không đổi kiến trúc.
- **Widget iOS bằng Expo** tốn thời gian hơn dự tính. Tín hiệu: > 3 ngày chưa hiện widget trên máy thật. Phản ứng: giữ widget trong phase 2 nhưng đẩy xuống sau Playwright; nếu vẫn kẹt, viết target Swift tay (vẫn trong Expo prebuild), không bỏ tính năng.
- **Link Zalo đổi hành vi**. Tín hiệu: bấm không mở chat. Phản ứng: nút "Sao chép số" đã có sẵn; đổi URL ở một hằng số.
- **Người dùng đòi link đẹp, dễ nhớ.** Tín hiệu: > 20% người thử nghiệm hỏi "sao link khó nhớ". Phản ứng: giữ mặc định ngẫu nhiên (Q11); tên đẹp là tính năng Pro tự bật ở phase 4, có cảnh báo; không đổi mặc định.
