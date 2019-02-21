#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "chenwei"
# Date: 2019/2/14

from django.conf.urls import url
from .views.wx import (
    ShareIndex, DefaultIndex, DefaultNavbar,
    DefaultNavigation, DefaultStore
)

urlpatterns = [
    url(r'^share/index$', ShareIndex.as_view()),
    url(r'^default/index$', DefaultIndex.as_view()),
    url(r'^default/store$', DefaultStore.as_view()),
    url(r'^default/navbar$', DefaultNavbar.as_view()),  # 底部导航栏
    url(r'^default/navigation-bar-color$', DefaultNavigation.as_view()),
]