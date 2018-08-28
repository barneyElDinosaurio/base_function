# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request


class SeluiumDemoSpider(scrapy.Spider):
    name = 'seluium_demo'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/65.0.3325.162 Safari/537.36',
        'Referer': 'http://quotes.toscrape.com/'}

    def start_requests(self):
        url = 'https://search.jd.com/Search?keyword=python&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=python&page=1&s=112&click=0'
        yield Request(url=url, headers=self.headers,dont_filter=True)

    def parse(self, response):
        base_url = 'https://search.jd.com/Search?keyword=python&enc=utf-8&qrst=1&rt=1&stop=1&vt=2&wq=python&page={}&s=112&click=0'
        for i in range(1, 10,2):
            yield Request(url=base_url.format(str(i)), callback=self.parse_item, headers=self.headers,dont_filter=True)

    def parse_item(self, response):
        print(response.text)
        # for node in response.xpath('//div[@class="quote"]'):
        #     print(node.xpath('.//span[@itemprop="text"]/text()').extract_first())
        #     print('')