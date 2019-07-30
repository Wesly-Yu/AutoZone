#coding:utf-8
import time
import os
import re
import sys
import pymysql
from pykeyboard import PyKeyboard
import pyautogui
import json
from django.http import JsonResponse,HttpResponse
from time import sleep
from  apscheduler.schedulers.background import BackgroundScheduler

PATH = lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__),p))


#添加到定时任务列表
def add_to_periodic_task():
    write_name_txt()
    print("开始啦")
    time.sleep(2)
    get_task_stepdata()
    time.sleep(1)
    run_in_terminal()

def get_webtask_times(singel_task_date):
    if singel_task_date != '':
        timechuo = time.mktime(time.strptime(singel_task_date,'%Y-%m-%d %H:%M:%S'))
        localtime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(timechuo))
        scheduler = BackgroundScheduler()
        scheduler.add_job(add_to_periodic_task,'date',run_date=localtime)
        scheduler.start()
        print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))
        try:
            # This is here to simulate application activity (which keeps the main thread alive).
            while True:
                time.sleep(2)
        except (KeyboardInterrupt, SystemExit):
            # Not strictly necessary if daemonic mode is enabled but should be done if possible
            scheduler.shutdown()
    else:
        print("没有收到时间设置参数")







#将定时任务数据库中的数据与用例所在的表连接查询
def get_task_stepdata():
    sqlSentence = "SELECT webtestlocation,webfindmethod,webkwargesone,webkwargestwo,webkwargesthree,webkwargesfour,b.task_casename,b.case_id FROM webtest_webcasestep AS a LEFT JOIN webtest_webtest_task AS b ON a.Webcase_id=b.case_id;"
    coon = pymysql.connect(user='root', password='test123456', db='autotest', port=3306, host='127.0.0.1',
                           charset='utf8')
    cursor = coon.cursor()
    webcasestepcheck = cursor.execute(sqlSentence)  # 读取页面上的执行步骤
    get_selectresult = cursor.fetchmany(webcasestepcheck)  # 获取所有的查询结果
    case_count = 0
    for one_result in get_selectresult:
        case_list = []
        case_list.append(one_result)
        case_count += 1                                #查看读取用例了多少次，即一遍一遍的读取数据库中的步骤
        run_webcasestep_intask(case_list,case_count)
        # readSQLCounts()
    coon.ping(reconnect=True)
    coon.commit()
    cursor.close()
    coon.close()

#获取总共有多少条step:
def readSQLCounts():
    sql2 = "SELECT count(*) FROM webtest_webcasestep AS a LEFT JOIN webtest_webtest_task AS b ON a.Webcase_id=b.case_id;"
    coon = pymysql.connect(user='root', password='test123456', db='autotest', port=3306, host='127.0.0.1',
                           charset='utf8')
    cursor = coon.cursor()
    get_counts = cursor.execute(sql2)                                   # 读取页面上的执行步骤数量
    get_countsnumber = cursor.fetchmany(get_counts)                     # 获取所有的查询结果数量
    coon.ping(reconnect=True)
    coon.commit()
    cursor.close()
    coon.close()
    return get_countsnumber

#获取用例名称：
def getcasename_from_SQL():
    sql2 = "SELECT task_casename FROM  webtest_webtest_task;"
    coon = pymysql.connect(user='root', password='test123456', db='autotest', port=3306, host='127.0.0.1',
                           charset='utf8')
    cursor = coon.cursor()
    get_counts = cursor.execute(sql2)
    get_casename = cursor.fetchmany(get_counts)
    coon.ping(reconnect=True)
    coon.commit()
    cursor.close()
    coon.close()
    return get_casename



