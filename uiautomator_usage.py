# -*-coding=utf-8-*-
__author__ = 'Rocky'
import time, os
import subprocess
from uiautomator import device as d
# 注意这个device是小写的

def basic_usage():
    '''
    info= d.info
    print info
    print type(info)
    for i in info:
        #print v
        print i,info[i]
    '''
    while True:
        info = d.info
        print info['currentPackageName']
        time.sleep(10)
        # com.taobao.taobao
        #com.jingdong.app.mall
        #com.suning.mobile.ebuy
        #com.kingpoint.gmcchh
        #com.jd.jrapp
        #com.tencent.mm


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

    # d(text=u'显示').click()
    #支持unicode

    d(scrollable=True).scroll(steps=3)


def launch_app():
    cmd = 'adb shell am start -n com.kingpoint.gmcchh/.ui.home.StartUpActivity'
    # os.system(cmd)
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    print p.stdout.read()

    if d(text=u'我的信箱').wait.exists(timeout=10000):
        d(text=u'关闭').click()

    if d(text=u'版本更新').wait.exists(timeout=15000):
        d(text=u'取消').click()
    else:
        print "Latest version"
    d(scrollable=True).scroll.to(text=u'签到赢话费')
    d(text=u'签到赢话费').click()
    print "Go"
    time.sleep(3)
    d(text=u'签到规则').click()
    #d(text=u'')
    #print result
    print "Done"


def darcy_test():
    pass


def wechat():
    cmd = 'adb shell am start -n com.tencent.mm/.ui.LauncherUI'
    # os.system(cmd)
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    print p.stdout.read()


def sunning():
    cmd = 'adb shell am start -n com.suning.mobile.ebuy/.base.host.InitialActivity'
    # os.system(cmd)
    p = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    print p.stdout.read()
    time.sleep(5)
    d(text=u'领云钻').click()
    time.sleep(8)
    d(text=u'打卡领云钻').wait.exists(timeout=10000)
    print "Done"


def text_search():
    if d(text=u'流量口令').wait.exists(timeout=10000):
        print "Found"
    else:
        print "Not found"


def step_by_step():
    # d(text=u'打卡领云钻').wait.exists(timeout=10000)
    #print "done"
    #result = d(text=u'').exists
    #print result
    pass


if __name__ == "__main__":
    step_by_step()
    # basic_usage()
    #operation_usage()
    #launch_app()
    #wechat()
    #sunning()
    text_search()