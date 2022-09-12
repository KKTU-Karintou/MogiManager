#メインプログラム

import tkinter as tk
from tkinter import messagebox as msg
import Global as G
import MainWindow
import Wakeup

# ルートウィンドウ作成
G.root.title("模擬店マネージャー ver.1.0.0a")
G.root.geometry("960x540")
G.root.maxsize(width=1920, height=1080)

Wakeup.FrmWakeup.place(y=0, x=0)

# アプリケーション開始処理
MainWindow.clock()
G.root.mainloop()