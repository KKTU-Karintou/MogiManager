import tkinter as tk
import tkinter.messagebox as msg
from parse import parse
import References as R
import Global as G
import DAO_SQLite3 as Dao
import SettingPanels as S

master = tk.Toplevel()
master.title("詳細設定")
master.resizable(False, False)
master.withdraw()

temp: tk.Label
def initWindow():
    global temp
    temp = tk.Label(master)

def CloseWindow():
    global temp
    temp.destroy()
    master.withdraw()

    # 営業時間設定
FrmSetOpentime = tk.Frame(master, width=640, height=360)

LblSOTitle = tk.Label(FrmSetOpentime, text="営業時間設定", font=("", 25))
LblSOTitle.place(y=0, x=0)


LblNowOpentime = tk.Label(FrmSetOpentime, text="現在の営業時間", font=("", 25))
LblNowOpentime.place(y=100, x=75)
LblChangeOpentime = tk.Label(FrmSetOpentime, text="変更後営業時間", font=("", 25), bg="blue")
LblChangeOpentime.place(y=200, x=75, anchor="w")
LblOpentimeBase = tk.Label(FrmSetOpentime, text="          ", font=("", 25), bg="green")
LblOpentimeBase.place(y=200, x=330, width=100, height=40, anchor="w")
EntOTHour = tk.Entry(FrmSetOpentime, font=("", 25), bd=0)
EntOTHour.place(y=200, x=330, width=35, anchor="w")
EntOTMin = tk.Entry(FrmSetOpentime, font=("", 25), bd=0)
EntOTMin.place(y=200, x=370, width=35, anchor="w")
LblClosetimeBase = tk.Label(FrmSetOpentime, text="          ", font=("", 25), bg="yellow")
LblClosetimeBase.place(y=200, x=460, width=100, height=40, anchor="w")
EntCTHour = tk.Entry(FrmSetOpentime, font=("", 25), bd=0)
EntCTHour.place(y=200, x=460, width=35, anchor="w")
EntCTMin = tk.Entry(FrmSetOpentime, font=("", 25), bd=0)
EntCTMin.place(y=200, x=500, width=35, anchor="w")

vcmd1 = (EntOTHour.register(R.validation), "%s", "%P")
EntOTHour.config(validate="key", vcmd=vcmd1)
vcmd2 = (EntOTMin.register(R.validation), "%s", "%P")
EntOTMin.config(validate="key", vcmd=vcmd2)
vcmd3 = (EntCTHour.register(R.validation), "%s", "%P")
EntCTHour.config(validate="key", vcmd=vcmd3)
vcmd4 = (EntCTMin.register(R.validation), "%s", "%P")
EntCTMin.config(validate="key", vcmd=vcmd4)

def InitSetOpentime():
    OT = G.OpenTime.get()
    CT = G.CloseTime.get()
    OT = parse("営業開始 : {}時{}分", OT).fixed
    CT = parse("営業終了 : {}時{}分", CT).fixed
    Text = "現在の営業時間  " + OT[0] + ":" + OT[1] + " → " + CT[0]+ ":" + CT[1]
    LblNowOpentime.config(text=Text)

    # 販売品目設定
FrmSetProduct = tk.Frame(master, width=1280, height=720)

LblSPTitle = tk.Label(FrmSetProduct, text="販売品目設定", font=("", 30))
LblSPTitle.place(y=0, x=0)

FrmProductHeader = tk.Frame(FrmSetProduct, width=1000, height=60, bg="yellow green")
FrmProductHeader.place(y=50, x=20)

FrmProducts = R.ScrollableFrame(FrmSetProduct, bar_x=False)
FrmProducts.place(y=110, x=20, width=1000, height=540)

FrmMenus = FrmProducts.scrollable_frame
FrmMenus.config(width=1000, bg="blue")

