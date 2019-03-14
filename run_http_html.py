# -*- coding: utf-8 -*-
import datetime
import os
import time
import config.config as cf
from Public.Express import send_demo
from Public.get_excel import datacel
from Public.py_Html import createHtml
from testCase.case import testinterface

'''执行测试的主要文件'''


def start_interface_html_http():
    starttime = datetime.datetime.now()
    day = time.strftime("%Y%m%d%H%M", time.localtime(time.time()))
    basdir = os.path.abspath(os.path.dirname(__file__))
    path = cf.CASE_PATH
    listid, listname, listisheader, listheader, listdata, listurl, listfangshi, listqiwang = datacel(path)
    listrelust, list_fail, list_pass, list_json, list_exption, list_weizhi = testinterface()
    filepath = os.path.join(basdir + '\\test_Report\\%s-result.html' % day)
    if os.path.exists(filepath) is False:
        os.system(r'touch %s' % filepath)
    endtime = datetime.datetime.now()
    createHtml(titles=u'http接口自动化测试报告', filepath=filepath, starttime=starttime, endtime=endtime, passge=list_pass,
               fail=list_fail, id=listid, name=listname, is_header=listisheader, header=listheader, url=listurl,
               meth=listfangshi, yuqi=listqiwang, json=list_json, relusts=listrelust, weizhi=list_weizhi,
               exceptions=list_exption)
    contec = u'http接口自动化测试完成，测试通过:%s,测试失败：%s，异常:%s,未知错误：%s,详情见：%s' % (
        list_pass, list_fail, list_exption, list_weizhi, filepath)
    send_demo(contec)


if __name__ == '__main__':
    start_interface_html_http()
