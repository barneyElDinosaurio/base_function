#-*-coding=utf-8-*-
__author__ = 'rocky'
import pandas as pd
import numpy as np
def excel_op():
    df=pd.read_excel("mystocks.xls")
    #rint df.head(20)
    df=df.fillna(0)
    #print df.head(20)
    code=df[[u'代码',u'资金发生数']]
    #print(code)
    #print type(code)
    code=code.fillna(0)
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
    for index,row in df.iterrows():
        print row[u'代码'],row[u'资金发生数']
excel_op()