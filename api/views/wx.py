#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "chenwei"
# Date: 2019/2/19

import os
from utils.base_view import BaseView


class ShareIndex(BaseView):

    def get(self, request):
        data = {
            "id": "1",
            "first": "0.00",
            "second": "0.00",
            "third": "0.00",
            "store_id": "2",
            "level": "0",
            "condition": "0",
            "share_condition": "0",
            "content": None,
            "pay_type": "0",
            "min_money": "1.00",
            "agree": None,
            "first_name": None,
            "second_name": None,
            "third_name": None,
            "pic_url_1": None,
            "pic_url_2": None,
            "price_type": "0",
            "bank": None,
            "remaining_sum": "0",
            "rebate": "0.00",
            "is_rebate": "0",
            "share_good_status": "0",
            "share_good_id": "0"
        }
        return self.ok(data=data, msg='success')


class DefaultIndex(BaseView):

    def get_store_data(self, store_id):
        return {
            "id": 2,
            "name": "MesShop商城",
            "copyright": "",
            "copyright_pic_url": None,
            "copyright_url": None,
            "contact_tel": "",
            "show_customer_service": 1,
            "cat_style": 1,
            "address": None,
            "is_offline": 0,
            "is_coupon": 1,
            "is_comment": 1,
            "is_share_price": 1,
            "is_member_price": 1,
            "dial": None,
            "dial_pic": None,
            "service": "",
            "cut_thread": None,
            "option": {
                "step": "",
                "service": "",
                "web_service": "",
                "web_service_url": "",
                "wxapp": None,
                "quick_navigation": {

                },
                "phone_auth": "",
                "good_negotiable": {

                },
                "quick_map": "",
                "web_service_status": ""
            },
            "purchase_frame": 0,
            "is_sales": 1,
            "quick_navigation": {},
            "good_negotiable": {},
            "buy_member": 0,
            "logo": None,
            "is_official_account": 0,
            "share_custom_data": {
                "menus": {
                    "money": {
                        "name": "分销佣金",
                        "icon": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/images/share-custom/img-share-price.png",
                        "open_type": "navigator",
                        "url": "/pages/share-money/share-money",
                        "tel": ""
                    },
                    "order": {
                        "name": "分销订单",
                        "icon": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/images/share-custom/img-share-order.png",
                        "open_type": "navigator",
                        "url": "/pages/share-order/share-order",
                        "tel": ""
                    },
                    "cash": {
                        "name": "提现明细",
                        "icon": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/images/share-custom/img-share-cash.png",
                        "open_type": "navigator",
                        "url": "/pages/cash-detail/cash-detail",
                        "tel": ""
                    },
                    "team": {
                        "name": "我的团队",
                        "icon": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/images/share-custom/img-share-team.png",
                        "open_type": "navigator",
                        "url": "/pages/share-team/share-team",
                        "tel": ""
                    },
                    "qrcode": {
                        "name": "推广二维码",
                        "icon": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/images/share-custom/img-share-qrcode.png",
                        "open_type": "navigator",
                        "url": "/pages/share-qrcode/share-qrcode",
                        "tel": ""
                    }
                },
                "words": {
                    "can_be_presented": {
                        "name": "可提现佣金",
                        "default": "可提现佣金"
                    },
                    "already_presented": {
                        "name": "已提现佣金",
                        "default": "已提现佣金"
                    },
                    "parent_name": {
                        "name": "推荐人",
                        "default": "推荐人"
                    },
                    "pending_money": {
                        "name": "待打款佣金",
                        "default": "待打款佣金"
                    },
                    "cash": {
                        "name": "提现",
                        "default": "提现"
                    },
                    "user_instructions": {
                        "name": "用户须知",
                        "default": "用户须知"
                    },
                    "apply_cash": {
                        "name": "我要提现",
                        "default": "我要提现"
                    },
                    "cash_type": {
                        "name": "提现方式",
                        "default": "提现方式"
                    },
                    "cash_money": {
                        "name": "提现金额",
                        "default": "提现金额"
                    },
                    "order_money_un": {
                        "name": "未结算佣金",
                        "default": "未结算佣金"
                    },
                    "share_name": {
                        "name": "分销商",
                        "default": "分销商"
                    }
                }
            }
        }

    def get_topic_list(self, baseUrl=None):
        return {
            'topic': {
                'logo_2': os.path.join(baseUrl, '/statics/images/home-page/icon-topic.png'),
                'logo_1': os.path.join(baseUrl, '/statics/images/home-page/icon-topic-1.png'),
                'heated': os.path.join(baseUrl, '/statics/images/home-page/icon-topic-r.png'),
                'count': 1,
            },
            'notice': {

                'name': '公告',
                'bg_color': '#f67f79',
                'color': '#ffffff',
                'icon': os.path.join(baseUrl, '/statics/images/home-page/icon-notice.png')

            },
            'video': [
                {
                    'name': 0,
                    'url': '',
                    'pic_url': '',
                },
                {
                    'name': 1,
                    'url': '',
                    'pic_url': '',
                },
            ],
            'coupon': {
                'bg': os.path.join(baseUrl, '/statics/images/home-page/icon-coupon-index.png'),
                'bg_1': os.path.join(baseUrl, '/statics/images/home-page/icon-coupon-no.png'),
            }
        }

    def get_miaosha_data(self):
        return {
            "code": 1,
            "msg": "暂无秒杀安排"
        }

    def get_pintuan_data(self):
        return {
            "goods_list": [
                {
                    "id": "1",
                    "pic": "http://img.alicdn.com/imgextra/i4/268451883/O1CN01Y5GFAb1PmSI5WPJWQ_!!0-item_pic.jpg",
                    "name": "当天发货【立减100元!送延保/送壳膜】iphonex Apple/苹果 iPhone X 全网通手机咨询苹果x 10 xs max xr",
                    "price": "6288.00",
                    "sale_num": 0
                },
                {
                    "id": "4",
                    "pic": "http://img.alicdn.com/imgextra/i1/1064168367/O1CN01njRg5n2Bg8MGieHQg_!!1064168367.jpg",
                    "name": "分期免息Apple/苹果 iPhone X 苹果x 5.8英寸iphonex美版国行手机",
                    "price": "4688.00",
                    "sale_num": 761
                },
                {
                    "id": "3",
                    "pic": "http://img.alicdn.com/imgextra/i1/2131348855/O1CN01EFWG9S2FHdefFNryh_!!2131348855.jpg",
                    "name": "Apple/苹果 iPhone X 苹果x 港版4G智能手机全新iphonex 国行美版",
                    "price": "4760.00",
                    "sale_num": 3735
                },
                {
                    "id": "2",
                    "pic": "http://img.alicdn.com/imgextra/i3/1776456424/O1CN010Ui9vX1xKEpBjq2MD_!!0-item_pic.jpg",
                    "name": "现货12分期/送购机壕礼苹果x 中移动Apple/苹果 iPhone X iphonex全网通4G手机iphone xr",
                    "price": "6288.00",
                    "sale_num": 57
                }
            ]
        }

    def get_yuyue_data(self):
        return [
            {
                "id": "1",
                "name": "mac pro",
                "cover_pic": "http://123.56.8.39/addons/zjhj_mall/core/web/uploads/image/store_2/17d7e3855ef34d239eb004a848a11238bc14f27c.jpg",
                "price": "1.00"
            }
        ]

    def get_act_modal_list(self):
        return []

    def get_banner_list(self):
        return [
            {
                "id": "1",
                "store_id": "2",
                "pic_url": "http://123.56.8.39/addons/zjhj_mall/core/web/uploads/image/store_2/1513dcf37ec18b32768efe3839d525327620ed16.jpeg",
                "title": "测试1",
                "page_url": "/pages/index/index",
                "sort": "100",
                "addtime": "1550673009",
                "is_delete": "0",
                "type": "1",
                "open_type": "navigate"
            },
            {
                "id": "2",
                "store_id": "2",
                "pic_url": "http://123.56.8.39/addons/zjhj_mall/core/web/uploads/image/store_2/4544a09548a99bbad232f0afb8b060e491544247.jpeg",
                "title": "测试2",
                "page_url": "/pages/member/member",
                "sort": "100",
                "addtime": "1550673029",
                "is_delete": "0",
                "type": "1",
                "open_type": "navigate"
            },
            {
                "id": "3",
                "store_id": "2",
                "pic_url": "http://123.56.8.39/addons/zjhj_mall/core/web/uploads/image/store_2/580154c205f4897a3c7fb89a744dac07d56daf9a.png",
                "title": "测试3",
                "page_url": "/pages/user/user",
                "sort": "100",
                "addtime": "1550673045",
                "is_delete": "0",
                "type": "1",
                "open_type": "navigate"
            }
        ]

    def get_coupon_list(self):
        """
        获取美券
        :return:
        """
        return []

    def get_module_list(self):
        return [
            {
                "name": "search"
            },
            {
                "name": "banner"
            },
            {
                "name": "block",
                "block_id": "2"
            },
            {
                "name": "pintuan"
            },
            {
                "name": "yuyue"
            }
        ]

    def get_nav_icon_list(self):
        return [
            {
                "name": "导航2",
                "pic_url": "http://123.56.8.39/addons/zjhj_mall/core/web/uploads/image/store_2/580154c205f4897a3c7fb89a744dac07d56daf9a.png",
                "url": "/pages/cart/cart",
                "open_type": "navigate"
            },
            {
                "name": "导航4",
                "pic_url": "http://123.56.8.39/addons/zjhj_mall/core/web/uploads/image/store_2/1204ac0816d435c93a64e2b9d720f25330c85144.png",
                "url": "/pages/user/user",
                "open_type": "navigate"
            },
            {
                "name": "导航栏1",
                "pic_url": "http://123.56.8.39/addons/zjhj_mall/core/web/uploads/image/store_2/695c4014e11794d79987b3e4a4db14dbb4278642.jpg",
                "url": "/pages/index/index",
                "open_type": "navigate"
            },
            {
                "name": "导航3",
                "pic_url": "http://123.56.8.39/addons/zjhj_mall/core/web/uploads/image/store_2/c82357787e8a698800989af1eb0818161ca34ffa.jpg",
                "url": "/pages/order/order?status=2",
                "open_type": "navigate"
            }
        ]

    def get_cat_list(self):
        return []

    def get_block_list(self):
        return [
            {
                "id": 1,
                "name": "这是一个测试板块",
                "data": {
                    "pic_list": [
                        {
                            "pic_url": "http://123.56.8.39/addons/zjhj_mall/core/web/uploads/image/store_2/39d85ad4281ef99745541a01f7b3d306730e6855.jpg",
                            "url": "/pages/index/index",
                            "open_type": "navigate"
                        }
                    ]
                },
                "style": 0
            },
            {
                "id": 2,
                "name": "板块测试2",
                "data": {
                    "pic_list": [
                        {
                            "pic_url": "http://123.56.8.39/addons/zjhj_mall/core/web/uploads/image/store_2/85828b91ceed14c1b44947d6350ed1b11749c0d5.jpg",
                            "url": "/pages/pt/order/order",
                            "open_type": "navigate"
                        }
                    ]
                },
                "style": 0
            }
        ]

    def get_update_list(self):
        return {
            "topic": {
                "logo_2": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/images/home-page/icon-topic.png",
                "logo_1": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/images/home-page/icon-topic-1.png",
                "heated": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/images/home-page/icon-topic-r.png",
                "count": 1,
                "topic_list": [

                ]
            },
            "notice": {
                "name": "公告",
                "bg_color": "#f67f79",
                "color": "#ffffff",
                "icon": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/images/home-page/icon-notice.png",
                "content": ""
            },
            "video": [
                {
                    "name": 0,
                    "url": "",
                    "pic_url": ""
                }
            ],
            "coupon": {
                "bg": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/images/home-page/icon-coupon-index.png",
                "bg_1": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/images/home-page/icon-coupon-no.png",
                "coupon_list": [

                ]
            }
        }

    def get_mch_list(self):
        return []

    def get(self, request):
        _platform = request.GET.get('_platform')
        store_id = request.GET.get('store_id', 1)
        _acid = request.GET.get('_acid', 2)
        page_id = request.GET.get('page_id', -1)

        if not store_id:
            return self.error(code=1, msg=u'Store不存在')

        data = {
            'module_list': self.get_module_list(),
            'store': self.get_store_data(store_id),
            'banner_list': self.get_banner_list(),
            'nav_icon_list': self.get_nav_icon_list(),
            'cat_goods_cols': 3,  # 首页分类商品列数
            'cat_list': self.get_cat_list(),
            'block_list': self.get_block_list(),
            'coupon_list': self.get_coupon_list(),
            'topic_list': self.get_topic_list(baseUrl=request.META['HTTP_HOST']),
            'nav_count': 0,
            'notice': '',
            'miaosha': self.get_miaosha_data(),
            'pintuan': self.get_pintuan_data(),
            'yuyue': self.get_yuyue_data(),
            'update_list': self.get_nav_icon_list(),
            'act_modal_list': self.get_act_modal_list(),
            'mch_list': self.get_mch_list(),
            'template': False
        }

        return self.ok(code=0, msg='success', data=data)


