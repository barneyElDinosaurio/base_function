# -*-coding=utf-8-*-
# @Time : 2018/8/29 14:27
# @File : wusong.py
import requests
# url="https://www.itslaw.com/api/v1/caseFiles?startIndex={}&countPerPage=20&sortType=1&conditions=wsFeature%2B1%2B15%2B%E5%A4%A9%E5%90%8C%E7%A0%81"
# url='https://www.itslaw.com/api/v1/caseFiles?startIndex=20&countPerPage=20&sortType=1&conditions=reason%2B2099%2B1%2B%E6%B0%91%E9%97%B4%E5%80%9F%E8%B4%B7%E7%BA%A0%E7%BA%B7'
url='https://www.itslaw.com/api/v1/caseFiles?startIndex=400&countPerPage=20&sortType=1&conditions=region%2B2%2B6%2B%E5%A4%A9%E6%B4%A5%E5%B8%82'
headers = {
'Host':'www.itslaw.com', 
'Connection':'keep-alive', 
'Cache-Control':'no-cache', 
'Accept':'application/json, text/plain, */*', 
'Pragma':'no-cache', 
'If-Modified-Since':'Mon, 26 Jul 1997 05:00:00 GMT', 
'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36', 
'Referer':'https://www.itslaw.com/search?searchMode=judgements&sortType=1&conditions=wsFeature%2B1%2B15%2B%E5%A4%A9%E5%90%8C%E7%A0%81&searchView=text', 
'Accept-Encoding':'gzip, deflate, br', 
'Accept-Language':'zh,en;q=0.9,en-US;q=0.8', 
# 'Cookie':'gr_user_id=6d1aaff1-563e-445c-816f-2a1f3a598639; showSubSiteTip=false; gr_session_id_8d9004219d790ea8=a9980804-2800-4ce3-940d-f6b6adc06e99; gr_session_id_8d9004219d790ea8_a9980804-2800-4ce3-940d-f6b6adc06e99=true; Hm_lvt_bc6f194cb44b24b9f44f1c8766c28008=1535452372,1535452372,1535559016,1535522445; Hm_lvt_e496ad63f9a0581b5e13ab0975484c5c=1535452372,1535452372,1535559016,1535522445; LXB_REFER=www.baidu.com; Hm_lpvt_e496ad63f9a0581b5e13ab0975484c5c=1535522513; Hm_lpvt_bc6f194cb44b24b9f44f1c8766c28008=1535522513; sessionId=d77b4063-3dbe-471b-8b96-eaea43009e15; _t=3fc00b4b-72f2-44bf-82f6-32fc00ccf3a7; subSiteCode=bj'
}

r = requests.get(url,headers=headers)
data = r.json()
for i in data.get('data').get('searchResult').get('judgements'):
    # print(i.get('id'),' '.join(i.get('keywords')))
    kw_list = i.get('keywords')
    print(kw_list)