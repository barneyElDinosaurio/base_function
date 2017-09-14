# coding: utf-8
import codecs
import json
import pprint
import pymongo,datetime

def basic_usage():
    client = pymongo.MongoClient('127.0.0.1', 27017)
    # db=client.test
    db = client.demo_api
    # collection=db.houseinfo_aug
    collection = db.first_collection
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

def getlianjia_price():
    client=pymongo.MongoClient('127.0.0.1',27017)
    db=client.test
    data=db.total_lianjia.find({'city_name':'深圳'})
    data_list=list(data)
    print len(data_list)
    for i in data_list:
        print type(i)
        #js=json.loads(i['price'])
        print i['price']['2017-07'][0]['price']

def update_testcase():
    client=pymongo.MongoClient('127.0.0.1',27017)
    db=client['test']
    collection=db['enterprise']
    collection2=db['enterprise_new']
    data=collection.find({})
    data_new=list(data)
    for i in range(10):
        print data_new[1]

def update_json():
    fp=codecs.open('enterprise.json','r')
    while 1:
        org=json.loads(fp.readline())
        link='http://shop.99114.com'+org['link']


def remove_data():
    client=pymongo.MongoClient('127.0.0.1',27017)
    db=client.test
    db.total_lianjia_add_position.find()
#basic_usage()
#query()
#remove()
#insert()
#update()
#getlianjia_price()
update_testcase()