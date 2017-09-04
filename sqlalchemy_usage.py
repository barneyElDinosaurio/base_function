# -*-coding=utf-8-*-
__author__ = 'xda'
#import sys
#reload(sys)
#sys.setdefaultencoding('utf-8')
from sqlalchemy import create_engine
import tushare as ts
import read_config

df = ts.get_tick_data('300333', date='2017-09-01')
print df

account = read_config.getUserData()
mysql_password = account['mysql_password']
engine = create_engine('mysql://root:%s@localhost/mydb?charset=utf8' % mysql_password)
df.to_sql('tick0901', engine)

