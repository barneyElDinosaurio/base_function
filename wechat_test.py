# -*-coding=utf-8-*-
import itchat, time, re
from itchat.content import *


@itchat.msg_register([TEXT])
def text_reply(msg):
    match = re.search(u'年', msg['Text']).span()
    if match:
        itchat.send((u'那我就祝你鸡年大吉吧'), msg['FromUserName'])


@itchat.msg_register([PICTURE, RECORDING, VIDEO, SHARING])
def other_reply(msg):
    itchat.send((u'那我就祝你鸡年大吉吧'), msg['FromUserName'])


itchat.auto_login(enableCmdQR=True, hotReload=True)
itchat.run()
