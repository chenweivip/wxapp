#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "chenwei"
# Date: 2019/2/16

import json
import time

class WxPay(object):

    def __init__(self):
        self.__wxpay_appid = ""
        self.__wxpay_appsecret = ""

        self.__wxpay_key = ""
        self.__wxpay_mchid = ""

        self.transfers = {
            "check_name": "NO_CHECK"
        }
        self.parameters = dict()
        self.jsApiObj = dict()
        self.payment = dict()

    def get_code(self, order, openid):
        """
        生成支付代码
        :param order:
        :param openid:
        :return:
        """
        if not openid:
            return False

        self.parameters['openid'] = openid
        self.parameters['body'] = order['body']
        self.parameters['out_trade_no'] = order['out_trade_no']
        self.parameters['total_fee'] = order['total_fee'] * 100  # 订单总金额，单位为分
        # 接收微信支付异步通知回调地址
        self.parameters['notify_url'] = order['notify_url']
        self.parameters['trade_type'] = "JSAPI"

        return self.getParameters()

    def getParameters(self):
        """
        封装参数
        :return:
        """
        # 最终的目的就是为了得到这个6个参数而已
        prepay_id = self.getPrepayId()
        self.sApiObj["appId"] = self.payment['wxpay_appid']
        self.jsApiObj["timeStamp"] = str(time.time())
        self.jsApiObj["nonceStr"] = self.createNoncestr()  # 随机串
        self.jsApiObj["package"] = "prepay_id=$prepay_id"  # 这个最烦人
        self.jsApiObj["signType"] = "MD5"  # 签名方式
        self.jsApiObj["paySign"] = self.getSign(self.jsApiObj)  # 微信签名

        # 转成json格式
        self.parameters = json.dumps(self.jsApiObj)
        return self.parameters

    def getPrepayId(self):
        """
        普通商户统一下单接口有参数说明的
        获取prepay_id
        :return:
        """
        # 设置接口链接
        url = "https://api.mch.weixin.qq.com/pay/unifiedorder"
        try:
            if not self.parameters['out_trade_no']:
                raise Exception('缺少统一支付接口必填参数out_trade_no！')
            elif not self.parameters["body"]:
                raise Exception('缺少统一支付接口必填参数body！')
            elif not self.parameters['total_fee']:
                raise Exception('缺少统一支付接口必填参数total_fee！')
            elif not self.parameters['notify_url']:
                raise Exception('缺少统一支付接口必填参数notify_url！')
            elif not self.parameters['trade_type']:
                raise Exception('缺少统一支付接口必填参数trade_type！')
            elif all([self.parameters["trade_type"] == "JSAPI", self.parameters["openid"]]):
                raise Exception('统一支付接口中，缺少必填参数openid！trade_type为JSAPI时，openid为必填参数！')

        except Exception:
            pass

    def getSign(self):
        """

        :return:
        """

    def createNoncestr(self):
        """

        :return:
        """