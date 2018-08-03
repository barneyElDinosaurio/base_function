import requests

def post():

	url='http://10.150.133.14:8000/barcode'
	
	data={'url':'http://gsxt.gdgs.gov.cn//GSpublicity/GSpublicityList.html?jumpid=rO0ABXQASntzZXJ2aWNlOmVudEluZm8sZW50Tm86YWEzZDJlZjEtMDE0Zi0xMDAwLWUwMDAtZGVj%0D%0AOTBhMGEwMTE1LHJlZ09yZzo0NDEzMDJ9%0D%0A'}
	for _ in range(10):
		r = requests.post(url=url, data=data)
		print(r.json())

post()