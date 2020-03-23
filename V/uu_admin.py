from M.util_db import DbMaker
from M.Models import Uu_admin
from V.handler import gen_password
from sqlalchemy import and_
import time

class Uuadmin():
    def __init__(self):
        self.session = DbMaker('admin').build()

    def register(self, uname, appid, phone):
        return self.register_uuadmin(uname, appid, phone)        

    def register_uuadmin(self, uname, appid, phone):
        uuid = str(time.time())
        password = gen_password(10)
        # whether this appid already exists
        sql_select = 'select * from uu_admin where appid="%s";'%appid
        sql_insert = 'insert into uu_admin(uuid, uname, phone, appid, password) values("%s", "%s", "%s", "%s", "%s")'%(uuid, uname, phone, appid, password)
        create_table_sql = ''' create table `%s.bu_overview`(
            id int(4) primary key,
            appid varchar(100) not null,
            user_num int(4) not null default 0,
            visit_num int(4) not null default 0,
            ds varchar(50) not null,
            create_at datetime default current_timestamp
        )'''%appid 
        try:
            check = self.session.execute(sql_select)
            # create database and essential tables in admin
            if check.fetchone() is None:
                self.create_db(appid)
                self.session.execute(sql_insert)
                self.session.execute(create_table_sql)
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