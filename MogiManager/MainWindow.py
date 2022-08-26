#メインウィンドウ

import tkinter as tk
import Global as G

FrmMainWindow = tk.Frame(G.root, width=1280, height=720)

LblTitle = tk.Label(FrmMainWindow, text="メインウィンドウ", font=("", 45))
LblTitle.place(y=0, x=0)