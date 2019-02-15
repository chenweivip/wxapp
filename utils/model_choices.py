#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "chenwei"
# Date: 2019/2/15


from .enum import Enum


class PAY_TYPE(Enum):
    WE_CHAT = (1, '微信支付')
    BALANCE = (2, '余额支付')
    PART_BALANCE_AND_WECHAT = (3, '部分微信部分余额支付')


class PAY_STATUS(Enum):
    SUCCESS = ('ok', '支付成功')
    CANCEL = ('cancel', '取消支付')
    FAIL = ('fail', '支付失败')


class ENVE_TYPE(Enum):
    COMMON = (0, '普通口令')
    TRUE_WISH = (1, '真心寄语')
    YOU_GUESS = (2, '你说我猜')
