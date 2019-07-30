#coding:utf-8
import requests, time, sys, re
import pymysql
import unittest
from trace import CoverageResults
import json
from idlelib.rpc import response_queue
import os
from  selenium import  webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
import time
from time import sleep





PATH = lambda p:os.path.abspath(os.path.join(os.path.dirname(__file__),p))


def test_webcase_step(case_list):
    for case in case_list:
        try:
            webtestlocation = case[0]
            print(webtestlocation)
            webfindmethod = case[1]
            print(webfindmethod)
            webkwargesone = case[2]
            print(webkwargesone)
            webkwargestwo = case[3]
            print(webkwargestwo)
            webkwargesthree = case[4]
            webassertdata = (case[5])
        except Exception as e:
            return '测试用例格式不正确！！%s'%e
        time.sleep(4)
        if webfindmethod =="sendkeys" and webtestlocation =="id":
            print(webkwargesone)






