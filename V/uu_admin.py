from M.util_db import DbMaker
from M.Models import Uu_admin
from V.handler import gen_password
from sqlalchemy import and_
import time

class Uuadmin():
    def __init__(self):
        self.session = DbMaker('admin').build()

    def register(self, uname, appid, phone):
        # code = self.create_db(appid)
        # if code is '300':
        #     return code
        return self.register_uuadmin(uname, appid, phone)        

    def register_uuadmin(self, uname, appid, phone):
        uuid = str(time.time())
        password = gen_password(10)
        sql_select = 'select * from uu_admin where appid="%s";'%appid
        sql_insert = 'insert into uu_admin(uuid, uname, phone, appid, password) values("%s", "%s", "%s", "%s", "%s")'%(uuid, uname, phone, appid, password)
        try:
            check = self.session.execute(sql_select)
            if check.fetchone() is None:
                self.create_db(appid)
                self.session.execute(sql_insert)
                self.session.commit()
            else:
                return '300'
        except Exception as e:
            return '500'
        return {'uname':uname, 'password':password, 'phone':phone, 'appid':appid}

    def create_db(self,appid):
        try:
            sql = 'create database %s;'%appid
            self.session.execute(sql)
        except Exception as e:
            return '300'
        return '200'

    def find_account(self, appid, pwd):
        user = self.session.query(Uu_admin).filter(and_(Uu_admin.password == pwd, Uu_admin.appid == appid)).first()
        if user is not None:
            from flask import session 
            session['super_user'] = user.super_user
        return False if user is None else True

    def find_account_by_session(self):
        from flask import session
        if session.get('appid') is None or session.get('password') is None:
            return False
        pwd = session.get('password')
        appid = session.get('appid')
        user = self.session.query(Uu_admin).filter(and_(Uu_admin.password == pwd, Uu_admin.appid == appid)).first()
        return False if user is None else True

    def change_password(self, appid, old, new):
        user = self.session.query(Uu_admin).filter(Uu_admin.appid == appid).first()
        if user is None or user.password!=old:
            return {'result': "incorrect information"}
        user.password = new
        try:
            self.session.commit() 
        except Exception as e:
            return {'result':"database error!"}
        return {"password":new, "result": "success"}


    def __del__(self):
        if self.session is not None:
            self.session.close()