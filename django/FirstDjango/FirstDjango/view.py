# coding: utf-8
from django.http import HttpResponse
from django.shortcuts import render
def FirstView(request):
    context={}
    context['value']="Value setup"
    return render(request,'firstview.html',context)
    #return HttpResponse("First View")