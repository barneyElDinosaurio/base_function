# -*-coding=utf-8-*-
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.font_manager import FontProperties

font = FontProperties(fname=r"c:\windows\fonts\simsun.ttc", size=14)


def personal_money():
    baidu_current = 2619
    baidu_fix = 50000
    jd = 19284
    lujinsuo = 43998
    icbc = 455
    cmb = 77
    zhifubao = 0
    stock_ht = 53200
    stock_gj = 19112
    fund = 3515
    qq = 1000
    X = [baidu_current + baidu_fix, jd, lujinsuo, icbc, cmb, stock_ht, stock_gj, fund, qq]
    labels = [u'百度', u'京东', u'陆金所', u'工行', u'招行', u'华泰', u'国金', u'广发', u'QQ']
    plt.figure()
    plt.subplot(2, 1, 1)
    p = plt.pie(X,
                labels=labels,

                autopct='%1.1f'
                )
    print p
    # plt.show()
    print p[1]
    # 中文乱码设置
    for font in p[1]:
        font.set_fontproperties(mpl.font_manager.FontProperties(
            fname='C:/Windows/winsxs/amd64_microsoft-windows-font-truetype-simfang_31bf3856ad364e35_6.1.7600.16385_none_e417159f3b4eb1b7/simfang.ttf'))

    plt.subplot(2, 1, 2)
    x2 = [baidu_fix + baidu_current + jd + lujinsuo + icbc + cmb + qq, fund + stock_gj + stock_ht]
    print x2
    labels2 = [u'现金', u'股票']
    p2 = plt.pie(x2, labels=labels2,autopct='%1.1f')

    for font2 in p2[1]:
        font2.set_fontproperties(mpl.font_manager.FontProperties(
            fname='C:/Windows/winsxs/amd64_microsoft-windows-font-truetype-simfang_31bf3856ad364e35_6.1.7600.16385_none_e417159f3b4eb1b7/simfang.ttf'))

    plt.show()


personal_money()
