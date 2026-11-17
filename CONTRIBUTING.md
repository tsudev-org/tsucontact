# Đóng góp cho Tsu Contact

_English summary below._

Cảm ơn bạn quan tâm. Tsu Contact là công cụ ngoại tuyến chuyển danh bạ CSV sang vCard (.vcf).

## Báo lỗi, đề xuất

- **Lỗi**: mở [issue](https://github.com/tsudev-org/tsucontact/issues/new/choose) theo mẫu "Báo lỗi" - ghi phiên bản,
  Windows, các bước tái hiện. **Đừng đính kèm danh bạ thật**: dùng tệp CSV giả lập.
- **Đề xuất tính năng**: mẫu "Đề xuất".
- **Lỗ hổng bảo mật**: KHÔNG mở issue công khai - xem [SECURITY.md](SECURITY.md).

## Gửi thay đổi (pull request)

1. Fork, tạo nhánh từ `main`.
2. Cài môi trường: Python 3.11+, `python -m pip install --require-hashes -r requirements.txt -r requirements-dev.txt`.
3. Viết mã kèm **test**: mọi chức năng mới hoặc lỗi được sửa phải có test trong `tests/` (pytest; dữ liệu đầu vào
   ngẫu nhiên dùng Hypothesis khi hợp lý). PR thiếu test cho thay đổi hành vi sẽ không được nhận.
4. Chạy cổng như CI trước khi gửi:
   ```bash
   python -m ruff check .
   python -m pytest -q tests
   ```
   CI chạy lại trên Linux và Windows, kèm `pip-audit` (lỗ hổng phụ thuộc) và `gitleaks` (lộ bí mật). Lint phải 0 cảnh báo.
5. Commit theo [Conventional Commits](https://www.conventionalcommits.org/) (`feat:`, `fix:`, `docs:`...).
6. Mở PR vào `main`; mô tả thay đổi và cách đã kiểm.

Phụ thuộc mới phải có giấy phép tương thích Apache-2.0 và được ghim hash trong `requirements*.txt`.

---

## English summary

- **Bugs / feature requests**: open an issue using the templates. Do not attach real contact data.
- **Security issues**: report privately, see [SECURITY.md](SECURITY.md).
- **Pull requests**: branch from `main`, add **tests** (pytest, Hypothesis where useful) for every new feature or bug
  fix, run `python -m ruff check .` and `python -m pytest -q tests` (zero lint warnings), use Conventional Commits.
  CI re-runs everything on Linux and Windows together with `pip-audit` and `gitleaks`. New dependencies must be
  Apache-2.0 compatible and hash-pinned.
