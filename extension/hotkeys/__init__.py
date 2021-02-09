# -*- coding: utf-8 -*-
""" Keyhac 設定ファイル：hotkeysパッケージメイン

Keyhac から呼び出されるパッケージ初期化処理。
パッケージ内の各モジュールに定義された configure 関数を呼出す。

"""

from extension.common import load_configs


def configure(keymap):
    """Keyhac 設定処理

    Args:
        keymap: config.py から引き渡される Keymap オブジェクト

    """

    # パッケージ内モジュールリストを取得し、configure 関数を呼出す
    for sub_module in load_configs(__file__):
        print(sub_module)
        sub_module.configure(keymap)
