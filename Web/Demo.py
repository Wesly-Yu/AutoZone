#coding:utf-8
import os
import  wx.html2

#
# path = os.path.abspath(os.path.dirname(__file__))  # 获取当前工程目录
# report_path = path + "\\report.html"
# browser = wx.html2.WebView.New(style=0,size=(-1,-1))
# browser.LoadURl


path = os.path.abspath(os.path.dirname(__file__))  # 获取当前工程目录
report_path = path + "\\report.html"
class Brower(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, "BROWER", size=(-1, -1))
        self.browser = wx.html2.WebView.New(self, style=0, size=(-1, -1))
        self.html_file = "test.html"
        self.browser.LoadURL(os.path.realpath(report_path))

if __name__ == '__main_':
    Brower()