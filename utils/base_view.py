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

    def ok(self, data=None, msg='', code=None):
        return self.as_json_response(0, msg=msg, data=data, code=code)

    def error(self, error=1, msg='服务器开小差了~', data=None, code=None):
        if error != 1:
            msg = ''
        return self.as_json_response(error, msg=msg, data=data, code=code)

    def as_json_response(self, error, msg='', data=None, status=200, code=None, extra=None):
        """return a http response with json content.
            如果定义了传了msg,且msg不为空,
        """
        if isinstance(error, ErrorInfo) and error:
            result = {
                'error': 1,
                'code': code,
                'extra': extra,
            }

            result['msg'] = msg or error.msg
        else:
            result = {
                'code': error and 1 or 0,
                'msg': msg,
                'extra': extra,
            }

            if error and code is None:
                result['code'] = ERROR.DEFAULT_ERROR_CODE
            elif error and code is not None:
                result['code'] = code
                result['msg'] = msg

        if data is not None:
            result['data'] = data

        # 如果是没有登录状态码统一设置为403
        if result.get('code') == ERROR.LOGIN_REQUIRED:
            status = 403

        return json_response(result, status)

    def _inner_dispatch_for_baseview(self, request, *args, **kwargs):
        response = super(BaseView, self).dispatch(request, *args, **kwargs)
        return response

    def dispatch(self, request, *args, **kwargs):
        version = request.GET.get('_version', '0.0.0')
        _platform = request.GET.get('_platform', 'wx')
        response = self._inner_dispatch_for_baseview(request, *args, **kwargs)
        return response


class BaseViewLoginRequired(LoginRequiredMixin, BaseView):
    def __init__(self, *args, **kwargs):
        super(BaseViewLoginRequired, self).__init__(*args, **kwargs)