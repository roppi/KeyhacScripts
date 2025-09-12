# -*- coding: utf-8 -*-
""" Keyhac 設定ファイル：IME 関連共通処理

Keyhac から呼び出される IME 関連の共通処理を定義する。

"""


def set_input_method(keymap, ime_status=None):
    """アクティブウインドウの IME 有効/無効を切替処理

    Args:
        keymap: config.py から引き渡される Keymap オブジェクト
        ime_status: 設定するIMEモード（未設定時は有効/無効を切替）

    """

    # IME の状態を格納する
    if ime_status != None:
        ime_status = ime_status
    else: 
        not keymap.getWindow().getImeStatus()
    
    # IMEのON/OFFをセット
    keymap.wnd.setImeStatus(ime_status)

    # IME の状態をバルーンヘルプで表示する
    keymap.popBalloon("ime_status", "[あ] IMEオン" if ime_status else "[A] IMEオフ", 500)
