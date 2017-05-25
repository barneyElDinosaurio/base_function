# -*-coding=utf-8-*-
__author__ = 'Rocky'
'''
http://30daydo.com
Contact: weigesysu@qq.com
'''
import itchat,datetime,re

def testcase1():
    id='@5493580a22c9ba5db849ba33d0911d3d'
    content=datetime.datetime.now().strftime("%H:%M:%S")
    itchat.auto_login(hotReload=True)
    #itchat.auto_login()
    itchat.send(content,toUserName='filehelper')
    account=itchat.get_friends(u'wwwei')
    print account
    print type(account)
    for i in account:
        #print type(i)
        #print i
        if i[u'PYQuanPin']==u'wwwei':
            print i['UserName']
            #print i
    #itchat.send(content, toUserName=id)

    print 'done'

def testcase2():
    itchat.auto_login(hotReload=True)
    print itchat.get_friends()


testcase1()
