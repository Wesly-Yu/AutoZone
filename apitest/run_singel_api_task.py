#coding:utf-8
from tkinter import COMMAND
import unittest
from apitest.tasks import singel_api_interfaceTest
import pymysql

def readSQL():
    sql ="SELECT task_id,task_modelname,task_casename,task_Apiurl,task_Apiheader,task_Apiformdata,task_Apimethod,task_Apiexpectresult,task_result from apitest_singel_apis_task"
    coon = pymysql.connect(user='root',password='test123456',db='autotest', port=3306, host='127.0.0.1',charset='utf8')
    cursor = coon.cursor()
    singel_api_task = cursor.execute(sql)
    singel_api_task_result = cursor.fetchmany(singel_api_task)
    for one_result in singel_api_task_result:
        case_list = []
        case_list.append(one_result)
        singel_api_interfaceTest(case_list)
        coon.ping(reconnect=True)
        coon.commit()
        cursor.close()
        coon.close()
# def ping(self, reconnect=True):
#     """Check if the server is alive"""
#     if self._sock is None:
#         if reconnect:
#             self.connect()
#             reconnect = False
#         else:
#             raise pymysql.err.Error("Already closed")
#     try:
#         self._execute_command(COMMAND.COM_PING, "")
#         return self._read_ok_packet()
#     except Exception:
#         if reconnect:
#             self.connect()
#             return self.ping(False)
#         else:
#             raise
# def reConnect(self):
#     try:
#         self.connection.ping()
#     except:
#         self.connection()

def read_Results():
    db = pymysql.connect(user='root',password='test123456',db='autotest', port=3306, host='127.0.0.1',charset='utf8')
    cursor = db.cursor()
    sql1 = "SELECT count(task_id) FROM apitest_singel_apis_task WHERE apitest_singel_apis_task.task_result='Pass'"
    passresult = cursor.execute(sql1)
    pass_count = [row[0] for row in cursor.fetchmany(passresult)][0]
    sql2 = "SELECT count(task_id) FROM apitest_singel_apis_task WHERE apitest_singel_apis_task.task_result='Fail'"
    failresult = cursor.execute(sql2)
    fail_count = [row[0] for row in cursor.fetchmany(failresult)][0]
    db.close()
    return pass_count, fail_count





#
# if __name__ == '__main__':
#     readSQL()
#     read_Results()
