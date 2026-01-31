import pandas as pd
import matplotlib.pyplot as plt
import os

# ===============================
# 0️⃣ 输出目录
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

# 合并城市坐标和流量
city_coords = pd.DataFrame([
    {'City': city, 'Lat': lat, 'Lon': lon, 'Avg_Data_Usage_GB': city_data_usage.get(city, 0)}
    for city, (lat, lon) in cities.items()
])

# ===============================
# 4️⃣ 绘制地图
# ===============================
plt.figure(figsize=(12, 10))
scatter = plt.scatter(
    city_coords['Lon'],
    city_coords['Lat'],
    s=city_coords['Avg_Data_Usage_GB']*20,  # 点大小，可调
    c=city_coords['Avg_Data_Usage_GB'],     # 颜色
    cmap='Reds',
    alpha=0.8,
    edgecolors='black'
)

for i, row in city_coords.iterrows():
    plt.text(row['Lon']+0.2, row['Lat']+0.2, f"{row['City']}\n{row['Avg_Data_Usage_GB']:.1f} GB",
             fontsize=10, fontweight='bold')

plt.colorbar(scatter, label='Average Data Usage (GB/month)')
plt.title("India City Monthly Data Usage", fontsize=22, color="#5ac8fa", fontweight='bold')
plt.xlabel("Longitude", fontsize=16, fontweight='bold')
plt.ylabel("Latitude", fontsize=16, fontweight='bold')
plt.grid(True, linestyle='--', alpha=0.5)

# 保存
map_path = os.path.join(output_dir, 'india_city_data_usage_map.png')
plt.savefig(map_path, dpi=300, transparent=True, bbox_inches='tight')
plt.show()

print("✅ 城市流量地图生成成功：", map_path)
