# ADR-0002 - Tsu Contact không có gói Pro, không đồng bộ/sao lưu đám mây

- **Trạng thái**: Chấp nhận - 21/11/2026
- **Bối cảnh**: phiếu toàn hệ `20261119-PRO1` (lưu cục bộ mặc định, Pro mới có đồng bộ/sao lưu đám mây; gói chung
  TsuDEV Pro 49.000 ₫/tháng - 490.000 ₫/năm, hợp đồng chung ở phiếu gốc mục 9). Bản sao phiếu:
  `logs/handover/20261119-PRO1_luu-cuc-bo-pro-dong-bo.md`.

## Kiểm kê dữ liệu rời thiết bị (đo 21/11/2026 trên `main`)

| Thành phần | Dữ liệu người dùng rời máy? | Bằng chứng |
| --- | --- | --- |
| App Windows (`tsucontact_*.exe`) | **Không.** Danh bạ chỉ nằm trong RAM khi app mở; settings (giao diện, ngôn ngữ) ở `%LOCALAPPDATA%\tsucontact\settings.json`; tệp vCard/báo cáo lỗi chỉ ghi vào nơi người dùng chọn | `src/` không import `socket`/`urllib`/`requests`/`http.client`; `tsucontact.spec` loại `PySide6.QtNetwork`, `QtNetworkAuth`, `QtWebSockets` khỏi gói; không có trình tự cập nhật |
| Website `contact.tsudev.com` | **Không.** Trang tĩnh (Cloudflare Workers Static Assets, không mã Worker), không biểu mẫu, không đo lường | `website/wrangler.jsonc`; JavaScript phía trình duyệt duy nhất là `public/theme.js` + `public/chep.js` (localStorage `tsudev-theme`, nút Chép). `fetch` trong `src/lib/noi-dung.ts` chạy LÚC BUILD (GitHub Releases API, catalog kho gói), không chạy ở trình duyệt |
| Máy chủ/API riêng | Không có | Repo không có thành phần dịch vụ |

## Quyết định

1. **Không có tính năng Pro, không đồng bộ, không sao lưu đám mây.** Việc của app là chuyển đổi một lần (CSV → vCard);
   không có dữ liệu cần giữ giữa các máy. Thêm đồng bộ sẽ đưa danh bạ (PII, mức D2) ra khỏi máy - trái hạng sản phẩm C
   và cam kết "danh bạ không rời khỏi máy" trên website.
2. **Ủng hộ** giữ như hiện tại: nút trong hộp Giới thiệu mở `https://tsudev.com/ung-ho` (tự nguyện, không mở khoá gì).
   Không cần huy hiệu PRO-C, JWS quyền lợi, `X-Tsu-Installation`, thông báo nhiều thiết bị - app không đăng nhập,
   không gọi mạng.
3. N5/N6 của phiếu gốc (giới hạn tần suất, giới hạn thân, lùi thời gian thử lại, không log nội dung liên hệ) **không có
   bề mặt để áp**: không có máy chủ. Trần đầu vào của lõi (`src/engine`: kích thước tệp, số dòng, số cột, độ dài ô) đã
   có và có test.
4. Nếu sau này cần đồng bộ (ví dụ lưu mẫu ghép cột), làm theo hợp đồng chung PRO1 mục 9 qua `tsudev-org/tsusync`, chỉ
   cho cấu hình - KHÔNG BAO GIỜ cho nội dung danh bạ - và mở ADR mới thay ADR này.

## Hệ quả

- Không có việc 👤 về giá/thanh toán cho repo này.
- Ân hạn người dùng cũ: không áp dụng (không có gì bị khoá).
