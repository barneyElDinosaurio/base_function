from django.shortcuts import render
from django.http import HttpResponse
import json
import simplejson
from rest_framework import viewsets
from myapps.serializers import CarSerializer, FraudSerializer, ProductQualitySerializer
from myapps.models import Car, TbFrauds2, ProductQuality, TbBackpaylist, TbSafeaccident,TbQualMissed,TbQualCancel
from django.views.decorators.csrf import csrf_exempt
# from rest_framework import serializers
from django.forms.models import model_to_dict
from bson import json_util
from myapps import product_qual
from myapps import construction_industry
from django.core import serializers


# from django.utils import simplejson


# Create your views here.
def myindex(request):
    response = json.dumps([{}])
    # response = json.dumps([{'status':'missing args'}])
    return HttpResponse(response, content_type='text/json')


def get_fraud(request, name):
    if request.method == 'GET':
        try:
            print(name)

            person = TbFrauds2.objects.filter(executed_name__icontains=name).all()
            print(person)
            if len(person) == 0:
                response = json.dumps([{'result': '0'}])
                return HttpResponse(response, content_type='text/json')

            # print(person.identity_number)
            # response = json.dumps([{'executed': person.executed_name, 'sex':person.gender,'age':person.age, 'identity_number': person.identity_number,
            #                         'court':person.court,'duty': person.duty}])
            data = serializers.serialize('json', person)
            # item = {}
            # if person is not None:
            #     for p in person:
            #         model_to_dict(p)
            # ret_data = []
            # for i in person:
            #     ret_data.append(model_to_dict(i))
            # # response = json.dumps(data)
            # print(ret_data)
            # print(type(ret_data))
            return HttpResponse(json.dumps(data), content_type='text/json')

        except Exception as e:
            print(e)
            print('can not find the person {}'.format(name))
            response = json.dumps([{'result': '0'}])
            return HttpResponse(response, content_type='text/json')


def get_car(request, name):
    if request.method == 'GET':
        try:
            print(name)
            car = Car.objects.all().get(car_name=name)
            print(car.top_speed)
            response = json.dumps([{'Car': car.car_name, 'Top Speed': car.top_speed}])
        except Exception as e:
            print(e)
            response = json.dumps([{'Error': 'No car with that name'}])
    return HttpResponse(response, content_type='text/json')


# 建筑企业欠薪查询
def people_bad_behavious(request):
    if request.method == 'GET':
        name = request.GET.get('name')
        try:
            ret = construction_industry.people_bad_behavious(name)
            if len(ret) == 0:
                response = [{'result': '0'}]
                return HttpResponse(json.dumps(response), content_type='application/json,charset=utf-8')
        except Exception as e:
            print(e)
            response = [{'result': '0'}]
            return HttpResponse(json.dumps(response), content_type='application/json,charset=utf-8')

        else:
            response = json.dumps(ret)

        # 最后看编码情况,如果有乱码则加上 ensure_ascii=False
        # return HttpResponse(json.dumps(resp,default=json_util.default,ensure_ascii=False), content_type='text/json')
        # return HttpResponse(json.dumps(ret_data,default=json_util.default), content_type='text/json')
        return HttpResponse(response, content_type='application/json,charset=utf-8')


# 产品质量查询
def get_product_quality(request):
    if request.method == 'GET':
        name = request.GET.get('name')
        print(name)
        try:
            ret = product_qual.run(name)
            if len(ret) == 0:
                resp = [{'result': '0'}]
                return HttpResponse(json.dumps(resp, ensure_ascii=False), content_type='application/json,charset=utf-8')

        except Exception as e:
            print(e)
            print('can not find the person {}'.format(name))
            resp = [{'result': '0'}]
            return HttpResponse(json.dumps(resp, ensure_ascii=False), content_type='application/json,charset=utf-8')

        else:
            resp = []
            colums = ['no', 'enterprise', 'location', 'product_name', 'product_detail_name', 'specifiction',
                      'product_grade', 'manufacture_number',
                      'spot_test_result', 'failed_item', 'tester', 'test_date', 'spot_test_type', 'sample_origin',
                      'spot_test_org']
            for each_item in ret:
                item = {}
                for index, value in enumerate(colums):
                    item[value] = each_item[index]
                resp.append(item)

            return HttpResponse(json.dumps(resp, ensure_ascii=False), content_type='application/json,charset=utf-8')
            # 最后看编码情况,如果有乱码则加上 ensure_ascii=False
            # return HttpResponse(json.dumps(resp,default=json_util.default,ensure_ascii=False), content_type='text/json')
            # return HttpResponse(json.dumps(ret_data,default=json_util.default), content_type='text/json')


