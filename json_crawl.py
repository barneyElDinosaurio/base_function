#-*-coding=utf-8-*-
import requests,urllib2,urllib,json
def using_requests():
    post_data = {'first':'true','kd':'Android','pn':'1'}
    url="http://www.lagou.com/jobs/positionAjax.json?city=%E6%B7%B1%E5%9C%B3&needAddtionalResult=false"
    r=requests.post(url,data=post_data)
    #r=requests.post("http://www.lagou.com/jobs/positionAjax.json?px=default",data=post_data)
    print r.text

def getJson():
    user_agent="Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0)"
    headers={"User-Agent":user_agent}
    url="http://www.lagou.com/jobs/positionAjax.json?city=%E6%B7%B1%E5%9C%B3&needAddtionalResult=false"

    data={"first":"false","pn":"2","kd":"Python"}
    post_data=urllib.urlencode(data)
    req=urllib2.Request(url,headers=headers,data=post_data)

    resp=urllib2.urlopen(req)
    return_data=resp.read()
    print return_data.decode("utf-8")
    f=open("json.txt",'w')
    f.write(return_data)
    f.close()
    json_data=json.loads(return_data)
    print type(json_data)
    #print json_data['success']
    #print json

#using_requests()

getJson()
