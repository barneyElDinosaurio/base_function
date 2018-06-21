from django.shortcuts import render
from django.http import HttpResponse
import json
from rest_framework import viewsets
from myapps.serializers import CarSerializer
from myapps.models import Car
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def myindex(request):
	response = json.dumps([{}])
	# response = json.dumps([{'status':'missing args'}])
	return HttpResponse(response,content_type='text/json')


def get_car(request,name):
	if request.method=='GET':
		try:
			print(name)
			car=Car.objects.all().get(car_name=name)
			print(car.top_speed)
			response=json.dumps([{'Car':car.car_name,'Top Speed':car.top_speed}])
		except Exception as e:
			print(e)
			response = json.dumps([{'Error':'No car with that name'}])
	return HttpResponse(response,content_type='text/json')

@csrf_exempt
def add_car(request):
	if request.method=='POST':
		print(request.body)
		payload=json.loads(request.body)
		car_name = payload.get('car_name')
		top_speed = payload.get('top_speed')
		car = Car(name=car_name,top_speed=top_speed)

		try:
			car.save()
			response = json.dumps([{'Success':'Car added successfully!'}])
		except:
			response = json.dumps([{'Error':'Car could not be add !'}])
		return HttpResponse(response,content_type='text/json')


class CarView(viewsets.ModelViewSet):
	queryset = Car.objects.all().order_by('top_speed')
	serializer_class = CarSerializer