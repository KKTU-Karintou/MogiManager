# テンプレートなのでコピーして使うこと
# これ単体でフレームの画面配置が可能
# 完成したらコードをコピーすることで簡単に移植できる
# 各種パラメータは適宜変更すること

# 必要があれば追加でインポートすること
from errno import EINTR



G.root.title("模擬店マネージャー ver.1.0.0a")
G.root.geometry(WIN_SIZE)
G.root.maxsize(width=WIN_W, height=WIN_H)

# グリッドを使うには G.refer クラスの DrawGrid メソッドを使ってください
# 配置が終わったら置換機能で インスタンス名.CvArea を 各フレーム名に設定してください
# 赤は200px, 濃いグレーは100px, 薄いグレーが20px

# FrmNewFrame は適切に変更すること

# ここ以降に書く

# ここまで
G.root.mainloop()
