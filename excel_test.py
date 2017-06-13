# -*-coding=utf-8-*-
__author__ = 'Rocky'
import xlrd, xlwt
from xlutils.copy import copy
import pandas as pd


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
    print df
'''
file="python_excel_test.xls"
rb=xlrd.open_workbook(file)
copy_excel(rb,1,'asking')
'''
#modify_excel2()
#运行通过
#add_sheet()

#getCodeFromExcel("ownstock.xls")

save_id()