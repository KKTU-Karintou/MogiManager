import tkinter as tk
from tkinter import messagebox
import Global as G

WIN_W = 1280
WIN_H = 720
WIN_SIZE = "1280x720"

master = tk.Toplevel(G.root, width=WIN_W, height=WIN_H)
master.title("システム設定")
master.geometry(WIN_SIZE)
master.maxsize(WIN_W, WIN_H)
master.withdraw()

temp: tk.Label
def initWindow():
    global temp
    temp = tk.Label(master)

FrmSettings = tk.Frame(master, width=WIN_W, height=WIN_H)
FrmSettings.place(y=0, x=0)

LblTitle = tk.Label(FrmSettings, text="システム設定", font=("", 45))
LblTitle.place(y=0, x=0)

LblAdminPswd = tk.Label(FrmSettings, text="管理者パスワード", font=("", 20))
LblAdminPswd.place(y=40, x=700, anchor="w")

EntAdminPswd = tk.Entry(FrmSettings, font=("", 20), width=12, show="*")
EntAdminPswd.place(y=40, x=920, anchor="w")

def checkPass():
    pswd = EntAdminPswd.get()
    if pswd == G.AdminPASSWORD:
        BtnPower.config(state='active')
        EntAdminPswd.delete(0, tk.END)
        FrmSettingButtons.place(y=WIN_H/2-40, x=WIN_W/2, anchor="c")
    else:
        messagebox.showwarning("", "パスワードが間違っています")

BtnActivate = tk.Button(FrmSettings, text="認証", command=checkPass, font=("", 20), width=5, height=1)
BtnActivate.place(y=40, x=1100, anchor="w")

def Shutdown():
    if messagebox.askyesno("アプリケーションの終了", "終了してよろしいですか？"):
        G.root.destroy()
        G.root = None

pwr = tk.PhotoImage(file=r"C:\Users\nakashima\Documents\VSCode\MogiManager\MogiManager\MogiManager\Layout\powerButton.png")
pwr = pwr.subsample(60, 60)
BtnPower = tk.Button(FrmSettings, image=pwr, command=Shutdown, bg="green", width=60, height=60, state='disabled')
BtnPower.place(y=10, x=1270, anchor="ne")

# items of setting buttons
FRM_W = 950
FRM_H = 430
FrmSettingButtons = tk.Frame(FrmSettings, width=FRM_W, height=FRM_H)

def common():
    return tk.Button(FrmSettingButtons, font=("", 25), bg="blue", fg="white", bd=5, width=15, height=3)

BtnSetPasswords = common()
BtnSetPasswords.config(text="パスワード設定", command="")
BtnSetPasswords.place(y=0, x=0, anchor="nw")

BtnSetFunctions = common()
BtnSetFunctions.config(text="機能利用設定", command="")
BtnSetFunctions.place(y=0, x=FRM_W/2, anchor="n")

BtnSetOpening = common()
BtnSetOpening.config(text="営業時間設定", command="")
BtnSetOpening.place(y=0, x=FRM_W, anchor="ne")

BtnSetItems = common()
BtnSetItems.config(text="販売品目設定", command="")
BtnSetItems.place(y=FRM_H/2, x=0, anchor="w")

BtnSetStocks = common()
BtnSetStocks.config(text="在庫設定", command="")
BtnSetStocks.place(y=FRM_H/2, x=FRM_W/2, anchor="c")

BtnSetShifts = common()
BtnSetShifts.config(text="シフト設定", command="")
BtnSetShifts.place(y=FRM_H/2, x=FRM_W, anchor="e")

BtnSetInitMoney = common()
BtnSetInitMoney.config(text="初期現金設定", command="")
BtnSetInitMoney.place(y=FRM_H, x=0, anchor="sw")

BtnSetRefTickets = common()
BtnSetRefTickets.config(text="整理券設定", command="")
BtnSetRefTickets.place(y=FRM_H, x=FRM_W/2, anchor="s")

BtnSetInfoPictures = common()
BtnSetInfoPictures.config(text="掲示画像設定", command="")
BtnSetInfoPictures.place(y=FRM_H, x=FRM_W, anchor="se")

BtnSalesInfo = tk.Button(FrmSettings, text="売上データ", command="", font=("", 30), bg="blue", fg="white", width=20, height=2)
BtnSalesInfo.place(y=620, x=WIN_W/2, anchor="c")

def CloseWindow():
    global temp
    temp.destroy()
    BtnPower.config(state='disabled')
    EntAdminPswd.delete(0, tk.END)
    FrmSettingButtons.place_forget()
    master.withdraw()

BtnClose = tk.Button(FrmSettings, text="閉じる", command=CloseWindow, font=("", 30), bg="blue", fg="white", width=10, height=2)
BtnClose.place(y=700, x=1260, anchor="se")

master.protocol("WM_DELETE_WINDOW", CloseWindow)