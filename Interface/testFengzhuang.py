# -*- coding: utf-8 -*-
from Public.test_requests import requ
""" 接口二次封装 """
# reques = requ()


class TestApi:
    def __init__(self, url, data, fangshi):
        self.url = url
        self.data = data
        self.fangshi = fangshi

    def testapi(self):
        if self.fangshi == 'POST' or self.fangshi == 'post':
            self.response = requ.post(self.url, self.data)
            return self.response
        elif self.fangshi == 'GET' or self.fangshi == 'get':
            self.response = requ.get(self.url, self.data)
            return self.response

    def getJson(self):
        json_data = self.testapi()
        return json_data


if __name__ == '__main__':
    TEST_URL_1 = 'http://127.0.0.1:5025/do/extra'
    DATA_1 = {"OrderCode": "1002", "ShipperCode": "SF", "LogisticCode": "118652124588863"}
    METHOD = 'POST'
    api = TestApi(TEST_URL_1, DATA_1, METHOD)
    res = api.getJson()
    print(res)
