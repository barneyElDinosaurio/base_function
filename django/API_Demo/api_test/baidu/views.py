from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse
import requests
# Create your views here.
import logging
def search(request):

    kw = request.GET.get('kw')
    print(kw)
    content = baidu_page(kw)
    return HttpResponse(content)

def baidu_page(kw):
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:31.0) Gecko/20100101 Firefox/31.0',
               }
    r=requests.get('http://www.baidu.com/s?wd={}'.format(kw),headers)
    print(r.text)
    return r.text