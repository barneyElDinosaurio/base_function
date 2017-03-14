# -*-coding=utf-8-*-
__author__ = 'Rocky'
import sys,time
import tushare as ts

DATA_GETTING_FLAG="#"
def basic_usage():
    df=ts.get_today_all()
    print df[df['code']=='000006']
    #print df.to_excel('tets.xls')
    #print df[df['code']=='000006']


def getNewStock():
    df= ts.new_stocks()
    df.to_excel('new_stock.xls')

def _write_console():
    sys.stdout.write(DATA_GETTING_FLAG)
    sys.stdout.flush()

def main():
    #basic_usage()
    #getNewStock()
    for i in range(20):
        _write_console()
        time.sleep(2)

if __name__=='__main__':

    main()