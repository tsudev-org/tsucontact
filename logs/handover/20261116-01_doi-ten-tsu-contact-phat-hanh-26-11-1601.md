# PHIẾU BÀN GIAO - Đổi tên Tsu Contact, phát hành 26.11.1601

- **Mã phiếu**: 20261116-01
- **Từ**: phiên `tsudev-contact-cf` (16/11/2026) - **Đến**: phiên kế tiếp của repo `tsucontact`
- **Trạng thái**: MỞ - phiên sau đọc trước khi nhận việc

## 1. Đã làm (đều merge + production có số đo)

| Hạng mục | Kết quả |
| --- | --- |
| Đổi tên | Tsu Contact / `tsucontact` (ADR-0001). Repo `tsudev-org/tsucontact` (bảo mật, ruleset 26943513, CodeQL default setup giữ nguyên; URL cũ 301). PR #26 |
| Phát hành | v26.11.1601: `tsucontact_26.11.1601_x64-setup.exe`, SBOM, `SHA256SUMS.txt` ký Sigstore + `.sigstore.json`; tải về kiểm `sha256sum -c` + `gh attestation verify` (exe, SUMS, --bundle) đạt; chạy thật trên Windows |
| Website | Worker mới `tsucontact` giữ `contact.tsudev.com`; khối Cài bằng lệnh; liên kết Ủng hộ; quét production 32/32 sạch trừ script Cloudflare |
| Scoop | scoop-bucket#10: gói `tsucontact` + `tsudev-contact` chuyển tiếp (`replacedBy`), CI cài thử thật đạt |
| Ủng hộ | Hộp Giới thiệu + chân trang + FUNDING.yml -> `https://tsudev.com/ung-ho` |
| Khác | README.en.md, Scorecard workflow, di trú thư mục cấu hình, `~/.claude/CLAUDE.md` cấm tạo lại `tsudev-contact` |

## 2. Còn lại

Việc 👤 cũ (Worker cũ, JavaScript Detections, thư mục cục bộ, tsudev#276, Neon, `WINGET_TOKEN`) đã XONG 16/11/2026 -
xem `logs/STATE.md` mục Đã hoàn thành. Thư mục cục bộ: `~/projects/tsucontact` (liên kết tạm đã xóa).

1. winget qua komac (`tsudev.TsuContact`): secret `WINGET_TOKEN` đã có. Thêm workflow komac (ghim SHA), `winget validate`
   + cài thử trên Windows, gửi PR bản đầu lên `microsoft/winget-pkgs` (bản 26.11.1601), rồi `"winget"` vào `channels`
   của `packaging/package.json` (khối Cài bằng lệnh tự hiện) và báo phiên tsudev khai winget trong catalog.
2. Best Practices passing (phiếu 20261115-01 mục 2.2, 2.4); good first issue (20261113-03 P1.5); SignPath khi D5 duyệt.
