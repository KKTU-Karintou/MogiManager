#メインウィンドウ
from re import T
import tkinter as tk
import datetime as dt
import Global as G
import Settings as S

WIN_W = 1920
WIN_H = 1080
TAB_W = 1000
TAB_H = 500

        # グリッドを使うには G.refer クラスの DrawGrid メソッドを使ってください
        # 配置が終わったら置換機能で インスタンス名.CvArea を 各フレーム名に設定してください
        # 赤は200px, 濃いグレーは100px, 薄いグレーが20px

### ベース画面      Main
#cv.CvArea => FrmMainWindow
FrmMainWindow = tk.Frame(G.root, width=WIN_W, height=WIN_H)
cv = G.refer()
cv.DrawGrid(FrmMainWindow, WIN_W, WIN_H)

openDate = tk.StringVar()
LblOpenDate = tk.Label(cv.CvArea, textvariable=openDate, font=("", 20), bd=3, relief=tk.SOLID, width=26)
LblOpenDate.place(y=10, x=10)

nowTime = tk.StringVar()
LblNowTime = tk.Label(cv.CvArea, textvariable=nowTime, font=("", 40), bd=3, relief=tk.SOLID, width=8)
LblNowTime.place(y=20, x=WIN_W/2, anchor=tk.N)


# commands
def OpenSettings():
    S.initWindow()
    S.master.grab_set()
    S.master.focus_set()
    S.master.transient(G.root)
    S.master.deiconify()
    G.root.wait_window(S.temp)
    if G.root!=None:
        S.master.grab_release()


BtnSettings = tk.Button(cv.CvArea, command=OpenSettings, text="🔑", font=("", 30), bg="orange", width=5, height=1)
BtnSettings.place(y=10, x=WIN_W-10, anchor="ne")


### 注文タブ        Orders
FrmOrder = tk.Frame(cv.CvArea, width=TAB_W, height=TAB_H)


### 整理券タブ      Reference Numbers
FrmRefNum = tk.Frame(cv.CvArea, width=TAB_W, height=TAB_H)


### 在庫タブ        Stocks
FrmStock = tk.Frame(cv.CvArea, width=TAB_W, height=TAB_H)


### 注文履歴タブ    Past Orders
FrmPastOrder = tk.Frame(cv.CvArea, width=TAB_W, height=TAB_H)



### 関数
def clock():
    n = dt.datetime.now()
    t = n.strftime('%H時%M分')
    G.NowTime = T
    nowTime.set(t)

    FrmMainWindow.after(100, clock)