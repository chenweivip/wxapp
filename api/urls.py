#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "chenwei"
# Date: 2019/2/14

from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^redpacket/ok$', Hello().as_view()),
]