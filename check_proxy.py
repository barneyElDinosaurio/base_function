
# -*-coding=utf-8-*-
# @Time : 2018/8/21 17:19
# @File : check_proxy.py

# -*-coding=utf-8-*-
# @Time : 2018/7/27 15:21
# @File : proxy.py
import requests
import time
import logging

logger = logging.getLogger('info_logger')

def get_proxy( retry=50):

    proxyurl = 'http://{}:8081/dynamicIp/common/getDynamicIp.do'.format()
    for i in range(1, retry + 1):
        try:
            r = requests.get(proxyurl, timeout=5)
        except Exception as e:
            logger.error('获取代理错误：{}'.format(e))
            logger.error('Failed to get proxy ip, retry {}'.format(i))
            time.sleep(1)

        else:
            js = r.json()
            proxyServer = {'http':'http://{0}:{1}'.format(js.get('ip'), js.get('port'))}
            return proxyServer


url = 'http://www.szcredit.com.cn/web/GSZJGSPT/QyxyDetail.aspx?rid=ff86d6dce2ee483bb2b2f852cc2cb1b1&cid=9144030079921798XW'
import requests
proxy = get_proxy()
r=requests.get(url='http://www.szcredit.com.cn/web/GSZJGSPT/QyxyDetail.aspx?rid=ff86d6dce2ee483bb2b2f852cc2cb1b1&cid=9144030079921798XW',headers={'User-Agent':'android/Firefox'},proxies=proxy)
print(r.status_code)
print(r.text)