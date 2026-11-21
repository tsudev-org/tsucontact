# PHIẾU YÊU CẦU - PRO1: lưu cục bộ mặc định, Pro mới có đồng bộ/sao lưu đám mây (tsucontact)

- **Mã phiếu**: 20261119-PRO1 (phiếu con)
- **Từ**: agent-qulythuchi (phiên `qulythuchi-b2`), 19/11/2026, theo yêu cầu trực tiếp của chủ dự án
- **Đến**: phiên kế tiếp của repo `tsucontact`
- **Trạng thái**: ĐÓNG 21/11/2026 - không có Pro (ADR-0002), xem mục 4
- **Phiếu gốc (ĐỌC TRƯỚC)**: `~/projects/logs/handover/20261119-PRO1_ke-hoach-luu-cuc-bo-pro-dong-bo-toan-he.md` - mục 1 (yêu cầu nguyên văn tóm tắt), 2 (nguyên tắc N1-N8), 3 (thông báo nhiều
  thiết bị, chu kỳ 30 ngày), 5 (khung việc mỗi repo), 7 (nghiệm thu), 8 (câu hỏi 👤). Phiếu này THAY hàng T7 của
  `~/projects/logs/handover/20261119-01_ke-hoach-toan-he-v3.8.0.md` cho repo này.

## 1. Việc riêng của repo này

Dịch vụ Python, không giữ dữ liệu người dùng cuối cần đồng bộ ⇒ **không có Pro**. Chỉ áp N5/N6: giới hạn tần suất, giới hạn thân, lùi thời gian thử lại, không log nội dung liên hệ. Kiểm kê và ghi kết quả.

## 2. Khung việc (tóm tắt phiếu gốc mục 5)

1. Kiểm kê: dữ liệu nào đang rời thiết bị, nằm ở đâu ⇒ ghi mục 4 dưới đây.
2. ADR riêng: phần nào là Pro, cách ân hạn cho người dùng cũ, kênh thanh toán theo PRODUCT_POLICY 3.3/4.3.
3. Mã: đọc quyền lợi (JWS tsudev, đệm ≤ 7 ngày), gate Pro ở MÁY CHỦ, thông báo nhiều thiết bị (5 test bắt buộc), màn
   Pro/Ủng hộ, huy hiệu PRO-C, vi + en, test.
4. Đo phản hồi thao tác chính (< 100 ms) và chịu tải (nếu có máy chủ), ghi vào PR.
5. Phiếu rà soát bảo mật + THREAT_MODEL. Không tự tạo khoá/tài khoản thanh toán thật ⇒ việc 👤.

## 3. Việc cần chủ dự án (👤)

Xem phiếu gốc mục 8 (giá Pro, ân hạn, nơi đặt dịch vụ đồng bộ dùng chung, ngoại lệ nhắc 30 ngày).

## 4. Kết quả xử lý (phiên nhận điền)

- 21/11/2026 - phiên agent-contact (tsucontact-5b): **ĐÓNG**. Kiểm kê + quyết định ở `docs/adr/0002-khong-co-pro-dong-bo.md`:
  app và website không gửi dữ liệu người dùng nào ra khỏi máy (không mã mạng, QtNetwork bị loại khỏi gói, website tĩnh
  không biểu mẫu/đo lường); **không có Pro, không đồng bộ**; N5/N6 không có bề mặt (không máy chủ); Ủng hộ giữ liên kết
  `tsudev.com/ung-ho`. Không có việc 👤.

## 5. Đã chốt (19/11/2026, bổ sung sau khi mở phiếu)

Chủ dự án giao agent chốt mọi câu hỏi mở và xác nhận **chưa có người dùng thật** ⇒ phiếu gốc mục 8 ĐÃ CHỐT, mục 9
là **HỢP ĐỒNG CHUNG** (mọi repo dùng đúng định danh, không tự đặt khác): gói chung **TsuDEV Pro 49.000 ₫/tháng,
490.000 ₫/năm**; Ủng hộ 20/50/100/200 nghìn; Play `tsudev_pro` (`thang`/`nam`) + `ung_ho_20k`…`ung_ho_200k`; JWS
quyền lợi (ES256, `exp` ≤ 7 ngày, `badge`, `devices_30d`); HTTP 402 `pro_required`; mã cài đặt `X-Tsu-Installation`;
dịch vụ đồng bộ dùng chung ở repo mới `tsudev-org/tsusync`; huy hiệu `TsuBadge`; nội dung thông báo vi/en nguyên văn.
Pro hết hạn: chặn đẩy, kéo/xuất 90 ngày, báo trước 30 và 7 ngày, dữ liệu trên thiết bị không bao giờ bị xoá.

Làm được NGAY (không phụ thuộc PRO-B/PRO-D): kiểm kê, ADR, màn Pro/Ủng hộ, thông báo nhiều thiết bị (nguồn quyền lợi giả
trong test), tắt mọi đường gửi dữ liệu người dùng lên mạng ở bản miễn phí. Thứ tự toàn hệ: phiếu gốc mục 9.5.


