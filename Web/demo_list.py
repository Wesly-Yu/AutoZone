# -*- coding: utf-8 -*-
import os
import re


def a():
    taskcasesuit = "test.txt"
    path = os.path.abspath(os.path.dirname(__file__))  # 获取当前工程目录
    project_path = os.path.join(path, taskcasesuit)  # 加入完整的目录和文件名称
    regx = "login"
    with open(project_path,'r+') as txtfile:
        p = re.compile(regx)
        lines = txtfile.readlines()[1:]
        lineb = [line for line in lines if p.search(line) is None]
        txtfile.truncate(0)
        txtfile.writelines(lineb)
# taskcasesuit = "test.txt"
# path = os.path.abspath(os.path.dirname(__file__))  # 获取当前工程目录
# project_path = os.path.join(path, taskcasesuit)  # 加入完整的目录和文件名称
# regx = "登录testhome"
# with open(project_path,'r+') as txtfile:
#     for line in txtfile.readlines():
#         data = re.match(r'.*?登录testhome',txtfile.readlines()).group(0)
#         info = s[len(data):]
#         data1 = re.sub(r'登录testhome','',info)
#         data = data + data1
#         print(data)


if __name__ == '__main__':
    a()

