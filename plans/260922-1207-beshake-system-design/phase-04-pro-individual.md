---
phase: 4
title: "Phase 4: Pro cá nhân"
status: todo
priority: P2
effort: "3-4 tuần"
dependencies: [2]
---

# Phase 4: Pro cá nhân
<!-- Updated: Validation Session 1 - route API chuyển sang apps/api (Hono); phase này làm sau phase 5 -->
<!-- Updated: Validation Session 2 - tên đẹp (vanity URL) là tính năng Pro tự bật, bước 12 -->

## Overview

Gói trả phí cho chị Lan mua trong app: quét danh thiếp giấy bằng AI, ghi chú/nhãn/nhắc gọi lại, thống kê sâu, thẻ song ngữ, khoá PIN, chữ ký email, hình nền họp, video/PDF, làm giàu thông tin bằng AI. Tính năng packet: #5, 8, 18, 19, 29, 31, 33, 35. Có thể làm sau phase 5 nếu giữ Q1.

## Requirements

- Functional:
  - Mua/gia hạn/khôi phục gói Pro (tháng, năm) qua Apple/Google bằng RevenueCat; webhook đổi `users.plan`; mọi giới hạn đọc từ `entitlements.ts`.
  - OCR: chụp/chọn ảnh → bản nháp liên hệ → sửa → lưu; hạn mức 5/200 lượt/tháng theo gói.
  - Ghi chú, nhãn, nhắc gọi lại (thông báo cục bộ + push).
  - Thống kê: lượt xem theo nguồn (link/QR/NFC/Wallet), lượt lưu, lượt bấm từng nút, chuỗi theo ngày 7/30/90.
  - Thẻ song ngữ Việt–Anh (chuyển theo ngôn ngữ trình duyệt, có nút đổi); khoá PIN; chữ ký email (HTML + PNG có QR); hình nền họp (PNG 1920×1080 có QR và tên); đính kèm video YouTube/Vimeo và PDF ≤ 20 MB.
  - Tên đẹp `beshake.me/<tên>` (Q11): tự bật, mặc định tắt, màn bật có cảnh báo "ai gõ tên cũng thấy thẻ này"; tắt → 404 ngay; `noindex` vẫn giữ trừ khi bật thêm "cho phép tìm kiếm".
  - AI làm giàu: từ email/công ty gợi ý chức danh, website, LinkedIn (chỉ đề xuất, người dùng xác nhận).
- Non-functional: OCR trả kết quả ≤ 8 s; độ chính xác trường tên/số/email ≥ 85% trên bộ 50 danh thiếp Việt; webhook thanh toán idempotent.

## Architecture

system-design §8.5 (OCR), §8.7 (thanh toán Pro), §9 (entitlements). OCR chạy trong worker, gọi Claude Haiku 4.5 với ảnh + JSON schema; kết quả lưu `scans.result`, đếm hạn mức bằng `COUNT(scans) WHERE user_id AND month`.

## Related Code Files

- Create: `apps/api/src/routes/{webhooks-revenuecat,scans,notes,reminders,analytics,billing}.ts`
- Create: `apps/worker/src/jobs/{ocr,enrich,reminder-push,analytics-rollup}.ts`, `apps/worker/src/lib/claude.ts`
- Create: `packages/core/src/{ocr-schema,signature-html,i18n-card}.ts` + test
- Create: `apps/mobile/src/screens/{Paywall,ScanCard,ContactDetail,AnalyticsPro,BilingualEditor,PinSettings}.tsx`
- Create: `apps/web/src/app/(dashboard)/{signature,background}/page.tsx` (sinh PNG bằng `@vercel/og` hoặc `sharp`)
- Modify: `apps/web/src/app/c/[id]/page.tsx` (PIN gate, song ngữ, video/PDF); Create: `apps/web/src/app/[vanity]/page.tsx` (tên đẹp, bước 12)
- Modify: `packages/db/src/schema/{scans,contacts,subscriptions}.ts` nếu thiếu cột

## Implementation Steps

