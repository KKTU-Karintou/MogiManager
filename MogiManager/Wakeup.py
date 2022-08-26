#営業設定画面

import tkinter as tk
import tkinter.ttk as ttk
import tkcalendar as tkc
import Global as G

FrmWakeup = tk.Frame(G.root, width=960, height=540)

LblTitle = tk.Label(FrmWakeup, text="営業設定", font=("", 45))
LblTitle.place(y=0, x=0)

LblOpenDate = tk.Label(FrmWakeup, text="営業日", font=("", 25))
LblOpenDate.place(y=100, x=100)

DpOpenDate = tkc.DateEntry(master=FrmWakeup, showweeknumbers=False, state="readonly", font=("", 20))
DpOpenDate.place(y=100, x=200)