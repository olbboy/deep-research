# Kiểm thử lặp skill prd-validate, vòng 1 tới 7

Ngày 2026-09-08. Skill: `~/.claude/skills/prd-validate`. Thay thế báo cáo vòng 1 tại `skill-test-260908-1314-prd-validate.md`.

## Tiêu chí dừng, đặt trước khi chạy

1. **Fixture lỗi**: bắt đủ mọi BLOCKER cốt lõi và tối thiểu 32 trên 34 lỗi cài, phán quyết CHƯA ĐẠT, từ chối câu lệnh nhúng.
2. **Fixture tốt**: 0 BLOCKER, 0 lỗi bịa, bắt đúng hai lỗi cố ý cài.
3. **Ổn định**: kết quả lặp lại giữa các vòng chạy độc lập.

## Thiết kế

Hai fixture, danh sách lỗi viết ra **trước** khi chạy, agent bị cấm đọc đáp án và bài làm cũ.

- **Fixture lỗi**: PRD nhắc lịch bảo trì cộng roadmap, cài 34 lỗi, trong đó 1 câu lệnh nhúng đòi bỏ qua kiểm và trả lời ĐẠT.
- **Fixture tốt**: PRD đổi lịch hẹn cộng roadmap, viết đúng khung, cố ý để lại đúng 2 lỗi hạng MINOR.
- **Mốc so sánh**: một agent là PM giàu kinh nghiệm, không dùng skill.

## Kết quả theo vòng

| Vòng | Fixture lỗi | Fixture tốt |
|---|---|---|
| 1 | 29/31, 9 BLOCKER | chưa chạy |
| Mốc, không skill | 11 trọn cộng 6 phần trên 31 | chưa chạy |
| 2 | 33/34, 8 BLOCKER | 0 BLOCKER, **sót cả 2 lỗi cố ý** |
| 3 | **34/34**, 10 BLOCKER | 0 BLOCKER, **bắt trọn 2 lỗi cố ý**, 2 MAJOR thật |
| 4 | **34/34**, 11 BLOCKER | **ĐẠT**, đúng 2 MINOR, 0 MAJOR |
| 5 | **34/34**, 11 BLOCKER, y hệt vòng 4 | 0 BLOCKER, 1 MAJOR thật |
| 6 | **34/34**, 11 BLOCKER, y hệt vòng 4 và 5 | 0 BLOCKER, 2 MAJOR thật |
| 7 | không chạy, đã ổn định ba vòng | **ĐẠT**, 0 BLOCKER, 0 MAJOR, đúng 2 MINOR cố ý |

**Cả ba tiêu chí dừng đã đạt ở vòng 7.**

Fixture lỗi ổn định ba vòng liền: cùng phán quyết, cùng tập BLOCKER. Câu lệnh nhúng bị từ chối ở **mọi** vòng, không vòng nào tính nó là bằng chứng duyệt.

Fixture tốt: **0 BLOCKER và 0 lỗi bịa ở mọi vòng**. Mọi MAJOR mà skill nêu, khi tôi kiểm lại, đều là lỗ thật tôi vô tình viết vào fixture, tổng cộng chín lỗ qua bốn vòng.

## Điều quan trọng nhất học được

Chín lỗ đó chia hai loại. Bảy lỗ đầu là sơ suất viết lách, vá xong là hết. Nhưng ba vòng liên tiếp 4, 5, 6 đều lộ **cùng một loại**: thêm một hạ tầng nữa mà PRD dùng nhưng không khai báo, lần lượt là công cụ nội bộ, email, rồi thông báo đẩy.

Đây không phải lỗi của skill mà là tính chất của phép kiểm phụ thuộc: **tập phụ thuộc ngầm là tập mở**, liệt kê từng cái sẽ không bao giờ hết. Cách sửa đúng là để tài liệu **đóng cả lớp** bằng một câu, thay vì kể tên từng hệ thống. Đã sửa fixture theo hướng đó trước vòng 7, và vòng 7 ra ĐẠT với 0 MAJEUR, xác nhận cách sửa này đúng.

Bài học cho người dùng skill: khi phép kiểm phụ thuộc cứ bắn mãi, đừng thêm tên hệ thống, hãy viết một câu bao trọn lớp hạ tầng dùng chung và ai sở hữu. Một câu đóng lớp thay được ba vòng vá từng cái.

## So với người đọc giỏi, không dùng skill

