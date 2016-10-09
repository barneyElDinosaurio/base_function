#-*-coding=utf-8-*-
__author__ = 'rocky'
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def excel_op():
    #print df.head(20)
    #df=df.fillna(0)
    #print df.head(20)
    #code=df[[u'代码',u'资金发生数']]
    #print(code)
    #print type(code)
    #code=code.fillna(0)
    #print code
    '''
    for i in code:
        if i is not None:
            print int(i)
    '''
    num=0
    '''
    for i in df:
        print num,
        print i
        print type(i)
        num=num+1
    '''
    '''
    for index,row in df.iterrows():
        #print row[u'代码'],row[u'资金发生数']
        print "index**********************"
        print index
        print "row************************"
        print row
    '''
def search():
    #遍历
    df=pd.read_excel("huatai2.xls")
    input_m=0.0
    output_m=0.0
    for index, row in df.iterrows():
        if row[u'业务']==u'存入':
            each_input=row[u'资金发生数']
            print u"存入",
            print each_input
            input_m=input_m+each_input
            #print type(money)
        if row[u'业务']==u'取出':
            each_output=row[u'资金发生数']
            print u"取出",
            print each_output
            #print type(money)
            output_m=output_m+each_output

    print "Sumary is %f" %(input_m-output_m)





def del_row():
    #删除某一行
    df=pd.read_excel("huatai2.xls")
    #可以获得某个index
    #print df[df[u'代码']==300141].index
    print df

    #print "\nAfter drop"
    df.drop(df[df[u'代码']==300141.0].index,inplace=True)
    new_df=df.drop(df[df[u'代码']==300141.0].index)
    #print ndf
    print df

def replace_test():
    #替换值

    df=pd.read_excel("huatai2.xls")
    s1=pd.Series(['a','b','c','d','e'])
    #print s1
    s2=pd.Series(['1','2','3','4','5'])
    #print s2

    s3=s1.replace(1,'k')
    #print s1
    #print s3
    print df
    df.replace(['20160722',u'卖出成交',2431.0,u'棕榈股份',13.00,300.0,3891.10,3905.71,u'自动'],['20160722','0','0','0',0,0,0,0,'0'],inplace=True)
    #df.replace(['20160722'],['20160725','0','0','0',0,0,0,0,'0'],inplace=True)
    print df

def replace_test2():
    temp='''
    E11 | R_31 | E21 | M_xxx |
    E12 | R_21 | E51 | M_relation |
    E33 | R_21 | E51 | M_yyy |
    E44 | R_41 | E46 | M_relation
    '''
    split_data=temp.split('|')
    t=[]
    for i in split_data:
       t.append(i.strip())
    print t
    data=[]
    result=[]
    l=len(t)/4
    print l
    for j in range(l):
        for k in range(l):
            data.append(t[4*k+j])
            #data.append(t[4*(j+1)+k])
            #data.append(t[4*(j+2)+k])
            #data.append(t[4*(j+3)+k])
    print data
    a=pd.Series(data[0:4])
    b=pd.Series(data[4:8])
    c=pd.Series(data[8:12])
    d=pd.Series(data[12:16])
    #print a
    print a
    print b
    print c
    print d
    print "fist"
    first=pd.DataFrame({'Entry1':a,'Relation':b,'Entry2':c,'Meta':d})
    print first
    new_df=pd.DataFrame({'Entry1':pd.Series(data[0:4]),'Relation':pd.Series(data[4:8]),'Entry2':pd.Series(data[8:12]),'Meta':pd.Series(data[12:16]),})
    #狗日的，一个冒号写成逗号搞了我一个下午。
    print "new_df"
    print new_df
    print "loc[0]"
    print new_df.loc[0]
    print "type of loc is "
    print type(new_df.loc[0])
    #a=pd.Series()
    print "log[2] entery2: "
    print new_df.loc[2,['Entry2']]

    #E511

    print new_df.at[2,"Entry2"]
    #at 是获取出来的值,而且是单个的值
    print "get row 1 2"
    print new_df[1:3]
    #only row 1,2

    print "\t iloc[2]"
    print new_df.iloc[2]
    print type(new_df.iloc[2])

    new_df['Entry1'].replace('E11','EE',inplace=True)
    print new_df

    #sclice
    print "\nsclice"
    print new_df.iloc[[1,3]]
    print "partion"
    print new_df.iloc[:,[1,3]]
    print "select one value" #r21
    print new_df.iloc[1,3]

    alist=['E11','E12']

    print new_df.isin(alist)


def data_type_test():
    data = pd.Series([0.25, 0.5, 0.75, 1.0],index=['a','b','c','d'])
    print data
    print data.values
    print type(data.values)
    print data.index
    for i in data.index:
        print i
    print data[1:3]
    print data['b']
    print df.columns
    print df[u'代码']
    #print df['col0']
    population_dict = {'California': 38332521,
               'Texas': 26448193,
               'New York': 19651127,
               'Florida': 19552860,
               'Illinois': 12882135}
    population=pd.Series(population_dict)
    print population
    print population["California"]
    new_df= pd.DataFrame(population,columns=['population'])
    print new_df
    data = [{'a': i, 'b': 2 * i}
    for i in range(3)]
    print data
    pd.DataFrame(data)
    ind = pd.Index([2, 3, 5, 7, 11])
    print ind

    print ind[::2]


    #print


def win_or_lost():
    l=len(df.index)

    for i in range(l):
        '''
        if item[u'业务'] == u'买入成交':
            item[u'资金发生数']=item[u'资金发生数']*-1
        '''
        #print item
        if df.iloc[i][u'业务']==u'买入成交':
            df.iloc[i][u'资金发生数']=-1*df.iloc[i][u'资金发生数']
            #print new_line
    #print df

    print df
    #print df
    #df.loc[df[u'业务']==u'买入成交',u'资金发生数']=0
    #print df

def select_function():
    df=pd.DataFrame(np.random.randn(6,4),columns=list("ABCD"))
    print df

    print df[(df.D>0) & (df.C>0)]


def get_static1():
    df=pd.read_excel("huatai2.xls")
    count=df[u'名称'].value_counts()
    print count
    plt=count.plot(kind='bar').get_figure()
    plt.savefig("plot.png")

def get_static2():
    df=pd.read_excel("huatai2.xls")
    high= df[df[u'资金发生数']>10000]
    #print high
    g=df.groupby(u'资金发生数')
    #print g.first()
    print g.last()

def my_data():
    #测试我自己的数据
    df=pd.read_excel("huatai2.xls")
    hsdq = df[df[u'名称']==u'和顺电气']
    print hsdq
    hsdq[hsdq[u'业务']==u'买入成交']

def string_op():
    a='ABCdEFG'
    s=pd.Series(list(a))
    print s.str.lower()
    print s.str.upper()
    print "Now s is : "
    print s
    print s.str.len()

def string_op2():
    a=['a1','b2','c3','d4','e5']
    s=pd.Series(a)
    print s
    print s.str.extract('\w(\d)')

def string_op3():
    # use regalar type
    s=pd.Series(["a1","dd2","1ww2","ef2","t1","g2","h7","ood","444","12er","1qa",np.nan,"z9"])
    print s
    p=r'[a-z][0-9]'
    print s.str.contains(p)
#excel_op()
#del_row()
#search()
#replace_test()
#data_type_test()
#excel_op()
#del_row()
#search()
#win_or_lost()
#replace_test2()
#select_function()
#get_static1()
#get_static2()
#my_data()
#string_op2()
string_op3()