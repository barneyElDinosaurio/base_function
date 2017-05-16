__author__ = 'rocchen'
import xlrd

filename = "Book1.xls"
data = xlrd.open_workbook(filename)
table = data.sheets()[0]
stock_id = table.col_values(0)
for i in stock_id:
    print i