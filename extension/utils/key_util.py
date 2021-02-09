# -*- coding: utf-8 -*-
""" Keyhac 設定ファイル：キー関連共通処理

Keyhac から呼び出されるキー関連の共通処理を定義する。

"""

import time

from keyhac import *


def set_user_modifier_keys(keymap):
    """ユーザモディファイアキーの設定を行う

    以下のキーのキーコード変更とユーザモディファイアキー登録を行う
    英数キー　：U0（キーコード：124（F13））
    無変換キー：U1（キーコード：125（F14））
    変換キー　：U2（キーコード：126（F15））

    Args:
        keymap: config.py から引き渡される Keymap オブジェクト

    Notes:
        英数キーは KeyUp を取得できないため、そのままでは修飾を解除できない。
        そのため、押下された場合に規定時間で修飾を自動解除するホットキー設定を追加する。

    """

    # グローバルマップを取得
    keymap_global = keymap.defineWindowKeymap()

    # 修飾解除時間
    release_time = 0.3

    def reset_modifier_wait():
        """修飾キー自動解除処理

        別スレッドで規定時間待機後、修飾キーをすべて解除する

        """
        def reset_modifier_async(self):
            time.sleep(release_time)
            keymap.modifier = 0

        JobQueue.defaultQueue().enqueue(JobItem(reset_modifier_async, None))

    # --------------------------------------------------
    # 英数キー
    # --------------------------------------------------
    # 英数キー(240) を [F13](124) に変更
    keymap.replaceKey('240', 124)
    # 英数キー(240) を ユーザー修飾キー0に設定
    keymap.defineModifier(124, "U0")

    # 単独の場合、規定時間後に修飾を解除
    keymap_global["124"] = reset_modifier_wait

    # --------------------------------------------------
    # 無変換キー
    # --------------------------------------------------
    # 無変換キー(29) を [F14](125) に変更
    keymap.replaceKey('29', 125)
    # 無変換キー(240) を ユーザー修飾キー1に設定
    keymap.defineModifier(125, "U1")

    # --------------------------------------------------
    # 変換キー
    # --------------------------------------------------
    # 変換キー(28) を [F15](126) に変更
    keymap.replaceKey('28', 126)
    # 変換キー(240) を ユーザー修飾キー2に設定
    keymap.defineModifier(126, "U2")


def set_keymap_app(keymap, hotkeys, *args, **kwargs):
    """指定されたキーマップに対してホットキーを設定する

    指定されたキーマップに対してホットキーを設定する。
    規定のキーが押された場合は、修飾を自動解除する。

    Args:
        keymap: config.py から引き渡される Keymap オブジェクト
        hotkeys: ホットキーのディクショナリー
        *args: keymap.defineWindowKeymap 向け引数
        **kwargs: keymap.defineWindowKeymap 向け引数

    """

    # 修飾解除対象のキー（大文字で指定）
    reset_key = "U0"

    def reset_modifier_key(param):
        """修飾キー自動解除ラッパー処理

        修飾キーを解除し、その後パラメータの内容を返却する。

        """
        keymap.modifier = 0
        return param

    # 指定された条件でキーマップを取得
    keymap_app = keymap.defineWindowKeymap(*args, **kwargs)

    # ホットキーの内容をキーマップに設定
    for key, value in hotkeys.items():
        keymap_app[key] = reset_modifier_key(value) if reset_key in str.upper(key) else value
