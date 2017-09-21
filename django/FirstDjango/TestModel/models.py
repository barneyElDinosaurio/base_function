# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Test(models.Model):
    name=models.CharField(max_length=128)

    def __unicode__(self):
        return self.name


class Publisher(models.Model):
    name = models.CharField(max_length=30)

    address = models.CharField(max_length=50)

    city = models.CharField(max_length=60)

    state_province = models.CharField(max_length=30)

    country = models.CharField(max_length=50)

    website = models.URLField()

    class Admin:

        pass




class Author(models.Model):
    salutation = models.CharField(max_length=10)

    first_name = models.CharField(max_length=30)

    last_name = models.CharField(max_length=40)

    email = models.EmailField()

    headshot = models.ImageField(upload_to='tmp')

    class Admin:

        pass



class Book(models.Model):
    title = models.CharField(max_length=100)

    authors = models.ManyToManyField(Author)

    publisher = models.ForeignKey(Publisher)

    publication_date = models.DateField()

    def __str__(self):
        return self.title

    class Admin:

        pass

class Pen(models.Model):
    name=models.CharField(max_length=30)

    def __unicode__(self):
        return self.name

class Shop(models.Model):
    name=models.CharField(max_length=30)
    pen=models.ForeignKey(Pen)

    def __unicode__(self):
        return self.name

sex_choices=(
    ('f','female'),
    ('m','male'),
)
class User(models.Model):
    name=models.CharField(max_length=20)
    sex=models.CharField(max_length=1,choices=sex_choices)

    def __unicode__(self):
        return self.name


class NewAuthor(models.Model):
    name=models.CharField(max_length=20)

    def __unicode__(self):
        return self.name

class NewBook(models.Model):
    name=models.CharField(max_length=20)
    author=models.ManyToManyField(NewAuthor)

    def __unicode__(self):
        return self.name

class Customer(models.Model):
    CUSTOMER_FROM_NAMES = (
            (1, u"无"),
            (2, u"首页登记"),
            (3, u"客服QQ"),
            (4, u"邮件"),
            (5, u"市场活动"),
            (6, u"电话咨询"),
            (7, u"电话外呼"),
            (8, u"商务扩展"),
            (9, u"内部推荐"),
            (10, u"公司分配"),
            )







