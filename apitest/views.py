#coding:utf-8
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib.auth.decorators import login_required
from django.contrib import auth
from django.contrib.auth import authenticate,login
from django.shortcuts import render
from apitest.models import need_data_Apis
from apitest.models import singel_Apis
from apitest.models import Create_product
from apitest.models import singel_apis_task
from  apitest.models import process_apis_task
from django.contrib import messages
import json
import os
import pymysql
from django.core.paginator import  Paginator, EmptyPage, PageNotAnInteger
from apitest.tasks import singel_api_interfaceTest
import time
from apitest.run_singel_api_task import readSQL ,read_Results
from  apscheduler.schedulers.background import BackgroundScheduler


def Login(request):
    if request.POST:
        username = password = ''
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username,password=password)  #认证给出的用户名和密码
        if user is not None and user.is_active:    #判断用户名和密码是否有效
            auth.login(request, user)
            request.session['user'] = username  #跨请求的保持user参数
            response = HttpResponseRedirect('/home/')
            return response
        else:
            messages.add_message(request, messages.WARNING, '账户或者密码错误，请检查')
            return render(request, 'login.html')

    return render(request, 'login.html')
def Home(request):
    return render(request, 'home.html')
def Logout(request):
    auth.logout(request)
    return render(request, 'login.html')
def welcome(request):
    return  render(request, 'welcome.html')



@login_required
def product_test_speed(request):
    return render(request, "product_test_speed.html")
def left(request):
    return render(request, "left.html")

@login_required
def singel_api_test(request):
    username = request.session.get('user','')
    steps = singel_Apis.objects.get_queryset().order_by('productid')
    paginator = Paginator(steps, 12)  # 生成paginator对象,设置每页显示15条记录
    page = request.GET.get('page', 1)  # 获取当前页为第1页
    currentPage = int(page)  # 把当前页转换成整数
    try:
        steps = paginator.page(page)  # 获取当前页码数的记录列表
    except PageNotAnInteger:
        steps = paginator.page(1)  # 如果输入的页数不是整数则显示第1页内容
    except EmptyPage:
        steps = paginator.page(paginator.num_pages)  # 如果输入的的页数不在系统的页数中，则显示最后一页
    return render(request, "singel_api_test.html", {"user": username, "steps": steps})

#添加单一的接口
@login_required
def add_singel_api(request):
    username = request.session.get('user')
    steps = singel_Apis.objects.all()
    if request.method == "POST":
        newModelname_data = request.POST.get("modelname",)
        newCasename_data = request.POST.get("casename",)
        newUrl_data = request.POST.get("addURL",)
        newMethod_data = request.POST.get("Method",)
        newMergeheaders_data  = json.loads(request.POST.get("addmergeheaders",))
        newMergeform_data = json.loads(request.POST.get("addmergeformdatas",))
        newMergecheck_data = json.loads(request.POST.get("addmergecheckdatas",))
        newCharger_data = request.POST.get("charger",)
        singel_Apis.objects.create(Product=newModelname_data, Apiname=newCasename_data, Apiurl=newUrl_data, Apiheader=newMergeheaders_data, Apimethod=newMethod_data, Apiformdata=newMergeform_data, Apiexpectresult=newMergecheck_data, Apischarger=newCharger_data)
    return render(request, "singel_api_test.html", {"user": username, "steps": steps})

#删除单一接口
@login_required
def del_singel_api(request):
    username = request.session.get('user')
    steps = singel_Apis.objects.all()
    if request.is_ajax():
        id = request.POST.get('id')
        singel_Apis.objects.filter(productid=id).delete()
    return render(request, "singel_api_test.html", {"user": username, "steps": steps})

#修改单一的接口
@login_required
def change_singel_api(request):
    username = request.session.get('user')
    steps = singel_Apis.objects.all()
    if request.is_ajax():
        newccase_id = request.POST.get("id", )
        newModelname_data = request.POST.get("change_modelname",None)
        newCasename_data = request.POST.get("change_casename", None)
        newUrl_data = request.POST.get("change_URL", None)
        newMethod_data = request.POST.get("change_Method", None)
        newMergeheaders_data = json.loads(request.POST.get("change_mergeheaders",None))
        newMergeform_data = json.loads(request.POST.get("change_mergeformdatas", None))
        newMergecheck_data = json.loads(request.POST.get("change_mergecheckdatas", None))
        newCharger_data = request.POST.get("change_charger",None)
        singel_Apis.objects.filter(productid=newccase_id).update(Product=newModelname_data, Apiname=newCasename_data, Apiurl=newUrl_data,
                                   Apiheader=newMergeheaders_data, Apimethod=newMethod_data,
                                    Apiformdata=newMergeform_data,
                                Apiexpectresult=newMergecheck_data, Apischarger=newCharger_data)
    return render(request, "singel_api_test.html", {"user": username, "steps": steps})

