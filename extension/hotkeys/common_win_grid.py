# -*- coding: utf-8 -*-
""" Keyhac 設定ファイル：共通ホットキー設定（ウインドウサイズ変更）

Keyhac から呼び出される共通ホットキー設定。
グリッド式の指定でウインドウ位置とサイズを変更する。

"""

from extension.utils.key_util import set_keymap_app
from extension.utils.window_util import WindowGrid


def configure(keymap):
    """Keyhac 設定処理：共通ホットキー設定（ウインドウサイズ変更）

    Args:
        keymap: config.py から引き渡される Keymap オブジェクト

    """

    # グリッド式ウインドウサイズ変更クラスを初期化
    win_grid = WindowGrid(keymap, 8, 8)
    # 現在移動対象のディスプレイNo
    mon_idx = 0

    def prev_mon():
        """前ディスプレイNo取得処理

        現在移動対象の前のディスプレイNoを取得する

        Returns:
            ディスプレイNo

        """

        nonlocal mon_idx
        win_grid.update_monitor_info()
        mon_idx = win_grid.get_next_monitor_idx(mon_idx, -1)

    def next_mon():
        """次ディスプレイNo取得処理

        現在移動対象の次のディスプレイNoを取得する

        Returns:
            ディスプレイNo

        """

        nonlocal mon_idx
        win_grid.update_monitor_info()
        mon_idx = win_grid.get_next_monitor_idx(mon_idx, 1)

    # ホットキーを定義
    hotkeys = {
               "U0-188": prev_mon,  # [英数]+[,]：ウインドウ移動ディスプレイ変更（前）
               "U0-190": next_mon,  # [英数]+[.]：ウインドウ移動ディスプレイ変更（次）

               # ウインドウ移動（メイン系）
               "U0-1": lambda: win_grid.move_window(0, 0, 5, 8, mon_idx),
               "U0-2": lambda: win_grid.move_window(0, 0, 5, 5, mon_idx),
               "U0-3": lambda: win_grid.move_window(0, 5, 5, 3, mon_idx),
               "U0-4": lambda: win_grid.move_window(0, 0, 5, 4, mon_idx),
               "U0-5": lambda: win_grid.move_window(0, 4, 5, 4, mon_idx),

               # ウインドウ移動（サブ系）
               "U0-6": lambda: win_grid.move_window(5, 0, 3, 8, mon_idx),
               "U0-7": lambda: win_grid.move_window(5, 0, 3, 5, mon_idx),
               "U0-8": lambda: win_grid.move_window(5, 5, 3, 3, mon_idx),
               "U0-9": lambda: win_grid.move_window(5, 0, 3, 4, mon_idx),
               "U0-0": lambda: win_grid.move_window(5, 4, 3, 4, mon_idx),

               }

    # キーマップにホットキーを反映
    set_keymap_app(keymap, hotkeys)
