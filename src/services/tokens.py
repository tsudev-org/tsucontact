# -*- coding: utf-8 -*-
"""Đọc token giao diện theo hai lớp của tsudev-standards v5.0.0 (DESIGN_SYSTEM mục 1.2):
lớp nền chung `.standards/tokens/design-tokens.json` + lớp bản sắc `.standards/tokens/products/contact.json`
(màu nhấn hồng san hô, bộ bo góc `tron`, font tiêu đề). Cả hai là bản sao chỉ-đọc - repo này KHÔNG tự khai màu.
Chỉ hai chế độ: light, dark (chế độ Ấm đã bỏ).

CẤM hard-code màu, cỡ chữ, bo góc, spacing trong `src/` (.standards/AGENTS.md).
Mọi giá trị giao diện lấy qua đối tượng `Tokens`. Module này thuần Python, không phụ
thuộc bộ công cụ giao diện nào.
"""
from __future__ import annotations

import json
from functools import cache

from src.utils.resource_path import resourcePath

TOKENS_FILE = '.standards/tokens/design-tokens.json'
PRODUCT_ID = 'contact'
PRODUCT_FILE = f'.standards/tokens/products/{PRODUCT_ID}.json'
# Bộ bo góc theo DESIGN_SYSTEM mục 1.2.3 (sm, md, lg, control); `control` 999 = nút viên thuốc.
SHAPES = {
    'sac': (2, 3, 4, 3),
    'chuan': (4, 6, 8, 6),
    'mem': (6, 10, 14, 10),
    'tron': (8, 14, 20, 999),
}
THEMES = ('light', 'dark')
DEFAULT_THEME = 'dark'
GENERIC_FAMILIES = {'system-ui', '-apple-system', 'sans-serif', 'serif', 'monospace'}


def _toPx(value) -> int:
    return int(str(value).replace('px', '').strip())


class Tokens:
    """Truy cập token theo một chủ đề cụ thể (light | dark)."""

    def __init__(self, data: dict, theme: str = DEFAULT_THEME):
        self._data = data
        self.theme = theme if theme in data['color'] else DEFAULT_THEME

    def color(self, name: str) -> str:
        return self._data['color'][self.theme][name]

    def size(self, name: str) -> int:
        """Cỡ chữ theo px, ví dụ size('body-desktop') -> 14."""
        return _toPx(self._data['typography']['font-size'][name])

    def space(self, step) -> int:
        """Khoảng cách theo bậc 4px, ví dụ space(4) -> 16."""
        return _toPx(self._data['spacing'][str(step)])

    def radius(self, name: str) -> int:
        return _toPx(self._data['radius'][name])

    def weight(self, name: str) -> int:
        return int(self._data['typography']['weight'][name])

    def motionMs(self, name: str) -> int:
        return int(str(self._data['motion'][name]).replace('ms', ''))

    def pill(self, height: int) -> int:
        """Bo góc nút cho control cao `height` px: Qt vẽ sai khi bán kính vượt nửa chiều cao, nên kẹp lại."""
        return min(self.radius('control'), height // 2)

    def displayFamilies(self) -> list[str]:
        """Font tiêu đề của sản phẩm (fontDisplay) rồi tới chuỗi font thân bài làm dự phòng."""
        return [self._data['typography']['font-display'], *self.families()]

    def families(self, mono: bool = False) -> list[str]:
        """Chuỗi font dự phòng của token, đã bỏ tên generic của CSS."""
        spec = self._data['typography']['font-mono' if mono else 'font-family']
        names = [part.strip().strip("'\"") for part in spec.split(',')]
        return [n for n in names if n.lower() not in GENERIC_FAMILIES]


@cache
def _loadData() -> dict:
    with open(resourcePath(TOKENS_FILE), encoding='utf-8') as f:
        data = json.load(f)
    with open(resourcePath(PRODUCT_FILE), encoding='utf-8') as f:
        product = json.load(f)
    if product.get('id') != PRODUCT_ID:
        raise ValueError(f'{PRODUCT_FILE}: id {product.get("id")!r} khác {PRODUCT_ID!r}')
    colors = {}
    for theme in THEMES:
        base = data['color'][theme]
        override = product['colors'][theme]
        unknown = set(override) - set(base)
        if unknown:   # sai tên vai trò thì ghi đè im lặng không có tác dụng: dừng sớm
            raise ValueError(f'{PRODUCT_FILE}: vai trò không có trong bảng chuẩn ({theme}): {sorted(unknown)}')
        colors[theme] = {**base, **override}
    data['color'] = colors
    sm, md, lg, control = SHAPES[product['shape']]
    data['radius'] = {**data['radius'], 'sm': f'{sm}px', 'md': f'{md}px', 'lg': f'{lg}px', 'control': f'{control}px'}
    data['typography'] = {**data['typography'], 'font-display': product['fontDisplay']}
    data['product'] = {k: product[k] for k in ('id', 'name', 'layout', 'shape', 'motif')}
    return data


@cache
def loadTokens(theme: str = DEFAULT_THEME) -> Tokens:
    return Tokens(_loadData(), theme)
