# coding:utf8

from .base_view import BaseView


class Hello(BaseView):

    def get(self, request):
        data = {
            'name': 'alex',
            'age': 25
        }
        return self.ok(data=data, message='请求成功')
