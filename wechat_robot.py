# -*-coding=utf-8-*-

import requests
import itchat
def demo_1():
    KEY = '44ff23cd75de4d5dac225b64c6700b77'

    def get_response(msg):
        apiUrl = 'http://www.tuling123.com/openapi/api'
        data = {
            'key'    : KEY,
            'info'   : msg,
            'userid' : 'wechat-robot',
        }
        try:
            r = requests.post(apiUrl, data=data).json()
            return r.get('text')
        except:
            return

    @itchat.msg_register(itchat.content.TEXT)
    def tuling_reply(msg):
        defaultReply = 'I received: ' + msg['Text']
        reply = get_response(msg['Text'])
        return reply or defaultReply

    itchat.auto_login(hotReload=True)
    itchat.run()

from wxpy import *
def demo_2():
    bot = Bot()
    my_friends = bot.friends().search(city='东莞')
    # my_friends = bot.friends().search('邱富根')
    print(my_friends)

    for i in my_friends:
        i.send('微信机器人')

demo_1()
# demo_2()
