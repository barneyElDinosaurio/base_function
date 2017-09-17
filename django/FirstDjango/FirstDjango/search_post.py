#-*-coding=utf-8-*-
from django.shortcuts import render_to_response,render
from django.views.decorators import csrf
'''
def form_post(requset):
    return render_to_response('post.html')
'''
def form_post2(request):
    ctx={}
    if request.POST:
        ctx['rlt']=request.POST['p']
    return render(request,'post.html',ctx)