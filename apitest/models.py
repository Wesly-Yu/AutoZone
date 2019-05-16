#coding;utf-8
from django.db import models

#数据库表

class Create_product(models.Model):
    productid = models.AutoField(primary_key=True, max_length=200, unique=True)
    modelname = models.CharField('模块名', default="", max_length=10)  #模块名称
    productname = models.CharField('项目名', max_length=200,)  #产品名
    tester = models.CharField('测试人员', max_length=200)  #测试人
    developer = models.CharField('开发人员', max_length=200)
    productdesc = models.CharField('模块描述', max_length=200)
    status = models.CharField('是否通过',max_length=20)
    create_time = models.DateTimeField('创建时间', auto_now=True)   #创建时间，自动获取当前时间
    def __str__(self):
        return self.productname


#带有数据依赖的接口，流程接口
class need_data_Apis(models.Model):
    process_name = models.CharField('流程名称', max_length=100)
    productid = models.AutoField(primary_key=True, max_length=200, unique=True)
    modelname = models.CharField('模块名称', max_length=100)
    depend_Apiname = models.CharField('用例名称', max_length=100)
    Apiurl_data = models.CharField('接口地址', max_length=200)
    Apimethod = models.CharField('请求方式', max_length=20, default='GET')
    Apiheader = models.CharField('请求头参数', max_length=800)
    Apiformdata = models.CharField('表单参数', max_length=800)
    Apidependdata = models.CharField('依赖的数据',max_length=100) #依赖数据
    Apiexpectresult = models.CharField('预期结果', max_length=200)  #预期结果
    Apischarger = models.CharField('负责人', max_length=50)
    create_time = models.DateTimeField('创建时间', auto_now=True)
    def __str__(self):
            return self.depend_Apiname

#单一API接口
class singel_Apis(models.Model):
    productid = models.AutoField(primary_key=True, max_length=200, unique=True)
    Product = models.CharField('产品名称', max_length=100)
    Apiname = models.CharField('接口名称', max_length=100)
    Apiurl = models.CharField('Url地址', max_length=200,null=True)
    Apiheader = models.CharField('请求头参数', max_length=800,null=True)
    Apiformdata = models.CharField('表单参数', max_length=800)
    Apimethod = models.CharField('请求方式', max_length=20, default='GET')
    Apiexpectresult = models.CharField('预期结果', max_length=200)
    Apischarger = models.CharField('负责人', max_length=50)
    create_time = models.DateTimeField('创建时间', auto_now=True,null=True)
    def __str__(self):
        return self.Apiname



#邮件配置表
class Email(models.Model):
    sender=models.CharField(max_length=20)
    receivers = models.CharField(max_length=100)
    host_dir = models.CharField(max_length=20)
    email_port=models.CharField(max_length=20, default="")
    username = models.CharField(max_length=20)
    passwd = models.CharField(max_length=20)
    Headerfrom = models.CharField(max_length=20)
    Headerto = models.CharField(max_length=100)
    subject = models.CharField(max_length=100,default="")
    def __str__(self):
        return self.username

#单一接口定时任务配置表
class singel_apis_task(models.Model):
    task_id = models.AutoField(primary_key=True, max_length=200, unique=True)
    task_modelname = models.CharField('任务模块', max_length=200)
    task_casename = models.CharField('任务用例名称', max_length=200)
    task_Apiurl = models.CharField('Url地址', max_length=200,null=True)
    task_Apiheader = models.CharField('请求头参数', max_length=800,null=True)
    task_Apiformdata = models.CharField('表单参数', max_length=800)
    task_Apimethod = models.CharField('请求方式', max_length=20, default='GET')
    task_Apiexpectresult = models.CharField('预期结果', max_length=200)
    task_status = models.CharField('状态', max_length=200, default=True)
    task_response = models.CharField('返回结果', max_length=500)
    task_retry = models.CharField('失败重跑次数', max_length=10)
    task_result = models.CharField('测试结果', max_length=20)
    update_time = models.DateTimeField(auto_now=True)
    create_time = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.task_modelname

#流程接口定时任务配置表
class process_apis_task(models.Model):
    task_id = models.AutoField(primary_key=True, max_length=200, unique=True)
    task_process_name = models.CharField('流程名称', max_length=100)
    task_modelname = models.CharField('模块名称', max_length=100)
    task_depend_Apiname = models.CharField('用例名称', max_length=100)
    task_Apiurl_data = models.CharField('接口地址', max_length=1024)
    task_Apimethod = models.CharField('请求方式', max_length=20, default='GET')
    task_Apiheader = models.CharField('请求头参数', max_length=800)
    task_Apiformdata = models.CharField('表单参数', max_length=800)
    task_Apidependdata = models.CharField('依赖的数据', max_length=100)  # 依赖数据
    task_Apiexpectresult = models.CharField('预期结果', max_length=200)  # 预期结果
    task_status = models.CharField('状态', max_length=200, default=True)
    task_response = models.CharField('返回结果', max_length=500)
    task_retry = models.CharField('失败重跑次数', max_length=10)
    task_result = models.CharField('测试结果', max_length=20)
    update_time = models.DateTimeField(auto_now=True)
    create_time = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.task_process_name



