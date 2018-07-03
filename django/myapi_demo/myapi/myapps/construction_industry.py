# -*-coding=utf-8-*-
import requests
from lxml import etree
import re
import random
from PIL import Image


def crawl(url, data):
    headers = {
        'User-Agent': 'Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/67.0.3396.99Safari/537.36'
    }

    p = requests.post(url=url, headers=headers, data=data)
    if p.status_code == 200:
        return p
    else:
        return None


def people_bad_behavious(name):
    # name = '何洁'
    url = 'http://113.108.219.40/Dop/Open/PersonPunishmentList.aspx'
    data = {'__EVENTTARGET': '',
            '__EVENTARGUMENT': '',
            'ctl00$ContentPlaceHolder1$txtPersonName': name,
            'ctl00$ContentPlaceHolder1$txtIdNum': '',
            'ctl00$ContentPlaceHolder1$Button1': '搜索'}
    r = crawl(url, data)
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


def company_bad_behavious(name):
    url = 'http://113.108.219.40/Dop/Open/EnterprisePunishmentList.aspx'
    data = {'__EVENTTARGET': '',
            '__EVENTARGUMENT': '',
            'ctl00$ContentPlaceHolder1$txtOrgName': name,
            'ctl00$ContentPlaceHolder1$txtOrgCode': '',
            'ctl00$ContentPlaceHolder1$Button1': '搜索'
            }

    r = crawl(url, data)
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
                    project_name = item.xpath('.//td')[1].xpath('.//a/text()')[0].strip()
                except:
                    project_name = None

                try:
                    project_name_url = item.xpath('.//td')[1].xpath('.//a/@href')[0].strip()
                except:
                    project_name_url = None

                try:
                    punish_institution = item.xpath('.//td')[2].xpath('.//span/text()')[0].strip()
                except:
                    punish_institution = None

                punish_date = item.xpath('.//td')[3].xpath('.//text()')[0].strip()

                item_dict['name'] = name
                item_dict['company_detail_url'] = name_url
                item_dict['project_name'] = project_name
                item_dict['project_name_url'] = project_name_url
                item_dict['punish_institution'] = punish_institution
                item_dict['punish_date'] = punish_date

                ret.append(item_dict)

    return ret


def company_backpay(name):
    print(name)
    url = 'http://113.108.219.40/Dop/Open/EnterprisePunishmentList.aspx'
    data = {'__EVENTTARGET': '',
            '__EVENTARGUMENT': '',
            'ctl00$ContentPlaceHolder1$txtOrgName': name,
            'ctl00$ContentPlaceHolder1$txtOrgCode': '',
            'ctl00$ContentPlaceHolder1$Button1': '搜索'
            }

    r = crawl(url, data)
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
                    project_name = item.xpath('.//td')[1].xpath('.//a/text()')[0].strip()
                except:
                    project_name = None

                try:
                    project_name_url = item.xpath('.//td')[1].xpath('.//a/@href')[0].strip()
                except:
                    project_name_url = None

                try:
                    punish_institution = item.xpath('.//td')[2].xpath('.//span/text()')[0].strip()
                except:
                    punish_institution = None

                punish_date = item.xpath('.//td')[3].xpath('.//text()')[0].strip()

                item_dict['name'] = name
                item_dict['company_detail_url'] = name_url
                item_dict['project_name'] = project_name
                item_dict['project_name_url'] = project_name_url
                item_dict['punish_institution'] = punish_institution
                item_dict['punish_date'] = punish_date

                ret.append(item_dict)

    return ret


def company_blacklist(name):
    url = 'http://113.108.219.40/Dop/Open/EnterpriseBlackList.aspx'

    data = {'ctl00$ContentPlaceHolder1$txtOrgName': name,
            'ctl00$ContentPlaceHolder1$txtOrgCode': '',
            'ctl00$ContentPlaceHolder1$Button1': '搜索'
            }

    r = crawl(url, data)
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
                    blacklist_type = item.xpath('.//td')[1].xpath('.//a/text()')[0].strip()
                except:
                    blacklist_type = None

                try:
                    blacklist_detail = item.xpath('.//td')[1].xpath('.//a/@href')[0].strip()
                except:
                    blacklist_detail = None

                try:
                    identify_institution = item.xpath('.//td')[2].xpath('.//span/text()')[0].strip()
                except:
                    identify_institution = None

                identify_date = item.xpath('.//td')[3].xpath('.//text()')[0].strip()

                item_dict['enterprise'] = name
                item_dict['enterprise_detail_url'] = name_url
                item_dict['blacklist_type'] = blacklist_type
                item_dict['blacklist_detail'] = blacklist_detail
                item_dict['identify_institution'] = identify_institution
                item_dict['identify_date'] = identify_date

                ret.append(item_dict)

    return ret


def accident(name):
    session = requests.Session()

    url = 'http://113.108.219.40/Dop/Search/SafetyAccidentList.aspx'
    headers = {
        'Cookies': 'UM_distinctid=1641b08da9a800-0e1bb87bdc335a-601a147a-1fa400-1641b08da9b2b9; CNZZDATA1261062804=671075873-1529461922-%7C1530090507; ASP.NET_SessionId=qqeonscclhhb5txvuxtonh1j',
        'Referer': 'http://113.108.219.40/Dop/Search/SafetyAccidentList.aspx',
        'User-Agent': 'Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/67.0.3396.99Safari/537.36'
    }
    r = session.get(url, headers=headers)
    response = etree.HTML(r.text)
    val = response.xpath('//input[@id="__VIEWSTATE"]/@value')[0]

    ts = random.random() * 1000
    code_url = 'http://113.108.219.40/Dop/CheckCode.aspx?codemark={}'.format(ts)

    s1 = session.get(code_url, headers=headers)
    with open('code.gif', 'wb') as f:
        f.write(s1.content)

    im = Image.open('code.gif')
    im.show()
    # code = input('input the code:')

    post_data = {
        '__EVENTTARGET': '',
        '__EVENTARGUMENT': '',
        'ctl00$ContentPlaceHolder1$txtPRJName': name,
        'ctl00$ContentPlaceHolder1$txtCheckCode': '',
        # 'ctl00$ContentPlaceHolder1$hidCheckCodeMark': str(ts),
        'ctl00$ContentPlaceHolder1$hidCheckCodeMark': '',
        'ctl00$ContentPlaceHolder1$btnSearch': '搜索'
    }

    post_data['__VIEWSTATE'] = val
    r = session.post(url=url, headers=headers, data=post_data)
    # r = crawl(url, post_data)
    print(r.text)

    # company_bad_behavious('广东英海建筑工程有限公司')


# accident('桥头')
