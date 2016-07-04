import requests
post_data = {'first':'true','kd':'Android','pn':'1'}

r=requests.post("http://www.lagou.com/jobs/positionAjax.json?px=default",data=post_data)
print r.text

