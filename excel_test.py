# -*-coding=utf-8-*-
__author__ = 'Rocky'
import xlrd, xlwt
from xlutils.copy import copy
import pandas as pd
import matplotlib.pyplot as plt

def write_excel():
    filename = "python_excel_test.xls"
    excel_file = xlwt.Workbook()
    sheet = excel_file.add_sheet('2016')
    row = 0
    col = 0
    ctype = 'string'
    value = 'Rocky1'
    xf = 0
    sheet.write(row, col, value)

    sheet2 = excel_file.add_sheet('2017')
    row = 0
    col = 0
    ctype = 'string'
    value = 'Rocky122'
    xf = 0
    sheet2.write(row, col, value)
    excel_file.save(filename)


def modify_excel():
    rb = xlrd.open_workbook("python_excel_test.xls")
    w = copy(rb)
    w.get_sheet(1).write(1, 1, "Hello")
    w.save('book2.xls')


def add_sheet():
    rb = xlrd.open_workbook("python_excel_test.xls")
    w = copy(rb)
    ws = w.add_sheet('new_sheet')
    ws.write(1, 1, "SS")
    w.save('new.xls')


def copy_excel(workbook, source_index, new_name):
    new_sheet = copy.copy(workbook.get_sheet(source_index))
    workbook._Workbook__worksheets.append(new_sheet)
    append_index = len(workbook._Workbook__worksheets) - 1
    workbook.set_active_sheet(append_index)
    workbook.get_sheet(append_index).set_name(new_name)


def getCodeFromExcel(filename):
    # 从excel表中获取代码
    df = pd.read_excel(filename)
    code_list = df[u'证券代码'].values
    for i in code_list:
        i = str(i)
        print type(i)
        print i.zfill(6)
        #print code_list


def modify_excel2():
    rb = xlrd.open_workbook("python_excel_test.xls")
    original_table = rb.sheets()[0]
    rows = original_table.nrows
    cols = original_table.ncols
    print rows, cols

    # w=copy(rb)
    #sheet=w.get_sheet(0)
    #w.save('book3.xls')


# 为了提取所有的testcase id
def save_id():
    df = pd.read_excel('2.xls',skiprows=[0])
    #print df.info()

    '''
    for i in range(len(df)):
        print str(df.iloc[i, 0]).strip(), ',',

    '''
def remove_use():
    l = [1,2,3,4]
    for i in l:
        if i != 4:
            l.remove(i)
    print l
def check_diff():
    df1=pd.read_excel('less1.xlsx')
    df2=pd.read_excel('more1.xlsx')
    print df1.info
    print df2.info
    print df1.dtypes
    print df2.dtypes
    id1=df1.icol(0).values
    id2=df2.icol(0).values
    #print id1
    #print id2
    ax1=list(id1)
    ax2=list(id2)
    for i in ax1:
        if i in ax2:
            ax2.remove(i)

    print ax2

    #print df


def profit_line():
    #df=pd.read_excel('d.xlsx',header=0,skiprows=[0])
    df=pd.read_excel('d.xlsx')
    print df[u'盈亏']
    #df.reset_index(level=None, drop=True, inplace=True, col_level=1, col_fill='')
    df.set_index(u'日期',inplace=True,drop=True)
    print df
    date_d,profit=df.index,df[u'盈亏'].values
    print type(profit)
    print 'type of date_d ',type(date_d)
    #date_d
    print "mean: ",df[u'盈亏'].mean()
    #print df[u'盈亏'].mean()
    print "count: ",df[u'盈亏'].count()
    print "description: ",df.describe()
    print "最大盈利: " ,df[u'盈亏'].max()
    print "发生在: ",df[df[u'盈亏']==df[u'盈亏'].max()].index.values[0]
    print "最大亏损: " ,df[df[u'盈亏']==df[u'盈亏'].min()].index.values[0]

    '''
    一些统计信息
    '''

    print "亏损多余1w的次数", df[df[u'盈亏']<-10000][u'盈亏'].count()
    print "盈利多余1w的次数", df[df[u'盈亏']>10000][u'盈亏'].count()

    #plt.plot(profit,'o')
    #plt.grid()
    '''
    x=range(1,len(profit)+1)
    plt.bar(x,profit,width=0.35)
    plt.show()
    '''
    '''
    plt.figure(1)
    plt.subplot(4,3,1)
    num=12
    l=len(profit)
    delta=l/12

    for i in range(num-1):
        plt.subplot(4,3,i+1)
        plt.plot(profit[delta*i:delta*(i+1)])
    plt.subplot(4,3,12)
    plt.plot(profit[delta*11:])
    plt.show()
    '''


    date_d1=date_d.map(lambda x:x.strftime("%Y-%m-%d"))
    print date_d1
    print type(date_d1)
    print type(profit)


    num=24
    l=len(profit)
    delta=l/num
    for i in range(num-1):
        #plt.subplot(4,3,i+1)
        plt.figure(i)
        plt.bar(date_d[delta*i:delta*(i+1)],profit[delta*i:delta*(i+1)])
        plt.grid()
        plt.title(str(i))
    #plt.subplot(4,3,12)
    plt.figure(num)
    plt.bar(date_d[delta*(num-1):],profit[delta*(num-1):])
    plt.grid()
    plt.title(str(num))
    plt.show()



#file="python_excel_test.xls"
#rb=xlrd.open_workbook(file)
#copy_excel(rb,1,'asking')

#modify_excel2()
#运行通过
#add_sheet()

#getCodeFromExcel("ownstock.xls")

#save_id()
#check_diff()
#remove_use()
profit_line()