def company_bad_behavious(request):
    if request.method == 'GET':
        name = request.GET.get('name')
        try:
            ret = construction_industry.company_bad_behavious(name)
            if len(ret) == 0:
                response = [{'result': '0'}]
                return HttpResponse(json.dumps(response), content_type='application/json,charset=utf-8')
        except Exception as e:
            print(e)
            response = [{'result': '0'}]
            return HttpResponse(json.dumps(response), content_type='application/json,charset=utf-8')

        else:
            response = json.dumps(ret)

        # 最后看编码情况,如果有乱码则加上 ensure_ascii=False
        # return HttpResponse(json.dumps(resp,default=json_util.default,ensure_ascii=False), content_type='text/json')
        # return HttpResponse(json.dumps(ret_data,default=json_util.default), content_type='text/json')
        return HttpResponse(response, content_type='application/json,charset=utf-8')


def company_backpay(request):
    if request.method == 'GET':
        name = request.GET.get('name')
        obj = TbBackpaylist.objects.filter(enterprise__icontains=name).all()

        if len(obj) > 0:
            data = serializers.serialize('json', obj)
            print(type(data))
            print(data)
            json_serializer = serializers.get_serializer('json')()
            resp = json_serializer.serialize(obj, ensure_ascii=False)
            print(type(json_serializer))
            return HttpResponse(simplejson.dumps(resp, ensure_ascii=False),
                                content_type='application/json,charset=utf-8')

        else:
            print('can not find the result {}'.format(name))
            response = json.dumps([{'result': '0'}])
            return HttpResponse(response, content_type='application/json,charset=utf-8')


def company_blacklist(request):
    if request.method == 'GET':
        name = request.GET.get('name')
        try:
            ret = construction_industry.company_blacklist(name)
            if len(ret) == 0:
                response = [{'result': '0'}]
                return HttpResponse(json.dumps(response), content_type='application/json,charset=utf-8')
        except Exception as e:
            print(e)
            response = [{'result': '0'}]
            return HttpResponse(json.dumps(response), content_type='application/json,charset=utf-8')

        else:
            response = json.dumps(ret)

        # 最后看编码情况,如果有乱码则加上 ensure_ascii=False
        # return HttpResponse(json.dumps(resp,default=json_util.default,ensure_ascii=False), content_type='text/json')
        # return HttpResponse(json.dumps(ret_data,default=json_util.default), content_type='text/json')
        return HttpResponse(response, content_type='application/json,charset=utf-8')


def accident(request):
    if request.method == 'GET':
        name = request.GET.get('name')

        obj = TbSafeaccident.objects.filter(title__icontains=name).all()

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

def qualcancel(request):
    if request.method == 'GET':
        name = request.GET.get('name')
        objs = TbQualCancel.objects.filter(enterprise__icontains=name).all()
        print(objs)
        if len(objs) > 0:
            data = serializers.serialize('json', objs)
            print(type(data))
            print(data)
            json_serializer = serializers.get_serializer('json')()
            resp = json_serializer.serialize(objs, ensure_ascii=False)
            print(type(json_serializer))
            return HttpResponse(eval(resp),
                                content_type='application/json,charset=utf-8')
        else:
            print('can not find the result {}'.format(name))
            response = json.dumps([{'result': '0'}])
            return HttpResponse(response, content_type='application/json,charset=utf-8')

def qualmiss(request):
    if request.method == 'GET':
        name = request.GET.get('name')

        obj = TbQualMissed.objects.filter(enterprise__icontains=name).all()

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



@csrf_exempt
def add_car(request):
    if request.method == 'POST':
        print(request.body)
        payload = json.loads(request.body)
        car_name = payload.get('car_name')
        top_speed = payload.get('top_speed')
        car = Car(name=car_name, top_speed=top_speed)

        try:
            car.save()
            response = json.dumps([{'Success': 'Car added successfully!'}])
        except:
            response = json.dumps([{'Error': 'Car could not be add !'}])
        return HttpResponse(response, content_type='text/json')


class CarView(viewsets.ModelViewSet):
    queryset = Car.objects.all().order_by('top_speed')
    serializer_class = CarSerializer


class FraudView(viewsets.ModelViewSet):
    queryset = TbFrauds2.objects.all()
    serializer_class = FraudSerializer


class ProductQualityView(viewsets.ModelViewSet):
    queryset = ProductQuality.objects.all()
    serializer_class = ProductQualitySerializer
