---
title: "BeShake — app + web danh thiếp điện tử: thiết kế hệ thống và lộ trình 6 phase"
description: "Monorepo TypeScript (Next.js + Hono API + Expo + Postgres + worker) trên VPS Singapore; MVP miễn phí (web trước) → Wallet/NFC → Doanh nghiệp → Pro → Tích hợp"
status: pending
priority: P1
effort: "17-25 tuần (1 dev)"
tags: [beshake, mobile, web, system-design]
created: 2026-09-22
---

# BeShake — thiết kế hệ thống và lộ trình

## Overview

Xây app BeShake (iOS + Android) và web beshake.me: danh thiếp điện tử cho thị trường Việt Nam, cá nhân dùng miễn phí, doanh nghiệp trả tiền. Thiết kế chi tiết ở [system-design.md](./system-design.md). Danh mục 67 tính năng có nguồn ở [findings packet](../reports/findings-packet-260922-0120-beshake-digital-namecard-features.md).

**Hợp đồng:** Outcome — app + web + gói doanh nghiệp, phase 2 là bản dùng được đầu tiên · Constraints — một ngôn ngữ TypeScript, trang công khai nhẹ, thẻ NFC chứa link web, vùng dữ liệu cấu hình được · Non-goals — pháp lý, App Clip, Apple Watch, điện thoại giả làm thẻ, native riêng · Acceptance — mục dưới.

**Quyết định** (xem system-design §2). Đã chốt với Leo 22/09: doanh nghiệp trả tiền trước; **web là trình sửa chính**, app làm sau web trong phase 2 (ra mắt web trước — mốc 2a); **API tách riêng bằng Hono** (`apps/api`); **VPS Singapore + Docker Compose**; **xưởng in tự ghi và khoá chip theo file BeShake cấp**, app chỉ đọc để nhận thẻ; **URL thẻ là mã ngẫu nhiên 12 ký tự** `beshake.me/c/<id>` (tên đẹp chỉ là tính năng Pro tự bật); **đổi link thì link cũ chết ngay**. Còn giả định (đổi được): form trao đổi ngược và nút VietQR có trong MVP.

## Goals

| # | Goal | Priority |
|---|------|----------|
| 1 | Mỗi người một eCard đủ thông tin như danh thiếp giấy, URL duy nhất **không đoán được**; người nhận xem và lưu danh bạ đúng tên tiếng Việt, không cần cài app, trên Android cũ lẫn iPhone | P1 |
| 2 | Chủ thẻ chia sẻ bằng link, QR (trực tuyến + ngoại tuyến), NFC, Wallet, widget; nhận lại liên hệ | P1 |
| 3 | Doanh nghiệp quản trị đội: mẫu khoá, nhập Excel, khoá/chuyển thẻ khi nghỉ việc, thống kê đội, thu tiền ngoài app | P1 |
| 4 | Gói Pro cá nhân mua trong app; OCR, thống kê sâu, song ngữ | P2 |
| 5 | Tích hợp SSO, CRM, API/webhook cho khách doanh nghiệp lớn | P2 |

## Phases

| # | Phase | Status | Effort | Phụ thuộc |
|---|-------|--------|--------|-----------|
| 1 | [Phase 1: Nền tảng](./phase-01-start.md) | Pending | 1–2 tuần | — |
| 2 | [Phase 2: MVP miễn phí](./phase-02-mvp-free.md) | Pending | 4–6 tuần | 1 |
| 3 | [Phase 3: Wallet + NFC](./phase-03-wallet-nfc.md) | Pending | 2–3 tuần | 2 |
| 4 | [Phase 4: Pro cá nhân](./phase-04-pro-individual.md) | Pending | 3–4 tuần | 2 |
| 5 | [Phase 5: Doanh nghiệp](./phase-05-business-org.md) | Pending | 4–6 tuần | 3 |
| 6 | [Phase 6: Tích hợp](./phase-06-integrations.md) | Pending | 3–4 tuần | 5 |

Thứ tự thực hiện đã chốt: **1 → 2 → 3 → 5 → 4 → 6** (doanh nghiệp trước Pro cá nhân; phase 4 và 5 độc lập nhau).

## Success Criteria

