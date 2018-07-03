import execjs

# Init environment
import requests

node = execjs.get()

# Params
method = 'GETCITYWEATHER'
city = '北京'
type = 'HOUR'
start_time = '2018-01-25 00:00:00'
end_time = '2018-01-25 23:00:00'

# Compile javascript
file = 'new.js'
import codecs
stream = codecs.open(file,'r',encoding='utf-8')
content = stream.read()
# print(content)
ctx = node.compile(content)

# Get params
js = 'getEncryptedData("{0}", "{1}", "{2}", "{3}", "{4}")'.format(method, city, type, start_time, end_time)
params = ctx.eval(js)
print(params)
api = 'https://www.aqistudy.cn/apinew/aqistudyapi.php'
response = requests.post(api, data={'d': params})
js = 'decodeData("{0}")'.format(response.text)
decrypted_data = ctx.eval(js)
print(decrypted_data)