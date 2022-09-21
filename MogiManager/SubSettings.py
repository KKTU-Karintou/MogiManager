import tkinter as tk
import tkinter.messagebox as msg
from parse import parse
import References as R
import Global as G
import DAO_SQLite3 as D
import SettingPanels as S

# ベースウィンドウ準備
master = tk.Toplevel()
master.title("詳細設定")
master.resizable(False, False)
master.withdraw()

# データベースアクセスオブジェクト
o = D.Dao()

# モーダルウィンドウ疑似実装
    ### 呼出元は対象としたウィジェットが destroy されたかどうかを見ている。
    ### destroy するとメモリごと消えるので、非表示に対応するため身代わりを用意する。
    ### グローバル変数の参照以外の操作は global を付けないとローカル変数として扱われる。
temp = tk.Label(master)
def initWindow():
    global temp
    temp = tk.Label(master)

def CloseWindow():
    global temp
    temp.destroy()
    temp = tk.Label(master)
    master.withdraw()


    ### 営業時間設定 ###
# ベースフレーム
FrmSetOpentime = tk.Frame(master, width=640, height=360)

# タイトル
LblSOTitle = tk.Label(FrmSetOpentime, text="営業時間設定", font=("", 25))
LblSOTitle.place(y=0, x=0)

# コンテンツ
LblNowOpeningTime = tk.Label(FrmSetOpentime, text="現在の営業時間", font=("", 25))
LblNowOpeningTime.place(y=100, x=75)
LblNowOpeningTimeStr = tk.Label(FrmSetOpentime, text="", font=("", 25))
LblNowOpeningTimeStr.place(y=100, x=330)
LblChangeOpeningTime = tk.Label(FrmSetOpentime, text="変更後営業時間", font=("", 25))
LblChangeOpeningTime.place(y=200, x=75, anchor="w")
LblOpeningTimeBase = tk.Label(FrmSetOpentime, text="00:00 → 00:00", font=("", 25))
LblOpeningTimeBase.place(y=200, x=330, anchor="w")
EntOTHour = tk.Entry(FrmSetOpentime, font=("", 25), bg="yellow", bd=1, relief=tk.SUNKEN)
EntOTHour.place(y=200, x=332, width=35, anchor="w")
EntOTMin = tk.Entry(FrmSetOpentime, font=("", 25), bg="yellow", bd=1, relief=tk.SUNKEN)
EntOTMin.place(y=200, x=374, width=35, anchor="w")
EntCTHour = tk.Entry(FrmSetOpentime, font=("", 25), bg="yellow", bd=1, relief=tk.SUNKEN)
EntCTHour.place(y=200, x=460, width=35, anchor="w")
EntCTMin = tk.Entry(FrmSetOpentime, font=("", 25), bg="yellow", bd=1, relief=tk.SUNKEN)
EntCTMin.place(y=200, x=502, width=35, anchor="w")

# 入力規制用(数字2桁まで受け付ける)
vcmd1 = (EntOTHour.register(R.validation2num), "%P")
EntOTHour.config(validate="key", vcmd=vcmd1)
vcmd2 = (EntOTMin.register(R.validation2num), "%P")
EntOTMin.config(validate="key", vcmd=vcmd2)
vcmd3 = (EntCTHour.register(R.validation2num), "%P")
EntCTHour.config(validate="key", vcmd=vcmd3)
vcmd4 = (EntCTMin.register(R.validation2num), "%P")
EntCTMin.config(validate="key", vcmd=vcmd4)

# コンテンツ設定
def InitSetOpentime():
    OT = G.OpenTime.get()
    CT = G.CloseTime.get()
    OT = parse("営業開始 : {}時{}分", OT).fixed
    CT = parse("営業終了 : {}時{}分", CT).fixed
    Text = OT[0] + ":" + OT[1] + " → " + CT[0]+ ":" + CT[1]
    LblNowOpeningTimeStr.config(text=Text)

# 営業時間変更適用
def ApplyOpeningTime():
    oth = EntOTHour.get()
    otm = EntOTMin.get()
    cth = EntCTHour.get()
    ctm = EntCTMin.get()
    
    if(len(oth)!=0 and len(otm)!=0 and len(cth)!=0 and len(ctm)!=0):
        fmt = f"営業開始 : {oth}時{otm}分"
        G.OpenTime.set(fmt)
        fmt = f"営業終了 : {cth}時{ctm}分"
        G.CloseTime.set(fmt)
        EntOTHour.delete(0, tk.END)
        EntOTMin.delete(0, tk.END)
        EntCTHour.delete(0, tk.END)
        EntCTMin.delete(0, tk.END)

        msg.showinfo("", "営業時間を変更しました。")
        CloseWindow()
    else:
        msg.showinfo("", "有効な値を入力してください。")

