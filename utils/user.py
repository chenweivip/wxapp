#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "chenwei"
# Date: 2019/2/15

import json
from functools import wraps
from django.http import HttpResponse


from .logger import auth_logger
from utils.error import ERROR as CODES


class DictWrapperUseDot(object):
    """wrap a dict, get key by dot syntax."""

    def __init__(self, _dict):
        assert isinstance(_dict, dict)
        self.__data = {}

        for k, v in _dict.items():
            if isinstance(v, dict):
                self.__data[k] = DictWrapperUseDot(v)
            else:
                self.__data[k] = v

    def __getattr__(self, attr):
        return self.__data[attr]


def get_user_by_request(request):
    """获取用户信息"""

    try:
        user_info = request.rpc["venus/account/user/self_user_detail"]().unwrap()
    except:
        return None

    if not user_info["logined"]:
        return None

    info = {
        "id": user_info["user_id"],
        "user_id": user_info["user_id"],
        "nick_name": user_info["nick_name"],
        "profile_pic": user_info["profile_pic"],
        "city_id": user_info["city_id"],
        "gender": user_info["gender"],
        "register_time": user_info["register_time"],
    }

    return DictWrapperUseDot(info)


def auth(request):
    user_info = get_user_by_request(request)
    if not user_info:
        return False

    request.user = user_info

    return True


def login_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):

        if auth(request):
            return view_func(request, *args, **kwargs)

        request_data = {'request': {key: value for key, value in request.REQUEST.items()}}
        auth_logger.error(json.dumps(request_data))

        result = {
            'error': 1,
            'message': CODES.getDesc(CODES.LOGIN_REQUIRED),
            'error_code': CODES.LOGIN_REQUIRED,
        }

        return HttpResponse(status=403, content=json.dumps(result))

    return _wrapped_view