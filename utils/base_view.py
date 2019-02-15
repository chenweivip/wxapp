#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "chenwei"
# Date: 2019/2/15

from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt

from .error import ERROR
from .response import json_response
from .user import login_required


class ErrorInfo(object):
    def __init__(self, code=None, msg=None):
        self.code = code
        self.msg = msg

    def __nonzero__(self):
        if self.code is None and self.msg is None:
            return False
        else:
            return True

    def __repr__(self):
        return '<ErrorInfo> code: %s, msg: %s' % (self.code, self.msg)


class LoginRequiredMixin(object):

    @classmethod
    def as_view(cls, **initkwargs):
        view = super(LoginRequiredMixin, cls).as_view(**initkwargs)
        return login_required(view)


class BaseView(View):
    decorators = [csrf_exempt, ]

    def get_ErrorInfo(self, error_code):
        return ErrorInfo(code=error_code, msg=ERROR.getDesc(error_code))

    def __init__(self, *args, **kwargs):
        super(BaseView, self).__init__(*args, **kwargs)

    @classmethod
    def as_view(cls, **initkwargs):
        view = super(BaseView, cls).as_view(**initkwargs)

        for deco in cls.decorators[::-1]:
            view = deco(view)

        return view

    def ok(self, data=None, message='', extra=None):
        return self.as_json_response(0, message=message, data=data, extra=extra)

    def error(self, error=1, message='服务器开小差了~', data=None, error_code=None):
        if error != 1:
            message = ''
        return self.as_json_response(error, message=message, data=data, error_code=error_code)

    def as_json_response(self, error, message='', data=None, status=200, error_code=None, extra=None):
        """return a http response with json content.
            如果定义了传了message,且message不为空,
        """
        if isinstance(error, ErrorInfo) and error:
            result = {
                'error': 1,
                'error_code': error.code,
                'extra': extra,
            }

            result['message'] = message or error.msg
        else:
            result = {
                'error': error and 1 or 0,
                'message': message,
                'extra': extra,
            }

            if error and error_code is None:
                result['error_code'] = ERROR.DEFAULT_ERROR_CODE
            elif error and error_code is not None:
                result['error_code'] = error_code
                result['message'] = ERROR.getDesc(error_code)

        if data is not None:
            result['data'] = data

        # 如果是没有登录状态码统一设置为403
        if result.get('error_code') == ERROR.LOGIN_REQUIRED:
            status = 403

        return json_response(result, status)


class BaseViewLoginRequired(LoginRequiredMixin, BaseView):
    def __init__(self, *args, **kwargs):
        super(BaseViewLoginRequired, self).__init__(*args, **kwargs)