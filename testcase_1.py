#-*-coding=utf-8-*-
#__author__ = 'rocky'
from uiautomator import Device as d
#from uiautomator import Device
def base_info():
    '''
    for v,k in enumerate(d.info):
        print v,k
    '''
    info=d.info
    print type(info)
    print info


def op_test():
    d.press.home()
    #d.screen.on()
if __name__=="__main__":
    #base_info()
    #op_test()

    print "Go"
    #t=Device('0331416080186')
    print "Start"

    #print t.info

    d.press.home()