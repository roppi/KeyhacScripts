# -*- coding: utf-8 -*-
""" Keyhac 設定ファイル：メイン

Keyhac から呼び出されるメインの設定ファイル。

"""

import extension.hotkeys as hotkeys
import extension.lists as lists


def configure(keymap):
    """Keyhac 設定処理

    Args:
        keymap: keymapから引き渡されるメインのKeymapオブジェクト

    """

    # Hotkey 設定読込み
    hotkeys.configure(keymap)
    # Lists 設定読込み
    lists.configure(keymap)
