# coding: utf-8
# coding: utf-8
import json
import urllib

import pymongo
import requests
# coding: utf-8
import json
import random
import urllib
from urllib import quote
import MySQLdb
import datetime
import requests
import time
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import redis
import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime, Integer, Text, INT
#from mayidaili import useproxy

engine = create_engine('mysql+pymysql://root:@localhost:3306/house?charset=utf8')
DBSession = sessionmaker(bind=engine)
Base = declarative_base()
session = DBSession()


class Advertiser(Base):
    __tablename__ = 'tb_sep'

    id = Column(Integer, primary_key=True)
    house_name = Column(String(80))
    city_name = Column(String(80))
    url = Column(String(300))
    price = Column(INT)
    latitude = Column(String(50))
    longitude = Column(String(50))
    origin = Column(String(80))
    months = Column(String(80))
    crawl_time = Column(DateTime)
    address = Column(String(300))
    building_date = Column(String(60))
    building_type = Column(String(60))


Base.metadata.create_all(engine)

dbname = 'test'
collection = 'fangtianxia_final1'
client = pymongo.MongoClient('127.0.0.1', 27017)
db = client[dbname]
data = db[collection].find({})
data_list = list(data)
for i in data_list:
    advertiser = Advertiser(
    house_name = i['name'],
    city_name = i['city_name'],
    url = i['url'],
    price = int(i['price']),
    latitude = i['latitude'],
    longitude = i['longitude'],
    origin = i['origin'],
    months = i['month_price'],
    crawl_time = i['crawl_date'],
    address = i['location'],
    building_date = i['building_date'],
    building_type = i['building_type']
    )
    session.add(advertiser)

    try:
        session.commit()
    except Exception as e:
        print(e)
        session.rollback()

session.close()