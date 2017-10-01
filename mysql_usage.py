# -*-coding=utf-8-*-
__author__ = 'xda'
import MySQLdb, sqlite3
import pandas as pd
from toolkit import Toolkit
import json


class mysql_usage():
    def __init__(self):
        # mysql_password = Toolkit.getUserData('data.cfg')['mysql_password']
        host = '192.168.137.44'
        user = 'rocky'
        db = 'mysql'
        # db='test_database'
        mysql_password = '123456z'
        self.db = MySQLdb.connect(host, user, mysql_password, db, charset='utf8')

    def DB_Usage(self):
        db = MySQLdb.connect("localhost", "root", "123456z", "house")
        cursor = db.cursor()
        cursor.execute("SELECT VERSION()")
        data = cursor.fetchone()
        print data
        # db.close()
        cmd = 'SELECT * from first;'
        df = pd.read_sql(cmd, db)
        print df
        db.close()

        db1 = sqlite3.connect("df_sql3.db")
        data = [[1, 2, 3, 4], [3, 4, 5, 6], [54, 234, 23, 222]]
        df1 = pd.DataFrame(data)
        print df1
        df1.to_sql("data", db1)

    def DB_Usage_sqlite(self):
        db = sqlite3.connect("db_sql_test.db")
        # cursor=db.cursor()
        # cursor.execute("SELECT VERSION()")
        # data=cursor.fetchone()
        # print data
        db.close()
        cmd = 'SELECT * from person;'
        df = pd.read_sql(cmd, db)
        print df

    def Aliyun(self):
        passwd = Toolkit.getUserData('data.cfg')['alipasswd']
        print passwd
        conn = MySQLdb.connect(host='bdm273219298.my3w.com',  # 远程主机的ip地址，
                               user='bdm273219298',  # MySQL用户名
                               db='bdm273219298_db',  # database名
                               passwd=passwd,  # 数据库密码
                               port=3306,  # 数据库监听端口，默认3306
                               charset="utf8")  # 指定utf8编码的连接
        cursor = conn.cursor()
        cursor.execute('SELECT VERSION()')
        data = cursor.fetchone()
        print data
        # 已经连通了，可以开搞。
        id = 31
        cmd1 = "insert into `aws_user_action_history_data`(`history_id`,`associate_content`,`associate_attached`,`addon_data`) values ('%d','huati','',''),('%d','','',''),('%d','Rocky-Title','ROCK-Content','')" % (
            id, id + 1, id + 2)
        cursor.execute(cmd1)
        # conn.commit()
        topic_id = 7
        title = "Hello" + str(topic_id)
        cmd2 = "insert into `aws_topic`(`topic_id`,`topic_title`,`add_time`,`discuss_count`,`topic_description`,`topic_pic`,`topic_lock`,`focus_count`,`user_related`,`url_token`,`merged_id`,`seo_title`,`parent_id`,`is_parent`,`discuss_count_last_week`,`discuss_count_last_month`,`discuss_count_update`) values('%d','huati5','1493370061','1','',null,'0','1','0',null,'0',null,'0','0','1','1','1493370061')" % topic_id
        cursor.execute(cmd2)
        # cursor.commit()
        arti_id = 5
        cmd3 = "insert into `aws_article`(`id`,`uid`,`title`,`message`,`comments`,`views`,`add_time`,`has_attach`,`lock`,`votes`,`title_fulltext`,`category_id`,`is_recommend`,`chapter_id`,`sort`) values('%d','1','ddThe Rocky23 IC ************TITLE','dddThe Rocky IC Content !!!!!!!!','0','1','1493370061','0','0','0','ic title','1','0',null,'0')" % arti_id
        cursor.execute(cmd3)
        # cursor.commit()
        cmd4 = "insert into `aws_topic_relation`(`id`,`topic_id`,`item_id`,`add_time`,`uid`,`type`) values('3','4','3','1493370061','1','article')"
        # cursor.execute(cmd4)
        conn.commit()
        conn.close()

    def create_table(self, table_name):
        cursor = self.db.cursor()
        create_cmd = '''
        CREATE TABLE ROCKYuuuuu(
        NAME TEXT,CITY_NAME TEXT,LOCATION TEXT,PRICE TEXT
        );
        '''
        print create_cmd
        cursor.execute(create_cmd)
        self.db.commit()
        self.db.close()

    def mysql_add_data(self, table):
        cursor = self.db.cursor()
        creat_db = '''
        create table if not exists houseinfo(
        name TEXT,city_name TEXT, location TEXT,price TEXT
        );
        '''
        cursor.execute(creat_db)
        self.db.commit()

        cursor.execute('select version()')
        data = cursor.fetchone()
        print data
        print type(data)
        my_dict = {"2017-07": [{"origin": "LJ", "price": 44267, "crawl_date": "2017-09-01"}]}
        price = json.dumps(my_dict)
        print price
        item2 = {'name': '万科', 'city_name': '深圳', 'location': '龙岗', 'price': price}
        item = {'name': 'wk2', 'city_name': '1sz1', 'location': 'lg1', 'price': '12111'}
        print item

        sql = '''
                insert into houseinfo ( name,city_name,location,price)
                values ('wk','sz','lg',12)  
                '''

        # 这个是可以正常运行的
        sql2 = '''insert into houseinfo ( name,city_name,location,price) values ('%s','%s','%s','%s')''' % (
        item2['name'], item2['city_name'], item2['location'], item2['price'])
        print sql2
        # sql 插入有问题
        cursor.execute(sql2)

        query_cmd = '''
        select name from first;
        '''
        # cursor.execute(sql)
        # data1=cursor.fetchone()
        # print data1

        self.db.commit()
        self.db.close()

    def query(self):
        vol = 500
        table = 'tick0901'
        sql_cmd1 = '''
        select * from %s where volume>%d;
        ''' % (table, vol)
        cursor = self.db.cursor()
        cursor.execute(sql_cmd1)
        # dataone=cursor.fetchone()
        dataall = cursor.fetchall()
        # print dataone
        for i in dataall:
            print i[0], i[1], i[2], i[3], i[4], i[5], i[6]

    def update(self):
        sql_cmd = '''
        update tick0901 set type='NA' where type='中性盘'
        '''
        cursor = self.db.cursor()
        cursor.execute(sql_cmd)
        self.db.commit()
        self.db.close()

    def transfer_data(self):
        fp = open('houseinfo_origin_all.json', 'r')
        cursor = self.db.cursor()
        linenumber = 0
        while 1:
            try:
                line = fp.readline()
                item = json.loads(line.strip())
                sql_cmd = '''
                insert into houseinfo(name,city_name,building_type,building_data,location,price) values('%s','%s','%s','%s','%s','%s')
                ''' % (item['name'], item['city_name'], item['building_type'], item['building_date'], item['location'],
                       json.dumps(item['price']))
                cursor.execute(sql_cmd)
                linenumber = linenumber + 1
            except Exception, e:
                print e
                print "EOF"
                break
        self.db.commit()
        self.db.close()
        print linenumber
        # print line

    def replace(self):
        cursor = self.db.cursor()
        cmd = '''
        insert into 
        '''

