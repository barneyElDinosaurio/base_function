# -*-coding=utf-8-*-
import requests

class GetAppInfo():

    def __init__(self):
        self.user_agent = "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)"
        self.header = {"User-Agent": self.user_agent}
        self.url='http://www.iapprank.com/'

    def getData(self):
        try:
            r=requests.get(url=self.url,headers=self.header)
            print r.status_code
            print r.text
            print 'done'
        except Exception , e:
            print e

def main():
    obj=GetAppInfo()
    obj.getData()


if __name__=='__main__':
    main()
