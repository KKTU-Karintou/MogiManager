# テンプレートなのでコピーして使うこと
# これ単体でフレームの画面配置が可能
# 完成したらコードをコピーすることで簡単に移植できる
# 各種パラメータは適宜変更すること

# 必要があれば追加でインポートすること
import tkinter as tk
import Global as G

WIN_W = 1920
WIN_H = 1080
TAB_W = 1000
TAB_H = 500

G.root.title("模擬店マネージャー ver.1.0.0a")
G.root.geometry('1920x1080')
G.root.maxsize(width=1920, height=1080)

        # グリッドを使うには G.refer クラスの DrawGrid メソッドを使ってください
        # 配置が終わったら置換機能で インスタンス名.CvArea を 各フレーム名に設定してください
        # 赤は200px, 濃いグレーは100px, 薄いグレーが20px

        # FrmNewFrame は適切に変更すること

FrmNewFrame = tk.Frame(G.root, width=WIN_W, height=WIN_H)
cv = G.refer()
cv.DrawGrid(FrmNewFrame, WIN_W, WIN_H)
FrmNewFrame.place(y=0, x=0)

# ここ以降に書く


# ここまで
G.root.mainloop()