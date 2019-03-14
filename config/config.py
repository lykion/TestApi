# -*- coding:utf-8 -*-
"""https://github.com/liwanlei/jiekou-python3/blob/master/run_http_html.py"""
Case_Fail_Try_Num = 3   # 失败重试次数

"""Excel"""
CASE_PATH = "F:\PyCharmProject\Kentra\jiekou_python3\\test_case_data\Text_Case.xlsx"    # Excel路径
CASE_SHEET_NAME = 'TestCase'    # 测试用例sheet的名字
CASE_ID = 1         # 用例ID
CASE_NAME = 2       # 用例名称
CASE_IS_HEADER = 3  # 是否有请求头
CASE_HEADER = 4     # 请求头
CASE_DATA = 5       # 参数
CASE_URL = 6        # url
CASE_METHOD = 7     # 请求方式
CASE_EXPECT = 8     # 断言
CASE_TEST_RESULT = 9    # 测试结果
CASE_TEST_TIME = 10     # 执行时间
CASE_ACTUAL_RESPONSE = 11   # 实际返回结果

"""Host"""
HOST = 'http://127.0.0.1:5025'
TEST_URL_1 = 'http://127.0.0.1:5025/do/extra'
TEST_URL_2 = 'http://127.0.0.1:5025/do/location'

"""调试使用"""
DATA_1 = {"OrderCode": "1002", "ShipperCode": "SF", "LogisticCode": "118652124588863"}
DATA_2 = {"lat": "30.544353", "lon": "104.074007"}
HEADER = {'Content-Type': 'application/json'}
# import requests
# import json
# res = requests.post(TEST_URL_1, json.dumps(DATA_1))
# res = requests.post(TEST_URL_2, json.dumps(DATA_2))
# print(res.json())
# print(type(json.dumps(DATA_1)))
