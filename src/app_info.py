# -*- coding: utf-8 -*-
"""Thông tin định danh ứng dụng - khai báo một nơi duy nhất."""

# Tên sản phẩm Tsu Contact (chủ dự án chốt 16/11/2026, docs/adr/0001-ten-san-pham-tsu-contact.md).
APP_NAME = "Tsu Contact"
APP_SLUG = "tsucontact"
# Quy ước: docs/DESIGN_SYSTEM.md mục 6 - {YY}.{M}.{DD}{NN}
# (26.8.2002 = bản phát hành thứ 02 ngày 20/08/2026). Bản trước quy ước: "5.2".
APP_VERSION = "26.11.2101"
APP_OS = "windows"
APP_ARCH = "x64"
# Nhận diện hệ sinh thái: .standards/docs/ECOSYSTEM_IDENTITY.md mục 2.3.
APP_AUTHOR = "TsuDEV"
# PUBLISHER là ĐỊNH DANH máy đọc (QSettings organizationName -> nơi lưu cài đặt, AppUserModelID): giữ chữ thường,
# đổi là máy đã cài mất cài đặt. Tên hiển thị (CompanyName, bản quyền) dùng PUBLISHER_DISPLAY - tsudev-standards v3.8.0.
PUBLISHER = "tsudev"
PUBLISHER_DISPLAY = "TsuDEV"
ECOSYSTEM_URL = "https://tsudev.com"
# Trang sản phẩm - thay cho liên kết Facebook cũ (chủ project không còn dùng, 10/11/2026).
SUPPORT_URL = "https://contact.tsudev.com"
REPO_URL = "https://github.com/tsudev-org/tsucontact"
# Ủng hộ tự nguyện: app chỉ mở trang trung tâm, không nhúng số tài khoản/QR
# (phiếu 20261112-01 + quyết định 20261112-02 mục 2).
DONATE_URL = "https://tsudev.com/ung-ho"
COPYRIGHT = "Copyright (c) 2026 TsuDEV"

# Tên file phát hành (không phần mở rộng) - dùng cho PyInstaller và scripts/build-win.ps1.
# Khuôn V1 (VERSIONING.md mục 2.2, từ 26.11.2101): {tên-gói}_{phiên bản}_{os}-{arch}-{loại};
# bản <= 26.11.1601 là `_x64-setup`.
RELEASE_BASENAME = f"{APP_SLUG}_{APP_VERSION}_{APP_OS}-{APP_ARCH}-setup"
