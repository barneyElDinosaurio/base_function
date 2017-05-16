# -*-coding=utf-8-*-
__author__ = 'Rocky'
import pandas as pd
import datetime
from pandas import DataFrame


def getData():
    filename = "300333.csv"
    df = pd.read_csv(filename)
    date = df['date']
    print date
    # df1=df.drop(0)
    #print df1
    df1 = df.set_index('date')
    #print df.index.values
    print df1


def getData():
    filename = "300333.csv"
    # df=pd.read_csv(filename,index_col='date')
    df = pd.read_csv(filename)
    print df['date'].values
    #new_date= datetime.datetime(df['date'].values)
    #
    # not work
    #date_list=[datetime.datetime.strptime(x,"%Y-%m-%d")for x in df['date'].values]
    #上面的可以，下面是另一种方法

    pd_date = pd.DatetimeIndex(df['date'].values)

    #print date_list

    df['date'] = pd_date
    print df
    new_df = df.set_index('date')
    print "*" * 20
    print new_df.index
    print new_df.ix[0]


if __name__ == "__main__":
    getData()