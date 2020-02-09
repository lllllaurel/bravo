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
    
    def build(self):
        return db

class Uu_admin(db.Model):
    __tablename__ = 'uu_admin'
    id = db.Column(db.Integer,primary_key = True,autoincrement = True)
    appid = db.Column(db.String(50),nullable = False)
    uuid = db.Column(db.String(20),nullable = False)
    uname = db.Column(db.String(20),nullable = False)
    phone = db.Column(db.String(20),nullable = False)
    last_login = db.Column(db.String(20),nullable = True)
    super_user = db.Column(db.Integer, default = 0)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)
    password = db.Column(db.String(20),nullable = False)

    def build(self):
        return db