def remote_mysql():
    conn = MySQLdb.connect(host='172.16.103.57:9990', user='parker', passwd='parker_3z7ljV0dDjRO', db='db_parker')
    cursor = conn.cursor()
    cursor.execute("SELECT count(*) from tb_houses;")
    data = cursor.fetchone()
    print data
    conn.close()

def remote_mysql2():
    '''
    可以运行
    :return:
    '''
    import MySQLdb
    from sshtunnel import SSHTunnelForwarder

    with SSHTunnelForwarder(
                ('gdgwcmcc.jpushoa.com', 8220),
            ssh_password="Java!444",
            ssh_username="chenjw",
            remote_bind_address=('172.16.103.57', 3306)) as server:
        conn = MySQLdb.connect(host='127.0.0.1',
                               port=server.local_bind_port,
                               user='parker',
                               passwd='parker_3z7ljV0dDjRO',
                               db='db_parker')

        cursor = conn.cursor()
        cursor.execute("SELECT count(*) from tb_houses;")
        data = cursor.fetchone()
        conn.close()

if __name__ == '__main__':
    # DB_Usage()
    # DB_Usage_sqlite()
    # Aliyun()
    #obj = mysql_usage()
    #obj.create_table('houseinfo')
    # obj.mysql_add_data('temp')
    # obj.query()
    # obj.update()
    # obj.transfer_data()
    #remote_mysql2()
    remote_mysql()
