#メインウィンドウ
from re import sub
import re
import tkinter as tk
import DAO_SQLite3 as dao
import datetime as dt
import Global as G
import Settings as S
import References as R
from decimal import Decimal, ROUND_HALF_UP


WIN_W = 1920
WIN_H = 1080
TAB_W = 1920
TAB_H = 880 

        # グリッドを使うには G.refer クラスの DrawGrid メソッドを使ってください
        # 配置が終わったら置換機能で インスタンス名.CvArea を 各フレーム名に設定してください
        # 赤は200px, 濃いグレーは100px, 薄いグレーが20px

### ベース画面      Main
#cv.CvArea => FrmMainWindow
FrmMainWindow = tk.Frame(G.root, width=WIN_W, height=WIN_H)
cv = G.refer()
cv.DrawGrid(FrmMainWindow, WIN_W, WIN_H)

LblOpenDate = tk.Label(cv.CvArea, textvariable=G.OpenDate, font=("", 28), bd=3, relief=tk.SOLID)
LblOpenDate.place(y=20, x=20, width=460, height=60)

LblNowTime = tk.Label(cv.CvArea, textvariable=G.NowTime, font=("", 55), bd=3, relief=tk.SOLID)
LblNowTime.place(y=20, x=WIN_W/2, anchor=tk.N, width=320, height=100)


LblOpenTime = tk.Label(cv.CvArea, textvariable=G.OpenTime, font=("", 25), bd=3, relief=tk.SOLID)
LblOpenTime.place(y=20, x=1160, width=320, height=45)
LblCloseTime = tk.Label(cv.CvArea, textvariable=G.CloseTime, font=("", 25), bd=3, relief=tk.SOLID)
LblCloseTime.place(y=75, x=1160, width=320, height=45)

### 注文タブ        Orders
# cv2.CvArea -> FrmOrderTab
FrmOrderTab = tk.Frame(cv.CvArea, width=TAB_W, height=TAB_H, bd=1, relief=tk.SOLID)
cv2 = G.refer()
cv2.DrawGrid(FrmOrderTab, TAB_W, TAB_H)
cv2.CvArea.config(bg="aqua")
FrmOrderTab.place(y=WIN_H, x=WIN_W, anchor="se")

FrmOrderHeafer = tk.Frame(cv2.CvArea, width=1000, height=60, bg="yellow green")
FrmOrderHeafer.place(y=20, x=20)

FrmOrderMenu = R.ScrollableFrame(cv2.CvArea, bar_x=False)
FrmOrderMenu.place(y=80, x=20, width=1000, height=640)

FrmMenus = FrmOrderMenu.scrollable_frame
FrmMenus.config(width=1000, bg="yellow green")

BaseX = 200
BaseY = 100
SpanY = 75
LblItemName = tk.Label(FrmOrderHeafer, text="商品名", font=("", 25))
LblItemName.place(y=30, x=BaseX, anchor="c")
LblItemPrice = tk.Label(FrmOrderHeafer, text="価格", font=("", 25))
LblItemPrice.place(y=30, x=BaseX+300, anchor="c")
LblItemCount = tk.Label(FrmOrderHeafer, text="数量", font=("", 25))
LblItemCount.place(y=30, x=BaseX+500, anchor="c")
LblItemStock = tk.Label(FrmOrderHeafer, text="在庫数", font=("", 25))
LblItemStock.place(y=30, x=BaseX+680, anchor="c")

