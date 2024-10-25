from datetime import datetime
import os
import time

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template import loader
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as django_default_login
from django.contrib.auth.views import login_required
from django.contrib.auth.models import User
from .form import *
from .models import *
from config_busi.models import *
from appcenter.models import *
from sys_user.func import *

# Create your views here.

"""

登录
注册
修改密码
默认注册为系统用户
模块管理员

"""


def register(request):
    if request.method == "GET":
        context = dict()
        context["registerform"] = RegisterForm()
        context["error_message"] = ""
        return HttpResponse(
            loader.get_template(f"register.html").render(context, request)
        )
    obj = mydict(request.POST)
    registerform = RegisterForm(request.POST)
    if not registerform.is_valid():
        return render(request, "login.html", locals())
    username = registerform.cleaned_data.get("username")
    password1 = registerform.cleaned_data.get("password1")
    password2 = registerform.cleaned_data.get("password2")

    user = User.objects.filter(username=username)
    if user:
        return render(
            request,
            "register.html",
            {"registerform": RegisterForm(), "error_message": "用户名已存在"},
        )
    if password1 != password2:
        return render(
            request,
            "register.html",
            {"registerform": RegisterForm(), "error_message": "密码不一致"},
        )
    user_table_id = obj.get("user_table_id")
    table_user_ins = None

    # 用户信息表

    if str(8395) == user_table_id:
        table_user_ins = mc_userinfo
    # 系统管理员

    if str(8417) == user_table_id:
        table_user_ins = mc_supermanager
    if table_user_ins is None:
        print("登录失败,table_user_ins is None,注意表单提交用户表类型与系统配置不符")
    my_user = table_user_ins.objects.filter(username=username)
    if my_user:
        print("该用户已经注册")
        return render(
            request,
            "register.html",
            {"registerform": RegisterForm(), "error_message": "用户名已存在"},
        )
    # save

    my_user = table_user_ins(username=username)
    my_user.save()

    user = User.objects.create_user(
        username=username,
        password=password1,
        email=registerform.cleaned_data.get("email"),
        is_superuser=True,
    )

    user.set_password(password1)
    user.save()
    return redirect("/")


def logout_view(request):
    logout(request)

    response = redirect("/")
    response.delete_cookie("username")
    response.delete_cookie("user_table_id")
    return response


def admin_logout_view(request):
    logout(request)
    response = redirect("/admin")
    response.delete_cookie("username")
    return response


def login_view(request):
    if request.method == "GET":
        context = dict()
        print("in login.html")
        context["loginform"] = LoginForm()

        # response = HttpResponse(loader.get_template('login_v6.html').render(context, request))

        response = HttpResponse(
            loader.get_template("login.html").render(context, request)
        )
        response.delete_cookie("user_table_id")
        return response
    # post

    obj = mydict(request.POST)
    loginform = LoginForm(request.POST)
    # print(loginform)

    if not loginform.is_valid():
        response = render(request, "login.html", locals())
        response.delete_cookie("user_table_id")
        return response
    username = loginform.cleaned_data.get("username")
    password = loginform.cleaned_data.get("password")
    # 与数据库中的用户名和密码比对，django默认保存密码是以哈希形式存储，并不是明文密码，这里的password验证默认调用的是User类的check_password方法，以哈希值比较。

    user = authenticate(request, username=username, password=password)

    user_table_id = obj.get("user_table_id")
    table_user_ins = None

    # 用户信息表

    if str(8395) == user_table_id:
        table_user_ins = mc_userinfo
        page = "userinfo"
    # 系统管理员

    if str(8417) == user_table_id:
        table_user_ins = mc_supermanager
        page = "supermanager"
    if table_user_ins is None:
        print("登录失败,table_user_ins is None,注意表单提交用户表类型与系统配置不符")
        error_message = "登录信息失效"
        return redirect("/", locals())
    my_user = table_user_ins.objects.filter(username=username)
    if len(my_user) == 0:
        print("登录失败")
        error_message = "登录信息失效"
        return redirect("/", locals())
    # 验证如果用户不为空

    if user is None:
        # 强制注册功能
        # 返回登录失败信息
        # error_message = 'login faild'
        # response = render(request, 'login.html', locals())
        # response.delete_cookie('user_table_id')
        # return response
        # 默认即注册:

        # save

        my_user = table_user_ins(username=username)
        my_user.save()
        user = User.objects.create_user(
            username=username,
            password=password,
            email="",
            is_superuser=True,
        )

        user.set_password(password)
        user.save()
    # login方法登录

    django_default_login(request, user)
    print("login success")
    response = HttpResponseRedirect("/index", locals())
    response.set_cookie("user_table_id", user_table_id)
    return response


