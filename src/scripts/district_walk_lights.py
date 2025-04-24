import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.colors as colors

# 데이터 불러오기
df = pd.read_csv("../docs/wedo.csv", encoding="cp949")
df_walk = df[df['신호등종류'] == '보행등']

# 자치구별 보행등 개수 집계
walk_counts = df_walk['자치구'].value_counts().reset_index()
walk_counts.columns = ['자치구', '보행등 개수']
walk_counts = walk_counts.sort_values(by='보행등 개수', ascending=False).reset_index(drop=True)

# 색상 매핑
norm = colors.Normalize(vmin=walk_counts["보행등 개수"].min(), vmax=walk_counts["보행등 개수"].max())
colormap = cm.ScalarMappable(norm=norm, cmap="YlOrRd")
colors_list = [colors.to_hex(colormap.to_rgba(val)) for val in walk_counts["보행등 개수"]]

# 시각화
plt.figure(figsize=(12, 6))
plt.bar(walk_counts["자치구"], walk_counts["보행등 개수"], color=colors_list)
plt.xticks(rotation=90)
plt.xlabel("자치구")
plt.ylabel("보행등 개수")
plt.title("서울시 자치구별 보행등 개수")
plt.tight_layout()
plt.savefig("../results/seoul_walk_light_by_district.png", dpi=300)
plt.show()

