#メインウィンドウ

import tkinter as tk
import Global as G

WIN_W = 1280
WIN_H = 720
TAB_W = 1000
TAB_H = 500

        #グリッドを使うには G.refer クラスの DrawGrid メソッドを使ってください
        #配置が終わったら置換機能で インスタンス名.CvArea を 各フレーム名に設定してください

### ベース画面      Main
#cv.CvArea => FrmMainWindow
FrmMainWindow = tk.Frame(G.root, width=WIN_W, height=WIN_H)
cv = G.refer()
cv.DrawGrid(FrmMainWindow, WIN_W, WIN_H)

LblTitle = tk.Label(cv.CvArea, text="メインウィンドウ", font=("", 45))
LblTitle.place(y=0, x=0)

### 注文タブ        Orders
FrmOrder = tk.Frame(cv.CvArea, width=TAB_W, height=TAB_H)


### 整理券タブ      Reference Numbers
FrmRefNum = tk.Frame(cv.CvArea, width=TAB_W, height=TAB_H)


### 在庫タブ        Stocks
FrmStock = tk.Frame(cv.CvArea, width=TAB_W, height=TAB_H)


### 注文履歴タブ    Past Orders
FrmPastOrder = tk.Frame(cv.CvArea, width=TAB_W, height=TAB_H)