class DefaultStore(BaseView):

    def getShareSetting(self):
        """
        分销设置
        :return:
        """
        return {
            "id": "1",
            "first": "0.00",
            "second": "0.00",
            "third": "0.00",
            "store_id": "2",
            "level": "0",
            "condition": "0",
            "share_condition": "0",
            "content": None,
            "pay_type": "0",
            "min_money": "1.00",
            "agree": None,
            "first_name": None,
            "second_name": None,
            "third_name": None,
            "pic_url_1": None,
            "pic_url_2": None,
            "price_type": "0",
            "bank": None,
            "remaining_sum": "0",
            "rebate": "0.00",
            "is_rebate": "0",
            "share_good_status": "0",
            "share_good_id": "0",
            "qrcode_bg": ""
        }

    def wxDefaultTitle(self):
        return [
            {
                'url': 'pages/share/index',
                'title': '分销中心',
            },
            {
                'url': 'pages/user/user',
                'title': '个人中心',
            },
            {
                'url': 'pages/pt/index/index',
                'title': '拼团',
            },
            {
                'url': 'pages/book/index/index',
                'title': '预约',
            },
            {
                'url': 'pages/fxhb/open/open',
                'title': '拆红包',
            },
            {
                'url': 'mch/shop-list/shop-list',
                'title': '好店推荐',
            },
            {
                'url': 'pages/cart/cart',
                'title': '购物车',
            },
            {
                'url': 'pages/cat/cat',
                'title': '分类',
            },
            {
                'url': 'pages/coupon/coupon',
                'title': '我的优惠券',
            },
            {
                'url': 'pages/coupon-list/coupon-list',
                'title': '领券中心',
            },
            {
                'url': 'pages/favorite/favorite',
                'title': '我的收藏',
            },
            {
                'url': 'mch/m/myshop/myshop',
                'title': '我的店铺',
            },
            {
                'url': 'mch/shop/shop',
                'title': '店铺首页',
            },
            {
                'url': 'pages/integral-mall/index/index',
                'title': '积分商城',
            },
            {
                'url': 'pages/topic-list/topic-list',
                'title': '专题',
            },
            {
                'url': 'pages/topic/topic',
                'title': '专题详情',
            },
        ]

    def get_data(self):
        return {
            "id": 2,
            "name": "MesShop商城",
            "copyright": "",
            "copyright_pic_url": None,
            "copyright_url": None,
            "contact_tel": "",
            "show_customer_service": 1,
            "cat_style": 1,
            "address": None,
            "is_offline": 0,
            "is_coupon": 1,
            "is_comment": 1,
            "is_share_price": 1,
            "is_member_price": 1,
            "dial": None,
            "dial_pic": None,
            "service": "",
            "cut_thread": None,
            "option": {
                "step": "",
                "service": "",
                "web_service": "",
                "web_service_url": "",
                "wxapp": None,
                "quick_navigation": {

                },
                "phone_auth": "",
                "good_negotiable": {

                },
                "quick_map": "",
                "web_service_status": ""
            },
            "purchase_frame": 0,
            "is_sales": 1,
            "quick_navigation": {

            },
            "good_negotiable": {

            },
            "buy_member": 0,
            "logo": None,
            "is_official_account": 0,
            "share_custom_data": {
                "menus": {
                    "money": {
                        "name": "分销佣金",
                        "icon": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/images/share-custom/img-share-price.png",
                        "open_type": "navigator",
                        "url": "/pages/share-money/share-money",
                        "tel": ""
                    },
                    "order": {
                        "name": "分销订单",
                        "icon": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/images/share-custom/img-share-order.png",
                        "open_type": "navigator",
                        "url": "/pages/share-order/share-order",
                        "tel": ""
                    },
                    "cash": {
                        "name": "提现明细",
                        "icon": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/images/share-custom/img-share-cash.png",
                        "open_type": "navigator",
                        "url": "/pages/cash-detail/cash-detail",
                        "tel": ""
                    },
                    "team": {
                        "name": "我的团队",
                        "icon": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/images/share-custom/img-share-team.png",
                        "open_type": "navigator",
                        "url": "/pages/share-team/share-team",
                        "tel": ""
                    },
                    "qrcode": {
                        "name": "推广二维码",
                        "icon": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/images/share-custom/img-share-qrcode.png",
                        "open_type": "navigator",
                        "url": "/pages/share-qrcode/share-qrcode",
                        "tel": ""
                    }
                },
                "words": {
                    "can_be_presented": {
                        "name": "可提现佣金",
                        "default": "可提现佣金"
                    },
                    "already_presented": {
                        "name": "已提现佣金",
                        "default": "已提现佣金"
                    },
                    "parent_name": {
                        "name": "推荐人",
                        "default": "推荐人"
                    },
                    "pending_money": {
                        "name": "待打款佣金",
                        "default": "待打款佣金"
                    },
                    "cash": {
                        "name": "提现",
                        "default": "提现"
                    },
                    "user_instructions": {
                        "name": "用户须知",
                        "default": "用户须知"
                    },
                    "apply_cash": {
                        "name": "我要提现",
                        "default": "我要提现"
                    },
                    "cash_type": {
                        "name": "提现方式",
                        "default": "提现方式"
                    },
                    "cash_money": {
                        "name": "提现金额",
                        "default": "提现金额"
                    },
                    "order_money_un": {
                        "name": "未结算佣金",
                        "default": "未结算佣金"
                    },
                    "share_name": {
                        "name": "分销商",
                        "default": "分销商"
                    }
                }
            }
        }

    def search(self, baseUrl=None):
        wxappUrl = os.path.join(baseUrl, 'static/wxapp/images')
        images = {
            "integralMall": {
                "register": {
                    "register_bg": {
                        "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/register.png"
                    }
                }
            },
            "pond": {
                "pond": {
                    "pond_head": {
                        "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/pond-head.png"
                    },
                    "pond_success": {
                        "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/pond-success.png"
                    },
                    "pond_empty": {
                        "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/pond-empty.png"
                    }
                }
            },
            "bargain": {
                "bargain_goods": {
                    "time_bg": {
                        "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-bargain-time.png"
                    },
                    "flow": {
                        "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-bargain-flow.png"
                    },
                    "click": {
                        "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-bargain-click.png"
                    },
                    "help": {
                        "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-bargain-help.png"
                    },
                    "price": {
                        "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-bargain-price.png"
                    },
                    "buy": {
                        "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-bargain-buy.png"
                    },
                    "jiantou": {
                        "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-bargain-jiantou.png"
                    },
                    "shuoming": {
                        "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-bargain-shuoming.png"
                    },
                    "goods": {
                        "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-bargain-goods.png"
                    }
                },
                "activity": {
                    "bg": {
                        "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-bargain-bg.png"
                    },
                    "buy": {
                        "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-bargain-activity-buy.png"
                    },
                    "continue": {
                        "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-bargain-activity-c.png"
                    },
                    "progress": {
                        "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-bargain-activity-progress.png"
                    },
                    "used": {
                        "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-bargain-activity-used.png"
                    },
                    "down": {
                        "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-bargain-activity-jiantou-down.png"
                    },
                    "up": {
                        "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-bargain-activity-jiantou-up.png"
                    },
                    "join": {
                        "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-bargain-activity-join.png"
                    },
                    "header_bg": {
                        "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-bargain-activity-header.png"
                    },
                    "help": {
                        "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-bargain-activity-help.png"
                    },
                    "join_m": {
                        "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-bargain-activity-join-m.png"
                    },
                    "x": {
                        "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-bargain-activity-x.png"
                    },
                    "more": {
                        "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-bargain-activity-more.png"
                    },
                    "buy_b": {
                        "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-bargain-activity-buy-b.png"
                    },
                    "header_bg_1": {
                        "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-bargain-activity-header-1.png"
                    },
                    "header_bg_2": {
                        "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-bargain-activity-header-2.png"
                    },
                    "header_bg_3": {
                        "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-bargain-activity-header-3.gif"
                    }
                },
                "list": {
                    "right": {
                        "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-bargain-list-right.png"
                    }
                }
            },
            "store": {
                "disabled": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/disabled.png"
                },
                "bg": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/bg.png"
                },
                "car": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/car.png"
                },
                "binding_pic": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/binding-pic.png"
                },
                "gold": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/gold.png"
                },
                "clear": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/clear.png"
                },
                "good_recommend": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/good-recommend.png"
                },
                "guige": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/guige.jpg"
                },
                "home_gwc": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/home-gwc.png"
                },
                "huiyuan_bg": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/huiyuan-bg.png"
                },
                "check": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-check.png"
                },
                "checked": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-checked.png"
                },
                "clerk": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-clerk.png"
                },
                "close": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-close.png"
                },
                "close2": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-close2.png"
                },
                "close3": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-close3.png"
                },
                "close4": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-close4.png"
                },
                "delete": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-delete.png"
                },
                "detail_love": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-detail-love.png"
                },
                "edit": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-edit.png"
                },
                "favorite": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-favorite.png"
                },
                "favorite_active": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-favorite-active.png"
                },
                "good_shop": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-good-shop.png"
                },
                "group_share": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-group-share.png"
                },
                "image_picker": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-image-picker.png"
                },
                "jiantou_r": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-jiantou-r.png"
                },
                "member_rights": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-member-rights.png"
                },
                "my_exchange": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-my-exchange.png"
                },
                "ntegration": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-ntegration.png"
                },
                "pay_right": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-pay-right.png"
                },
                "icon_play": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-play.png"
                },
                "service": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-service.png"
                },
                "shuoming": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-shuoming.png"
                },
                "store": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-store.png"
                },
                "time_bg": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-time-bg.png"
                },
                "time_split": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-time-split.png"
                },
                "uncheck": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-uncheck.png"
                },
                "up": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-up.png"
                },
                "address": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-address.png"
                },
                "order_status_bar": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/img-order-status-bar.png"
                },
                "pc_login": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/img-pc-login.png"
                },
                "jia": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/jia.png"
                },
                "jian": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/jian.png"
                },
                "jiangli": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/jiangli.png"
                },
                "quick_hot": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/quick-hot.png"
                },
                "search_index": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/serach-index-icon.png"
                },
                "shou": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/shou.png"
                },
                "video_play": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/video-play.png"
                },
                "yougoods": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/yougoods.jpg"
                },
                "binding": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/binding.png",
                    "remark": "绑定公众号"
                },
                "binding_yes": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/binding_yes.png",
                    "remark": "已绑定公众号"
                },
                "share_commission": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/share_commission.png",
                    "remark": "商品详情分销价"
                },
                "member_price": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/member_price.png",
                    "remark": "商品详情会员价"
                }
            },
            "pt": {
                "active": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/ico-pt-active.png"
                },
                "text": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-pt-text.png"
                },
                "group_bg": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-pt-group-bg.png"
                },
                "address_bottom": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/pt-addres-bottom.png"
                },
                "address_top": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/pt-addres-top.png"
                },
                "address": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/pt-address.png"
                },
                "details": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/pt-details-pt.png"
                },
                "empty_order": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/pt-empty-order.png"
                },
                "fail": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/pt-fail.png"
                },
                "favorite": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/pt-favorite.png"
                },
                "go_home": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/pt-go-home.png"
                },
                "no_group_num": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/pt-no-group-num-pic.png"
                },
                "search_clear": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/pt-search-clear.png"
                },
                "search": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/pt-search-icon.png"
                },
                "shop_car": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/pt-shop-car.png"
                },
                "success": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/pt-success.png"
                }
            },
            "balance": {
                "left": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-balance-left.png"
                },
                "right": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-balance-right.png"
                },
                "recharge": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-balance-recharge.png"
                },
                "recharge_bg": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-balance-recharge-bg.png"
                }
            },
            "card": {
                "btn": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-card-btn.png"
                },
                "del": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-card-del.png"
                },
                "qrcode": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-card-qrcode.png"
                },
                "top": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-card-top.png"
                }
            },
            "coupon": {
                "coupon": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-coupon.png"
                },
                "disabled": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-coupon-disabled.png"
                },
                "enabled": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-coupon-enabled.png"
                },
                "index": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-coupon-index.png"
                },
                "no": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-coupon-no.png"
                },
                "bg": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/img-get-coupon-bg.png"
                },
                "item_bg": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/img-get-coupon-item-bg.png"
                }
            },
            "system": {
                "wechatapp": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-wechatapp.png"
                },
                "yuyue": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-yuyue.png"
                },
                "loading": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/loading.svg"
                },
                "loading2": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/loading2.svg"
                },
                "loading_black": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/loading-black.svg"
                },
                "alipay": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-alipay.png"
                }
            },
            "integral": {
                "all": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-integral-all.png"
                },
                "close": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-integral-close.png"
                },
                "detail": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-integral-detail.png"
                },
                "head": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-integral-head.png"
                },
                "shibai": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-integral-shibai.png"
                },
                "success": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-integral-success.png"
                }
            },
            "miaosha": {
                "miaosha": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-miaosha.png"
                },
                "ms_activity_bg": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/ms_activity_bg.png",
                    "remark": "秒杀活动到计时背景图"
                }
            },
            "notice": {
                "jiantou": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-notice-jiantou.png"
                },
                "title": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-notice-title.png"
                },
                "notice": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-notice.png"
                }
            },
            "point": {
                "gray": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-point-gray.png"
                },
                "green": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-point-green.png"
                }
            },
            "register": {
                "register": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-register.png"
                },
                "is_register": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-is-register.png"
                },
                "close": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-register-close.png"
                },
                "head": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-register-head.png"
                },
                "left": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-register-left.png"
                },
                "right": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-register-right.png"
                },
                "quan": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-register-quan.png"
                },
                "sign_in": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-register-sign-in.png"
                }
            },
            "search": {
                "search": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-search.png"
                },
                "search_no": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-search-no.png"
                },
                "s_up": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/search_up.png"
                }
            },
            "share": {
                "share": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-share.png"
                },
                "ant": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-share-ant.png"
                },
                "bank": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-share-bank.png"
                },
                "friend": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-share-friend.png"
                },
                "qrcode": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-share-qrcode.png"
                },
                "selected": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-share-selected.png"
                },
                "tip": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-share-tip.png"
                },
                "wechat": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-share-wechat.png"
                },
                "down": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/img-share-down.png"
                },
                "info": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/img-share-info.png"
                },
                "money": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/img-share-money.png"
                },
                "img_qrcode": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/img-share-qrcode.png"
                },
                "right": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/img-share-right.png"
                },
                "shop": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/img-share-shop.png"
                }
            },
            "shop": {
                "dingwei": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-shop-dingwei.png"
                },
                "love": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-shop-love.png"
                },
                "nav": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-shop-nav.png"
                },
                "nav_one": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-shop-nav-1.png"
                },
                "search": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-shop-search.png"
                },
                "tel": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-shop-tel.png"
                },
                "down": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-shop-down.png"
                }
            },
            "sort": {
                "down": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-sort-down.png"
                },
                "down_active": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-sort-down-active.png"
                },
                "up": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-sort-up.png"
                },
                "up_active": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-sort-up-active.png"
                }
            },
            "topic": {
                "love": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-topic-love.png"
                },
                "love_active": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-topic-love-active.png"
                },
                "share": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-topic-share.png"
                }
            },
            "user": {
                "kf": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-user-kf.png"
                },
                "level": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-user-level.png"
                },
                "balance": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-user-balance.png"
                },
                "wallet": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-user-wallet.png"
                },
                "integral": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-user-integral.png"
                },
                "coupon_xia": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/user-coupon-xia.png"
                }
            },
            "cart": {
                "add": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/cart-add.png"
                },
                "less": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/cart-less.png"
                },
                "no_add": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/cart-no-add.png"
                },
                "no_less": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/cart-no-less.png"
                }
            },
            "nav": {
                "cart": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/nav-icon-cart.png"
                },
                "index": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/nav-icon-index.png"
                }
            },
            "yy": {
                "form_title": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/yy-form-title.png"
                }
            },
            "scratch": {
                "index": {
                    "scratch_bg": {
                        "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/scratch_bg.png"
                    },
                    "scratch_success": {
                        "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/scratch_success.png"
                    }
                }
            },
            "goods": {
                "goods": {
                    "address": {
                        "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-goods-address.png"
                    }
                }
            },
            "step": {
                "dare_bg": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/dare-bg.png"
                },
                "home_bg": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/home-bg.png"
                },
                "join_bg": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/join-bg.png"
                },
                "detail_bg": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/detail-bg.png"
                },
                "log_bg": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/log-bg.png"
                }
            },
            "lottery": {
                "time": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/lottery_time.png"
                }
            },
            "cell": {
                "cell_1": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-cell-1.png"
                },
                "cell_2": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-cell-2.png"
                },
                "cell_3": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-cell-3.png"
                },
                "cell_4": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-cell-4.png"
                },
                "cell_5": {
                    "url": "http://123.56.8.39/addons/zjhj_mall/core/web/statics/wxapp/images/icon-cell-5.png"
                }
            }
        }
        return images

    def index(self):
        return self.wxDefaultTitle()

    def get_permission_list(self):
        return [
            "miaosha",
            "pintuan",
            "book",
            "fxhb",
            "mch",
            "integralmall",
            "permission",
            "pond",
            "scratch",
            "coupon",
            "share",
            "topic",
            "video",
            "copyright",
            "bargain",
            "alipay",
            "lottery",
            "step",
            "diy",
            "gwd"
        ]

    def get_config(self, baseUrl=None):
        # 服务器图片
        wxappImg = self.search(baseUrl=baseUrl)

        # 小程序页面标题
        wxBarTitle = self.index()

        # 商城配置信息
        data = self.get_data()

        # 支付宝配置
        alipay_mp_config = {
            'cs_tnt_inst_id': None,
            'cs_scene': None
        }

        config = {
            'share_setting': self.getShareSetting(),
            'wxapp_img': wxappImg,
            'wx_bar_title': wxBarTitle,
            'store_name': '我爱罗',
            'contact_tel': '12343242342342',
            'show_customer_service': 1,
            'store': data,
            'alipay_mp_config': alipay_mp_config,
            'permission_list': self.get_permission_list(),
        }
        return config

    def get(self, request):
        store_id = request.GET.get('store_id', 1)
        if not store_id:
            return self.error(code=1, msg='Store Is NULL')

        data = self.get_config(baseUrl=request.META['HTTP_HOST'])

        return self.ok(code=0, msg='success', data=data)


