# -*-coding=utf-8-*-
__author__ = 'Rocky'
import pandas as pd
import datetime
from pandas import DataFrame
import tushare as ts


def GetstockData(code,start,end=None):
    api=ts.get_apis()
    if not end:
        end = datetime.datetime.now().strftime('%Y-%m-%d')
        print(end)
    df = ts.bar(code,conn=api,freq='D',start_date=start,end_date=end)
    df.to_excel('data/'+code+'.xls')


def getData():
    filename = "300333.csv"
    df = pd.read_csv(filename)
    date = df['date']
    print(date)
    # df1=df.drop(0)
    #print(df1)
    df1 = df.set_index('date')
    #print(df.index.values)
    print(df1)


def getData():
    filename = "300333.csv"
    # df=pd.read_csv(filename,index_col='date')
    df = pd.read_csv(filename)
    print(df['date'].values)
    #new_date= datetime.datetime(df['date'].values)
    #
    # not work
    #date_list=[datetime.datetime.strptime(x,"%Y-%m-%d")for x in df['date'].values]
    #上面的可以，下面是另一种方法

    pd_date = pd.DatetimeIndex(df['date'].values)

    #print(date_list)

    df['date'] = pd_date
    print(df)
    new_df = df.set_index('date')
    print("*" * 20)
    print(new_df.index)
    print(new_df.ix[0])


if __name__ == "__main__":
    GetstockData('600609','2016-01-01')
    print('done')