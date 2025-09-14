# -*- coding: utf-8 -*-
""" Keyhac 設定ファイル：固定文字列リスト設定（Windows設定）

Keyhac から呼び出される固定文字列リスト設定。

"""

from keyhac import *
from extension.utils.window_util import open_system_folder


def configure(keymap):
    """Keyhac 設定処理：固定文字列リスト設定

    Args:
        keymap: config.py から引き渡される Keymap オブジェクト

    """

    # Fixed phrases
    fixed_items = [
        # ("デスクトップ", lambda:open_system_folder(keymap, "%USERPROFILE%\Desktop")),
        # ("マイドキュメント", lambda:open_system_folder(keymap, "%USERPROFILE%\Documents")),
        # ("ダウンロード", lambda:open_system_folder(keymap, "%USERPROFILE%\Downloads")),
        ("ゴミ箱", lambda:open_system_folder(keymap, "shell:RecycleBinFolder")),
        # ("------------------------------", None),
        # ("UserHome", lambda:open_system_folder(keymap, "%USERPROFILE%")),
        # ("AppData", lambda:open_system_folder(keymap, "%APPDATA%")),
        # ("LocalAppData", lambda:open_system_folder(keymap, "%LOCALAPPDATA%")),
        # ("Temp", lambda:open_system_folder(keymap, "%TEMP%")),
        # ("------------------------------", None),
        ("コントロールパネル", lambda:open_system_folder(keymap, "control.exe")),
        ("ネットワーク接続", lambda:open_system_folder(keymap, "ncpa.cpl")),
        ("プログラムと機能", lambda:open_system_folder(keymap, "appwiz.cpl")),
        ("コンピュータの管理", lambda:open_system_folder(keymap, "compmgmt.msc")),
        ("ローカルセキュリティポリシー", lambda:open_system_folder(keymap, "secpol.msc")),
        ("ローカルグループポリシー", lambda:open_system_folder(keymap, "gpedit.msc")),
    ]

    # Clipboard history list extensions
    keymap.cblisters += [
        ("システムフォルダ", cblister_FixedPhrase(fixed_items)), ]