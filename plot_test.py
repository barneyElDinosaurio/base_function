# -*-  coding=utf-8 -*-
import json

__author__ = 'rocky chen'
import matplotlib.pyplot as plt
from pandas import DataFrame, Series
import pandas as pd
import numpy as np
from matplotlib import mlab
from matplotlib import rcParams
import tushare as ts
import matplotlib
import os
import talib
import matplotlib.dates as mdates
from matplotlib.finance import candlestick2_ochl,volume_overlay
# from mpl_finance import candlestick_ochl
# from mpl_finance import candlestick2_ochl
matplotlib.style.use('ggplot')

data_path = os.path.join(os.getcwd(), 'data')
if not os.path.exists(data_path):
    os.mkdir(data_path)
os.chdir(data_path)
api = ts.get_apis()


def plot_test1():
    x = [1, 2]
    y = [2, 4]
    # plt.scatter(x,y)

    plt.scatter(x, y, color='red', marker='x')
    plt.axis([0, 10, 0, 10])
    plt.show()


def from_book():
    fig = plt.figure()
    ax1 = fig.add_subplot(2, 2, 1)
    ax2 = fig.add_subplot(2, 2, 2)
    ax3 = fig.add_subplot(2, 2, 3)
    ax4 = fig.add_subplot(2, 2, 4)
    ax1.hist(range(100), bins=20, color='k', alpha=0.3)
    x2 = np.arange(10)
    ax2.plot(x2, x2 * 5, label='x=y')
    # ax2.legend()
    plt.show()


def pd_plot():
    s = Series(np.random.randn(10).cumsum(), index=range(0, 100, 10))
    print s
    s.plot()
    # 为啥不能显示，只能在ipython上作用 ？
    df = pd.DataFrame(np.random.randn(10, 4).cumsum(0), index=np.arange(0, 100, 10), columns=['A', 'B', 'C', 'D'])
    df.plot()


def bar_test():
    fig1 = plt.figure(2)
    rect = plt.bar(left=(0.2, 1), height=(1, 0.5), width=0.2, align='center', yerr=0.000001)
    plt.title("PE")
    plt.xticks((0.2, 1), ('one', 'two'))
    plt.show()


# 最简单的话直线
def plot_line():
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 6, 8, 10]
    plt.plot(x, y)
    plt.show()


def plot_bar():
    # x = [1, 2, 3, 4, 5]
    x = ['1', '2', 'x', '4', '5']
    y = [2, 4, 6, 8, 10]
    plt.bar(x, y)
    plt.show()


def multi_plot():
    plt.figure(1)
    plt.figure(2)
    ax1 = plt.subplot(211)
    ax2 = plt.subplot(212)
    x = np.linspace(0, 3, 100)
    print x
    for i in xrange(5):
        plt.figure(1)
        plt.plot(x, np.exp(i * x / 3))
        plt.sca(ax1)
        plt.plot(x, np.sin(i * x))
        plt.sca(ax2)
        plt.plot(x, np.cos(i * x))
    plt.show()


def plot_csdn():
    date_list = []
    range_list = []
    f = open('csdn_range.txt', 'r')
    for i in f.readlines():
        # print i
        date_, range_ = i.split('\t')
        date_list.append(date_)
        range_list.append(range_)
    # plt.axis([0,33,0,20000])
    # plt.xlim(0,50)
    # plt.plot(date_list,range_list)
    plt.plot(range_list)
    plt.ylim([13000, 19000])
    plt.show()


def two_in_one_canvas():
    # fig,ax=plt.subplots(211)
    df = ts.get_hist_data('300333', '2015-01-01', '2016-12-30')
    closed = df.close
    vol = df.volume / 10000
    print closed
    print vol
    # closed.plot()
    closed.plot()
    vol.plot()
    plt.show()


def line_define():
    labels = 'frogs', 'hogs', 'dogs', 'logs'
    sizes = 15, 20, 45, 10
    colors = 'yellowgreen', 'gold', 'lightskyblue', 'lightcoral'
    explode = 0, 0.1, 0, 0
    # 画的是饼状图
    plt.pie(sizes, explode=explode, labels=labels, colors=colors, autopct='%1.1f%%', shadow=True, startangle=50)
    plt.axis('equal')
    plt.show()


def hist_test():
    mu, sigma = 100, 15
    x = mu + sigma * np.random.randn(10000)

    # 数据的直方图
    n, bins, patches = plt.hist(x, 50, normed=1, facecolor='g', alpha=0.75)

    plt.xlabel('Smarts')
    plt.ylabel('Probability')
    # 添加标题
    plt.title('Histogram of IQ')
    # 添加文字
    plt.text(60, .025, r'$mu=100, sigma=15$')
    plt.axis([40, 160, 0, 0.03])
    plt.grid(True)
    plt.show()


