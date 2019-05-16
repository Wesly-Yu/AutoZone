from django.db import models
from  apitest.models import Create_product

#web自动化数据表
class Webcase(models.Model):
    webcase_models = models.CharField('所属模块', max_length=250)
    webcasename = models.CharField('测试用例名称', max_length=50)
    webcasedesc = models.CharField('步骤描述',max_length=50)
    webteststep = models.CharField('测试步骤',max_length=200)
    webcase_charger = models.CharField('负责人', max_length=200)
    creat_time = models.DateTimeField('创建时间', auto_now=True)
    class Meta:
        verbose_name ='web测试步骤'
        verbose_name_plural='web测试步骤'
    def __str__(self):
        return  self.webcasename


#步骤编辑
class Webcasestep(models.Model):
    Webcase = models.ForeignKey(Webcase,on_delete=models.CASCADE)                  #关联 add_web_name的id
    Locator = (('id', 'id'), ('xpath', 'xpath'), ('css', 'css'), ('图片', '图片'), ('name', 'name'), ('link', 'link'), ('classname', 'classname'),('tagname', 'tagname'))
    webtestlocation = models.CharField(verbose_name='定位方式',choices=Locator,default='0',max_length=200)
    webfindmethod = models.CharField('方法|操作', max_length=200,blank=True,null=True)
    webkwargesone = models.CharField('参数1', max_length=200,blank=True)
    webkwargestwo = models.CharField('参数2', max_length=200,blank=True)
    webkwargesthree = models.CharField('参数3', max_length=200,blank=True)
    webkwargesfour = models.CharField('参数4', max_length=200, blank=True)
    webassertdata = models.CharField('验证数据', max_length=200,blank=True)
    webtestresult = models.CharField('测试结果', max_length=50,blank=True)
    webcomments = models.CharField('备注', max_length=200,blank=True)
    def __str__(self):
        return  self.webfindmethod


#关键字
class Webcase_keywords(models.Model):
    keyword_id = models.AutoField(primary_key=True,unique=True,max_length=200)
    library = models.CharField('库名',max_length=50)
    keyword = models.CharField('关键字',max_length=200)
    parameter = models.CharField('参数',max_length=200)
    comment = models.CharField('参数2',max_length=200)

#web定时任务配置表
class webtest_task(models.Model):
    task_id = models.AutoField(primary_key=True, max_length=200, unique=True)
    task_modelname = models.CharField('模块名称', max_length=100)
    task_casename = models.CharField('任务用例名称', max_length=200)
    task_stepdesc = models.CharField('任务步骤描述',max_length=100,null=True)
    task_status = models.CharField('状态', max_length=200, default=True)
    task_retry = models.CharField('失败重跑次数', max_length=10)
    task_result = models.CharField('测试结果', max_length=20)
    update_time = models.DateTimeField(auto_now=True)
    create_time = models.DateTimeField(auto_now=True)
    case_id = models.CharField('测试用例名称的ID',max_length=200,null=True)

#邮件配置表
class Email(models.Model):
    email_id = models.AutoField(primary_key=True,max_length=200,unique=True)
    sender=models.CharField(max_length=20)                                          #发件人邮箱号
    receivers = models.CharField(max_length=100)                                    #收件人
    body = models.CharField(max_length=20)                                          #邮件主题内容
    email_port=models.CharField(max_length=20, default="")                          #邮件端口
    username = models.CharField(max_length=20)                                      #发件人邮箱账号
    passwd = models.CharField(max_length=20)                                        #发件人密码
    subject = models.CharField(max_length=100,default="")                           #主题名称
    email_server = models.CharField(max_length=20,default="")                       #发送邮箱服务器
    def __str__(self):
        return self.username