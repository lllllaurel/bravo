from flask import Flask, render_template, request, jsonify, session, redirect
from V.data import ShowData
import V.handler as Handler
from V.uu_admin import Uuadmin
import datetime, os

app = Flask(__name__)
app.config['SECRET_KEY']=os.urandom(24)

# login
@app.route('/login', methods=['GET', 'POST'])
def navi_login():
    appid = request.form.get('appid')
    password = request.form.get('password')
    checked = request.form.get('remember')
    
    db = Uuadmin()
    if db.find_account_by_session():
        return redirect('/')
    if db.find_account(appid, password):
        session.permanent = True
        if checked == 'on':
            app.permanent_session_lifetime = datetime.timedelta(days=7)
        else:
            app.permanent_session_lifetime = datetime.timedelta(minutes=30)
        session['appid'] = appid 
        session['password'] = password
        return redirect('/')
    else:
        return render_template('login.html', incorrect = True)

@app.route('/login/changepassword')
def change_password():
    old = request.args.get('old')
    new = request.args.get('new')
    appid = request.args.get('appid')
    admin = Uuadmin()
    result = admin.change_password(appid, old, new)
    del admin 
    return jsonify(result)

# data preview
@app.route('/')
def navi_global():
    if not Handler.is_logged():
        return render_template('login.html')
    appid = session.get('appid')
    tb = '`'+appid+'.bu_overview`'
    ds = datetime.datetime.now().strftime("%Y%m%d")
    data = ShowData()
    visitors, visitors7, visitors30, visitors365, users, visistors_total, data_total = data.list_info(tb, ds)
    del data
    return render_template('homepage.html', visitors=visitors, visitors7=visitors7, visitors30=visitors30, visitors365=visitors365, usernum=users, visistors_total=visistors_total, data_total=data_total)

# log out
@app.route('/logout')
def logout():
    if session.get('appid') is not None:
        session.pop('appid')
    if session.get('password') is not None:
        session.pop('password')
    return render_template('login.html')

# data detail
@app.route('/data')
def navi_data():
    if not Handler.is_logged():
        return render_template('login.html')

    appid = session.get('appid')
    tablename = request.args.get('table')
    limit = request.args.get('limit')
    limit = [0,10] if limit is None else limit.split('-')
    keyword = request.args.get('keyword')

    data = ShowData()
    comments, tables = data.list_tables(appid)
    if len(tables) is 0 or len(comments) is 0:
        del data
        return render_template('database.html', tables=[], comments=[], tablelen=0, thiscomment='no data', thisname='none', columns=[], details=[], height=0, wide=0)
    tablename=tables[0] if (tablename is None) else tablename
    tablecomment = Handler.find_comm_by_tb(tables, comments, tablename)
    columns = data.list_columns('admin', tablename)
    details = data.data_detail(tablename, limit, Handler.reformat_keyword(keyword))
    details.reverse()
    height = min((int(limit[1])-int(limit[0])), len(details))
    del data
    return render_template('database.html', tables=tables, comments=comments, tablelen=len(tables), thiscomment=tablecomment, thisname=tablename, columns=columns, details=details, height=len(details), wide=len(columns))

@app.route('/overview')
def overview():
    appid = session.get('appid')
    tb = '`'+appid+'.bu_overview`'
    sevenDaysAgo = (datetime.datetime.now() - datetime.timedelta(days = 7))
    ds = sevenDaysAgo.strftime("%Y%m%d")
    data = ShowData()
    users, visits = data.fetch_overview(tb, ds)
    del data
    r = {}
    r['users'] = users 
    r['visits'] = visits
    return jsonify(r)

# register new application
@app.route('/register')
def register():
    if not Handler.is_logged():
        return render_template('login.html')
    return render_template('register.html')
@app.route('/register/appid')
def register_appid():
    uname = request.args.get('uname')
    appid = request.args.get('appid')
    phone = request.args.get('phone')
    ua = Uuadmin()
    result = ua.register(uname, appid, phone)
    del ua
    return jsonify(result)

# test
@app.route('/test')
def test():
    from V.handler import gen_password
    return gen_password(8)

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=3000, debug=True, threaded=True)