def multi_plot_rocky():
    plt.figure(1)
    # plt.figure(2)
    # plt.figure(3)
    # plt.figure(4)

    # plt.figure(1)
    ax1 = plt.subplot(2, 2, 1)
    ax2 = plt.subplot(2, 2, 2)
    ax3 = plt.subplot(2, 2, 3)
    ax4 = plt.subplot(2, 2, 4)
    x1 = range(0, 10)
    x2 = range(0, 20)
    x3 = range(0, 30)
    x4 = range(0, 40)
    plt.plot(x1, 'o')
    plt.sca(ax1)

    plt.plot(x2)
    plt.sca(ax2)

    plt.plot(x3)
    plt.sca(ax3)

    plt.plot(x4)
    plt.sca(ax4)

    plt.show()


def multi_plot_rocky2():
    plt.figure(1)
    # plt.figure(2)
    # plt.figure(3)
    # plt.figure(4)

    # plt.figure(1)
    # ax1=plt.subplot(2,2,1)
    # ax2=plt.subplot(2,2,2)
    # ax3=plt.subplot(2,2,3)
    # ax4=plt.subplot(2,2,4)
    x1 = range(0, 10)
    x2 = range(0, 20)
    x3 = range(0, 30)
    x4 = range(0, 40)
    plt.subplot(2, 2, 1)
    plt.title('x1')
    plt.plot(x1, 'o')
    # plt.sca(ax1)

    plt.subplot(2, 2, 2)
    plt.title('x2')
    plt.plot(x2)
    # plt.sca(ax2)

    plt.subplot(2, 2, 3)
    plt.title('x3')

    plt.plot(x3)
    # plt.sca(ax3)
    plt.subplot(2, 2, 4)
    plt.title('x4')

    plt.plot(x4)
    # plt.sca(ax4)
    # plt.subplot(2,1,1)
    # plt.title('x1')
    plt.show()


def other_mil():
    plt.figure(1)
    plt.subplot(211)
    plt.plot([1, 2, 3])
    plt.subplot(212)
    plt.plot([4, 5, 6])

    plt.figure(2)
    plt.plot([4, 5, 6])

    plt.figure(1)
    plt.subplot(211)
    plt.title('Easy as 1,2,3')
    plt.show()


def testcase1():
    # http://www.jianshu.com/p/1ad947f98e4c

    np.random.seed(2000)
    y = np.random.standard_normal((20, 2)).cumsum(axis=0)

    plt.figure(figsize=(7, 4))
    plt.plot(y[:, 0], lw=1.5, label='1st')
    plt.plot(y[:, 1], lw=1.5, label='2nd')
    plt.plot(y, 'ro')
    plt.grid(True)
    plt.legend(loc=0)
    plt.axis('tight')
    plt.xlabel('index')
    plt.ylabel('value')
    plt.title('A Simple Plot')
    plt.show()


def testcase2():
    x = np.arange(10)
    print x
    fig = plt.figure()
    ax = plt.subplot(111)

    for i in xrange(5):
        # ax.plot(x, i * x, label='y=%dx' %i)
        ax.plot(x, i * x, label='$y = %ix$' % i)

    # ax.legend(bbox_to_anchor=(1.2,1.2))
    ax.legend()

    plt.show()


def pie_test():
    plt.figure()
    x = [1, 1, 3]
    plt.pie(x)
    plt.show()


def hist_case1():
    # 概率分布直方图
    # 高斯分布
    # 均值为0
    mean = 0
    # 标准差为1，反应数据集中还是分散的值
    sigma = 1
    x = mean + sigma * np.random.randn(10000)
    fig, (ax0, ax1) = plt.subplots(nrows=2, figsize=(9, 6))
    # 第二个参数是柱子宽一些还是窄一些，越大越窄越密
    ax0.hist(x, 500, normed=1, histtype='bar', facecolor='yellowgreen', alpha=0.75)
    ##pdf概率分布图，一万个数落在某个区间内的数有多少个  
    ax0.set_title('pdf')
    ax1.hist(x, 20, normed=1, histtype='bar', facecolor='pink', alpha=0.75, cumulative=True, rwidth=0.8)
    # cdf累计概率函数，cumulative累计。比如需要统计小于5的数的概率
    ax1.set_title("cdf")
    fig.subplots_adjust(hspace=0.4)
    plt.show()


def my_hist():
    plt.figure('hello')
    x = np.random.randn(1000)
    print x
    plt.hist(x, bins=10, histtype='bar', alpha=0.75)
    plt.show()


def captcha():
    import string, random, os
    from PIL import ImageDraw, Image, ImageFont
    letter = string.ascii_lowercase + string.ascii_uppercase
    x = random.choice(letter)
    lens = 4
    random_text = ''
    for _ in range(lens):
        random_text += random.choice(letter)
    print random_text

    image = Image.new('RGB', (400, 100))
    font = ImageFont.truetype('msyh.ttf')
    draw = ImageDraw.Draw(image)
    xy = (100, 50)
    draw.text(xy=xy, text=random_text, font=font)
    image.show()


