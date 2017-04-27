#-*-coding=utf-8-*-
__author__ = 'xda'
import MySQLdb,sqlite3
import pandas as pd
from toolkit import Toolkit
def DB_Usage():
    db=MySQLdb.connect("localhost","root","xxxxx","first_lesson")
    cursor=db.cursor()
    cursor.execute("SELECT VERSION()")
    data=cursor.fetchone()
    print data
    #db.close()
    cmd='SELECT * from person;'
    df=pd.read_sql(cmd,db)
    print df
    db.close()


    db1=sqlite3.connect("df_sql3.db")
    data=[[1,2,3,4],[3,4,5,6],[54,234,23,222]]
    df1=pd.DataFrame(data)
    print df1
    df1.to_sql("data",db1)


def DB_Usage_sqlite():
    db=sqlite3.connect("db_sql_test.db")
    #cursor=db.cursor()
    #cursor.execute("SELECT VERSION()")
    #data=cursor.fetchone()
    #print data
    db.close()
    cmd='SELECT * from person;'
    df=pd.read_sql(cmd,db)
    print df

def Aliyun():
    conn = MySQLdb.connect(host = 'qdm225205669.my3w.com',  # 远程主机的ip地址，
                                            user = 'qdm225205669',   # MySQL用户名
                                            db = 'qdm225205669_db',   # database名
                                            passwd = '',   # 数据库密码
                                            port = 3306,  #数据库监听端口，默认3306
                                            charset = "utf8")  #指定utf8编码的连接
    cursor=conn.cursor()
    cursor.execute('SELECT VERSION()')
    data=cursor.fetchone()
    print data

#DB_Usage()
#DB_Usage_sqlite()
Aliyun()