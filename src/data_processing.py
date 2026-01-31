import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
import folium
import os

# ===============================
# 1️⃣ 读取数据
# ===============================
csv_path = r'D:\pythonproject\keshihuapingtai\static\data\phone_india.csv'
df = pd.read_csv(csv_path)

output_dir = r'D:\pythonproject\keshihuapingtai\static\img'
os.makedirs(output_dir, exist_ok=True)

# ===============================
# 2️⃣ 品牌市场份额饼图
# ===============================
brand_counts = df['Phone Brand'].value_counts()
brand_share = (brand_counts / len(df) * 100).round(2)

top_brands = brand_share.head(10)

plt.figure(figsize=(10, 8))
wedges, texts, autotexts = plt.pie(
    top_brands.values,
    labels=top_brands.index,
    autopct='%1.1f%%',
    startangle=140
)

for t in texts:
    t.set_color("#5ac8fa")
    t.set_fontsize(14)
    t.set_fontweight("bold")

for at in autotexts:
    at.set_color("black")
    at.set_fontsize(14)



pie_path = os.path.join(output_dir, 'shoujifene.png')
plt.savefig(pie_path, dpi=300, transparent=True, bbox_inches='tight')
plt.close()

# ===============================
# 3️⃣ 年龄分组
# ===============================
bins = [0, 20, 30, 40, 120]
labels = ['0-20', '21-30', '31-40', '41+']
df['Age_Group'] = pd.cut(df['Age'], bins=bins, labels=labels)

colors = [
    "#00eaff", "#5ac8fa", "#3498db",
    "#1abc9c", "#9b59b6", "#f1c40f"
]

# ===============================
# 4️⃣ 玫瑰图（2×2）
# ===============================
fig, axes = plt.subplots(
    2, 2,
    figsize=(18, 16),
    subplot_kw={'polar': True}
)

axes = axes.flatten()

for i, age_group in enumerate(labels):
    ax = axes[i]
    df_age = df[df['Age_Group'] == age_group]

    if df_age.empty:
        ax.axis("off")
        continue

    usage = df_age['Primary Use'].value_counts()
    percent = usage / usage.sum() * 100

    angles = np.linspace(0, 2 * np.pi, len(percent), endpoint=False)
    width = 2 * np.pi / len(percent)

    ax.bar(
        angles,
        percent.values,
        width=width,
        color=colors[:len(percent)],
        alpha=0.85
    )

    ax.set_theta_zero_location("N")
    ax.set_theta_direction(-1)
    ax.set_yticks([])
    ax.set_thetagrids(
        np.degrees(angles),
        percent.index,
        fontsize=26,
        color="#aeefff",
    fontweight = 'bold'
    )

    ax.set_title(
        f"{age_group} Age Group",
        fontsize=28,
        color="#5ac8fa",
        pad=20,
        fontweight='bold'
    )

    ax.grid(color="#1f3b6f", linestyle="--", alpha=0.6)
    ax.set_facecolor("none")

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
fig.patch.set_alpha(0)

rose_path = os.path.join(output_dir, 'rose_age_4_groups.png')
plt.savefig(rose_path, dpi=300, transparent=True, bbox_inches='tight')
plt.show()
csv_path = r'D:\pythonproject\keshihuapingtai\data\phone_india.csv'
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
    edgecolors='#5ac8fa'
)

for i, row in city_coords.iterrows():
    plt.text(row['Lon']+0.2, row['Lat']+0.2, f"{row['City']}\n{row['Avg_Data_Usage_GB']:.1f} GB",
             fontsize=16, fontweight='bold',color='#5ac8fa')

cbar = plt.colorbar(scatter, label='Average Data Usage (GB/month)',pad=0.08)
cbar.ax.yaxis.set_tick_params(color='#5ac8fa', labelcolor='#5ac8fa', labelsize=18)
cbar.outline.set_edgecolor('#5ac8fa')
cbar.set_label('Average Data Usage (GB/month)', color='#5ac8fa', fontsize=16, fontweight='bold')

plt.xlabel("Longitude", fontsize=22, fontweight='bold', color='#5ac8fa')
plt.ylabel("Latitude", fontsize=22, fontweight='bold',color='#5ac8fa')
plt.tick_params(axis='x', colors='#5ac8fa', labelsize=20)
plt.tick_params(axis='y', colors='#5ac8fa', labelsize=20)
plt.grid(True, linestyle='--', alpha=0.5)

# 保存
map_path = os.path.join(output_dir, 'india_city_data_usage_map.png')
plt.savefig(map_path, dpi=300, transparent=True, bbox_inches='tight')
plt.show()

print("✅ 城市流量地图生成成功：", map_path)
print("✅ 图表生成成功：")
print(pie_path)
print(rose_path)
