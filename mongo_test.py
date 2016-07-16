#-*-coding=utf-8-*-
__author__ = 'rocchen'
import pymongo
client=pymongo.MongoClient('localhost',1999)
db=client.test
print db.name
print db.my_collection
u=dict(name="user1",age=23)
