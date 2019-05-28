#coding=utf-8
from django.shortcuts import render
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
import json
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.contrib import auth
from django.contrib import messages
from django.core.paginator import  Paginator, EmptyPage, PageNotAnInteger
from apptest.models import Appcasestep,Appcase,Appcase_keywords,apptest_task
from django.core.paginator import  Paginator, EmptyPage, PageNotAnInteger
import os
import pyautogui
from apptest.tasks import write_name_txt,readSQLCounts,get_task_stepdata,getcasename_from_SQL,get_apptask_times
import time
from apptest.get_appcase_stepdata import readappcaseSQL,write_to_txt,remove_apptest_txt,run_in_terminal

# Create your views here.


#显示web测试用例界面
@login_required
def app_testcase_page(request):
    username = request.session.get('user', '')
    appcases = Appcase.objects.get_queryset().order_by('id')
    paginator = Paginator(appcases, 12)  # 生成paginator对象,设置每页显示15条记录
    page = request.GET.get('page', 1)  # 获取当前页为第1页
    currentPage = int(page)  # 把当前页转换成整数
    try:
        appcases = paginator.page(page)  # 获取当前页码数的记录列表
    except PageNotAnInteger:
        appcases = paginator.page(1)  # 如果输入的页数不是整数则显示第1页内容
    except EmptyPage:
        appcases = paginator.page(paginator.num_pages)  # 如果输入的的页数不在系统的页数中，则显示最后一页
    return render(request, "App_test_robotframework.html", {"user": username, "webcases": appcases})

# #app测试用例名称添加
@login_required
def add_app_casename(request):
    username = request.session.get('user', '')
    appcases = Appcase.objects.all()
    if request.method == "POST":
        appmodelname = request.POST.get("appmodelname", )
        appcasename = request.POST.get("appcasename", )
        appcharger = request.POST.get("appcharger", )
        appaddcasedesc = request.POST.get("appaddcasedesc", )
        Appcase.objects.get_or_create(appcase_models=appmodelname,appcasename=appcasename,appcase_charger=appcharger,appcasedesc=appaddcasedesc)
        return render(request, "App_test_robotframework.html", {"user": username, "appcases":appcases})


#删除app测试用例
@login_required
def del_app_casename(request):
    username = request.session.get('user', '')
    appcases =Appcase.objects.all()
    if request.method == "POST":
        appcaseID = request.POST.get("id", )
        Appcase.objects.filter(id=appcaseID).delete()
        return render(request, "App_test_robotframework.html", {"user": username, "appcases":appcases})



#显示app测试步骤添加
@login_required
def display_app_casesteps(request):
    username = request.session.get('user', '')
    appcaseid = request.GET.get('appcase.id',None)
    appcase = Appcase.objects.get(id=appcaseid)
    appcasesteps = Appcasestep.objects.all()
    return render(request,"appcasestep_manage.html",{"user": username,"appcasesteps":appcasesteps,"appcase":appcase})


#删除web测试步骤
@login_required
def delete_app_casesteps(request):
    appcaseid = request.POST.get("casename_id")
    username = request.session.get('user', '')
    appcase = Appcase.objects.get(id=appcaseid)
    appcasesteps = Appcasestep.objects.all()
    stepid = request.POST.get("step_id")
    Appcasestep.objects.filter(Appcase_id=appcaseid,id=stepid).delete()
    return render(request, "appcasestep_manage.html",{"user": username, "appcasesteps": appcasesteps, "appcase": appcase})


#上传图片
@login_required
def upload_file(request):
    path = os.path.abspath(os.path.dirname(__file__))
    media_path = path+"\\"+"media"
    media_name_list = os.listdir(media_path)
    # 请求方法为POST时，进行处理
    if request.method == "POST":
        # 获取上传的文件，如果没有文件，则默认为None
        File = request.FILES.get("myfile", None)
        if File is None:
            return HttpResponse(u"没有需要上传的文件")
        else:
            #打开特定的文件进行二进制的写操作
            #print(os.path.exists('/temp_file/'))
            with open("./apptest/media/%s" % File.name, 'wb+') as f:
                #分块写入文件
                for chunk in  File.chunks():
                    if str(File) in media_name_list:
                        return HttpResponse("截图文件:" + File.name + "已存在请查看")
                    else:
                        f.write(chunk)
                        return HttpResponse("UPload over!")
    else:
        return  render(request, "test.html")


#立即执行测试用例
@login_required
def maoyan_test(request):
    username = request.session.get('user', '')
    tasks = Appcasestep.objects.all()
    if request.method == "POST":
        upperlevel_id = request.POST.get("casename_id")
        write_to_txt(upperlevel_id)
        time.sleep(1)
        readappcaseSQL(upperlevel_id)
    return render(request, "appcasestep_manage.html",{"user": username, "tasks": tasks})

#用例执行成功后保存
@login_required
def remove_test_txt(request):
    username = request.session.get('user', '')
    tasks = Appcasestep.objects.all()
    if request.method =="POST":
        txtname = request.POST.get("casename_id")
        remove_apptest_txt(txtname)
    return render(request, "appcasestep_manage.html", {"user": username, "tasks": tasks})



#展示web定时任务界面
@login_required
def appUI_periodic_task(request):
    username = request.session.get('user','')
    tasks = apptest_task.objects.all()
    cases = Appcase.objects.all()
    singel_tasks = apptest_task.objects.get_queryset().order_by('task_id')
    paginator = Paginator(singel_tasks, 15)  # 生成paginator对象,设置每页显示15条记录
    page = request.GET.get('page', 1)  # 获取当前页为第1页
    currentPage = int(page)  # 把当前页转换成整数
    try:
        singel_tasks = paginator.page(page)  # 获取当前页码数的记录列表
    except PageNotAnInteger:
        singel_tasks = paginator.page(1)  # 如果输入的页数不是整数则显示第1页内容
    except EmptyPage:
        singel_tasks = paginator.page(paginator.num_pages)  # 如果输入的的页数不在系统的页数中，则显示最后一页
    return  render(request, "appcase_periodic_task.html", {"user": username, "singel_tasks": singel_tasks,"cases":cases,"tasks": tasks})

#添加webUI测试定时任务在模态框汇总
@login_required
def add_task_appcase_test(request):
    username = request.session.get('user', '')
    tasks = apptest_task.objects.all()
    if request.method == "POST":
        objs = request.POST.get("objstring")
        obj = json.loads(objs)
        for i in range(0, len(obj)):
            id=int(obj[i]['id'])
            appcase_models = obj[i]['appcase_models']
            appcasename = obj[i]['appcasename']
            appcasedesc = obj[i]['appcasedesc']
            apptest_task.objects.create(case_id=id,task_modelname=appcase_models,task_casename=appcasename,task_stepdesc=appcasedesc)
        return  render(request, "appcase_periodic_task.html",{"user": username, "tasks": tasks})


#立即执行当前列表内的任务
@login_required
def run_appcase_immediately(request):
    username = request.session.get('user', '')
    tasks = apptest_task.objects.all()
    if request.method == "POST":
        write_name_txt()
        time.sleep(2)
        get_task_stepdata()
        time.sleep(1)
        run_in_terminal()
    return render(request, "appcase_periodic_task.html", {"user": username, "tasks": tasks})



#获取前端的定时任务时间并传递给task
def get_appcase_task_time(request):
    username = request.session.get('user', '')
    data = {
        'username':username,
        'use':'webcase_periodic_tasktime_get',
    }
    if request.method == "POST":
        singel_task_date = request.POST.get('date')
        get_apptask_times(singel_task_date)
    return HttpResponse(json.dumps(data))