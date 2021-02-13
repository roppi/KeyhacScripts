# -*- coding: utf-8 -*-
""" Keyhac 設定ファイル：共通ホットキー設定

Keyhac から呼び出される共通ホットキー設定。

"""

import extension.utils.ime_util as ime_util
import extension.utils.key_util as key_util
from extension.utils.window_util import activate_window


def configure(keymap):
    # ユーザモディファイアキーを設定
    # 第2引数（release_time）はタイピング速度に合わせて調整してください。
    # [英数]キーを使った組合せが認識されない場合　→　長く設定
    # [英数]キーを使った組合せの誤認識が多い場合　→　短く設定
    key_util.set_user_modifier_keys(keymap, 0.3)

    # ホットキーを定義
    hotkeys = {"U0-R": keymap.command_ReloadConfig,                         # [英数]+[r]：設定リロード
               "U0-F": keymap.command_ClipboardList,                        # [英数]+[f]：クリップボードヒストリの表示

               "U0-A": lambda: ime_util.set_input_method(keymap),           # [英数]+[a]：IMEの有効/無効切替
               # "125": lambda: ime_util.set_input_method(keymap, False),     # [無変換]  ：IMEの無効化
               # "126": lambda: ime_util.set_input_method(keymap, True),      # [変換]    ：IMEの有効化

               # よくあるCtrlキー系の処理を英数キーでも可能に
               "U0-X": "C-X",                                               # [英数]+[x]：切り取り
               "U0-C": "C-C",                                               # [英数]+[c]：コピー
               "U0-V": "C-V",                                               # [英数]+[v]：貼り付け
               "U0-N": "C-N",                                               # [英数]+[n]：新規
               "U0-O": "C-O",                                               # [英数]+[o]：開く
               "U0-S": "C-S",                                               # [英数]+[s]：保存

               # コトリエ風、入力中文字種別変更
               "U0-J": "F6",                                                # [英数]+[j]：「ひらがな」に変換する
               "U0-K": "F7",                                                # [英数]+[k]：「カタカナ」に変換する
               "U0-L": "F8",                                                # [英数]+[l]：「半角カタカナ」に変換する
               "U0-Plus": "F9",                                             # [英数]+[;]：「全角英数」に変換する
               "U0-Colon": "F10",                                           # [英数]+[:]：「半角英数」に変換する

               # [英数]+[E]：内骨格を起動
               "U0-E": lambda: activate_window(keymap, "cfiler.exe", directory="../cfiler", force=True),
               }

    # キーマップにホットキーを反映
    key_util.set_keymap_app(keymap, hotkeys)
