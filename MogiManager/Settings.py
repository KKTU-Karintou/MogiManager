import tkinter as tk
import tkinter.messagebox as msg
import Global as G
import SubSettings as S

# ベースウィンドウ準備
WIN_W = 1280
WIN_H = 720
WIN_SIZE = "1280x720"

master = tk.Toplevel(width=WIN_W, height=WIN_H)
master.title("システム設定")
master.geometry(WIN_SIZE)
master.resizable(False, False)
master.withdraw()

# モーダルウィンドウ疑似実装 ###
    ### 呼出元は対象としたウィジェットが destroy されたかどうかを見ている。
    ### destroy するとメモリごと消えるので、非表示に対応するため身代わりを用意する。
    ### グローバル変数の参照以外の操作は global を付けないとローカル変数として扱われる。
temp: tk.Label
def initWindow():
    global temp
    temp = tk.Label(master)
    BtnPower.config(state="disabled")
    EntAdminPswd.config(state="normal")
    BtnActivate.config(state="normal")

def CloseWindow():
    global temp
    temp.destroy()
    BtnPower.config(state="disabled")
    EntAdminPswd.config(state="normal")
    BtnActivate.config(state="normal")
    EntAdminPswd.delete(0, tk.END)
    FrmSettingButtons.place_forget()
    master.withdraw()

# 設定一覧用ベースフレーム
FrmSettings = tk.Frame(master, width=WIN_W, height=WIN_H)
FrmSettings.place(y=0, x=0)

# タイトル
LblTitle = tk.Label(FrmSettings, text="システム設定", font=("", 45))
LblTitle.place(y=0, x=0)


    ### パスワード認証機能 ###
LblAdminPswd = tk.Label(FrmSettings, text="管理者パスワード", font=("", 20))
LblAdminPswd.place(y=40, x=700, anchor="w")
EntAdminPswd = tk.Entry(FrmSettings, font=("", 20), width=12, show="*")
EntAdminPswd.place(y=40, x=920, anchor="w")

def checkPass():
    pw = EntAdminPswd.get()
    if pw == G.ADMIN_PASSWORD or pw == G.MASTER_PASSWORD:
        BtnPower.config(state='active')
        EntAdminPswd.delete(0, tk.END)
        EntAdminPswd.config(state="readonly")
        BtnActivate.config(state="disabled")
        FrmSettingButtons.place(y=WIN_H/2-40, x=WIN_W/2, anchor="c")

    else:
        msg.showwarning("", "パスワードが間違っています")

BtnActivate = tk.Button(FrmSettings, text="認証", command=checkPass, font=("", 20), width=5, height=1)
BtnActivate.place(y=40, x=1100, anchor="w")


    ### アプリケーション終了機能 ###
def Shutdown():
    if msg.askyesno("アプリケーションの終了", "終了してよろしいですか？"):
        G.root.destroy()
        # GUIが消し飛んでも処理は残っているのでコントロールロック解除処理用に残しておく
        G.root = None

pwr = tk.PhotoImage(file="MogiManager/powerButton.png")
pwr = pwr.subsample(60, 60)
BtnPower = tk.Button(FrmSettings, image=pwr, command=Shutdown, bg="green", width=60, height=60, state='disabled')
BtnPower.place(y=10, x=1270, anchor="ne")


    ### 各種設定用ボタン生成 ###
FRM_W = 950
FRM_H = 430
FrmSettingButtons = tk.Frame(FrmSettings, width=FRM_W, height=FRM_H)

# ボタンは文字とコールバック以外共通なのでまとめる
def common():
    return tk.Button(FrmSettingButtons, font=("", 25), bg="blue", fg="white", bd=5, width=15, height=3)


    ### パスワード設定 ###
BtnSetPasswords = common()
BtnSetPasswords.config(text="パスワード設定", command="")
BtnSetPasswords.place(y=0, x=0, anchor="nw")


    ### 機能利用設定 ###
BtnSetFunctions = common()
BtnSetFunctions.config(text="機能利用設定", command="")
BtnSetFunctions.place(y=0, x=FRM_W/2, anchor="n")


    ### 営業時間設定 ###
def OpenSetOpentime():
    S.initWindow()
    S.master.geometry("640x360")
    S.InitSetOpentime()
    S.FrmSetOpentime.place(y=0, x=0, width=640, height=360)
    S.master.grab_set()
    S.master.focus_set()
    S.master.transient(master)
    S.master.deiconify()
    master.wait_window(S.temp)
    S.FrmSetOpentime.place_forget()
    S.master.grab_release()

BtnSetOpening = common()
BtnSetOpening.config(text="営業時間設定", command=OpenSetOpentime)
BtnSetOpening.place(y=0, x=FRM_W, anchor="ne")


    ### 販売品目設定 ###
def OpenSetProduct():
    # 初期化/画面構成設定
    S.RefreshTable()
    S.initWindow()
    S.master.geometry("1280x720")
    S.master.grab_set()
    S.master.focus_set()
    S.master.transient(master)
    S.master.deiconify()

    # コンテンツ設定
    S.FrmSetProduct.place(y=0, x=0, width=1280, height=720)
    S.LblNowProductBaseTax.config(text=G.BaseTax)
    S.LblNowProductBaseTax.lift()
    S.LblNowProductRedTax.config(text=G.ReduceTax)
    S.LblNowProductRedTax.lift()
    
    # 閉じられるまで待つ
    master.wait_window(S.temp)

    # 初期化
    S.FrmSetProduct.place_forget()
    S.master.grab_release()

BtnSetItems = common()
BtnSetItems.config(text="販売品目設定", command=OpenSetProduct)
BtnSetItems.place(y=FRM_H/2, x=0, anchor="w")


    ### 在庫設定 ###
BtnSetStocks = common()
BtnSetStocks.config(text="在庫設定", command="")
BtnSetStocks.place(y=FRM_H/2, x=FRM_W/2, anchor="c")


    ### シフト設定 ###
BtnSetShifts = common()
BtnSetShifts.config(text="シフト設定", command="")
BtnSetShifts.place(y=FRM_H/2, x=FRM_W, anchor="e")


    ### 初期現金設定 ###
BtnSetInitMoney = common()
BtnSetInitMoney.config(text="初期現金設定", command="")
BtnSetInitMoney.place(y=FRM_H, x=0, anchor="sw")


    ### 整理券設定 ###
BtnSetRefTickets = common()
BtnSetRefTickets.config(text="整理券設定", command="")
BtnSetRefTickets.place(y=FRM_H, x=FRM_W/2, anchor="s")


    ### 掲示画像設定 ###
BtnSetInfoPictures = common()
BtnSetInfoPictures.config(text="掲示画像設定", command="")
BtnSetInfoPictures.place(y=FRM_H, x=FRM_W, anchor="se")


    ### 売上データ ###
BtnSalesInfo = tk.Button(FrmSettings, text="売上データ", command="", font=("", 30), bg="blue", fg="white", width=20, height=2)
BtnSalesInfo.place(y=620, x=WIN_W/2, anchor="c")


# 閉じるボタン
BtnClose = tk.Button(FrmSettings, text="閉じる", command=CloseWindow, font=("", 30), bg="blue", fg="white", width=10, height=2)
BtnClose.place(y=700, x=1260, anchor="se")

# ×ボタンにコールバックを設定
master.protocol("WM_DELETE_WINDOW", CloseWindow)