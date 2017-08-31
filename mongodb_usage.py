# coding: utf-8
import pprint
import pymongo,datetime
client=pymongo.MongoClient('127.0.0.1',27017)
#db=client.test
db=client.demo_api
#collection=db.houseinfo_aug
collection=db.first_collection
def basic_usage():
    #data={"name":"a","sex":"F","school":"THSU"}
    #ata2={"name":"b","sex":"F","school":"SYSU"}
    #collection.insert(data)
    #collection.save(data2)
    print db.first_collection
    print db.first_collection.find()
    arr=list(db.first_collection.find())
    print arr
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
    #data={"_id":"100001","name":"rocky","age":21,"date":date}
    for i in xrange (10000000,20000000):
        data={'_id':i}
        collection.insert(data)

def update():
    db. first_collection.update({'name':'rocky','age':19},{'name':'rocky','age':199})

#basic_usage()
#query()
#remove()
#insert()
update()