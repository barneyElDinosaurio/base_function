# -*-coding=utf-8-*-
__author__ = 'rocchen'
import sqlite3
def insert():
    conn = sqlite3.connect("rocky_sqlite.db")
    print "open database passed"
    table_create = '''
                    CREATE TABLE COMPANY
                    (ID INT PRIMARY KEY,
                    NAME TEXT,
                    AGE INT,
                    ADDRESS CHAR(50),
                    SALARY REAL
                    );
                    '''
    conn.execute(table_create)
    temp="2017-12-12"
    #paul="INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES(1,?,32,'CALIFORNIA',2000.00);"
    allen="INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES(2,'ALLEN',72,'CALIFORNIA',20500.00);"
    teddy="INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES(3,'TEDDY',732,'CALIFORNIA',52000.00);"
    mark="INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES(4,'MARK',327,'CALIFORNIA',3000.00);"
    conn.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) VALUES(?,?,32,'CALIFORNIA',2000.00)",temp)
    conn.execute(allen)
    conn.execute(teddy)
    conn.execute(mark)
    conn.commit()
    conn.close()


def query():
    conn=sqlite3.connect(db_name)
    print "open database successful"
    query_command='select id,name,age,address,salary from COMPANY'
    data=conn.execute(query_command)
    for i in data:
        print "ID:\t%d" %i[0],
        print "NAME:\t%s" %i[1],
        print "AGE:\t%d" %i[2],
        print "ADDRESS:\t%s"% i[3],
        print "SALARY:\t%f" %i[4]

def update():
    salary=7777.3
    update_command='update COMPANY set SALARY=%f where ID=4' %salary
    conn=sqlite3.connect(db_name)
    conn.execute(update_command)
    conn.commit()
    #¼ÇµÃÒªcommit

insert()
#db_name='rocky_sqlite.db'
#query()
#update()
#print "After update"
#query()