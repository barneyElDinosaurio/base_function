#-*-coding=utf-8-*-
#__author__ = 'rocky'
from uiautomator import device as d
#from uiautomator import Device
import time
def base_info():
    '''
    for v,k in enumerate(d.info):
        print v,k
    '''
    info=d.info
    print type(info)
    print info

def click_test():
    d.click(371,1524)

def op_test():
    d.press.home()
    #d.screen.on()
<<<<<<< HEAD
def scroll_test():
    try:
        d(scrollable=True).scroll.to(text="Linksys_2G")
        d(text='Linksys_2G').click()
    except:
        print "Not found"
=======
def liuliang():
    d(text=u'全部').click()
    time.sleep(4)
    d(text=u'领流量').click()
    time.sleep(5)
    #这个签到好像找不到
    #d(text=u'签到').click()
    d.click(271,813)
    time.sleep(1)
    d.click(271,813)
    time.sleep(5)
    print "get liu liang"

>>>>>>> origin/master
if __name__=="__main__":
    #base_info()
    #op_test()

    print "Go"
    #t=Device('0331416080186')
    print "Start"

    #print t.info

<<<<<<< HEAD

    #d.press.home()
    #d.swipe(200,500,700,500)

    #d.press.home()
    #click_test()

    scroll_test()
=======
    '''
    d.press.home()
    d.swipe(200,500,700,500)

    #d.press.home()
    click_test()
    '''
    liuliang()

>>>>>>> origin/master

