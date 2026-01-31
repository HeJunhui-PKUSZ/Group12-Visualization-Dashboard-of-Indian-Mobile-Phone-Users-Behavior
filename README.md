<img width="1674" height="960" alt="image" src="https://github.com/user-attachments/assets/54050ae5-cf77-4c3a-b5c1-1f13f90ee9f1" />

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
├── messages.csv/                       # 用户留言信息提交的csv文件
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
- `silhouette_score` 
- `StandardScaler` 
```

## 📁 Usage使用方法

### 1.Generate Various Analysis Charts生成各类分析图

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

### 2. Launch Visualization Dashboard启动可视化大屏

运行 `app.py` 脚本,进入可视化大屏网址
运行 app.py 脚本启动服务，访问输出的网址即可查看可视化大屏：
Run the app.py script to start the service, and access the output URL to view the visualization dashboard:
```
python src/app.py
```

## 🎯 Visualization Dashboard Introduction可视化展示

### 1.Dashboard Homepage大屏首页
<img width="1674" height="960" alt="image" src="https://github.com/user-attachments/assets/54050ae5-cf77-4c3a-b5c1-1f13f90ee9f1" />

### 2.Basic Operations基本操作

```
1.The dashboard mainly consists of seven parts: pie chart, dataset introduction, rose chart, message board, heatmap, k-means clustering, and word cloud. Among them, for the pie chart, rose chart, heatmap, and word cloud, clicking "More" allows you to enlarge and view the images as well as their result explanations; clicking the image enables full-screen viewing, and you can zoom in or out using the mouse wheel; clicking "Download" lets you save the images to your local device; clicking "Close" returns you to the dashboard. Examples are as follows:
1.大屏主要包含包括饼图、数据集介绍、玫瑰图、留言板、热力图、 k-means 聚类、词云七个部分，其中饼图、玫瑰图、热力图、词云图点击 More 可放大查看图片以及结果说明，点击图片可全屏查看图片通过鼠标滑轮可缩放图片，点击 Download 可下载图片至本地，点击 Close 回到大屏，例如下所示：
```
<img width="974" height="574" alt="image" src="https://github.com/user-attachments/assets/2f40caa8-be87-424e-aebd-bbb099ae177f" />
<img width="970" height="572" alt="image" src="https://github.com/user-attachments/assets/e2b77794-66ad-4749-8532-5321c692edcc" />

```
2.Regarding the dataset introduction section, it includes a data description, a dataset download function, and a button to navigate to the original dataset introduction. When you hover your mouse over "Download", it changes color; clicking it allows you to download the original dataset. Clicking "Go to source data" will navigate to the URL of the original dataset in a new page, as shown below:
2.对于数据集介绍部分，包含数据介绍部分，下载数据集，跳转到原始数据集介绍按钮，鼠标悬浮 Download 变色，点击可下载原始数据集，点击 Go to source data 可在新页面跳转到原始数据集的网址，如下所示：
```
<img width="930" height="516" alt="image" src="https://github.com/user-attachments/assets/6e6974d3-4064-4385-85a7-ab7aec32556a" />
<img width="960" height="560" alt="image" src="https://github.com/user-attachments/assets/a76bf593-41e0-4976-99b5-5eb4e3a4ee50" />

```
3.Regarding the message board section, it includes a message input box and a message submission button. When you hover your mouse over "Contact Us", its color changes; clicking it will bring up a pop-up displaying contact information. After entering your message and clicking "Submit", a pop-up will ask if you are willing to provide personal information. You can choose to agree, submit directly, or continue editing:
If you agree: A pop-up will appear for you to fill in your personal information, including nickname, gender (selected via a drop-down box), email address, and contact phone number. Click "Submit" to send both your message and personal information.
If you disagree: Your message will be submitted directly.
If you choose "Continue Editing": You can keep modifying your message.
Examples are as follows:
3.对于留言板部分，包含留言输入框，留言提交按钮，鼠标悬浮 Contact Us 变色，点击弹窗显示联系方式，输入留言后点击submit 提交后弹窗询问是否愿意提供个人信息，用户可选择愿意，直接提交或者继续编辑，愿意则弹窗填写个人信息，包含昵称、下拉框选择性别、邮箱以及联系电话，点击 submit 提交留言以及个人信息，不愿意则直接提交留言，点击继续编辑可继续填写留言。如下所示：
```
<img width="1872" height="988" alt="image" src="https://github.com/user-attachments/assets/b9ea904c-3a42-4e22-9b10-0d7406e56e69" />

```
4.Regarding the K-means clustering section, clicking "More" allows you to view the aggregation curves generated by using two methods—the elbow method and silhouette coefficient—to assist in selecting the optimal number of clusters for this clustering analysis. When K=4, the slope of the error reduction curve tends to flatten, and the silhouette coefficient reaches its peak, indicating that the clustering effect is relatively optimal at this point. Therefore, the final number of clusters determined is 4. Scrolling the mouse wheel reveals the second graph, which is a two-dimensional scatter plot of the clustering results. It can be seen that each clustering result has clear boundaries, and the data points are relatively compact, indicating good clustering performance. Continuing to scroll the mouse wheel, the third graph shows the cluster centers of each cluster. All images can be viewed in full screen by clicking on them, zoomed in or out using the mouse wheel. When you hover the mouse over "Download", its color changes; clicking it allows you to download the image, and clicking "Close" closes the enlarged view, as shown below:
4.对于 K-means 聚类部分，点击 More，可查看本次聚类采用了肘部法与轮廓系数两种方法来辅助选择最优簇数所生成的聚合曲线图，当 K 为 4 时，误差下降曲线的斜率趋于平缓，且轮廓系数达到峰值，表明此时聚类效果较优 t。因此，最终确定的聚类簇数为4，滑动鼠标滑轮可看到第二个图为聚类结果的二维散点图，可以看出各聚类结果有明显的界限，同时数据之间也比较紧密，说明聚类效果较好，继续滑动鼠标滑轮，第三个图为各簇的聚类中心，所有图片均可通过点击全屏查看，通过鼠标滑轮可缩放，鼠标悬浮Download 均变色，点击可下载，点击 Close 关闭，如下所示：
```
<img width="1872" height="988" alt="image" src="https://github.com/user-attachments/assets/bb925c49-db1b-4732-b62f-33c7af2b6794" />

### 3. 网站可视化


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

