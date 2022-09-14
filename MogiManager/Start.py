#営業設定画面

import tkinter as tk
import tkinter.ttk as ttk
import tkcalendar as tkc
import tkinter.messagebox as msg
import Global as G
import MainWindow as M

G.root.title("模擬店マネージャー ver.1.0.0a")
G.root.geometry("960x540")
G.root.maxsize(width=1920, height=1080)

monitor_height = G.root.winfo_screenheight()
monitor_width = G.root.winfo_screenwidth()
  
FrmWakeup = tk.Frame(G.root, width=960, height=540)
FrmWakeup.place(y=0, x=0)

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

def nextWindow():
    pw = EntPassword.get()
    if pw == G.WAKEUP_PASSWORD or pw == G.MASTER_PASSWORD:
        date = DeOpenDate.get_date()
        d_week = {'Sun': '日', 'Mon': '月', 'Tue': '火', 'Wed': '水',
                  'Thu': '木', 'Fri': '金', 'Sat': '土'}
        key = date.strftime('%a')
        w = d_week[key]
        d = date.strftime('営業日：%Y年%m月%d日 ') + f'{w}'
        e = date.strftime('%Y_%m_%d')
        f = date.strftime('%Y')
        G.OpenDate.set(d)
        G.OpenDateStr = e
        G.OpenDateYear = f

        FrmWakeup.destroy()
        G.root.geometry("1920x1080")
        if(monitor_width==1920 and monitor_height==1080):
            G.root.attributes('-fullscreen', True)
        M.FrmMainWindow.place(y=0, x=0)
    else:
        msg.showwarning("", "パスワードが正しくありません")
    

BtnChange = tk.Button(FrmWakeup, text="営業開始", command=nextWindow, font=("", 35), bg="#1111ff", width=8, height=2)
BtnChange.place(y=460, x=480, anchor=tk.CENTER)

def Shutdown():
    if msg.askyesno("アプリケーションの終了", "終了してよろしいですか？"):
        G.root.destroy()
        G.root = None

BtnShutdown = tk.Button(FrmWakeup, text="終了", command=Shutdown, font=("", 30), bg="orange")
BtnShutdown.place(y=10, x=950, anchor="ne")

G.root.protocol("WM_DELETE_WINDOW", Shutdown)
M.clock()
M.total()
G.root.mainloop()