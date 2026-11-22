# STATE.md - Trạng thái project (agent đọc đầu phiên, cập nhật cuối phiên)

> **Phiên kế tiếp:** đọc phiếu `logs/handover/20261122-01_*`. Phiếu toàn hệ 20261117-P2: đọc `~/projects/logs/handover/20261117-P2_ke-hoach-phan-phoi-tin-cay-da-nen-tang.md` hàng 1 (`tsucontact`) ở mục 3
> + `.standards/docs/DISTRIBUTION_TRUST.md` (chuẩn v3.7.0) + `.standards/docs/VERSIONING.md` mục 2. Khuôn thẻ/tên tệp mới chỉ áp
> cho bản phát hành KẾ TIẾP, đọc mục 2.4 (updater đã cài) trước khi đổi.

## Hàng đợi task (làm từ trên xuống)
- [ ] **SignPath Foundation - HOÃN** (👤 chọn 22/11/2026): chỉ nộp khi đạt >= 4/6 ngưỡng (phiếu toàn hệ `20261113-02` mục 5; 22/11 đạt 1/6: 0 sao, 0 người đóng góp ngoài, 149 lượt tải; lotus-share bị từ chối 12/11 vì lý do này) VÀ toàn hệ chọn tsucontact là dự án nộp. Đã sẵn: trang https://contact.tsudev.com/code-signing-policy/ (nguồn `docs/CODE_SIGNING_POLICY.md`), nội dung đơn `tools/signpath/don.json`, người nộp `~/.config/tsudev/signpath-applicant.json` (NGOÀI repo), công cụ `cd website && node ../tools/signpath/nop-don.mjs [--submit] [--headed]` (mặc định chỉ điền thử + chụp ảnh). Được duyệt ⇒ đổi mục "Signing provider" của chính sách sang câu ghi công, tích hợp action SignPath vào `build-release-win.yml`.
- [ ] **winget** `tsudev.TsuContact` ⏳ CHỜ MODERATOR: PR cũ #477388 bị bot ĐÓNG (nhánh rỗng). 22/11/2026 gửi mới **winget-pkgs #486443** - 26.11.2201, `InstallerType: inno`, `Scope: user`, ProductCode `{6F1C2B7E-4A0D-4E5B-9C3A-7D2E1B8F4C60}_is1`, `winget validate` đạt; manifest ở `packaging/winget/manifests/`. Khi merge: thêm `"winget"` vào `channels` + khai `winget: 'tsudev.TsuContact'` ở tsudev `packages/ui/src/lib/ecosystem.ts`. Bản sau: tự động hoá (komac chưa cài ở WSL; `WINGET_TOKEN` có trong secret repo). Gửi PR bằng tài khoản gh mặc định `tsudev-tsudev` (chủ fork), qua API, không clone.
- [x] **Best Practices passing** ✅ 17/11/2026 (phiên tsudev-27): hồ sơ [16836](https://www.bestpractices.dev/projects/16836) passing 100% - câu trả lời `docs/best-practices.json` (mỗi Met có bằng chứng), thêm CONTRIBUTING.md + mẫu issue (#30); huy hiệu ở README. Còn: good first issue (phiếu 20261113-03).
- [x] **QU-STD-AUTH** XONG 11/11/2026: bộ quy ước v3.4.0 (TS-15) xếp repo này hạng C; hạng C không bắt buộc đăng nhập, app chạy trọn ngoại tuyến không tài khoản (`.standards/docs/AUTH_AND_ACCOUNT.md` mục 1).

### Gợi ý (chưa phải task)
- Xóa chứng thư thử nghiệm tự ký còn sót trong kho tin cậy của Windows (phiếu 20260820-03).
- Muốn hết cảnh báo SmartScreen phải mua chứng thư OV/EV.
- Trình cài đặt (shortcut Start Menu, gỡ cài đặt) nếu người dùng cần.

## Đang thực hiện
| Task | Agent | Bắt đầu |
|---|---|---|

## Đã hoàn thành (mới nhất trên cùng)
- 22/11/2026 - **Phiên agent-tsucontact (tsucontact-6)**: VirusTotal bản 26.11.2101 lên 3/74 (thêm Microsoft `Wacatac.B!ml`) ⇒ bỏ bản đó (giữ nháp). Đo 7 cách đóng gói trên CI ⇒ PR #44: onedir + bootloader PyInstaller dựng từ nguồn + bộ cài Inno Setup (lzma2/max không solid) + zip portable. Phát hành **v26.11.2201** (Release nháp trước, tag build: cả hai tệp **0/74**, SHA256SUMS + attestation đạt, cài/chạy/gỡ thật trên Windows) rồi công bố; deploy contact.tsudev.com (trang Tải về hiện bộ cài + zip); Scoop `tsucontact` 26.11.2201 dùng zip (scoop-bucket#27, CI cài thật xanh); winget-pkgs #486443. Phiếu `20261122-01`.
- 21/11/2026 - **Phiên agent-contact (tsucontact-5b)**: phiếu STD50 đóng (PR #39 bản sắc hồng san hô + Nunito + bo `tron`; PR #40 bố cục `cong-cu` + hoạ tiết `the-xep`, trang Bắt đầu của app; deploy contact.tsudev.com 2 lần); phiếu PRO1 đóng (ADR-0002: không Pro, không đồng bộ, không dữ liệu rời máy); phiếu V1 áp cho bản **26.11.2101** (`tsucontact_{v}_windows-x64-setup.exe`, tiêu đề `Tsu Contact {v}`); `.standards` v5.0.0.
- 16/11/2026 - Việc 👤 sau đổi tên, đều đã đo lại: chủ dự án xóa Worker cũ `tsudev-contact` (`contact.tsudev.com` vẫn 200 trên Worker `tsucontact`); JavaScript Detections đã tắt (phiên tsudev-swico-34, tsudev#280; HTML không còn `challenge-platform`); tsudev#276 (TRADEMARKS) chủ dự án duyệt + merge; nội dung hệ sinh thái áp lên Neon (`/docs/gioi-thieu-he-sinh-thai-tsudev` hiện Tsu Contact, `/docs/cai-ung-dung-bang-winget` hiện `tsucontact`); secret `WINGET_TOKEN` đã đặt; thư mục cục bộ là `~/projects/tsucontact`, liên kết tạm `~/projects/tsudev-contact` đã xóa.
- 16/11/2026 - **Đổi tên Tsu Contact** (ADR-0001): repo `tsudev-org/tsucontact`, phát hành **v26.11.1601** (SHA256SUMS ký Sigstore), Worker `tsucontact` deploy `contact.tsudev.com`, Scoop `tsucontact` (scoop-bucket#10), khối Cài bằng lệnh, Ủng hộ -> tsudev.com/ung-ho, Scorecard, README.en.md. PR #26. Bàn giao: phiếu `20261116-01`.
- 11/11/2026 - Giấy phép **Apache-2.0** (chủ project giao phiên đóng gói chọn phương án tối ưu): đồng bộ swico/lotus, có điều khoản bằng sáng chế, là giấy phép OSI (đủ điều kiện ký Authenticode miễn phí qua SignPath), tương thích PySide6 LGPL-3.0 liên kết động. `LICENSE`, `NOTICE` kèm trong `.exe`.
- 10/11/2026 - Phiếu `20261110-05` (giao diện đen + tím kiểu Supabase): website + app PySide6 chỉ Sáng/Tối/Hệ thống, mặc định Tối; màu riêng ở `tokens/extensions.tsudev-contact.json`. Chi tiết: mục Kết quả của phiếu.
- 10/11/2026 - Kết phiên: nhả khóa (commit nhả khóa trước đó bị mất khi tạo lại nhánh website), phiếu bàn giao `20261110-02`.
- 10/11/2026 - Merge #9, #13 (thay #10 bị GitHub tự đóng khi xóa nhánh base), #11, #12; phát hành **v26.11.1001** (Actions: test, build, SBOM, attestation đều đạt; đã tải về kiểm SHA-256 + `gh attestation verify` + chạy thật trên Windows); deploy **https://contact.tsudev.com** (9 trang 200, header bảo mật đủ, HTTP->HTTPS 301); `homepage` repo đổi sang trang này; bật ruleset "Bảo vệ main" (id 26943513, 4 check bắt buộc); merge Dependabot #14 (setup-python v7.1.0, đã đối chiếu SHA) và #16 (playwright 1.65); gửi phiếu `tsudev/logs/handover/20261110-04_*`.
- 10/11/2026 - Nâng cấp toàn diện (4 PR xếp chồng, CI xanh): PR #9 bỏ Facebook, nhận diện tsudev, QU-STD-1/2/BRAND (icon), README hạng C; PR #10 PySide6 + lõi `src/engine` (vá chèn vCard, PII chỉ trong RAM, trần đầu vào, chuẩn hóa SĐT VN), i18n vi/en, QU-STD-TABLE, 84 test, khóa hash, SBOM; PR #11 CI (ruff, pytest Linux+Windows, pip-audit, gitleaks), attestation, Dependabot; PR #12 website contact.tsudev.com (chưa deploy - chờ bản phát hành mới)
- 20/08/2026 - T14: repo chuyển **public**; Actions hết bị chặn, chạy trọn pipeline xanh (run `32291387041`); sửa 2 lỗi workflow (cache pip thiếu requirements.txt, đối chiếu tag khi chạy tay)
- 20/08/2026 - T13 `8470ceb`: `scripts/sign-win.ps1` ký Authenticode + dấu thời gian miễn phí, `build-win.ps1` thêm `-Sign` và tự ghi `release/SHA256SUMS.txt`
- 20/08/2026 - T12 `f528c3a`: `tests/test_gui_smoke.py` + `scripts/test-gui-win.ps1` tự động hóa kịch bản GUI (5 test, chạy thật trên Windows và trên runner CI); phát hiện & sửa lỗi gọi `root.after` từ thread nền
- 20/08/2026 - T11 `4eed8a5`: cửa sổ xem trước dùng nhãn vCard + cột `Dòng CSV` + chú thích cột CSV nguồn (6 test)
- 20/08/2026 - T10: push `main` lên repo private; tạo Release `v26.8.2002` kèm `.exe` + `SHA256SUMS.txt`; thêm workflow tự build khi đẩy tag
- 20/08/2026 - T9: chủ đề Sáng/Ấm/Tối + `src/services/settings.py` (ghi nhớ lựa chọn), 18/18 test
- 20/08/2026 - T8 `a47aa98`: chạy thử GUI thật trên Windows → phát hiện & sửa 2 lỗi (nút mất chữ, đoán cột CSV)
- 20/08/2026 - Build thật: `release/tsudev-contact_26.8.2002_x64-setup.exe` (18.5 MB), đã chạy thử file .exe
- 20/08/2026 - T7: thêm `scripts/build-win.ps1` (deps → test → PyInstaller → `release/`)
- 20/08/2026 - T6: chuẩn hóa tên phát hành - `APP_VERSION=26.8.2001`, `RELEASE_BASENAME` trong `src/app_info.py`, `Contacts.spec` gói 1-file
- 20/08/2026 - T5: tạo repo private `tsudev-tsudev/tsudev-contact`, push `main` (không file PII nào được theo dõi)
- 20/08/2026 - T3+T4 `b947660`: tách `contacts.pyw` → `src/`, giao diện dùng `tokens/`, thêm 8 test, sửa 3 lỗi
- 20/08/2026 - T2 `332c74d`: thêm CHANGELOG / ARCHITECTURE / .env.example, viết lại README
- 20/08/2026 - T1 `5032a7f`: `git init`, ignore dữ liệu danh bạ PII
- 19/08/2026 - Khởi tạo bộ quy ước v1.0.0

## Quyết định quan trọng
- 22/11/2026 - **Đóng gói Windows = onedir + bộ cài Inno Setup + zip portable** (bỏ PyInstaller một tệp): onefile bị antivirus học máy gắn cờ kể cả khi tự dựng bootloader. `-setup.exe` là bộ cài theo người dùng (không admin), AppId Inno `{6F1C2B7E-4A0D-4E5B-9C3A-7D2E1B8F4C60}` KHÔNG đổi. Scoop dùng zip; winget dùng bộ cài. Bootloader dựng từ sdist có hash (`PYINSTALLER_COMPILE_BOOTLOADER=1`) trong workflow. Phát hành: tạo Release NHÁP trước rồi mới đẩy tag; VirusTotal sạch mới `--draft=false`.
- 21/11/2026 - **Bản sắc sản phẩm** (tsudev-standards v5.0.0): màu/bo góc/font/hoạ tiết CHỈ đọc từ `.standards/tokens/products/contact.json` (web: `products.css` + `data-product`; app: `src/services/tokens.py`). KHÔNG tự khai màu ở repo này; muốn đổi ⇒ PR vào tsudev-standards.
- 21/11/2026 - **Không có Pro/đồng bộ** (ADR-0002): app không gọi mạng; nếu sau này cần thì chỉ đồng bộ cấu hình, không bao giờ nội dung danh bạ.
- 16/11/2026 - **Tên sản phẩm Tsu Contact, định danh `tsucontact`** (ADR-0001). Tên `tsudev-contact` cấm tạo lại trong `tsudev-org`/`tsudev-tsudev` (chuyển hướng GitHub). Tệp phát hành giữ hậu tố `-setup` theo VERSIONING.md.
- 10/11/2026 - **PR xếp chồng**: merge PR dưới với `--delete-branch` làm GitHub ĐÓNG (không đổi base) PR phía trên. Cách đúng: merge không xóa nhánh -> `gh pr edit <trên> --base main` -> mới xóa nhánh; đồng bộ bằng `git merge origin/main` (không rebase/force-push).
- 10/11/2026 - Ruleset `main`: bắt buộc PR + 4 check (`Lint + test (Linux)`, `Test (Windows)`, `Quét lộ bí mật (gitleaks)`, `Kiểm quy ước`), nhánh phải cập nhật với main, giải quyết hết hội thoại; admin chỉ bypass qua PR (giống tsudev-files).
- 10/11/2026 - **Giao diện PySide6-Essentials** thay tkinter (exe ~26 MB); lõi `src/engine` thuần Python. Tên `engine` vì `.gitignore` chuẩn chặn đường dẫn `core`.
- 10/11/2026 - **Ngoại tuyến 100%**: không tự kiểm tra cập nhật, QtNetwork bị loại khỏi bản đóng gói. Hạng sản phẩm C.
- 10/11/2026 - **Danh bạ chỉ trong RAM**; settings ở `%LOCALAPPDATA%\tsudev-contact`; khởi động xóa `contacts_data.db` bản cũ để lại trong %TEMP%.
- 10/11/2026 - Website `contact.tsudev.com` = tên miền con 1 cấp, cùng khung Astro + Cloudflare Workers với files.tsudev.com, nằm trong `website/` của repo này.
- 10/11/2026 - Phụ thuộc: sửa `requirements*.in` rồi `scripts/lock-deps.sh` (uv `--universal --generate-hashes`); mọi nơi cài bằng `--require-hashes`.
- 20/08/2026 - **Repo đã chuyển PUBLIC** theo yêu cầu chủ project. Hệ quả đã kiểm chứng: GitHub Actions chạy lại bình thường (hết lỗi chặn thanh toán), phút Actions miễn phí không giới hạn, trang Releases ai cũng tải được. Toàn bộ project không dùng dịch vụ trả phí nào.
- 20/08/2026 - **Ký số**: chỉ dùng công cụ miễn phí có sẵn của Windows (`Set-AuthenticodeSignature` + timestamp RFC3161). Chứng thư tự ký KHÔNG gỡ được SmartScreen trên máy khác - chấp nhận, thay bằng đối chiếu `SHA256SUMS.txt`. Không mua chứng thư OV/EV.
- 20/08/2026 - Workflow **không bật `cache: pip`**: repo không có `requirements.txt` (phụ thuộc khai báo trong `scripts/build-win.ps1`); thêm file chỉ để cache là trùng lặp không đáng, repo public nên không cần tiết kiệm phút.
- 20/08/2026 - **tkinter không an toàn đa luồng**: mọi cập nhật UI từ thread nền phải qua `queue.Queue` do main thread rút (`ContactsApp._pumpUiQueue`), tuyệt đối không gọi `root.after` từ thread khác.
- 20/08/2026 - Phát hành qua **GitHub Releases**, tag `v<APP_VERSION>` (ví dụ `v26.8.2002`). Workflow chỉ chạy theo tag để tiết kiệm phút Actions; runner `windows-latest` tính 2x phút.
- 20/08/2026 - Repo giữ **private**: trang Releases chỉ mở được với tài khoản có quyền. Muốn ai cũng tải được thì phải chuyển repo sang public (chủ project quyết định).
- 20/08/2026 - **Cách chạy GUI/build Windows từ WSL**: gọi `powershell.exe` (interop) dùng Python 3.11 sẵn có trên Windows, tạo venv trong `%TEMP%\tsudev-contact-build`. Không cần cài `python3-tk` trong WSL.
- 20/08/2026 - Chủ đề sáng giữ ttk theme `vista` (native đẹp); ấm/tối bắt buộc `clam` vì `vista` bỏ qua màu nền. Nút hành động chính dùng `tk.Button` để chắc chắn đủ tương phản.
- 20/08/2026 - `scripts/build-win.ps1` phải lưu **UTF-8 CÓ BOM**: PowerShell 5.1 đọc .ps1 không BOM theo ANSI → hỏng tiếng Việt, lỗi cú pháp.
- 20/08/2026 - Không thêm trình cài đặt (Inno/NSIS): `Contacts.spec` chuyển sang **gói 1-file**, chính file `.exe` đó là bản `-setup.exe` theo quy ước. Thêm installer chỉ khi cần shortcut/uninstaller.
- 20/08/2026 - `src/app_info.py` là nguồn duy nhất của tên bản phát hành (`RELEASE_BASENAME`); spec và script build đều đọc từ đó. Bản kế tiếp trong ngày chỉ cần tăng `NN`.
- 20/08/2026 - `src/` dùng `snake_case` cho file/thư mục (Python không import được dấu gạch ngang); hàm/biến giữ `camelCase`.
- 20/08/2026 - Logic chuyển đổi tách khỏi tkinter, giao tiếp qua callback → test được không cần màn hình.
- 20/08/2026 - Giao diện đọc thẳng `tokens/design-tokens.json` qua `src/services/tokens.py`; cỡ chữ truyền tkinter dạng số âm = pixel.
- 20/08/2026 - CSDL tạm đặt ở thư mục temp người dùng, không đặt cạnh file thực thi (chỉ-đọc + chứa PII).
- 19/08/2026 - Dùng Inter làm font chuẩn; token là nguồn chân lý duy nhất; region ưu tiên Singapore → Nhật Bản.
