from M.util_db import DbMaker
from M.Models import Uu_tables
import time

class Uuadmin():
    def __init__(self):
        self.session = DbMaker('admin').build()

    def register(self, uname, appid, phone):
        code = self.create_db(appid)
        if code is '300':
            return code
        return self.register_uuadmin(uname, appid, phone)        

    def register_uuadmin(self, uname, appid, phone):
        uuid = str(time.time())
        sql_select = 'select * from uu_admin where appid="%s";'%appid
        sql_insert = 'insert into uu_admin(uuid, uname, phone, appid) values("%s", "%s", "%s", "%s")'%(uuid, uname, phone, appid)
        try:
            check = self.session.execute(sql_select)
            if check.fetchone() is None:
                self.session.execute(sql_insert, {uuid:uuid, uname:uname, appid:appid, phone:phone})
                self.session.commit()
        except Exception as e:
            return '500'
        return '200'

    def create_db(self,appid):
        try:
            sql = 'create database %s;'%appid
            self.session.execute(sql)
        except Exception as e:
            return '300'
        return '200'

    def __del__(self):
        self.session.close()