def fill_between_usage():
    x = np.linspace(-np.pi * 2, np.pi * 2, 100)
    y = np.sin(x)
    plt.plot(x, y)
    plt.fill_between(x, y)
    plt.show()

'''
两幅图在一起，上面是k线，下面是成交量
'''
def stock_plot():
    left, width = 0.1, 0.8
    rect_vol = [left, 0.1, width, 0.3]
    rect_main = [left, 0.4, width, 0.5]
    fig = plt.figure()
    conn = ts.get_apis()
    df = ts.bar('300333', conn=conn, start_date='2018-01-01')
    del df['code']
    df.reset_index(inplace=True)
    dates=df['datetime'].values

    df['datetime'] = df['datetime'].map(mdates.date2num)
    # dates=df['datetime'].values
    vol = df['vol'].values
    ax_vol = fig.add_axes(rect_vol)
    ax_vol.fill_between(dates, vol,color = 'y')
    # 横坐标时间旋转
    plt.setp(ax_vol.get_xticklabels(), rotation=30, horizontalalignment='right')
    ax_main = fig.add_axes(rect_main)
    candlestick_ochl(ax_main,df.values,width=0.6,colordown='g',colorup='r')
    ax_main.axes.get_xaxis().set_visible(False)
    ax_main.set_title("STOCK LINE")

    ts.close_apis(conn)
    plt.show()


def stock_line():
    api = ts.get_apis()
    df = ts.bar('300141', conn=api, start_date='2018-01-01')
    # print df
    del df['code']
    df.reset_index(inplace=True)
    print df
    df['datetime'] = df['datetime'].map(mdates.date2num)
    ax1 = plt.subplot2grid((6, 1), (0, 0), rowspan=5)
    ax2 = plt.subplot2grid((6, 1), (5, 0), rowspan=5, sharex=ax1)
    ax1.xaxis_date()
    candlestick_ochl(ax1, df.values, width=1, colorup='r', colordown='g')
    # ax2.fill_between(ax1,df['vol'].values,0)
    plt.show()
    ts.close_apis(api)

'''
网络上的教程：
https://ipreacher.github.io/2017/candlestick/
'''
def plot_stock_line(code,start):
    fig = plt.figure(figsize=(10,15))
    # fig,(ax,ax2)=plt.subplots(2,1,sharex=True,figsize=(16,10))
    ax=fig.add_axes([0,0.2,1,0.5])
    ax2=fig.add_axes([0,0,1,0.2])
    df = ts.bar(code,conn=api,start_date=start)
    # df=df.sort_values(by='datetime')
    df = df.sort_index()
    df =df.reset_index()
    # df = ts.get_k_data('300141',start='2018-03-01')
    # df['date']=df['date'].dt.strftime('%Y-%m-%d')
    df['datetime']=df['datetime'].dt.strftime('%Y-%m-%d')
    sma5=talib.SMA(df['close'].values,5)
    sma20=talib.SMA(df['close'].values,20)
    # ax.set_xticks(range(0,len(df),20))
    # # ax.set_xticklabels(df['date'][::5])
    # ax.set_xticklabels(df['datetime'][::20])
    candlestick2_ochl(ax,df['open'],df['close'],df['high'],df['low'],width=0.5,colorup='r',colordown='g',alpha=0.6)
    # ax.set_title(code)
    ax.plot(sma5)
    ax.plot(sma20)


    # df['vol'].plot(kind='bar')
    volume_overlay(ax2,df['open'],df['close'],df['vol'],width=0.5,alpha=0.8,colordown='g',colorup='r')
    ax2.set_xticks(range(0,len(df),20))
    # ax.set_xticklabels(df['date'][::5])
    ax2.set_xticklabels(df['datetime'][::20])
    # ax2.grid(True)

    # plt.setp(ax.get_xticklabels(), rotation=30, horizontalalignment='right')
    # plt.grid(True)
    # plt.subplots_adjust(hspace=0)
    plt.show()

def get_selected_stock():
    with open('../codes.txt') as f:
        js_data = json.load(f)

    code_list = js_data.get('example1')
    for code in code_list:
        print code,code_list[code]
        plot_stock_line(code,'2018-01-01')
    ts.close_apis(api)

def main():
    # from_book()
    # plot_test1()
    # pd_plot()
    # bar_test()
    # plot_line()
    # plot_bar()
    # multi_plot()
    # plot_csdn()
    # two_in_one_canvas()
    # line_define()
    # hist_test()
    # multi_plot_rocky2()
    # other_mil()
    # testcase1()
    # testcase2()
    # pie_test()
    # hist_case1()
    # my_hist()
    # captcha()
    # stock_plot()
    # fill_between_usage()
    # stock_line()
    plot_stock_line('300333','2017-09-01')
    # get_selected_stock()

main()
