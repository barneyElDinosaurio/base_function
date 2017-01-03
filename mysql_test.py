#-*-coding=utf-8-*-
__author__ = 'xda'
#import sys
#reload(sys)
#sys.setdefaultencoding('utf-8')
from sqlalchemy import create_engine
import tushare as ts

df=ts.get_tick_data('300333',date='2016-12-27')
print df
engine=create_engine('mysql://root:temp@localhost/mydb?charset=utf8')
df.to_sql('tick_data1',engine)