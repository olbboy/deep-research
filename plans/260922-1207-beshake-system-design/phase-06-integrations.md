---
phase: 6
title: "Phase 6: Tích hợp"
status: todo
priority: P2
effort: "3-4 tuần"
dependencies: [5]
---

# Phase 6: Tích hợp
<!-- Updated: Validation Session 1 - route API chuyển sang apps/api (Hono); gói @better-auth/sso -->

## Overview

Những thứ khách doanh nghiệp lớn hỏi trước khi ký: đăng nhập bằng tài khoản công ty (Microsoft Entra, Google Workspace), đồng bộ lead vào CRM (HubSpot trước, Salesforce sau), webhook và API công khai, Zapier, quét thẻ đeo sự kiện, xuất hoá đơn điện tử qua nhà cung cấp, SCIM khi có khách yêu cầu. Tính năng packet: #30, 43–45, 48, 59.

## Requirements

- Functional:
  - SSO: OIDC với Microsoft Entra ID và Google Workspace qua plugin SSO của Better Auth; bật/tắt và bắt buộc theo tổ chức; SAML khi khách yêu cầu.
  - CRM: kết nối HubSpot bằng OAuth; lead mới → tạo/cập nhật contact (khớp theo email rồi số điện thoại); đồng bộ hai chiều trường cơ bản; nhật ký đồng bộ.
  - Webhook đi ra: sự kiện `lead.created`, `card.viewed`, `member.suspended`…; ký HMAC; thử lại 5 lần lũy tiến; trang xem lịch sử gửi.
  - API công khai tại `api.beshake.me/v1` với API key theo tổ chức, phạm vi quyền, giới hạn tần suất; tài liệu OpenAPI sinh từ zod.
  - Zapier: dùng REST hooks trên webhook + API key.
  - Quét thẻ đeo sự kiện: đọc QR/mã vạch trên badge (chuẩn phổ biến: vCard/URL/mã số), map vào `contacts` với `source=badge`.
  - Hoá đơn điện tử cho đơn doanh nghiệp qua API nhà cung cấp (ví dụ MISA meInvoice): tạo hoá đơn khi đơn `paid`, lưu PDF vào `invoices`.
  - SCIM (tuỳ khách): cấp/thu hồi tài khoản từ Entra/Okta.
- Non-functional: đồng bộ CRM ≤ 60 s sau lead; webhook gửi thành công ≥ 99% trong 24 h; API key chỉ lưu hash.

## Architecture

system-design §6 (integrations, webhooks, api_keys, invoices), §12 (HMAC, mã hoá token). Mọi tích hợp chạy trong worker, API chỉ xếp việc.

## Related Code Files

- Create: `apps/api/src/routes/orgs/{sso,integrations,webhooks,api-keys}.ts`, `apps/api/src/routes/oauth-hubspot.ts`
- Create: `apps/api/src/routes/public-api/*.ts` (API key) + `GET api.beshake.me/openapi.json`
- Create: `apps/worker/src/jobs/{crm-sync,webhook-deliver,einvoice-issue,scim-apply}.ts`, `apps/worker/src/lib/{hubspot,salesforce,meinvoice}.ts`
- Create: `packages/core/src/{webhook-sign,badge-parse,contact-dedupe}.ts` + test
- Create: `apps/mobile/src/screens/ScanBadge.tsx`
- Modify: `apps/api/src/auth.ts` (`@better-auth/sso`, SCIM)

## Implementation Steps

1. SSO: gói `@better-auth/sso` (kiểm npm 22/09: 1.7.5); màn admin nhập issuer/client; chế độ "bắt buộc SSO" chặn đăng nhập mật khẩu cho domain email của tổ chức.
2. Webhook đi ra + API key + OpenAPI: làm trước CRM vì CRM và Zapier đều đứng trên lớp này. Ký `X-BeShake-Signature: sha256=…`, `webhook_deliveries` lưu mã trả về; thử lại 1, 5, 30, 120, 600 phút.
3. HubSpot: app OAuth (scopes contacts), lưu token mã hoá; job `crm-sync` theo lead; `contact-dedupe` (email → số điện thoại chuẩn E.164); nhật ký ở admin; nộp app HubSpot để review nếu cần niêm yết.
4. Zapier: tài liệu "Zap mẫu" dùng REST hook; không cần app Zapier riêng ở bước đầu.
5. Quét thẻ đeo: `badge-parse` nhận diện vCard/URL/mã số; màn quét trong app dùng camera; gắn `event_name` để lọc lead theo sự kiện.
6. Hoá đơn điện tử: adapter `meinvoice` (đổi nhà cung cấp qua interface); tạo khi đơn `paid`, lưu PDF; gửi email cho `billing_email`.
7. Salesforce: cùng interface với HubSpot, làm khi có khách đầu tiên yêu cầu.
8. SCIM: bật khi có khách yêu cầu; map `active=false` → luồng offboarding phase 5.

## Todo

- [ ] Đăng nhập Microsoft Entra vào org thử nghiệm; chế độ bắt buộc SSO chặn mật khẩu
- [ ] Webhook nhận tại `webhook.site`, chữ ký kiểm đúng, thử lại khi trả 500
- [ ] Lead → HubSpot contact ≤ 60 s; lead trùng email không tạo bản sao
- [ ] OpenAPI mở được bằng Swagger UI; API key sai → 401, thiếu scope → 403
- [ ] Quét badge vCard và URL ra đúng liên hệ
- [ ] Đơn `paid` → hoá đơn PDF trong `invoices` (sandbox nhà cung cấp)

## Success Criteria

- [ ] Một khách doanh nghiệp dùng SSO + HubSpot thật trong 2 tuần không lỗi đồng bộ chưa xử lý
- [ ] Bảng giá Business liệt kê đúng những gì đã chạy (không quảng cáo thứ chưa có — bài học Becard, packet C04)

## Risk Assessment

- **Review app HubSpot/Salesforce chậm**. Tín hiệu: quá 3 tuần chưa duyệt. Phản ứng: dùng "private app"/connected app cho từng khách trong lúc chờ.
- **Giới hạn tần suất CRM** khi khách nhập 500 lead cùng lúc. Tín hiệu: HTTP 429 trong `crm-sync`. Phản ứng: BullMQ rate limiter theo `integration_id`, hàng đợi riêng.
- **SSO cấu hình sai khoá khách khỏi hệ thống**. Tín hiệu: owner không đăng nhập được sau khi bật bắt buộc. Phản ứng: owner luôn có đường đăng nhập email OTP dự phòng (không bao giờ chặn owner).
- **Nhà cung cấp hoá đơn đổi API**. Tín hiệu: job `einvoice-issue` lỗi hàng loạt. Phản ứng: adapter interface, đơn vẫn `paid`, hoá đơn phát hành lại sau.
