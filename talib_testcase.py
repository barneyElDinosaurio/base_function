# -*-coding=utf-8-*-
__author__ = 'Rocky'
'''
http://30daydo.com
Contact: weigesysu@qq.com
'''
import talib
import numpy as np
import tushare as ts
from matplotlib import pyplot as plt
from setting import get_engine
import pandas as pd
pd.set_option('expand_frame_repr',False)

def baseAPI():
    # 通过tushare获取股票信息
    df = ts.get_k_data('300580', start='2017-01-12', end='2017-05-26')
    # 提取收盘价
    closed = df['close'].values
    # 获取均线的数据，通过timeperiod参数来分别获取 5,10,20 日均线的数据。
    ma5 = talib.SMA(closed, timeperiod=5)
    ma10 = talib.SMA(closed, timeperiod=10)
    ma20 = talib.SMA(closed, timeperiod=20)

    # 打印出来每一个数据
    print(closed)
    print(ma5)
    print(ma10)
    print(ma20)

    # 通过plog函数可以很方便的绘制出每一条均线
    plt.plot(closed)
    plt.plot(ma5)
    plt.plot(ma10)
    plt.plot(ma20)
    # 添加网格，可有可无，只是让图像好看点
    plt.grid()
    # 记得加这一句，不然不会显示图像
    plt.show()


def boll():
    # 通过tushare获取股票信息
    df = ts.get_k_data('300580', start='2017-01-12', end='2017-05-26')
    # 提取收盘价
    closed = df['close'].values

    upper, middle, lower = talib.BBANDS(closed, matype=talib.MA_Type.SMA)
    print(upper, middle, lower)
    plt.plot(upper)
    plt.plot(middle)
    plt.plot(lower)
    plt.grid()
    plt.show()
    diff1 = upper - middle
    diff2 = middle - lower
    print(diff1)
    print(diff2)


def price_moment():
    df = ts.get_k_data('300580', start='2017-01-12', end='2017-05-26')
    closed = df['close'].values
    ouput = talib.MOM(closed, timeperiod=5)
    print(closed)
    print(ouput)
    plt.plot(ouput)
    plt.grid()
    plt.show()


def ma_type_test():
    # MA_Type: 0=SMA, 1=EMA, 2=WMA, 3=DEMA, 4=TEMA, 5=TRIMA, 6=KAMA, 7=MAMA, 8=T3 (Default=SMA)
    df = ts.get_k_data('300580', start='2017-01-12', end='2017-05-26')
    closed = df['close'].values
    sma = talib.MA(closed, timeperiod=10, matype=0)
    ema = talib.MA(closed, timeperiod=10, matype=1)
    wma = talib.MA(closed, timeperiod=10, matype=2)
    dema = talib.MA(closed, timeperiod=10, matype=3)
    tema = talib.MA(closed, timeperiod=10, matype=4)
    trima = talib.MA(closed, timeperiod=10, matype=5)
    kma = talib.MA(closed, timeperiod=10, matype=6)
    mama = talib.MA(closed, timeperiod=10, matype=7)
    t3 = talib.MA(closed, timeperiod=10, matype=8)
    # ouput=talib.MA(closed,timeperiod=5,matype=0)
    print(closed)
    plt.ylim([0, 40])
    plt.plot(sma, 'r--')
    plt.plot(ema, 'g-*')
    plt.plot(wma)
    plt.plot(dema)
    plt.plot(tema)
    plt.plot(trima)
    plt.plot(kma)
    plt.plot(mama)
    plt.plot(t3)
    plt.grid()
    plt.text(7, 30, 'BST')

    plt.show()

def get_all_code():
    engine = get_engine('db_stock')
    df = pd.read_sql('basic_info',engine,index_col='index')
    for code in df['code'].values:
        find_pattern(code)

def find_pattern(code):
    pattern = ''
    engine = get_engine('history')
    try:
        df = pd.read_sql(code, engine, index_col='index',)
    except Exception as e:
        print(e)
        return
    # print(df)
    # for i in  df['open'].astype('float').values:
    #     print(type(i))
    # print(df['high'].values)
    # print(df['low'].values)
    # print(df['close'].values)
    result = talib.CDLDARKCLOUDCOVER(df['open'].astype('float').values,
                            df['high'].astype('float').values,
                           df['low'].astype('float').values,
                          df['close'].astype('float').values)

    df['CDL2CROWS']=result
    if len(df[df['CDL2CROWS']!=0])!=0:
        print(df[df['CDL2CROWS']!=0])
# baseAPI()
# boll()
# price_moment()
# ma_type_test()
# find_pattern('000333')
get_all_code()