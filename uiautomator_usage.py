# -*-coding=utf-8-*-
__author__ = 'Rocky'

from uiautomator import device as d
#注意这个device是小写的

def basic_usage():

    info= d.info
    print info
    print type(info)
    for i in info:
        #print v
        print i,info[i]

    print info['currentPackageName']

def operation_usage():

    '''
    d.press.home()
    result=d(text=u'设置').wait.exists(timeout=10000)
    #单位是毫秒, 如果timeout还没有找到，就返回false
    print "next"
    if result:
        print "You press setting"
    else:
        print "You don't touch any thing"
    '''

    '''
    if d(text=u'设置').exists:
        d(text='WLAN').click()
    else:
        print "move"
    '''

    #d(text=u'显示').click()
    #支持unicode

    d(scrollable=True).scroll(steps=3)

if __name__=="__main__":
    #basic_usage()
    operation_usage()