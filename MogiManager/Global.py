import tkinter as tk
import datetime as dt

# ルートウィンドウ
root = tk.Tk()

# グローバル変数
OpenDate = '2022年01月01日 (月)'
NowTime = '00時00分'

WakeupPASSWORD = ""
AdminPASSWORD = "ggrks"

# 汎用イベント処理
def CloseApp():
    root.destroy()



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