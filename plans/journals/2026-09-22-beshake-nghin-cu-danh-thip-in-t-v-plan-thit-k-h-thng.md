---
title: "BeShake: nghiên cứu danh thiếp điện tử và plan thiết kế hệ thống"
date: 2026-09-22
summary: "Deep research 105+4 agent → findings packet 57 claim; brainstorm + plan 6 phase, monorepo TypeScript, thẻ NFC ghi mã ổn định tại xưởng"
---

# BeShake: nghiên cứu danh thiếp điện tử và plan thiết kế hệ thống

## Đã làm
- Workflow `deep-research`: 5 góc, 23 nguồn, 110 claim, kiểm 25 (17 giữ, 8 bác). Thêm 4 agent bù: kỹ thuật NFC/Wallet/vCard, pháp lý VN, đối thủ quốc tế, đối thủ VN.
- Controller tự mở lại nguồn gốc các claim tác động lớn (becard.uk bằng trình duyệt, iTunes API, whois, Công báo, tài liệu Apple/Google).
- Đầu ra: `plans/reports/findings-packet-260922-0120-beshake-digital-namecard-features.md` (67 tính năng, 57 claim) + `verification-log-260922-0120-...md`.
- Brainstorm (ak-brainstorm) + plan (ak-plan, chế độ nhanh theo yêu cầu "ngay lập tức, không phỏng vấn"): `plans/260922-1207-beshake-system-design/` — `system-design.md`, `plan.md`, 6 phase, 55 việc; `ak plan validate` hợp lệ; `ak plan use` đã trỏ.

## Phát hiện đáng nhớ
- becard.me → becard.uk, công ty Áo (Behires Services GmbH), chỉ bán B2B, tối thiểu 10 giấy phép; nhiều trang tính năng "đang xây dựng", docs API 404.
- `beshake.me` chưa ai đăng ký (whois 21/09); `beshake.com` đã có chủ. Tên trùng họ "be…" của Be Group — chưa tra nhãn hiệu.
- Google Play Instant khai tử 12/2025; iPhone đọc NFC nền từ XS, cần link web thật; App Clip 15 MB khi mở bằng NFC/QR.
- Số rating trong blog so sánh của Blinq (0–3 phiếu) là số lỗi thời; số thật lấy từ iTunes API.
- Thị trường VN: 11 thương hiệu web-only bán thẻ 99.000–350.000đ/3–5 năm; app Việt lớn nhất 131 lượt đánh giá; Zalo 81,3 triệu MAU là đối thủ thật.
- Luật đã đổi: Nghị định 13/2023 và 123/2020 hết hiệu lực (Luật 91/2025, Nghị định 254/2026). Người dùng sau đó yêu cầu gác pháp lý khỏi plan → ghi là non-goal.

## Quyết định
- Kiến trúc A: monorepo TypeScript (Next.js web+API, Expo mobile, Postgres+Drizzle, Better Auth, Redis+BullMQ, S3, Claude Haiku 4.5 OCR, passkit-generator + Google Wallet, RevenueCat + SePay). So với Supabase (gãy ở phase doanh nghiệp) và Cloudflare-native (gãy ở ký pass Apple).
- Thẻ NFC ghi **mã thẻ** `beshake.me/t/<code>`, không ghi slug người dùng: xưởng ghi + khoá trước khi biết ai mua; app chỉ đọc để nhận thẻ; chuyển thẻ khi nghỉ việc không cần ghi lại chip.
- Quyết định giả định Q1–Q6 ghi ở system-design §2, mỗi cái kèm "nếu đổi thì phần nào của plan đổi".

## Bước kế
- Leo chốt Q1 (ai trả tiền trước) và Q6 (app-first hay web-first) → có thể đảo thứ tự phase 4/5 và bước trong phase 2.
- Đăng ký `beshake.me`, tra nhãn hiệu, nộp Apple Developer + Google Wallet issuer (có thời gian chờ).
- Gợi ý chạy `/ak:plan validate` trước khi cook phase 1.

> Historical work record — not durable authority. Prefer docs/specs/ADRs for current decisions.
