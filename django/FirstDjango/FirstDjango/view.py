# coding: utf-8
from django.http import HttpResponse
from django.shortcuts import render,render_to_response
from TestModel.models import Test,NewBook,NewAuthor
def FirstView(request):
    context={}
    context['value']="Value setup"
    return render(request,'firstview.html',context)
    #return HttpResponse("First View")

def dbshow(request):
    test=Test.objects.all()
    return render(request,'db.html',{'teststr':test})

def books(request):
    authors=NewAuthor.objects.all()
    return render_to_response('books.html',{'authors':authors})