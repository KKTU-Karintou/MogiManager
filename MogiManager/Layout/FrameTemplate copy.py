# テンプレートなのでコピーして使うこと
# これ単体でフレームの画面配置が可能
# 完成したらコードをコピーすることで簡単に移植できる
# 各種パラメータは適宜変更すること

# 必要があれば追加でインポートすること
import tkinter as tk
import Global as G

WIN_W = 1920
WIN_H = 1080
WIN_SIZE = "1920x1080"
TAB_W = 1300
TAB_H = 800
TAB_SIZE = "1300x800"

G.root.title("模擬店マネージャー ver.1.0.0a")
G.root.geometry(TAB_SIZE)
G.root.maxsize(width=TAB_W, height=TAB_H)

        # グリッドを使うには G.refer クラスの DrawGrid メソッドを使ってください
        # 配置が終わったら置換機能で インスタンス名.CvArea を 各フレーム名に設定してください
        # 赤は200px, 濃いグレーは100px, 薄いグレーが20px

        # FrmNewFrame は適切に変更すること

FrmOrder = tk.Frame(G.root, width=TAB_W, height=TAB_H)
cv = G.refer()
cv.DrawGrid(FrmOrder, TAB_W, TAB_H)
FrmOrder.place(y=0, x=0)

# ここ以降に書く


# ここまで
G.root.mainloop()