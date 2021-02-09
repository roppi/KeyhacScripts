# -*- coding: utf-8 -*-
""" Keyhac 設定ファイル：共通処理

Keyhac から呼び出される共通処理を定義する。

"""

import pathlib
import importlib
import re


def load_configs(module_path_str):
    """パッケージ内モジュール読み込み処理

    パッケージ内のモジュール読込みを行う
    ※サブパッケージ内のモジュールは対象外

    またモジュールのファイル名の先頭が「_」など英字以外のファイルは読込み対象外とする

    Args:
        module_path_str: パッケージのディレクトリパス（文字列）

    Returns:
        パッケージ内モジュールリスト

    """

    # 指定ディレクトリからモジュール名を取得
    module_path = pathlib.Path(module_path_str)
    module_name = module_path.parents[0].name

    modules = []
    for filepath in module_path.parent.iterdir():
        # ファイル名がアルファベット始まりでない場合はスキップ
        if not re.match(r'[a-zA-Z][\w.]+\.py$', filepath.name):
            continue

        # モジュール名を取得しリストに追加
        sub_module_name = filepath.stem
        module = importlib.import_module(f'{module_name}.{sub_module_name}')

        modules.append(module)

    # モジュール名リストを返却
    return modules
