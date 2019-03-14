# -*- coding: utf-8 -*-
import requests
import json
import xlrd
from Public.log import LOG, logger
from Public.get_excel import datacel
import config.config as cf


@logger('requests封装')
class requ():

    def get(url, param):  # get消息
        try:
            r = requests.get(url, param)
            r.encoding = 'UTF-8'
            json_response = json.loads(r.text)
            return {'code': '200', 'result': json_response}
        except Exception as e:
            LOG.info('get请求出错，出错原因:%s' % e)
            return {'code': '1', 'result': 'get请求出错，出错原因:%s' % e}

    def post(url, param):  # post消息
        data = json.dumps(param)
        try:
            r = requests.post(url, data)
            json_response = json.loads(r.text)
            return {'code': '200', 'result': json_response}
        except Exception as e:
            LOG.info('post请求出错，出错原因:%s' % e)
            return {'code': '1', 'result': 'post请求出错，出错原因:%s' % e}


if __name__ == '__main__':
    list_id, list_name, list_is_header, list_header, list_data, list_url, list_method, list_expect = datacel(cf.CASE_PATH)
    workbook = xlrd.open_workbook(cf.CASE_PATH)
    sheet = workbook.sheets()[0]
    for i in range(len(list_url)):
        result = requ.post(cf.HOST+list_url[i], json.loads(list_data[i]))
        LOG.info(result)