@login_required
def create_product(request):
    username = request.session.get('user', '')
    # products = Create_product.objects.all()
    products = Create_product.objects.get_queryset().order_by('productid')
    paginator = Paginator(products, 12)  #生成paginator对象,设置每页显示12条记录
    page = request.GET.get('page',1) #获取当前页为第1页
    currentPage = int(page)   #把当前页转换成整数
    try:
        products = paginator.page(page) #获取当前页码数的记录列表
    except PageNotAnInteger:
        products = paginator.page(1) #如果输入的页数不是整数则显示第1页内容
    except EmptyPage:
        products = paginator.page(paginator.num_pages)   #如果输入的的页数不在系统的页数中，则显示最后一页
    return render(request, "create_product.html", {"user":username, "products": products})

@login_required
def product_add_data(request):
    username = request.session.get('user')
    products = Create_product.objects.all()
    if request.method == "POST":
        Model_Name = request.POST.get("modelname", )
        Product_Name = request.POST.get("productname", )
        Tester = request.POST.get("tester", )
        Developer = request.POST.get("developer", )
        Productdesc = request.POST.get("productdesc", )
        Status = request.POST.get("status", )
        Create_product.objects.get_or_create(modelname=Model_Name, productname=Product_Name, tester=Tester, developer=Developer, productdesc=Productdesc,status=Status)
    return render(request, "create_product.html", {"user": username, "products": products})


@login_required
def product_delete_data(request):
    username = request.session.get('user', '')
    products = Create_product.objects.all()
    if request.is_ajax():
        id = request.POST.get('path')
        Create_product.objects.filter(productid=id).delete()
    return render(request, "create_product.html", {"user": username, "products": products})


@login_required
def product_change_data(request):
    username = request.session.get('user')
    products = Create_product.objects.all()
    if request.is_ajax():
        ID = request.POST.get('id')
        change_Model_Name = request.POST.get("changemodel", None)
        change_ProductName = request.POST.get("changeproduct", None)
        change_Tester = request.POST.get("changetester",None)
        change_Developer = request.POST.get("changedeveloper",None)
        change_Productdesc = request.POST.get("changeproductdesc", None)
        change_Status = request.POST.get("changestatus", None)
        Create_product.objects.filter(productid=ID).update(modelname=change_Model_Name, productname=change_ProductName, tester=change_Tester,
                                      developer=change_Developer, productdesc=change_Productdesc, status=change_Status)
    return render(request, "create_product.html", {"user": username, "products": products})

@login_required
def process_api_test(request):
    username = request.session.get('user','')
    steps = need_data_Apis.objects.get_queryset().order_by('productid')
    paginator = Paginator(steps, 12)  # 生成paginator对象,设置每页显示15条记录
    page = request.GET.get('page', 1)  # 获取当前页为第1页
    currentPage = int(page)  # 把当前页转换成整数
    try:
        steps = paginator.page(page)  # 获取当前页码数的记录列表
    except PageNotAnInteger:
        steps = paginator.page(1)  # 如果输入的页数不是整数则显示第1页内容
    except EmptyPage:
        steps = paginator.page(paginator.num_pages)  # 如果输入的的页数不在系统的页数中，则显示最后一页
    return render(request, "with_data_depend_api.html", {"user": username, "steps": steps})


#添加流程接口
@login_required
def add_process_api_test(request):
    username = request.session.get('user','')
    steps = need_data_Apis.objects.all()
    if request.method == "POST":
        newprocessname = request.POST.get("processname")
        newprocessModelname_data = request.POST.get("modelname", )
        newprocessCasename_data = request.POST.get("casename", )
        newprocessUrl_data = request.POST.get("addURL", )
        newprocessMethod_data = request.POST.get("Method", )
        newprocessMergeheaders_data = json.loads(request.POST.get("addmergeheaders", ))
        newprocessMergeform_data = json.loads(request.POST.get("addmergeformdatas", ))
        newprocessMergedepend_data = json.loads(request.POST.get("addmergedependdatas", ))
        newprocessMergecheck_data = json.loads(request.POST.get("addmergecheckdatas", ))
        newprocessCharger_data = request.POST.get("charger", )
        need_data_Apis.objects.create(modelname=newprocessModelname_data, depend_Apiname=newprocessCasename_data, Apiurl_data=newprocessUrl_data,process_name=newprocessname,
                                   Apiheader=newprocessMergeheaders_data, Apimethod=newprocessMethod_data, Apiformdata=newprocessMergeform_data,
                                   Apiexpectresult=newprocessMergecheck_data, Apischarger=newprocessCharger_data, Apidependdata=newprocessMergedepend_data)
    return render(request, "with_data_depend_api.html", {"user": username, "steps": steps})

