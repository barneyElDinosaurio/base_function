# -*-coding=utf-8-*-

__author__ = 'Rocky'
'''
http://30daydo.com
Email: weigesysu@qq.com
'''
import requests
import json
from lxml import etree
def getContent():
    url = 'http://quotes.money.163.com/f10/gdfx_000011.html'
    '''
    headers = {'Accept-Language': 'zh-CN,zh;q=0.9', 'Accept-Encoding': 'gzip,deflate,br', 'Host': 'sp0.baidu.com',
               'Accept': '*/*',
               'User-Agent': 'Mozilla/5.0(WindowsNT6.1;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/65.0.3325.162Safari/537.36',
               'Connection': 'keep-alive',
               'Cookie': 'BAIDUID=807FDFD8452E0BBE9D4E90BE4ACA3E48:FG=1;BIDUPSID=807FDFD8452E0BBE9D4E90BE4ACA3E48;PSTM=1510554299;MCITY=-340%3A;pgv_pvi=5560071168;H_PS_PSSID=1437_21116_18560_26350_26578_20929;PSINO=6',
               'Pragma': 'no-cache', 'Cache-Control': 'no-cache',
               'Referer': 'https://www.baidu.com/s?ie=utf-8&f=8&rsv_bp=0&rsv_idx=1&tn=baidu&wd=%E5%A4%B1%E4%BF%A1%E4%BA%BA&rsv_pq=ba070cee00021d68&rsv_t=af202PtBAFQNGpj0I7C5T4usPJQM4XwFNcLDD7LLLYIzLiejH%2Br66BFrgCg&rqlang=cn&rsv_enter=1&rsv_sug3=11&rsv_sug1=11&rsv_sug7=100&rsv_sug2=0&inputT=2625&rsv_sug4=2625'}
      '''
    headers = {'User-Agent':'Mozilla/5.0(WindowsNT6.1;Win64;x64)AppleWebKit/537.36(KHTML,likeGecko)Chrome/65.0.3325.162Safari/537.36'}
    r = requests.get(url, headers=headers)
    # js= json.loads(r.text)

    print r.text
    tree = etree.HTML(r.text)
    return r.text,tree

def main():
    getContent()


if __name__ == '__main__':
    main()