def usercenter(request):
    if request.method == "GET":
        context = dict()
        context["usercenterform"] = UserCenterForm()
        context["error_message"] = ""
    return render(request, "config_user/index.html", locals())


def index(request):

    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    username = request.user.username

    table_user_ins = None

    # 用户信息表

    if str(8395) == user_table_id:
        table_user_ins = mc_userinfo
        page = "userinfo"
    # 系统管理员

    if str(8417) == user_table_id:
        table_user_ins = mc_supermanager
        page = "supermanager"
    if table_user_ins is None:
        print("登录失败,table_user_ins is None,注意表单提交用户表类型与系统配置不符")
        error_message = "登录信息失效"
        return redirect("/", locals())
    my_user = table_user_ins.objects.filter(username=username)
    if len(my_user) == 0:
        print("登录失败")
        error_message = "登录信息失效"
        return redirect("/", locals())
    if request.method == "GET":
        # 主页默认配置信息

        """若需控制访问权限，可在此处加上判断条件，如：
            if not request.user.is_superuser:
                return render(request, 'index.html', locals())

            # 判断表内容对于当前用户的权限:
                1. 若是管理员，则显示所有项目
                2. 若是普通用户，则显示当前用户所属内容

        Returns:
            response: 请求处理
        """

        tab_mc_videoinfo = {
            "params": mc_videoinfo().toParams_zh(),
            "records": mc_videoinfo.objects.all()[::-1],
            "json": [m.toJson() for m in mc_videoinfo.objects.all()[::-1]],
        }

        tab_mc_videocategkwkwory = {
            "params": mc_videocategkwkwory().toParams_zh(),
            "records": mc_videocategkwkwory.objects.all()[::-1],
            "json": [m.toJson() for m in mc_videocategkwkwory.objects.all()[::-1]],
        }

        tab_mc_videotag = {
            "params": mc_videotag().toParams_zh(),
            "records": mc_videotag.objects.all()[::-1],
            "json": [m.toJson() for m in mc_videotag.objects.all()[::-1]],
        }

        tab_mc_videofilestkwkworage = {
            "params": mc_videofilestkwkworage().toParams_zh(),
            "records": mc_videofilestkwkworage.objects.all()[::-1],
            "json": [m.toJson() for m in mc_videofilestkwkworage.objects.all()[::-1]],
        }

        tab_mc_videoplayreckwkword = {
            "params": mc_videoplayreckwkword().toParams_zh(),
            "records": mc_videoplayreckwkword.objects.all()[::-1],
            "json": [m.toJson() for m in mc_videoplayreckwkword.objects.all()[::-1]],
        }

        tab_mc_videocomment = {
            "params": mc_videocomment().toParams_zh(),
            "records": mc_videocomment.objects.all()[::-1],
            "json": [m.toJson() for m in mc_videocomment.objects.all()[::-1]],
        }

        tab_mc_videolike = {
            "params": mc_videolike().toParams_zh(),
            "records": mc_videolike.objects.all()[::-1],
            "json": [m.toJson() for m in mc_videolike.objects.all()[::-1]],
        }

        tab_mc_videoshare = {
            "params": mc_videoshare().toParams_zh(),
            "records": mc_videoshare.objects.all()[::-1],
            "json": [m.toJson() for m in mc_videoshare.objects.all()[::-1]],
        }

        tab_mc_videoviewduration = {
            "params": mc_videoviewduration().toParams_zh(),
            "records": mc_videoviewduration.objects.all()[::-1],
            "json": [m.toJson() for m in mc_videoviewduration.objects.all()[::-1]],
        }

        tab_mc_videouploader = {
            "params": mc_videouploader().toParams_zh(),
            "records": mc_videouploader.objects.all()[::-1],
            "json": [m.toJson() for m in mc_videouploader.objects.all()[::-1]],
        }

        tab_mc_userinfo = {
            "params": mc_userinfo().toParams_zh(),
            "records": mc_userinfo.objects.all()[::-1],
            "json": [m.toJson() for m in mc_userinfo.objects.all()[::-1]],
        }

        tab_mc_userpermkwkwission = {
            "params": mc_userpermkwkwission().toParams_zh(),
            "records": mc_userpermkwkwission.objects.all()[::-1],
            "json": [m.toJson() for m in mc_userpermkwkwission.objects.all()[::-1]],
        }

        tab_mc_userwatchhkwkwistkwkwory = {
            "params": mc_userwatchhkwkwistkwkwory().toParams_zh(),
            "records": mc_userwatchhkwkwistkwkwory.objects.all()[::-1],
            "json": [
                m.toJson() for m in mc_userwatchhkwkwistkwkwory.objects.all()[::-1]
            ],
        }

        tab_mc_videoauditstatus = {
            "params": mc_videoauditstatus().toParams_zh(),
            "records": mc_videoauditstatus.objects.all()[::-1],
            "json": [m.toJson() for m in mc_videoauditstatus.objects.all()[::-1]],
        }

        tab_mc_videocoverimage = {
            "params": mc_videocoverimage().toParams_zh(),
            "records": mc_videocoverimage.objects.all()[::-1],
            "json": [m.toJson() for m in mc_videocoverimage.objects.all()[::-1]],
        }

        tab_mc_videomatrixconfig = {
            "params": mc_videomatrixconfig().toParams_zh(),
            "records": mc_videomatrixconfig.objects.all()[::-1],
            "json": [m.toJson() for m in mc_videomatrixconfig.objects.all()[::-1]],
        }

        tab_mc_videomatrixnode = {
            "params": mc_videomatrixnode().toParams_zh(),
            "records": mc_videomatrixnode.objects.all()[::-1],
            "json": [m.toJson() for m in mc_videomatrixnode.objects.all()[::-1]],
        }

        tab_mc_videomatrixplayreckwkword = {
            "params": mc_videomatrixplayreckwkword().toParams_zh(),
            "records": mc_videomatrixplayreckwkword.objects.all()[::-1],
            "json": [
                m.toJson() for m in mc_videomatrixplayreckwkword.objects.all()[::-1]
            ],
        }

        tab_mc_videorelatedcontent = {
            "params": mc_videorelatedcontent().toParams_zh(),
            "records": mc_videorelatedcontent.objects.all()[::-1],
            "json": [m.toJson() for m in mc_videorelatedcontent.objects.all()[::-1]],
        }

        tab_mc_videoerrkwkworlog = {
            "params": mc_videoerrkwkworlog().toParams_zh(),
            "records": mc_videoerrkwkworlog.objects.all()[::-1],
            "json": [m.toJson() for m in mc_videoerrkwkworlog.objects.all()[::-1]],
        }

        tab_mc_videopopularity = {
            "params": mc_videopopularity().toParams_zh(),
            "records": mc_videopopularity.objects.all()[::-1],
            "json": [m.toJson() for m in mc_videopopularity.objects.all()[::-1]],
        }

        tab_mc_videorecommendationparams = {
            "params": mc_videorecommendationparams().toParams_zh(),
            "records": mc_videorecommendationparams.objects.all()[::-1],
            "json": [
                m.toJson() for m in mc_videorecommendationparams.objects.all()[::-1]
            ],
        }

        tab_mc_videoadinfo = {
            "params": mc_videoadinfo().toParams_zh(),
            "records": mc_videoadinfo.objects.all()[::-1],
            "json": [m.toJson() for m in mc_videoadinfo.objects.all()[::-1]],
        }

        tab_mc_videoadplayreckwkword = {
            "params": mc_videoadplayreckwkword().toParams_zh(),
            "records": mc_videoadplayreckwkword.objects.all()[::-1],
            "json": [m.toJson() for m in mc_videoadplayreckwkword.objects.all()[::-1]],
        }

        tab_mc_videodanmu = {
            "params": mc_videodanmu().toParams_zh(),
            "records": mc_videodanmu.objects.all()[::-1],
            "json": [m.toJson() for m in mc_videodanmu.objects.all()[::-1]],
        }

        tab_mc_videodanmublockwkwkwords = {
            "params": mc_videodanmublockwkwkwords().toParams_zh(),
            "records": mc_videodanmublockwkwkwords.objects.all()[::-1],
            "json": [
                m.toJson() for m in mc_videodanmublockwkwkwords.objects.all()[::-1]
            ],
        }

        tab_mc_videomultilkwkwingualsubtitles = {
            "params": mc_videomultilkwkwingualsubtitles().toParams_zh(),
            "records": mc_videomultilkwkwingualsubtitles.objects.all()[::-1],
            "json": [
                m.toJson()
                for m in mc_videomultilkwkwingualsubtitles.objects.all()[::-1]
            ],
        }

        tab_mc_videotranscodkwkwingtkwkwask = {
            "params": mc_videotranscodkwkwingtkwkwask().toParams_zh(),
            "records": mc_videotranscodkwkwingtkwkwask.objects.all()[::-1],
            "json": [
                m.toJson() for m in mc_videotranscodkwkwingtkwkwask.objects.all()[::-1]
            ],
        }

        tab_mc_videoanalyskwkwismetrics = {
            "params": mc_videoanalyskwkwismetrics().toParams_zh(),
            "records": mc_videoanalyskwkwismetrics.objects.all()[::-1],
            "json": [
                m.toJson() for m in mc_videoanalyskwkwismetrics.objects.all()[::-1]
            ],
        }

        tab_mc_videoqualityassessment = {
            "params": mc_videoqualityassessment().toParams_zh(),
            "records": mc_videoqualityassessment.objects.all()[::-1],
            "json": [m.toJson() for m in mc_videoqualityassessment.objects.all()[::-1]],
        }

        tab_mc_videowatermarkinfo = {
            "params": mc_videowatermarkinfo().toParams_zh(),
            "records": mc_videowatermarkinfo.objects.all()[::-1],
            "json": [m.toJson() for m in mc_videowatermarkinfo.objects.all()[::-1]],
        }

        tab_mc_videocopyrightinfo = {
            "params": mc_videocopyrightinfo().toParams_zh(),
            "records": mc_videocopyrightinfo.objects.all()[::-1],
            "json": [m.toJson() for m in mc_videocopyrightinfo.objects.all()[::-1]],
        }

        tab_mc_supermanager = {
            "params": mc_supermanager().toParams_zh(),
            "records": mc_supermanager.objects.all()[::-1],
            "json": [m.toJson() for m in mc_supermanager.objects.all()[::-1]],
        }
    __version__ = settings.GLOBAL_VERSION

    if request.method == "GET":

        # 配置不同用户访问的主页不同
        # return render(request, f'index_{page}.html', locals())

        return render(request, f"index{__version__}.html", locals())
    # 处理post请求，一般不建议在这里添加多余功能。

    return render(request, f"index{__version__}.html", locals())
