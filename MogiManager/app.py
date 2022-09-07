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

def nextWindow():
    pw = Wakeup.EntPassword.get()
    if pw==G.WakeupPASSWORD:
        G.OpenDate = Wakeup.DeOpenDate.get_date()
        d_week = {'Sun': '日', 'Mon': '月', 'Tue': '火', 'Wed': '水',
                  'Thu': '木', 'Fri': '金', 'Sat': '土'}
        key = G.OpenDate.strftime('%a')
        w = d_week[key]
        d = G.OpenDate.strftime('営業日：%Y年%m月%d日 ') + f'{w}'
        G.OpenDate = d
        MainWindow.openDate.set(d)

        Wakeup.FrmWakeup.place_forget()
        G.root.geometry("1920x1080")
        #G.root.attributes('-fullscreen', True)
        MainWindow.FrmMainWindow.place(y=0, x=0)
    else:
        msg.showwarning("", "パスワードが正しくありません")
    

BtnChange = tk.Button(Wakeup.FrmWakeup, text="営業開始", command=nextWindow, font=("", 35), bg="#1111ff", width=8, height=2)
BtnChange.place(y=460, x=480, anchor=tk.CENTER)

# アプリケーション開始処理
MainWindow.clock()
G.root.mainloop()