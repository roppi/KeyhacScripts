# -*- coding: utf-8 -*-
""" Keyhac 設定ファイル：固定文字列リスト設定の雛形

Keyhac から呼び出される固定文字列リスト設定。

"""

from keyhac import *


def configure(keymap):
    """Keyhac 設定処理：固定文字列リスト設定

    Args:
        keymap: config.py から引き渡される Keymap オブジェクト

    """

    # Fixed phrases
    fixed_items = [
        ("name@server.net", "name@server.net"),
        ("Address", "San Francisco, CA 94128"),
        ("Phone number", "03-4567-8901"),
    ]

    # Clipboard history list extensions
    keymap.cblisters += [
        ("Fixed phrase", cblister_FixedPhrase(fixed_items)), ]
