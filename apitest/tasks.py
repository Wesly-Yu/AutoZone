# coding:utf-8
import requests, time, sys, re
import urllib,zlib
import pymysql
import requests
import unittest
from trace import CoverageResults
import json
from idlelib.rpc import response_queue
from  time import sleep
import os
import requests



PATH = lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__),p))

global driver
def singel_api_interfaceTest(case_list):
    result_flage = []
    responses = []
    # global expectresult
    for case  in case_list:
        try:
            case_id = case[0]
            modelname = case[1]
            case_name= case[2]
            url =case[3]
            header = eval(case[4])
            formdata =json.dumps(eval(case[5]))
            method = case[6]
            expectresult = eval(case[7])
            assert_keys = list(expectresult.keys())
            assert_values = list(expectresult.values())
        except Exception as  e :
            return '测试用例格式不正确！！%s'%e
        if method.upper() == 'GET':
            if len(formdata) == 0:
                formdata = None
                results = requests.get(url=url, headers=header)
                res = assert_result(results, assert_keys, assert_values, default=None)
                responses.append(res)
                if res == len(assert_keys):
                    result_flage.append('pass')
                    caseWriteResult(case_id, modelname, case_name, results, 'Pass')
                else:
                    result_flage.append('fail')
                    caseWriteResult(case_id, modelname, case_name, results, 'Fail')
            else:
                results = requests.get(url=url, headers=header,formdata=formdata)
                res = assert_result(results, assert_keys, assert_values, default=None)
                responses.append(res)
                if res == len(assert_keys):
                    result_flage.append('pass')
                    caseWriteResult(case_id, modelname, case_name, results, 'Pass')
                else:
                    result_flage.append('fail')
                    caseWriteResult(case_id, modelname, case_name, results, 'Fail')

        if method == "Post":
            if len(formdata) == 0:
                formdata = None
                results = requests.post(url=url, headers=header)
                res = assert_result(results, assert_keys, assert_values, default=None)
                responses.append(res)
                if res == len(assert_keys):
                    result_flage.append('pass')
                    caseWriteResult(case_id, modelname, case_name, results, 'Pass')
                else:
                    result_flage.append('fail')
                    caseWriteResult(case_id, modelname, case_name, results, 'Fail')
            else:
                results = requests.post(url=url, headers=header, data=formdata)
                print(results.json())
                res = assert_result(results, assert_keys, assert_values, default=None)
                responses.append(res)
                if res == len(assert_keys):
                    result_flage.append('pass')
                    caseWriteResult(case_id, modelname, case_name, results, 'Pass')
                else:
                    result_flage.append('fail')
                    caseWriteResult(case_id, modelname, case_name, results, 'Fail')
        if method.upper() == 'PUT':
            if len(formdata) == 0:
                formdatas = None
                results = requests.put(url=url, headers=header,data=formdatas)
                res = assert_result(results, assert_keys, assert_values, default=None)
                responses.append(res)
                if res == len(assert_keys):
                    result_flage.append('pass')
                    caseWriteResult(case_id, modelname, case_name, results, 'Pass')
                else:
                    result_flage.append('fail')
                    caseWriteResult(case_id, modelname, case_name, results, 'Fail')
            else:
                formdatas = formdata
                results = requests.put(url=url, headers=header,data=formdatas)
                res = assert_result(results, assert_keys, assert_values, default=None)
                responses.append(res)
                if res == len(assert_keys):
                    caseWriteResult(case_id, modelname, case_name, results, 'Pass')
                else:
                    result_flage.append('fail')
                    caseWriteResult(case_id, modelname, case_name, results, 'Fail')
        if method.upper() == 'PATCH':
            if len(header) == 0:
                header = None
                results = requests.put(url=url, header=header,data=formdata)
                res = assert_result(results, assert_keys, assert_values, default=None)
                responses.append(res)
                if res == len(assert_keys):
                    result_flage.append('pass')
                    caseWriteResult(case_id, modelname, case_name, results, 'Pass')
                else:
                    result_flage.append('fail')
                    caseWriteResult(case_id, modelname, case_name, results, 'Fail')
            else:
                results = requests.put(url=url, headers=header, data=formdata)
                res = assert_result(results, assert_keys, assert_values, default=None)
                responses.append(res)
                if res == len(assert_keys):
                    result_flage.append('pass')
                    caseWriteResult(case_id, modelname, case_name, results, 'Pass')
                else:
                    result_flage.append('fail')
                    caseWriteResult(case_id, modelname, case_name, results, 'Fail')






#断言和世界返回值比较的方法:
def assert_result(results,assert_keys,assert_values,default=None):
    responseJson = eval(results.text)
    j = 0
    for i in range(0, len(assert_keys)):
        for key, value in responseJson.items():         #遍历key值
            if key == assert_keys[i]:
                if str(value) == assert_values[i]:              #判断返回值中key的value和断言的value是否一致
                    print("PASS")
                    j+=1
                else:
                    print("断言参数不在返回值中")
            else:
                if type(value) is dict:
                    re = assert_result(value,assert_keys)
                    if re is not default:
                        print(re)
    return j


# #将期望结果和断言取出
# def readRes(results,expectresult):
#            #文本转换成json字符串
#     assert_result(results, assert_keys, assert_values, default=None)
#     return assert_keys, assert_values, responseJson


#读写测试结果到数据库
def caseWriteResult(case_id, modelname, case_name, results, result_number):
    results = str(results.json())
    now = time.strftime("%Y-%m-%d %H:%M:%S")
    sql = "UPDATE  apitest_singel_apis_task set apitest_singel_apis_task.task_modelname=%s, apitest_singel_apis_task.task_casename=%s,apitest_singel_apis_task.task_response=%s,apitest_singel_apis_task.task_result=%s,apitest_singel_apis_task.create_time=%s where apitest_singel_apis_task.task_id=%s;"
    param = (modelname, case_name, results, result_number, now, case_id)
    coon = pymysql.connect(user='root', password='test123456', db='autotest', port=3306, host='127.0.0.1',
                           charset='utf8')
    cursor = coon.cursor()
    print(result_number)
    coon.ping(reconnect=True)
    cursor.execute(sql, param)
    coon.commit()
    cursor.close()
    coon.close()

#提交测试bug到页面报告
# def writeBug(bug_id,model_name,case_name,request,response,expectresult):
# current_path = os.getcwd()
# report_path = os.path.join(current_path, "Report")
# now = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
#
# # 报告地址&名称
# report_title = 'Example报告' + now + ".html"     # 如果不能打开这个文件，可能是now的格式，不支持：和空格
#
# # 报告描述
# desc = '用于展示修改样式后的HTMLTestRunner'

# if __name__ == '__main__':








