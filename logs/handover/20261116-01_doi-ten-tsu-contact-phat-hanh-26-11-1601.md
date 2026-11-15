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

1. 👤 Xóa Worker cũ `tsudev-contact` trên Cloudflare (không còn route/tên miền; phiên bị chặn quyền xóa):
   `cd website && npx wrangler delete --name tsudev-contact`.
2. 👤 Tắt Cloudflare JavaScript Detections (script nội tuyến bị CSP chặn trên mọi `*.tsudev.com`) - phiếu tsudev 20261116-C1.
3. 👤 Đổi tên thư mục cục bộ `~/projects/tsudev-contact` -> `~/projects/tsucontact` khi không còn phiên nào mở trong đó
   (`mv` + `git remote` đã trỏ URL mới). Nếu phiên này đã đổi thì bỏ qua.
4. winget qua komac (`tsudev.TsuContact`) - chờ 👤 secret `WINGET_TOKEN`; sau đó `"winget"` vào `channels` (khối Cài bằng lệnh tự hiện).
5. Best Practices passing (phiếu 20261115-01 mục 2.2, 2.4); good first issue (20261113-03 P1.5); SignPath khi D5 duyệt.
6. Phiên tsudev nhận phiếu 20261116-C1 (catalog, ecosystem.ts, TRADEMARKS ⛔).
