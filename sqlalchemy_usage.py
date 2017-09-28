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
from anjuke import getcitylist
from sqlalchemy import create_engine,text,func
from sqlalchemy.orm import sessionmaker,relationship
import redis
import datetime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime, Integer, Text, INT,ForeignKey,Index
#from mayidaili import useproxy

engine = create_engine('mysql+pymysql://root:123456z@localhost:3306/db_parker?charset=utf8')
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
    '''
    def __repr__(self):
        return "House Name:%scity_name:%s" %(self.house_name,self.city_name)
    '''
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
    #price_r=relationship('Price',backref='houseinfo')
    #house=session.query(House).join(Price).filter(House.city_name=='珠海').filter(Price.origin=='FTX').first()
    #print  house.house_name,type(house.price)
    #print len(house)
    #print house.house_name
    '''
    for item in house:
        print item.house_name
        for i in item.price:
            print i.price
            #i.price=9999
            print i.origin
            print i.months
    '''
        #session.commit()
    #session.close()
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

    #price_info=session.query(House).join(Price).filter(text("city_name=:val1")).scalar()
    '''
    price_info=session.query(House).join(Price).filter(text("city_name=:val1")).params(val1='东莞',val2='AJK').first()
    #print price_info.price.price
    print price_info.house_name
    print price_info.city_name
    for i in  price_info.price:
        print i.price
        print i.origin
        print i.months
        print i.crawl_time
    '''
    #count=session.query(House.city_name).join(Price).filter(Price.origin=='LJ').count()
    #print count
    #print len(city_name)
    #print city_name
    #print city_name.house_name
    #print city_name.city_name
    #print city_name.address
    d=getcitylist()
    names = d.values()
    #print type(names)
    #for v in names:
        #print v

    number=session.query(func.count(House.city_name),House.city_name).join(Price).filter(Price.origin=='AJK').group_by(House.city_name).all()
    #print len(number)
    name_in_db=[]
    for i in number:
        #print i[0],i[1]
        name_in_db.append(i[1])
        #pass
        #if i[1] not in names:
            #print i[1]

    #for i in
    x=0
    for i in names:
        if i not in name_in_db:
            print i
            x=x+1
    print x

def query_name():
    ret=session.query(House.house_name,House.city_name).join(Price).filter(Price.origin=='AJK').filter(House.city_name=='滁州').all()
    print len(ret)

def update_city_name():
    q=session.query(House).join(Price).filter(House.city_name=='天长').all()
    for i in range(len(q)):
        #q[i][1]='滁州'
        #print q[i][0]
        #print q[i][1]
        q[i].city_name=u'滁州'
    try:
        session.commit()
    except:
       session.rollback()
    session.close()


def update_info():
    dbname = 'test'
    collection = 'qfang_house'
    client = pymongo.MongoClient('127.0.0.1', 27017)
    db = client[dbname]
    data = db[collection].find({})
    mongo_data = list(data)

    for mon_info in mongo_data:

        db_house = session.query(House).filter(House.house_name ==mon_info['name']).filter(House.city_name ==mon_info['city_name']).first()
        if db_house:
            print 'has same name and city'
            print  mon_info['name']
            print mon_info['city_name']
            #for  price_info in db_house.price:
            p=Price(
                price=mon_info['price'],
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
                url=mon_info['url'],
                latitude=mon_info['latitude'],
                longitude=mon_info['longitude'],
                address=mon_info['location'],
                building_date=mon_info['building_date'],
                building_type=mon_info['building_type']
            )
            price = Price(
                price=int(mon_info['price']),
                origin=mon_info['origin'],
                months=mon_info['month_price'],
                crawl_time=mon_info['crawl_date']
            )

            house.price.append(price)
            session.add(house)


        try:
            session.commit()
        except Exception, e:
            print e
            session.rollback()

if __name__=='__main__':
    #query_case()
    #update_info()
    #query_name()
    update_city_name()