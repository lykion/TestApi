# -*- coding: utf-8 -*-
""" 读取Excel """
import xlrd
import config.config as cf


def datacel(filrpath):
    all_case = []
    workbook = xlrd.open_workbook(filrpath)
    sheet = workbook.sheets()[0]
    nrows = sheet.nrows
    for i in range(1, nrows):
        all_case.append({"id": int(sheet.cell(i, cf.CASE_ID-1).value),
                         'name': sheet.cell(i, cf.CASE_NAME-1).value,
                         'is_header': sheet.cell(i, cf.CASE_IS_HEADER-1).value,
                         'header': sheet.cell(i, cf.CASE_HEADER-1).value,
                         'data': sheet.cell(i, cf.CASE_DATA-1).value,
                         'url': sheet.cell(i, cf.CASE_URL-1).value,
                         'fangshi': sheet.cell(i, cf.CASE_METHOD-1).value,
                         'assert': int(sheet.cell(i, cf.CASE_EXPECT-1).value)})
    return all_case


if __name__ == '__main__':
    all = datacel(cf.CASE_PATH)
    print(all)
