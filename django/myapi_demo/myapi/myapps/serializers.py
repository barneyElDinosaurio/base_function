from rest_framework import serializers
from myapps.models import Car, TbFrauds2,ProductQuality


class CarSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Car
        fields = ('id', 'url', 'car_name', 'top_speed')


class FraudSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = TbFrauds2
        fields = ('id', 'url', 'executed_name', 'identity_number', 'duty')


class ProductQualitySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ProductQuality
        fields =('id','url','enterprise_name')

