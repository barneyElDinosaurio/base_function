#-*-coding=utf-8-*-
from pandas import Series,DataFrame
import pandas as pd
import numpy as np
import datetime

def format_line(obj=""):
    print "*"*20
    print obj


def format_line():
    print "*"*20


def series_1():
    s=Series(['a','b','c','d','e'])
    print s
    print type(s)
    print type(s.index)
    print s.index
    print s.values

    r=Series([1,3,5,7,9],index=['A','B','C','D','E'])
    print r
    print r.index

    print r[['A','D']]

    print r[r>5]
    print r>5

    print 'AN' in r
    format_line()
    dict={"Username":"Rocky","Sex":"Male","Country":"China","Langauge":"Chinese"}
    t=Series(dict)
    print t

    t.index.name="Info"
    t.name="Database"
    format_line()
    print t

    t.index=['Mingzhi',"Sex","Country","Languge"]
    format_line(t)


    i=t.index
    format_line(i)

    #i[1]="A"

    j=r.reindex(['E','D','C',"B",'A'])
    format_line(j)


def dataframe_1():
    data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'], 'year': [2000, 2001, 2002, 2001, 2002],'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
    df=pd.DataFrame(data)
    print df
    format_line()
    print df['year']
    format_line()
    print df.year
    format_line()
    print df.ix[2]

    df['year']=2019
    format_line()
    print df

    df['year']=[2012,2999,1111,333,1212]
    format_line(df)

    new_series=Series(['New york',"Los Angles",'Golden state',"Huston",'Nevada'],index=[0,1,3,2,4])
    df['state']=new_series
    format_line(df)

    df['colleage']=['UC',"LA","HK","YL","BK"]
    format_line(df)

    format_line(df.values)

    print 5 in df.index

    format_line(df)
    col=['year','state','pop']
    new_df=df.reindex(columns=col)
    format_line(new_df)

def dataframe_op():
    df=pd.DataFrame(np.arange(16).reshape(4,4),index=["Ohio",'Colorado','Utah','New york'],columns=['One','Two','Three','Four'])
    format_line(df)
    df['Two']
    print df

    #format_line(df['Two'])
    #format_line(df[['Two','One']])
    #format_line(df[:2])
    #format_line(df[df['Three']>5])
    #format_line(df[0:2])

    #format_line()

    new_df= df>10
    print new_df
    #df[df>10]=0
    print df
    print df.ix[2]

    print df.ix[df.Three>5,:3]

def sort_test():
    obj=Series(np.arange(5),index=['a','d','b','c','e'])
    print obj
    print obj.sort_index()

    obj2=DataFrame(np.arange(16).reshape(4,4),index=['3','4','6','1'],columns=['f','b','c','d'])
    format_line(obj2)

    print obj2.sort_index()

    format_line()

    print obj2.sort_index(axis=1)

    format_line()

    obj2.ix[2,'f']=99
    print obj2
    print obj2.sort_values(by='f')

def sort_test2():
    s=Series([7,6,7,-5,2,6,4,0])
    print s.rank()
    print s.rank(method="first")


def dup_index():
    df=DataFrame(np.arange(16).reshape(4,4),index=['a','a','b','c'])
    print df
    print df.ix['a']

def df_static():
    df=pd.DataFrame(np.arange(25).reshape(5,5),index=['a','c','d','f','g'],columns=['A','B','C','D','E'])
    print df
    print df.sum(axis=1)
    print df.describe()

def multi_index():
    #df=DataFrame(np.random.randn(10),index=[['a','b','a','c','a','b','c','a','a','c'],
    df=DataFrame(np.random.randn(16).reshape(4,4),index=[['a','b','a','c'],
                                     [1,2,3,2]],columns=[["Hot","Cold","Hot","Cold"],["Good","Bad","Bad","Good"]])
    print df
    print df.index
    df2=DataFrame(np.arange(16).reshape(4,4),index=["1",'2','3','4'],columns=["A","B","C","D"])
    print df2
    print df2.icol(2)
    print df2.ix['3']
    print df2['C']

def Store():
    df=pd.read_table('sample.txt',sep=',',header=None)
    print df

def merge_op():
    df1=DataFrame({'key':['b','b','a','c','a','a','b'],'data_one':range(7)})
    df2=DataFrame({'key':['a','b','e'],'data_tow':[7,4,99]})
    print df1
    format_line()
    print df2
    format_line()
    print pd.merge(df1,df2,how='outer')
    #print df_m
    #print pd.merge(df1,df2,how='outer')
    #print df3

def data_aggre():
    #排序测试
    df=pd.DataFrame({"Weather":["Cold","HOT","WARM","HOT","HOT"],"Place":["HK","BJ","NY","LD","SZ"],"Price":[12,2,3,12,6]})
    df1=pd.DataFrame({"Weather":["Cold","HOT","WARM","HOT","HOT"],"Place":["HK","BJ","NY","LD","SZ"],"Price":[12,2,3,12,6]})
    df2=pd.DataFrame({"Weather":["HOT","WARM"],"Place": ["JJ","JP"],"Price":[99,77]})
    print df
    group_weather=df.groupby('Price')
    i =0
    for name, group in group_weather:
        i=i+1
        print "Group",i,name
        print group
    #df2=pd.DataFrame()
    print pd.concat([df1,df2])
    #print df3
    print df
    df1.append(df2)
    print df1
    print df1.index.values[1]

def type_test():
    df=pd.DataFrame({"Weather":["Cold","HOT","WARM","HOT","HOT"],"Place":["HK","BJ","NY","LD","SZ"],"Price":[12,2,3,12,6]})
    print type(df)
    print df[:2]
    print type(df[:2])

def date_op():
    start=pd.date_range('2015-01-01',periods=50)
    #print start
    print type(start)

    date_list=[datetime.datetime(2017,1,1),datetime.datetime(2017,1,2),datetime.datetime(2017,1,3),datetime.datetime(2017,1,4)]
    df=pd.DataFrame(np.random.randn(4),index=date_list)
    print df
    print df.index[2]
    format_line()

    s_x=pd.date_range('2000-1-1',periods=1000)
    df_x=pd.DataFrame(np.arange(2000).reshape(1000,2),index=s_x)
    print df_x
    print df_x.ix['2002/09/24']
    print df_x[1]
    #这样子就会选择的列
    #选取行就用ix
    print df_x.ix['2001-09']

def cumsum_test():
    a=np.array([[1,2,3],[4,5,6]])
    b=np.cumsum(a)

    print a
    print b

if __name__=="__main__":
    #series_1()
    #dataframe_1()
    #dataframe_op()
    #sort_test()
    #sort_test2()
    #dup_index()
    #df_static()
    #multi_index()
    #Store()
    #merge_op()
    #data_aggre()
    #type_test()
    #date_op()
    cumsum_test()