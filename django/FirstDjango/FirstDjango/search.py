#-*-coding=utf-8-*-
from django.shortcuts import render_to_response

from  django.http import HttpResponse

def search_form(request):
    return render_to_response('search.html')

'''
def search_get(request):
    request.encoding='utf-8'
    if 'q' in request.GET:
        message="you search "+request.GET['q']
    else:
        message='you enter nothing'

    return HttpResponse(message)
'''