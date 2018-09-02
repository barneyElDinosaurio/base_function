# -*-coding=utf-8-*-
import hashlib
import json
import logging
import time
import requests
from scrapy.downloadermiddlewares.retry import RetryMiddleware
from scrapy.downloadermiddlewares.useragent import UserAgentMiddleware
from headerchange import config
import random
# from headerchange.user_agents import agents
from fake_useragent import UserAgent
from scrapy.utils.response import response_status_message

class CustomUserAgentMiddleware(UserAgentMiddleware):

    def process_request(self, request, spider):

        agent = UserAgent()
        request.headers["User-Agent"] = agent.random


class CustomProxyMiddleware(object):
    def process_request(self, request, spider):
        proxy = self.get_proxy()
        request.meta['proxy'] = proxy

    def get_proxy(self,retry=5):
        proxyurl = 'http://{}:8081/dynamicIp/common/getDynamicIp.do'.format(config.proxyip)
        count = 0
        for i in range(retry):
            try:
                r = requests.get(proxyurl, timeout=10)
            except Exception as e:
                logging.error(e)
                count += 1
                logging.error('代理获取失败,重试' + str(count))
                time.sleep(1)

            else:
                js = r.json()
                proxyServer = 'http://{0}:{1}'.format(js.get('ip'), js.get('port'))
                return proxyServer

        return None


class CustomRetryMiddleware(RetryMiddleware):
    def process_response(self, request, response, spider):
        if request.meta.get('dont_retry', False):
            return response

        if response.status in self.retry_http_codes:
            reason = response_status_message(response.status)
            return self._retry(request, reason, spider) or response

        # customiz' here
        # content = response.text
        if not response.xpath('//table[@class="list_2_tab"]/tbody/tr'):

            proxy = self.get_proxy()
            logging.info('>>>>>>>> 替换代理重试')
            request.meta['proxy']=proxy

            return self._retry(request, response.body, spider) or response

        return response

    def get_proxy(self,retry=5):
        proxyurl = 'http://{}:8081/dynamicIp/common/getDynamicIp.do'.format(config.proxyip)
        count = 0
        for i in range(retry):
            try:
                r = requests.get(proxyurl, timeout=10)
            except Exception as e:
                logging.error(e)
                count += 1
                logging.error('代理获取失败,重试' + str(count))
                time.sleep(1)

            else:
                js = r.json()
                proxyServer = 'http://{0}:{1}'.format(js.get('ip'), js.get('port'))
                return proxyServer

        return None