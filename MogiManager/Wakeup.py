#営業設定画面

import tkinter as tk
import tkinter.ttk as ttk
import tkcalendar as tkc
import tkinter.messagebox as msg
import Global as G

FrmWakeup = tk.Frame(G.root, width=960, height=540)

LblTitle = tk.Label(FrmWakeup, text="営業設定", font=("", 45))
LblTitle.place(y=0, x=0)

# 営業日
LblOpenDate = tk.Label(FrmWakeup, text="営業日", font=("", 25), anchor="e")
LblOpenDate.place(y=150, x=430, anchor="e")
openDate = tk.StringVar()
DeOpenDate = tkc.DateEntry(master=FrmWakeup, textvariable=openDate, showweeknumbers=False, state="readonly", font=("", 20))
DeOpenDate.place(y=150, x=450, anchor="w")

# 初期現金
LblInitMoney = tk.Label(FrmWakeup, text="初期現金                円", font=("", 25), anchor="e")
LblInitMoney.place(y=200, x=624, anchor="e")
EntInitMoney = tk.Entry(FrmWakeup, font=("", 25), width=7, justify="right")
EntInitMoney.place(y=200, x=450, anchor="w")

# 担当者 Person In Charge : PIC
LblPIC = tk.Label(FrmWakeup, text="担当者", font=("", 25), anchor="e")
LblPIC.place(y=250, x=430, anchor="e")
EntPIC = tk.Entry(FrmWakeup, font=("", 20), width=10)
EntPIC.place(y=250, x=450, anchor="w")

# パスワード
LblPassword = tk.Label(FrmWakeup, text="起動パスワード", font=("", 25), anchor="e")
LblPassword.place(y=335, x=430, anchor="e")
EntPassword = tk.Entry(FrmWakeup, font=("", 25), width=15, show="*")
EntPassword.place(y=335, x=450, anchor="w")

def Shutdown():
    if msg.askyesno("アプリケーションの終了", "終了してよろしいですか？"):
        G.root.destroy()
        G.root = None

BtnShutdown = tk.Button(FrmWakeup, text="終了", command=Shutdown, font=("", 30), bg="orange")
BtnShutdown.place(y=10, x=950, anchor="ne")

G.root.protocol("WM_DELETE_WINDOW", Shutdown)