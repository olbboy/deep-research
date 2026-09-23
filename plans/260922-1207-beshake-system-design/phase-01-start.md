---
phase: 1
title: "Phase 1: Nền tảng"
status: todo
priority: P1
effort: "1-2 tuần"
dependencies: []
---

# Phase 1: Nền tảng
<!-- Updated: Validation Session 1 - API tách riêng (Hono, apps/api); VPS Singapore -->
<!-- Updated: Validation Session 2 - public_id ngẫu nhiên thay slug; packages/core/public-id.ts -->

## Overview

Dựng khung monorepo, cơ sở dữ liệu, đăng nhập, CI và môi trường staging tại beshake.me — để từ phase 2 mọi tính năng chỉ là "thêm bảng, thêm route, thêm màn hình". Kèm các việc hành chính có thời gian chờ (tài khoản Apple, Google Wallet) phải nộp ngay.

## Requirements

- Functional: đăng ký/đăng nhập bằng email + OTP, Google, Apple (cả web và app); tạo được một thẻ trống và mở được `staging.beshake.me/c/<id>` (trang tạm; `<id>` là `public_id` 12 ký tự ngẫu nhiên — Q11).
- Non-functional: TypeScript `strict`; CI chạy lint + typecheck + unit + API test; backup Postgres hằng đêm; `/healthz` trả 200; bí mật không nằm trong repo.

## Architecture

Xem [system-design.md](./system-design.md) §4 (thành phần), §5 (cấu trúc thư mục), §6 (bảng), §13 (hạ tầng). Phase này tạo đủ bảng của §6 nhưng chỉ dùng `users`, `cards`.

## Related Code Files

- Create: `package.json`, `pnpm-workspace.yaml`, `turbo.json`
- Create: `apps/web/` (Next.js), `apps/api/` (Hono), `apps/mobile/` (Expo, dev build), `apps/worker/` (BullMQ khung rỗng)
- Create: `packages/core/src/{entitlements,public-id,slug}.ts` + test
- Create: `packages/db/src/schema/*.ts`, `packages/db/drizzle.config.ts`, `packages/db/migrations/0001_init.sql`
- Create: `packages/api-client/`, `packages/ui/`, `packages/config/`
- Create: `apps/api/src/auth.ts` (Better Auth server), `apps/web/src/lib/auth-client.ts`, `apps/mobile/src/lib/auth-client.ts` (client)
- Create: `infra/docker-compose.yml`, `infra/Caddyfile`, `infra/backup.sh`, `.env.example`
- Create: `.github/workflows/ci.yml`, `apps/mobile/eas.json`
- Create: `apps/web/public/.well-known/apple-app-site-association`, `.../assetlinks.json` (khung)

## Implementation Steps

0. **Việc ngoài code, làm trước (có thời gian chờ):** đăng ký `beshake.me` (kiểm thêm `beshake.vn`); Apple Developer Program; Google Play Console; tài khoản issuer Google Wallet — xin quyền phát hành ngay (mặc định ở chế độ thử); tài khoản RevenueCat, SePay, Cloudflare (R2 + Turnstile), Sentry, Resend.
1. Khởi tạo Turborepo + pnpm; bốn app (web, api, mobile, worker) + năm package như §5. Bật `strict`, eslint/prettier dùng chung từ `packages/config`.
2. `packages/db`: viết schema Drizzle cho **toàn bộ** bảng ở §6 (để phase sau không đổi migration đầu), sinh `0001_init.sql`, seed một user + một card mẫu "Nguyễn Thị Lan".
3. Better Auth: server trong `apps/api` (email + OTP qua Resend, Google, Apple, Microsoft), bật plugin `organization` (chưa dùng UI); cookie phiên đặt trên domain `beshake.me` để web dùng chung. Client Expo dùng `@better-auth/expo`; lưu session bằng SecureStore.
4. `packages/core`: `entitlements.ts` (§9), `public-id.ts` (12 ký tự base58 từ `crypto.randomBytes`, và mã NFC 13 ký tự base32 Crockford — Q11) và `slug.ts` (quy tắc tên đẹp + từ cấm, dùng ở phase 4) kèm test Vitest; test `public-id` kiểm phân bố ký tự và không trùng trong 1 triệu lần sinh.
5. `apps/api`: Hono + zod; `GET /healthz`, `GET /v1/me`, `GET /v1/public/cards/:id`. `apps/web`: trang tạm `/c/<id>` gọi API nội bộ, trả HTML tối giản; `/healthz`.
6. `apps/mobile`: màn hình đăng nhập, màn hình "thẻ của tôi" (đọc từ API). Tạo **dev build** bằng EAS (không dùng Expo Go, vì phase 3 cần module NFC).
7. `infra/docker-compose.yml`: caddy, web, api, worker, postgres, redis, minio (tuỳ chọn); Caddy: `beshake.me` → web, `api.beshake.me` → api. `backup.sh` = `pg_dump` + đẩy lên R2, chạy bằng cron trong container.
8. CI: GitHub Actions chạy `turbo lint typecheck test build`; job deploy = build image → SSH vào VPS → `docker compose up -d`. Bảo vệ nhánh `main`.
9. Deploy staging lên VPS Singapore (Q7); DNS `staging.beshake.me`, `staging-api.beshake.me`; kiểm TLS, `/healthz` ở cả web lẫn api, backup chạy thật một lần.
10. Đặt file AASA/assetlinks khung với `appID`/`package_name` thật, nội dung đường dẫn sẽ điền ở phase 3.

## Todo

- [ ] Bước 0 nộp hết đơn, ghi ngày nộp vào README
- [ ] Monorepo chạy `pnpm dev` lên cả web lẫn mobile
- [ ] Migration `0001_init` áp lên staging
- [ ] Đăng nhập 3 cách trên web và app
- [ ] CI xanh, deploy staging tự động từ `main`
- [ ] Backup hằng đêm có file trên R2

## Success Criteria

- [ ] `staging.beshake.me/c/<id của thẻ seed>` trả HTML (web → api → DB); `/healthz` 200 ở cả web và api
- [ ] Đăng nhập Google trên iPhone thật và Android thật, phiên giữ sau khi tắt app
- [ ] `pnpm test` phủ 100% nhánh `entitlements.ts`, `public-id.ts`, `slug.ts`
- [ ] Không có bí mật trong git (`gitleaks` trong CI báo 0)

## Risk Assessment

- **Module native với Expo** (NFC, widget ở phase sau) không chạy trong Expo Go. Tín hiệu: `pnpm dev` mobile không load module → đã dùng dev build từ đầu, nên chỉ cần thêm config plugin; không đổi kiến trúc.
- **Plugin Expo của Better Auth** còn trẻ. Tín hiệu: session mất sau khi tắt app hoặc cookie không gửi. Phản ứng: chuyển client mobile sang bearer token (Better Auth hỗ trợ), giữ nguyên server.
- **Tài khoản Apple/Google duyệt chậm** (vài ngày đến vài tuần). Tín hiệu: chưa có tài khoản khi bắt đầu phase 3. Phản ứng: phase 3 làm NFC trước, Wallet sau; không chặn phase 2.
