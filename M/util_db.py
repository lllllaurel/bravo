from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DbMaker():

    def __init__(self, db_name):
        #在此登录的是root, 冒号后面为密码，按需修改，MySQL默认端口是3306。并填上创建的数据库名如youcaihua
        URI = 'mysql://root:1234@127.0.0.1:3306/%s?charset=utf8'%db_name
        # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
        #查询时会显示原始SQL语句
        engine = create_engine(URI) #绑定数据库
        DBSession = sessionmaker(bind=engine)
        self.db_session = DBSession()

    def build(self):
        return self.db_session


    def __del__(self):
        self.db_session.close()