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
        "U1-T": keymap.InputTextCommand(datetime.datetime.now().strftime("%Y/%m/%d %H:%M:%S"))  # [無変換]+[T]：現在日時出力
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

    # キーマップを取得
    keymap_app = get_keymap_app(keymap, **app_param)

    # 動的処理をマッピング
    keymap_app["U1-0"] = md_to_text
    keymap_app["U1-1"] = md_to_header1
    keymap_app["U1-2"] = md_to_header2
    keymap_app["U1-3"] = md_to_header3
    keymap_app["U1-4"] = md_to_header4
    keymap_app["U1-5"] = md_to_header5