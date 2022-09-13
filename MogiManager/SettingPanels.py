import tkinter as tk
import tkinter.messagebox as msg
import DAO_SQLite3 as D
import DAO_VARIABLE as V

master = tk.Toplevel()
master.withdraw()

temp: tk.Label
def initWindow():
    global temp
    temp = tk.Label(master)

# 販売品目設定：商品追加/編集
FrmProduct = tk.Frame(master, width=500, height=600)

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

# commands
def AddProduct():
    dao = D.Dao()
    item = V.item()
    item.name = EntProductName.get()
    item.price = EntProductPrice.get()
    item.inTax = ProductIntax.get()
    item.reduceTax = ProductRedtax.get()
    item.stocks = "empty"

    dao.AddItem(item)
    msg.showinfo("", "登録しました")
    CloseWindow()

# system
def CloseWindow():
    global temp
    temp.destroy()
    master.withdraw()

BtnProductCancel.config(command=CloseWindow)
BtnProductApply.config(command=AddProduct)

master.protocol("WM_DELETE_WINDOW", CloseWindow)