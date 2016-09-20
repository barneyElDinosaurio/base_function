# -*-coding=utf-8-*-
__author__ = 'Rocky'
import xlrd,xlwt
filename="python_excel_test.xls"
excel_file=xlwt.Workbook()
sheet=excel_file.add_sheet('2016')
row=0
col=0
ctype='string'
value='Rocky1'
xf=0
sheet.write(row,col,value)
excel_file.save(filename)