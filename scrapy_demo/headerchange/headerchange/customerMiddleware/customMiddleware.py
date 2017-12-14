#-*-coding=utf-8-*-
from scrapy.contrib.downloadermiddleware.useragent import UserAgentMiddleware

class CustomerUserAgent(UserAgentMiddleware):
    def process_request(self, request, spider):
        ua='HELLO World?????????'
        request.headers.setdefault('User-Agent',ua)
