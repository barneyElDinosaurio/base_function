# -*-coding=utf-8-*-
__author__ = 'Rocky'
import tushare as ts
def basic_usage():
    df=ts.get_today_all()
    print df[df['code']=='000006']
    #print df.to_excel('tets.xls')
    #print df[df['code']=='000006']

def quanshan():
    ts.set_broker('htzq',user='xxxxx',passwd='xxxxx')
    ts.get_broker()
    htzq=ts.TraderAPI('htzq')
    htzq.login()
    info=htzq.baseinfo()
    print info

def main():
    #basic_usage()
    quanshan()


if __name__=='__main__':
    main()