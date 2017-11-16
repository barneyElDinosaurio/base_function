#-*-coding=utf-8-*-
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
from sqlalchemy import event
from sqlalchemy import DDL
engine = create_engine('mysql+pymysql://root:123456z@localhost:3306/stock?charset=utf8')
DBSession = sessionmaker(bind=engine)
Base = declarative_base()
session = DBSession()


class House(Base):
    __tablename__ = 'delivery'

    `index`

    u'成交日期'

    `摘要`
    text,
    `证券名称`
    text,
    `合同编号`
    bigint(20)
    DEFAULT
    NULL,
    `成交数量`
    bigint(20)
    DEFAULT
    NULL,
    `成交均价`
    double
    DEFAULT
    NULL,
    `成交金额`
    bigint(20)
    DEFAULT
    NULL,
    `手续费`
    bigint(20)
    DEFAULT
    NULL,
    `印花税`
    double
    DEFAULT
    NULL,
    `其他杂费`
    double
    DEFAULT
    NULL,
    `发生金额`
    double
    DEFAULT
    NULL,
    `股东帐户`
    text,
    `备注`
    bigint(20)
    DEFAULT
    NULL,
    `操作`
    text,
    `证券代码`
    bigint(20)
    DEFAULT
    NULL,
    `结算汇率`
    bigint(20)
    DEFAULT
    NULL,
    KEY
    `ix_delivery_index`(`index`)

    )