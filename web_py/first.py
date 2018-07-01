# -*-coding=utf-8-*-

__author__ = 'Rocky'
'''
http://30daydo.com
Email: weigesysu@qq.com
'''
import web


urls = (
    '/','Index'
)

class Index(object):

    def GET(self):
        return 'hello world'

if __name__ == '__main__':
    web.application(urls,globals()).run()