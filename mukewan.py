# -*-coding=utf-8-*-
import requests
headers = {
    "User - Agent": "mukewang/5.1.4 (Android 4.4.2; Huawei H60-L02 Build/HDH60-L02),Network WIFI",
    "APP-INFO": "mukewang/5.1.4 (Android 4.4.2; Huawei H60-L02 Build/HDH60-L02),Network WIFI",
    "Host": "www.imooc.com",
    "Connection": "Keep-Alive",
    "Content-Type": "application/x-www-form-urlencoded"
}
for i in range(1, 10):
    formdata = {
        "typeid": "18",
        "page": str(i),
    }
    r=requests.post(url='http://www.imooc.com/api3/articlelist',headers=headers,data=formdata)
    #print r.text
    print r.json()['errorDesc']
