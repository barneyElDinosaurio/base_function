# -*-coding=utf-8-*-
import numpy as np
import pandas as pd
from pandas import Series
import matplotlib.pyplot as plt
from setting import get_engine
import time
#显示全部的行
pd.set_option('display.max_rows',None)

def df_practice():
    a = [1, -23, 4, 5, 6, 7, -4, 34, 3, 5, 33]
    b = [-2, 55, -5, 99, 3, -3, 55, 3, -1, 4, 7]
    df = pd.DataFrame({'A': a, 'B': b})
    print df
    #df.loc[(df['A']>0) & (df['B']<0),'A']=100
    #赋值测试
    #df.ix[(df['A'] > 0) & (df['B'] < 0), 'A'] = 100
    print df
    print df.ix[0, 0]
    print df.dtypes
    print df['A'].idxmax()

# 计算相关系数
def corr_number():
    a = pd.Series([1])
    b = pd.Series([2])
    if (b / a)[0] == 2:
        print "ok"
    c = [2, 4, 6, 8, 10, 12, 14, 16, 18]
    d = [i * 2  for i in c]
    print d
    #d[0] = 3
    s1 = Series(c)
    s2 = Series(d)

    corr = s1.corr(s2)
    print corr


def plot_test():
    s = Series(np.random.rand(20))
    #s.plot()
    #plt.show(s.plot(kind='hist'))
    ax = s.plot(kind='bar')
    fig = ax.get_figure()
    fig.savefig('1.png')


def compare_values():
    a = -10
    c = a + 1
    b = -9.299
    if a >= b and b < c:
        print "Got"


def autolabel(rects):
    for rect in rects:
        height = rect.get_height()
        print height


def calculate():
    total = []
    df = pd.read_excel('2017-04-15_all_.xls')
    '''
    i=-10
    dfx= df[(df['changepercent']>=(i+0.1)) & (df['changepercent']<((i+1))*1.000)]
    print dfx
    print dfx['changepercent'].iloc[0]
    print len(dfx)
    '''
    count = len(df[(df['changepercent'] >= -10.2) & (df['changepercent'] < -9)])
    total.append(count)
    for i in range(-9, 9, 1):
        #print i
        #print df[(df['changepercent']>=i) & (df['changepercent']<(i+1))]
        count = len(df[(df['changepercent'] >= i * 1.00) & (df['changepercent'] < ((i + 1)) * 1.00)])
        #print count
        total.append(count)
        #time.sleep(60)
        #total.append(count)
    count = len(df[(df['changepercent'] >= 9)])
    total.append(count)
    #print df
    sum = 0
    for i in range(len(total)):
        sum = sum + total[i]
    print sum
    print total
    #plt.style.use('ggplot')
    fig1 = plt.figure(len(total))
    df_figure = pd.Series(total, index=[range(-10, 10)])
    print df_figure
    #fg=df_figure.plot(kind='bar',title="2017-04-12",grid=True,table=True,)
    mycolor = ['g'] * 10
    mycolor2 = ['r'] * 10
    mycolor3 = list(mycolor, )
    mycolor.append(mycolor2)
    print len(total)
    fg = df_figure.plot(kind='bar', table=True)
    #autolabel(fg)
    plt.show(fg)


def jianshu():
    df = pd.read_excel('2017-04-15_all_.xls')
    print df.info()


def func(x):
    return x * 2


def apply_map_test():
    df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [10, 20, 30, 40, 50]})
    print df
    new_df = df.applymap(func)
    print new_df
    new_df1 = df.applymap(lambda x: x * 2)
    print new_df1

    df2 = df.apply(func)
    print df2


#行 合并
def row_merge():
    df = pd.DataFrame({'A': [1, 2, 3, 4, 5], 'B': [10, 20, 30, 40, 50]})
    df2 = pd.DataFrame({'A': [6], 'B': [60]})
    df_x = [df, df2]
    result = pd.concat(df_x)
    result = result.reset_index(drop=True)
    print result
    print df['A'][0]

def dataframe_create():
    df=pd.DataFrame()
    df['name']=[i for i in range(1,10)]
    print df
    df['id']=[chr(i) for i in range(ord('a'),ord('a')+9)]
    print df
    df = df.set_index('name',drop=False)
    print df

def dataframe_create1():
    l=10
    today=1
    code = 110
    name ='hello'
    opens = 1
    close =10
    high=0
    low=0
    vol=99
    amount=99
    df = pd.DataFrame(columns=[ 'datetime', 'code', 'name', 'open', 'close', 'high', 'low', 'vol', 'amount'])
    df.loc[99] = [ today, code, name, opens, close, high, low, vol, amount]
    print df
    engine = get_engine('test')
    #df.to_sql('test',engine,if_exists='append')

def main():

    #df_practice()
    #corr_number()
    #plot_test()
    #calculate()
    #compare_values()
    #jianshu()
    #apply_map_test()
    row_merge()
    #dataframe_create1()

main()