BtnSOCancel = tk.Button(FrmSetOpentime, text="キャンセル", command=CloseWindow, font=("", 26), bg="blue")
BtnSOCancel.place(y=300, x=320-25, width=175, height=75, anchor="e")
BtnSOApply = tk.Button(FrmSetOpentime, text="適用", command=ApplyOpeningTime, font=("", 26), bg="blue")
BtnSOApply.place(y=300, x=320+25, width=175, height=75, anchor="w")

    ### 販売品目設定 ###
# ベースフレーム
FrmSetProduct = tk.Frame(master, width=1280, height=720)

# タイトル
LblSPTitle = tk.Label(FrmSetProduct, text="販売品目設定", font=("", 30))
LblSPTitle.place(y=0, x=0)

# 税率設定用フレーム
FrmProductTax = tk.Frame(FrmSetProduct, width=240, height=270, bd=3, relief=tk.SOLID)
FrmProductTax.place(y=10, x=1270, anchor="ne")

# 税率設定コンテンツ
LblSetProductTax = tk.Label(FrmProductTax, text="税率設定", font=("", 27))
LblSetProductTax.place(y=10, x=120, anchor="n")
LblProductBaseTax = tk.Label(FrmProductTax, text="税率      %", font=("", 25))
LblProductBaseTax.place(y=100, x=220, anchor="e")
EntProductBaseTax = tk.Entry(FrmProductTax, font=("", 25), justify=tk.CENTER, state="readonly")
EntProductBaseTax.place(y=100, x=190, width=40, anchor="e")
LblNowProductBaseTax = tk.Label(FrmProductTax, font=("", 25))
LblNowProductBaseTax.place(y=100, x=190, width=40, anchor="e")
LblProductRedTax = tk.Label(FrmProductTax, text="軽減税率      %", font=("", 25))
LblProductRedTax.place(y=150, x=220, anchor="e")
EntProductRedTax = tk.Entry(FrmProductTax, font=("", 25), justify=tk.CENTER, state="readonly")
EntProductRedTax.place(y=150, x=190, width=40, anchor="e")
LblNowProductRedTax = tk.Label(FrmProductTax, font=("", 25))
LblNowProductRedTax.place(y=150, x=190, width=40, anchor="e")
BtnSetProductTax = tk.Button(FrmProductTax, text="税率変更", font=("", 25), bg="orange")
BtnSetProductTax.place(y=200, x=120, width=200, height=60, anchor="n")

# 入力規制用(数字2桁まで受け付ける)
vcmd5 = (EntProductBaseTax.register(R.validation2num), "%P")
EntProductBaseTax.config(validate="key", vcmd=vcmd5)
vcmd6 = (EntProductRedTax.register(R.validation2num), "%P")
EntProductRedTax.config(validate="key", vcmd=vcmd6)

def EditTaxRate():
    EntProductBaseTax.config(state="normal")
    EntProductBaseTax.lift()
    EntProductRedTax.config(state="normal")
    EntProductRedTax.lift()
    BtnSetProductTax.config(text="適用", command=ApplyTaxRate)

def ApplyTaxRate():
    bt = EntProductBaseTax.get()
    rt = EntProductRedTax.get()
    if(len(bt)>0 and len(rt)>0):
        EntProductBaseTax.config(state="readonly")
        EntProductRedTax.config(state="readonly")
        G.BaseTax = int(bt)
        G.ReduceTax = int(rt)
        BtnSetProductTax.config(text="税率変更", command=EditTaxRate)
        LblNowProductBaseTax.config(text=G.BaseTax)
        LblNowProductBaseTax.lift()
        LblNowProductRedTax.config(text=G.ReduceTax)
        LblNowProductRedTax.lift()
    else:
        msg.showwarning("", "有効な値を入力してください")

# 一覧用ヘッダーフレーム
FrmProductHeader = tk.Frame(FrmSetProduct, width=1000, height=60, bg="yellow green")
FrmProductHeader.place(y=50, x=20)

# ヘッダーコンテンツ
BaseX = 200
LblItemName = tk.Label(FrmProductHeader, text="商品名", font=("", 25))
LblItemName.place(y=30, x=BaseX, anchor="c")
LblItemPrice = tk.Label(FrmProductHeader, text="価格", font=("", 25))
LblItemPrice.place(y=30, x=BaseX+300, anchor="c")
LblItemIntax = tk.Label(FrmProductHeader, text="内税", font=("", 25))
LblItemIntax.place(y=30, x=BaseX+450, anchor="c")
LblItemRedtax = tk.Label(FrmProductHeader, text="軽減税", font=("", 25))
LblItemRedtax.place(y=30, x=BaseX+575, anchor="c")

# 一覧用スクロールバー付きベースフレーム
FrmProducts = R.ScrollableFrame(FrmSetProduct, bar_x=False)
FrmProducts.place(y=110, x=20, width=1000, height=540)

# ベースフレームへのアクセス簡便化
FrmMenus = FrmProducts.scrollable_frame
FrmMenus.config(width=1000, height=200, bg="blue")

