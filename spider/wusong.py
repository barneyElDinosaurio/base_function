# -*-coding=utf-8-*-
# @Time : 2018/8/29 14:27
# @File : wusong.py
import requests
from urllib import parse

# url="https://www.itslaw.com/api/v1/caseFiles?startIndex={}&countPerPage=20&sortType=1&conditions=wsFeature%2B1%2B15%2B%E5%A4%A9%E5%90%8C%E7%A0%81"
# url='https://www.itslaw.com/api/v1/caseFiles?startIndex=20&countPerPage=20&sortType=1&conditions=reason%2B2099%2B1%2B%E6%B0%91%E9%97%B4%E5%80%9F%E8%B4%B7%E7%BA%A0%E7%BA%B7'
url = 'https://www.itslaw.com/api/v1/caseFiles?startIndex=400&countPerPage=20&sortType=1&conditions=region%2B2%2B6%2B%E5%A4%A9%E6%B4%A5%E5%B8%82'
headers = {
    'Host': 'www.itslaw.com',
    'Connection': 'keep-alive',
    'Cache-Control': 'no-cache',
    'Accept': 'application/json, text/plain, */*',
    'Pragma': 'no-cache',
    'If-Modified-Since': 'Mon, 26 Jul 1997 05:00:00 GMT',
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
    'Referer': 'https://www.itslaw.com/search?searchMode=judgements&sortType=1&conditions=wsFeature%2B1%2B15%2B%E5%A4%A9%E5%90%8C%E7%A0%81&searchView=text',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'zh,en;q=0.9,en-US;q=0.8',
    # 'Cookie':'gr_user_id=6d1aaff1-563e-445c-816f-2a1f3a598639; showSubSiteTip=false; gr_session_id_8d9004219d790ea8=a9980804-2800-4ce3-940d-f6b6adc06e99; gr_session_id_8d9004219d790ea8_a9980804-2800-4ce3-940d-f6b6adc06e99=true; Hm_lvt_bc6f194cb44b24b9f44f1c8766c28008=1535452372,1535452372,1535559016,1535522445; Hm_lvt_e496ad63f9a0581b5e13ab0975484c5c=1535452372,1535452372,1535559016,1535522445; LXB_REFER=www.baidu.com; Hm_lpvt_e496ad63f9a0581b5e13ab0975484c5c=1535522513; Hm_lpvt_bc6f194cb44b24b9f44f1c8766c28008=1535522513; sessionId=d77b4063-3dbe-471b-8b96-eaea43009e15; _t=3fc00b4b-72f2-44bf-82f6-32fc00ccf3a7; subSiteCode=bj'
}


def search_all():
    r = requests.get(url, headers=headers)
    data = r.json()
    for i in data.get('data').get('searchResult').get('judgements'):
        # print(i.get('id'),' '.join(i.get('keywords')))
        kw_list = i.get('keywords')
        print(kw_list)


def search_kw(kw):
    base_url='https://www.itslaw.com/api/v1/caseFiles?startIndex=0&countPerPage=20&sortType=1&conditions=searchWord'
    # url = 'caseFiles?startIndex=0&countPerPage=20&sortType=1&conditions=litigant+3044439+1+{}'.format(kw.strip())
    concat_word = '+{}+1+{}'.format(kw,kw)
    url=parse.quote(concat_word)

    visit_url=base_url+url
    print(visit_url)
    # url='https://www.itslaw.com/api/v1/caseFiles?startIndex=0&countPerPage=20&sortType=1&conditions=searchWord%2B360%2B1%2B360'
    headers = {
        'Host': 'www.itslaw.com', 'Connection': 'keep-alive', 'Cache-Control': 'no-cache',
         'Accept': 'application/json,text/plain,*/*', 'Pragma': 'no-cache',
         'If-Modified-Since': 'Mon,26Jul199705:00:00GMT',
         'User-Agent': 'Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/67.0.3396.99Safari/537.36',
         'Referer': 'https://www.itslaw.com/search?searchMode=judgements&sortType=1&conditions=litigant%2B3044439%2B1%2B%E6%B7%B1%E5%9C%B3%E5%B8%82%E8%85%BE%E8%AE%AF%E7%94%B5%E5%95%86%E4%BF%A1%E6%81%AF%E6%8A%80%E6%9C%AF%E6%9C%89%E9%99%90%E5%85%AC%E5%8F%B8&searchView=text',
         'Accept-Encoding': 'gzip,deflate,br', 'Accept-Language': 'zh,en;q=0.9,en-US;q=0.8',
         'Cookie': 'gr_user_id=6d1aaff1-563e-445c-816f-2a1f3a598639;showSubSiteTip=false;LXB_REFER=mail.126.com;Hm_lvt_bc6f194cb44b24b9f44f1c8766c28008=1535559016,1535522445,1535549915,1535549974;Hm_lvt_e496ad63f9a0581b5e13ab0975484c5c=1535559016,1535522445,1535549915,1535549974;Hm_lpvt_bc6f194cb44b24b9f44f1c8766c28008=1535550638;Hm_lpvt_e496ad63f9a0581b5e13ab0975484c5c=1535550638;_u=dda0bd31-449f-4774-9120-29f0d4437fbf;_i=869e23cb-d931-4f5e-b711-86fc6e33fae7;_t=3fc00b4b-72f2-44bf-82f6-32fc00ccf3a7;subSiteCode=bj;gr_session_id_8d9004219d790ea8=f24458b3-df5d-4842-944b-de46297dbd7f;gr_session_id_8d9004219d790ea8_f24458b3-df5d-4842-944b-de46297dbd7f=true;_p=44f09cbd-1a82-4fb1-834c-b796584c6028;sessionId=2e1b2dee-8805-4396-a612-9eacd5da81f7'}
    print(visit_url)
    r = requests.get(visit_url, headers=headers)

    try:
        print(r.text)
        data = r.json()
    except Exception as e:
        print(e)
    else:
        for i in data.get('data').get('searchResult').get('judgements'):
            # print(i.get('id'),' '.join(i.get('keywords')))
            # kw_list = i.get('keywords')
            # print(kw_list)
            print(i)


kw = '腾讯'
search_kw(kw)