- [ ] **Chị Lan → anh Tuấn:** quét QR bằng Android 10 Chrome, trang mở với LCP < 1,5 s trên 4G, bấm "Lưu danh bạ" ra đúng "Nguyễn Thị Lan" (họ/đệm/tên đúng ô) trên iOS 17 và Android 12; không có cửa sổ ép cài app.
- [ ] **Form trao đổi ngược:** anh Tuấn điền số → chị Lan nhận push trong ≤ 5 s; xuất CSV ra đủ cột.
- [ ] **Chống cào:** URL thẻ 12 ký tự base58 (2⁷⁰) — với 1 triệu thẻ, đoán ở 1.000 lần/giây cần > 1.000 năm; script thử 100.000 URL ngẫu nhiên trong 10 phút → 0 thẻ trúng và bị chặn sau ngưỡng; không trang liệt kê thẻ; `noindex` mặc định; bấm "Đổi link" → link cũ 404 ngay, thẻ NFC vẫn mở.
- [ ] **NFC:** thẻ ghi sẵn tại xưởng, khoá chip; chạm iPhone XS+ ở màn hình chính → thông báo mở đúng thẻ; app NFC Tools không ghi đè được; nhận thẻ trong app ≤ 3 chạm.
- [ ] **Wallet:** thêm pass Apple và Google; sửa chức danh → pass Apple tự cập nhật ≤ 60 s.
- [ ] **Anh Minh:** nhập 40 nhân viên từ Excel < 5 phút, mọi thẻ đúng mẫu logo và không sửa được cột khoá; vô hiệu 1 người → thẻ NFC cũ báo "chưa kích hoạt" ngay, gắn sang người mới không cần ghi lại chip.
- [ ] **Thanh toán:** mua Pro trong app (sandbox) → gói mở ≤ 30 s; chuyển khoản VietQR cho đơn doanh nghiệp → seat kích hoạt tự động khi SePay báo tiền về.
- [ ] **Chất lượng:** CI xanh (lint, typecheck, unit, API test); `packages/core` phủ 100% nhánh; Sentry không lỗi chưa xử lý sau 7 ngày staging.

## Validation Log

### Session 1 — 2026-09-22
**Trigger:** Leo chọn `/ak:plan validate` ngay sau khi plan viết xong (chế độ nhanh theo yêu cầu "lập plan ngay", không red-team).
**Questions asked:** 6 quyết định (2 ở bước handoff brainstorm, 4 ở validate) + 1 câu chọn bước kế tiếp.

### Verification Results
- **Tier:** Full (6 phase). Dự án chưa có mã nên các vai trò kiểm đường dẫn, ký hiệu, contract không áp dụng; thay bằng kiểm sự tồn tại và phiên bản thư viện trên registry npm (22/09/2026).
- **Claims checked:** 11 · **Verified:** 10 · **Failed:** 0 · **Unverified:** 1
- Verified: passkit-generator 3.6.1, react-native-nfc-manager 3.17.2 (bản cuối 28/11/2025), better-auth 1.7.5, @better-auth/expo 1.7.5, @better-auth/sso 1.7.5, drizzle-orm 0.45.3, bullmq 6.3.8, @bacons/apple-targets 5.0.0, qrcode 1.5.4, zod 4.6.5, turbo 2.11.2.
- Unverified: plugin `organization` nằm trong gói `better-auth` (không kiểm được qua README trên registry; đối chiếu tài liệu khi bắt đầu phase 1).
- Ghi chú: `nfc-pcsc` 0.8.1 (bản cuối 2021) → loại khỏi plan theo Q10.

#### Questions & Answers
1. **[Scope]** Ai là người trả tiền đầu tiên?
   - Options: Doanh nghiệp trước (Recommended) | Cá nhân trước | Cả hai song song
   - **Answer:** Doanh nghiệp trước
   - **Rationale:** thứ tự thực hiện 1→2→3→5→4→6; thu tiền doanh nghiệp ngoài IAP.
2. **[Architecture]** Chủ thẻ sửa thẻ ở đâu là chính?
   - Options: App là chính (Recommended) | Web là chính
   - **Answer:** Web là chính
   - **Rationale:** đảo bước 1 và 9 của phase 2; dashboard web đầy đủ ngay MVP; app vẫn có editor nhưng làm sau.
