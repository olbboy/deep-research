---
phase: 3
title: "Phase 3: Wallet + NFC"
status: todo
priority: P1
effort: "2-3 tuần"
dependencies: [2]
---

# Phase 3: Wallet + NFC
<!-- Updated: Validation Session 1 - xưởng tự ghi chip theo file BeShake; API Hono; bỏ đầu đọc USB -->
<!-- Updated: Validation Session 2 - mã thẻ NFC 13 ký tự base32 (2⁶⁵); 302 về /c/<id> -->

## Overview

Thẻ vào Apple Wallet / Google Wallet và tự cập nhật; thẻ NFC vật lý ghi sẵn mã tại xưởng, khoá chip, khách nhận thẻ trong app; nhân viên nghỉ thì chuyển thẻ không cần ghi lại. Tính năng packet: #14, 15, 50–54.

## Requirements

- Functional:
  - `/t/<code>`: 302 về thẻ đã gắn; "chưa kích hoạt" nếu chưa gắn; 404 nếu đã thu hồi. Ghi `event(view, nfc)`.
  - Cấp phát (Q10): admin tạo lô mã + mật khẩu khoá → CSV cho xưởng ghi và khoá bằng máy của xưởng; nghiệm thu lô bằng app (5% mẫu). App: chạm thẻ → nhận thẻ (claim) ≤ 3 chạm; chế độ cấp phát trong app chỉ cho lô nhỏ (< 50) và thẻ trắng người dùng tự mua (Android; iOS best-effort).
  - Apple Wallet: generic pass, QR `?s=wallet`, web service 5 endpoint, đẩy cập nhật qua APNs khi sửa thẻ.
  - Google Wallet: Generic class/object, link "Save to Google Wallet" (JWT), PATCH khi sửa thẻ.
  - Universal link / App Link cho `/c/*` và `/t/*`: máy có app thì mở app.
- Non-functional: `/t/<code>` p95 < 50 ms; pass Apple cập nhật ≤ 60 s; thẻ khoá không bị app NFC Tools ghi đè.

## Architecture

system-design §7 (mã thẻ ổn định), §8.2 (cấp phát → nhận thẻ), §8.4 (Wallet), §8.6 (chuyển thẻ). Chip: NTAG213 đủ cho URL (`https://beshake.me/t/<13 ký tự>` ≈ 38 byte, packet C36). Mã 13 ký tự base32 Crockford từ CSPRNG (2⁶⁵ — Q11): với 1 triệu thẻ, đoán ở 1.000 lần/giây cần ~1.000 năm mới trúng một thẻ; mã 8 ký tự cũ chỉ mất ~18 phút.

## Related Code Files

- Create: `apps/web/src/app/t/[code]/route.ts`
- Create: `apps/api/src/routes/tags.ts` (batches, export-csv, claim, transfer, verify)
- Create: `apps/api/src/routes/wallet-apple.ts` (5 endpoint chuẩn Apple dưới `/wallet/apple/v1/...`)
- Create: `apps/api/src/routes/wallet-google.ts` (link "Save to Google Wallet")
- Create: `apps/worker/src/jobs/{apple-pass-build,apple-pass-push,google-pass-sync}.ts`
- Create: `apps/worker/src/lib/{passkit,apns,google-wallet}.ts`
- Create: `apps/mobile/src/nfc/{read-tag,write-tag,lock-ntag21x,provision-mode}.ts`, `apps/mobile/src/screens/{ClaimTag,VerifyBatch,ProvisionTags,WriteOwnTag}.tsx`
- Create: `infra/secrets/README.md` (cách nạp chứng chỉ Pass Type ID, WWDR, service account Google — không commit file)
- Modify: `apps/web/public/.well-known/apple-app-site-association`, `assetlinks.json` (đường dẫn thật)
- Modify: `apps/mobile/app.config.ts` (entitlements NFC, associated domains, `react-native-nfc-manager` plugin)

## Implementation Steps

