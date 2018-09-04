# -*-coding=utf-8-*-
# @Time : 2018/9/3 15:12
# @File : court_sxr.py
# @author : chenjinwei
import copy
import re
import shutil
import requests
from scrapy.selector import Selector
import base64
import time
import pymongo


name = '广元'
# cidno = '360423197812221010'
cidno = ''

headers = {
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
    'Accept-Encoding': 'gzip,deflate', 'Accept-Language': 'zh,en;q=0.9,en-US;q=0.8',
    'Cache-Control': 'no-cache', 'Connection': 'keep-alive',
    'Host': 'zxgk.court.gov.cn', 'Pragma': 'no-cache', 'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0(WindowsNT6.1;WOW64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/67.0.3396.99Safari/537.36'
}

session = requests.session()
session.headers.update(headers)

mongo = pymongo.MongoClient('10.18.6.102',27018)
doc = mongo['spider']['zgfsxr']

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
print(get_session.text)

response = Selector(text=get_session.text)
image_url = response.xpath('//img[@id="captchaImg"]/@src').extract_first()
# print(image_url)
cap_id = re.search('captchaId=(.*?)&', image_url).group(1)
full_image_url = 'http://zxgk.court.gov.cn/shixin/' + image_url

failure_count = 0
server_failure = 0
# 如设置过大的测试次数，需要添加代理，否则易被封IP
total_count = 1
loop_count = total_count

while loop_count > 0:
    # 下载图片
    try:
        png_strean = session.get(full_image_url)
        with open('test.png', 'wb') as f:
            f.write(png_strean.content)

    except Exception as e:
        print(e)

    # 调用接口识别验证码
    code = crack_code('test.png')

    # 识别出错后重新下载新的图片
    if code == '100' or code == '101':
        print('接口端识别失败或者有干扰线')
        server_failure += 1
        try:
            shutil.copy('test.png', 'shibie{}.png'.format(int(time.time())))
        except Exception as e:
            print(e)

        continue

    # 填充post data
    payload = {
        'pName': name,
        'pCardNum': cidno,
        'pProvince': '0',
        'pCode': code,
        'captchaId': cap_id,
    }

    post_url = 'http://zxgk.court.gov.cn/shixin/findDis'

    try:
        resp_content = session.post(url=post_url, data=payload)
        # print(resp_content.text)
        hold_session = copy.deepcopy(session)

    except Exception as e:
        print(e)
        print('提交post数据异常')
        continue

    else:
        if '验证码错误或验证码已过期' in resp_content.text:
            print('识别的验证码和网站不一样')
            try:
                shutil.copy('test.png', 'yanzhen{}.png'.format(int(time.time())))
            except Exception as e:
                print(e)

            failure_count += 1
            continue

        response = Selector(text=resp_content.text)

        t = response.xpath('//table[@class="Resultlist"]/tbody/tr')[1:]
        try:
            count_number = int(re.search('共(\d+)条', resp_content.text).group(1))
        except Exception as e:
            print(e)
            count_number = 0

        # 第一页的情况
        for i in t:
            # ret = i.xpath('string(.)').extract_first().strip()
            case_id = i.xpath('.//a[@class="View"]/@id').extract_first()
            detail_url = 'http://zxgk.court.gov.cn/shixin/disDetail?id={}&pCode={}&captchaId={}'.format(case_id, code,
                                                                                                        cap_id)
            session.headers.update({'X-Requested-With': 'XMLHttpRequest'})
            s4 = session.get(url=detail_url)
            ret = s4.json()
            print(ret)
            doc.insert(ret)


        # 第二页到后面的情况

        if count_number > 10:
            total_page = count_number//10

            for p in range(2,total_page+1):
                payload_page = {
                    'currentPage':str(p),
                    'pName': name,
                    'pCardNum': cidno,
                    'pProvince': '0',
                    'pCode': code,
                    'captchaId': cap_id,
                }

                try:
                    # 需要把header remove
                    resp_content = hold_session.post(url=post_url, data=payload)
                    print(resp_content.text)
                except Exception as e:
                    print(e)
                    print('提交post数据异常')
                    continue

                else:
                    if '验证码错误或验证码已过期' in resp_content.text:
                        print('识别的验证码和网站不一样')
                        try:
                            shutil.copy('test.png', 'yanzhen{}.png'.format(int(time.time())))
                        except Exception as e:
                            print(e)

                        failure_count += 1
                        continue

                    response = Selector(text=resp_content.text)
                    t = response.xpath('//table[@class="Resultlist"]/tbody/tr')[1:]

                    for i in t:
                        # ret = i.xpath('string(.)').extract_first().strip()
                        case_id = i.xpath('.//a[@class="View"]/@id').extract_first()
                        detail_url = 'http://zxgk.court.gov.cn/shixin/disDetail?id={}&pCode={}&captchaId={}'.format(
                            case_id, code,
                            cap_id)
                        session.headers.update({'X-Requested-With': 'XMLHttpRequest'})
                        s4 = session.get(url=detail_url)
                        ret = s4.json()
                        print(ret)
                        doc.insert(ret)




print('Failure rate >>> {}%'.format((failure_count / total_count) * 100))
print('Server Failure rate >>> {}%'.format((server_failure / total_count) * 100))
