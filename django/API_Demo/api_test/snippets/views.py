from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
# Create your views here.
import logging
logger = logging.getLogger('info_logger')
def test1(request):
    if request.method=='POST':
        post_data=request.POST
        logger.info(type(post_data))
        logger.info('post data :: {}'.format(post_data))
        return HttpResponse(post_data)