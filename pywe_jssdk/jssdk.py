# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import time

import shortuuid
from pywe_sign import jsapi_signature
from pywe_ticket import ticket


__all__ = ['jsapi_signature_params']


def jsapi_signature_params(appid=None, secret=None, url=None, token=None, storage=None, token_fetched_func=None, ticket_fetched_func=None, full=False):
    nonceStr, timestamp, tk, url = shortuuid.uuid(), int(time.time()), ticket(appid, secret, token=token, storage=storage, token_fetched_func=token_fetched_func, ticket_fetched_func=ticket_fetched_func), url.split('#')[0]
    data = {
        'noncestr': nonceStr,
        'jsapi_ticket': tk,
        'timestamp': timestamp,
        'url': url
    }
    signature = jsapi_signature(data)
    params = {
        'appId': appid,
        'nonceStr': nonceStr,
        'timestamp': timestamp,
        'signature': signature,
    }
    if full:
        params['ticket'] = tk
        params['url'] = url
    return params
