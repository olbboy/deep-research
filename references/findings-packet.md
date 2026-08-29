# Findings packet

Ba artifact mỗi lần chạy. Không playbook, không battlecard.

## Nơi ghi và tên

- Thư mục: `reports/<topic>/` nếu tồn tại, không thì `plans/reports/`
- `findings-packet-{YYMMDD-HHmm}-{slug}.md`
- `verification-log-{YYMMDD-HHmm}-{slug}.md`
- Điểm mù: section trong packet **và** liệt kê lại cuối log

Template: `assets/findings-packet-template.md`, `assets/verification-log-template.md`.

## Packet — bắt buộc có

1. Objective, thị trường, thời điểm (UTC+7, `DD/MM/YYYY`)
2. Công cụ đã dùng (`mr` / web runtime) và engine verifier nếu có (`logprob` / `sampling`)
3. Bảng claim: câu · tag · số đúng như nguồn (không làm tròn) · URL · `primary_origin` · `source_type`
4. Range khi nhiều hãng khác số — mỗi nguồn một con số
5. Section điểm mù / câu mở / cờ human-review (đúng 3 câu nếu gate yêu cầu)
6. Claim `Sai`: không ở body; trỏ sang log

## Mapping verdict → tag

| Verdict kiem-chung + mức | Tag | Việc làm |
|--------------------------|-----|----------|
| Đúng + Cao | `[CONFIRMED]` | Dùng; chỉ khi vòng Independence cho phép |
| Đúng + Vừa | `[HIGH CONFIDENCE]` | Dùng; ghi bất định nhỏ |
| Phức tạp hơn claim | `[ASSESSED]` | Giữ nuance / range |
| Chưa đủ (yếu / 1 nguồn) | `[LOW CONFIDENCE]` | Caveat; ưu tiên range |
| Chưa đủ (không nguồn độc lập) | `[BLIND SPOT]` | Không viết như sự thật |
| Sai | — | Xóa khỏi packet; ghi log |

Không nâng tag trên verdict. Không nâng tag bằng điểm verifier.

## Log — một khối mỗi claim

Giữ nguyên khối verdict tiếng Việt của `kiem-chung-thong-tin` nếu skill đó chạy.
Kèm: Independence (`max_tag`, origin), diễn giải thay thế, trọng số nguồn đã loại (`weight < 0.3`).