3. **[Architecture]** Máy chủ đặt ở đâu và chạy kiểu gì?
   - Options: VPS tại Việt Nam, Docker Compose (Recommended) | VPS tại Singapore, Docker Compose | PaaS (Railway/Render) Singapore
   - **Answer:** VPS tại Singapore, Docker Compose
   - **Rationale:** system-design §13 cố định vùng; nhiều nhà cung cấp; Q3 cũ bị thay.
4. **[Architecture]** API nằm trong Next.js (route handlers) hay tách thành dịch vụ riêng (Hono) ngay từ đầu?
   - Options: Trong Next.js (Recommended) | Tách Hono ngay từ đầu
   - **Answer:** Tách Hono ngay từ đầu
   - **Rationale:** thêm `apps/api`; Next.js không chạm DB; mọi route, webhook, Wallet web service chuyển sang Hono; phase 1 thêm ~1 tuần.
5. **[Scope]** Với web là chính: bản ra mắt đầu tiên (cuối phase 2) gồm gì?
   - Options: Web ra trước, app theo sau trong cùng phase 2 (Recommended) | Chờ đủ cả web lẫn app mới ra mắt
   - **Answer:** Web ra trước, app theo sau
   - **Rationale:** phase 2 chia mốc 2a (web) và 2b (app).
6. **[Risk]** Ai ghi mã thẻ lên chip NFC và khoá chip?
   - Options: Xưởng tự ghi bằng máy của họ theo file BeShake cấp (Recommended) | App Android tại xưởng là chính | Đầu đọc USB + script Node là chính
   - **Answer:** Xưởng tự ghi theo file BeShake cấp
   - **Rationale:** thêm bảng `tag_batches`, API xuất lô CSV, màn nghiệm thu mẫu 5%; bỏ đầu đọc USB; app giữ chế độ cấp phát cho lô nhỏ.

#### Confirmed Decisions
- Q1 doanh nghiệp trả tiền trước — phase 5 trước phase 4.
- Q6 web là trình sửa chính — editor web ở bước 1 phase 2.
- Q7 VPS Singapore + Docker Compose — thay Q3.
- Q8 API tách Hono (`apps/api`, `api.beshake.me`) — chỉ api và worker chạm Postgres/Redis.
- Q9 web ra mắt trước — mốc 2a/2b trong phase 2.
- Q10 xưởng ghi và khoá chip theo file BeShake — nghiệm thu lô bằng app.

#### Action Items
- [x] system-design: §2 (Q1, Q3, Q6–Q10), §3, §4, §5, §6 (`tag_batches`), §7, §8.1, §8.2, §8.4, §8.5, §8.7, §13, §14, §15
- [x] plan.md: mô tả, quyết định, thứ tự phase
- [x] phase 1–6: đường dẫn `apps/api`, mốc 2a/2b, nghiệm thu lô, `@better-auth/sso`, marker `Validation Session 1`
- [ ] Phase 1 bước 0: hỏi xưởng có máy mã hoá đặt được mật khẩu NTAG21x theo file không (system-design §15.3); nếu không, chế độ cấp phát trong app thành đường chính (đảo Q10)

#### Impact on Phases
- Phase 1: thêm `apps/api` (Hono); auth server chuyển sang api; Compose thêm `api`; `staging-api.beshake.me`.
- Phase 2: mốc 2a/2b; route sang Hono; editor web trước editor app; lead/thống kê trên web trước.
- Phase 3: cấp phát qua xưởng + nghiệm thu mẫu; API thẻ theo lô; Wallet web service trên Hono; bỏ USB.
- Phase 4: đường dẫn route; thực hiện sau phase 5.
- Phase 5: đường dẫn route; SePay webhook và xác minh tên miền trên api.
- Phase 6: đường dẫn route; `@better-auth/sso`; OpenAPI tại `api.beshake.me/openapi.json`.

### Whole-Plan Consistency Sweep
- Files reread: plan.md, system-design.md, phase-01-start.md, phase-02-mvp-free.md, phase-03-wallet-nfc.md, phase-04-pro-individual.md, phase-05-business-org.md, phase-06-integrations.md
- Decision deltas checked: 6 (Q1, Q6, Q7, Q8, Q9, Q10)
- Reconciled stale references: 5 (`/api/v1` ở phase-06 và `packages/api-client`; `POST /scans` ở system-design §8.5 và phase-04; Q3 thay bằng Q7)
- Unresolved contradictions: 0

