# -*- coding: utf-8 -*-
from Public.fengzhuang_dict import res
from Public.log import LOG, logger


@logger('断言测试结果')
def assert_in(asserqiwang, fanhuijson):
    """ assertqiwang的格式是：xx=yy """
    if len(asserqiwang.split('=')) >= 1:    # xx.split('=') xx转换后的格式是：['xx', 'yy']
        data = asserqiwang.split('&')       # xx.split('&') xx转换后的格式是：['xx=yy']
        result = dict([(item.split('=')) for item in data])     # 此处是把 assertqiwang 转成 dict：{'xx': 'yy'}
        # result.keys() 表示result中的项; result.values()表示各项的值
        key = ([str(key) for key in result.keys()])[0]
        # value1 = ([(str(res(fanhuijson, key))) for key in result.keys()])
        value1 = res(fanhuijson, key)
        LOG.info('实际返回的值：{}'.format(value1))
        value2 = ([(str(value)) for value in result.values()])
        LOG.info('期望得到的结果：{}'.format(value2))
        if value1 == value2:
            return {'code': 200, "result": 'pass'}
        else:
            return {'code': 1001, 'result': 'fail'}
    else:
        LOG.info('填写测试预期值')
        return {"code": 1002, 'result': '填写测试预期值'}


@logger('断言测试结果')
def assertre(asserqingwang):
    if len(asserqingwang.split('=')) > 1:
        data = asserqingwang.split('&')
        result = dict([(item.split('=')) for item in data])
        return result
    else:
        LOG.info('填写测试预期值')
        return {"code": 200, 'result': '填写测试预期值'}


if __name__ == '__main__':
    fanhui = {'code': '0', 'result': {'code': '200', 'msg': 'ok', 'result': '操作成功', 'location': {'province': '四川', 'city': '成都', 'area': '高新区', 'address': '成都市武侯区世纪城南路156号附近'}}}
    string = 'code=0'
    LOG.info(string)
    res = assert_in(string, fanhui)
    LOG.info(res)
