# coding: utf-8
import pymongo,datetime
client=pymongo.MongoClient('127.0.0.1',27017)
#db=client.test
db=client.py_create_db
#collection=db.houseinfo_aug
collection=db.test_collection
def basic_usage():
    data={"name":"a","sex":"F","school":"THSU"}
    data2={"name":"b","sex":"F","school":"SYSU"}
    collection.insert(data)
    collection.save(data2)

def query():
    print collection.count()
    print collection.find({'name':'a'})
    ''''
    for i in collection.find({'name':'a'}):
        print i
    '''
    for i in collection.find():
        print i

def remove():
    collection.remove({"name":"b"})

def insert():
    date=datetime.datetime.now()
    data={"name":"rocky","age":21,"date":date}
    collection.insert(data)

#basic_usage()
#query()
#remove()
insert()