#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "chenwei"
# Date: 2019/2/15

from django.db import models
from utils.model_choices import PAY_TYPE, ENVE_TYPE, PAY_STATUS


class User(models.Model):
    class Meta:
        verbose_name = u''
        app_label = ''
        db_table = ''
        verbose_name_plural = verbose_name

    open_id = models.CharField(max_length=36, verbose_name=u'微信openid', db_index=True)
    user_name = models.CharField(max_length=255, null=True, verbose_name=u'用户名/昵称')
    form_id = models.CharField(max_length=64, null=False, verbose_name=u'小程序表单提交的formId')


class Order(models.Model):
    class Meta:
        verbose_name = u''
        app_label = ''
        db_table = ''
        verbose_name_plural = verbose_name

    pay_type = models.IntegerField(choices=PAY_TYPE, default=0, verbose_name=u'支付类型')
    pay_status = models.CharField(max_length=50, choices=PAY_STATUS, default='', verbose_name=u'支付状态')
    transaction_id = models.CharField(max_length=50, null=True, verbose_name=u'微信支付订单号')
    out_trade_no = models.CharField(max_length=50, null=True, verbose_name=u'商户订单号')
    prepay_id = models.CharField(max_length=64, null=False, verbose_name=u'支付产生的prepay_id')
    nonce_str = models.CharField(max_length=50, null=True, verbose_name=u'本地随机生成的订单号')


class Enve(models.Model):
    class Meta:
        verbose_name = u''
        app_label = ''
        db_table = ''
        verbose_name_plural = verbose_name

    quest = models.CharField(max_length=150, verbose_name=u'口令或者问题', null=False)
    quest_py = models.CharField(max_length=255, verbose_name=u'口令拼音', null=True)
    answer = models.CharField(max_length=255, verbose_name=u'答案', null=False)
    answer_py = models.CharField(max_length=255, null=True, verbose_name=u'答案拼音')
    user_id = models.BigIntegerField(verbose_name=u'用户id')
    show_amount = models.FloatField(default=0.00, verbose_name=u'显示余额')
    amount = models.FloatField(default=0.00, verbose_name=u'金额')
    commission = models.FloatField(default=0.00, verbose_name=u'佣金')
    num = models.IntegerField(default=0, verbose_name=u'个数')
    receive_num = models.IntegerField(default=0, verbose_name=u'已领取个数')
    be_overdue = models.BooleanField(default=False, verbose_name=u'红包是否过期')
    enve_type = models.IntegerField(verbose_name=u'红包类型', choices=ENVE_TYPE, default=ENVE_TYPE.COMMON)
    add_time = models.DateTimeField(auto_now_add=True, verbose_name=u'添加时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name=u'更新时间')
    is_adv = models.BooleanField(default=False, verbose_name=u'是否为广告红包')
    adv_url = models.CharField(max_length=255, verbose_name=u'广告文件')
    voice_url = models.CharField(max_length=255, verbose_name=u'你说我猜语音文件')
    video_url = models.CharField(max_length=255, verbose_name=u'你说我猜语音文件')
    adv_text = models.CharField(max_length=255, verbose_name=u'广告语')
    share2square = models.BooleanField(default=False, verbose_name=u'是否分享到广场')
    voice_dura = models.IntegerField(verbose_name=u'语音时长 毫秒数')
    dels = models.BooleanField(default=False, verbose_name=u'是否删除')


class EnveReceive(models.Model):
    class Meta:
        verbose_name = u''
        app_label = ''
        db_table = ''
        verbose_name_plural = verbose_name

    pid = models.ForeignKey(Enve)
    receive_answer = models.CharField(max_length=255, verbose_name=u'答案')
    user_id = models.IntegerField(verbose_name=u'用户ID')
    nick_name = models.CharField(verbose_name=u'昵称', max_length=150, default='')
    head_img = models.CharField(verbose_name=u'头像', max_length=150, default='')
    receive_amount = models.FloatField(verbose_name=u'金额', default=0.0)
    receive_num = models.IntegerField(verbose_name=u'领取个数', default=0)
    voice_url = models.CharField(verbose_name=u'微信语音路径', default='')
    durat = models.CharField(verbose_name=u'语音时长', default='')
    add_time = models.DateTimeField(verbose_name=u'领取时间', auto_now_add=True)
    is_best = models.BooleanField(verbose_name=u'是否为最佳', default=False)


class PayLog(models.Model):
    class Meta:
        verbose_name = u''
        app_label = ''
        db_table = ''
        verbose_name_plural = verbose_name

    pay_type = models.IntegerField(choices=PAY_TYPE, default=0, verbose_name=u'支付类型')
    transaction_id = models.CharField(max_length=50, null=True, verbose_name=u'微信支付订单号')
    status = models.CharField(max_length=50, choices=PAY_STATUS, default='', verbose_name=u'支付状态')
    desc = models.CharField(max_length=150, verbose_name=u'简述', default='')
    action = models.CharField(max_length=150, verbose_name=u'来源', default='')
    content = models.TextField(verbose_name=u'log具体内容')
    add_time = models.DateTimeField(verbose_name=u'领取时间', auto_now_add=True)




















