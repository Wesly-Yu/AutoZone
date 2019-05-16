import os
import time
def write_name_txt():
    taskcasesuit = "test.txt"
    path = os.path.abspath(os.path.dirname(__file__))  # 获取当前工程目录
    project_path = os.path.join(path, taskcasesuit)  # 加入完整的目录和文件名称
    content1 = "*** Settings ***\n"
    content4 = "Library           Selenium2Library\n"
    content5 = "Library           SikuliLibrary\n"
    content2 = "Test Setup\tdd Needed Image Path\n"
    content3 = "Test Teardown\tClose Browser\n"
    content6 = "*** Variables ***\n"
    content7 = "${picture_path}    F:/AutoZone/webtest/media\n"
    content8 = "*** Keywords ***\n"
    content9 = "Add Needed Image Path\n"
    content10 = "\tAdd Image Path    ${picture_path}\n"
    content11 = "*** Test Cases ***\n"
    txtfile = open(project_path, "a+")
    txtfile.writelines([content1,"\r",content2,"\r",content3,"\r",content4,"\r",content5,"\r",content6,"\r",content7,"\r", content8,"\r",content9,"\r",content10,"\r",content11,"\r"])
    time.sleep(1)
    txtfile.close()
    print("主体写入完成")

if __name__ == '__main__':
    write_name_txt()

