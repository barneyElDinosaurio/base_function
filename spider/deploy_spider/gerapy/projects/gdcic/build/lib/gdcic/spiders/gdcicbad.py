# -*- coding: utf-8 -*-
import scrapy
import logging
from gdcic.items import GdcicItem


class GdcicbadSpider(scrapy.Spider):
    name = 'gdcicbad'
    # allowed_domains = ['gdcic.gov.cn']
    # start_urls = ['http://gdcic.gov.cn/']
    logging.basicConfig(
        filename='log.txt',
        format='%(levelname)s: %(message)s',
        level=logging.INFO
    )

    def __init__(self):
        self.url = 'http://www.gdcic.gov.cn/ZWGK/twoPublicity2.aspx'

        self.headers = {
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
            'Accept-Encoding': 'gzip,deflate', 'Accept-Language': 'zh-CN,zh;q=0.9', 'Cache-Control': 'no-cache',
            'Content-Type': 'application/x-www-form-urlencoded',
            # 'Cookie': 'ASP.NET_SessionId=frligxryjpbj1lcysuyjnsm5;safedog-flow-item=C4561395C7DD6F855EF23B1359E436C8;_gscu_168135779=29454859uql03320;_gscbrs_168135779=1;_gscs_168135779=t2945796867hghw29|pv:4',
            'Host': 'www.gdcic.gov.cn', 'Origin': 'http://www.gdcic.gov.cn', 'Pragma': 'no-cache',
            'Proxy-Connection': 'keep-alive', 'Referer': 'http://www.gdcic.gov.cn/ZWGK/twoPublicity2.aspx',
            'Upgrade-Insecure-Requests': '1',
            'User-Agent': 'Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/67.0.3396.87Safari/537.36'}

        self.data = {
            '__VIEWSTATE': 'ZSVLVvMKsZluFyGJS/0yIEml2K0u7pCRC9WkB5Y6g3bNF9vLmH+ewhEZH7PhZuaZ/Yj7647otLuFkvVpQREpo1+0mmisl4HO42wRh49dxO7mortFQag2z350knrap1uTs/JLpFiLl/d/3F00OW/SAO9RqXiGIOEcFLab6nOdd4B6thmhit9ys4c1pLfe2izvBgo2F1OAxhr4HC3547+1iw1E3iavpv/y/Q/jYklOU8optqBl',
            '__EVENTTARGET': 'ctl00$ctl00$WebContent$WebContent$pager$netPager',
            '__EVENTARGUMENT': '1',
            '__EVENTVALIDATION': 'XFvf/bUPh5zJYoC1AOVZqx69GGxsgg49pBnmwVk3tTpHDJiX8XZgPmbKWWlRG4hUkQJ6N4TiPNdWW8B0l86med6bN96y7ig3FiHgVDWgg1LSiZ/mkuqBBde5nug1ism5PTA7Fw==',
            'ctl00$ctl00$WebContent$WebContent$TextBox1': '',
            'ctl00$ctl00$WebContent$WebContent$TextBox2': ''
        }

    def start_requests(self):
        for i in range(1, 4):
            self.data['__EVENTARGUMENT'] = str(i)
            yield scrapy.FormRequest(url=self.url, formdata=self.data, headers=self.headers, dont_filter=True)

    def parse(self, response):
        host_url ='http://www.gdcic.gov.cn'
        node = response.xpath('//div[@class="twopub-scroll"]/table/tr')
        for i in node[1:]:
            item = GdcicItem()
            content = i.xpath('.//td')

            item['enterprise'] = content[0].xpath('.//text()').extract_first()
            try:
                item['enterprise_link']= host_url+ content[0].xpath('.//a/@href').extract_first()
            except:
                item['enterprise_link']=None

            item['punish_file'] = content[1].xpath('.//text()').extract_first()
            item['punish_file_no'] = content[2].xpath('.//span/text()').extract_first()
            item['punish_dept'] = content[3].xpath('.//text()').extract_first()
            item['punish_date'] = content[4].xpath('.//text()').extract_first()
            yield item
