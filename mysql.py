# -*-coding=utf-8-*-
__author__ = 'xda'
import MySQLdb, sqlite3
import pandas as pd
from toolkit import Toolkit


def DB_Usage():
    db = MySQLdb.connect("localhost", "root", "xxxxx", "first_lesson")
    cursor = db.cursor()
    cursor.execute("SELECT VERSION()")
    data = cursor.fetchone()
    print data
    #db.close()
    cmd = 'SELECT * from person;'
    df = pd.read_sql(cmd, db)
    print df
    db.close()

    db1 = sqlite3.connect("df_sql3.db")
    data = [[1, 2, 3, 4], [3, 4, 5, 6], [54, 234, 23, 222]]
    df1 = pd.DataFrame(data)
    print df1
    df1.to_sql("data", db1)


def DB_Usage_sqlite():
    db = sqlite3.connect("db_sql_test.db")
    #cursor=db.cursor()
    #cursor.execute("SELECT VERSION()")
    #data=cursor.fetchone()
    #print data
    db.close()
    cmd = 'SELECT * from person;'
    df = pd.read_sql(cmd, db)
    print df


def Aliyun():
    passwd = Toolkit.getUserData('data.cfg')['alipasswd']
    print passwd
    conn = MySQLdb.connect(host='bdm273219298.my3w.com',  # 远程主机的ip地址，
                           user='bdm273219298',  # MySQL用户名
                           db='bdm273219298_db',  # database名
                           passwd=passwd,  # 数据库密码
                           port=3306,  #数据库监听端口，默认3306
                           charset="utf8")  #指定utf8编码的连接
    cursor = conn.cursor()
    cursor.execute('SELECT VERSION()')
    data = cursor.fetchone()
    print data
    #已经连通了，可以开搞。
    id = 31
    cmd1 = "insert into `aws_user_action_history_data`(`history_id`,`associate_content`,`associate_attached`,`addon_data`) values ('%d','huati','',''),('%d','','',''),('%d','Rocky-Title','ROCK-Content','')" % (
    id, id + 1, id + 2)
    cursor.execute(cmd1)
    #conn.commit()
    topic_id = 7
    title = "Hello" + str(topic_id)
    cmd2 = "insert into `aws_topic`(`topic_id`,`topic_title`,`add_time`,`discuss_count`,`topic_description`,`topic_pic`,`topic_lock`,`focus_count`,`user_related`,`url_token`,`merged_id`,`seo_title`,`parent_id`,`is_parent`,`discuss_count_last_week`,`discuss_count_last_month`,`discuss_count_update`) values('%d','huati5','1493370061','1','',null,'0','1','0',null,'0',null,'0','0','1','1','1493370061')" % topic_id
    cursor.execute(cmd2)
    #cursor.commit()
    arti_id = 5
    cmd3 = "insert into `aws_article`(`id`,`uid`,`title`,`message`,`comments`,`views`,`add_time`,`has_attach`,`lock`,`votes`,`title_fulltext`,`category_id`,`is_recommend`,`chapter_id`,`sort`) values('%d','1','ddThe Rocky23 IC ************TITLE','dddThe Rocky IC Content !!!!!!!!','0','1','1493370061','0','0','0','ic title','1','0',null,'0')" % arti_id
    cursor.execute(cmd3)
    #cursor.commit()
    cmd4 = "insert into `aws_topic_relation`(`id`,`topic_id`,`item_id`,`add_time`,`uid`,`type`) values('3','4','3','1493370061','1','article')"
    #cursor.execute(cmd4)
    conn.commit()
    conn.close()


#DB_Usage()
#DB_Usage_sqlite()
Aliyun()