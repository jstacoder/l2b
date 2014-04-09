import MySQLdb as dbapi
from login_utils import encrypt_password

def get_db_connection(host=None,user=None,pw=None,dbname=None):
    if host is None:
        host = '174.140.227.137'
    if user is None:
        user = 'user_data'
    if pw is None:
        pw = '14wp88'
    if dbname is None:
        dbname = 'user_data'
    conn = dbapi.connect(host,user,pw,dbname)
    return conn

def register_user(username,pw_1,pw_2,email=None):
    ''' must check input before using this function '''
    rtn = True
    db = get_db_connection()
    cur = db.cursor()
    if pw_1 != pw_2:
        rtn = False
    SQL = 'INSERT INTO `user_data` (`username`,`email`,`password`) VALUES ("{0}","{1}","{2}")'.format(username,encrypt_password(pw_1),email)
    return SQL
    cur.execute(SQL)
    cur.close()
    db.close()
    return rtn

def get_db_column(db,colName):
    cur = db.cursor()
    SQL = 'SELECT {0} FROM `user_data`'.format(colName)
    cur.execute(SQL)
    res = cur.fetchall()
    cur.close()
    db.close()
    return res

def check_username(name):
    db = get_db_connection()
    names = get_db_column(db,'username')
    return not name in names

def check_email(email):
    db = get_db_connection()
    emails = get_db_column(db,'email')
    return not email in emails

def get_id_from_user(db,user):
    cur = db.cursor()
    SQL = 'SELECT `id` FROM `user_data` WHERE `username` = {0}'.format(user)
    cur.execute(SQL)
    res = CUR.fetchone()

    
