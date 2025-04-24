import pandas as pd
import folium

# 데이터 불러오기
df_smart = pd.read_csv("../docs/smart_stat.csv", encoding="cp949")

# 서울특별시 → 광진구 필터링
seoul_df = df_smart[df_smart["시도명"] == "서울특별시"]
gwangjin_df = seoul_df[seoul_df["시군구명"] == "광진구"]

# 지도 중심 설정
map_center = [gwangjin_df["위도"].mean(), gwangjin_df["경도"].mean()]
gwangjin_map = folium.Map(location=map_center, zoom_start=14)

# 마커 추가
for _, row in gwangjin_df.iterrows():
    folium.CircleMarker(
        location=[row["위도"], row["경도"]],
        radius=4,
        color="blue",
        fill=True,
        fill_opacity=0.6,
        popup=row["소재지도로명주소"]
    ).add_to(gwangjin_map)

# 결과 지도 저장 또는 시각화
gwangjin_map.save("../results/gwangjin_smart_light_map.html")

