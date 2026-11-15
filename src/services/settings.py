# -*- coding: utf-8 -*-
"""Tùy chọn người dùng: lưu trong thư mục cấu hình riêng của người dùng, ghi nguyên tử.

- Windows: %LOCALAPPDATA%\\tsucontact\\settings.json
- Linux/macOS: $XDG_CONFIG_HOME/tsucontact (mặc định ~/.config/tsucontact)

Bản <= 26.11.1001 dùng thư mục `tsudev-contact`: lần chạy đầu tự chuyển sang tên mới (`migrateLegacyConfig`).

KHÔNG dùng thư mục temp dùng chung (bản cũ dùng %TEMP% / /tmp: đường dẫn đoán trước được,
máy nhiều người dùng trên Linux có thể bị cài symlink). File này chỉ chứa tùy chọn hiển
thị - tuyệt đối không chứa dữ liệu danh bạ. Mọi giá trị đọc ra đều được kiểm lại.
"""
from __future__ import annotations

import json
import os
import sys
import tempfile

APP_DIRNAME = 'tsucontact'
LEGACY_DIRNAME = 'tsudev-contact'   # tên trước 16/11/2026
SETTINGS_FILE = 'settings.json'
MAX_SETTINGS_BYTES = 64 * 1024

THEMES = ('light', 'dark', 'system')   # chế độ Ấm đã bỏ (phiếu 20261110-05); 'warm' cũ đọc thành 'light'
LANGUAGES = ('vi', 'en')
PAGE_SIZES = (10, 20, 50, 100, 200)       # .standards/docs/DATA_TABLE.md mục 2

DEFAULTS = {
    'theme': 'dark',
    'language': 'vi',
    'pagesize.preview': 10,
    'fixLeadingZero': True,
    'dropDuplicatePhones': False,
}
_VALIDATORS = {
    'theme': lambda v: v in THEMES,
    'language': lambda v: v in LANGUAGES,
    'pagesize.preview': lambda v: type(v) is int and v in PAGE_SIZES,
    'fixLeadingZero': lambda v: type(v) is bool,
    'dropDuplicatePhones': lambda v: type(v) is bool,
}


def _configBase() -> str:
    if sys.platform == 'win32':
        return os.environ.get('LOCALAPPDATA') or os.path.expanduser(r'~\AppData\Local')
    return os.environ.get('XDG_CONFIG_HOME') or os.path.expanduser('~/.config')


def configDir() -> str:
    return os.path.join(_configBase(), APP_DIRNAME)


def migrateLegacyConfig(base: str | None = None) -> bool:
    """Chuyển thư mục cấu hình tên cũ `tsudev-contact` sang `tsucontact` (một lần).

    Chỉ đổi tên khi thư mục mới chưa có và thư mục cũ là thư mục thật (không theo symlink).
    Lỗi bất kỳ: bỏ qua, app dùng mặc định - tệp chỉ chứa tùy chọn hiển thị.
    """
    base = base or _configBase()
    old, new = os.path.join(base, LEGACY_DIRNAME), os.path.join(base, APP_DIRNAME)
    try:
        if os.path.lexists(new) or not os.path.isdir(old) or os.path.islink(old):
            return False
        os.rename(old, new)
        return True
    except OSError:
        return False


def settingsPath() -> str:
    return os.path.join(configDir(), SETTINGS_FILE)


class Settings:
    """Đọc một lần, ghi nguyên tử mỗi khi đổi. Lỗi đọc/ghi không bao giờ làm sập app."""

    def __init__(self, path: str | None = None):
        self.path = path or settingsPath()
        self._values = dict(DEFAULTS)
        self._load()

    def _load(self) -> None:
        try:
            if os.path.getsize(self.path) > MAX_SETTINGS_BYTES:
                return
            with open(self.path, encoding='utf-8') as f:
                stored = json.load(f)
        except (OSError, ValueError):
            return
        if isinstance(stored, dict):
            if stored.get('theme') == 'warm':   # người từng chọn Ấm muốn nền sáng
                stored['theme'] = 'light'
            for key, value in stored.items():
                if key in _VALIDATORS and _VALIDATORS[key](value):
                    self._values[key] = value

    def get(self, key: str):
        return self._values[key]

    def set(self, key: str, value) -> None:
        if key not in _VALIDATORS:
            raise KeyError(f'Tùy chọn không hợp lệ: {key}')
        if not _VALIDATORS[key](value):
            raise ValueError(f'Giá trị không hợp lệ cho {key}: {value!r}')
        self._values[key] = value
        self._save()

    def _save(self) -> None:
        directory = os.path.dirname(self.path)
        try:
            os.makedirs(directory, exist_ok=True)
            fd, tempPath = tempfile.mkstemp(prefix='.settings-', suffix='.tmp', dir=directory)
            try:
                with os.fdopen(fd, 'w', encoding='utf-8') as f:
                    json.dump(self._values, f, ensure_ascii=False, indent=2)
                os.replace(tempPath, self.path)
            except BaseException:
                try:
                    os.unlink(tempPath)
                except OSError:
                    pass
                raise
        except OSError:
            pass  # đĩa đầy / chỉ-đọc: mất tùy chọn hiển thị, app vẫn chạy


def removeLegacyData() -> list[str]:
    """Xóa dữ liệu các bản cũ để lại trong thư mục temp, gồm CSDL chứa danh bạ (PII).

    Bản <= 26.8.2002 ghi `contacts_data.db` (toàn bộ danh bạ lần chuyển gần nhất) vào
    %TEMP%\\tsudev-contact (tên cũ) và không bao giờ xóa. Chỉ xóa đúng các tên file app đã tạo,
    và chỉ khi đó là file thường (không theo symlink).
    """
    removed = []
    legacyDir = os.path.join(tempfile.gettempdir(), LEGACY_DIRNAME)
    for name in ('contacts_data.db', 'contacts_data.db-journal', 'settings.json'):
        path = os.path.join(legacyDir, name)
        try:
            if os.path.isfile(path) and not os.path.islink(path):
                os.remove(path)
                removed.append(path)
        except OSError:
            pass
    try:
        if os.path.isdir(legacyDir) and not os.path.islink(legacyDir) and not os.listdir(legacyDir):
            os.rmdir(legacyDir)
    except OSError:
        pass
    return removed
