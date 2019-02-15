#! /usr/bin/env python
# -*- coding: utf-8 -*-
# __author__ = "chenwei"
# Date: 2019/2/15

import json
from django.http import HttpResponse


def json_response(result, status=200, extra_headers=None):
    if extra_headers is None:
        extra_headers = {}

    if 'extra' not in result:
        result['extra'] = {}

    if 'data' not in result:
        result['data'] = {}

    response = HttpResponse(
        json.dumps(result),
        content_type="application/json; charset=UTF-8",
        status=status,
    )
    for header_key, header_value in extra_headers.items():
        response[header_key] = header_value

    return response
