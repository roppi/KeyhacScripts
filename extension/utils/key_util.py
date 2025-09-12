# -*- coding: utf-8 -*-
""" Keyhac 設定ファイル：キー関連共通処理
Keyhac から呼び出されるキー関連の共通処理を定義する。
"""

import time
import re

from keyhac import *

# 修飾自動解除対象のキー（大文字で指定）
key_util_release_keys = []


def set_user_modifier_keys(keymap, release_time = 0, release_keys = []):
    """ユーザモディファイアキーの設定を行う
    以下のキーのキーコード変更とユーザモディファイアキー登録を行う
    英数キー　：U0（キーコード：124（F13））
    無変換キー：U1（キーコード：125（F14））
    変換キー　：U2（キーコード：126（F15））

    Args:
        keymap: config.py から引き渡される Keymap オブジェクト
        release_time: 修飾キー自動解除時間
        release_keys: 自動解除が必要な修飾キーの配列

    Notes:
        英数キーは KeyUp を取得できないため、そのままでは修飾を解除できない。
        そのため、押下された場合に規定時間で修飾を自動解除するホットキー設定を追加する。
    """

    # グローバルマップを取得
    keymap_global = keymap.defineWindowKeymap()
    # 修飾自動解除キー配列を取得
    global key_util_release_keys

    def reset_modifier_wait():
        """修飾キー自動解除処理
        別スレッドで規定時間待機後、修飾キーをすべて解除する
        """
        def reset_modifier_async(self):
            time.sleep(release_time)
            keymap.modifier = 0

        JobQueue.defaultQueue().enqueue(JobItem(reset_modifier_async, None))

    # 修飾解除が必要なキーをグローバル変数に登録
    if release_keys: key_util_release_keys = key_util_release_keys + release_keys

    # --------------------------------------------------
    # 英数キー
    # --------------------------------------------------
    # 英数キー(240) を [F13](124) に変更
    keymap.replaceKey('240', 124)
    # [F13](124) を ユーザモディファイアキー0に設定
    keymap.defineModifier(124, "U0")

    # 自動解除対象の場合、単独の押下で規定時間後に修飾を解除
    if "U0" in key_util_release_keys:
        keymap_global["124"] = reset_modifier_wait

    # --------------------------------------------------
    # 無変換キー
    # --------------------------------------------------
    # 無変換キー(29) を [F14](125) に変更
    keymap.replaceKey('29', 125)
    # [F14](125) を ユーザモディファイアキー1に設定
    keymap.defineModifier(125, "U1")

    # --------------------------------------------------
    # 変換キー
    # --------------------------------------------------
    # 変換キー(28) を [F15](126) に変更
    keymap.replaceKey('28', 126)
    # [F15](126) を ユーザモディファイアキー2に設定
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
    # 修飾自動解除キー配列を取得
    global key_util_release_keys

    def reset_modifier_key(func):
        """修飾キー自動解除ラッパー処理
        修飾キーを解除し、その後パラメータの内容を返却する。
        """
        def reset_modifier_wrapper():
            keymap.modifier = 0
            return func()

        return lambda: reset_modifier_wrapper()

    # 指定された条件でキーマップを取得
    keymap_app = keymap.defineWindowKeymap(*args, **kwargs)

    # ホットキーの内容をキーマップに設定
    for key, value in hotkeys.items():
        is_need_reset = sum(reset_key in str.upper(key) for reset_key in key_util_release_keys)
        keymap_app[key] = reset_modifier_key(value) if is_need_reset and callable(value) else value


def get_keymap_app(keymap, *args, **kwargs):
    """ 指定されたキーマップを取得する
    defineWindowKeymap の単純なラッパーメソッド

    Args:
        keymap: config.py から引き渡される Keymap オブジェクト
        *args: keymap.defineWindowKeymap 向け引数
        **kwargs: keymap.defineWindowKeymap 向け引数

    Returns: 指定されたキーマップ
    """
    return keymap.defineWindowKeymap(*args, **kwargs)


def sleep(secondes = 0.1):
    time.sleep(secondes)


def get_clipboard():
    return getClipboardText()


def set_clipboard(text):
    setClipboardText(text)


def send_keys(keymap, *keys):
    keymap.beginInput()
    for key in keys:
        keymap.setInput_FromString(str(key))
    keymap.endInput()


def reg_replace_line(keymap, match, replace):
    # クリップボードの内容を退避
    swap_cb = get_clipboard()

    # 行コピー（切り取りだとUndo履歴が残るため）
    send_keys(keymap, "Home", "S-End", "C-Insert")
    sleep(0.05)

    # 正規表現置換した結果を貼り付け
    result = re.sub(match, replace, get_clipboard())
    set_clipboard(result)
    sleep(0.05)

    # 正規表現置換した結果を貼り付け
    result = re.sub(match, replace, get_clipboard())
    set_clipboard(result)
    sleep(0.05)
    send_keys(keymap, "C-V")

    # クリップボードの内容を戻す
    sleep(0.05)
    set_clipboard(swap_cb)