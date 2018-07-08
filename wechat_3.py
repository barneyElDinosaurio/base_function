# -*-coding=utf-8-*-
import itchat

'''
itchat.auto_login()
#name='filehelper'
name='distantance'

itchat.send("hello file helper",toUserName=name)
'''


@itchat.msg_register(itchat.content.TEXT)
def text_reply(msg):
    #return msg['Text']+u',真好玩'
    my_msg = u'帅哥给我发个红包好吗? '
    print(msg['FromUserName'])
    return my_msg


itchat.auto_login()
all_user = itchat.search_friends()
print(all_user)
itchat.run()