1. `/t/[code]` (Next.js) gọi `GET /v1/public/tags/:code` (API: một truy vấn theo `nfc_tags.code`, index unique) → 302 / trang "chưa kích hoạt" / 404; ghi event kèm `code`.
2. API thẻ (Hono): `POST /v1/tags/batches` (admin: sinh N mã 13 ký tự base32 Crockford bằng `packages/core/public-id.ts`, `provisioned`, + mật khẩu khoá theo lô, lưu `tag_batches`), `GET /v1/tags/batches/:id/export.csv` (mã, URL, mật khẩu — chỉ admin, ghi `audit_logs`), `POST /v1/tags/claim` (kiểm `provisioned`, gắn `card_id`), `POST /v1/tags/transfer` (org admin, đổi `card_id`, ghi `audit_logs`), `POST /v1/tags/verify` (nghiệm thu: lưu `uid`, kết quả thử ghi đè).
3. Mobile NFC — **đọc trước**: `react-native-nfc-manager` đọc NDEF URI, tách `code`, gọi `claim`. Đây là đường mọi người dùng đi, kể cả iPhone.
4. **Nghiệm thu lô từ xưởng (đường chính, Q10):** màn `VerifyBatch` quét ngẫu nhiên 5% thẻ: đọc URL (đúng mã trong lô), lưu `uid`, rồi thử ghi đè (phải thất bại vì chip đã khoá) → `POST /v1/tags/verify`; lô đạt → `accepted`, không đạt → `rejected` và trả xưởng. Trước khi ký hợp đồng: gửi xưởng file CSV thử 20 thẻ và kiểm bằng đúng quy trình này.
5. Mobile NFC — **chế độ cấp phát trong app** (lô nhỏ < 50 hoặc thẻ trắng người dùng tự mua): Android ghi NDEF URI rồi gửi lệnh NTAG21x qua `transceive` (đặt `PWD`/`PACK`, `AUTH0` bảo vệ từ trang dữ liệu, `ACCESS` cấm ghi khi chưa xác thực); iOS ghi NDEF bằng Core NFC, khoá bằng `sendMifareCommand` (best-effort, có thông báo nếu không khoá được).
6. Apple Wallet: chứng chỉ Pass Type ID + WWDR nạp qua biến môi trường (base64); worker `apple-pass-build` bằng `passkit-generator` (generic, `webServiceURL`, `authenticationToken` ngẫu nhiên/pass); route web service chuẩn trên Hono (`api.beshake.me/wallet/apple/v1/...`); `apple-pass-push` gửi APNs (HTTP/2) tới `wallet_devices` khi `cards.version` tăng.
7. Google Wallet: tạo class một lần; object mỗi thẻ; link lưu = JWT ký bằng service account; `google-pass-sync` PATCH khi sửa. Nếu issuer còn ở chế độ thử → dùng tài khoản test, phát hành khi được duyệt.
8. Universal link: AASA (`/c/*`, `/t/*`, loại trừ `/api/*`), assetlinks; app xử lý mở từ link → màn xem thẻ (nếu là thẻ của mình thì editor).
9. Kịch bản chuyển thẻ end-to-end với dữ liệu seed: vô hiệu → `/t/<code>` báo chưa kích hoạt → gắn người mới → mở đúng thẻ mới.

## Todo

- [ ] `/t/<code>` 3 trạng thái, p95 < 50 ms
- [ ] Claim thẻ trên iPhone XS và Android 10
- [ ] Lô thử 20 thẻ từ xưởng: 100% URL đúng, NFC Tools không ghi đè được; chế độ cấp phát trong app ghi + khoá 10 thẻ trắng trên Android
- [ ] Pass Apple cài được, QR trên pass mở đúng thẻ, cập nhật ≤ 60 s
- [ ] Link Google Wallet lưu được trên Android thật
- [ ] Universal link mở app khi đã cài, mở web khi chưa

## Success Criteria

- [ ] Tiêu chí "NFC" và "Wallet" trong `plan.md` đạt trên thiết bị thật
- [ ] Chạm thẻ khi Camera đang mở trên iPhone → không đọc (đúng như tài liệu Apple) nhưng QR in trên thẻ vẫn mở được trang

## Risk Assessment

- **Xưởng ghi sai hoặc không khoá chip.** Tín hiệu: nghiệm thu 5% mẫu thấy URL sai hoặc NFC Tools ghi đè được. Phản ứng: từ chối lô (hợp đồng ghi rõ tiêu chí nghiệm thu), không phát hành; đường chính không phụ thuộc mã BeShake nên không đổi kiến trúc.
- **Chế độ cấp phát trong app** (lô nhỏ) không khoá được trên vài máy Android. Tín hiệu: > 5% thẻ không khoá. Phản ứng: chỉ dùng máy Android trong danh sách đã kiểm; lô lớn luôn đi qua xưởng.
- **Google Wallet chưa được cấp quyền phát hành** khi đến phase. Tín hiệu: issuer vẫn "demo". Phản ứng: phát hành Apple trước, Google ẩn sau cờ tính năng; không chặn phase 4/5.
- **Chứng chỉ Apple hết hạn** (Pass Type ID 1 năm, WWDR). Tín hiệu: job build pass lỗi ký. Phản ứng: cảnh báo 30 ngày trước hạn trong worker (`cert-expiry-check`), ghi quy trình gia hạn vào `infra/secrets/README.md`.
