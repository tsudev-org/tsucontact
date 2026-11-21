# PHIẾU YÊU CẦU - Bản sắc riêng của Tsu Contact (tsudev-standards v5.0.0)

- **Mã phiếu**: 20261121-STD50
- **Từ**: phiên tsudev-standards, 21/11/2026 - **Đến**: phiên kế tiếp của `tsucontact`
- **Trạng thái**: ĐÓNG 21/11/2026 (PR #39 + #40, deploy contact.tsudev.com, app phát hành 26.11.2101)
- **Nguồn**: https://github.com/tsudev-org/tsudev-standards/releases/tag/v5.0.0 - `docs/DESIGN_SYSTEM.md` mục 1.2,
  CHANGELOG 5.0.0 "Hướng dẫn nâng cấp"
- **Bối cảnh**: chủ dự án muốn mỗi sản phẩm có đặc trưng nổi bật riêng (màu, giao diện, bố cục). Trước v5.0.0, 9/11
  sản phẩm dùng cùng một màu xanh. Từ v5.0.0: nền/chữ/trạng thái/tiếp cận là chung; màu nhấn, bố cục, bo góc, hoạ
  tiết, font tiêu đề là riêng, khai ở `.standards/tokens/products/contact.json` - KHÔNG tự khai lại tại repo này.

## Bản sắc đã chốt cho `tsucontact`

| Trường | Giá trị |
| --- | --- |
| `data-product` | `contact` |
| Màu chính Tối / Sáng | `#F182BA` / `#AD447C` (hue OKLCH 350; lý do: logo xám đá + bạc hà; bạc hà trùng TsuDisk (logo TsuDisk xanh ngọc chiếm 67%) nên nhận hồng san hô ấm của danh bạ con người) |
| Bố cục `layout` | `cong-cu` - vùng thao tác chính (kéo thả/chọn tệp/nút chạy) ngay màn đầu, căn giữa; giới thiệu nằm dưới |
| Bo góc `shape` | `tron` - 8/14/20px, nút viên thuốc 999px |
| Hoạ tiết `motif` | `the-xep` (tĩnh, ở hero + `og-image`, phủ ≤ 15%) |
| Font tiêu đề | Nunito (tự host woff2 bộ `vietnamese`, tối đa 2 độ đậm) |

Muốn đổi bất kỳ giá trị nào: PR vào tsudev-standards (sửa `hue`/`layout`... + chạy `gen-product-palette.mjs`), cổng
kiểm chống trùng phải xanh. KHÔNG ghi đè tại repo này.

## Việc cần làm - chia hai PR, mỗi PR một phiên

**PR 1 - màu + hình** (`feat(ui): bản sắc contact theo tsudev-standards v5.0.0`):
1. Sync `.standards/` lên v5.0.0 (bước `curl` sync-standards.sh trước, theo `docs/SYNC.md`).
2. Web: nạp `.standards/tokens/tokens.css` rồi `.standards/tokens/products.css`; `<html data-product="contact">` (cạnh
   `data-theme`). Desktop/di động: gộp đè `products/contact.json` lên `color.light`/`color.dark` lúc build.
3. Xoá bảng màu tự khai (`palette.css`, `extensions.*.json`, dải `--color-*` riêng) và mã màu cứng còn sót.
4. Giá trị đã lưu `warm` đọc thành `light` (khối `warm` đã gỡ khỏi token).
5. Nút dùng `var(--radius-control)`; h1-h3 và số liệu lớn dùng `var(--font-display)`.
6. Ảnh chụp trước/sau, Sáng + Tối, đính vào PR. Cổng kiểm + test xanh.

**PR 2 - bố cục** (`feat(ui): bố cục cong-cu + hoạ tiết the-xep`):
1. Dựng phần THÂN trang chủ website / màn hình đầu app theo `cong-cu`; header, khu tài khoản, chân trang, bộ chọn
   giao diện giữ theo `ECOSYSTEM_IDENTITY.md` mục 4.
2. Hoạ tiết `the-xep` tĩnh ở hero, vẽ bằng `accent`/`glow`; sinh lại `og-image.png` cùng hoạ tiết.
3. Ảnh chụp trước/sau, Sáng + Tối.

## Việc riêng của repo này

- Màu chính là hồng san hô (hue 350), KHÔNG phải bạc hà của logo: bạc hà trùng TsuDisk (cổng kiểm chặn). Logo giữ nguyên.

## Kết quả xử lý

- 21/11/2026 - phiên agent-contact (tsucontact-5b):
  - **PR 1 #39** (merge `ca5973c`): sync v5.0.0; web nạp `.standards/tokens/tokens.css` + `products.css`,
    `data-product="contact"`; xoá `palette.css`, `src/styles/tokens.css`, `tokens/extensions.tsucontact.json`; bo góc
    `--radius-*`, nút `--radius-control`; h1-h3 Nunito tự host (latin + vietnamese, 600/700). App: `src/services/tokens.py`
    gộp `products/contact.json` (màu + bộ `tron` + `fontDisplay`), Qt kẹp bán kính viên thuốc ≤ nửa chiều cao
    (`Tokens.pill`), Nunito đi kèm `.exe`. `warm` → `light` vẫn giữ (test sẵn có). Ảnh trước/sau: `docs/anh-chup/20261121-std50/`.
  - **PR 2 #40** (merge `364165d`): trang chủ `cong-cu` (nút tải `.exe` + lệnh Scoop ngay màn đầu), hoạ tiết `the-xep`
    ở hero + `og-image.png` (màu đọc từ `products/contact.json`); app có trang Bắt đầu (vùng kéo thả lớn căn giữa).
  - Kiểm: pytest 97 passed, a11y 9 trang × 2 chế độ 0 lỗi, check-theme 0 lỗi, brand-assets khớp, CI 10/10 xanh.
  - Deploy `contact.tsudev.com` sau mỗi PR (Worker `tsucontact`). App mang bản sắc mới từ bản 26.11.2101. 
