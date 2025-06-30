项目名称：淘宝女装商品采集与入库

简介：
本项目基于 DrissionPage 实现淘宝女装商品的自动化采集、数据清洗，并将结果存入 MySQL 数据库。适用于电商数据分析、商品信息收集等场景。

项目结构：
- main.py         主程序，负责页面采集、数据清洗与入库
- db.py           数据库操作模块，负责数据写入
- clean.py        数据清洗模块，去重、去空值
- requirements.txt 依赖库列表
- README.md       简体中文和英文简要说明
- __pycache__/    Python 编译缓存文件夹

依赖环境：
- Python 3.8+
- drissionpage
- pymysql
- pandas
（详见 requirements.txt）

数据库准备：
1. 确保本地 MySQL 已安装并启动。
2. 创建数据库和数据表，示例 SQL：
   CREATE DATABASE taobao_fashion DEFAULT CHARSET utf8mb4;
   USE taobao_fashion;
   CREATE TABLE taobao_fashion (
       id INT AUTO_INCREMENT PRIMARY KEY,
       name VARCHAR(255),
       price FLOAT,
       brand VARCHAR(255),
       sales VARCHAR(255),
       shop VARCHAR(255),
       url VARCHAR(512)
   );

3. 修改 db.py 中数据库连接配置（如有需要）。

使用方法：
1. 安装依赖：
   pip install -r requirements.txt

2. 运行主程序：
   python main.py

3. 可在 main.py 中修改采集关键词和页数：
   main(keyword='女装', max_pages=3)

功能说明：
- 自动打开淘宝搜索页，采集商品名称、价格、图片、店铺、销量、链接等信息。
- 数据清洗去重、去空值后写入 MySQL。
- 控制台输出采集与入库进度。

注意事项：
- 采集淘宝数据需科学上网，且请遵守相关网站的爬虫政策。
- DrissionPage 需正确配置 Chromium 浏览器环境。

如有问题请提交 issue 或联系作者。
