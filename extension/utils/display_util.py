# -*- coding: utf-8 -*-
""" Keyhac 設定ファイル：ディスプレイ関連共通処理

Keyhac から呼び出されるディスプレイ関連の共通処理を定義する。

"""

import pyauto


class WindowGrid:
    """グリッド式ウインドウサイズ変更クラス

    画面を縦・横それぞれ指定の数に仮想的に分割し、
    ウインドウの位置・サイズをマス目（グリッド）の番号で指定可能とする。

    """

    def __init__(self, keymap, rows, cols):
        """WindowGrid 初期化処理

        Keymap と画面の分割数を指定し、 WindwGrid を初期化する。

        Args:
            keymap: config.py から引き渡される Keymap オブジェクト
            rows: 画面の縦の分割数
            cols: 画面の横の分割数

        """

        self.keymap = keymap
        self.grid_rows = rows
        self.grid_cols = cols

        # ディスプレイ情報を取得
        self.monitor_info = pyauto.Window.getMonitorInfo()

        # print(self.monitor_info)

    def _get_grid_size(self, monitor=0, rows=None, cols=None):
        """画面の開始位置、1マスのピクセル数を返却する

        指定されたディスプレイの描画開始位置と分割後の1マスのピクセル数を返却する

        Args:
            monitor: 取得対象のディスプレイNo
            rows: 画面の縦の分割数（未指定時はコンストラクタで指定された値を使用）
            cols: 画面の横の分割数（未指定時はコンストラクタで指定された値を使用）

        Returns:
            ディスプレイ開始位置（x）
            ディスプレイ開始位置（y）
            グリッドサイズ（幅）
            グリッドサイズ（高さ）

        """

        # ディスプレイNoを範囲内に正規化
        mon_idx = monitor % self._get_monitor_len()

        # ディスプレイ情報を取得
        mon_work_rect = self.monitor_info[mon_idx][1]

        # グリッドサイズを算出
        mon_width = abs(mon_work_rect[0] - mon_work_rect[2])
        mon_height = abs(mon_work_rect[1] - mon_work_rect[3])
        grid_width = mon_width // (cols or self.grid_cols)
        grid_height = mon_height // (rows or self.grid_rows)

        # print(monitor, mon_idx, mon_width, mon_height, grid_width, grid_height)

        # ディスプレイの開始位置とグリッドサイズを返却
        return mon_work_rect[0], mon_work_rect[1], grid_width, grid_height

    def _get_monitor_len(self):
        """ディスプレイ数を返却する

        Returns:
            ディスプレイ数

        """
        return len(self.monitor_info)

    def get_next_monitor_idx(self, pos, offset):
        """指定数オフセットしたディスプレイNoを返却する

        Args:
            pos: 現在のディスプレイNo
            offset: オフセットする数

        Returns:
            オフセット後のディスプレイNo

        """

        # ディスプレイNoとオフセットを範囲内に正規化
        mon_no = self._get_monitor_len()
        if (not pos) or pos < 0 or mon_no < pos:
            pos = 0
        offset = offset % mon_no

        # オフセット後のディスプレイNoを返却
        return (mon_no + pos + offset) % mon_no

    def update_monitor_info(self, rows=None, cols=None):
        """ディスプレイ情報更新処理

        最新のディスプレイ情報及び規定の分割数を更新する

        Args:
            rows: 画面の縦の分割数（未指定時はコンストラクタで指定された値を使用）
            cols: 画面の横の分割数（未指定時はコンストラクタで指定された値を使用）

        """

        # ディスプレイ情報を更新
        self.monitor_info = pyauto.Window.getMonitorInfo()

        # 指定された場合は分割数を更新
        if rows:
            self.grid_rows = rows
        if cols:
            self.grid_cols = cols

    def move_window(self, x, y, width, height, monitor=0, rows=None, cols=None):
        """ウインドウ移動処理

        アクティブなウインドウを指定の位置に移動する

        Args:
            x: ウインドウの開始位置（x）
            y: ウインドウの開始位置（y）
            width: ウインドウの幅
            height: ウインドウの高さ
            monitor: ディスプレイNo（未指定時はメインディスプレイ）
            rows: 画面の縦の分割数（未指定時はコンストラクタで指定された値を使用）
            cols: 画面の横の分割数（未指定時はコンストラクタで指定された値を使用）

        """

        # グリッドサイズを取得
        mon_x, mon_y, grid_width, grid_height = self._get_grid_size(monitor, rows, cols)

        # ウインドウサイズを設定
        start_x = mon_x + x * grid_width
        start_y = mon_y + y * grid_height
        end_x = start_x + width * grid_width
        end_y = start_y + height * grid_height

        # print(start_x, start_y, end_x, end_y)

        # ウインドウを取得
        window = self.keymap.getTopLevelWindow()

        # ウインドウのギャップを取得
        win_rect = window.getRect()
        cli_rect = window.getClientRect()

        edge_w = abs(((win_rect[2] - win_rect[0]) - (cli_rect[2] - cli_rect[0])) // 2)
        edge_h = abs((win_rect[3] - win_rect[1]) - (cli_rect[3] - cli_rect[1]))

        # print(win_rect, cli_rect, edge_w, edge_h)

        # サイズを設定（最大化時は解除）
        if window.isMaximized():
            window.restore()

        window.setRect([start_x - edge_w, start_y, end_x + edge_w, end_y + edge_h])