BaseX = 200
BaseY = 100
SpanY = 75
LblItemName = tk.Label(FrmProductHeader, text="商品名", font=("", 25))
LblItemName.place(y=30, x=BaseX, anchor="c")
LblItemPrice = tk.Label(FrmProductHeader, text="価格", font=("", 25))
LblItemPrice.place(y=30, x=BaseX+300, anchor="c")
LblItemIntax = tk.Label(FrmProductHeader, text="内税", font=("", 25))
LblItemIntax.place(y=30, x=BaseX+450, anchor="c")
LblItemRedtax = tk.Label(FrmProductHeader, text="軽減税", font=("", 25))
LblItemRedtax.place(y=30, x=BaseX+575, anchor="c")

FrmMenus.config(height=200)

# 一覧生成(再生成)
FrmContents = tk.Frame(FrmMenus, width=1000)
FrmContents.place(y=0, x=0)

def RefreshTable():
    global FrmContents

    FrmContents.destroy()
    FrmContents = tk.Frame(FrmMenus, width=1000, bg='orange')
    FrmContents.place(y=0, x=0)

    o = Dao.Dao()
    row_data = []
    items = o.FindAllItems()
    for i in range(len(items)):
        item = R.ProductSet(FrmContents)
        item.id = items[i].id
        item.name.set(items[i].name)
        item.price.set(items[i].price)
        item.bool_inTax = items[i].inTax
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

    for i in range(len(row_data)):
        row_data[i].lbl_name.place(y=BaseY+SpanY*i-50, x=BaseX, anchor="c")
        row_data[i].lbl_price.place(y=BaseY+SpanY*i-50, x=BaseX+300, anchor="c")
        row_data[i].lbl_inTax.place(y=BaseY+SpanY*i-50, x=BaseX+450, anchor="c")
        row_data[i].lbl_redTax.place(y=BaseY+SpanY*i-50, x=BaseX+575, anchor="c")
        row_data[i].btn_edit.place(y=BaseY+SpanY*i-50, x=BaseX+700, anchor="c")
        row_data[i].btn_edit.bind("<Button-1>", row_data[i].EditProduct)
        row_data[i].btn_edit.bind("<Button-1>", EditProduct, "+")

        FrmMenus.config(height=BaseY+SpanY*i)
        FrmContents.config(height=BaseY+SpanY*i)


def AddProduct():
    S.initWindow()
    S.BtnProductApply.config(command=S.AddProduct, text="登録")
    S.master.geometry("500x600")
    S.master.deiconify()
    S.FrmProduct.place(y=0, x=0, width=500, height=600)
    S.master.grab_set()
    S.master.focus_set()
    S.master.transient(FrmSetProduct)
    master.wait_window(S.temp)
    S.FrmProduct.place_forget()
    S.EntProductName.delete(0, tk.END)
    S.EntProductPrice.delete(0, tk.END)
    S.ProductIntax.set(False)
    S.ProductRedtax.set(False)
    RefreshTable()
    S.master.grab_release()

def EditProduct(event):
    print("OPEN EDIT PRODUCT")
    S.initWindow()
    S.BtnProductApply.config(command=lambda:S.EditProduct(), text="更新")
    S.master.geometry("500x600")
    S.master.deiconify()
    S.FrmProduct.place(y=0, x=0, width=500, height=600)
    S.master.grab_set()
    S.master.focus_set()
    S.master.transient(FrmSetProduct)
    master.wait_window(S.temp)
    S.FrmProduct.place_forget()
    S.EntProductName.delete(0, tk.END)
    S.EntProductPrice.delete(0, tk.END)
    S.ProductIntax.set(False)
    S.ProductRedtax.set(False)
    RefreshTable()
    S.master.grab_release()

BtnAddProduct = tk.Button(FrmSetProduct, text="商品追加", command=AddProduct, font=("", 35), bg="orange")
BtnAddProduct.place(y=500, x=1030)


BtnClose = tk.Button(FrmSetProduct, text="閉じる", command=CloseWindow, font=("", 35), bg="blue", fg="white")
BtnClose.place(y=700, x=1260, anchor="se")

master.protocol("WM_DELETE_WINDOW", CloseWindow)