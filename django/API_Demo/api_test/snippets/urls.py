from django.conf.urls import url
# from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views
# import views
urlpatterns = [
    url(r'hello', views.test1),
]

# urlpatterns = format_suffix_patterns(urlpatterns):4