1. RevenueCat: cấu hình sản phẩm `pro_monthly`, `pro_yearly` ở App Store Connect + Play Console; SDK trong app; màn Paywall có "Khôi phục mua hàng" và link điều khoản (App Store yêu cầu); webhook → `subscriptions` (khoá theo `event_id`) → `users.plan`.
2. Gắn `can(plan, feature)` vào **API trước** (từ chối 402/403), UI sau (ẩn/khoá nút). Viết test API "free bị từ chối, pro được".
3. OCR: presigned upload → `POST /v1/scans` → job `ocr` → Claude Haiku 4.5, prompt cố định + JSON schema; hậu xử lý: chuẩn hoá số điện thoại Việt (+84), tách tên theo `name_parts`; app hiện bản nháp.
4. Bộ kiểm 50 ảnh danh thiếp Việt (tự chụp, đa dạng font/nền) chấm điểm tự động; giữ trong `apps/worker/test/fixtures` (không có dữ liệu người thật ngoài nhóm).
5. Ghi chú/nhãn/nhắc: cột trên `contacts`; job `reminder-push` mỗi 5 phút; thông báo cục bộ trong app làm dự phòng.
6. Thống kê Pro: job `analytics-rollup` gộp `events` theo ngày vào bảng `event_daily` (card_id, ngày, type, source, count); API trả chuỗi; màn hình biểu đồ.
7. Song ngữ: `cards.i18n = {en: {title, company, fields...}}`; trang công khai chọn theo `Accept-Language`, nút đổi lưu cookie.
8. PIN: đặt/mở khoá; trang công khai hiện form PIN, cookie ký 24 h; sai 5 lần → chờ 15 phút.
9. Chữ ký email và hình nền họp: sinh phía server (PNG) + đoạn HTML sao chép; hướng dẫn dán vào Gmail/Outlook/Zoom.
10. Video/PDF: PDF lên S3 presigned, video chỉ lưu URL YouTube/Vimeo và nhúng.
11. AI làm giàu: job `enrich` gọi Claude với dữ liệu đã có → gợi ý; người dùng bấm "Áp dụng".
12. Tên đẹp (Q11): cột `cards.vanity_slug` (quy tắc và từ cấm từ `packages/core/slug.ts`), route `apps/web/src/app/[vanity]/page.tsx` dựng cùng component với `/c/[id]` (không chuyển hướng, để tắt tên là mất dấu); quyền `vanity` trong `entitlements.ts`; thử lời cảnh báo với 5 người dùng trước khi phát hành (system-design §15.6).

## Todo

- [ ] Mua Pro sandbox trên iOS và Android → `users.plan=pro` ≤ 30 s
- [ ] Khôi phục mua hàng hoạt động sau khi cài lại app
- [ ] OCR ≥ 85% trên bộ 50 ảnh
- [ ] Hạn mức OCR chặn đúng ở lượt thứ 6 (free)
- [ ] Thống kê nguồn khớp với `events` (kiểm bằng truy vấn tay)
- [ ] Trang song ngữ đổi đúng theo trình duyệt tiếng Anh
- [ ] PIN sai 5 lần bị chặn
- [ ] Tên đẹp: bật → `beshake.me/<tên>` mở; tắt → 404 ngay; gói Free không thấy nút bật

## Success Criteria

- [ ] Tiêu chí "Thanh toán (Pro)" trong `plan.md` đạt
- [ ] Người dùng thử: 5 người quét 10 danh thiếp mỗi người, sửa trung bình < 2 trường/thẻ

## Risk Assessment

- **Duyệt IAP bị từ chối** (thiếu khôi phục mua hàng, thiếu link điều khoản, gói không rõ). Tín hiệu: reviewer trả về mục 3.1. Phản ứng: checklist Paywall ở bước 1; không đổi kiến trúc.
- **OCR kém với font/nền đặc thù** (danh thiếp in nhũ, nền tối). Tín hiệu: < 85% trên bộ kiểm. Phản ứng: tiền xử lý ảnh (xoay, tăng tương phản, cắt viền) trong worker trước; nếu vẫn kém thì đổi model qua một hằng số.
- **Chi phí AI vượt dự tính** ở gói Pro không giới hạn. Tín hiệu: `scans.cost_cents`/user/tháng > giá gói. Phản ứng: hạn mức Pro 200/tháng đã đặt; cảnh báo khi 80%.
