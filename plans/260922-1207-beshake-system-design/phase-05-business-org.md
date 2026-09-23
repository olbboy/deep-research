---
phase: 5
title: "Phase 5: Doanh nghiệp"
status: todo
priority: P1
effort: "4-6 tuần"
dependencies: [3]
---

# Phase 5: Doanh nghiệp
<!-- Updated: Validation Session 1 - route API chuyển sang apps/api (Hono); làm trước phase 4 -->

## Overview

Anh Minh trang bị 40 nhân viên: bảng quản trị trên web, mẫu khoá thương hiệu, nhập từ Excel, Spaces, phân quyền, vô hiệu/chuyển thẻ khi nghỉ việc, danh bạ chung, thống kê đội, đặt thẻ in logo theo lô, thu tiền theo seat bằng chuyển khoản VietQR (SePay), tên miền riêng. Tính năng packet: #7, 30, 36–42, 46, 47, 49, 52. Đây là nơi ra tiền theo Q1.

## Requirements

- Functional:
  - Tổ chức: tạo, mời thành viên (email), vai trò owner/admin/member, Spaces (chi nhánh), `audit_logs` cho mọi hành động admin.
  - Mẫu khoá: logo, màu, bố cục, link mặc định; `locked_fields` nhân viên không sửa; đổi mẫu → mọi thẻ cập nhật (và pass Wallet đẩy lại).
  - Nhập hàng loạt: CSV/XLSX với cột Họ / Tên đệm / Tên / Chức danh / SĐT / Email / Space → tạo user + thẻ + email chào; báo lỗi từng dòng.
  - Offboarding: vô hiệu thành viên → thẻ `inactive` (trang hiện "Liên hệ công ty"), thẻ NFC về `provisioned`, chuyển cho người mới không cần ghi lại chip.
  - Danh bạ chung: lead của mọi thành viên gộp về tổ chức (tuỳ chọn theo mẫu), lọc theo Space, xuất CSV.
  - Thống kê đội: lượt xem/lưu/lead theo thành viên, Space, nguồn; phễu lead (mới → đã liên hệ → chốt).
  - Thanh toán: gói Business theo seat/năm; đơn hàng → QR VietQR (SePay) với nội dung = mã đơn → webhook kích hoạt seat; đơn thẻ vật lý in logo theo lô, trạng thái sản xuất/giao.
  - Tên miền riêng `card.congty.vn` (CNAME → beshake.me, TLS tự động).
  - Dashboard cá nhân hiện thẻ do công ty cấp với ô khoá (trình sửa web đã đầy đủ từ phase 2).
- Non-functional: nhập 500 dòng < 2 phút (job nền, tiến độ hiển thị); mọi hành động admin có `audit_logs`; webhook SePay idempotent theo `transaction_id`.

## Architecture

system-design §6 (organizations, memberships, spaces, templates, orders, subscriptions), §8.6 (offboarding), §8.7 (thanh toán doanh nghiệp), §13 (Caddy on-demand TLS cho tên miền riêng). Better Auth plugin `organization` cung cấp tổ chức/vai trò/lời mời; BeShake thêm Spaces và mẫu.

## Related Code Files

- Create: `apps/web/src/app/(admin)/org/[orgId]/{members,templates,import,tags,contacts,analytics,billing,domain}/page.tsx`
- Create: `apps/api/src/routes/orgs/{members,templates,imports,tags,contacts,analytics,orders,domains}.ts`
- Create: `apps/api/src/routes/webhooks-sepay.ts`
- Create: `apps/worker/src/jobs/{bulk-import,template-propagate,order-status,sepay-reconcile}.ts`
- Create: `packages/core/src/{template-merge,import-parser,vietqr-order}.ts` + test
- Create: `apps/mobile/src/screens/{OrgCard,LockedFieldNotice}.tsx` (thẻ do công ty cấp: ô khoá hiện xám)
- Modify: `infra/Caddyfile` (on-demand TLS + endpoint `ask` kiểm tên miền thuộc tổ chức nào)
- Modify: `apps/web/src/app/c/[id]/page.tsx` (đọc theo host nếu là tên miền riêng)

## Implementation Steps

