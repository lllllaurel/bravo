from M.util_db import DbMaker
from M.Models import Uu_tables
import datetime
from datetime import timedelta

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
        limit1 = max(int(limit[0])-1, 0)
        limit2 = int(limit[1])-limit1
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

    def list_info(self, tb, ds):
        now = datetime.datetime.now()
        date7 = (datetime.datetime.now() - timedelta(days=now.weekday()))
        date30 = datetime.datetime(now.year, now.month, 1)
        date365 = datetime.datetime(now.year, 1, 1)
        ds = now.strftime("%Y%m%d")
        ds7 = date7.strftime("%Y%m%d")
        ds30 = date30.strftime("%Y%m%d")
        ds365 = date365.strftime("%Y%m%d")
        #this dat
        sql = 'select visit_num from %s where ds=%s'%(tb, ds)
        #this week
        sql7 = 'select sum(visit_num) from %s where ds>=%s'%(tb, ds7)
        #this month
        sql30 = 'select sum(visit_num) from %s where ds>=%s'%(tb, ds30)
        #this year
        sql365 = 'select sum(visit_num) from %s where ds>=%s'%(tb, ds365)
        #total num of visits
        sql_total = 'select sum(visit_num) from %s '% tb
        #total num of users
        sql_users = 'select user_num from %s where ds=%s'%(tb, ds)
        #data amount
        sql_data = 'select count(1) from %s' % tb
        v = self.session.execute(sql)
        v7 = self.session.execute(sql7)
        v30 = self.session.execute(sql30)
        v365 = self.session.execute(sql365)
        v_users = self.session.execute(sql_users)
        v_total = self.session.execute(sql_total)
        v_data = self.session.execute(sql_data)
        res = v.fetchone()
        res7 = v7.fetchone()
        res30 = v30.fetchone()
        res365 = v365.fetchone()
        res_users = v_users.fetchone()
        res_total = v_total.fetchone()
        res_data = v_data.fetchone()
        visitors = res[0] if res is not None else 0
        visitors7 = res7[0] if res7 is not None else 0
        visitors30 = res30[0] if res30 is not None else 0
        visitors365 = res365[0] if res365 is not None else 0
        users = res_users[0] if res_users is not None else 0
        visitors_total = res_total[0] if res_total is not None else 0
        data_total = res_data[0] if res_data is not None else 0
        return [visitors, visitors7, visitors30, visitors365, users, visitors_total, data_total]