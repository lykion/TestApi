# -*- coding: utf-8 -*-
import xlrd
from Public.log import LOG, logger
import config.config as cf
""" 从Excel文件读取测试用例 """


@logger('解析测试用例文件')
def datacel(filrpath):
    try:
        workbook = xlrd.open_workbook(filrpath)
        sheet = workbook.sheets()[0]
        nrows = sheet.nrows
        list_id = []
        list_is_header = []
        list_header = []
        list_url = []
        list_fangshi = []
        list_qiwang = []
        # listrelut = []
        list_name = []
        list_data = []
        for i in range(1, nrows):
            list_id.append(int(sheet.cell(i, cf.CASE_ID-1).value))
            list_name.append(sheet.cell(i, cf.CASE_NAME-1).value)
            list_is_header.append(sheet.cell(i, cf.CASE_IS_HEADER-1).value)
            list_header.append(sheet.cell(i, cf.CASE_HEADER-1).value)
            list_url.append(sheet.cell(i, cf.CASE_URL-1).value)
            list_data.append(sheet.cell(i, cf.CASE_DATA-1).value)
            list_fangshi.append(sheet.cell(i, cf.CASE_METHOD-1).value)
            list_qiwang.append(sheet.cell(i, cf.CASE_EXPECT-1).value)
            # list_qiwang.append((sheet.cell(i, cf.CASE_EXPECT-1).value))
        return list_id, list_name, list_is_header, list_header, list_data, list_url, list_fangshi, list_qiwang
    except Exception as e:
        LOG.info('打开测试用例失败，原因是:%s' % e)
        return


if __name__ == '__main__':
    result = datacel(cf.CASE_PATH)
    LOG.info(result)
