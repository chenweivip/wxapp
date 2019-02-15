#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "chenwei"
# Date: 2019/2/15

from .enum import Enum, unique


@unique
class ERROR(int, Enum):
    """错误码"""
    SUCCESS = (0, '请求成功')

    LOGIN_REQUIRED = (70000, '请登录后再试')
    DEFAULT_ERROR_CODE = (40005, '请求失败')
    UNIVERSAL = (99999, '通用错误码')


