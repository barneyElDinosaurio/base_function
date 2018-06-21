import requests
import json
def post_data():
	name = 'jeep'
	speed = 98
	url ='http://127.0.0.1:8000/myapps/'
	data = {'car_name':name,'top_speed':speed}
	# js_data = json.dumps(data)
	r = requests.post(url= url,data=data)
	print(r.text)


def get_data():
	name = {'car_name':'honda'}
	js=json.dumps(name)
	url='http://127.0.0.1:8000/myapps/5'
	# url ='http://127.0.0.1:8000/'+js
	print(url)
	# data = {'car_name':name,'top_speed':speed}
	# js_data = json.dumps(data)
	r = requests.get(url= url)
	print(r.text)

get_data()
# post_data()
