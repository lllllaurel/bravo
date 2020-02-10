# bravo 

中间件程序，现仅完成基本功能

目录结构

|- root

|--- M:数据库文件

|--- static/asserts:静态文件（js \css \ upload等）

|--- templates:html模版文件

|--- V:核心代码

|--- run.py:入口、路由分发


项目依赖
- Mysql数据库
- Flask框架
- sqlalchemy数据库管理包
 
>pip install Flask

>pip instal sqlalchemy

数据库 admin
- uu_admin
- uu_tables

启动方法：
1. 安装依赖
2. mysql建库（或根据我提供的sql文件备份）
3. 修改util_db.py ，URI中的用户名和密码根据本地配置的mysql用户名和密码进行修改，用于连接mysql
4. 运行项目根目录下的run.py文件（当前默认端口：3000）
5. 浏览器localhost:3000，即可打开项目

其它说明：
1. js\css 文件在basic.html中引用
2. static/asserts/js/main.js 为项目的主要js文件，可在此基础上修改，也可新增等，该文件已在basic.html中引用
3. static/asserts/css 下可添加css文件，在basic.html中引用即可生效
4. static/asserts/bak 文件下的admin.sql已插入测试数据，可直接备份到数据库里