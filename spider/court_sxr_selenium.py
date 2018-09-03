# -*-coding=utf-8-*-
# @Time : 2018/9/3 14:28
# @File : court_sxr_selenium.py
import time
from selenium import webdriver
import base64
import requests
from PIL import Image


# 编码
def img_to_b64(img_path):
    with open(img_path, 'rb') as f:
        base64_data = base64.b64encode(f.read())
    return base64_data.decode('utf-8')


# 查询接口
def crack_code(img_path):
    img_b64 = img_to_b64(img_path)  # 转为base64编码
    img_dict = {'img': img_b64}
    res = requests.post('http://10.18.4.211:5001/Captcha_api', data=img_dict, verify=False, timeout=5)
    return res.text


# 验证码截图后放大到160*70
def capture_picture(driver, name):
    driver.get_screenshot_as_file('full.png')
    element = driver.find_element_by_id('captchaImg')
    left = int(element.location['x'])
    top = int(element.location['y'])
    right = int(element.location['x'] + element.size['width'])
    bottom = int(element.location['y'] + element.size['height'])

    im = Image.open('full.png')
    im = im.crop((left, top, right, bottom))
    im = im.resize((160, 70), Image.ANTIALIAS)
    im.save(name)


# 使用selenium输入数据
def main():

    # 失信人信息
    sxr_name = '黎东初'
    cidno = '360423197812221010'

    options = webdriver.ChromeOptions()
    options.add_argument(
        '--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36')
    driver = webdriver.Chrome(executable_path=r'D:\Python\selenium\chromedriver.exe',
                              chrome_options=options)
    driver.implicitly_wait(40)

    url = 'http://zxgk.court.gov.cn/shixin/index_form.do'
    driver.get(url)

    username = driver.find_element_by_id("pName")
    username.clear()
    username.send_keys(sxr_name)

    psd = driver.find_element_by_id("pCardNum")
    psd.clear()
    psd.send_keys(cidno)

    v_code = driver.find_element_by_id("pCode")
    v_code.clear()

    img_reflash = driver.find_element_by_id('captchaImg')
    img_reflash.click()
    time.sleep(1.5)

    capture_picture(driver, 'code.png')
    code = crack_code('code.png')
    v_code.send_keys(code)
    time.sleep(0.1)

    commit = driver.find_element_by_id("button")
    commit.click()
    time.sleep(5)

    count = 0

    while 1:
        handles = driver.window_handles
        driver.switch_to.window(handles[1])
        time.sleep(0.3)
        source = driver.page_source

        # 得到正确结果，退出, 否则继续尝试
        if '查询结果' in source:
            break

        driver.close()
        driver.switch_to.window(handles[0])

        v_code = driver.find_element_by_id("pCode")
        v_code.clear()

        img_reflash = driver.find_element_by_id('captchaImg')
        img_reflash.click()
        time.sleep(2.5)

        capture_picture(driver, '{}.png'.format(count))
        code = crack_code('{}.png'.format(count))
        v_code.send_keys(code)
        time.sleep(0.1)
        commit = driver.find_element_by_id("button")
        commit.click()
        time.sleep(3)
        count += 1

if __name__ == '__main__':
    main()
