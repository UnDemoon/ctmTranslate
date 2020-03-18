#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2018-1-31 15:09:44
# @Author  : Demoon (a_share@sina.com)
# @Link    :
# @Version : $Id$
# @title   :

import http.client
import hashlib
import urllib
import random

#引入谷歌翻译模块
from googletrans import Translator

appid = '20151113000005349'
secretKey = 'osubCEzlGjzvw8qdQc41'


def bdTrans(words, fromL='auto', toL='zh'):
    res = {
    'state':False,
    'connect':''
    }
    httpClient = None
    myurl = '/api/trans/vip/translate'
    q = words
    fromLang = fromL
    toLang = toL
    salt = random.randint(32768, 65536)

    sign = appid+q+str(salt)+secretKey
    m1 = hashlib.md5()
    m1.update(sign.encode("utf-8"))
    sign = m1.hexdigest()
    myurl = myurl+'?appid='+appid+'&q='+urllib.request.quote(q)+'&from='+fromLang+'&to='+toLang+'&salt='+str(salt)+'&sign='+sign
    #myurl = 'http://fanyi.youdao.com/openapi.do?keyfrom=<keyfrom>&key=<key>&type=data&doctype=xml&version=1.1&q=这里是有道翻译API'
    try:
        httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
        httpClient.request('GET', myurl)

        response = httpClient.getresponse()
        res['state'] = True
        res['connect'] = response.read()
    except e:
        res['state'] = False
        res['connect'] = e
    finally:
        if httpClient:
            httpClient.close()
    return res
