from django.shortcuts import render
from django.http import HttpResponse
from django.core import serializers
import json
# Create your views here.
from mystock.models import TbBasicInfo
def show(request):
	if request.method=='GET':
		name = request.GET.get('name')
		if name:
			print('name ',name)
			obj = TbBasicInfo.objects.filter(name=name).all()
			print('len of obj: ',len(obj))
			# data = serializers.serialize('json',obj)
			json_serializer = serializers.get_serializer('json')()
			resp = json_serializer.serialize(obj, ensure_ascii=False)
			 # ret = eval(data)
			return HttpResponse(eval(resp),content_type='text/json,charset=utf-8')

		else:
			data=[{'result':'0'}]
			return HttpResponse(json.dumps(data,ensure_ascii=False),content_type='text/json,charset=utf-8')


	return HttpResponse('None')