# -*- coding:utf-8 -*-
#    author    :   丁雪峰
#    time      :   2019-03-16 22:07:15
#    email     :   fengidri@yeah.net
#    version   :   1.0.1



import os
import json
conf = open(os.path.expanduser("~/.httppic.json")).read()
conf = json.loads(conf)

public = conf['public']
private = conf['private']
domain = conf['domain']

class upyun:
    user = conf['upyun']['user']
    passwd = conf['upyun']['password']
    bucket = conf['upyun']['bucket']



