# AutoZone
## web，APP ，接口 UI自动化一体测试平台<br>
与其他测试平台相比有什么优点：<br>
    1.测试平台解决了web，app,H5页面部分元素无法定位的痛点，只需要对无法定位的点进行截图，然后上传到工程目录下后，在自动化用例里面输入图片的名称与格式就会进行图像的匹配识别，识别到后会完成点击与判断页面是否存在等操作<br>
    2.采用Robotframework 的关键字系统，只需要输入关键字 加上元素的定位等方式，减少代码量的编写<br>
    3.可以自己编写第三库进行导入，扩展性极强<br>
    4.接口测试与UI测试可以同时进行，采用了python的多进程与协程操作，减少自动化用例的运行时间
      开发测试平台的初衷：希望web,app的UI自动化和接口的自动化能够一起执行，去掉jenkins构建，代码重构，繁多等问题。
      本平台是1.0版本，后续还将完善更多的功能（考虑是作成一个测试的客户端还是网页）<br>

### 什么是AutoZone测试平台
### AutoZone开源平台是一个开源自动化测试解决方案，基于RobotFramework进行二次开发，支持RobotFramework几乎所有的库。并能够实现图像识别查找GUI等功能。
采用了哪些开源技术/框架
* python3<br>
* Django<br>
* Bootstrap3<br>
* requests<br>
* pymysql<br>
* pyautoGUI<br>
* Pyhook<br>
* robotframework<br>
* Selenium2library<br>
* SikuliLIbrary<br>
* APSscheduler<br>
* openCV<br>
等库与插件<br>
### 配置运行的环境
首先
