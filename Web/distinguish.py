#coding:utf-8
from  selenium import  webdriver
from  PIL import Image
from time import  sleep
import pytesseract
import time
import sys
import re
import json
import urllib,base64
from urllib import request
from  urllib import parse
import ssl
from urllib.request import urlopen
from Web.ShowapiRequest import ShowapiRequest

import pytesseract
from PIL import Image

# im = Image.open('E:\code2.png')
#
# # 转化为灰度图像
# im = im.convert('L')  # 转化为灰度图像
# threshold = 127
# table = []
# for i in range(256):
#     if i < threshold:
#         table.append(0)
#     else:
#         table.append(1)
#
# ime = im.point(table, '1')
# print(pytesseract.image_to_string(ime))

# def main():
#     im = Image.open('E:\code2.png')
#     im = im.convert('L')  #转换为灰度图像
#     threshold = 127
#     table = []
#     for i in range(256):
#         if i < threshold:
#             table.append(0)
#         else:
#             table.append(1)
#     im = im.point(table,'1')
#     tessdata_dir_config = '--tessdata-dir "E://Program Files (x86)//Tesseract-OCR//tessdata"'
#     code = pytesseract.image_to_string(im,config=tessdata_dir_config)
#     print(code)
# if __name__ == '__main__':
#     main()


# driver = webdriver.Chrome()
# driver.get("http://117.174.109.10:16002/index")
# driver.maximize_window()
# time.sleep(4)
# driver.save_screenshot("E:/che.png")
# code_element = driver.find_element_by_id("imgObj")
# sleep(2)
# left = code_element.location['x']
# top = code_element.location['y']
# right = code_element.size['width']+left
# height = code_element.size['height']+top
# imge = Image.open("E:/che.png")
# pic = imge.crop((left,top,right,height))
# pic.save("E:/che2.png")
# driver.close()


# def get_token():
#     url = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=SXr0ie9NCZQZXIFmBhGlH97o&client_secret=bDnuxvENGeRTHDPrcDVsu8hIVvcuZtqP'
#     response = request.urlopen(url)
#     page = response.read().decode('utf-8')
#     page = json.loads(page)
#     access_token = page['access_token']
#     recognition_word_high(access_token)
#     return access_token
# def recognition_word_high(access_token):
#     request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic"
#     f = open("E:/code3.png",'rb')
#     img = base64.b64encode(f.read())
#     params = {"image":img}
#     access_token = access_token
#     headers = {"Content-Type": "application/x-www-form-urlencoded"}
#     params = parse.urlencode(params).encode('UTF-8')
#     request_url = request_url + "?access_token=" + access_token
#     request = urllib.request.Request(url=request_url,data=params,headers=headers)
#     response = urllib.request.urlopen(request)
#     print(response.read())
#
# if __name__ == '__main__':
#     get_token()

def get_code():
    image = open("E:/code3.png", 'rb')
    img = base64.b64encode(image.read())
    r = ShowapiRequest("http://route.showapi.com/184-4", "85060", "624075410c1f4901b124f1110b93b90e")
    r.addBodyPara("img_base64","")
    r.addBodyPara("typeId", "34")
    r.addBodyPara("convert_to_jpg", "0")
    r.addBodyPara("enctype", "application/x-www-form-urlencoded")
    r.addBodyPara("needMorePrecise", "1")
    r.addFilePara("image", r"E:\che3.png") #文件上传时设置
    res = r.post()
    print(res.text)  # 返回信息
if __name__ == '__main__':
    get_code()

