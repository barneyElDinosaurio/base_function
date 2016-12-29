__author__ = 'xda'
import MySQLdb
import pandas as pd
def DB_Usage():
    db=MySQLdb.connect("localhost","root","123456z","first_lesson")
    cursor=db.cursor()
    cursor.execute("SELECT VERSION()")
    data=cursor.fetchone()
    print data
    db.close()
    cmd='SELECT * from person;'
    df=pd.read_sql(cmd,db)
    print df

DB_Usage()