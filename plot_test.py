#-*-  coding=utf-8 -*-
__author__ = 'rocky chen'
import matplotlib.pyplot as plt
from pandas import DataFrame,Series
import pandas as pd
import numpy as np

def plot_test1():
    x=[1,2]
    y=[2,4]
    #plt.scatter(x,y)
    plt.scatter(x,y,color='red',marker='x')
    plt.axis([0,10,0,10])
    plt.show()


def plot_test2():
    pass

def from_book():
    fig=plt.figure()
    ax1=fig.add_subplot(2,2,1)
    ax2=fig.add_subplot(2,2,2)
    ax3=fig.add_subplot(2,2,3)
    ax4=fig.add_subplot(2,2,4)
    ax1.hist(range(100),bins=20,color='k',alpha=0.3)


def pd_plot():
    s=Series(np.random.randn(10).cumsum(),index=range(0,100,10))
    print s
    s.plot()
    #为啥不能显示，只能在ipython上作用
    df=pd.DataFrame(np.random.randn(10,4).cumsum(0),index=np.arange(0,100,10),columns=['A','B','C','D'])
    df.plot()
#from_book()
#plot_test1()
pd_plot()