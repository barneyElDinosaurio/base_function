#-*-coding=utf-8-*-
__author__ = 'rocky'
import pandas as pd
import numpy as np
df=pd.read_excel("huatai2.xls")


def excel_op():
    #rint df.head(20)
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

    #可以获得某个index
    #print df[df[u'代码']==300141].index
    #print df

    #print "\nAfter drop"
    ndf=df.drop(df[df[u'代码']==300141.0].index)
    print ndf


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
#excel_op()
#del_row()
#search()
win_or_lost()