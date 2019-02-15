#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "chenwei"
# Date: 2019/2/15

from utils.base_view import BaseView
from api.models import Enve, User, EnveReceive

REDPACKET_CONFIG = {
    'RECEIVE_AMOUNT_MIN': 0.01,
    'AMOUNT_MIN': 0.01,
}


class SaveEnve(BaseView):

    def post(self, request):

        data = {
            'amount': request.POST.get('amount'),
            'num': request.POST.get('amount'),
            'is_adv': request.POST.get('amount'),
            'enve_type': request.POST.get('amount'),
            'form_id': request.POST.get('amount'),
            'token': request.POST.get('amount'),
            'adv_url': request.POST.get('amount'),
            'video_url': request.POST.get('amount'),
            'adv_text': request.POST.get('amount'),
            'share2square': request.POST.get('amount'),
            'quest': request.POST.get('amount'),
            'voice_url': request.POST.get('amount'),
            'voice_dura': request.POST.get('amount'),
            'answer': request.POST.get('amount'),
        }

        Enve.objects.create(**data)

        #  判断是否符合最低领取红包金额要求
        if data['amount'] < REDPACKET_CONFIG['RECEIVE_AMOUNT_MIN'] * data['num']:
            return self.error(message=u'不符合领红包最低金额要求', error_code=50000)

        # 判断是否符合最低红包金额要求
        if data['amount'] < REDPACKET_CONFIG['AMOUNT_MIN']:
            return self.error(message=u'不符合红包最低金额要求', error_code=50000)

        # 查询用户余额, 根据open_id
        User.objects.get(open_id=data['open_id'])



















