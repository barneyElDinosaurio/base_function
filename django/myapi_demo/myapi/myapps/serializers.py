from rest_framework import serializers
from myapps.models import Car

class CarSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model=Car
		fields =('id','url','car_name','top_speed')