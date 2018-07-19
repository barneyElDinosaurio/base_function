# -*-coding=utf-8-*-
import pymysql
import time

import setting

connect = pymysql.connect(host=setting.MYSQL_HOST, port=setting.MYSQL_PORT, user=setting.MYSQL_USER,
                          passwd=setting.MYSQL_PASSWD, db=setting.MYSQL_DBNAME, charset='utf8')


def losecredit():
    name = '3486df4a8d4b21cfab42a1f56d52313e'
    idnum = '3622060fa9d08684b088f8769d8ee5c5'
    cursor = connect.cursor()
    cmd1 = 'select * from dishonest t where t.fnameGbkMd5=\'{}\''.format(name)
    cursor.execute(cmd1)
    ret = cursor.fetchall()
    if not ret:
        print("None")
        return

    for item in ret:
        flag = item[-1]
        # flag 为 1 身份证完整
        if flag == 1:
            cmd_1 = '''select t.fname,t.idNum from dishonest t where t.fnameGbkMd5=\'{0}\' and t.idNumMd5=\'{}\''''.format(
                name, idnum)
            cursor.execute(cmd_1)
            ret2 = cursor.fetchall()
        else:
            first_of_idnum = int(idnum[0], 16)
            if first_of_idnum == 0:
                cmd_2 = '''SELECT t.fname,t.idNum FROM dishonest t WHERE t.fnameGbkMd5 = \'{0}\' AND EXISTS (SELECT  1 FROM  credit t1 WHERE  t1.idNumMd5 = \'{1}\' AND CONCAT(LEFT(t1.idNum, 4),RIGHT(t1.idNum, 4)) = CONCAT(LEFT(t.idNum, 4),RIGHT(t.idNum, 4)))'''.format(
                    name, idnum)
            else:
                cmd_2 = '''SELECT t.fname,t.idNum FROM dishonest t WHERE t.fnameGbkMd5 = \'{0}\' AND EXISTS (SELECT  1 FROM  credit{1} t1 WHERE  t1.idNumMd5 = \'{2}\' AND CONCAT(LEFT(t1.idNum, 4),RIGHT(t1.idNum, 4)) = CONCAT(LEFT(t.idNum, 4),RIGHT(t.idNum, 4)))'''.format(
                    name, first_of_idnum, idnum)

            cursor.execute(cmd_2)
            ret2 = cursor.fetchall()
        if ret2:
            id_set = set()
            for i in ret2:
                # print(i)
                name_decode = i[0]
                id_set.add(i[1])

            id_list = list(id_set)
            query_set = []
            for i in id_list:
                query_set.append("\""+i+"\"")

            query_sets = ','.join(query_set)
            cmd_3 = '''SELECT DISTINCT t.cidno,t.fname, t.region, t.case_time, t.case_no, t.court, t.basis_no, t.detail,  t.fullfil, t.publish_time FROM   dw_person_dishonest t where  t.fname=\'{}\' and t.cidno in({})'''.format(name_decode,query_sets)
            cursor.execute(cmd_3)
            result = cursor.fetchall()
            colums=['cidno','fname','region','case_time','case_no','court','basis_no','detail','fullfil','publish_time']
            resp=[]

            for j in result:
                print('*****'*5)
                d={}
                for index, value in enumerate(j):
                    d[colums[index]]=value
                resp.append(d)
            return resp
        else:
            print("can not find the idnum")
            return None


def query_idnum(name):
    db_num =16
    for i in range(16):
        if i==0:
            tb_name = 'credit'
        else:
            tb_name='credit{}'.format(i)
        cmd = 'select * from'


# ret = losecredit()
# print(ret)
