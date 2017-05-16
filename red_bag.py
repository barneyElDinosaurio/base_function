# -*-coding=utf-8-*-
__author__ = 'Rocky'
from uiautomator import device as d


def zhifubao():
    while 1:
        if d(text=u'再来一次').wait.exists(timeout=10000):
            d(text=u'再来一次').click()


def QQ():
    while 1:
        # d(scrollable=True).scroll.to(text=u'红包')
        #d(scrollable=True).scroll.backward(steps=100)
        if d(text=u'红包').exists:
            print "find one"


if __name__ == "__main__":
    # zhifubao()
    QQ()