# -*-coding=utf-8-*-
import json
import urllib
import pymongo
import requests
import json
import random
import urllib
from urllib import quote
import MySQLdb
import datetime
import requests
import time
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,relationship
import redis
import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime, Integer, Text, INT,ForeignKey,Index
#from mayidaili import useproxy
from sqlalchemy import event
from sqlalchemy import DDL

engine = create_engine('mysql+pymysql://root:123456z@localhost:3306/house?charset=utf8')
DBSession = sessionmaker(bind=engine)
Base = declarative_base()
session = DBSession()


class House(Base):
    __tablename__ = 'tb_house'

    id = Column(Integer, primary_key=True)
    house_name = Column(String(80),index=True)
    city_name = Column(String(80),index=True)
    url = Column(String(300))
    price = relationship('Price',backref='houseinfo',cascade="all, delete-orphan",lazy='dynamic',passive_deletes=True)
    latitude = Column(String(50))
    longitude = Column(String(50))
    address = Column(String(300))
    building_date = Column(String(60))
    building_type = Column(String(60))

    __table_args__ = (
        #UniqueConstraint('id', 'name', name='uix_id_name'),  # 联合唯一索引
        Index('house_name', 'city_name'),  # 联合索引
    )

event.listen(
        House.__table__,
        "after_create",
        DDL("ALTER TABLE %(table)s AUTO_INCREMENT = 100000;")
    )

class Price(Base):
    __tablename__ = 'tb_price'
    id = Column(Integer, primary_key=True)
    price = Column(Integer)
    origin = Column(String(80))
    months = Column(String(80))
    crawl_time = Column(DateTime)
    uid= Column(Integer,ForeignKey('tb_house.id'))

Base.metadata.create_all(engine)

def query_case():
    price_r=relationship('Price',backref='houseinfo')
    house=session.query(House).join(Price).filter(House.city_name=='珠海').filter(Price.origin=='FTX').first()
    #print  house.house_name,type(house.price)
    #print len(house)
    for item in house:
        print item.house_name
        for i in item.price:
            print i.price
            i.price=9999
            print i.origin
            print i.months
        session.commit()
    session.close()
    #house = session.query(House).join(Price,isouter=True).filter(House.city_name=='珠海').filter(Price.origin=='FTX').first()
    #print house.house_name, house.price,house.city_name,house.address

    #for i in house:
        #print i
    #print house
    '''
    for h in house:
        h.house_name
    '''
    #print house.first()
    #query_case()
def update_info():
    dbname = 'test'
    collection = 'total_lianjia_baidu'
    client = pymongo.MongoClient('127.0.0.1', 27017)
    db = client[dbname]
    data = db[collection].find({})
    mongo_data = list(data)

    for mon_info in mongo_data:

        db_house = session.query(House).filter(House.house_name ==mon_info['name']).filter(House.city_name ==mon_info['city_name']).first()
        if db_house:
            #print 'has same name and city'
            #print  mon_info['name']
            #print mon_info['city_name']
            # 需要添加判断, 以防同一个价格数据插入多次
            p=Price(
                price=int(mon_info['price']),
                origin = mon_info['origin'],
                months = mon_info['month_price'],
                crawl_time = mon_info['crawl_date'],
                uid = db_house.id
            )
            db_house.price.append(p)

        else:
            house = House(
                house_name=mon_info['name'],
                city_name=mon_info['city_name'],
                #url=mon_info['url'],
                latitude=mon_info['latitude'],
                longitude=mon_info['longitude'],
                address=mon_info['location'],
                building_date=mon_info['building_date'],
                building_type=mon_info['building_type']
            )
            price = Price(
                price=int(mon_info['price']['2017-07'][0]['price']),
                origin=mon_info['price']['2017-07'][0]['origin'],
                months='2017-07',
                crawl_time=mon_info['price']['2017-07'][0]['crawl_date']
            )

            house.price.append(price)
            session.add(house)

        try:
            session.commit()
        except Exception, e:
            print e
            session.rollback()

update_info()
session.close()