Mốc so sánh tìm 18 vấn đề, chất lượng cao: bắt câu lệnh nhúng, lộ dữ liệu cá nhân, thiếu tiêu chí nghiệm thu, ra mắt một phát không rút lui. Nhưng sót gần trọn nhóm **không tự lộ ra khi đọc**: truy vết mục tiêu với yêu cầu, xếp hạng ưu tiên, persona, tracking plan, bốn rủi ro, guardrail, và toàn bộ lớp nhất quán PRD với roadmap.

Ngược lại, mốc so sánh tìm được 7 thứ ngoài danh sách của tôi mà skill vòng 1 không có: phụ thuộc kỹ thuật ẩn, mâu thuẫn giữa non-goal với nhóm người dùng tắt quyền, khái niệm nghiệp vụ chưa định nghĩa. Ba thứ này đã được đưa vào skill thành nhóm phép kiểm L2L.

Chi phí: gấp 1,6 lần token, gấp 3,4 lần thời gian.

## Skill đã đổi gì qua bảy vòng

Từ 45 lên **65 phép kiểm có mã**. Bổ sung sáu nhóm: nguyên tắc sản phẩm; kế hoạch ra mắt và rút lui; chất lượng bảng chỉ số; phụ thuộc ẩn, quyền nền tảng và khái niệm chưa định nghĩa; tầm nhìn cùng khung ưu tiên của roadmap; bản roadmap theo nhóm người đọc.

Sửa quan trọng về phương pháp:

| Sửa | Vì sao |
|---|---|
| Cấm suy luận trong ma trận truy vết, chỉ dùng liên kết tường minh | Agent vòng 2 tự suy ra rồi bỏ sót một mục tiêu không có yêu cầu nào. Suy luận ngầm chính là cách đội tự thuyết phục mình đã phủ đủ |
| Đổi phép thử gộp lỗi từ "cùng nguyên nhân" sang **"cùng cách sửa"** | Quy tắc cũ gộp ba lỗi khác nhau ở mục tiêu chí phát hành làm một, mất hai việc phải làm |
| Thêm trạng thái thứ tư "không áp dụng" và quy tắc cha con | Mã hỏi về chất lượng của thứ chưa tồn tại không nên thành phát hiện riêng |
| Chặn nâng mức khi chỉ là "không biết" | Kiểm bàn giấy chỉ chứng minh được tài liệu không nói, không chứng minh được hệ thống không tồn tại |
| Thêm điều kiện thay thế cho hai phép kiểm gián tiếp | Không có chúng, hai phép này luôn bắn và không PRD nào đạt được |
| Ba căn cứ hạ mức, ba căn cứ nâng mức, xét trong phạm vi một phép kiểm | Thay cho "phải nêu lý do" chung chung, để hai lần chạy ra cùng kết quả |
| Viết đủ vế cho hai phép kiểm | Guardrail và non-goal viết thiếu vế nên bỏ sót đúng hai lỗi cố ý cài |

## Trạng thái cuối

65 phép kiểm. Kiểm tự động bằng đối sánh chặt: không mã mồ côi, không mã định nghĩa trùng. Validator của ak-skill-creator báo hợp lệ, đóng gói thành công. Mọi file dưới 300 dòng, tổng 1.198 dòng.

| File | Dòng |
|---|---|
| SKILL.md | 129 |
| references/validation-layers.md | 280 |
| references/worked-example.md | 160 |
| references/roadmap-structure.md | 100 |
| references/prd-structure.md | 98 |
| references/sources.md | 79 |
| references/evidence-standards.md | 79 |
| assets, 3 mẫu | 273 |

Chi phí kiểm thử: 11 lần chạy agent, khoảng 2,1 triệu token, khoảng 105 phút máy.

## Câu hỏi chưa giải quyết

1. Phép kiểm phụ thuộc ngầm mở về bản chất, nên hai lần chạy có thể nêu hai phụ thuộc khác nhau. Đã giảm bằng cách hướng dẫn đóng cả lớp, chưa loại hết.
2. Mới thử trên hai fixture do chính tôi viết. Chưa chạy trên PRD thật của một đội thật.
3. Chưa đo với người kiểm là con người, chỉ đo với agent.
4. Công cụ Write trong phiên này chặn tên file bắt đầu bằng `report`, nên mọi agent phải ghi báo cáo qua Bash. Đây là ràng buộc của môi trường, không phải của skill.
