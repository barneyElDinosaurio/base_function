# coding: utf-8
import codecs
import json
import pprint
import pymongo, datetime
import pandas as pd
host = 'localhost'
client = pymongo.MongoClient(host, 27017)

def basic_usage():
    client = pymongo.MongoClient(host, 27017)
    # db=client.test
    db = client.demo_api
    # collection=db.houseinfo_aug
    collection = db.first_collection
    # data={"name":"a","sex":"F","school":"THSU"}
    # ata2={"name":"b","sex":"F","school":"SYSU"}
    # collection.insert(data)
    # collection.save(data2)
    print(db.first_collection)
    print(db.first_collection.find())
    arr = list(db.first_collection.find())
    print(arr)


def query():
    print(collection.count())
    print(collection.find({'name': 'a'}))
    ''''
    for i in collection.find({'name':'a'}):
        print(i)
    '''
    for i in collection.find():
        print(i)


def remove():
    collection.remove({"name": "b"})


def insert():
    client = pymongo.MongoClient(host, 27017)
    # db=client.test
    db = client.demo_api
    # collection=db.houseinfo_aug
    collection = db.first_collection
    date = datetime.datetime.now()
    data = {"_id": "100001", "name": "rocky", "age": 21, "date": date}
    for i in xrange(100, 200):
        # data={'_id':i}
        data['_id'] = i
        collection.save(data)


def update():
    db.first_collection.update({'name': 'rocky', 'age': 19}, {'name': 'rocky', 'age': 199})


def getlianjia_price():
    client = pymongo.MongoClient('127.0.0.1', 27017)
    db = client.test
    data = db.total_lianjia.find({'city_name': '深圳'})
    data_list = list(data)
    print(len(data_list))
    for i in data_list:
        print(type(i))
        # js=json.loads(i['price'])
        print(i['price']['2017-07'][0]['price'])


def update_testcase():
    client = pymongo.MongoClient('127.0.0.1', 27017)
    db = client['test']
    collection = db['enterprise']
    collection2 = db['enterprise_new']
    data = collection.find({})
    data_new = list(data)
    for i in range(10):
        print(data_new[1])


def update_json():
    fp = codecs.open('enterprise.json', 'r')
    while 1:
        org = json.loads(fp.readline())
        link = 'http://shop.99114.com' + org['link']


def remove_data():
    client = pymongo.MongoClient('127.0.0.1', 27017)
    db = client.test
    data = db.fangtianxia_remove_same.find({'city_name': '北京'})
    curr = list(data)
    # print(len(curr))
    for i in curr:
        print(i['city_name'])
        db.fangtianxia_remove_same.remove({'city_name': i['city_name']})


def insert_bj():
    client = pymongo.MongoClient('127.0.0.1', 27017)
    db = client.test
    bj_data = db.fangtianxia.find({'city_name': '北京'})
    data = list(bj_data)
    print(len(data))
    for i in data:
        # print(i)
        db.fangtianxia_remove_same.insert(i)


def update_url():
    dbname = 'test'
    collection = 'fangtianxia_final1'

    client = pymongo.MongoClient('127.0.0.1', 27017)
    db = client[dbname]
    data = db[collection].find({})
    data_list = list(data)
    for i in data_list:
        org_url = i['url']
        # new_url=org_url.replace('//','/')
        # print(new_url)
        print(org_url)
        db[collection].update({'url': org_url},
                              {'$set': {'crawl_date': '2017-09-15', 'month_price': '2017-09', 'origin': 'FTX'}})


