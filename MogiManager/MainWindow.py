#メインウィンドウ

import tkinter as tk
import Global as G

FrmMainWindow = tk.Frame(G.root, width=1280, height=720)
cv = G.refer()
cv.DrawGrid(FrmMainWindow, 1280, 720)

LblTitle = tk.Label(cv.CvArea, text="メインウィンドウ", font=("", 45))
LblTitle.place(y=0, x=0)