#删除流程接口
@login_required
def del_process_api_test(request):
    username = request.session.get('user','')
    steps = need_data_Apis.objects.all()
    if request.is_ajax():
        id = request.POST.get('id')
        need_data_Apis.objects.filter(productid=id).delete()
    return render(request, "with_data_depend_api.html", {"user": username, "steps": steps})

#修改流程接口
@login_required
def change_process_api_test(request):
    username = request.session.get('user','')
    steps = need_data_Apis.objects.all()
    if request.is_ajax():
        id = request.POST.get('id')
        newprocessname = request.POST.get("change_processname")
        newprocessModelname_data = request.POST.get("change_modelname", )
        newprocessCasename_data = request.POST.get("change_casename", )
        newprocessUrl_data = request.POST.get("change_URL", )
        newprocessMethod_data = request.POST.get("change_Method", )
        newprocessMergeheaders_data = json.loads(request.POST.get("change_mergeheaders", ))
        newprocessMergeform_data = json.loads(request.POST.get("change_mergeformdatas", ))
        newprocessMergedepend_data = json.loads(request.POST.get("change_mergedependdatas", ))
        newprocessMergecheck_data = json.loads(request.POST.get("change_mergecheckdatas", ))
        newprocessCharger_data = request.POST.get("change_charger", )
        need_data_Apis.objects.filter(productid=id).update(modelname=newprocessModelname_data, depend_Apiname=newprocessCasename_data, Apiurl_data=newprocessUrl_data, process_name=newprocessname,
                                   Apiheader=newprocessMergeheaders_data, Apimethod=newprocessMethod_data,
                                    Apiformdata=newprocessMergeform_data,
                                   Apiexpectresult=newprocessMergecheck_data, Apischarger=newprocessCharger_data, Apidependdata=newprocessMergedepend_data)
    return render(request, "with_data_depend_api.html", {"user": username, "steps": steps})



#展示单一接口定时任务界面
#展示单一接口定时任务在模态框汇总
@login_required
def periodic_task(request):
    username = request.session.get('user','')
    steps = singel_Apis.objects.all()
    tasks = singel_apis_task.objects.all()
    singel_tasks = singel_apis_task.objects.get_queryset().order_by('task_id')
    paginator = Paginator(singel_tasks, 15)  # 生成paginator对象,设置每页显示15条记录
    page = request.GET.get('page', 1)  # 获取当前页为第1页
    currentPage = int(page)  # 把当前页转换成整数
    try:
        singel_tasks = paginator.page(page)  # 获取当前页码数的记录列表
    except PageNotAnInteger:
        singel_tasks = paginator.page(1)  # 如果输入的页数不是整数则显示第1页内容
    except EmptyPage:
        singel_tasks = paginator.page(paginator.num_pages)  # 如果输入的的页数不在系统的页数中，则显示最后一页
    return  render(request, "singel_periodic_task.html", {"user": username, "singel_tasks": singel_tasks, "steps": steps, "tasks":tasks})



#添加单一接口定时任务在模态框汇总
@login_required
def add_task_singel_api_test(request,id=None, modelname=None, apiname=None, apiurl=None, apimethod=None, apiheader=None, apiparameter=None, apiformdata=None, apiexpectresult=None):
    username = request.session.get('user','')
    tasks = singel_apis_task.objects.all()
    if request.method == "POST":
        objs =request.POST.get("objstring")
        obj = json.loads(objs)
        for i in range(0, len(obj)):
            modelname = obj[i]['modelname']
            casename = obj[i]['apiname']
            url = obj[i]['apiurl']
            method = obj[i]['apimethod']
            header = obj[i]['apiheader']
            formdata = obj[i]['apiformdata']
            apiexpectresult = obj[i]['apiexpectresult']
            singel_apis_task.objects.create(task_modelname=modelname, task_casename=casename,task_Apiurl=url, task_Apimethod=method, task_Apiheader=header, task_Apiformdata=formdata, task_Apiexpectresult=apiexpectresult)
        return render(request, "singel_periodic_task.html", {"user": username, "tasks": tasks})

#删除单一接口定时任务
def del_task_singel_api_test(request):
    username = request.session.get('user','')
    tasks = singel_apis_task.objects.all()
    if request.is_ajax():
        id = request.POST.get('id')
        singel_apis_task.objects.filter(task_id=id).delete()
    return render(request, "singel_periodic_task.html", {"user": username, "tasks": tasks})





