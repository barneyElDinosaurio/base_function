#-*-coding=utf-8-*-
#__author__ = 'rocky'
from uiautomator import device as d
#from uiautomator import Device
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
def liuliang():
    d(text='签到').click()

if __name__=="__main__":
    #base_info()
    #op_test()

    print "Go"
    #t=Device('0331416080186')
    print "Start"

    #print t.info

    '''
    d.press.home()
    d.swipe(200,500,700,500)

    #d.press.home()
    click_test()
    '''
    liuliang()


