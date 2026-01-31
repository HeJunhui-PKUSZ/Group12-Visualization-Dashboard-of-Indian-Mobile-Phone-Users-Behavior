import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import os

# 读取数据并计算总消费
df = pd.read_csv(r'D:\pythonproject\keshihuapingtai\static\data\phone_india.csv')
df['Total_Spend'] = df['E-commerce Spend (INR/month)'] + df['Monthly Recharge Cost (INR)']

# 划分高/普通消费用户
threshold = df['Total_Spend'].quantile(0.8)
high_df = df[df['Total_Spend'] >= threshold]
normal_df = df[df['Total_Spend'] < threshold]

# 统计词频
high_counts = high_df['Primary Use'].value_counts().to_dict()
normal_counts = normal_df['Primary Use'].value_counts().to_dict()

# 创建词云（都使用透明背景）
font_path = r'C:/Windows/Fonts/simhei.ttf'

# 增加词云高度到800
wc_high = WordCloud(
    width=800, height=800,  # 高度从600增加到800
    font_path=font_path,
    background_color=None,
    mode='RGBA'
).generate_from_frequencies(high_counts)

wc_normal = WordCloud(
    width=800, height=800,  # 高度从600增加到800
    font_path=font_path,
    background_color=None,
    mode='RGBA'
).generate_from_frequencies(normal_counts)

# 绘图（调整图形大小使图更高）
plt.figure(figsize=(16, 12))  # 高度从9增加到12，比例4:3

# 左图
plt.subplot(1, 2, 1)
plt.imshow(wc_high, interpolation='bilinear')
plt.axis('off')
plt.title('High-Spending Users', fontsize=36, pad=30, color='#5ac8fa', fontweight='bold')  # 增加pad

# 右图
plt.subplot(1, 2, 2)
plt.imshow(wc_normal, interpolation='bilinear')
plt.axis('off')
plt.title('Normal-Spending Users', fontsize=36, pad=30, color='#5ac8fa', fontweight='bold')  # 增加pad

# 在左右图中间添加虚线分隔线
plt.axvline(x=8, ymin=0.001, ymax=0.999, color='#5ac8fa',
            linestyle='--', linewidth=7, alpha=0.7)

# 调整子图间距，让图更高
plt.tight_layout(pad=3.0)  # 增加子图间距

# 保存
output_dir = r'D:\pythonproject\keshihuapingtai\static\img'
os.makedirs(output_dir, exist_ok=True)
save_path = os.path.join(output_dir, 'primary_use_wordcloud_high_vs_normal.png')

plt.savefig(save_path, dpi=300, bbox_inches='tight', transparent=True)
plt.show()

print('词云已生成：', save_path)