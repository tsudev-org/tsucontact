# PHIẾU BÀN GIAO - Bản sắc v5.0.0, bố cục cong-cu, phát hành 26.11.2101 (đang NHÁP vì VirusTotal)

- **Từ**: phiên agent-contact (tsucontact-5b), 21/11/2026 - **Đến**: phiên kế tiếp của `tsucontact`
- **Trạng thái**: ĐÓNG 22/11/2026 - 26.11.2101 bỏ, thay bằng 26.11.2201 (phiếu `20261122-01`)

## 1. Đã xong (đều đã đo)

| Việc | Kết quả |
| --- | --- |
| Phiếu STD50 PR 1 (#39) | `.standards` v5.0.0; web `tokens.css` + `products.css` + `data-product="contact"`; app gộp `products/contact.json`; Nunito; bo `tron` |
| Phiếu STD50 PR 2 (#40) | Trang chủ `cong-cu` (nút tải `.exe` + lệnh Scoop ngay màn đầu), hoạ tiết `the-xep` hero + og-image; app có trang Bắt đầu |
| Deploy | `contact.tsudev.com` deploy sau #39 và #40 (Worker `tsucontact`, 200, `data-product="contact"`, có `.thao-tac`) |
| Phiếu PRO1 | ĐÓNG - ADR-0002 (không Pro/đồng bộ; không dữ liệu rời máy) |
| Phiếu V1 | Áp cho 26.11.2101: `tsucontact_{v}_windows-x64-setup.exe`, tiêu đề `Tsu Contact {v}` (#41) |
| Release v26.11.2101 | Build/SBOM/attestation/ký SHA256SUMS XANH (run 44925260875); **job VirusTotal đỏ: Bkav + APEX (2/71)** ⇒ Release tự về NHÁP. Đã yêu cầu Reanalyze qua API (vẫn 2/71). Hồ sơ `docs/store/antivirus.md` (#42) |

## 2. Việc còn lại (theo thứ tự)

1. 👤 Chủ dự án: nộp báo nhầm Bkav (hạn nội bộ 23/11/2026) theo `docs/store/antivirus.md`, HOẶC chấp nhận công bố dù
   còn 2 cờ học máy. Không quyết ⇒ Release giữ nháp (DISTRIBUTION_TRUST mục 3.1).
2. Agent (sau khi gỡ cờ hoặc 👤 chấp nhận): re-run job `virustotal` của run 44925260875 →
   `gh release edit v26.11.2101 --draft=false -R tsudev-org/tsucontact` → deploy website (`cd website && npm run deploy`,
   wrangler đã đăng nhập) → PR scoop-bucket `bucket/tsucontact.json` 26.11.2101 (url/hash mới, checkver
   `^v(\d{2}\.\d{1,2}\.\d{4})$`, autoupdate `tsucontact_$version_windows-x64-setup.exe`, `python3 tools/catalog.py`;
   mẫu: scoop-bucket#25) → điền `logs/store/antivirus.md`.
3. Phòng báo nhầm lâu dài: bootloader PyInstaller dựng từ nguồn hoặc `--onedir` + bộ cài; xin SignPath Foundation.
4. winget `tsudev.TsuContact`: PR winget-pkgs #477388 (26.11.1601) còn chờ moderator; sau khi nhận mới gửi 26.11.2101
   (komac, `WINGET_TOKEN` có sẵn; khoá ở `~/.config/tsudev/winget.env`).

## 3. Lưu ý kỹ thuật

- Màu/bo góc/font CHỈ đọc từ `.standards/tokens/products/contact.json`; không khai lại ở repo.
- Qt bỏ `border-radius` > nửa chiều cao ⇒ dùng `Tokens.pill(h)` (AKB LES-20261121-2340-621a).
- Ảnh chụp: `node website/scripts/chup-anh.mjs <thư-mục> [url]` (web); ảnh app chụp offscreen bằng `MainWindow.grab()`.
- Khoá VirusTotal: `~/.config/tsudev/virustotal.env` (một dòng khoá thô).
