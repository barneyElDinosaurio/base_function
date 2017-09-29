# coding: utf-8
import json
import urllib
import pymongo
import requests
import json
import random
import urllib
from urllib import quote
import MySQLdb
import time
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,relationship
import redis
import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime, Integer, Text, INT,ForeignKey
#from mayidaili import useproxy

engine = create_engine('mysql+pymysql://root:123456z@localhost:3306/house?charset=utf8')
DBSession = sessionmaker(bind=engine)
Base = declarative_base()
session = DBSession()


class House(Base):
    __tablename__ = 'tb_house'

    id = Column(Integer, primary_key=True)
    house_name = Column(String(80))
    city_name = Column(String(80))
    url = Column(String(300))
    price = relationship('Price',backref='houseinfo')
    latitude = Column(String(50))
    longitude = Column(String(50))
    address = Column(String(300))
    building_date = Column(String(60))
    building_type = Column(String(60))


class Price(Base):
    __tablename__ = 'tb_price'
    id = Column(Integer, primary_key=True)
    price = Column(Integer)
    origin = Column(String(80))
    months = Column(String(80))
    crawl_time = Column(DateTime)
    uid= Column(Integer,ForeignKey('tb_house.id'))

Base.metadata.create_all(engine)

dbname = 'test'
collection = 'fangtianxia_final1'
client = pymongo.MongoClient('127.0.0.1', 27017)
db = client[dbname]
data = db[collection].find({})
data_list = list(data)
x=0
for i in data_list:
    house = House(
    house_name = i['name'],
    city_name = i['city_name'],
    url = i['url'],
    latitude = i['latitude'],
    longitude = i['longitude'],
    address = i['location'],
    building_date = i['building_date'],
    building_type = i['building_type']
    )
    price=Price(
    price = int(i['price']),
    origin = i['origin'],
    months = i['month_price'],
    crawl_time = i['crawl_date']
    )

    house.price.append(price)
    session.add(house)
    try:
        session.commit()
    except Exception, e:
        print e
        session.rollback()
session.close()