# -*-coding=utf-8-*-

# @Time : 2018/9/3 13:26
# @File : court_sxr.py
import re
import requests
import urllib.request
from scrapy.selector import Selector
from PIL import Image
import base64

headers1 = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; rv:11.0) like Gecko',
    'Referer': 'http://zxgk.court.gov.cn/shixin/new_index.html'
}
session = requests.Session()

session.headers.update(headers1)

def img_to_b64(img_path):
    with open(img_path, 'rb') as f:
        base64_data = base64.b64encode(f.read())
    return base64_data.decode('utf-8')

def crack_code(img_path):

    # img_path = 'test45.png'  # 图片路径

    img_b64 = img_to_b64(img_path)  # 转为base64编码
    img_dict = {'img': img_b64}
    res = requests.post('http://10.18.4.211:5001/Captcha_api', data=img_dict, verify=False, timeout=5)
    # print(res.text)
    return res.text

session.headers.update({'Referer':'http://zxgk.court.gov.cn/shixin/new_index.html'})

get_session=session.get(url='http://zxgk.court.gov.cn/shixin/new_index.html')

verfiy_code_url = 'http://zxgk.court.gov.cn/shixin/index_form.do'
# http://zxgk.court.gov.cn/zhixing/new_index.html
s1 = session.get(url=verfiy_code_url)
# print(s1.text)
response = Selector(text=s1.text)
image_url = response.xpath('//img[@id="captchaImg"]/@src').extract_first()
cap_id=re.search('captchaId=(.*?)&',image_url).group(1)

print(image_url)
full_image_url = 'http://zxgk.court.gov.cn/shixin/' + image_url
try:
    png_strean = session.get(full_image_url)
    with open('test.png','wb') as f:
        f.write(png_strean.content)

except Exception as e:
    print(e)

code=crack_code('test.png')
print(code)


payload={
    'pName':'黎东初',
    'pCardNum':'360423197812221010',
    'pProvince':'0',
    'pCode':code,
    'captchaId':cap_id,

}
post_url='http://zxgk.court.gov.cn/shixin/findDis'
try:
    s2=session.post(url=post_url)
    print(s2.status_code)
except Exception as e:
    print(e)

else:
    print(s2.text)

