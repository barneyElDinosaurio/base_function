# -*-  coding=utf-8 -*-
__author__ = 'rocky chen'
import matplotlib.pyplot as plt
from pandas import DataFrame, Series
import pandas as pd
import numpy as np
from matplotlib import mlab
from matplotlib import rcParams
import tushare as ts

def plot_test1():
    x = [1, 2]
    y = [2, 4]
    #plt.scatter(x,y)
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


def pd_plot():
    s = Series(np.random.randn(10).cumsum(), index=range(0, 100, 10))
    print s
    s.plot()
    #为啥不能显示，只能在ipython上作用 ？
    df = pd.DataFrame(np.random.randn(10, 4).cumsum(0), index=np.arange(0, 100, 10), columns=['A', 'B', 'C', 'D'])
    df.plot()


def bar_test():
    fig1 = plt.figure(2)
    rect = plt.bar(left=(0.2, 1), height=(1, 0.5), width=0.2, align='center', yerr=0.000001)
    plt.title("PE")
    plt.xticks((0.2, 1), ('one', 'two'))
    plt.show()


#最简单的话直线
def plot_line():
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 6, 8, 10]
    plt.plot(x, y)
    plt.show()


def plot_bar():
    x = [1, 2, 3, 4, 5]
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

def two_in_one_canvas():
    fig,ax=plt.subplots()
    df=ts.get_hist_data('300333')
    closed=df.close
    vol=df.volume
    print closed
    print vol
    closed.plot(ax)
    vol.plot(ax)
    plt.show()
#from_book()
#plot_test1()
#pd_plot()
#bar_test()
#plot_line()
#plot_bar()
#multi_plot()
two_in_one_canvas()