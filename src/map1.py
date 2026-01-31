import pandas as pd
import folium
import os

# ===============================
# 输出目录
# ===============================
output_dir = r'D:\pythonproject\keshihuapingtai\static\img'
os.makedirs(output_dir, exist_ok=True)

# ===============================
# 1️⃣ 读取数据
# ===============================
csv_path = r'D:\pythonproject\keshihuapingtai\static\data\phone_india.csv'
df = pd.read_csv(csv_path)

# ===============================
# 2️⃣ 城市坐标
# ===============================
cities = {
    'Mumbai': (19.0760, 72.8777),
    'Delhi': (28.7041, 77.1025),
    'Ahmedabad': (23.0225, 72.5714),
    'Pune': (18.5204, 73.8567),
    'Jaipur': (26.9124, 75.7873),
    'Lucknow': (26.8467, 80.9462),
    'Kolkata': (22.5726, 88.3639),
    'Bangalore': (12.9716, 77.5946),
    'Chennai': (13.0827, 80.2707),
    'Hyderabad': (17.3850, 78.4867)
}

# ===============================
# 3️⃣ 统计城市平均流量
# ===============================
city_data_usage = df.groupby('Location')['Data Usage (GB/month)'].mean()

# ===============================
# 4️⃣ 创建 folium 地图
# ===============================
# 设置初始地图中心在印度
india_map = folium.Map(location=[22.0, 79.0], zoom_start=5)

# 最大最小流量，用于比例尺
max_usage = city_data_usage.max()
min_usage = city_data_usage.min()

# 添加圆圈标记
# 添加圆圈标记
for city, (lat, lon) in cities.items():
    usage = city_data_usage.get(city, 0)

    # 基础半径
    base_radius = 5000 + (usage / max_usage) * 15000

    # 如果流量高于最大值的一半，红色圆圈再放大 1.5 倍
    if usage > max_usage * 0.5:
        radius = base_radius * 1.5
        color = 'red'
    else:
        radius = base_radius
        color = 'orange'

    folium.Circle(
        location=[lat, lon],
        radius=radius,
        color=color,
        fill=True,
        fill_opacity=0.6,
        popup=f"{city}<br>Average Data Usage: {usage:.1f} GB/month"
    ).add_to(india_map)

# ===============================
# 5️⃣ 保存地图
# ===============================
map_path = os.path.join(output_dir, 'india_city_data_usage_map.html')
india_map.save(map_path)

print("✅ 交互式城市流量地图生成成功：", map_path)
