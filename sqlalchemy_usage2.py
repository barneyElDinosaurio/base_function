# coding: utf-8
'''
使用sqlalchemy查询 非ORM的 表
'''
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy import Column, String, DateTime, Integer, Text, INT,ForeignKey,Index
engine = create_engine('mysql+pymysql://root:@localhost:3306/stock?charset=utf8',echo=True)
#DBSession = sessionmaker(bind=engine)
#session = DBSession()
Base = declarative_base(engine)


class Delivery(Base):
    __tablename__ = 'baseinfo'
    __table_args__ = {'autoload': True}

def loadSession():
    metadata = Base.metadata
    Session = sessionmaker(bind=engine)
    session = Session()
    return session

class Baseinfo(Base):
    __tablename__='baseinfo'
    code=Text()

Base.metadata.create_all(engine)

session=loadSession()
all = session.query(Baseinfo).all()
