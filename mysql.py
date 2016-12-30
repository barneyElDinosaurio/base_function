__author__ = 'xda'
import MySQLdb,sqlite3
import pandas as pd
def DB_Usage():
    db=MySQLdb.connect("localhost","root","123456z","first_lesson")
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

DB_Usage()
#DB_Usage_sqlite()