from flask import Flask, current_app
from flask_sqlalchemy import SQLAlchemy
import datetime

db = SQLAlchemy()

class Uu_tables(db.Model):
    __tablename__ = 'uu_tables' 
    id = db.Column(db.Integer,primary_key = True,autoincrement = True)
    appid = db.Column(db.String(100),nullable = False)
    tablename = db.Column(db.String(50),nullable = False)
    tablecomment = db.Column(db.String(50),nullable = False)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)

    #repr()方法显示一个可读字符串
    def __repr__(self):
        return 'Role:%s'% self.name

    def build(self):
        return db