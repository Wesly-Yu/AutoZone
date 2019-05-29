# AutoZone
## web，APP ，接口 UI自动化一体测试平台<br>
与其他测试平台相比有什么优点：<br>
    1.测试平台解决了web，app部分元素无法定位的痛点，只需要对无法定位的点进行截图，然后上传到工程目录下后，在自动化用例里面输入图片的名称与格式就会进行图像的匹配识别，识别到后会完成点击与判断页面是否存在等操作<br>
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
首先安装python3.6版本或者3.7版本（有以前的安装库的尽量卸载，避免安装包版本的冲突，如果冲突了卸载了再安装很费时间，亲测这些坑），<br>然后找到目录下的requirements.txt文件，按住shift +右键点击在此处打开Power shell窗口<br>, 然后输入pip install -r requirement.txt,等待安装完毕，
安装mysql数据库（我的版本为5.7），<br>
导入关键字说明文件autotest.sql，在数据中新建一个连接，
新建的连接名称与账户密码都应该与Django settings文件中的此处一样：![image](https://github.com/Wesly-Yu/AutoZone/blob/master/images/20190526221134.png)<br>
你需要设置你的各种参数，不一定要与我的一样！！！，我是通过navicat连接，你也可以选择别的工具<br>
新建数据库命名为autotest,然后导入目录下的autotest.sql这个文件，navicat导入数据库文件，不会的同学请百度<br>
至此环境配置已经完成。
### 如何运行
下载完整的工程文件后，pycharm中打开
运行(也可以用pycharm的快捷键ctrl+alt +R)<br>
python manage.py runserver 指定希望运行的端口,也可以在在pycharm中设定端口号(8080有时候会被占用)![image](https://github.com/Wesly-Yu/AutoZone/blob/master/images/20190526222403.png)<br>
在下方的命令行中输入createsuperuser,下方自带提示功能的![image](https://github.com/Wesly-Yu/AutoZone/blob/master/images/2.png)<br>
创建后才能登陆，使用功能，否则会报错！<br>
然后在网页上输入网址比如127.0.0.1:9000/admin/,然后输入你 createsuperuser中设置的账户和密码,如果忘记了再次设置新的即可<br>
登陆Django自带的admin页面后显示如下:![image](https://github.com/Wesly-Yu/AutoZone/blob/master/images/3.png),在箭头所指示的地方添加平台的使用用户<br>
在页面中输入http://127.0.0.1:8000/login/ 后登陆页面如下![image](https://github.com/Wesly-Yu/AutoZone/blob/master/images/login.png)
ps:背景刚开始看还可以，后面越看越丑，有推荐的嘛？
创建登录的账号和密码：
###### 登陆后页面展示如下一些功能:
![image](https://github.com/Wesly-Yu/AutoZone/blob/master/images/tools.png)
![image](https://github.com/Wesly-Yu/AutoZone/blob/master/images/shouye.png)<br>
###### 可以根据不同的项目新建用例作为关联管理：<br>
![image](https://github.com/Wesly-Yu/AutoZone/blob/master/images/xiangmu.png)
###### 不同的项目添加不同的测试进度，进行展示:<br>
![image](https://github.com/Wesly-Yu/AutoZone/blob/master/images/jindu.png)
###### 接口参数添加页面如下:
![image](https://github.com/Wesly-Yu/AutoZone/blob/master/images/jiekou.png)
也可以在Assert 中可以对多个参数做判断（后续将增加对返回值参数是否存在与数据库中的断言）
###### 测试报告如下
![image](https://github.com/Wesly-Yu/AutoZone/blob/master/images/report.png)
###### Web自动化
web自动化步骤的添加和robotframework的一样，区别是增加了填写的参数位置固定了。步骤添加页面设计来源于Django 自带的admin模板 +suit这个美化过<br>
![image](https://github.com/Wesly-Yu/AutoZone/blob/master/images/web-ui.png)
###### 支持关键字蓝色高亮显示
只需将需要点击的图标截图名称填写进步骤里面(支持定位输入框,页面按键，链接等)
![image](https://github.com/Wesly-Yu/AutoZone/blob/master/images/picture.png)
###### 图片上传的路径平台已做设定，选择上传就可以了。注：图片识别并点击截图，需要如下的截图才能识别:<br>
如百度的查询按键：![image](https://github.com/Wesly-Yu/AutoZone/blob/master/images/baidu.png)<br>
如Testerhome的登陆按键![image](https://github.com/Wesly-Yu/AutoZone/blob/master/images/denglu.png)<br>
这是页面的上传功能按键：![image](https://github.com/Wesly-Yu/AutoZone/blob/master/images/update.png)<br>
等，图片背景变换会导致识别不到对应的截图，所以要保持点击的图标背景与截图的一致
所有测试用例支持运行所选部分和全部，支持定时任务的执行（与jenkins定时执行构建任务一样）接口与UI自动化可以一起执行，接口和UI需要分别设置<br>
![image](https://github.com/Wesly-Yu/AutoZone/blob/master/images/time.png)
###### 测试报告暂时用的robotframework的，UI的报告生成在指定的位置可以在页面中点开查看，接口的结果是通多读取数据库的参数展示的，后续将测试报告改的和web的测试报告一致。
![image](https://github.com/Wesly-Yu/AutoZone/blob/master/images/report.png)
###### 支持向添加到数据库的邮箱发送测试报告
![image](https://github.com/Wesly-Yu/AutoZone/blob/master/images/email.png)
###### web功能下可查看所有的对应的关键字查询与说明
![image](https://github.com/Wesly-Yu/AutoZone/blob/master/images/keywords.png)
测试平台的基本情况 已经讲解完成，后续将讲解相应部分的代码
我的QQ:1633235633@qq.com，有问题可以联系。后续开发完后将公布github地址，进行开源以便发现更多的问题

