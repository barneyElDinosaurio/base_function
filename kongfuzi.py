#-*-coding=utf-8-*-
import requests
from spider.header_toolkit import getheader
import random,time
def send(phone):
    session=requests.Session()
    session.get('https://login.kongfz.com')
    time.sleep(random.random()*5)
    # phone=
    url="https://login.kongfz.com/Pc/Ajax/sendMobileCheckCode"
    headers=getheader()
    print headers
    del headers['Cookie']
    data={'mobile':phone,'bizType':'2'}
    # headers1={}
    r=session.post(url=url,data=data,headers=headers)
    print r.status_code
    print r.text
    try:
        if r.json().get('status')=='true':
            print "work"
            return True
        if r.json().has_key('errInfo'):
            print r.json().get('errInfo')
            print "not work"
            time.sleep(random.random()*60*5)
            return False
    except Exception as e:
        print e
        return False

def main():
    while 1:
        send()
        time.sleep(60)
if __name__ == '__main__':
    main()