class DefaultNavbar(BaseView):

    def get_navbar(self, store_id=None, path=None):
        if not store_id:
            default_navbar = {
                'background_image': 'data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAEAAAABAQMAAAAl21bKAAAAA1BMVEX///+nxBvIAAAACklEQVQI12NgAAAAAgAB4iG8MwAAAABJRU5ErkJggg==',
                'border_color': 'rgba(0,0,0,.1)',
                'navs': [
                    {
                        'url': 'pages/index/index',
                        'icon': os.path.join(path, 'static/images/appnavbar/nav-icon-index.png'),
                        'active_icon': os.path.join(path, 'static/images/appnavbar/nav-icon-index.active.png'),
                        'text': '商城',
                        'color': '#888',
                        'active_color': "#ff4544",
                    },
                    {
                        'url': 'pages/cat/cat',
                        'icon': os.path.join(path, 'static/images/appnavbar/nav-icon-cat.png'),
                        'active_icon': os.path.join(path, 'static/images/appnavbar/nav-icon-cat.active.png'),
                        'text': '分类',
                        'color': '#888',
                        'active_color': '#ff4544',
                    },
                    {
                        'url': 'pages/cart/cart',
                        'icon': os.path.join(path, 'static/images/appnavbar/nav-icon-cart.png'),
                        'active_icon': os.path.join(path, 'static/images/appnavbar/nav-icon-cart.active.png'),
                        'text': '购物车',
                        'color': '#888',
                        'active_color': '#ff4544',
                    },
                    {
                        'url': 'pages/user/user',
                        'icon': os.path.join(path, 'static/images/appnavbar/nav-icon-user.png'),
                        'active_icon': os.path.join(path, 'static/images/appnavbar/nav-icon-user.active.png'),
                        'text': '我',
                        'color': '#888',
                        'active_color': '#ff4544',
                    },
                ],
            }
        else:
            default_navbar = {}

        return default_navbar

    def get(self, request):
        """
        底部导航栏
        :param request:
        :return:
        """
        data = self.get_navbar(path=request.META['HTTP_HOST'])
        return self.ok(code=0, msg='success', data=data)


class DefaultNavigation(BaseView):

    def get_background_color(self, store_id=None):
        if not store_id:
            default = {
                'frontColor': '#000000',
                'backgroundColor': '#eee8e8',
                'bottomBackgroundColor': '#ffffff',
            }
        else:
            default = {}

        return default

    def get(self, request):
        """
        顶部导航栏颜色
        :param request:
        :return:
        """
        store_id = request.GET.get('store_id')
        data = self.get_background_color(store_id=store_id)
        return self.ok(code=0, msg='success', data=data)
