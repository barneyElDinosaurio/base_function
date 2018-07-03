"""myapi URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url,include
from django.contrib import admin
from myapps import views
from rest_framework import routers

router = routers.DefaultRouter()
# router.register('myapps',views.CarView)
router.register('myapps',views.ProductQualityView)
urlpatterns = [

    url(r'^admin/', admin.site.urls),
	url('',include(router.urls)), 
    url(r'^fraud/(\S+)/$',views.get_fraud),
    url(r'^productqual/$',views.get_product_quality), # 产品质量
    url(r'^personbadbehavious/$',views.people_bad_behavious), # 人员不良行为
    url(r'^companybadbehavious/$',views.company_bad_behavious), # 企业不良行为
    url(r'^companybackpay/$',views.company_backpay), # 企业欠薪投诉
    url(r'^companyblacklist/$',views.company_blacklist), # 企业欠薪投诉
    url(r'^accident/$',views.accident), # 安全事故
    url(r'^qualcancel/$',views.qualcancel), # 证书注销
    url(r'^qualmiss/$',views.qualmiss), # 证书遗失



    # url(r'^/(\S+)/$',views.get_fraud)
    # url('', views.myindex),
    # url(r'^(\S+)/$', views.get_car),
    # url(r'^vw/$', views.get_car),
    # url(r'<str:car_name>', views.get_car),

]