from M.util_db import DbMaker
from M.Models import Uu_tables

class ShowData():

    def __init__(self):
        self.session = DbMaker('admin').build()

    def list_tables(self, appid):
        o = self.session.query(Uu_tables).filter(Uu_tables.appid==appid).all()
        comments = [item.tablecomment for item in o]
        names = [item.tablename for item in o]
        return comments, names

    def list_columns(self, dbname, tablename):
        sql = "select column_name from information_schema.columns where table_schema='%s' and table_name='%s';"%(dbname, tablename)
        result = self.session.execute(sql)
        roxies = result.fetchall()
        return [r[0] for r in roxies]

    def data_detail(self, table_name, limit, keyword=None):
        limit1 = limit[0]
        limit2 = limit[1]
        try:
            if keyword is None:
                sql = 'select * from `%s` limit %s, %s;'%(table_name, limit1, limit2)
                exe = self.session.execute(sql)
            else: 
                sql = 'select * from `%s` where %s limit %s, %s;'%(table_name, keyword, limit1, limit2)
                exe = self.session.execute(sql)
        except Exception as e:
            return []
        result = exe.fetchall()
        if result is not None:
            result.reverse()
            return [resp for resp in result]
        return []

    def fetch_overview(self, tb, ds):
        sql = 'select user_num, visit_num from %s where ds>%s'%(tb, ds)
        exe = self.session.execute(sql)
        all = exe.fetchall()
        return [r[0] for r in all], [r[1] for r in all]