1. Bật UI tổ chức từ plugin `organization`: tạo org, mời, vai trò; thêm bảng `spaces` và cột `space_id` ở membership.
2. Mẫu: `templates` + hàm `template-merge(card, template)` trong `packages/core` (mẫu thắng ở cột khoá, thẻ thắng ở cột mở); job `template-propagate` khi mẫu đổi → tăng `cards.version` → phase 3 tự đẩy pass.
3. Nhập hàng loạt: parser CSV/XLSX (`import-parser`), kiểm từng dòng (SĐT, email, trùng), tạo user "chờ kích hoạt" + thẻ theo mẫu + email chào (Resend); tiến độ qua polling `/imports/:id`.
4. Quản lý thẻ NFC theo tổ chức: danh sách thẻ, gắn/chuyển/thu hồi; nhận theo lô từ đơn hàng (mã thẻ đã cấp phát ở xưởng).
5. Offboarding: một hành động → membership `suspended`, cards `inactive`, tags `provisioned`, pass đẩy "Đã ngừng", `audit_logs`.
6. Danh bạ chung + thống kê đội: truy vấn `contacts`/`event_daily` theo `org_id`, `space_id`; phễu = cột `stage` trên `contacts` (chỉ tổ chức dùng).
7. Thanh toán: bảng giá seat/năm; `orders` → VietQR (SePay, nội dung `BS<orderId>`); webhook kiểm chữ ký, khớp mã đơn, kích hoạt `subscriptions.seats`; job `sepay-reconcile` mỗi giờ đối chiếu đơn chờ. Đơn thẻ vật lý: form địa chỉ, số lượng, file logo → trạng thái `pending/paid/producing/shipped`.
8. Tên miền riêng: admin thêm domain → hiện hướng dẫn CNAME → Caddy on-demand TLS hỏi `api.beshake.me/v1/domains/verify?host=` → trang công khai đọc `organizations.custom_domain` theo host.
9. Dashboard cá nhân: thêm mục "thẻ do công ty cấp" (ô khoá hiện xám, nút liên hệ admin) — trình sửa web đã có từ phase 2.

## Todo

- [ ] Tạo org, mời 3 người, phân vai trò, Spaces
- [ ] Đổi mẫu → 40 thẻ đổi theo, pass Apple cập nhật
- [ ] Nhập file 40 dòng có lỗi cố ý ở 3 dòng → báo đúng 3 dòng, 37 thẻ tạo
- [ ] Vô hiệu 1 người → `/t/<code>` báo chưa kích hoạt → gắn người mới
- [ ] SePay sandbox: chuyển khoản đúng nội dung → seat mở ≤ 60 s; sai nội dung → nằm ở "chờ đối chiếu"
- [ ] Tên miền riêng có TLS trong < 5 phút sau khi trỏ CNAME

## Success Criteria

- [ ] Tiêu chí "Anh Minh" và "Thanh toán (doanh nghiệp)" trong `plan.md` đạt
- [ ] Một công ty thử nghiệm thật (≥ 10 người) dùng 2 tuần, admin không cần hỗ trợ kỹ thuật để onboard

## Risk Assessment

- **Tách tên trong file Excel sai** (khách gộp "Nguyễn Thị Lan" một cột). Tín hiệu: > 10% dòng cần sửa tay. Phản ứng: bắt buộc 3 cột Họ/Tên đệm/Tên trong mẫu tải về; nếu chỉ có 1 cột thì tách theo quy tắc Việt (từ đầu = họ, từ cuối = tên) và đánh dấu "cần kiểm".
- **Tiền về nhưng nội dung chuyển khoản sai** → không khớp đơn. Tín hiệu: hàng đợi "chờ đối chiếu" tăng. Phản ứng: màn đối chiếu tay cho Hà + khớp mờ theo số tiền và thời gian.
- **Caddy on-demand TLS bị lạm dụng** (ai cũng trỏ domain vào). Tín hiệu: request `ask` từ host lạ. Phản ứng: endpoint `ask` chỉ trả 200 cho domain đã xác minh trong DB.
- **Plugin organization không phủ Spaces/khoá mẫu**: đã tách Spaces và templates thành bảng riêng của BeShake ngay từ đầu, không sửa plugin.