def get_price():
    dbname = 'test'
    collection = 'total_lianjia_baidu'
    client = pymongo.MongoClient('127.0.0.1', 27017)
    db = client[dbname]
    data = db[collection].find({})
    data_list = list(data)
    for i in data_list:
        try:
            price = i['price']['2017-07'][0]['price']
            # print(type(price))
            # print(price)
        except:
            print(i['name'])
            print(i['city_name'])
        # url=i['url']
        # print(price)
        # if city_name==u'合川':
        # db[collection].update({'url': url}, {'$set': {'city_name': '郑州'}})

        if price > 0 and price <= 1000:
            print(price)

            # print(i['url'])
        # new_url = org_url.replace('//', '/')
        # print(new_url)
        # db[collection].update({'url': url}, {'$set': {'price': 0}})


def change_city():
    dbname = 'anjuke_mobile'
    collection = 'mobile_complete_update_change_price'
    client = pymongo.MongoClient('127.0.0.1', 27017)
    db = client[dbname]
    # data = db[collection].find({'city_name':'溧阳'})
    # data_list = list(data)
    # for i in data_list:
    db[collection].update({'city_name': '溧阳'}, {'$set': {'city_name': '常州'}}, {'multi': True})


def update_id():
    collection = client['test']['update']
    url = 'qq.com'
    html = '<hello world!!!!!!!!!!!!!!!>'
    collection.update({'_id': url}, {'$set': {'html': html}}, upsert=True)


class Mongo():
    def __init__(self, db, collection):
        self.collection = client[db][collection]

    def __getitem__(self, item):
        return self.collection.find({'_id': item})

    def __setitem__(self, key, value):
        self.collection.update({'_id': key}, {'$set': {'html': value}}, upsert=True)


def mongo_case1():
    mongo = Mongo()
    # mongo['baidu.com']='http://baidu.com'
    # mongo['jd.com']='http://jd.com'
    # mongo['taobao.com']='http://taobao.com'
    mongo['qq.com'] = 'http://qq.com'


# basic_usage()
# query()
# remove()
# insert()
# update()
# getlianjia_price()
# update_testcase()
# remove_data()
# insert_bj()
# update_url()
# get_price()
# change_city()
# update_id()
# mongo_case1()

# 便于在ubuntu查询 mongo数据库
class StockMongo():
    def __init__(self, db, collection):
        self.collection = client[db][collection]

    def __getitem__(self, item):
        return self.collection.find({'_id': item})

    def __setitem__(self, key, value):
        self.collection.update({'_id': key}, {'$set': {'html': value}}, upsert=True)

    def find(self):
        ret = self.collection.find({})
        for i in ret:
            for k,v in i.items():
                if k!='_id':
                    print(k,v)

    def show_industry(self):
        ret = self.collection.find({},{'_id':0})
        print(ret)
        print(type(ret))
        for item in ret:

            print(item.get(u'版块名称'))

    def findone(self,name):
        ret = self.collection.find({u'版块名称':name})
        for i in ret:
            codes= i.get(u'代码',None)
            for code in codes:
                print(code)


def remove_str(x):
    ret = x.strip()
    l = ret.split('.')
    return '-'.join(l)
    # return x.strip()


def mongo_calculation():
    collection=client['proxyip']['pool']
    result={}

    ret = collection.find({},{'created_at':1,'source':1})

    ret = collection.find({})

    print('start to calculate')
    count =0
    # ret= collection.find_one({'source':u'持仓盈亏'},{'description':1,'source_link':1})

    ret_list = list(ret)
    df = pd.DataFrame(ret_list)

    del df['_id']
    print(df.info())

    # del df['_id']

    print(df.info())
    print(df.head())
    # df['ip']=list(map(lambda x:x.strip(),df['ip']))
    df['ips']=df['ip'].map(remove_str)
    print(df['ips'])

    # for i in ret:
    #     count+=1
    #     result.setdefault(i.get('source'),0)
    #     result[i.get('source')]+=1
    # # print(result)
    # for k,v in result.items():
    #     print(k,v)


def main():
    # obj=StockMongo('stock','industry')
    # obj.find()
    # obj.findone(u'中成')
    # obj.show_industry()
    mongo_calculation()

if __name__ == '__main__':
    main()
