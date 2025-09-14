# -*- coding: utf-8 -*-
""" Keyhac 設定ファイル：共通ホットキー設定（FastStone Capture によるスクショ関連）

Keyhac から呼び出される共通ホットキー設定。

"""

from extension.utils.key_util import set_keymap_app


def configure(keymap):
    # ホットキーを定義
    hotkeys = {
        # [英数]+[P]：PrintScreenを基本として各種モディファイアを定義
        # [英数]+[P]：全画面キャプチャ
        "U0-P": "PrintScreen",
        # [Alt]+[英数]+[P]：アクティブウインドウキャプチャ
        "U0-A-P": "A-PrintScreen",
        # [Shift]+[英数]+[P]：オブジェクト範囲キャプチャ
        "U0-S-P": "S-PrintScreen",
        # [Ctrl]+[英数]+[P]：領域キャプチャ
        "U0-C-P": "C-PrintScreen",
        # [Ctrl]+[Shift]+[英数]+[P]：スクロールキャプチャ
        "U0-C-S-P": "C-A-PrintScreen",
        # [Ctrl]+[Alt]+[英数]+[P]：前回領域キャプチャ
        "U0-C-A-P": "C-S-PrintScreen",
    }

    # キーマップにホットキーを反映
    set_keymap_app(keymap, hotkeys)
