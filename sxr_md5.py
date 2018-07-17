# -*-coding=utf-8-*-
import pymysql
import setting

connect = pymysql.connect(host=setting.MYSQL_HOST, port=setting.MYSQL_PORT, user=setting.MYSQL_USER,
                          passwd=setting.MYSQL_PASSWD, db=setting.MYSQL_DBNAME, charset='utf8')


def losecredit():
    name = '6591ee8fc212f28d070f377e4cd052c9'
    idnum = 'dacee6aa0491b2f0485301f7b125aec2'
    cursor = connect.cursor()
    cmd1 = 'select * from dishonest t where t.fnameGbkMd5=\'{}\''.format(name)
    cursor.execute(cmd1)
    ret = cursor.fetchall()
    if not ret:
        print("none")
        return

    for item in ret:
        flag = item[-1]
        # print(flag)
        if flag == 1:
            pass
        else:
            first_of_idnum = int(idnum[0], 16)
            if first_of_idnum == 0:
                cmd2 = '''SELECT t.fname,t.idNum FROM dishonest t WHERE t.fnameGbkMd5 = \'{0}\' AND EXISTS (SELECT  1 FROM  credit t1 WHERE  t1.idNumMd5 = \'{1}\' AND CONCAT(LEFT(t1.idNum, 4),RIGHT(t1.idNum, 4)) = CONCAT(LEFT(t.idNum, 4),RIGHT(t.idNum, 4)))'''.format(
                    name, idnum)
            else:
                cmd2 = '''SELECT t.fname,t.idNum FROM dishonest t WHERE t.fnameGbkMd5 = \'{0}\' AND EXISTS (SELECT  1 FROM  credit{1} t1 WHERE  t1.idNumMd5 = \'{2}\' AND CONCAT(LEFT(t1.idNum, 4),RIGHT(t1.idNum, 4)) = CONCAT(LEFT(t.idNum, 4),RIGHT(t.idNum, 4)))'''.format(
                    name, first_of_idnum, idnum)

            # print(cmd2)
            cursor.execute(cmd2)
            ret2 = cursor.fetchall()
            print(len(ret2))


losecredit()
