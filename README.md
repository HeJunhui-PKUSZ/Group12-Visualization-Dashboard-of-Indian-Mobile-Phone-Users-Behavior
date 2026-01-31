
##  Visualization Dashboard of Indian Mobile Phone Users' Behavior

# 印度手机用户行为可视化大屏



## 📚 Project Introduction项目简介

This project mainly conducts behavioral analysis on Indian mobile phone users, performs visualization processing on mobile phone users' behavioral data (including age, gender, screen time, data usage, app usage, etc.), and selects users' consumption behaviors for k-means clustering.

本项目主要对印度手机用户进行行为分析，对手机用户行为数据，包括年龄、性别、屏幕时间、数据使用量、应用使用情况等数据做可视化处理，并选择用户的消费行为进行k-means聚类。


## 📁 Data Source数据来源

The original dataset used in this paper is from the public dataset on Kaggle, with a total of 17,686 records. The dataset includes 16 fields such as user gender, age, total daily mobile phone screen time, monthly consumption amount on e-commerce platforms, monthly mobile data usage, and total daily call duration. The names and meanings of each field are as follows:

本文采用的原始数据集来自kaggle公开的数据集共17686条，该数据集包括用户的性别、年龄、每天使用手机屏幕的总时间、每月在电子商务平台上的消费金额、每月使用的移动数据量以及每天通话的总时长等共16个字段，具体各字段名称及其含义如下

```
字段名	                       字段含义
User ID                    	   用户唯一标识符
Age	                           用户年龄
Gender	                       用户性别
Location	                   用户所在城市
Phone Brand	                   用户使用的手机品牌
OS	                           用户手机的操作系统
Screen Time (hrs/day)	       用户每天使用手机屏幕的总时间（小时）
Data Usage (GB/month)	       用户每月使用的移动数据量（GB）
Calls Duration (min/day)	   用户每天通话的总时长（分钟）
Number of Apps Installed	   用户手机上安装的应用程序数量
Social Media Time (hrs/day)	   用户每天在社交媒体上花费的时间（小时）
E-commerce Spend(INR/month)	   用户每月在电子商务平台上的消费金额（印度卢比）
Streaming Time (hrs/day)	   用户每天在流媒体平台（如视频、音乐）上花费的时间（小时）
Gaming Time (hrs/day)	       用户每天在手机游戏上花费的时间（小时）
Monthly Recharge Cost (INR)	   用户每月为手机充值或支付套餐费用的金额（印度卢比）
Primary Use	                   用户使用手机的主要用途
```


## 🎯  Research Objectives研究目标

Through the integration and dynamic analysis of multi-dimensional data on users' interaction with smartphones, this study aims to reveal the inherent logic of user behavior and provide a scientific basis for commercial innovation and social governance in the digital age.

本研究通过用户与智能手机交互多维度数据整合与动态分析，旨在揭示用户行为的内在逻辑，并为数字时代的商业创新与社会治理提供科学依据。


## 📁 Project Structure项目结构

```
keshihuapingtai/
├── src/                                    # 原代码
│   ├── app.py/                               # 进入可视化大屏网址
│   ├── ciyun.py/                             # 生成词云
│   └── data_processing.py/                   # 生成饼图、玫瑰图、热力图
│   └── k-means.py/                           # k-means聚类
│   └── map.py/                               # 生成地图
│   └── map1.py/                              # 生成地图html
├── static/                                   # 源代码
│   ├── css.py/                             # css文件
│       ├── style.css/
│       ├── app.css/
│   ├── data/                             # 源数据
│       ├── phone_india.csv            
│   ├── img                               # 生成的图片
│   └── favicon.ico                   # 网址的图表
│
├── templates/                               # html文件
│   ├── index.html/                      # 首页html
│
├── README.md/                                    # readme文件

```

## 🔧 Environment Configuration环境配置
```
pandas>=1.5.0
numpy>=1.23.0
matplotlib>=3.6.0
seaborn>=0.12.0
scikit-learn>=1.2.0
streamlit>=1.20.0
```

### Basic Dependency Version Requirements基础依赖版本要求
```
- Python 版本：3.8+
- `pandas`
- `numpy`
- `scipy`
- `matplotlib`
- `seaborn`
- `scikit-learn` 
- `geopandas` 
- `shapely` 
- `networkx` 
- `wordcloud` 
- `flask` 
- `KMeans` 
- `os` 
- `csv` 
- `KMeans` 
- `silhouette_score` 
- `StandardScaler` 
```

## 📁 Usage使用方法

### 1.Generate Various Analysis Charts
### 1.生成各类分析图

运行 `ciyun.py,data_processing.py,k-means.py,map.py,map1.py ` 脚本，生成各类数据分析图
运行以下脚本，生成对应的数据分析可视化图表：
Run the following scripts to generate corresponding data analysis and visualization charts:
```
python src/ciyun.py
python src/data_processing.py
python src/k-means.py
python src/map.py
python src/map1.py
```

### 2. Launch Visualization Dashboard
### 2. 启动可视化大屏

运行 `app.py` 脚本,进入可视化大屏网址
运行 app.py 脚本启动服务，访问输出的网址即可查看可视化大屏：
Run the app.py script to start the service, and access the output URL to view the visualization dashboard:
```
python src/app.py
```

## 💡 Future Work未来工作
- **选择更多字段进行数据分析 | Select more fields for data analysis**
- **选择更多的字段进行聚类 | Select more fields for clustering**
- **连接本地数据库 | Connect to local database**

## 👥 Team Members团队成员

```
-[何俊辉] (2501212913) | [He Junhui] (2501212913)
-[张骋旭] (2501212936) | [Zhang Chengxu] (2501212936)
-[陆胤] (2501212930)| [Lu Yin] (2501212930)
-[陈安杰] (2501112421)| [Chen Anjie] (2501112421)
```

