# -*-coding=utf-8-*-
# 这是一个简单的hello 不依赖其他的文件

import sys
from django.conf import settings
from django.conf.urls import url
from django.http import HttpResponse, HttpResponseBadRequest
import logging
from PIL import Image, ImageDraw
from io import BytesIO
from django.core.cache import cache

logging.basicConfig(level=logging.INFO)
settings.configure(
    DEBUG=True,
    SECRET_KEY='thisisthesecretkey',
    ROOT_URLCONF=__name__,
    MIDDLEWARE_CLASS=(
        'django.middleware.common.CommonMiddleware',
        'django.middleware.csrf.CsrfViewMiddleware',
        'django.middleware.clcikjacking.XFrameOptionsMiddleware',
    ),
)


def index(request):
    return HttpResponse('One file hello world')


def placeholder(request, width, height):
    form = ImageForm({'width': width, 'height': height})

    if form.is_valid():
        fm_width = form.cleaned_data['width']
        fm_height = form.cleaned_data['height']
        image = form.general_image()

        return HttpResponse(image, content_type='image/png')

    else:
        return HttpResponseBadRequest("Error in url")


from django import forms


class ImageForm(forms.Form):
    height = forms.IntegerField(min_value=1, max_value=1800)
    width = forms.IntegerField(min_value=1, max_value=1800)

    def general_image(self, image_format='PNG'):
        fm_width = self.cleaned_data['width']
        fm_height = self.cleaned_data['height']

        key = '{}.{}.{}'.format(fm_width, fm_height, image_format)
        content = cache.get(key)
        if content is None:
            image = Image.new('RGB', (fm_width, fm_height), color=122)

            draw = ImageDraw.Draw(image)
            text = '{}x{}'.format(fm_width, fm_height)
            text_width, text_height = draw.textsize(text)

            if text_width < fm_width and text_height < fm_height:
                text_top = (fm_height - text_height) // 2
                text_left = (fm_width - text_width) // 2

                draw.text((text_top, text_left), text, fill=(255, 255, 255))

            content = BytesIO()
            image.save(content, image_format)
            content.seek(0)
            cache.set(key, content, 60 * 60)

        return content


urlpatterns = (
    url(r'^$', index, name='homepage'),
    url(r'^image/(?P<width>[0-9]+)x(?P<height>[0-9]+)/$', placeholder, name='placeholder'),
)

if __name__ == '__main__':
    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
