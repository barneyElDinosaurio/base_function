# -*-coding=utf-8-*-
import redis

__author__ = 'xda'
import MySQLdb, sqlite3
import pandas as pd
from toolkit import Toolkit
import json,os
from setting import get_mysql_conn,get_engine

db = 'qdm225205669_db'
# engine = get_engine('daily')
conn = get_mysql_conn(db,local=False)

def groupcheck():
    cur =conn.cursor()
    cmd = 'select `email` from aws_users group by`email`'
    cur.execute(cmd)
    ret = cur.fetchall()
    domain = {}
    for i in ret:
        mail = i[0].split('@')[1]
        domain.setdefault(mail,0)
        domain[mail]+=1

    result = sorted(domain.items(),key=lambda x:x[1],reverse=True)
    print(result)

class MysqlUsage():
    def __init__(self):
        self.conn=get_mysql_conn('db_zdt',local=True)
    def getVersion(self):
        cur = self.db.cursor()
        cur.execute('select version()')
        data = cur.fetchone()
        print(data)

    def query(self):
        cursor = self.db.cursor()
        cmd = 'select * from `{}` where datetime = \'{}\''
        cursor.execute(cmd.format('300333', '2017-11-15'))
        data = cursor.fetchall()
        for i in data[0]:
            print(i,)
        print
        print(data[0])
        '''
        for i in data:
            print(i)
        '''

    def delete_item(self):
        cursor = self.db.cursor()
        cmd = 'select table_name from information_schema.`TABLES` where table_schema=\'{}\';'
        cursor.execute(cmd.format('history'))
        data = cursor.fetchall()
        for i in data:
            code = i[0]
            cmd_del = 'delete  from `{}` where datetime = \'2017-11-17\';'
            try:
                cursor.execute(cmd_del.format(code))
                # print(cursor.fetchall())
                self.db.commit()
            except Exception, e:
                print(e)
                self.db.rollback()

    def modify_table(self):
        engine_line = get_engine('db_selection')
        df = pd.read_sql_table('xiayinxian', engine_line, index_col='index')
        df['ocupy_ration'] = df['ocupy_ration'].map(lambda x: '%.3f' % x)
        # print(df)
        df.to_sql('xiayingxian', engine_line)

    def sql_table(self):

        df = pd.read_sql_table('2017-11-17', engine, index_col='index')

    def DB_Usage(self):

        db1 = sqlite3.connect("df_sql3.db")
        data = [[1, 2, 3, 4], [3, 4, 5, 6], [54, 234, 23, 222]]
        df1 = pd.DataFrame(data)
        print(df1)
        df1.to_sql("data", db1)

    def DB_Usage_sqlite(self):
        db = sqlite3.connect("db_sql_test.db")
        # cursor=db.cursor()
        # cursor.execute("SELECT VERSION()")
        # data=cursor.fetchone()
        # print(data)
        db.close()
        cmd = 'SELECT * from person;'
        df = pd.read_sql(cmd, db)
        print(df)

    def Aliyun(self):
        passwd = Toolkit.getUserData('data.cfg')['alipasswd']
        print(passwd)
        conn = MySQLdb.connect(host='',  # 远程主机的ip地址，
                               user='',  # MySQL用户名
                               db='',  # database名
                               passwd=passwd,  # 数据库密码
                               port=3306,  # 数据库监听端口，默认3306
                               charset="utf8")  # 指定utf8编码的连接
        cursor = conn.cursor()
        cursor.execute('SELECT VERSION()')
        data = cursor.fetchone()
        print(data)
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
        print(create_cmd)
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
        print(data)
        print(type(data))
        my_dict = {"2017-07": [{"origin": "LJ", "price": 44267, "crawl_date": "2017-09-01"}]}
        price = json.dumps(my_dict)
        print(price)
        item2 = {'name': '万科', 'city_name': '深圳', 'location': '龙岗', 'price': price}
        item = {'name': 'wk2', 'city_name': '1sz1', 'location': 'lg1', 'price': '12111'}
        print(item)

        sql = '''
                insert into houseinfo ( name,city_name,location,price)
                values ('wk','sz','lg',12)  
                '''

        # 这个是可以正常运行的
        sql2 = '''insert into houseinfo ( name,city_name,location,price) values ('%s','%s','%s','%s')''' % (
            item2['name'], item2['city_name'], item2['location'], item2['price'])
        print(sql2)
        # sql 插入有问题
        cursor.execute(sql2)

        query_cmd = '''
        select name from first;
        '''
        # cursor.execute(sql)
        # data1=cursor.fetchone()
        # print(data1)

        self.db.commit()
        self.db.close()

    def query_base(self):
        vol = 500
        table = 'tick0901'
        sql_cmd1 = '''
        select * from %s where volume>%d;
        ''' % (table, vol)
        cursor = self.db.cursor()
        cursor.execute(sql_cmd1)
        # dataone=cursor.fetchone()
        dataall = cursor.fetchall()
        # print(dataone)
        for i in dataall:
            print(i[0], i[1], i[2], i[3], i[4], i[5], i[6])

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
                print(e)
                print("EOF")
                break
        self.db.commit()
        self.db.close()
        print(linenumber)
        # print(line)

    def replace(self):
        cursor = self.db.cursor()
        cmd = '''
        insert into 
        '''

    def show_all_table(self):
        cur = self.conn.cursor()
        cmd='show tables;'
        cur.execute(cmd)
        content = cur.fetchall()
        for item in content:
            print(item[0])

