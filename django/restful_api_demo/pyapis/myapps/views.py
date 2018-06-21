# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
import json
# Create your views here.
def myindex(request):
	response = json.dumps({'status':'no data'})
	return HttpResponse(response,content_type='text/json')

def get_car(request):
	if request.method=='GET':
		
		try:
			car=Car.objects.get(name=car_name)
			response=json.dumps([{'Car':car.name,'Top Speed':car.top_speed}])
		except:
			response = jsom.dumps([{'Error':'No car with that name'}])


	return HttpResponse(response,content_type='text/json')