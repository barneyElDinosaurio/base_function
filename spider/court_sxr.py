# -*-coding=utf-8-*-
# @Time : 2018/9/3 15:12
# @File : court_sxr.py
# @author : chenjinwei

import re
import requests
from scrapy.selector import Selector
import base64

name = '黎东初'
cidno = '360423197812221010'

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip,deflate', 'Accept-Language': 'zh,en;q=0.9,en-US;q=0.8',
    'Cache-Control': 'no-cache', 'Connection': 'keep-alive',
    'Host': 'zxgk.court.gov.cn', 'Pragma': 'no-cache', 'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/67.0.3396.99Safari/537.36'
}

session = requests.session()
session.headers.update(headers)


# 编码
def img_to_b64(img_path):
    with open(img_path, 'rb') as f:
        base64_data = base64.b64encode(f.read())
    return base64_data.decode('utf-8')


# 接口识别验证码
def crack_code(img_path):
    img_b64 = img_to_b64(img_path)  # 转为base64编码
    img_dict = {'img': img_b64}
    res = requests.post('http://10.18.4.211:5001/Captcha_api', data=img_dict, verify=False, timeout=5)
    return res.text


url = 'http://zxgk.court.gov.cn/shixin/index_form.do'
get_session = session.get(url=url)

response = Selector(text=get_session.text)
image_url = response.xpath('//img[@id="captchaImg"]/@src').extract_first()
cap_id = re.search('captchaId=(.*?)&', image_url).group(1)
full_image_url = 'http://zxgk.court.gov.cn/shixin/' + image_url

# 下载图片
try:
    png_strean = session.get(full_image_url)
    with open('test.png', 'wb') as f:
        f.write(png_strean.content)

except Exception as e:
    print(e)

# 调用接口识别验证码
code = crack_code('test.png')

# 填充post data
payload = {
    'pName': name,
    'pCardNum': cidno,
    'pProvince': '0',
    'pCode': code,
    'captchaId': cap_id,
}

failure_count = 0

# 如设置过大的测试次数，需要添加代理，否则易被封IP
total_count = 10
loop_count = total_count

# 测试成功率
while loop_count > 0:
    post_url = 'http://zxgk.court.gov.cn/shixin/findDis'
    try:
        resp_content = session.post(url=post_url, data=payload)
    except Exception as e:
        print(e)
    else:
        response = Selector(text=resp_content.text)
        t = response.xpath('//table[@class="Resultlist"]/tbody/tr')[1:]

        if not t:
            failure_count += 1

        for i in t:
            ret = i.xpath('string(.)').extract_first().strip()
            print(ret)

    loop_count = loop_count - 1

print('Failure rate >>> {}%'.format((failure_count / total_count) * 100))
