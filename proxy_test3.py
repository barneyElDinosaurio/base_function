# -*-coding=utf-8-*-
import base64

import requests
import config

proxy = "http://proxy.asiainfo.com:8080"
proxy_type = "http"
proxy_auth_username = "wanglu"
proxy_auth_password = "ai@@119"

'''
            request.meta['proxy'] = conf.proxy

            # Use the following lines if your proxy requires authentication
            proxy_user_pass = conf.proxy_auth_username+":"+conf.proxy_auth_password
            # setup basic authentication for the proxy
            encoded_user_pass = base64.encodestring(proxy_user_pass)
            request.headers['Proxy-Authorization'] = 'Basic ' + encoded_user_pass
'''


def demo():
    proxy_user_pass = proxy_auth_username + ":" + proxy_auth_password
    # setup basic authentication for the proxy
    print(proxy_user_pass)
    encoded_user_pass = base64.encodestring(proxy_user_pass).strip()
    auth = 'Basic ' + encoded_user_pass
    headers = {
        'User-Agent': 'Mozilla 5.0 (Windows NT 6.1; Win64; x64) AppleWebKit 537.36 (KHTML, like Gecko) Chrome 62.0.3202.94 Safari 537.36',
        'Proxy-Authorization':auth
    }
    print(headers)
    proxies={proxy_type:proxy}
    url = 'http://members.3322.org/dyndns/getip'
    for _ in range(3):
        try:
            r = requests.get(url=url, headers=headers,proxies=proxies)
            print(r.text)
        except Exception as e:
            print(e)


demo()