BaseY2 = 10
BaseX2 = 1800
SpanY2 = 100
Font = ("", 30)
Subtotal = tk.IntVar()
LblSubtotal = tk.Label(cv2.CvArea, text="小計                      円", font=Font, anchor="e")
LblSubtotal.place(y=BaseY2+SpanY2, x=BaseX2, anchor="e")
EntSubtotal = tk.Entry(cv2.CvArea, textvariable=Subtotal, font=Font, state="readonly", justify=tk.RIGHT, bd=3)
EntSubtotal.place(y=BaseY2+SpanY2, x=BaseX2-70, anchor="e", width=200)
Intax = tk.IntVar()
LblIntax = tk.Label(cv2.CvArea, text="内税                      円", font=Font, anchor="e")
LblIntax.place(y=BaseY2+SpanY2*2, x=BaseX2, anchor="e")
EntIntax = tk.Entry(cv2.CvArea, textvariable=Intax, font=Font, state="readonly", justify=tk.RIGHT, bd=3)
EntIntax.place(y=BaseY2+SpanY2*2, x=BaseX2-70, anchor="e", width=200)
Outtax = tk.IntVar()
LblOuttax = tk.Label(cv2.CvArea, text="外税                      円", font=Font, anchor="e")
LblOuttax.place(y=BaseY2+SpanY2*3, x=BaseX2, anchor="e")
EntOuttax = tk.Entry(cv2.CvArea, textvariable=Outtax, font=Font, state="readonly", justify=tk.RIGHT, bd=3)
EntOuttax.place(y=BaseY2+SpanY2*3, x=BaseX2-70, anchor="e", width=200)
Total = tk.IntVar()
LblTotal = tk.Label(cv2.CvArea, text="合計                      円", font=Font, anchor="e")
LblTotal.place(y=BaseY2+SpanY2*4, x=BaseX2, anchor="e")
EntTotal = tk.Entry(cv2.CvArea, textvariable=Total, font=Font, state="readonly", justify=tk.RIGHT, bd=3)
EntTotal.place(y=BaseY2+SpanY2*4, x=BaseX2-70, anchor="e", width=200)
LblReceive = tk.Label(cv2.CvArea, text="お預かり                      円", font=Font, anchor="e")
LblReceive.place(y=BaseY2+SpanY2*5, x=BaseX2, anchor="e")
EntReceive = tk.Entry(cv2.CvArea, font=Font, justify=tk.RIGHT, bd=3, bg="yellow")
EntReceive.place(y=BaseY2+SpanY2*5, x=BaseX2-70, anchor="e", width=200)
Change = tk.IntVar()
LblChange = tk.Label(cv2.CvArea, text="おつり                      円", font=Font, anchor="e")
LblChange.place(y=BaseY2+SpanY2*6, x=BaseX2, anchor="e")
EntChange = tk.Entry(cv2.CvArea, textvariable=Change, font=Font, state="readonly", justify=tk.RIGHT, bd=3)
EntChange.place(y=BaseY2+SpanY2*6, x=BaseX2-70, anchor="e", width=200)

BtnClearOrder = tk.Button(cv2.CvArea, text="注文一括クリア", font=("", 35))
BtnClearOrder.place(y=740, x=50, width=350, height=100)


# タブ切り替え
def OrderTab():
    TabButtonChange(0)
    FrmOrderTab.lift()


### 整理券タブ      Reference Numbers
FrmRefNumTab = tk.Frame(cv.CvArea, width=TAB_W, height=TAB_H)
FrmRefNumTab.place(y=WIN_H, x=WIN_W, anchor="se")

LblTitleRefNum = tk.Label(FrmRefNumTab, text="整理券タブ", font=("", 45))
LblTitleRefNum.place(y=0, x=0)


def RefNumTab():
    TabButtonChange(1)
    FrmRefNumTab.lift()

### 在庫タブ        Stocks
FrmStockTab = tk.Frame(cv.CvArea, width=TAB_W, height=TAB_H)
FrmStockTab.place(y=WIN_H, x=WIN_W, anchor="se")

LblTitleStock = tk.Label(FrmStockTab, text="在庫タブ", font=("", 45))
LblTitleStock.place(y=0, x=0)

def StockTab():
    TabButtonChange(2)
    FrmStockTab.lift()

### 注文履歴タブ    Past Orders
FrmPastOrderTab = tk.Frame(cv.CvArea, width=TAB_W, height=TAB_H)

FrmPastOrderTab.place(y=WIN_H, x=WIN_W, anchor="se")

LblTitlePastOrder = tk.Label(FrmPastOrderTab, text="注文履歴タブ", font=("", 45))
LblTitlePastOrder.place(y=0, x=0)

def PastOrderTab():
    TabButtonChange(3)
    FrmPastOrderTab.lift()

### タブ切り替えボタン
BtnTab = []
for i in range(4):
    Btn = tk.Button(cv.CvArea, bg="blue", font=("", 28), bd=3, relief=tk.SOLID)
    BtnTab.append(Btn)

_BaseY = 100
_BaseX = 40
BTN_W = 180
BTN_H = 100
BtnTab[0].config(text="注文受付", command=OrderTab)
BtnTab[0].place(y=_BaseY, x=_BaseX, width=BTN_W, height=BTN_H)
BtnTab[1].config(text="整理券", command=RefNumTab, bg="blue")
BtnTab[1].place(y=_BaseY, x=_BaseX+175, width=BTN_W, height=BTN_H)
BtnTab[2].config(text="在庫", command=StockTab, bg="blue")
BtnTab[2].place(y=_BaseY, x=_BaseX+350, width=BTN_W, height=BTN_H)
BtnTab[3].config(text="注文履歴", command=PastOrderTab)
BtnTab[3].place(y=_BaseY, x=_BaseX+525, width=BTN_W, height=BTN_H)

