#coding:utf-8
from win32con import WM_INPUTLANGCHANGEREQUEST
import win32gui
import win32api




# 语言代码
# https://msdn.microsoft.com/en-us/library/cc233982.aspx

def switch_langrage():
    LID = {0x0804: "Chinese (Simplified) (People's Republic of China)",
           0x0409: 'English (United States)'}

    # 获取前景窗口句柄
    hwnd = win32gui.GetForegroundWindow()

    # 获取前景窗口标题
    title = win32gui.GetWindowText(hwnd)
    print('当前窗口：' + title)

    # 获取键盘布局列表
    im_list = win32api.GetKeyboardLayoutList()
    im_list = list(map(hex, im_list))
    print(im_list)

    # 设置键盘布局为英文
    result = win32api.SendMessage(
        hwnd,
        WM_INPUTLANGCHANGEREQUEST,
        0,
        0x0409)
    if result == 0:
        print('设置英文键盘成功！')

