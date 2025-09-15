# -*- coding: utf-8 -*-
""" Keyhac 設定ファイル：共通ホットキー設定

Keyhac から呼び出される共通ホットキー設定。

"""

import extension.utils.ime_util as ime_util
import extension.utils.key_util as key_util
from extension.utils.window_util import activate_window


def configure(keymap):
    # ユーザモディファイアキーを設定
    # 第2引数: 自動解除されるまでの時間。
    # 　　　　　誤操作が多ければ短く、反対に認識されないときは長めに設定して下さい。
    # 第3引数: 自動解除対象の修飾キー。[英数]キーの場合は"U0"を設定。
    key_util.set_user_modifier_keys(keymap, 0.3, ["U0"])
    # キーコード置換済みの場合は、ともに省略可能です。（こちらの方が安定します）
    # key_util.set_user_modifier_keys(keymap)
    
    # ホットキーを定義
    hotkeys = {
        "U0-F": keymap.command_ClipboardList,                        # [英数]+[f]：クリップボードヒストリの表示

        "O-125": lambda: ime_util.set_input_method(keymap, False),   # [無変換]  ：IMEの無効化
        "O-126": lambda: ime_util.set_input_method(keymap, True),    # [変換]    ：IMEの有効化

        # よく使う処理を押しやすい位置に
        "U0-A": "C-X",                                               # [英数]+[a]：切り取り
        "U0-S": "C-C",                                               # [英数]+[s]：コピー
        "U0-D": "C-V",                                               # [英数]+[d]：貼り付け
        "U0-S-D": "C-S-V",                                           # [英数]+[Shift]+[d]：貼り付け（書式なし）
        
        "U0-Q": "A-F4",                                              # [英数]+[q]：アプリを終了
        "U0-W": "C-F4",                                              # [英数]+[w]：タブを閉じる
        
        "U0-I": "Insert",                                            # [英数]+[i]：挿入
        "U0-BackSlash": "S-F10",                                     # [英数]+[\]：コンテキストメニュー
        
        "U0-125": "Back",                                            # [英数]+[無変換] ：バックスペース
        "U0-126": "Delete",                                          # [英数]+[変換]   ：デリート
        "U0-Space": "W-Slash",                                       # [英数]+[スペース]：再変換

        # コトエリ風、入力中文字種別変更
        "U0-J": "F6",                                                # [英数]+[j]：「ひらがな」に変換する
        "U0-K": "F7",                                                # [英数]+[k]：「カタカナ」に変換する
        "U0-L": "F8",                                                # [英数]+[l]：「半角カタカナ」に変換する
        "U0-Plus": "F9",                                             # [英数]+[;]：「全角英数」に変換する
        "U0-Colon": "F10",                                           # [英数]+[:]：「半角英数」に変換する

        # [英数]+[r]：設定リロード
        "U0-R": lambda: activate_window(keymap, "restart_keyhac.bat", directory="", force=True),
    }

    # キーマップにホットキーを反映
    key_util.set_keymap_app(keymap, hotkeys)