def TabButtonChange(this: int):
    for i in range(4):
        if(i==this):
            BtnTab[i].config(bg="white", fg="black", font=("", 30, "bold"))
        else:
            BtnTab[i].config(bg="blue", fg="white", font=("", 28, "normal"))


# 設定画面表示
def OpenSettings():
    S.initWindow()
    S.master.grab_set()
    S.master.focus_set()
    S.master.transient(G.root)
    S.master.deiconify()
    G.root.wait_window(S.temp)
    if(G.root!=None):
        S.master.grab_release()
    if(G.UpdateItemList):
        RefreshItems()
        G.UpdateItemList = False

BtnSettings = tk.Button(cv.CvArea, command=OpenSettings, text="🔑", font=("", 30), bg="orange", width=5, height=1)
BtnSettings.place(y=10, x=WIN_W-10, anchor="ne")

# 初期化
OrderTab()
TabButtonChange(0)

FrmContents = tk.Frame(FrmMenus, width=1000)
FrmContents.place(y=0, x=0)
data = []
def RefreshItems():
    global FrmContents, data

    FrmContents.destroy()
    FrmContents = tk.Frame(FrmMenus, width=1000, bg='orange')
    FrmContents.place(y=0, x=0)

    o = dao.Dao()
    data = list()
    items = o.FindAllItems()
    for i in range(len(items)):
        item = R.ItemSet(FrmContents)
        item.name.set(items[i].name)
        item.price.set(items[i].price)
        item.inTax = items[i].inTax
        item.redTax = items[i].reduceTax
        data.append(item)

    for i in range(len(data)):
        data[i].lbl_name.place(y=BaseY+SpanY*i-60, x=BaseX, anchor="c")
        data[i].lbl_price.place(y=BaseY+SpanY*i-60, x=BaseX+300, anchor="c")
        data[i].btn_countdown.place(y=BaseY+SpanY*i-60, x=BaseX+475, width=70, height=50, anchor="e")
        data[i].lbl_count.place(y=BaseY+SpanY*i-60, x=BaseX+500, anchor="c")
        data[i].btn_countup.place(y=BaseY+SpanY*i-60, x=BaseX+525, width=70, height=50, anchor="w")
        data[i].lbl_stock.place(y=BaseY+SpanY*i-60, x=BaseX+680, anchor="c")

        FrmMenus.config(height=BaseY+SpanY*i-20)
        FrmContents.config(height=BaseY+SpanY*i-20)

RefreshItems()

# commands
def ClearOrder():
    for i in range(len(data)):
        data[i].NoC.set(0)
    EntReceive.delete(0, tk.END)

# buttons
BtnClearOrder.config(command=ClearOrder)

### 関数
def clock():
    n = dt.datetime.now()
    t = n.strftime('%H時%M分')
    G.NowTime.set(t)

    FrmMainWindow.after(100, clock)

vcmd = (EntReceive.register(R.validation), "%s", "%P")
EntReceive.config(validate="key", vcmd=vcmd)

def total():
    subtotalSum = 0
    intaxSum = 0
    outtaxSum = 0
    totalSum = 0
    receive = EntReceive.get()
    received = 0
    if(len(receive)>0):
        received = int(receive)

    change = 0
    for d in data:
        count = d.NoC.get()
        s = d.price.get()
        i = 0
        o = 0
        if(d.inTax):
            if(d.redTax):
                i = s - s/(1+G.ReduceTax/100)
            else:
                i = s - s/(1+G.BaseTax/100)
            i = Decimal(str(i)).quantize(Decimal('0'), rounding=ROUND_HALF_UP)
        else:
            if(d.redTax):
                o = int(s*(G.ReduceTax/100))
            else:
                o = int(s*(G.BaseTax/100))
        subtotalSum += s * count
        intaxSum += i * count
        outtaxSum += o * count
        totalSum = subtotalSum + outtaxSum

    Subtotal.set(subtotalSum)
    Intax.set(intaxSum)
    Outtax.set(outtaxSum)
    Total.set(totalSum)
    change = received - totalSum
    Change.set(change)

    FrmMainWindow.after(250, total)