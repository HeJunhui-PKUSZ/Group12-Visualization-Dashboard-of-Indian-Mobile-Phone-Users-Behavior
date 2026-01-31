import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# =========================
# 1. 路径 & 参数配置
# =========================
data_path = r'D:\pythonproject\keshihuapingtai\static\data\phone_india.csv'
output_dir = r'D:\pythonproject\keshihuapingtai\static\img'
os.makedirs(output_dir, exist_ok=True)

elbow_path = os.path.join(output_dir, 'elbow_silhouette.png')
scatter_path = os.path.join(output_dir, 'cluster_scatter.png')
center_bar_path = os.path.join(output_dir, 'cluster_centers_bar.png')

features = [
    'E-commerce Spend (INR/month)',
    'Monthly Recharge Cost (INR)'
]

# =========================
# 2. 读取数据 & 标准化
# =========================
df = pd.read_csv(data_path)
X = df[features].dropna()

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# =========================
# 3. 肘部法 & 轮廓系数
# =========================
sse = []
silhouette_scores = []
K_range = range(2, 11)

for k in K_range:
    kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
    labels = kmeans.fit_predict(X_scaled)
    sse.append(kmeans.inertia_)
    silhouette_scores.append(silhouette_score(X_scaled, labels))

optimal_k = K_range[np.argmax(silhouette_scores)]
print(f'Optimal K: {optimal_k}')

# =========================
# 4. 肘部法 + 轮廓系数图
# =========================
fig, axes = plt.subplots(1, 2, figsize=(8, 4), facecolor='none')

axis_color = '#FF9900'
title_color = '#5AC8FA'

# ---- 肘部法 ----
axes[0].plot(K_range, sse, marker='o', linewidth=2.2, color='#4F7CAC')
axes[0].axvline(optimal_k, linestyle='--', color='#9E2A2B')

axes[0].set_title('Elbow Method', color=title_color, fontweight='bold')
axes[0].set_xlabel('Number of Clusters (K)', color=axis_color, fontweight='bold')
axes[0].set_ylabel('SSE', color=axis_color, fontweight='bold')

# ---- 轮廓系数 ----
axes[1].plot(K_range, silhouette_scores, marker='o', linewidth=2.2, color='#C18F59')
axes[1].axvline(optimal_k, linestyle='--', color='#9E2A2B')

axes[1].set_title('Silhouette Analysis', color=title_color, fontweight='bold')
axes[1].set_xlabel('Number of Clusters (K)', color=axis_color, fontweight='bold')
axes[1].set_ylabel('Silhouette Score', color=axis_color, fontweight='bold')

for ax in axes:
    ax.tick_params(colors=axis_color)
    for spine in ax.spines.values():
        spine.set_color(axis_color)
    ax.grid(alpha=0.25)
    ax.set_facecolor('none')

plt.tight_layout()
plt.savefig(elbow_path, dpi=300, transparent=True, bbox_inches='tight')
plt.close()

print(f'肘部法与轮廓系数图已保存：{elbow_path}')

# =========================
# 5. 最优 KMeans 聚类
# =========================
final_kmeans = KMeans(
    n_clusters=optimal_k,
    random_state=42,
    n_init=10
)

df.loc[X.index, 'Cluster_KMeans'] = final_kmeans.fit_predict(X_scaled)

# =========================
# 6. 聚类结果二维散点图
# =========================
fig, ax = plt.subplots(figsize=(8, 5), facecolor='none')

cluster_colors = [
    '#4F7CAC', '#C18F59', '#9E2A2B', '#5AC8FA', '#8E9AAF'
]

for cluster_id in range(optimal_k):
    data = df[df['Cluster_KMeans'] == cluster_id]
    ax.scatter(
        data[features[0]],
        data[features[1]],
        s=55,
        alpha=0.82,
        color=cluster_colors[cluster_id],
        edgecolors='white',
        linewidths=0.6,
        label=f'Cluster {cluster_id}'
    )

ax.set_title('User Consumption Behavior Clustering',
             color=title_color, fontweight='bold')

ax.set_xlabel(features[0], color=axis_color, fontweight='bold')
ax.set_ylabel(features[1], color=axis_color, fontweight='bold')

ax.tick_params(colors=axis_color)
for spine in ax.spines.values():
    spine.set_color(axis_color)

legend = ax.legend(frameon=False)
for text in legend.get_texts():
    text.set_color('black')

ax.grid(alpha=0.2)
ax.set_facecolor('none')

plt.tight_layout()
plt.savefig(scatter_path, dpi=300, transparent=True, bbox_inches='tight')
plt.close()

print(f'聚类散点图已保存：{scatter_path}')

# =========================
# 7. ⭐ 聚类中心柱状图（横坐标 = Cluster）
# =========================
centers_scaled = final_kmeans.cluster_centers_
centers = scaler.inverse_transform(centers_scaled)

centers_df = pd.DataFrame(
    centers,
    columns=features,
    index=[f'Cluster {i}' for i in range(optimal_k)]
)

fig, ax = plt.subplots(figsize=(8, 5), facecolor='none')

x = np.arange(optimal_k)
bar_width = 0.35

ax.bar(
    x - bar_width / 2,
    centers_df[features[0]],
    width=bar_width,
    color='#4F7CAC',
    label='E-commerce Spend'
)

ax.bar(
    x + bar_width / 2,
    centers_df[features[1]],
    width=bar_width,
    color='#C18F59',
    label='Monthly Recharge Cost'
)

ax.set_xticks(x)
ax.set_xticklabels(centers_df.index, color='#FF6600')

ax.set_ylabel('Average Value (INR)', fontweight='bold', color='#FF6600')
ax.set_title('Comparison of Cluster Centers',
             fontweight='bold', color=title_color)
ax.tick_params(axis='x', colors=axis_color, labelsize=11)
ax.tick_params(axis='y', colors=axis_color, labelsize=11)
legend = ax.legend(frameon=False)
for text in legend.get_texts():
    text.set_color('#FF0000')

ax.grid(axis='y', alpha=0.25)
ax.set_facecolor('none')

plt.tight_layout()
plt.savefig(center_bar_path, dpi=300, transparent=True, bbox_inches='tight')
plt.close()

print(f'聚类中心柱状图已保存：{center_bar_path}')
