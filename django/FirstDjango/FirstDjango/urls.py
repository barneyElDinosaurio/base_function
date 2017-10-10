#-*-coding=utf-8-*-
"""FirstDjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from . import view,testdb,search,search_post
#from django.conf.urls. import *
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',view.FirstView),
    url(r'first',view.FirstView),
    url(r'^insert$',testdb.insert),
    url(r'^get$',testdb.search),
    url(r'^search_form$',search.search_form),
    #url(r'^search',search.search_get),
    #url(r'^post$',search_post.form_post),
    url(r'^search_post$',search_post.form_post2),
    # 无法执行
    url(r'^dbtest/$',view.dbshow),
    url(r'^books/$',view.books),
    url(r'^date/$',view.showdate),
    url(r'^ajax_list/$', view.ajax_list, name='ajax-list'),

    url(r'^ajax_dict/$', view.ajax_dict, name='ajax-dict'),
    url(r'^[A,B]',view.show_string),
    url(r'^header/$',view.getAgent),
    url(r'^notfound/$',view.notfound),
    url(r'^time/$',view.time_show),
    url(r'^mytime/plug/(\d{1,2})$',view.time_show2),
    url(r'^current$',view.current_date),
    url(r'^filter$',view.filter_usage),
    url(r'^filter2$',view.filter_usage2),
    #url(r'^admin/', include('django.contrib.admin.urls')),


]
