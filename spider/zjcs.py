# -*-coding=utf-8-*-

# @Time : 2018/9/12 16:52
# @File : zjcs.py
import json

import requests

headers = {
    'Accept': 'application/json,text/javascript,*/*;q=0.01',
    'Accept-Encoding': 'gzip,deflate',
    'Accept-Language': 'zh,en;q=0.9,en-US;q=0.8', 'Cache-Control': 'no-cache',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json;charset=UTF-8', 'Host': '222.218.31.5:889',
    'Origin': 'http://222.218.31.5:889', 'Pragma': 'no-cache',
    'Referer': 'http://222.218.31.5:889/epoint-web-zwdt/nxzjjg/pages/agencyResource/resourceLibrary.html',
    'User-Agent': 'Mozilla/5.0 AppleWebKit/537.36(KHTML,likeGecko)Chrome/67.0.3396.99Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}

url = 'http://222.218.31.5:889/epoint-web-zwdt/rest/XT_Interface_ZJCS/XT_GetAgencyList'
page_detail = {'CurrentPageIndex': '1', 'PageSize': '10', 'area': '', 'servicetype': '', 'searchagencyname': '',
               'zzlb': '',
               'zzdj': '', 'special': ''}

js_page_detail = json.dumps(page_detail)
# print(js_page_detail)
formdata = {
    'ValidateData': 'epointoa@5Hq7cJgKyD_Ixe7M18iAPFMzIT0=@MTQ3MzY0ODAxOA==@E0AA0BB134F165CAFB19A736FF460742EE13B9DAA4165B2F1B9CAC9C8AB3E421',
    'paras': page_detail}
# print(formdata)
js=json.dumps(formdata)
print(js)
r = requests.post(url=url, headers=headers, json=formdata)
print(r.json())