#将步骤中的参数读取出来
def run_webcasestep_intask(case_list,case_count):
    get_case_count = case_count
    counts = readSQLCounts()
    new_count = list(counts)  # 将元祖转换为列表
    step_counts = new_count[0][0]  # 将数据库查询到的步骤数量取出
    taskcasesuit = "test.txt"
    path = os.path.abspath(os.path.dirname(__file__))  # 获取当前工程目录
    project_path = os.path.join(path, taskcasesuit)  # 加入完整的目录和文件名称
    for case in case_list:
        try:
            webtestlocation = case[0]
            webfindmethod = case[1]
            webkwargesone = case[2]
            webkwargestwo = case[3]
            webkwargesthree = case[4]
            webkwargesfour = case[5]
            taskcasename = case[6]
            case_id = case[7]
        except Exception as e:
            return '测试用例格式不正确！！%s' % e
        with open(project_path, 'a+') as txtfile:
            txtfile.seek(0)
            r = txtfile.readlines()
            str1 = "Test0" + case_id + "\n"
            str2 = "\t" + "[Documentation]" + "\t" + "\t" + taskcasename + "\n"
            if str1 in r:
                print("已经写入了")
            else:
                txtfile.write("\r" + str1)
            if str2 in r:
                print("也已经写入了")
            else:
                txtfile.write(str2)
            try:  # 判断参数的长度 并分别写入
                if webkwargesone == "":
                    txtfile.write("\t" + webfindmethod + "\n")
                elif webkwargestwo == "":
                    txtfile.write("\t" + webfindmethod + "\t" + webkwargesone + "\n")
                elif webkwargesthree == "":
                    txtfile.write("\t" + webfindmethod + "\t" + webkwargesone + "\t" + webkwargestwo + "\n")
                elif webkwargesfour == "":
                    txtfile.write(
                        "\t" + webfindmethod + "\t" + webkwargesone + "\t" + webkwargestwo + "\t" + webkwargesthree + "\n")
                else:
                    txtfile.write(
                        "\t" + webfindmethod + "\t" + webkwargesone + "\t" + webkwargestwo + "\t" + webkwargesthree + "\t" + webkwargesfour + "\n")
            except Exception as e:
                print("Failed,please retry.....")
            txtfile.close()
            print("over")
            if get_case_count == step_counts:
                print(get_case_count)
                time.sleep(2)
                # run_in_terminal(taskcasename)
                print("正在运行脚本")
            else:
                print("数据正在写入中")




#写入用例的名称和变量、调用的第三方库
def write_name_txt():
    taskcasesuit = "test.txt"
    path = os.path.abspath(os.path.dirname(__file__))  # 获取当前工程目录
    project_path = os.path.join(path, taskcasesuit)  # 加入完整的目录和文件名称
    content1 = "*** Settings ***\n"
    content4 = "Library           Selenium2Library\n"
    content5 = "Library           SikuliLibrary\n"
    content2 = "Test Setup\tadd Needed Image Path\n"
    content3 = "Test Teardown\tClose Browser\n"
    content6 = "*** Variables ***\n"
    content7 = "${picture_path}    F:/AutoZone/robotframework/media\n"
    content8 = "*** Keywords ***\n"
    content9 = "Add Needed Image Path\n"
    content10 = "\tAdd Image Path    ${picture_path}\n"
    content11 = "*** Test Cases ***\n"
    txtfile = open(project_path, "a+")
    txtfile.writelines(
        [content1, "\r", content2, "\r", content3, "\r", content4, "\r", content5, "\r", content6, "\r", content7, "\r",
         content8, "\r", content9, "\r", content10, "\r", content11, "\r"])
    time.sleep(1)
    txtfile.close()
    print("主体写入完成")




#在Terminal中通过快捷键输入执行命令
def  run_in_terminal():
    k = PyKeyboard()
    sub = os.popen("where python")
    pathone = sub.read()
    regx = re.split('python.exe',pathone)
    runpath = '"' + regx[0] + 'Scripts\pybot.bat' + '"' + ' -d results  '+ "test.txt"
    pyautogui.keyDown('alt')
    pyautogui.press('f12')
    pyautogui.keyUp('alt')
    time.sleep(3)
    k.type_string('cd robotframework')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    k.type_string(runpath)
    time.sleep(1)
    pyautogui.press('enter')


