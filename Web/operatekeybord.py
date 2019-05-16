#coding=utf-8
import time
import win32api
import win32con
import pyautogui
import  sys
import os
import re
import pykeyboard,pymouse
from pymouse import *
from pykeyboard import PyKeyboard

m = PyMouse()
k = PyKeyboard()
sub = os.popen("where python")
pathone = sub.read()
regx = re.split('python.exe',pathone)
runpath ='"'+ regx[0] + 'Scripts\pybot.bat'+'"' +' -d results test006.txt'
print(runpath)
# k.press_key(k.alt_key)
# k.tab_key(k.function_keys[])
# k.release_key(k.alt_key)
# time.sleep(2)
pyautogui.keyDown('alt')
pyautogui.press('f12')
pyautogui.keyUp('alt')
time.sleep(1)
k.type_string('cd webtest')
time.sleep(1)
pyautogui.press('enter')
time.sleep(1)
k.type_string(runpath)
time.sleep(1)
pyautogui.press('enter')



