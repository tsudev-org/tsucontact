# PHIẾU BÀN GIAO - Bộ cài Inno + zip portable, phát hành 26.11.2201 (thay 26.11.2101)

- **Từ**: phiên agent-tsucontact (tsucontact-6), 22/11/2026 - **Đến**: phiên kế tiếp của `tsucontact`
- **Trạng thái**: MỞ - chỉ còn việc chờ bên ngoài (mục 2)

## 1. Đã xong (đều đã đo)

| Việc | Kết quả |
| --- | --- |
| VirusTotal 26.11.2101 | Đo lại 22/11: **3/74** (Bkav, Microsoft `Trojan:Win32/Wacatac.B!ml`, APEX) ⇒ không công bố, Release giữ nháp |
| Thử nghiệm đóng gói | 2 lượt CI (run 45023853651, 45024719995), 7 biến thể - bảng ở `docs/store/antivirus.md` |
| PR #44 | spec chỉ onedir; `packaging/inno/tsucontact.iss`; `build-win.ps1` ra `-setup.exe` (Inno) + `-portable.zip`; workflow dựng bootloader từ nguồn, chứng thực + quét cả `.zip`; website nhận 2 loại gói |
| v26.11.2201 | Release tạo NHÁP trước → tag → run 45027781335 xanh, VirusTotal **0/74** cả bộ cài và zip → `sha256sum -c`, `gh attestation verify` (exe, zip, SUMS) đạt → công bố |
| Thử thật trên Windows | Bộ cài im lặng `/VERYSILENT /CURRENTUSER`: cài không admin, mở app, mục gỡ cài đặt `26.11.2201 / TsuDEV`, gỡ sạch; zip giải nén chạy được |
| Website | `npm run deploy`; `/tai-ve/` hiện "Bộ cài (khuyên dùng)" + "Bản chạy ngay", nút trang chủ trỏ bộ cài 2201 |
| Scoop | scoop-bucket#27 (merge): `tsucontact` 26.11.2201 dùng zip, checkver `^v(\d{2}\.\d{1,2}\.\d{4})$`, CI cài thật xanh |
| winget | PR cũ #477388 bị bot đóng (nhánh rỗng); gửi mới **#486443** (inno, user scope), `winget validate` đạt |

## 2. Việc còn lại (cập nhật lượt 2, 22/11/2026 - chủ dự án uỷ quyền làm tiếp)

1. winget #486443: bước 1-7 của pipeline kiểm định ĐẠT (manifest, URL, quét bộ cài, CLA); bước 8 cài thử đang chạy lúc
   kết phiên; sau đó chờ moderator. Bot báo lỗi ⇒ sửa trên nhánh `tsudev-tsudev/winget-pkgs:tsudev.TsuContact-26.11.2201`
   (API contents, gh mặc định). Merge xong: kênh winget ở tsudev `packages/ui/src/lib/ecosystem.ts` (phiếu cho repo tsudev).
2. SignPath: **HOÃN** theo lựa chọn của chủ dự án (1/6 ngưỡng; lotus-share bị từ chối 12/11 vì thiếu uy tín công khai).
   Đã sẵn sàng (PR #46, deploy): trang https://contact.tsudev.com/code-signing-policy/, đơn `tools/signpath/don.json`,
   công cụ `nop-don.mjs` (điền thử đã chạy, ảnh đúng mọi ô). Người nộp: `~/.config/tsudev/signpath-applicant.json`.
   Chỉ gửi (`--submit`) khi đạt >= 4/6 VÀ toàn hệ chọn tsucontact là dự án nộp (mỗi lần một dự án).
3. 👤 Xoay khoá `~/.config/tsudev/winget.env` (lỡ in ra nhật ký phiên cục bộ ở lượt 1).
4. ✅ Release nháp `v26.11.2101` ĐÃ XOÁ (gồm tệp `.exe` bị gắn cờ); GIỮ thẻ git `v26.11.2101` (CHANGELOG + hồ sơ antivirus
   trỏ tới, không viết lại lịch sử thẻ đã đẩy).

## 3. Lưu ý kỹ thuật

- Cờ học máy với bộ cài Inno không ổn định (cùng cấu hình: 0/74 rồi 1/74 DeepInstinct). Bị cờ ⇒ dựng lại (tệp mới) trước
  khi nộp báo nhầm. Zip luôn 0/74.
- PowerShell trên máy Windows này hỏng `Microsoft.PowerShell.Utility` (không có `Start-Sleep`, `Format-Table`,
  `Add-Type`): dùng `[Threading.Thread]::Sleep()`, giải nén bằng Python từ WSL.
- Máy WSL không có ruff/pytest/komac; kiểm mã bằng CI của PR.
- `scripts/build-win.ps1` cần Inno Setup 6 (`-Iscc`); runner `windows-latest` có sẵn.