def remote_mysql():
    conn = MySQLdb.connect(host='172.16.103.57:9990', user='parker', passwd='parker_3z7ljV0dDjRO', db='db_parker')
    cursor = conn.cursor()
    cursor.execute("SELECT count(*) from tb_houses;")
    data = cursor.fetchone()
    print(data)
    conn.close()


def remote_mysql2():
    '''
    可以运行
    :return:
    '''
    import MySQLdb
    from sshtunnel import SSHTunnelForwarder

    with SSHTunnelForwarder(
            ('x', 8220),
            ssh_password="x",
            ssh_username="x",
            remote_bind_address=('x', 3306)) as server:
        conn = MySQLdb.connect(host='127.0.0.1',
                               port=server.local_bind_port,
                               user='x',
                               passwd='x',
                               db='db_parker')

        cursor = conn.cursor()
        cursor.execute("SELECT count(*) from tb_houses;")
        data = cursor.fetchone()
        conn.close()


def create_db_case():
    low_db = get_mysql_conn('db_selection')
    low_cursor = low_db.cursor()
    code = '12345'
    cur_low = 12.22
    date = '2017-01-11'
    name = u'总公司'
    create_cmd = 'create table if not exists break_low ' \
                 '(`index` int primary key auto_increment,code text ,name text , cur_low float ,datetime datetime);'
    low_cursor.execute(create_cmd)
    insert_cmd = 'insert into break_low (code,name,cur_low,datetime) values (%s,%s,%s,%s);'
    low_info = (code, name, cur_low, date)
    low_cursor.execute(insert_cmd, low_info)
    low_db.commit()

# 删除某一行
def remove_row():
    r = redis.StrictRedis('localhost',6379,db=0)
    db=get_mysql_conn('history')
    cur = db.cursor()
    for k in r.keys():
        print(k)
        cmd = 'delete from `{}` where datetime > \'2017-11-16\';'.format(k)
        try:
            cur.execute(cmd)
            db.commit()
        except:
            db.rollback()
    db.close()


def run_sql_script():
    cur_db='python_test'

    # db = MySQLdb.connect(MYSQL_HOST, MYSQL_USER, MYSQL_PASSWORD, cur_db, charset='utf8')
    # cur=db.cursor()
    # with open('world.sql','r') as f:
    #     cur.executescript(f.read())
    # db.commit()
    # db.close()

    import sqlite3

    db=sqlite3.connect(cur_db)
    cur=db.cursor()
    with open('world.sql','rb') as f:
        cur.executescript(f.read())

def put_to_redis():
    r = redis.Redis(host='localhost', port=6379, db=10)
    conn = get_mysql_conn('db_parker',local=True)
    cursor = conn.cursor()
    cmd = 'select `identity_number` from frauds'
    cursor.execute(cmd)
    ret = cursor.fetchall()
    for i in ret:
        r.lpush('identity',i[0])


def main():
    # DB_Usage()
    # DB_Usage_sqlite()
    # Aliyun()
    # obj = MysqlUsage()
    # obj.query()
    # obj.delete_item()
    # obj.modify_table()
    # obj.sql_table()
    # obj.create_table('houseinfo')
    # obj.mysql_add_data('temp')
    # obj.query()
    # obj.update()
    # obj.transfer_data()
    # obj.show_all_table()
    # remote_mysql2()
    # remote_mysql()
    # create_db_case()
    # remove_row()
    # run_sql_script()
    # groupcheck()
    put_to_redis()

if __name__ == '__main__':
    data_path=os.path.join(os.getcwd(),'data')
    os.chdir(data_path) 
    main()
