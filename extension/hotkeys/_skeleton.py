# -*- coding: utf-8 -*-
""" Keyhac 設定ファイル：アプリ向けホットキー設定の雛形

Keyhac から呼び出されるアプリ向けホットキー設定の雛形。

"""

from extension.utils.key_util import set_keymap_app


def configure(keymap):
    """Keyhac 設定処理：アプリ向けホットキー設定

    Args:
        keymap: config.py から引き渡される Keymap オブジェクト

    """

    # キーマップ取得条件を設定
    # 対象となるアプリ（ウインドウ）の情報を設定する。
    app_param = {"exe_name": "対象の実行ファイル名.exe"}
    # アプリに依らない共通のホットキーとする場合は、以下のコメントを解除
    # app_param = None

    # ホットキーを定義
    # 「実際に押すキー：コンピュータに送られるキー」として設定する。
    hotkeys = {"U1-C": lambda: None,            # キーを無効にするときは None を設定
               "U1-E": "F2",                    # 単純なキーの置換
               "U1-Right": ["A-H", "R"],        # 複数のキーを置換する場合はリストにする

               }

    # キーマップにホットキーを反映
    set_keymap_app(keymap, hotkeys, **app_param)
