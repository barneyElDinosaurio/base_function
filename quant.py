# -*-coding=utf-8-*-
__author__ = 'xda'
import tushare as ts


def quanshan():
    #Failed
    ts.set_token('de0596189f600d1dc59c509e5b6a1387e4e29cb6225697a25ef9d5d2a425d854')
    ts.get_token()
    mt = ts.Market()
    print mt
    df = mt.TickRTSnapshot(securityID='000001.XSHE')
    print df


def getIndustry():
    df = ts.get_area_classified()
    df.to_csv('area.csv', encoding='gbk')
    print df


def main():
    getIndustry()


main()