import matplotlib.pyplot as plt
import numpy as np

# データの生成
x = np.linspace(-5, 5, 100)
y1 = np.sin(x)
y2 = np.sin(2 * x)

# プロットの作成
plt.figure(figsize=(6, 4))
plt.plot(x, y1, label="Sin(x)", color="lightblue")
plt.plot(x, y2, label="Sin(2x)", color="lightgreen")

# グラフの設定
plt.title("Sine Wave Plot")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True, axis="x")
plt.legend(loc="upper right")

# グラフの表示
plt.show()
#githubに連携します
#git
#コミット2回目
#コミット3回目