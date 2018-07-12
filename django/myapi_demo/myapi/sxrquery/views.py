from django.shortcuts import render
from django.http import HttpResponse
import json
import simplejson
from rest_framework import viewsets
# Create your views here.
from sxrquery.models import HljShixin1106
from django.core import serializers

def sxrquery(request):
    if request.method == 'GET':
        name = request.GET.get('name')

        obj = HljShixin1106.objects.filter(frname1__icontains=name).all()

        if len(obj) > 0:
            data = serializers.serialize('json', obj)
            print(type(data))
            print(data)
            json_serializer = serializers.get_serializer('json')()
            resp = json_serializer.serialize(obj, ensure_ascii=False)
            print(type(json_serializer))
            return HttpResponse(eval(resp),
                                content_type='application/json,charset=utf-8')

        else:
            print('can not find the result {}'.format(name))
            response = json.dumps([{'result': '0'}])
            return HttpResponse(response, content_type='application/json,charset=utf-8')
