#-*-coding=utf-8-*-
__author__ = 'rocchen'
import tushare as ts
import datetime
import urllib2

#df=ts.get_hist_data('300141',start='2011-01-01',end='2016-7-13')
#�������ֻ�ܻ�ȡ��3�������

import pandas as pd
import matplotlib
import matplotlib.pyplot
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
#���ڵĸ�ʽ����ת��
delta=60*7/5
#���ǵ������շǽ���
day0=datetime.date(datetime.date.today().year,datetime.date.today().month,datetime.date.today().day)
day30=day0-datetime.timedelta(delta)
print day30
day30=day30.strftime("%Y-%m-%d")
day0=day0.strftime("%Y-%m-%d")

def get_all_stock_id():
    #获取所有股票代码
    for i in stock_info.index:
        print i

def date_test():
    data=stock_info.ix['300141']['timeToMarket']
    print data
    print type(data)
    data=str(data)
    #print type(data)
    #print data[1:4]
    #print data[4:6]
    #print data
    date_format=data[0:4]+'-'+data[4:6]+'-'+data[6:8]
    #print date_format
    #日期的格式进行转换
    delta=60*7/5
    #考虑到周六日非交易
    day0=datetime.date(datetime.date.today().year,datetime.date.today().month,datetime.date.today().day)
    day30=day0-datetime.timedelta(delta)
    #print day30
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
    df = ts.get_hist_data('300141',start=day30,end=day0)
    print df.dtypes
    print df.index
    t1=df.iloc[0]
    print type(t1)

    t2=df[:1]
    print type(t2)
    print t2.index.values[0]


def news():
    getnews=ts.get_latest_news()
    print type(getnews)
    print getnews
    #print getnews
    '''
    for i in getnews:
        print i
    '''

def empty_type():
    id ="300527"
    df=ts.get_hist_data(id)
    print type(df)
    if df is None:
        print "None"
    else:
        print "Not Empty"

def exception_test():

    #遇到一些停牌的


    stockid='002316'
    df=ts.get_hist_data(stockid,start='20160601',end='20160701')
    if df.empty:
        print "empty"

def get_basic():

    hsdq=stock_info.ix['300141']
    print hsdq
    report=ts.get_report_data(2014,1)
    print report

    #hsdq=stock_info.ix['300141']
    #print hsdq
    #report=ts.get_report_data(2014,1)
    #print report
    print '*'*20
    df=ts.get_today_all()
    zrkj=df[df['code']=='300333']
    print type(zrkj)
    print type(zrkj['code'])
    print zrkj['name'].values[0]





def detail_tushare():

    #获取所有A股的基本信息

    all_file="http://218.244.146.57/static/all.csv"
    req=urllib2.Request(all_file)
    text = urllib2.urlopen(req).read()
    print text




def get_profit():
    #获取业绩
    pass

def get_real_time():
    df=ts.get_today_all()
    print df

def get_mount():
    df = ts.get_tick_data('300141',date='2016-07-25')
    df.plot()
    print df

def for_test():
    for _ in range(10):
        # only for loop, no variable
        print "Hello"

def plot_test():
    df=ts.get_hist_data('600415',start='2015-04-01',end='2015-06-18')
    # 所有的结果汇图
    df.plot()
    # 只将stock最高值进行汇图
    df.high.plot()
    # 指定绘图的四个量，并指定线条颜色
    with pd.plot_params.use('x_compat', True):
        df.open.plot(color='g')
        df.close.plot(color='y')
        df.high.plot(color='r')
        df.low.plot(color='b')
    # 指定绘图的长宽尺度及背景网格
    with pd.plot_params.use('x_compat', True):
        df.high.plot(color='r',figsize=(10,4),grid='on')
        df.low.plot(color='b',figsize=(10,4),grid='on')

def plot_test2():
    fig = matplotlib.pyplot.gcf()
    df = ts.get_hist_data('600415', start='2015-04-01', end='2015-06-18')
    with pd.plot_params.use('x_compat', True):
        df.high.plot(color='r', figsize=(10, 4), grid='on')
        df.low.plot(color='b', figsize=(10, 4), grid='on')
        fig.savefig('graph.png')

def get_each_mount():
    url='http://market.finance.sina.com.cn/downxls.php?date=2016-07-25&symbol=sz300141'
    req=urllib2.Request(url)
    resp=urllib2.urlopen(req)
    content=resp.read()
    data= content.decode('GBK')
    print len(data)

    TICK_COLUMNS = ['time', 'price', 'change', 'volume', 'amount', 'type']

def save_excel():
    df=ts.get_today_all()
    df.to_excel('1.xls',sheet_name='all_stock')
    df2=ts.get_hist_data('300333')
    df2.to_excel('1.xls',sheet_name='basic_info')
    df.ExcelWriter
    out=pd.ExcelWriter("2.xls")
    df.to_excel()


def gsz():
    hq=ts.get_today_all()
    hq['trade']=hq.apply(lambda x:x.settlement if x.trade == 0 else x.trade,axis=1)
    basedata=stock_info[['outstanding','totals','reservedPerShare','esp']]
    hqdata=hq[['code','name','trade','mktcap','nmc']]
    hqdata=hqdata.set_index('code')
    data=basedata.merge(hqdata,left_index=True,right_index=True)
    print data.head(10)


def new_api():
    data=ts.get_k_data('300333')
    print data

#读取我的股票列表
def getStockList(filename):
    f=open(filename,'r')
    stock_list=[]
    for i in f.readlines():

        stock_list.append(i.strip())
    return stock_list

#获取大单的数据
def getBigVol(code):
    #获取当天的分笔

    #today_vol=ts.get_today_ticks(code)
    #hist_vol=ts.get_tick_data(code,date='2016-11-28')
    #print today_vol.head(10)

    #print hist_vol

    hist_big_deal=ts.get_sina_dd(code,date='2016-12-01',vol=500)
    if hist_big_deal is None:
        print "No Big Deal"
    else :
        print hist_big_deal


#get_all_stock_id()
#check_type()
#news()


empty_type()
#exception_test()
get_basic()
#detail_tushare()

#empty_type()
#exception_test()
#get_basic()
#detail_tushare()
#get_all_stock_id()
#get_real_time()
#get_mount()
#for_test()
#get_each_mount()
#plot_test2()
#save_excel()

#get_real_time()
#gsz()
#new_api()
filename="mystock.txt"
getStockList(filename)
getBigVol('300527')
get_real_time()

