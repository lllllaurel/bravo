from flask import Flask
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config.conf import DatabaseConfig

app = Flask(__name__)
class DbMaker():

    def __init__(self, dbname = 'admin'):
        #在此登录的是root, 冒号后面为密码，按需修改，MySQL默认端口是3306。并填上创建的数据库名如youcaihua
        app.config.from_object(DatabaseConfig)
        URI = 'mysql://%s:%s@127.0.0.1:3306/%s?charset=utf8'%(app.config['USER'], app.config['PASSWORD'], dbname)
        # app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
        #查询时会显示原始SQL语句
        engine = create_engine(URI) #绑定数据库
        DBSession = sessionmaker(bind=engine)
        self.db_session = DBSession()

    def build(self):
        return self.db_session


    def __del__(self):
        self.db_session.close()