# -*- coding: utf-8 -*-
from Interface.testFengzhuang import TestApi
from Public.get_excel import datacel
from Public.log import LOG, logger
from Public.panduan import assert_in
from Public.write import write_to_excel
import os
import json
import datetime
import config.config as cf

path = cf.CASE_PATH
"""从Excel单元格取出来后的类型是string"""
listid, listname, listisheader, listheader, listdata, listurl, listfangshi, listqiwang = datacel(path)
# print(listid, listname, listisheader, listheader, listdata, listurl, listfangshi, listqiwang)


@logger('测试')
def testinterface():
    list_pass = 0
    list_fail = 0
    list_json = []
    listrelust = []
    list_weizhi = 0
    list_exption = 0
    error_num = 0
    for i in range(len(listurl)):
        while error_num <= cf.Case_Fail_Try_Num + 1:
            """需要将listdata转换成dict在传参"""
            start_time = datetime.datetime.now()
            api = TestApi(url=cf.HOST+listurl[i], data=json.loads(listdata[i]), fangshi=listfangshi[i])
            apijson = api.getJson()
            if apijson['code'] == '200':    # 注意apijson中code的值是字符串，所以判断的时候也要写成字符串类型
                LOG.info('inputdata>> 参数:%s, url:%s, 返回:%s, 预期:%s' % (listdata[i], listurl[i], apijson, listqiwang[i]))
                LOG.info("期望的返回值是：{}, 类型：{}".format(listqiwang[1], type(listqiwang[i])))
                LOG.info("接口返回的实际值是：{}".format(apijson))
                assert_re = assert_in(asserqiwang=listqiwang[i], fanhuijson=apijson)
                LOG.info('---------------------------------------------------------------------------------------------')
                LOG.info('期望结果 {}；测试用例中期望结果的类型：{}'.format(listqiwang[i], type(listqiwang[i])))
                LOG.info('接口返回的结果 {}'.format(apijson))
                LOG.info('断言结果：{}'.format(assert_re))
                LOG.info('---------------------------------------------------------------------------------------------')
                if assert_re['code'] == 200:
                    list_json.append(apijson['result'])
                    listrelust.append('pass')
                    list_pass += 1
                    error_num = 0
                    # range(len(listurl))的索引是从0开始的，所以要openpyxl调用时要+2
                    write_to_excel(cf.CASE_PATH, cf.CASE_SHEET_NAME, i+2, cf.CASE_TEST_TIME, start_time)
                    write_to_excel(cf.CASE_PATH, cf.CASE_SHEET_NAME, i+2, cf.CASE_TEST_RESULT, 'Pass')
                    write_to_excel(cf.CASE_PATH, cf.CASE_SHEET_NAME, i+2, cf.CASE_ACTUAL_RESPONSE, str(apijson['result']))
                    break                           # 如果使用continue，case会无线执行
                elif assert_re['code'] == 1001:
                    write_to_excel(cf.CASE_PATH, cf.CASE_SHEET_NAME, i + 2, cf.CASE_TEST_TIME, start_time)
                    write_to_excel(cf.CASE_PATH, cf.CASE_SHEET_NAME, i + 2, cf.CASE_TEST_RESULT, 'Fail')
                    write_to_excel(cf.CASE_PATH, cf.CASE_SHEET_NAME, i + 2, cf.CASE_ACTUAL_RESPONSE, '测试失败')
                    if error_num <= cf.Case_Fail_Try_Num:
                        error_num += 1
                        LOG.info('失败重试中')
                    else:
                        LOG.info('失败重试中次数用完，最后结果')
                        error_num = 0
                        list_fail += 1
                        listrelust.append('fail')
                        list_json.append(apijson['result'])
                        break
                elif assert_re['code'] == 1002:
                    write_to_excel(cf.CASE_PATH, cf.CASE_SHEET_NAME, i + 2, cf.CASE_TEST_TIME, start_time)
                    write_to_excel(cf.CASE_PATH, cf.CASE_SHEET_NAME, i + 2, cf.CASE_TEST_RESULT, 'Fail')
                    write_to_excel(cf.CASE_PATH, cf.CASE_SHEET_NAME, i + 2, cf.CASE_ACTUAL_RESPONSE, '测试失败')
                    if error_num < cf.Case_Fail_Try_Num:
                        error_num += 1
                        LOG.info('失败重试中')
                    else:
                        LOG.info('失败重试中次数用完，最后结果')
                        error_num = 0
                        list_exption += 1
                        listrelust.append('exception')
                        list_json.append(assert_re['result'])
                        break
                else:
                    if error_num < cf.Case_Fail_Try_Num:
                        error_num += 1
                        LOG.info('失败重试中')
                    else:
                        LOG.info('失败重试中次数用完，最后结果')
                        error_num = 0
                        list_weizhi += 1
                        listrelust.append('未知错误')
                        list_json.append('未知错误')
                        break
            else:
                if error_num < cf.Case_Fail_Try_Num:
                    error_num += 1
                    LOG.info('失败重试中')
                else:
                    LOG.info('失败重试中次数用完，最后结果')
                    error_num = 0
                    list_exption += 1
                    listrelust.append('exception')
                    list_json.append(apijson['result'])
                    break
    return listrelust, list_fail, list_pass, list_json, list_exption, list_weizhi


if __name__ == '__main__':
    res = testinterface()
    LOG.info(res)
