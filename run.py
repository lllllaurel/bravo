from flask import Flask, render_template, request, jsonify
from V.data import ShowData
import V.handler as Handler
from V.uu_admin import Uuadmin
import datetime

app = Flask(__name__)

#登陆
@app.route('/login')
def navi_login():
    return render_template('login.html')

#数据总览
@app.route('/')
def navi_global():
    return render_template('homepage.html')

#数据详情
@app.route('/data')
def navi_data():
    appid = 'automata' #接收参数 appid
    tablename = request.args.get('table')
    limit = request.args.get('limit')
    limit = [0,10] if limit is None else limit.split('-')
    keyword = request.args.get('keyword')

    data = ShowData()
    comments, tables = data.list_tables(appid)
    tablename=tables[0] if (tablename is None) else tablename
    tablecomment = Handler.find_comm_by_tb(tables, comments, tablename)

    columns = data.list_columns('admin', tablename)
    details = data.data_detail(tablename, limit, Handler.reformat_keyword(keyword))
    details.reverse()
    height = min((int(limit[1])-int(limit[0])), len(details))
    return render_template('database.html', tables=tables, comments=comments, tablelen=len(tables), thiscomment=tablecomment, thisname=tablename, columns=columns, details=details, height=len(details), wide=len(columns))

@app.route('/overview')
def overview():
    appid = 'automata'
    tb = '`'+appid+'.bu_overview`'
    sevenDaysAgo = (datetime.datetime.now() - datetime.timedelta(days = 7))
    ds = sevenDaysAgo.strftime("%Y%m%d")
    users, visits = ShowData().fetch_overview(tb, ds)
    r = {}
    r['users'] = users 
    r['visits'] = visits
    return jsonify(r)

#注册新应用
@app.route('/register')
def register():
    return render_template('register.html')
@app.route('/register/appid')
def register_appid():
    uname = request.args.get('uname')
    appid = request.args.get('appid')
    phone = request.args.get('phone')
    ua = Uuadmin()
    return ua.register(uname, appid, phone)

#测试
@app.route('/test')
def test():
    data = ShowData()
    rows = data.list_columns('admin', 'uu_tables')  
    return ','.join([r[0] for r in rows])

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3000, debug=True, threaded=True)