# -*- coding: utf-8 -*-
"""
Created on Fri Aug 31 14:58:31 2018

@author: liuxinyu
"""

"""
接口返回
1.成功识别则返回验证码具体内容
2.识别失败: 101
3.验证码中含有干扰线: 100
"""



import base64
import requests


def img_to_b64(img_path):
    with open(img_path,'rb') as f:
        base64_data=base64.b64encode(f.read())
    return base64_data.decode('utf-8')

img_path = '1536032291.png' #图片路径

img_b64 = img_to_b64(img_path) #转为base64编码
img_dict={'img':img_b64}
res=requests.post('http://10.18.4.211:5001/Captcha_api',data=img_dict,verify=False,timeout=5)
print(res.text)
