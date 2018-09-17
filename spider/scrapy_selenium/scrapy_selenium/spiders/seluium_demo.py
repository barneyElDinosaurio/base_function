# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request
from scrapy_selenium.items import ScrapySeleniumItem

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
        # print(response.text)
        # for node in response.xpath('//div[@class="quote"]'):
        #     print(node.xpath('.//span[@itemprop="text"]/text()').extract_first())
        #     print('')
        for sel in response.css('ul.gl-warp.clearfix > li.gl-item'):
            item = ScrapySeleniumItem()
            name = sel.css('div.p-name').xpath('string(.//em)').extract_first()
            price = sel.css('div.p-price i::text').extract_first()
            try:
                remark = sel.xpath('.//div[(@class="p-commit" or @class="p-comm")]').xpath('string(.)').extract_first()
                if remark:
                    remark = remark.strip()
            except:
                remark = None
            try:
                price = float(price)
            except:
                price = price

            # 自营
            # shop=sel.css('div.p-shopnum span::text').extract_first()

            # 出版社

            publish = sel.css('div.p-shopnum a::text').extract_first()
            if publish is None:
                publish = sel.css('div.p-shop a::text').extract_first()
            # if shop is None:
            #     shop=sel.css('div.p-shopnum a::text').extract_first()
            #     publish=None

            item['name'] = name
            item['price'] = price
            item['remark'] = remark
            item['publish'] = publish
            # item['shop']=shop
            yield item