# 一覧生成(再生成処理)
    ### 生成したオブジェクト群は画面に配置後、制御を離れる。
    ### そのためフレームごと破棄すれば参照がなくなり破棄される。はず・・・
FrmContents = tk.Frame(FrmMenus, width=1000)
FrmContents.place(y=0, x=0)

BaseY = 100
SpanY = 75
def RefreshTable():
    global FrmContents

    # 既存のフレームを破棄して再生成
    FrmContents.destroy()
    FrmContents = tk.Frame(FrmMenus, width=1000, bg='orange')
    FrmContents.place(y=0, x=0)

    # データを読み出す
    row_data = []
    items = o.FindAllItems()
    for i in range(len(items)):
        item = R.ProductSet(FrmContents)
        item.id = items[i].id
        item.name.set(items[i].name)
        item.price.set(items[i].price)
        item.bool_inTax = items[i].inTax
        # わかりやすいように bool を「はい、いいえ」に変換する。
        if(items[i].inTax):
            item.inTax.set("はい")
        else:
            item.inTax.set("いいえ")
        item.bool_redTax = items[i].reduceTax
        if(items[i].reduceTax):
            item.redTax.set("はい")
        else:
            item.redTax.set("いいえ")

        row_data.append(item)

    # 並べる
    for i in range(len(row_data)):
        row_data[i].lbl_name.place(y=BaseY+SpanY*i-50, x=BaseX, anchor="c")
        row_data[i].lbl_price.place(y=BaseY+SpanY*i-50, x=BaseX+300, anchor="c")
        row_data[i].lbl_inTax.place(y=BaseY+SpanY*i-50, x=BaseX+450, anchor="c")
        row_data[i].lbl_redTax.place(y=BaseY+SpanY*i-50, x=BaseX+575, anchor="c")
        row_data[i].btn_edit.place(y=BaseY+SpanY*i-50, x=BaseX+700, anchor="c")
        row_data[i].btn_edit.bind("<Button-1>", row_data[i].PrepareEditProduct)
        row_data[i].btn_edit.bind("<Button-1>", EditProduct, "+")

        # 行数に合わせて表示領域を伸ばしておく(伸ばされるのはスクロール対象フレーム)
            ### 本来は FrmMenus がスクロール対象フレームだが、更新の際に破棄する必要がある。
            ### そのため、さらにフレームを重ねている。
        FrmMenus.config(height=BaseY+SpanY*i)
        FrmContents.config(height=BaseY+SpanY*i)

def Cleanup():
    # コントロールロックを外す
    S.master.grab_release()

    # コンテンツの初期化
    S.FrmProduct.place_forget()
    S.EntProductName.delete(0, tk.END)
    S.EntProductPrice.delete(0, tk.END)
    S.ProductIntax.set(False)
    S.ProductRedtax.set(False)

    # 更新があれば一覧も更新
    if(G.UpdateItemList):
        RefreshTable()

def AddProduct():
    # コンテンツ設定
    S.LblProductTitle.config(text="商品追加")
    S.BtnProductApply.config(command=S.AddProduct, text="登録")
    S.FrmProduct.place(y=0, x=0, width=500, height=600)

    # 初期化/画面構成設定
    S.initWindow()
    S.master.geometry("500x600")
    S.master.transient(master)
    S.master.grab_set()
    S.master.focus_set()
    S.master.deiconify()

    # 閉じられるまで待つ
    master.wait_window(S.temp)

    # 初期化
    Cleanup()

def EditProduct(event):
    # コンテンツ設定
    S.LblProductTitle.config(text="商品編集")
    S.BtnProductApply.config(command=S.ApplyProduct, text="更新")

    data = o.FindItemById(G.ProductEditId)
    S.EntProductName.insert(0, data.name)
    S.EntProductPrice.insert(0, data.price)
    S.ProductIntax.set(data.inTax)
    S.ProductRedtax.set(data.reduceTax)
    S.FrmProduct.place(y=0, x=0, width=500, height=600)
    S.BtnProductDelete.place(y=500, x=20)

    # 初期化/画面構成設定
    S.initWindow()
    S.master.geometry("500x600")
    S.master.deiconify()
    S.master.transient(master)
    S.master.grab_set()
    S.master.focus_set()

    # 閉じられるまで待つ
    master.wait_window(S.temp)

    # 初期化
    Cleanup()

# ボタン
BtnAddProduct = tk.Button(FrmSetProduct, text="商品追加", command=AddProduct, font=("", 35), bg="orange")
BtnAddProduct.place(y=500, x=1030)

BtnSPClose = tk.Button(FrmSetProduct, text="閉じる", command=CloseWindow, font=("", 35), bg="blue", fg="white")
BtnSPClose.place(y=700, x=1260, anchor="se")

# 各ボタンのコールバック設定
BtnSetProductTax.config(command=EditTaxRate)

# ×ボタンにコールバックを設定
master.protocol("WM_DELETE_WINDOW", CloseWindow)