# -*- coding: UTF-8 -*-
import base64
import datetime
import hashlib
import hmac
import requests

# Tip 1
# 使用时需要根据自己配置与需求提供参数 key secret uri method

class config:
    user = 'None'
    passwd = 'None'
    bucket = "None"

def httpdate_rfc1123(dt=None):
    dt = dt or datetime.datetime.utcnow()
    return dt.strftime('%a, %d %b %Y %H:%M:%S GMT')

def MD5(value):
    return hashlib.md5(value.encode()).hexdigest()

def sign(client_key, client_secret, method, uri, date, policy=None, md5=None):
    # Tip 4
    # MD5 信息可选
    print method, uri
    client_secret = MD5(client_secret)
    signarr = []
    for v in [method, uri, date, policy, md5]:
        if v != None:
            signarr.append(v)
    signstr = '&'.join(signarr)
    signstr = base64.b64encode(
        hmac.new(client_secret.encode(), signstr.encode(),
                 digestmod=hashlib.sha1).digest()
    ).decode()
    return 'UPYUN %s:%s' % (client_key, signstr)

def putfile(local_path, url_path):
    c = open(local_path).read()
    gmt = httpdate_rfc1123()

    method = 'PUT'

    url_path = '/%s%s' % (config.bucket, url_path)

    url = "http://v0.api.upyun.com%s" % url_path

    headers = {}
    sg = sign(config.user, config.passwd, method, url_path, gmt)
    headers['Authorization'] = sg
    headers['Date']          = gmt

    res = requests.request(method, url, data = c, headers = headers)
    return res


