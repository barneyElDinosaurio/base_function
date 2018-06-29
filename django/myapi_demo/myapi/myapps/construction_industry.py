# -*-coding=utf-8-*-
import requests
from lxml import etree


def crawl(name):
    url = 'http://113.108.219.40/Dop/Open/PersonPunishmentList.aspx'
    data = {'__EVENTTARGET': '',
            '__EVENTARGUMENT': '',
            'ctl00$ContentPlaceHolder1$txtPersonName': name,
            'ctl00$ContentPlaceHolder1$txtIdNum': '',
            'ctl00$ContentPlaceHolder1$Button1': '搜索'}
    headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
               'Accept-Encoding': 'gzip,deflate',
               'Accept-Language': 'zh,en;q=0.9,en-US;q=0.8',
               'Cache-Control': 'no-cache',
               'Connection': 'keep-alive',
               # 'Content-Length': '6287',
               'Content-Type': 'application/x-www-form-urlencoded',
               # 'Cookie': 'UM_distinctid=1641b08da9a800-0e1bb87bdc335a-601a147a-1fa400-1641b08da9b2b9;CNZZDATA1261062804=671075873-1529461922-%7C1530090507;ASP.NET_SessionId=tuxjcy2h3lp12igblod32oia',
               'Host': '113.108.219.40',
               'Origin': 'http://113.108.219.40', 'Pragma': 'no-cache',
               'Referer': 'http://113.108.219.40/Dop/Open/PersonPunishmentList.aspx', 'Upgrade-Insecure-Requests': '1',
               'User-Agent': 'Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/67.0.3396.99Safari/537.36'}

    p = requests.post(url=url, headers=headers, data=data)
    if p.status_code == 200:
        return p
    else:
        return None


def run(name):
    # name = '何洁'
    r = crawl(name)
    ret = []

    if r is not None:
        response = etree.HTML(r.text)
        person_list = response.xpath('//table[@class="data-list"]/tr')
        if len(person_list) > 1:
            for item in person_list[1:]:
                item_dict = {}
                try:
                    name = item.xpath('.//td')[0].xpath('.//a/text()')[0].strip()
                except:
                    name = item.xpath('.//td')[0].xpath('.//text()')[0].strip()

                try:
                    name_url = item.xpath('.//td')[0].xpath('.//a/@href')[0].strip()
                except:
                    name_url = None

                try:
                    punish_file = item.xpath('.//td')[1].xpath('.//a/text()')[0].strip()
                except:
                    punish_file = None

                try:
                    punish_file_url = item.xpath('.//td')[1].xpath('.//a/@href')[0].strip()
                except:
                    punish_file_url = None

                try:
                    punish_institution = item.xpath('.//td')[2].xpath('.//span/text()')[0].strip()
                except:
                    punish_institution = None

                punish_date = item.xpath('.//td')[3].xpath('.//text()')[0].strip()

                item_dict['name'] = name
                item_dict['person_detail_url'] = name_url
                item_dict['punish_file'] = punish_file
                item_dict['punish_file_url'] = punish_file_url
                item_dict['punish_institution'] = punish_institution
                item_dict['punish_date'] = punish_date

                ret.append(item_dict)

    return ret

