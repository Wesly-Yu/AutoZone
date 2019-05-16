# coding:utf-8
import re
import os
import random

cases = ['openbrowser','www.baidu.com','chrome']
a = str(random.random())
robotcasename = "test00"+ a +".txt"
print(robotcasename)
path = os.path.abspath(os.path.dirname(__file__))  # 获取当前工程目录
project_path = os.path.join(path, robotcasename)  # 加入完整的目录和文件名称
content1 = "*** Settings ***\n"
content2 = "Library           Selenium2Library\n"
content3 = "*** Variables ***\n"
content4 = "*** Test Cases ***\n"
txtfile = open(project_path, "a")
txtfile.writelines([content1, content2, "\r", content3, "\r", content4, "\r", "test00"+a, "\r", ])
txtfile.close()
for case in cases:
    try:
        txtfile = open(project_path, "a")
        txtfile.write("\t"+str(case[0]+"\t"+str(case[1])+"\t"+str(case[2])))
        txtfile.write("\r")
    except Exception as e:
        print("Failed")
        break
txtfile.close()
print("写入完成")
f1 = open(project_path).read()
f2 = f1.replace("\t","  ")
path = os.path.abspath(os.path.dirname(__file__))  # 获取当前工程目录
newpath = os.path.join(path, "testcase.txt")
f3 = open(newpath,"w")
f3.write(f2)
f3.close()



