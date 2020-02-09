#根据表注释返回表名
def find_tb_by_comm(tb, comm, comment):
    if tb is None or comm is None or comment is None:
        raise Exception("[find_tb_by_comm]invalid table comment!")
    return tb[comm.index(comment)]
#根据表名返回表注释
def find_comm_by_tb(tb, comm, name):
    if tb is None or comm is None or name is None:
        raise Exception("[find_comm_by_tb]invalid table name!")
    return comm[tb.index(name)]

#重构参数
def reformat_keyword(keyword):
    if keyword is None:
        return None 
    keyword_split = keyword.split(':')
    return keyword_split[0]+'="%s"'%keyword_split[1]

#随机生成密码
def gen_password(bits):
    import random 
    r = []
    for i in range(bits):
        if i%2==0:
            r.append(random.choice('abcdefghijklmnopqrstuvwxyz'))
        else:
            r.append(random.choice('1234567890'))
    return ''.join(r)

#判断登陆状态
def is_logged():
    from V.uu_admin import Uuadmin
    db = Uuadmin()
    return db.find_account_by_session()