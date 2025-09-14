# -*- coding: utf-8 -*-
""" Keyhac 設定ファイル：エクセル向けホットキー設定

Keyhac から呼び出されるエクセル向けホットキー設定。

"""

from extension.utils.key_util import set_keymap_app


def configure(keymap):
    """Keyhac 設定処理：エクセル向けホットキー設定

    Args:
        keymap: config.py から引き渡される Keymap オブジェクト

    """

    # キーマップ取得条件を設定
    app_param = {"exe_name": "EXCEL.exe"}
    # ホットキーを定義
    hotkeys = {
        "F1": lambda: None,              # ヘルプ無効
        "U1-N": "C-PageUp",              # [無変換]+[N]：シート移動（前）
        "U1-M": "C-PageDown",            # [無変換]+[M]：シート移動（次）
        "U1-188": "C-S-Tab",             # [無変換]+[,]：ブック移動（前）
        "U1-190": "C-Tab",               # [無変換]+[.]：ブック移動（次）

        "U1-E": ["F2", "Up"],            # [無変換]+[E]：セル編集

        "U1-U": "C-189",                 # [無変換]+[U]：行・列の削除
        "U1-I": "C-S-Plus",              # [無変換]+[I]：行・列の追加
        "U1-O": "S-Space",               # [無変換]+[O]：行の選択
        "U1-P": "C-Space",               # [無変換]+[P]：列の選択

        "U1-Left": ["A-H", "A", "L"],    # [無変換]+[←]：セルの左寄せ
        "U1-Up": ["A-H", "A", "C"],      # [無変換]+[↑]：セルの中央寄せ
        "U1-Right": ["A-H", "A", "R"],   # [無変換]+[→]：セルの右寄せ
        "U1-Down": ["A-H", "M", "C"],    # [無変換]+[↓]：セルの結合/解除

        "U1-1": ["A-H", "F", "D", "O"],  # [無変換]+[1]：オブジェクトの選択
        "U1-2": ["A-F", "E", "A"],       # [無変換]+[2]：PDFエクスポート
        
        "U1-0": ["145"],                 # [無変換]+[0]：スクロールロック
    }

    # キーマップにホットキーを反映
    set_keymap_app(keymap, hotkeys, **app_param)
