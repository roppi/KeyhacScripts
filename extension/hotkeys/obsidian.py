# -*- coding: utf-8 -*-
""" Keyhac 設定ファイル：Obsidian向けホットキー設定の雛形

Keyhac から呼び出されるObsidian向けホットキー設定の雛形。

"""
import datetime

from extension.utils.key_util import *


def configure(keymap):
    """Keyhac 設定処理：Obsidian向けホットキー設定

    Args:
        keymap: config.py から引き渡される Keymap オブジェクト

    """

    # キーマップ取得条件を設定
    # 対象となるアプリ（ウインドウ）の情報を設定する。
    app_param = {"exe_name": "Obsidian.exe"}
    # アプリに依らない共通のホットキーとする場合は、以下のコメントを解除
    # app_param = None

    # ホットキーを定義
    hotkeys = {
        "U1-0": lambda: md_to_text(),        # [無変換]+[0]：ヘッダを通常テキストに変更
        "U1-1": lambda: md_to_header1(),     # [無変換]+[1]：ヘッダをH1に変更
        "U1-2": lambda: md_to_header2(),     # [無変換]+[2]：ヘッダをH2に変更
        "U1-3": lambda: md_to_header3(),     # [無変換]+[3]：ヘッダをH3に変更
        "U1-4": lambda: md_to_header4(),     # [無変換]+[4]：ヘッダをH4に変更
        "U1-5": lambda: md_to_header5(),     # [無変換]+[5]：ヘッダをH5に変更
    }

    # キーマップにホットキーを反映
    set_keymap_app(keymap, hotkeys, **app_param)

    # ====================
    # 動的処理定義
    # ====================
    # ヘッダ置換処理
    def md_to_text():
        reg_replace_line(keymap, "^(#+ )?", "")
    def md_to_header1():
        reg_replace_line(keymap, "^(#+ )?", "# ")
    def md_to_header2():
        reg_replace_line(keymap, "^(#+ )?", "## ")
    def md_to_header3():
        reg_replace_line(keymap, "^(#+ )?", "### ")
    def md_to_header4():
        reg_replace_line(keymap, "^(#+ )?", "#### ")
    def md_to_header5():
        reg_replace_line(keymap, "^(#+ )?", "##### ")