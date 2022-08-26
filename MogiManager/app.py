#メインプログラム

import tkinter as tk
import Global as G
import MainWindow
import Wakeup

# トップレベルウィンドウ作成
G.root.title("模擬店マネージャー ver.1.0.0a")
G.root.geometry('960x540')
G.root.resizable(width=False, height=False)

Wakeup.FrmWakeup.place(y=0, x=0)


def nextWindow():
    Wakeup.FrmWakeup.place_forget()
    G.root.geometry('1280x720')
    MainWindow.FrmMainWindow.place(y=0, x=0)

BtnChange = tk.Button(Wakeup.FrmWakeup, text="営業開始", command=nextWindow, font=("", 35), bg="#1111ff", width=10, height=3)
BtnChange.place(y=220, x=430)

# メインループ
G.root.mainloop()