### Session 2 — 2026-09-22
**Trigger:** Leo brainstorm "tính năng cơ bản: mỗi người một eCard, URL duy nhất đủ phức tạp để không cào được" — phát hiện plan đang dùng tên đẹp đoán được và mã NFC 8 ký tự quá ngắn.
**Questions asked:** 2

#### Questions & Answers
1. **[Architecture]** Định dạng URL của mỗi eCard — hợp đồng công khai, rất khó đổi sau khi in lên thẻ và ghi vào chip?
   - Options: A. Chỉ mã ngẫu nhiên 12 ký tự (Recommended) | B. Tên + đuôi ngẫu nhiên | C. Giữ tên đẹp như plan cũ
   - **Answer:** A
   - **Rationale:** 58¹² ≈ 2⁷⁰; với 1 triệu thẻ, đoán ở 1.000 lần/giây cần ~37.000 năm. Tên đẹp đoán được trong 1 giây bằng danh sách tên → chỉ còn là tính năng Pro tự bật (phase 4).
2. **[Risk]** Khi chủ thẻ bấm "Đổi link" vì nghi bị lộ, link cũ xử lý thế nào?
   - Options: Chết ngay lập tức (Recommended) | Chuyển hướng 30 ngày rồi chết
   - **Answer:** Chết ngay
   - **Rationale:** thẻ NFC không ảnh hưởng (chip trỏ qua mã thẻ); QR in giấy phải in lại, app cảnh báo trước.

#### Confirmed Decisions
- Q11: `cards.public_id` 12 ký tự base58 từ CSPRNG; URL `beshake.me/c/<id>`; mã NFC 13 ký tự base32 (2⁶⁵); tên đẹp = cột `vanity_slug`, Pro, tự bật, mặc định tắt.
- Q12: đổi link → `public_id` mới, link cũ 404 ngay, đồng nhất với 404 thường.
- Chống cào ngoài URL: không trang liệt kê, không sitemap thẻ, `noindex` mặc định, rate limit theo IP + dải /24, chặn thì trả trang trống + Turnstile, thời gian phản hồi 404 đồng nhất.

#### Action Items
- [x] system-design §1, §2 (Q11, Q12), §5, §6 (`public_id`, `vanity_slug`, `link_rotated_at`, `seo_indexable`, mã NFC 13), §7 (URL + mục chống cào), §8.1, §9, §12, §14, §15
- [x] plan.md: goal 1, quyết định, tiêu chí "Chống cào"
- [x] phase 1 (`public-id.ts`, route `:id`), phase 2 (route `/c/[id]`, đổi link, chống cào, bước 12, bộ trường ngang danh thiếp giấy), phase 3 (mã 13 ký tự), phase 4 (tên đẹp, bước 12)

#### Impact on Phases
- Phase 1: `packages/core/public-id.ts` + test; API `GET /v1/public/cards/:id`.
- Phase 2: mọi route công khai đổi sang `/c/[id]`; thêm đổi link, rate limit theo dải mạng, 404 đồng nhất, `noindex`; kịch bản kiểm 100.000 URL; bộ trường ngang danh thiếp giấy (phòng ban, logo, câu giới thiệu, số bàn, chỉ đường).
- Phase 3: mã thẻ NFC 13 ký tự; URL trên chip ≈ 38 byte.
- Phase 4: tên đẹp tự bật (bước 12), quyền `vanity` trong entitlements.

### Whole-Plan Consistency Sweep (Session 2)
- Files reread: plan.md, system-design.md, phase-01-start.md, phase-02-mvp-free.md, phase-03-wallet-nfc.md, phase-04-pro-individual.md, phase-05-business-org.md, phase-06-integrations.md
- Decision deltas checked: 3 (Q11 URL ngẫu nhiên, Q12 đổi link, mã NFC 8 → 13 ký tự)
- Reconciled stale references: 6 (`<slug>`/`[slug]` ở phase-01 yêu cầu, phase-02 yêu cầu chia sẻ, phase-03 universal link ×2, phase-04 và phase-05 đường dẫn route)
- Unresolved contradictions: 0

<!-- slug: beshake-system-design -->