#展示流程接口定时任务界面
@login_required
def process_periodic_task(request):
    username = request.session.get('user','')
    tasks = process_apis_task.objects.all()
    steps = need_data_Apis.objects.all()
    singel_tasks = process_apis_task.objects.get_queryset().order_by('task_id')
    paginator = Paginator(singel_tasks, 15)  # 生成paginator对象,设置每页显示15条记录
    page = request.GET.get('page', 1)  # 获取当前页为第1页
    currentPage = int(page)  # 把当前页转换成整数
    try:
        singel_tasks = paginator.page(page)  # 获取当前页码数的记录列表
    except PageNotAnInteger:
        singel_tasks = paginator.page(1)  # 如果输入的页数不是整数则显示第1页内容
    except EmptyPage:
        singel_tasks = paginator.page(paginator.num_pages)  # 如果输入的的页数不在系统的页数中，则显示最后一页
    return  render(request, "process_periodic_task.html", {"user": username, "singel_tasks": singel_tasks, "steps": steps, "tasks": tasks})

#删除流程接口定时任务
@login_required
def del_task_process_api_test(request):
    username = request.session.get('user','')
    tasks = process_apis_task.objects.all()
    if request.is_ajax():
        id = request.POST.get('id')
        process_apis_task.objects.filter(task_id=id).delete()
    return render(request, "process_periodic_task.html", {"user": username, "tasks": tasks})



#添加流程接口定时任务在模态框汇总
@login_required
def add_process_api_test_task(request,id=None, modelname=None, apiname=None, apiurl=None, apimethod=None, apiheader=None, apiparameter=None, apiformdata=None, apiexpectresult=None):
    username = request.session.get('user','')
    tasks = process_apis_task.objects.all()
    if request.method == "POST":
        objs =request.POST.get("objstring")
        obj = json.loads(objs)
        for i in range(0, len(obj)):
            modelname = obj[i]['modelname']
            casename = obj[i]['apiname']
            process_name = obj[i]['process_name']
            url = obj[i]['apiurl']
            method = obj[i]['apimethod']
            header = obj[i]['apiheader']
            dependdata = obj[i]['apidependdata']
            formdata = obj[i]['apiformdata']
            apiexpectresult = obj[i]['apiexpectresult']
            process_apis_task.objects.create(task_modelname=modelname, task_depend_Apiname=casename, task_process_name=process_name, task_Apidependdata=dependdata, task_Apiurl_data=url, task_Apimethod=method, task_Apiheader=header, task_Apiformdata=formdata, task_Apiexpectresult=apiexpectresult)
        return render(request, "singel_periodic_task.html", {"user": username, "tasks": tasks})

#立即执行测试用例
@login_required
def start_singel_apis_task(request):
    username = request.session.get('user', '')
    tasks = singel_apis_task.objects.all()
    if request.method == "POST":
        readSQL()
        return render(request, "singel_periodic_task.html",{"user": username})

#获取单一接口执行时间
def get_singel_api_task_time(request):
    username = request.session.get('user', '')
    tasks = process_apis_task.objects.all()
    if request.method == "POST":
        singel_task_date = request.POST.get('date')
        singel_task_frequency = request.POST.get('frequency')
        if singel_task_date & singel_task_frequency !='':
            try:
                scheduler = BackgroundScheduler()
                # 指定时间执行
                scheduler.add_jobstore(start_singel_apis_task, 'date', run_date=singel_task_date)
                #调度开始
                scheduler.start()
                print('Press Ctrl+{0} to exit'.format('Break' if os.name == 'nt' else 'C'))
            except (KeyboardInterrupt, SystemExit):               #键盘打断则退出
                scheduler.shutdown()
        else:
            try:
                scheduler = BackgroundScheduler()
                # 指定间隔时间执行一次
                scheduler.add_jobstore(start_singel_apis_task, 'interval', minutes =singel_task_frequency)
                #调度开始
                scheduler.start()
            except (KeyboardInterrupt, SystemExit):                 #键盘打断则退出
                scheduler.shutdown()
        return render(request, "singel_periodic_task.html", {"user": username, "tasks": tasks})



#请求进度条
@login_required
def get_progress_bar(request):
    response={}
    global finish
    getfinish=finish
    # print (getfinish)
    finish = 0
    response["getfinish"]=getfinish
    return JsonResponse(response)




#将测试结果显示到测试报告中
@login_required
def write_singel_apis_result(request, fail_count=None,pass_count=None):
    username = request.session.get('user', '')
    tasks = singel_apis_task.objects.all()
    read_Results()
    (Pass_count,Fail_count) = read_Results()
    return render(request, "testReport.html", {"user": username, "tasks":tasks, "pass_count":Pass_count, "fail_count":Fail_count})


