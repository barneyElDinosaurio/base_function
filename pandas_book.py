from pandas import Series,DataFrame
import pandas as pd
import numpy as np

def format_line(obj=""):
    print "*"*20
    print obj

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

if __name__=="__main__":
    #series_1()
    #dataframe_1()
    #dataframe_op()
    #sort_test()
    #sort_test2()
    #dup_index()
    #df_static()
    #multi_index()
    Store()