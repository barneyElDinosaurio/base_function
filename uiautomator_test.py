# -*-coding=utf-8-*-
#__author__ = 'rocky'
from uiautomator import device as d
#from uiautomator import Device
import time


def base_info():
    '''
    for v,k in enumerate(d.info):
        print(v,k)
    '''
    info = d.info
    print(type(info))
    print(info)


def click_test():
    d.click(371, 1524)


def op_test():
    d.press.home()
    #d.screen.on()


def scroll_test():
    try:
        d(scrollable=True).scroll.to(text="Linksys_2G")
        d(text='Linksys_2G').click()
    except:
        print("Not found")


def liuliang():
    d(text=u'全部').click()
    time.sleep(4)
    d(text=u'领流量').click()
    time.sleep(5)
    #这个签到好像找不到
    #d(text=u'签到').click()
    d.click(271, 813)
    time.sleep(1)
    d.click(271, 813)
    time.sleep(5)
    print("get liu liang")


def each_dianpu():
    mid_x = 1080 / 2
    #d.click(919,566)
    time.sleep(3)

    d.click(mid_x, 1868)
    #点击免费试用
    time.sleep(3)
    d.click(mid_x, 1311)
    time.sleep(2)
    d.click(mid_x, 1555)
    time.sleep(3)
    d.press.back()
    time.sleep(5)
    d.press.back()
    time.sleep(5)
    #返回到试用列表


def main():
    #base_info()



    #base_info()

    #op_test()

    print("Go")
    #t=Device('0331416080186')
    print("Start")

    #print(t.info)



    #d.press.home()
    #d.swipe(200,500,700,500)

    #d.press.home()
    #click_test()

    #scroll_test()

    '''
    d.press.home()
    d.swipe(200,500,700,500)

    #d.press.home()
    click_test()
    '''
    #liuliang()
    #d(text=u'数码科技').click()
    #if d(text=u'腾讯体育').exists:
    #print("Existed")
    #d.dump("hierarchy.xml")
    #d.swipe(500,1570,500,400)
    delta_each = 400
    time.sleep(3)

    for dragtime in range(20):
        print('dragtime')
        for i in range(3):
            d.click(919, 420 + i * delta_each)
            print('click')
            time.sleep(8)
            #each_dianpu()
            each_dianpu()
            time.sleep(8)
        d.swipe(919, 420 + delta_each * 3, 919, 400)
        time.sleep(5)


if __name__ == "__main__":
    main()



