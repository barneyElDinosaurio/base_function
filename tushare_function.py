#-*-coding=utf-8-*-
__author__ = 'rocchen'
import tushare as ts
import datetime
#df=ts.get_hist_data('300141',start='2011-01-01',end='2016-7-13')
#这个函数只能获取近3年的数据
#print df

stock_info=ts.get_stock_basics()

data=stock_info.ix['300141']['timeToMarket']
print data
print type(data)
data=str(data)
print type(data)
print data[1:4]
print data[4:6]
print data
date_format=data[0:4]+'-'+data[4:6]+'-'+data[6:8]
print date_format
#日期的格式进行转换

day0=datetime.date(datetime.date.today().year,datetime.date.today().month,datetime.date.today().day)
day30=day0-datetime.timedelta(60)
print day30
day30=day30.strftime("%Y-%m-%d")
day0=day0.strftime("%Y-%m-%d")

'''
data="20101112"
index=0
for i in data:
    print index
    print i
    index=index+1
print data[1:3]
'''
df = ts.get_h_data('300141',start=day30,end=day0)
#这个函数可以获取所有的历史数据
#print df
highest= df['high']
lowest=df['low']
price_30_max = highest.max()
price_30_min = lowest.min()
print price_30_max
print price_30_min
#oneData= df.ix['2016-07-11']
#print oneData.iloc[0,1]
#print type(oneData)
for i in highest.len:
    print i

#print type(t)
