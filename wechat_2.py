# -*-coding=utf-8-*-
# 接上段程序
# 通过该命令安装该API： pip install itchat
import itchat
import os
# 通过该命令安装该API： pip install NetEaseMusicApi
from NetEaseMusicApi import interact_select_song

#with open('stop.mp3', 'w') as f: pass
def close_music():
    #os.startfile('stop.mp3')
    print "MP3"


@itchat.msg_register(itchat.content.TEXT)
def music_player(msg):
    if msg['ToUserName'] != 'filehelper':
        return
    if msg['Text'] == u'关机':
        itchat.send(u'你的macbook准备关机', 'filehelper')
    if msg['Text'] == u'帮助':
        itchat.send(u'帮助信息', 'filehelper')
    else:
        itchat.send(u'请输入正确的指令', 'filehelper')
        #itchat.send(interact_select_song(msg['Text']), 'filehelper')


HELP_MSG = u"我是rocky小秘书"
itchat.auto_login(True)
itchat.send(HELP_MSG, 'filehelper')
itchat.run(debug=True)