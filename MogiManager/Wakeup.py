#営業設定画面

import tkinter as tk
import tkinter.ttk as ttk
import tkcalendar as tkc
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

# 天候
LblWeather = tk.Label(FrmWakeup, text="天気", font=("", 25), anchor="e")
LblWeather.place(y=200, x=430, anchor="e")
weathers = ["晴れ", "くもり", "雨", "雪", "その他"]
weather = tk.StringVar()
CbWeather = ttk.Combobox(FrmWakeup, value=weathers, textvariable=weather, state="readonly", font=("", 20), width=10)
CbWeather.place(y=200, x=450, anchor="w")

# 初期現金
LblInitMoney = tk.Label(FrmWakeup, text="初期現金                円", font=("", 25), anchor="e")
LblInitMoney.place(y=250, x=624, anchor="e")
initMoney = tk.IntVar()
EntInitMoney = tk.Entry(FrmWakeup, textvariable=initMoney, font=("", 25), width=7, justify="right")
EntInitMoney.place(y=250, x=450, anchor="w")

# パスワード
LblPassword = tk.Label(FrmWakeup, text="起動パスワード", font=("", 25), anchor="e")
LblPassword.place(y=335, x=430, anchor="e")
password = tk.StringVar()
EntPassword = tk.Entry(FrmWakeup, textvariable=password, font=("", 25), width=15, show="*")
EntPassword.place(y=335, x=450, anchor="w")