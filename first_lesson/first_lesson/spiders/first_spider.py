import scrapy
import time
from first_lesson.items import FirstLessonItem

class FirstSpider(scrapy.Spider):
    name='dmoztools'
    allowed_domains=['dmoztools.net']
    start_urls=[
        "http://www.dmoztools.net/Computers/Programming/Languages/Python/Books/",
        #"http://www.dmoztools.net/Computers/Programming/Languages/Python/Resources/"
    ]

    def parse(self, response):
        #filename=response.url.split('/')[-2]+'.html'
        print 'Header',response.headers
        #print "Got it"
        #time.sleep(5)
        #with open(filename,'w') as f:
            #f.write(response.body)
        for sel in response.xpath('//div[@class="site-title"]'):
            item=FirstLessonItem()
            #link=sel.xpath('.//div[@class="title-and-desc"]/a/@href').extract()
            title=sel.xpath('text()').extract()[0]
            #esc=sel.xpath('text()').extract()
            #print title,link,desc
            #print '\n'
            item['title']=title
            yield item
            #print '\n'