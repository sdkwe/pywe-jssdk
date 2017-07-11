# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import time

import shortuuid
from pywe_sign import jsapi_signature
from pywe_ticket import ticket


__all__ = ['jsapi_signature_params']


def jsapi_signature_params(appid=None, secret=None, url=None, storage=None):
    nonceStr, timestamp = shortuuid.uuid(), int(time.time())
    data = {
        'noncestr': nonceStr,
        'jsapi_ticket': ticket(appid, secret, storage=storage),
        'timestamp': timestamp,
        'url': ''.join(url.split('#')[:-1])
    }
    signature = jsapi_signature(data)
    return {
        'appId': appid,
        'nonceStr': nonceStr,
        'timestamp': timestamp,
        'signature': signature,
    }
