# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

from sqlalchemy import Column, String , DateTime, Integer, Text,Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import datetime

# engine = create_engine('mysql+pymysql://crawler:Crawler@1234@10.18.4.211:3367/spider?charset=utf8')
engine = create_engine('mysql+pymysql://root:123456z@localhost/spider?charset=utf8')


Base = declarative_base()

class CreditRecord(Base):
    __tablename__ = 'tb_gdcic'

    id = Column(Integer, primary_key=True,autoincrement=True)
    enterprise = Column(String(180),comment='')
    enterprise_link = Column(String(380),comment='')
    punish_file = Column(String(100),comment='')
    punish_file_no = Column(String(50),comment='')
    punish_dept = Column(String(80),comment='')
    punish_date = Column(Date,comment='')
    crawl_date = Column(DateTime, default=datetime.datetime.now())

Base.metadata.create_all(engine)
DBSession = sessionmaker(bind=engine)


class GdcicPipeline(object):
    def open_spider(self, spider):
        self.session = DBSession()

    def process_item(self, item, spider):
        obj = CreditRecord(
            enterprise=item['enterprise'],
            enterprise_link=item['enterprise_link'],
            punish_file=item['punish_file'],
            punish_file_no=item['punish_file_no'],
            punish_dept=item['punish_dept'],
            punish_date=item['punish_date']
        )

        self.session.add(obj)
        try:
            self.session.commit()
        except Exception as e:
            print(e)
            self.session.rollback()

        return item
