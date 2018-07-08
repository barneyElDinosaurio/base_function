# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from models import Customer
from django.shortcuts import render

# Create your views here.
class Testcase():
    customer_list=Customer.CUSTOMER_FROM_NAMES
    print(customer_list)


obj=Testcase()

