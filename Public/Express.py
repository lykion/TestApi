# -*- coding:utf-8 -*-
import requests
import json
import config.config as cf


def send_demo(content):
    url = cf.TEST_URL_1
    param = cf.DATA_1
    f = requests.post(url, json.dumps(param))
    if f.status_code == 200:
        return True
    else:
        return False
