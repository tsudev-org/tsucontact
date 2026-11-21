# Hồ sơ báo nhầm antivirus - Tsu Contact

Theo `.standards/docs/DISTRIBUTION_TRUST.md` mục 3-3.1. Agent soạn; chủ dự án (👤) nộp ở cổng cần tài khoản/email.

## Bản 26.11.2101 (phát hiện 21/11/2026, hạn nộp nội bộ 23/11/2026)

| Trường | Giá trị |
| --- | --- |
| Sản phẩm | Tsu Contact 26.11.2101 (TsuDEV) - chuyển danh bạ CSV sang vCard, chạy ngoại tuyến |
| Tệp | `tsucontact_26.11.2101_windows-x64-setup.exe` (PyInstaller một tệp, Python 3.11 + PySide6) |
| SHA-256 | `528e524195de8169f9511622cd43ecf38faee953bf0d40273fa27483c62a6125` |
| VirusTotal | https://www.virustotal.com/gui/file/528e524195de8169f9511622cd43ecf38faee953bf0d40273fa27483c62a6125 - **2/71**: Bkav Pro `W32.Malware.7FCDDA8B`, APEX `Malicious`; 69 engine sạch (gồm Microsoft, Kaspersky, ESET, Bitdefender, Avast) |
| Mã nguồn | https://github.com/tsudev-org/tsucontact - thẻ `v26.11.2101`, commit `8b6c8b2f8e9eea03e92c446e91cbbae0ee48e91b` |
| Build | GitHub Actions `build-release-win.yml`, run 44925260875 - chứng thực nguồn gốc SLSA: `gh attestation verify tsucontact_26.11.2101_windows-x64-setup.exe --repo tsudev-org/tsucontact` |
| SBOM | `tsucontact_26.11.2101_windows-x64-setup.cdx.json` (CycloneDX, đính cùng Release) |
| Hành vi | Không kết nối mạng (QtNetwork bị loại khỏi gói), không ghi registry, không tự khởi động, không tải mã. Chỉ đọc tệp CSV người dùng chọn và ghi tệp .vcf/.csv vào nơi người dùng chọn; cài đặt giao diện ở `%LOCALAPPDATA%\tsucontact\settings.json` |
| Chính sách | Quyền riêng tư: https://tsudev.com/privacy - Bảo mật: https://github.com/tsudev-org/tsucontact/blob/main/SECURITY.md - Kiến trúc: https://contact.tsudev.com/bao-mat/kien-truc/ |
| Chữ ký Authenticode | Chưa có (chưa có chứng chỉ; SignPath Foundation là hướng miễn phí) |

### Nơi nộp (chỉ hãng ĐANG gắn cờ)

1. **Bkav** - kênh báo nhầm trên trang chính thức bkav.com.vn (tra địa chỉ hiện hành lúc nộp, agent chưa xác minh): đính tệp `.exe` (nén zip, mật khẩu
   `infected`), dán bảng trên. Tiêu đề gợi ý: `False positive: W32.Malware.7FCDDA8B - Tsu Contact 26.11.2101`.
2. **APEX** (engine học máy trên VirusTotal) - qua nút đề nghị phân tích lại trên VirusTotal (Reanalyze)
   sau 24-48 giờ; nếu cờ còn, liên hệ nhà cung cấp theo trang engine trên VirusTotal.
3. Sau khi gỡ: chạy lại job `virustotal` (Actions → Build & Release → Re-run failed jobs) - xanh thì Release tự giữ
   nguyên ghi chú, bỏ nháp bằng tay: `gh release edit v26.11.2101 --draft=false -R tsudev-org/tsucontact`.

### Phòng lâu dài (việc agent, phiên sau)

PyInstaller `--onefile` là mẫu hay bị engine học máy gắn cờ (chuẩn khuyến nghị tránh). Hướng: dựng bootloader
PyInstaller từ nguồn trên runner (`PYINSTALLER_COMPILE_BOOTLOADER=1`, sdist có hash trong `requirements-dev.txt`) hoặc
chuyển `--onedir` + bộ cài; sau đó xin ký Authenticode miễn phí qua SignPath Foundation (đủ điều kiện: Apache-2.0).
