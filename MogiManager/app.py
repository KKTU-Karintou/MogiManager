#メインプログラム

import tkinter as tk
from tkinter import messagebox as msg
import Global as G
import MainWindow
import Wakeup

# ルートウィンドウ作成
G.root.title("模擬店マネージャー ver.1.0.0a")
G.root.geometry('960x540')
G.root.resizable(width=False, height=False)

Wakeup.FrmWakeup.place(y=0, x=0)

def nextWindow():
    pw = Wakeup.EntPassword.get()
    if pw=="password":
        Wakeup.FrmWakeup.place_forget()
        G.root.geometry('1280x720')
        MainWindow.FrmMainWindow.place(y=0, x=0)
    else:
        msg.showwarning("", "パスワードが正しくありません")
    

BtnChange = tk.Button(Wakeup.cv.CvArea, text="営業開始", command=nextWindow, font=("", 35), bg="#1111ff", width=8, height=2)
BtnChange.place(y=460, x=480, anchor=tk.CENTER)

# メインループ
G.root.mainloop()