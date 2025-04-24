import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.colors as colors

# 데이터 불러오기
df = pd.read_csv("../docs/gwangjin_stat.csv", encoding='cp949')

# 구분된 시각화를 위해 분리
df_walk = df[["구간", "평균조도(LX)", "보행등 개수"]].copy()
df_car = df[["구간", "평균조도(LX)", "차도등 개수"]].copy()

# 전체 시각화
fig, ax = plt.subplots(figsize=(14, 6))
norm = colors.Normalize(vmin=df["평균조도(LX)"].min(), vmax=df["평균조도(LX)"].max())
colormap = cm.ScalarMappable(norm=norm, cmap="YlOrRd")
walk_colors = [colors.to_hex(colormap.to_rgba(val)) for val in df_walk["평균조도(LX)"]]
car_colors = [colors.to_hex(colormap.to_rgba(val)) for val in df_car["평균조도(LX)"]]

ax.bar(df_walk["구간"], df_walk["보행등 개수"], color=walk_colors, label="보행등", alpha=0.7)
ax.bar([i + 0.25 for i in range(len(df_car))], df_car["차도등 개수"], color=car_colors, label="차도등", alpha=0.7)
ax.set_xticks([i + 0.125 for i in range(len(df))])
ax.set_xticklabels(df["구간"], rotation=90)
ax.set_xlabel("도로 구간")
ax.set_ylabel("등 개수")
ax.set_title("광진구 도로 구간별 보행등 / 차도등 개수 및 조도 시각화")
ax.legend()
plt.tight_layout()
plt.show()

# 조도 상하위 5개 구간 시각화
highlight_df = pd.concat([
    df.sort_values(by="평균조도(LX)", ascending=False).head(5),
    df.sort_values(by="평균조도(LX)", ascending=True).head(5)
])
highlight_df["color"] = highlight_df["평균조도(LX)"].apply(lambda val: colors.to_hex(colormap.to_rgba(val)))

fig, ax = plt.subplots(figsize=(12, 6))
bar_width = 0.4
x = range(len(highlight_df))

ax.bar(x, highlight_df["보행등 개수"], width=bar_width, label="보행등", color=highlight_df["color"], align='center')
ax.bar([i + bar_width for i in x], highlight_df["차도등 개수"], width=bar_width, label="차도등", color=highlight_df["color"], alpha=0.7)
ax.set_xticks([i + bar_width / 2 for i in x])
ax.set_xticklabels(highlight_df["구간"], rotation=90)
ax.set_ylabel("등 개수")
ax.set_title("조도 상위/하위 5개 도로 구간별 보행등 및 차도등 개수")
ax.legend()
plt.tight_layout()
plt.show()

