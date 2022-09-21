import tkinter as tk

# ルートウィンドウ
root = tk.Tk()
root.resizable(False, False)

# グローバル変数
OpenDateYear = '2022'
OpenDateStr = '2022_01_01'
OpenDate = tk.StringVar(value='2022年01月01日 (月)')
NowTime = tk.StringVar(value='00時00分')
OpenTime = tk.StringVar(value='営業開始 : 09時00分')
CloseTime = tk.StringVar(value='営業終了 : 16時00分')

ProductEditId = 0

# 状態フラグ
UpdateItemList = False

### システム設定用
#Password
MASTER_PASSWORD = "#MASTER"
WAKEUP_PASSWORD = ''
ADMIN_PASSWORD = ''

#Function : True / False
UseReferenceFunc = False
UseStockFunc = False
UseShowOrderFunc = False
UseShowInfoFunc = False

#Tax : %
BaseTax = int(10)
ReduceTax = int(8)

#ReferenceNumber
BEGIN_REFNUM = 1
LIMIT_REFNUM = 99
currentRefNum = 1

# 関数用クラス
class refer():
    def DrawGrid(self, frame, width: int, height: int):
        self.CvArea = tk.Canvas(frame, width=width, height=height)
        self.CvArea.place(x=0, y=0)

        for i in range(width):
            if i%40==0:
                self.CvArea.create_line(i*5, 0, i*5, height, width=2, fill="red")
            elif i%20==0:
                self.CvArea.create_line(i*5, 0, i*5, height, fill="gray")
            elif i%4==0:
                self.CvArea.create_line(i*5, 0, i*5, height, fill="light gray")

        for i in range(height):
            if i%40==0:
                self.CvArea.create_line(0, i*5, width, i*5, width=2, fill="red")
            elif i%20==0:
                self.CvArea.create_line(0, i*5, width, i*5, fill="gray")
            elif i%4==0:
                self.CvArea.create_line(0, i*5, width, i*5, fill="light gray")