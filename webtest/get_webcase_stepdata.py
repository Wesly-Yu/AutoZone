#coding:utf-8
import time
import os
import re
import sys
import pymysql
from pykeyboard import PyKeyboard
import pyautogui
PATH = lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__),p))
path = os.path.abspath(os.path.dirname(__file__))  # 获取当前工程目录
from webtest.set_langurage import switch_langrage



def readwebcaseSQL(upperlevel_id):
    sql = "SELECT webtestlocation,webfindmethod,webkwargesone,webkwargestwo,webkwargesthree,webkwargesfour,webassertdata from webtest_webcasestep where Webcase_id="+upperlevel_id
    coon = pymysql.connect(user='root', password='test123456', db='autotest', port=3306, host='127.0.0.1',
                           charset='utf8')
    cursor = coon.cursor()
    webcasestepcheck = cursor.execute(sql)  #读取页面上的执行步骤
    get_selectresult = cursor.fetchmany(webcasestepcheck)  #获取所有的查询结果
    case_count = 0
    for one_result in get_selectresult:
        case_list = []
        case_list.append(one_result)
        case_count+=1
        test_webcase_step(upperlevel_id,case_list,case_count)
        readSQLCounts(upperlevel_id)
        coon.ping(reconnect=True)
        print(case_count)
    coon.commit()
    cursor.close()
    coon.close()


def readSQLCounts(upperlevel_id):
    sql2 = "SELECT count(*)from webtest_webcasestep where Webcase_id=" + upperlevel_id
    coon = pymysql.connect(user='root', password='test123456', db='autotest', port=3306, host='127.0.0.1',
                           charset='utf8')
    cursor = coon.cursor()
    get_counts = cursor.execute(sql2)  # 读取页面上的执行步骤数量
    get_countsnumber = cursor.fetchmany(get_counts)  # 获取所有的查询结果数量
    coon.ping(reconnect=True)
    coon.commit()
    cursor.close()
    coon.close()
    return get_countsnumber


#将数据库中的数据取出并写入到txt中
def test_webcase_step(upperlevel_id,case_list,case_count):
    case_count = case_count                     #获取从数据库中读取了多少次，即获得了需要执行的用例行数！！
    number = str(upperlevel_id)
    counts = readSQLCounts(upperlevel_id)
    new_count = list(counts)
    step_counts = new_count[0][0]
    robotcasename = "test00" + number + ".txt"
    for case in case_list:
        try:
            webtestlocation = case[0]
            webfindmethod = case[1]
            webkwargesone = case[2]
            webkwargestwo = case[3]
            webkwargesthree = case[4]
            webkwargesfour = case[6]
            # webassertdata = case[7]
            time.sleep(1)
            path = os.path.abspath(os.path.dirname(__file__))  # 获取当前工程目录
            project_path = os.path.join(path, robotcasename)  # 加入完整的目录和文件名称
            txtfile = open(project_path, "a")
            try:
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
            if case_count == step_counts:
                print(case_count)
                time.sleep(2)
                run_in_terminal(upperlevel_id)
                print("正在运行脚本")
            else:
                print("数据正在写入中")
        except  Exception as e:
            print("出错了")



#写入用例的名称和变量、调用的第三方库
def write_to_txt(upperlevel_id):
    number = str(upperlevel_id)
    robotcasename = "test00"+number+".txt"
    path = os.path.abspath(os.path.dirname(__file__))  # 获取当前工程目录
    project_path = os.path.join(path, robotcasename)  # 加入完整的目录和文件名称
    mediapath = path + "\\" + "media"
    content1 = "*** Settings ***\n"
    content7 = "Library           Selenium2Library\n"
    content5 = "Library           SikuliLibrary\n"
    content8 = "Test Teardown       Close Browser\n"
    content3 = "*** Variables ***\n"
    content6 = "${picture_path}"+"    "+mediapath+"\n"
    content4 = "*** Test Cases ***\n"
    txtfile = open(project_path, "a")
    txtfile.writelines([content1,"\r",content7,"\r",content5,"\r",content8,"\r",content3,"\r",content6,"\r", content4,"\r", "test00"+number, "\r"])
    time.sleep(3)
    txtfile.close()
    print("主体写入完成")

# 移除指定路径下的txt文件
def remove_webtest_txt(txtname):
    number = str(txtname)
    robotcasename = "test00" + number + ".txt"
    path = os.path.abspath(os.path.dirname(__file__))  # 获取当前工程目录
    project_path = os.path.join(path, robotcasename)  # 加入完整的目录和文件名称
    try:
        if(os.path.exists(project_path)):
            os.remove(project_path)
            print("成功移除测试脚本")
        else:
            print("要删除的脚本文件不存在")
    except Exception as e:
        print("Failed,please retry.....")


#在Terminal中通过快捷键输入执行命令
def  run_in_terminal(upperlevel_id):
    robotcasename = "test00" + str(upperlevel_id) + ".txt"
    k = PyKeyboard()
    sub = os.popen("where python")
    pathone = sub.read()
    regx = re.split('python.exe',pathone)
    runpath = '"' + regx[0] + 'Scripts\pybot.bat' + '"' + ' -d results  '+ robotcasename
    pyautogui.keyDown('alt')
    pyautogui.press('f12')
    pyautogui.keyUp('alt')
    time.sleep(3)
    switch_langrage()
    k.type_string('cd webtest')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    k.type_string(runpath)
    time.sleep(1)
    pyautogui.press('enter')


