# ADR-0001: Tên sản phẩm Tsu Contact, định danh `tsucontact`

- **Trạng thái**: Đã chấp nhận (16/11/2026, chủ dự án)
- **Tiền lệ**: `tsudev-org/tsufiles` ADR-0003 (đổi `tsudev-files` -> TsuFiles, `tsufiles`)

## 1. Bối cảnh

Chủ dự án (16/11/2026) chốt tên sản phẩm mới **Tsu Contact** cho thống nhất với hệ sinh thái tsudev (TsuFiles,
TsuGameLabs), đồng thời đổi tên repo và thư mục `tsudev-contact` thành `tsucontact`. Các tên cũ (`tsudev-contact`,
`tsudev Contacts`, `Contacts`) phải biến mất khỏi sản phẩm, trừ chỗ lịch sử hoặc tương thích bắt buộc giữ.

## 2. Quyết định

| Hạng mục | Trước | Sau |
| --- | --- | --- |
| Tên hiển thị (app, website, tài liệu) | `tsudev-contact`, `Contacts` | **Tsu Contact** |
| Định danh máy (`APP_SLUG`, gói, Worker) | `tsudev-contact` | `tsucontact` |
| Repo GitHub | `tsudev-org/tsudev-contact` | `tsudev-org/tsucontact` (đổi 16/11/2026) |
| Tệp phát hành | `tsudev-contact_<v>_x64-setup.exe` | `tsucontact_<v>_x64-setup.exe` (khuôn `VERSIONING.md` mục 2) |
| Thư mục cấu hình | `%LOCALAPPDATA%\tsudev-contact` | `%LOCALAPPDATA%\tsucontact`, tự chuyển một lần (`migrateLegacyConfig`) |
| Tệp đóng gói, điểm vào | `Contacts.spec`, `contacts.pyw` | `tsucontact.spec`, `tsucontact.pyw` |
| Token màu riêng | `tokens/extensions.tsudev-contact.json` | `tokens/extensions.tsucontact.json` |
| Mã winget (chưa phát hành) | `tsudev.Contact` | `tsudev.TsuContact` |
| Gói Scoop | `tsudev-contact` | `tsucontact` mới; `tsudev-contact` thành gói chuyển tiếp (mẫu `tsudev-lotus`) |
| Worker Cloudflare | `tsudev-contact` | `tsucontact` (giữ tên miền `contact.tsudev.com`) |
| Ủng hộ | chưa có | nút "Ủng hộ tsudev" trong hộp Giới thiệu + chân trang website + `.github/FUNDING.yml`, đều mở `https://tsudev.com/ung-ho` (quyết định `20261112-02`) |

Giữ nguyên: tên miền `contact.tsudev.com`, logo `logo-contact`, giấy phép Apache-2.0 và dòng bản quyền, lịch sử
(`CHANGELOG.md` bản cũ, `logs/`).

## 3. Hệ quả

- App ngoại tuyến, không có trình tự cập nhật, nên đổi tên tệp phát hành không làm bản đã cài mắc kẹt. Ràng buộc duy
  nhất là `autoupdate` của gói Scoop (đọc tên tệp + `SHA256SUMS.txt`): sửa ở `tsudev-org/scoop-bucket` cùng lúc phát
  hành bản đầu tiên mang tên mới.
- **Cấm vĩnh viễn** tạo lại repo/fork/đổi tên thành `tsudev-contact` trong `tsudev-org` (và `tsudev-tsudev`): chuyển
  hướng GitHub mất ngay, link tải Release cũ và gói Scoop cũ gãy im lặng. Đã ghi vào `~/.claude/CLAUDE.md` của máy
  phát triển.
- Lựa chọn giao diện của người dùng bản cũ được giữ nhờ di trú thư mục cấu hình; dữ liệu tạm bản <= 26.8.2002 trong
  `%TEMP%\tsudev-contact` vẫn được dọn như trước.
