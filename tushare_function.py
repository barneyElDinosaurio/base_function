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
delta=60*7/5
#考虑到周六日非交易
day0=datetime.date(datetime.date.today().year,datetime.date.today().month,datetime.date.today().day)
day30=day0-datetime.timedelta(delta)
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

def get_high_test():
    df = ts.get_h_data('300141',start=day30,end=day0)
    #这个函数可以获取所有的历史数据
    #print df
    #current= df[:1]
    #current=df.iloc[0]
    print df
    current=df.ix['2016-07-15']
    print current
    current_high=current['high'].values[0]
    print current_high
    highest= df['high']
    lowest=df['low']

    price_30_max = highest.max()
    price_30_min = lowest.min()

    print df[df.high>=price_30_max]
    #得出出现最大值的那一天
    print df[df.low<=price_30_min]
    #得出出现最小值的那一天

    print price_30_max
    print price_30_min
    #oneData= df.ix['2016-07-11']
    #print oneData.iloc[0,1]
    #print type(oneData)
    #for i in highest.len:
    #    print i

    #print type(t)
    if current_high>=price_30_max:
        print stock_info.ix['300141']['name'].decode('utf-8')


def get_all_stock_id():
    print len(stock_info.index)
    for i in  stock_info.index:
        print i


def check_type():
    df = ts.get_h_data('300141',start=day30,end=day0)
    print df.dtypes
    print df.index


def news():
    getnews=ts.get_latest_news()
    print type(getnews)
    print getnews
    #print getnews
    '''
    for i in getnews:
        print i
    '''


#get_all_stock_id()
#check_type()
news()