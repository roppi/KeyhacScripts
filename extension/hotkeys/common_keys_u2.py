# -*- coding: utf-8 -*-
""" Keyhac 設定ファイル：共通ホットキー設定（変換キー）

Keyhac から呼び出される共通ホットキー設定（変換キー）

"""

from extension.utils.key_util import set_keymap_app


def configure(keymap):
    # ホットキーを定義
    hotkeys = {
        # テンキー
        "U2-Space"        : "0",            # [変換]+[スペース]：0
        "U2-X"            : "1",            # [変換]+[x]：1
        "U2-C"            : "2",            # [変換]+[c]：2
        "U2-V"            : "3",            # [変換]+[v]：3
        "U2-S"            : "4",            # [変換]+[s]：4
        "U2-D"            : "5",            # [変換]+[d]：5
        "U2-F"            : "6",            # [変換]+[f]：6
        "U2-W"            : "7",            # [変換]+[w]：7
        "U2-E"            : "8",            # [変換]+[e]：8
        "U2-R"            : "9",            # [変換]+[r]：9

        "U2-G"            : "Add",          # [変換]+[g]：+
        "U2-T"            : "Subtract",     # [変換]+[t]：-
        "U2-A"            : "Multiply",     # [変換]+[a]：x
        "U2-Q"            : "Divide",       # [変換]+[q]：/
        "U2-B"            : "S-Minus",      # [変換]+[b]：=
        "U2-Z"            : "Decimal",      # [変換]+[z]：.


        # 移動系（単一キー）
        "U2-H"            : "Left",         # [変換]+[h]：左矢印キー
        "U2-J"            : "Down",         # [変換]+[j]：下矢印キー
        "U2-K"            : "Up",           # [変換]+[k]：上矢印キー
        "U2-L"            : "Right",        # [変換]+[l]：右矢印キー

        "U2-Semicolon"    : "Home",         # [変換]+[;]：Home
        "U2-Colon"        : "End",          # [変換]+[:]：End
        "U2-CloseBracket" : lambda: None,   # [変換]+[]]：無効（誤操作防止）
        "U2-Slash"        : "PageUp",       # [変換]+[/]：PageUp
        "U2-BackSlash"    : "PageDown",     # [変換]+[\]：PageDown

        # 移動系（修飾キーコンボ）
        "U2-S-H"          : "S-Left",       # [Shift]+[変換]+[h]：左矢印キー（選択）
        "U2-S-J"          : "S-Down",       # [Shift]+[変換]+[j]：下矢印キー（選択）
        "U2-S-K"          : "S-Up",         # [Shift]+[変換]+[k]：上矢印キー（選択）
        "U2-S-L"          : "S-Right",      # [Shift]+[変換]+[l]：右矢印キー（選択）
        "U2-C-H"          : "C-Left",       # [Ctrl]+[変換]+[h]：左矢印キー（語移動）
        "U2-C-J"          : "C-Down",       # [Ctrl]+[変換]+[j]：下矢印キー（語移動）
        "U2-C-K"          : "C-Up",         # [Ctrl]+[変換]+[k]：上矢印キー（語移動）
        "U2-C-L"          : "C-Right",      # [Ctrl]+[変換]+[l]：右矢印キー（語移動）
        "U2-C-S-H"        : "C-S-Left",     # [Ctrl]+[Shift]+[変換]+[h]：左矢印キー（選択＋語移動）
        "U2-C-S-J"        : "C-S-Down",     # [Ctrl]+[Shift]+[変換]+[j]：下矢印キー（選択＋語移動）
        "U2-C-S-K"        : "C-S-Up",       # [Ctrl]+[Shift]+[変換]+[k]：上矢印キー（選択＋語移動）
        "U2-C-S-L"        : "C-S-Right",    # [Ctrl]+[Shift]+[変換]+[l]：右矢印キー（選択＋語移動）

        "U2-A-H"          : "A-Left",       # [Alt]+[変換]+[h]：左矢印キー（SakuraEditor矩形選択）
        "U2-A-J"          : "A-Down",       # [Alt]+[変換]+[j]：下矢印キー（SakuraEditor矩形選択）
        "U2-A-K"          : "A-Up",         # [Alt]+[変換]+[k]：上矢印キー（SakuraEditor矩形選択）
        "U2-A-L"          : "A-Right",      # [Alt]+[変換]+[l]：右矢印キー（SakuraEditor矩形選択）
        "U2-C-A-S-H"      : "C-A-S-Left",   # [Ctrl]+[Alt]+[Shift]+[変換]+[h]：左矢印キー（VSCode矩形選択）
        "U2-C-A-S-J"      : "C-A-S-Down",   # [Ctrl]+[Alt]+[Shift]+[変換]+[j]：下矢印キー（VSCode矩形選択）
        "U2-C-A-S-K"      : "C-A-S-Up",     # [Ctrl]+[Alt]+[Shift]+[変換]+[k]：上矢印キー（VSCode矩形選択）
        "U2-C-A-S-L"      : "C-A-S-Right",  # [Ctrl]+[Alt]+[Shift]+[変換]+[l]：右矢印キー（VSCode矩形選択）

        "U2-S-Semicolon"  : "S-Home",       # [Shift]+[変換]+[;]：Home    （選択）
        "U2-S-Colon"      : "S-End",        # [Shift]+[変換]+[:]：End     （選択）
        "U2-S-Slash"      : "S-PageUp",     # [Shift]+[変換]+[/]：PageUp  （選択）
        "U2-S-BackSlash"  : "S-PageDown",   # [Shift]+[変換]+[\]：PageDown（選択）
        "U2-C-Semicolon"  : "C-Home",       # [Ctrl]+[変換]+[;]：Home     （先頭へ移動）
        "U2-C-Colon"      : "C-End",        # [Ctrl]+[変換]+[:]：End      （末尾へ移動）
        "U2-C-Slash"      : "C-PageUp",     # [Ctrl]+[変換]+[/]：PageUp   （前のシートへ移動）
        "U2-C-BackSlash"  : "C-PageDown",   # [Ctrl]+[変換]+[\]：PageDown （次のシートへ移動）
        "U2-C-S-Semicolon": "C-S-Home",     # [Ctrl]+[Shift]+[変換]+[;]：Home（選択＋先頭へ移動）
        "U2-C-S-Colon"    : "C-S-End",      # [Ctrl]+[Shift]+[変換]+[:]：End （選択＋末尾へ移動）
    }

    # キーマップにホットキーを反映
    set_keymap_app(keymap, hotkeys)
