import tkinter as tk
import tkinter.messagebox as msg
import Global as G
import DAO_SQLite3 as D
import DAO_VARIABLE as V

# ベースウィンドウ準備
master = G.dialog3
master.resizable(False, False)
master.withdraw()

LblTest = tk.Label(master, text="見えないはず", font=("", 35))
LblTest.place(y=0, x=0)

# データベースアクセスオブジェクト
o = D.Dao()

# モーダルウィンドウ疑似実装
    ### 呼出元は対象としたウィジェットが destroy されたかどうかを見ている。
    ### destroy するとメモリごと消えるので、非表示に対応するため身代わりを用意する。
    ### グローバル変数の参照以外の操作は global を付けないとローカル変数として扱われる。
temp = None
def initWindow():
    global temp
    if(temp==None):
        temp = tk.Label(master)

def CloseWindow():
    global temp
    temp.destroy()
    temp = None
    master.withdraw()


    ### 販売品目設定：商品追加/編集/削除 ###
FrmProduct = tk.Frame(master, width=500, height=600, bg="yellow green")
FrmProduct.place(y=0, x=0)

LblProductTitle = tk.Label(FrmProduct, text="商品追加", font=("", 25))
LblProductTitle.place(y=20, x=250, anchor="c")

LblProductName = tk.Label(FrmProduct, text="商品名", font=("", 20))
LblProductName.place(y=50, x=30)
EntProductName = tk.Entry(FrmProduct, font=("", 20))
EntProductName.place(y=50, x=120)

LblProductPrice = tk.Label(FrmProduct, text="価格", font=("", 20))
LblProductPrice.place(y=100, x=30)
EntProductPrice = tk.Entry(FrmProduct, font=("", 20))
EntProductPrice.place(y=100, x=120)

ProductIntax = tk.BooleanVar(value=False)
LblProductIntax = tk.Label(FrmProduct, text="内税", font=("", 20))
LblProductIntax.place(y=150, x=30)
CbProductIntax = tk.Checkbutton(FrmProduct, variable=ProductIntax)
CbProductIntax.place(y=150, x=120)

ProductRedtax = tk.BooleanVar(value=False)
LblProductRedtax = tk.Label(FrmProduct, text="軽減税", font=("", 20))
LblProductRedtax.place(y=200, x=30)
CbProductRedtax = tk.Checkbutton(FrmProduct, variable=ProductRedtax)
CbProductRedtax.place(y=200, x=120, width=40, height=40)

BtnProductStock = tk.Button(FrmProduct, text="在庫連動設定", font=("", 25), bg="blue")
BtnProductStock.place(y=400, x=250, anchor="c")

BtnProductApply = tk.Button(FrmProduct, text="追加", font=("", 25), bg="blue")
BtnProductApply.place(y=500, x=400)
BtnProductCancel = tk.Button(FrmProduct, text="キャンセル", font=("", 25), bg="blue")
BtnProductCancel.place(y=500, x=200)
BtnProductDelete = tk.Button(FrmProduct, text="削除", font=("", 25), bg="blue")

# コールバック
def AddProduct():
    item = V.item()
    item.name = EntProductName.get()
    item.price = EntProductPrice.get()
    item.inTax = ProductIntax.get()
    item.reduceTax = ProductRedtax.get()
    item.stocks = "empty"

    o.AddItem(item)
    msg.showinfo("", "登録しました")
    G.UpdateItemList = True
    CloseWindow()

def ApplyProduct():
    item = V.item()
    item.id = G.ProductEditId
    item.name = EntProductName.get()
    item.price = EntProductPrice.get()
    item.inTax = ProductIntax.get()
    item.reduceTax = ProductRedtax.get()
    item.stocks = "empty"

    o.UpdateItem(item)
    G.UpdateItemList = True
    msg.showinfo("", "更新しました")
    CloseWindow()

def DeleteProduct():
    sel = msg.askokcancel("", "削除すると過去の売上データで詳細を確認できなくなります。\nよろしいですか？")
    if(sel):
        id = G.ProductEditId

        o.DeleteItem(id)
        G.UpdateItemList = True
        msg.showinfo("", "削除しました")
        CloseWindow()


# 各ボタンのコールバック設定
BtnProductCancel.config(command=CloseWindow)
BtnProductDelete.config(command=DeleteProduct)

# ×ボタンにコールバックを設定
master.protocol("WM_DELETE_WINDOW", CloseWindow)