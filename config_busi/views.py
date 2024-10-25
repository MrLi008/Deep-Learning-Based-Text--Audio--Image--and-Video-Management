from datetime import datetime
import os
import time
import uuid

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import login_required
from .form import *
from .models import *
from appcenter.models import *
from sys_user.func import *


def resp(res, msg, url=None, **kwargs):
    return {"res": res, "msg": msg, "url": url, **kwargs}


# Create your views here.


def index(request):
    records = [
        {
            "id": 1,
        },
        {"id": 2},
    ]
    return render(request, "config_visual/index.html", locals())


@login_required
def view_videoinfo(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 视频信息表 系统管理员(8417)

    if user_table_id == str(8417):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 视频ID

        mcauthfield_videoid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 视频标题

        mcauthfield_videotitle = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 视频描述

        mcauthfield_videodescription = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 上传时间

        mcauthfield_uploadtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 视频时长秒

        mcauthfield_duration = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 视频分辨率

        mcauthfield_resolution = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 文件类型

        mcauthfield_filetype = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 文件大小KBMBGB

        mcauthfield_filesize = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 创建者ID关联用户

        mcauthfield_creatkwkworid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 类别ID关联视频类别

        mcauthfield_categkwkworyid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }
    # 视频信息表 用户信息表(8395)

    if user_table_id == str(8395):
        config_user_table = mc_userinfo
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 视频ID

        mcauthfield_videoid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 视频标题

        mcauthfield_videotitle = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 视频描述

        mcauthfield_videodescription = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 上传时间

        mcauthfield_uploadtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 视频时长秒

        mcauthfield_duration = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 视频分辨率

        mcauthfield_resolution = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 文件类型

        mcauthfield_filetype = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 文件大小KBMBGB

        mcauthfield_filesize = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 创建者ID关联用户

        mcauthfield_creatkwkworid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 类别ID关联视频类别

        mcauthfield_categkwkworyid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_videoinfo.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_videoinfo().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_videoinfo.objects.filter(**filter)
        else:
            records = mc_videoinfo.objects.all()
        # 加载界面中下拉框所需数据

        data_mc_userinfo_57907 = []
        for m in mc_userinfo.objects.all():
            mobj = m.toJson()
            data_mc_userinfo_57907.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("username"),
                }
            )
        data_mc_videocategkwkwory_57908 = []
        for m in mc_videocategkwkwory.objects.all():
            mobj = m.toJson()
            data_mc_videocategkwkwory_57908.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("name"),
                }
            )
        return render(request, "config_busi/videoinfo.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_videoinfo()

        # 视频ID

        if mcauthfield_videoid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.videoid = str(uuid.uuid4())
        # 视频标题

        if mcauthfield_videotitle["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.videotitle = obj.get("videotitle")
        # 视频描述

        if mcauthfield_videodescription["mcauthchange"]:

            # TextField # 其他情况/待补充

            ins_table_busi.videodescription = obj.get("videodescription")
        # 上传时间

        if mcauthfield_uploadtime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.uploadtime = obj.get("uploadtime")
        # 视频时长秒

        if mcauthfield_duration["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.duration = obj.get("duration")
        # 视频分辨率

        if mcauthfield_resolution["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.resolution = obj.get("resolution")
        # 文件类型

        if mcauthfield_filetype["mcauthchange"]:

            # Save FileFileField 若上传了文件

            if "filetype" in request.FILES:
                ins_table_busi.filetype = request.FILES["filetype"]
        # 文件大小KBMBGB

        if mcauthfield_filesize["mcauthchange"]:

            # Save FileFileField 若上传了文件

            if "filesize" in request.FILES:
                ins_table_busi.filesize = request.FILES["filesize"]
        # 创建者ID关联用户

        if mcauthfield_creatkwkworid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.creatkwkworid = obj.get("creatkwkworid")
        # 类别ID关联视频类别

        if mcauthfield_categkwkworyid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.categkwkworyid = obj.get("categkwkworyid")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_videoinfo.objects.get(id=obj.get("_id_upd"))

        # 视频ID

        if mcauthfield_videoid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.videoid = str(uuid.uuid4())

            ins_table_busi.videoid = str(ins_table_busi.videoid)
        # 视频标题

        if mcauthfield_videotitle["mcauthchange"]:

            # CharField

            ins_table_busi.videotitle = obj.get("videotitle")
        # 视频描述

        if mcauthfield_videodescription["mcauthchange"]:

            # TextField

            ins_table_busi.videodescription = obj.get("videodescription")
        # 上传时间

        if mcauthfield_uploadtime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.uploadtime = obj.get("uploadtime")
        # 视频时长秒

        if mcauthfield_duration["mcauthchange"]:

            # CharField

            ins_table_busi.duration = obj.get("duration")
        # 视频分辨率

        if mcauthfield_resolution["mcauthchange"]:

            # CharField

            ins_table_busi.resolution = obj.get("resolution")
        # 文件类型

        if mcauthfield_filetype["mcauthchange"]:

            # Save File FileField

            if "filetype" in request.FILES:
                ins_table_busi.filetype = request.FILES["filetype"]
        # 文件大小KBMBGB

        if mcauthfield_filesize["mcauthchange"]:

            # Save File FileField

            if "filesize" in request.FILES:
                ins_table_busi.filesize = request.FILES["filesize"]
        # 创建者ID关联用户

        if mcauthfield_creatkwkworid["mcauthchange"]:

            # SelectField

            ins_table_busi.creatkwkworid = obj.get("creatkwkworid")
        # 类别ID关联视频类别

        if mcauthfield_categkwkworyid["mcauthchange"]:

            # SelectField

            ins_table_busi.categkwkworyid = obj.get("categkwkworyid")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_videoinfo.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_videoinfo.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/videoinfo")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_videocategkwkwory(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 视频分类表 系统管理员(8417)

    if user_table_id == str(8417):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 分类名称

        mcauthfield_name = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 分类描述

        mcauthfield_description = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 父分类ID用于构建分类层级如果为顶级分类则为NULL

        mcauthfield_parentid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 创建时间

        mcauthfield_createtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 更新时间

        mcauthfield_updatetime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 是否激活用于控制分类是否显示在前端

        mcauthfield_kwkwisactive = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 排序顺序

        mcauthfield_skwkwortorder = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }
    # 视频分类表 用户信息表(8395)

    if user_table_id == str(8395):
        config_user_table = mc_userinfo
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 分类名称

        mcauthfield_name = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 分类描述

        mcauthfield_description = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 父分类ID用于构建分类层级如果为顶级分类则为NULL

        mcauthfield_parentid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 创建时间

        mcauthfield_createtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 更新时间

        mcauthfield_updatetime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 是否激活用于控制分类是否显示在前端

        mcauthfield_kwkwisactive = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 排序顺序

        mcauthfield_skwkwortorder = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_videocategkwkwory.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_videocategkwkwory().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_videocategkwkwory.objects.filter(**filter)
        else:
            records = mc_videocategkwkwory.objects.all()
        # 加载界面中下拉框所需数据

        return render(request, "config_busi/videocategkwkwory.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_videocategkwkwory()

        # 分类名称

        if mcauthfield_name["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.name = obj.get("name")
        # 分类描述

        if mcauthfield_description["mcauthchange"]:

            # TextField # 其他情况/待补充

            ins_table_busi.description = obj.get("description")
        # 父分类ID用于构建分类层级如果为顶级分类则为NULL

        if mcauthfield_parentid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.parentid = str(uuid.uuid4())
        # 创建时间

        if mcauthfield_createtime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.createtime = obj.get("createtime")
        # 更新时间

        if mcauthfield_updatetime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.updatetime = obj.get("updatetime")
        # 是否激活用于控制分类是否显示在前端

        if mcauthfield_kwkwisactive["mcauthchange"]:

            # BooleanField # 其他情况/待补充

            ins_table_busi.kwkwisactive = obj.get("kwkwisactive")
        # 排序顺序

        if mcauthfield_skwkwortorder["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.skwkwortorder = obj.get("skwkwortorder")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_videocategkwkwory.objects.get(id=obj.get("_id_upd"))

        # 分类名称

        if mcauthfield_name["mcauthchange"]:

            # CharField

            ins_table_busi.name = obj.get("name")
        # 分类描述

        if mcauthfield_description["mcauthchange"]:

            # TextField

            ins_table_busi.description = obj.get("description")
        # 父分类ID用于构建分类层级如果为顶级分类则为NULL

        if mcauthfield_parentid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.parentid = str(uuid.uuid4())

            ins_table_busi.parentid = str(ins_table_busi.parentid)
        # 创建时间

        if mcauthfield_createtime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.createtime = obj.get("createtime")
        # 更新时间

        if mcauthfield_updatetime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.updatetime = obj.get("updatetime")
        # 是否激活用于控制分类是否显示在前端

        if mcauthfield_kwkwisactive["mcauthchange"]:

            # BooleanField

            ins_table_busi.kwkwisactive = obj.get("kwkwisactive")
        # 排序顺序

        if mcauthfield_skwkwortorder["mcauthchange"]:

            # CharField

            ins_table_busi.skwkwortorder = obj.get("skwkwortorder")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_videocategkwkwory.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_videocategkwkwory.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/videocategkwkwory")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_videotag(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 视频标签表 系统管理员(8417)

    if user_table_id == str(8417):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 标签ID

        mcauthfield_tagid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 标签名称

        mcauthfield_tagname = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 视频ID关联字段指向视频中的视频ID

        mcauthfield_videoid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 创建时间

        mcauthfield_createtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 更新时间

        mcauthfield_updatetime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 是否激活用于标记标签是否可用

        mcauthfield_kwkwisactive = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 标签描述

        mcauthfield_description = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 创建者ID关联字段指向用户中的用户ID

        mcauthfield_creatkwkworid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }
    # 视频标签表 用户信息表(8395)

    if user_table_id == str(8395):
        config_user_table = mc_userinfo
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 标签ID

        mcauthfield_tagid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 标签名称

        mcauthfield_tagname = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 视频ID关联字段指向视频中的视频ID

        mcauthfield_videoid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 创建时间

        mcauthfield_createtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 更新时间

        mcauthfield_updatetime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 是否激活用于标记标签是否可用

        mcauthfield_kwkwisactive = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 标签描述

        mcauthfield_description = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 创建者ID关联字段指向用户中的用户ID

        mcauthfield_creatkwkworid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_videotag.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_videotag().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_videotag.objects.filter(**filter)
        else:
            records = mc_videotag.objects.all()
        # 加载界面中下拉框所需数据

        data_mc_videoinfo_57918 = []
        for m in mc_videoinfo.objects.all():
            mobj = m.toJson()
            data_mc_videoinfo_57918.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("videotitle"),
                }
            )
        data_mc_userinfo_57923 = []
        for m in mc_userinfo.objects.all():
            mobj = m.toJson()
            data_mc_userinfo_57923.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("username"),
                }
            )
        return render(request, "config_busi/videotag.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_videotag()

        # 标签ID

        if mcauthfield_tagid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.tagid = str(uuid.uuid4())
        # 标签名称

        if mcauthfield_tagname["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.tagname = obj.get("tagname")
        # 视频ID关联字段指向视频中的视频ID

        if mcauthfield_videoid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.videoid = obj.get("videoid")
        # 创建时间

        if mcauthfield_createtime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.createtime = obj.get("createtime")
        # 更新时间

        if mcauthfield_updatetime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.updatetime = obj.get("updatetime")
        # 是否激活用于标记标签是否可用

        if mcauthfield_kwkwisactive["mcauthchange"]:

            # BooleanField # 其他情况/待补充

            ins_table_busi.kwkwisactive = obj.get("kwkwisactive")
        # 标签描述

        if mcauthfield_description["mcauthchange"]:

            # TextField # 其他情况/待补充

            ins_table_busi.description = obj.get("description")
        # 创建者ID关联字段指向用户中的用户ID

        if mcauthfield_creatkwkworid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.creatkwkworid = obj.get("creatkwkworid")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_videotag.objects.get(id=obj.get("_id_upd"))

        # 标签ID

        if mcauthfield_tagid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.tagid = str(uuid.uuid4())

            ins_table_busi.tagid = str(ins_table_busi.tagid)
        # 标签名称

        if mcauthfield_tagname["mcauthchange"]:

            # CharField

            ins_table_busi.tagname = obj.get("tagname")
        # 视频ID关联字段指向视频中的视频ID

        if mcauthfield_videoid["mcauthchange"]:

            # SelectField

            ins_table_busi.videoid = obj.get("videoid")
        # 创建时间

        if mcauthfield_createtime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.createtime = obj.get("createtime")
        # 更新时间

        if mcauthfield_updatetime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.updatetime = obj.get("updatetime")
        # 是否激活用于标记标签是否可用

        if mcauthfield_kwkwisactive["mcauthchange"]:

            # BooleanField

            ins_table_busi.kwkwisactive = obj.get("kwkwisactive")
        # 标签描述

        if mcauthfield_description["mcauthchange"]:

            # TextField

            ins_table_busi.description = obj.get("description")
        # 创建者ID关联字段指向用户中的用户ID

        if mcauthfield_creatkwkworid["mcauthchange"]:

            # SelectField

            ins_table_busi.creatkwkworid = obj.get("creatkwkworid")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_videotag.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_videotag.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/videotag")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_videofilestkwkworage(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 视频文件存储表 系统管理员(8417)

    if user_table_id == str(8417):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 视频ID

        mcauthfield_videoid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 文件名

        mcauthfield_filename = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 文件存储路径

        mcauthfield_filepath = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 文件大小单位MB

        mcauthfield_filesize = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 上传时间

        mcauthfield_uploadtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 视频时长单位秒

        mcauthfield_duration = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 分辨率例如1920x1080

        mcauthfield_resolution = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 视频格式例如mp4

        mcauthfield_kwkwfkwkwormat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 创建者ID关联用户

        mcauthfield_creatkwkworid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 分类ID关联视频分类

        mcauthfield_categkwkworyid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }
    # 视频文件存储表 用户信息表(8395)

    if user_table_id == str(8395):
        config_user_table = mc_userinfo
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 视频ID

        mcauthfield_videoid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 文件名

        mcauthfield_filename = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 文件存储路径

        mcauthfield_filepath = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 文件大小单位MB

        mcauthfield_filesize = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 上传时间

        mcauthfield_uploadtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 视频时长单位秒

        mcauthfield_duration = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 分辨率例如1920x1080

        mcauthfield_resolution = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 视频格式例如mp4

        mcauthfield_kwkwfkwkwormat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 创建者ID关联用户

        mcauthfield_creatkwkworid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 分类ID关联视频分类

        mcauthfield_categkwkworyid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_videofilestkwkworage.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_videofilestkwkworage().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_videofilestkwkworage.objects.filter(**filter)
        else:
            records = mc_videofilestkwkworage.objects.all()
        # 加载界面中下拉框所需数据

        data_mc_userinfo_57932 = []
        for m in mc_userinfo.objects.all():
            mobj = m.toJson()
            data_mc_userinfo_57932.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("username"),
                }
            )
        data_mc_videocategkwkwory_57933 = []
        for m in mc_videocategkwkwory.objects.all():
            mobj = m.toJson()
            data_mc_videocategkwkwory_57933.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("name"),
                }
            )
        return render(request, "config_busi/videofilestkwkworage.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_videofilestkwkworage()

        # 视频ID

        if mcauthfield_videoid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.videoid = str(uuid.uuid4())
        # 文件名

        if mcauthfield_filename["mcauthchange"]:

            # Save FileFileField 若上传了文件

            if "filename" in request.FILES:
                ins_table_busi.filename = request.FILES["filename"]
        # 文件存储路径

        if mcauthfield_filepath["mcauthchange"]:

            # Save FileFileField 若上传了文件

            if "filepath" in request.FILES:
                ins_table_busi.filepath = request.FILES["filepath"]
        # 文件大小单位MB

        if mcauthfield_filesize["mcauthchange"]:

            # Save FileFileField 若上传了文件

            if "filesize" in request.FILES:
                ins_table_busi.filesize = request.FILES["filesize"]
        # 上传时间

        if mcauthfield_uploadtime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.uploadtime = obj.get("uploadtime")
        # 视频时长单位秒

        if mcauthfield_duration["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.duration = obj.get("duration")
        # 分辨率例如1920x1080

        if mcauthfield_resolution["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.resolution = obj.get("resolution")
        # 视频格式例如mp4

        if mcauthfield_kwkwfkwkwormat["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.kwkwfkwkwormat = obj.get("kwkwfkwkwormat")
        # 创建者ID关联用户

        if mcauthfield_creatkwkworid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.creatkwkworid = obj.get("creatkwkworid")
        # 分类ID关联视频分类

        if mcauthfield_categkwkworyid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.categkwkworyid = obj.get("categkwkworyid")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_videofilestkwkworage.objects.get(id=obj.get("_id_upd"))

        # 视频ID

        if mcauthfield_videoid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.videoid = str(uuid.uuid4())

            ins_table_busi.videoid = str(ins_table_busi.videoid)
        # 文件名

        if mcauthfield_filename["mcauthchange"]:

            # Save File FileField

            if "filename" in request.FILES:
                ins_table_busi.filename = request.FILES["filename"]
        # 文件存储路径

        if mcauthfield_filepath["mcauthchange"]:

            # Save File FileField

            if "filepath" in request.FILES:
                ins_table_busi.filepath = request.FILES["filepath"]
        # 文件大小单位MB

        if mcauthfield_filesize["mcauthchange"]:

            # Save File FileField

            if "filesize" in request.FILES:
                ins_table_busi.filesize = request.FILES["filesize"]
        # 上传时间

        if mcauthfield_uploadtime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.uploadtime = obj.get("uploadtime")
        # 视频时长单位秒

        if mcauthfield_duration["mcauthchange"]:

            # CharField

            ins_table_busi.duration = obj.get("duration")
        # 分辨率例如1920x1080

        if mcauthfield_resolution["mcauthchange"]:

            # CharField

            ins_table_busi.resolution = obj.get("resolution")
        # 视频格式例如mp4

        if mcauthfield_kwkwfkwkwormat["mcauthchange"]:

            # CharField

            ins_table_busi.kwkwfkwkwormat = obj.get("kwkwfkwkwormat")
        # 创建者ID关联用户

        if mcauthfield_creatkwkworid["mcauthchange"]:

            # SelectField

            ins_table_busi.creatkwkworid = obj.get("creatkwkworid")
        # 分类ID关联视频分类

        if mcauthfield_categkwkworyid["mcauthchange"]:

            # SelectField

            ins_table_busi.categkwkworyid = obj.get("categkwkworyid")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_videofilestkwkworage.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_videofilestkwkworage.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/videofilestkwkworage")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_videoplayreckwkword(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 视频播放记录表 系统管理员(8417)

    if user_table_id == str(8417):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 视频ID关联视频信息

        mcauthfield_videoid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 用户ID关联用户信息

        mcauthfield_userid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 播放开始时间

        mcauthfield_playstarttime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 播放结束时间

        mcauthfield_playendtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 播放时长秒

        mcauthfield_playduration = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 播放状态如已完成、暂停、中断

        mcauthfield_playstatus = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 设备类型如手机、平板、电脑

        mcauthfield_devicetype = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # IP地址

        mcauthfield_ipaddress = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 播放位置可选根据IP解析的地理位置

        mcauthfield_location = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }
    # 视频播放记录表 用户信息表(8395)

    if user_table_id == str(8395):
        config_user_table = mc_userinfo
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 视频ID关联视频信息

        mcauthfield_videoid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 用户ID关联用户信息

        mcauthfield_userid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 播放开始时间

        mcauthfield_playstarttime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 播放结束时间

        mcauthfield_playendtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 播放时长秒

        mcauthfield_playduration = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 播放状态如已完成、暂停、中断

        mcauthfield_playstatus = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 设备类型如手机、平板、电脑

        mcauthfield_devicetype = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # IP地址

        mcauthfield_ipaddress = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 播放位置可选根据IP解析的地理位置

        mcauthfield_location = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_videoplayreckwkword.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_videoplayreckwkword().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_videoplayreckwkword.objects.filter(**filter)
        else:
            records = mc_videoplayreckwkword.objects.all()
        # 加载界面中下拉框所需数据

        data_mc_videoinfo_57934 = []
        for m in mc_videoinfo.objects.all():
            mobj = m.toJson()
            data_mc_videoinfo_57934.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("videotitle"),
                }
            )
        data_mc_userinfo_57935 = []
        for m in mc_userinfo.objects.all():
            mobj = m.toJson()
            data_mc_userinfo_57935.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("username"),
                }
            )
        return render(request, "config_busi/videoplayreckwkword.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_videoplayreckwkword()

        # 视频ID关联视频信息

        if mcauthfield_videoid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.videoid = obj.get("videoid")
        # 用户ID关联用户信息

        if mcauthfield_userid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.userid = obj.get("userid")
        # 播放开始时间

        if mcauthfield_playstarttime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.playstarttime = obj.get("playstarttime")
        # 播放结束时间

        if mcauthfield_playendtime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.playendtime = obj.get("playendtime")
        # 播放时长秒

        if mcauthfield_playduration["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.playduration = obj.get("playduration")
        # 播放状态如已完成、暂停、中断

        if mcauthfield_playstatus["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.playstatus = obj.get("playstatus")
        # 设备类型如手机、平板、电脑

        if mcauthfield_devicetype["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.devicetype = obj.get("devicetype")
        # IP地址

        if mcauthfield_ipaddress["mcauthchange"]:

            # TextField # 其他情况/待补充

            ins_table_busi.ipaddress = obj.get("ipaddress")
        # 播放位置可选根据IP解析的地理位置

        if mcauthfield_location["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.location = obj.get("location")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_videoplayreckwkword.objects.get(id=obj.get("_id_upd"))

        # 视频ID关联视频信息

        if mcauthfield_videoid["mcauthchange"]:

            # SelectField

            ins_table_busi.videoid = obj.get("videoid")
        # 用户ID关联用户信息

        if mcauthfield_userid["mcauthchange"]:

            # SelectField

            ins_table_busi.userid = obj.get("userid")
        # 播放开始时间

        if mcauthfield_playstarttime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.playstarttime = obj.get("playstarttime")
        # 播放结束时间

        if mcauthfield_playendtime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.playendtime = obj.get("playendtime")
        # 播放时长秒

        if mcauthfield_playduration["mcauthchange"]:

            # CharField

            ins_table_busi.playduration = obj.get("playduration")
        # 播放状态如已完成、暂停、中断

        if mcauthfield_playstatus["mcauthchange"]:

            # CharField

            ins_table_busi.playstatus = obj.get("playstatus")
        # 设备类型如手机、平板、电脑

        if mcauthfield_devicetype["mcauthchange"]:

            # CharField

            ins_table_busi.devicetype = obj.get("devicetype")
        # IP地址

        if mcauthfield_ipaddress["mcauthchange"]:

            # TextField

            ins_table_busi.ipaddress = obj.get("ipaddress")
        # 播放位置可选根据IP解析的地理位置

        if mcauthfield_location["mcauthchange"]:

            # CharField

            ins_table_busi.location = obj.get("location")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_videoplayreckwkword.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_videoplayreckwkword.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/videoplayreckwkword")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_videocomment(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 视频评论表 系统管理员(8417)

    if user_table_id == str(8417):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 关联视频ID

        mcauthfield_videoid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 关联用户ID

        mcauthfield_userid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 评论内容

        mcauthfield_content = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 创建时间

        mcauthfield_createtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 点赞数

        mcauthfield_likecount = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 回复数

        mcauthfield_replycount = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 是否已删除

        mcauthfield_kwkwiskwkwdeleted = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 关联父评论ID

        mcauthfield_parentid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }
    # 视频评论表 用户信息表(8395)

    if user_table_id == str(8395):
        config_user_table = mc_userinfo
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 关联视频ID

        mcauthfield_videoid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 关联用户ID

        mcauthfield_userid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 评论内容

        mcauthfield_content = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 创建时间

        mcauthfield_createtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 点赞数

        mcauthfield_likecount = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 回复数

        mcauthfield_replycount = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 是否已删除

        mcauthfield_kwkwiskwkwdeleted = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 关联父评论ID

        mcauthfield_parentid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_videocomment.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_videocomment().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_videocomment.objects.filter(**filter)
        else:
            records = mc_videocomment.objects.all()
        # 加载界面中下拉框所需数据

        data_mc_videoinfo_57943 = []
        for m in mc_videoinfo.objects.all():
            mobj = m.toJson()
            data_mc_videoinfo_57943.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("videotitle"),
                }
            )
        data_mc_userinfo_57944 = []
        for m in mc_userinfo.objects.all():
            mobj = m.toJson()
            data_mc_userinfo_57944.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("username"),
                }
            )
        data_mc_videocomment_57950 = []
        for m in mc_videocomment.objects.all():
            mobj = m.toJson()
            data_mc_videocomment_57950.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("content"),
                }
            )
        return render(request, "config_busi/videocomment.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_videocomment()

        # 关联视频ID

        if mcauthfield_videoid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.videoid = obj.get("videoid")
        # 关联用户ID

        if mcauthfield_userid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.userid = obj.get("userid")
        # 评论内容

        if mcauthfield_content["mcauthchange"]:

            # TextField # 其他情况/待补充

            ins_table_busi.content = obj.get("content")
        # 创建时间

        if mcauthfield_createtime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.createtime = obj.get("createtime")
        # 点赞数

        if mcauthfield_likecount["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.likecount = obj.get("likecount")
        # 回复数

        if mcauthfield_replycount["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.replycount = obj.get("replycount")
        # 是否已删除

        if mcauthfield_kwkwiskwkwdeleted["mcauthchange"]:

            # BooleanField # 其他情况/待补充

            ins_table_busi.kwkwiskwkwdeleted = obj.get("kwkwiskwkwdeleted")
        # 关联父评论ID

        if mcauthfield_parentid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.parentid = obj.get("parentid")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_videocomment.objects.get(id=obj.get("_id_upd"))

        # 关联视频ID

        if mcauthfield_videoid["mcauthchange"]:

            # SelectField

            ins_table_busi.videoid = obj.get("videoid")
        # 关联用户ID

        if mcauthfield_userid["mcauthchange"]:

            # SelectField

            ins_table_busi.userid = obj.get("userid")
        # 评论内容

        if mcauthfield_content["mcauthchange"]:

            # TextField

            ins_table_busi.content = obj.get("content")
        # 创建时间

        if mcauthfield_createtime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.createtime = obj.get("createtime")
        # 点赞数

        if mcauthfield_likecount["mcauthchange"]:

            # CharField

            ins_table_busi.likecount = obj.get("likecount")
        # 回复数

        if mcauthfield_replycount["mcauthchange"]:

            # CharField

            ins_table_busi.replycount = obj.get("replycount")
        # 是否已删除

        if mcauthfield_kwkwiskwkwdeleted["mcauthchange"]:

            # BooleanField

            ins_table_busi.kwkwiskwkwdeleted = obj.get("kwkwiskwkwdeleted")
        # 关联父评论ID

        if mcauthfield_parentid["mcauthchange"]:

            # SelectField

            ins_table_busi.parentid = obj.get("parentid")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_videocomment.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_videocomment.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/videocomment")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_videolike(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 视频点赞表 系统管理员(8417)

    if user_table_id == str(8417):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 关联视频ID

        mcauthfield_videoid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 关联用户ID

        mcauthfield_userid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 点赞时间

        mcauthfield_liketime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 是否点赞1为已点赞0为未点赞用于取消点赞功能

        mcauthfield_kwkwisliked = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 点赞时的IP地址

        mcauthfield_ipaddress = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 点赞类型如普通点赞、特殊点赞等可用枚举或示

        mcauthfield_liketype = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 点赞平台如Web、iOS、Android等

        mcauthfield_platkwkwfkwkworm = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 设备ID可选用于追踪用户设备

        mcauthfield_deviceid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }
    # 视频点赞表 用户信息表(8395)

    if user_table_id == str(8395):
        config_user_table = mc_userinfo
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 关联视频ID

        mcauthfield_videoid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 关联用户ID

        mcauthfield_userid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 点赞时间

        mcauthfield_liketime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 是否点赞1为已点赞0为未点赞用于取消点赞功能

        mcauthfield_kwkwisliked = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 点赞时的IP地址

        mcauthfield_ipaddress = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 点赞类型如普通点赞、特殊点赞等可用枚举或示

        mcauthfield_liketype = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 点赞平台如Web、iOS、Android等

        mcauthfield_platkwkwfkwkworm = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 设备ID可选用于追踪用户设备

        mcauthfield_deviceid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_videolike.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_videolike().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_videolike.objects.filter(**filter)
        else:
            records = mc_videolike.objects.all()
        # 加载界面中下拉框所需数据

        data_mc_videoinfo_57951 = []
        for m in mc_videoinfo.objects.all():
            mobj = m.toJson()
            data_mc_videoinfo_57951.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("videotitle"),
                }
            )
        data_mc_userinfo_57952 = []
        for m in mc_userinfo.objects.all():
            mobj = m.toJson()
            data_mc_userinfo_57952.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("username"),
                }
            )
        return render(request, "config_busi/videolike.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_videolike()

        # 关联视频ID

        if mcauthfield_videoid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.videoid = obj.get("videoid")
        # 关联用户ID

        if mcauthfield_userid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.userid = obj.get("userid")
        # 点赞时间

        if mcauthfield_liketime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.liketime = obj.get("liketime")
        # 是否点赞1为已点赞0为未点赞用于取消点赞功能

        if mcauthfield_kwkwisliked["mcauthchange"]:

            # BooleanField # 其他情况/待补充

            ins_table_busi.kwkwisliked = obj.get("kwkwisliked")
        # 点赞时的IP地址

        if mcauthfield_ipaddress["mcauthchange"]:

            # TextField # 其他情况/待补充

            ins_table_busi.ipaddress = obj.get("ipaddress")
        # 点赞类型如普通点赞、特殊点赞等可用枚举或示

        if mcauthfield_liketype["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.liketype = obj.get("liketype")
        # 点赞平台如Web、iOS、Android等

        if mcauthfield_platkwkwfkwkworm["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.platkwkwfkwkworm = obj.get("platkwkwfkwkworm")
        # 设备ID可选用于追踪用户设备

        if mcauthfield_deviceid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.deviceid = str(uuid.uuid4())
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_videolike.objects.get(id=obj.get("_id_upd"))

        # 关联视频ID

        if mcauthfield_videoid["mcauthchange"]:

            # SelectField

            ins_table_busi.videoid = obj.get("videoid")
        # 关联用户ID

        if mcauthfield_userid["mcauthchange"]:

            # SelectField

            ins_table_busi.userid = obj.get("userid")
        # 点赞时间

        if mcauthfield_liketime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.liketime = obj.get("liketime")
        # 是否点赞1为已点赞0为未点赞用于取消点赞功能

        if mcauthfield_kwkwisliked["mcauthchange"]:

            # BooleanField

            ins_table_busi.kwkwisliked = obj.get("kwkwisliked")
        # 点赞时的IP地址

        if mcauthfield_ipaddress["mcauthchange"]:

            # TextField

            ins_table_busi.ipaddress = obj.get("ipaddress")
        # 点赞类型如普通点赞、特殊点赞等可用枚举或示

        if mcauthfield_liketype["mcauthchange"]:

            # CharField

            ins_table_busi.liketype = obj.get("liketype")
        # 点赞平台如Web、iOS、Android等

        if mcauthfield_platkwkwfkwkworm["mcauthchange"]:

            # CharField

            ins_table_busi.platkwkwfkwkworm = obj.get("platkwkwfkwkworm")
        # 设备ID可选用于追踪用户设备

        if mcauthfield_deviceid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.deviceid = str(uuid.uuid4())

            ins_table_busi.deviceid = str(ins_table_busi.deviceid)
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_videolike.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_videolike.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/videolike")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_videoshare(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 视频分享表 系统管理员(8417)

    if user_table_id == str(8417):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 视频分享ID

        mcauthfield_id = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 关联视频ID

        mcauthfield_videoid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 关联用户ID

        mcauthfield_userid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 分享时间

        mcauthfield_sharetime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 视频标题

        mcauthfield_title = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 视频描述

        mcauthfield_description = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 缩略图URL

        mcauthfield_thumbnailurl = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 观看次数

        mcauthfield_viewcount = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 点赞次数

        mcauthfield_likecount = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 评论次数

        mcauthfield_commentcount = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 分享状态例如已分享、已删除

        mcauthfield_sharestatus = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }
    # 视频分享表 用户信息表(8395)

    if user_table_id == str(8395):
        config_user_table = mc_userinfo
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 视频分享ID

        mcauthfield_id = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 关联视频ID

        mcauthfield_videoid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 关联用户ID

        mcauthfield_userid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 分享时间

        mcauthfield_sharetime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 视频标题

        mcauthfield_title = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 视频描述

        mcauthfield_description = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 缩略图URL

        mcauthfield_thumbnailurl = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 观看次数

        mcauthfield_viewcount = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 点赞次数

        mcauthfield_likecount = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 评论次数

        mcauthfield_commentcount = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 分享状态例如已分享、已删除

        mcauthfield_sharestatus = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_videoshare.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_videoshare().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_videoshare.objects.filter(**filter)
        else:
            records = mc_videoshare.objects.all()
        # 加载界面中下拉框所需数据

        data_mc_videoinfo_57960 = []
        for m in mc_videoinfo.objects.all():
            mobj = m.toJson()
            data_mc_videoinfo_57960.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("videotitle"),
                }
            )
        data_mc_userinfo_57961 = []
        for m in mc_userinfo.objects.all():
            mobj = m.toJson()
            data_mc_userinfo_57961.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("username"),
                }
            )
        return render(request, "config_busi/videoshare.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_videoshare()

        # 视频分享ID

        if mcauthfield_id["mcauthchange"]:

            # UUIDField # 其他情况/待补充

            ins_table_busi.id = obj.get("id")
        # 关联视频ID

        if mcauthfield_videoid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.videoid = obj.get("videoid")
        # 关联用户ID

        if mcauthfield_userid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.userid = obj.get("userid")
        # 分享时间

        if mcauthfield_sharetime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.sharetime = obj.get("sharetime")
        # 视频标题

        if mcauthfield_title["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.title = obj.get("title")
        # 视频描述

        if mcauthfield_description["mcauthchange"]:

            # TextField # 其他情况/待补充

            ins_table_busi.description = obj.get("description")
        # 缩略图URL

        if mcauthfield_thumbnailurl["mcauthchange"]:

            # URLField # 其他情况/待补充

            ins_table_busi.thumbnailurl = obj.get("thumbnailurl")
        # 观看次数

        if mcauthfield_viewcount["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.viewcount = obj.get("viewcount")
        # 点赞次数

        if mcauthfield_likecount["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.likecount = obj.get("likecount")
        # 评论次数

        if mcauthfield_commentcount["mcauthchange"]:

            # TextField # 其他情况/待补充

            ins_table_busi.commentcount = obj.get("commentcount")
        # 分享状态例如已分享、已删除

        if mcauthfield_sharestatus["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.sharestatus = obj.get("sharestatus")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_videoshare.objects.get(id=obj.get("_id_upd"))

        # 视频分享ID

        if mcauthfield_id["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.id = str(uuid.uuid4())

            ins_table_busi.id = str(ins_table_busi.id)
        # 关联视频ID

        if mcauthfield_videoid["mcauthchange"]:

            # SelectField

            ins_table_busi.videoid = obj.get("videoid")
        # 关联用户ID

        if mcauthfield_userid["mcauthchange"]:

            # SelectField

            ins_table_busi.userid = obj.get("userid")
        # 分享时间

        if mcauthfield_sharetime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.sharetime = obj.get("sharetime")
        # 视频标题

        if mcauthfield_title["mcauthchange"]:

            # CharField

            ins_table_busi.title = obj.get("title")
        # 视频描述

        if mcauthfield_description["mcauthchange"]:

            # TextField

            ins_table_busi.description = obj.get("description")
        # 缩略图URL

        if mcauthfield_thumbnailurl["mcauthchange"]:

            # URLField

            ins_table_busi.thumbnailurl = obj.get("thumbnailurl")
        # 观看次数

        if mcauthfield_viewcount["mcauthchange"]:

            # CharField

            ins_table_busi.viewcount = obj.get("viewcount")
        # 点赞次数

        if mcauthfield_likecount["mcauthchange"]:

            # CharField

            ins_table_busi.likecount = obj.get("likecount")
        # 评论次数

        if mcauthfield_commentcount["mcauthchange"]:

            # TextField

            ins_table_busi.commentcount = obj.get("commentcount")
        # 分享状态例如已分享、已删除

        if mcauthfield_sharestatus["mcauthchange"]:

            # CharField

            ins_table_busi.sharestatus = obj.get("sharestatus")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_videoshare.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_videoshare.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/videoshare")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_videoviewduration(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 视频观看时长统计表 系统管理员(8417)

    if user_table_id == str(8417):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 关联视频ID

        mcauthfield_videoid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 关联用户ID

        mcauthfield_userid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 观看开始时间

        mcauthfield_viewstarttime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 观看结束时间

        mcauthfield_viewendtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 观看时长秒

        mcauthfield_duration = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 设备类型

        mcauthfield_devicetype = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 观看地点

        mcauthfield_viewlocation = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 网络类型

        mcauthfield_netwkwkworktype = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 是否观看完成0未完成1已完成

        mcauthfield_kwkwiscompleted = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }
    # 视频观看时长统计表 用户信息表(8395)

    if user_table_id == str(8395):
        config_user_table = mc_userinfo
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 关联视频ID

        mcauthfield_videoid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 关联用户ID

        mcauthfield_userid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 观看开始时间

        mcauthfield_viewstarttime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 观看结束时间

        mcauthfield_viewendtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 观看时长秒

        mcauthfield_duration = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 设备类型

        mcauthfield_devicetype = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 观看地点

        mcauthfield_viewlocation = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 网络类型

        mcauthfield_netwkwkworktype = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 是否观看完成0未完成1已完成

        mcauthfield_kwkwiscompleted = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_videoviewduration.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_videoviewduration().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_videoviewduration.objects.filter(**filter)
        else:
            records = mc_videoviewduration.objects.all()
        # 加载界面中下拉框所需数据

        data_mc_videoinfo_57970 = []
        for m in mc_videoinfo.objects.all():
            mobj = m.toJson()
            data_mc_videoinfo_57970.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("videotitle"),
                }
            )
        data_mc_userinfo_57971 = []
        for m in mc_userinfo.objects.all():
            mobj = m.toJson()
            data_mc_userinfo_57971.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("username"),
                }
            )
        return render(request, "config_busi/videoviewduration.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_videoviewduration()

        # 关联视频ID

        if mcauthfield_videoid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.videoid = obj.get("videoid")
        # 关联用户ID

        if mcauthfield_userid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.userid = obj.get("userid")
        # 观看开始时间

        if mcauthfield_viewstarttime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.viewstarttime = obj.get("viewstarttime")
        # 观看结束时间

        if mcauthfield_viewendtime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.viewendtime = obj.get("viewendtime")
        # 观看时长秒

        if mcauthfield_duration["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.duration = obj.get("duration")
        # 设备类型

        if mcauthfield_devicetype["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.devicetype = obj.get("devicetype")
        # 观看地点

        if mcauthfield_viewlocation["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.viewlocation = obj.get("viewlocation")
        # 网络类型

        if mcauthfield_netwkwkworktype["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.netwkwkworktype = obj.get("netwkwkworktype")
        # 是否观看完成0未完成1已完成

        if mcauthfield_kwkwiscompleted["mcauthchange"]:

            # BooleanField # 其他情况/待补充

            ins_table_busi.kwkwiscompleted = obj.get("kwkwiscompleted")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_videoviewduration.objects.get(id=obj.get("_id_upd"))

        # 关联视频ID

        if mcauthfield_videoid["mcauthchange"]:

            # SelectField

            ins_table_busi.videoid = obj.get("videoid")
        # 关联用户ID

        if mcauthfield_userid["mcauthchange"]:

            # SelectField

            ins_table_busi.userid = obj.get("userid")
        # 观看开始时间

        if mcauthfield_viewstarttime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.viewstarttime = obj.get("viewstarttime")
        # 观看结束时间

        if mcauthfield_viewendtime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.viewendtime = obj.get("viewendtime")
        # 观看时长秒

        if mcauthfield_duration["mcauthchange"]:

            # CharField

            ins_table_busi.duration = obj.get("duration")
        # 设备类型

        if mcauthfield_devicetype["mcauthchange"]:

            # CharField

            ins_table_busi.devicetype = obj.get("devicetype")
        # 观看地点

        if mcauthfield_viewlocation["mcauthchange"]:

            # CharField

            ins_table_busi.viewlocation = obj.get("viewlocation")
        # 网络类型

        if mcauthfield_netwkwkworktype["mcauthchange"]:

            # CharField

            ins_table_busi.netwkwkworktype = obj.get("netwkwkworktype")
        # 是否观看完成0未完成1已完成

        if mcauthfield_kwkwiscompleted["mcauthchange"]:

            # BooleanField

            ins_table_busi.kwkwiscompleted = obj.get("kwkwiscompleted")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_videoviewduration.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_videoviewduration.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/videoviewduration")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_videouploader(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 视频上传用户表 系统管理员(8417)

    if user_table_id == str(8417):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 关联用户ID

        mcauthfield_userid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 用户名

        mcauthfield_username = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 电子邮件

        mcauthfield_email = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 电话号码

        mcauthfield_phonenumber = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 上传时间

        mcauthfield_uploadtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 视频ID

        mcauthfield_videoid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 视频标题

        mcauthfield_videotitle = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 视频描述

        mcauthfield_videodescription = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 视频分类ID

        mcauthfield_videocategkwkworyid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 视频状态如审核中、已发布、已删除

        mcauthfield_videostatus = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }
    # 视频上传用户表 用户信息表(8395)

    if user_table_id == str(8395):
        config_user_table = mc_userinfo
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 关联用户ID

        mcauthfield_userid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 用户名

        mcauthfield_username = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 电子邮件

        mcauthfield_email = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 电话号码

        mcauthfield_phonenumber = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 上传时间

        mcauthfield_uploadtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 视频ID

        mcauthfield_videoid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 视频标题

        mcauthfield_videotitle = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 视频描述

        mcauthfield_videodescription = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 视频分类ID

        mcauthfield_videocategkwkworyid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 视频状态如审核中、已发布、已删除

        mcauthfield_videostatus = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_videouploader.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_videouploader().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_videouploader.objects.filter(**filter)
        else:
            records = mc_videouploader.objects.all()
        # 加载界面中下拉框所需数据

        data_mc_userinfo_57979 = []
        for m in mc_userinfo.objects.all():
            mobj = m.toJson()
            data_mc_userinfo_57979.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("username"),
                }
            )
        return render(request, "config_busi/videouploader.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_videouploader()

        # 关联用户ID

        if mcauthfield_userid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.userid = obj.get("userid")
        # 用户名

        if mcauthfield_username["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.username = obj.get("username")
        # 电子邮件

        if mcauthfield_email["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.email = obj.get("email")
        # 电话号码

        if mcauthfield_phonenumber["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.phonenumber = obj.get("phonenumber")
        # 上传时间

        if mcauthfield_uploadtime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.uploadtime = obj.get("uploadtime")
        # 视频ID

        if mcauthfield_videoid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.videoid = str(uuid.uuid4())
        # 视频标题

        if mcauthfield_videotitle["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.videotitle = obj.get("videotitle")
        # 视频描述

        if mcauthfield_videodescription["mcauthchange"]:

            # TextField # 其他情况/待补充

            ins_table_busi.videodescription = obj.get("videodescription")
        # 视频分类ID

        if mcauthfield_videocategkwkworyid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.videocategkwkworyid = str(uuid.uuid4())
        # 视频状态如审核中、已发布、已删除

        if mcauthfield_videostatus["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.videostatus = obj.get("videostatus")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_videouploader.objects.get(id=obj.get("_id_upd"))

        # 关联用户ID

        if mcauthfield_userid["mcauthchange"]:

            # SelectField

            ins_table_busi.userid = obj.get("userid")
        # 用户名

        if mcauthfield_username["mcauthchange"]:

            # CharField

            ins_table_busi.username = obj.get("username")
        # 电子邮件

        if mcauthfield_email["mcauthchange"]:

            # CharField

            ins_table_busi.email = obj.get("email")
        # 电话号码

        if mcauthfield_phonenumber["mcauthchange"]:

            # CharField

            ins_table_busi.phonenumber = obj.get("phonenumber")
        # 上传时间

        if mcauthfield_uploadtime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.uploadtime = obj.get("uploadtime")
        # 视频ID

        if mcauthfield_videoid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.videoid = str(uuid.uuid4())

            ins_table_busi.videoid = str(ins_table_busi.videoid)
        # 视频标题

        if mcauthfield_videotitle["mcauthchange"]:

            # CharField

            ins_table_busi.videotitle = obj.get("videotitle")
        # 视频描述

        if mcauthfield_videodescription["mcauthchange"]:

            # TextField

            ins_table_busi.videodescription = obj.get("videodescription")
        # 视频分类ID

        if mcauthfield_videocategkwkworyid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.videocategkwkworyid = str(uuid.uuid4())

            ins_table_busi.videocategkwkworyid = str(ins_table_busi.videocategkwkworyid)
        # 视频状态如审核中、已发布、已删除

        if mcauthfield_videostatus["mcauthchange"]:

            # CharField

            ins_table_busi.videostatus = obj.get("videostatus")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_videouploader.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_videouploader.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/videouploader")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_userinfo(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 用户信息表 系统管理员(8417)

    if user_table_id == str(8417):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 用户ID

        mcauthfield_userid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 用户名

        mcauthfield_username = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 用户邮箱

        mcauthfield_useremail = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 用户密码

        mcauthfield_userpkwkwasswkwkword = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 电话号码

        mcauthfield_phonenumber = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 性别

        mcauthfield_gender = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 出生日期

        mcauthfield_birthdate = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 注册日期

        mcauthfield_regkwkwisterdate = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 用户角色

        mcauthfield_userrole = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 最后登录时间

        mcauthfield_lkwkwastlogkwkwintime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }
    # 用户信息表 用户信息表(8395)

    if user_table_id == str(8395):
        config_user_table = mc_userinfo
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 用户ID

        mcauthfield_userid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 用户名

        mcauthfield_username = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 用户邮箱

        mcauthfield_useremail = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 用户密码

        mcauthfield_userpkwkwasswkwkword = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 电话号码

        mcauthfield_phonenumber = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 性别

        mcauthfield_gender = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 出生日期

        mcauthfield_birthdate = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 注册日期

        mcauthfield_regkwkwisterdate = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 用户角色

        mcauthfield_userrole = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 最后登录时间

        mcauthfield_lkwkwastlogkwkwintime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_userinfo.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_userinfo().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_userinfo.objects.filter(**filter)
        else:
            records = mc_userinfo.objects.all()
        # 加载界面中下拉框所需数据

        return render(request, "config_busi/userinfo.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_userinfo()

        # 用户ID

        if mcauthfield_userid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.userid = str(uuid.uuid4())
        # 用户名

        if mcauthfield_username["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.username = obj.get("username")
        # 用户邮箱

        if mcauthfield_useremail["mcauthchange"]:

            # EmailField # 其他情况/待补充

            ins_table_busi.useremail = obj.get("useremail")
        # 用户密码

        if mcauthfield_userpkwkwasswkwkword["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.userpkwkwasswkwkword = obj.get("userpkwkwasswkwkword")
        # 电话号码

        if mcauthfield_phonenumber["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.phonenumber = obj.get("phonenumber")
        # 性别

        if mcauthfield_gender["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.gender = obj.get("gender")
        # 出生日期

        if mcauthfield_birthdate["mcauthchange"]:

            # DateField # 其他情况/待补充

            ins_table_busi.birthdate = obj.get("birthdate")
        # 注册日期

        if mcauthfield_regkwkwisterdate["mcauthchange"]:

            # DateField # 其他情况/待补充

            ins_table_busi.regkwkwisterdate = obj.get("regkwkwisterdate")
        # 用户角色

        if mcauthfield_userrole["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.userrole = obj.get("userrole")
        # 最后登录时间

        if mcauthfield_lkwkwastlogkwkwintime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.lkwkwastlogkwkwintime = obj.get("lkwkwastlogkwkwintime")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_userinfo.objects.get(id=obj.get("_id_upd"))

        # 用户ID

        if mcauthfield_userid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.userid = str(uuid.uuid4())

            ins_table_busi.userid = str(ins_table_busi.userid)
        # 用户名

        if mcauthfield_username["mcauthchange"]:

            # CharField

            ins_table_busi.username = obj.get("username")
        # 用户邮箱

        if mcauthfield_useremail["mcauthchange"]:

            # EmailField

            ins_table_busi.useremail = obj.get("useremail")
        # 用户密码

        if mcauthfield_userpkwkwasswkwkword["mcauthchange"]:

            # CharField

            ins_table_busi.userpkwkwasswkwkword = obj.get("userpkwkwasswkwkword")
        # 电话号码

        if mcauthfield_phonenumber["mcauthchange"]:

            # CharField

            ins_table_busi.phonenumber = obj.get("phonenumber")
        # 性别

        if mcauthfield_gender["mcauthchange"]:

            # CharField

            ins_table_busi.gender = obj.get("gender")
        # 出生日期

        if mcauthfield_birthdate["mcauthchange"]:

            # DateField

            ins_table_busi.birthdate = obj.get("birthdate")
        # 注册日期

        if mcauthfield_regkwkwisterdate["mcauthchange"]:

            # DateField

            ins_table_busi.regkwkwisterdate = obj.get("regkwkwisterdate")
        # 用户角色

        if mcauthfield_userrole["mcauthchange"]:

            # CharField

            ins_table_busi.userrole = obj.get("userrole")
        # 最后登录时间

        if mcauthfield_lkwkwastlogkwkwintime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.lkwkwastlogkwkwintime = obj.get("lkwkwastlogkwkwintime")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_userinfo.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_userinfo.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/userinfo")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_userpermkwkwission(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 用户权限表 系统管理员(8417)

    if user_table_id == str(8417):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 关联用户ID

        mcauthfield_userid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 关联权限ID

        mcauthfield_permkwkwissionid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 角色名称

        mcauthfield_rolename = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 权限名称

        mcauthfield_permkwkwissionname = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 创建时间

        mcauthfield_createtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 更新时间

        mcauthfield_updatetime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 是否激活

        mcauthfield_isactive = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 描述

        mcauthfield_description = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }
    # 用户权限表 用户信息表(8395)

    if user_table_id == str(8395):
        config_user_table = mc_userinfo
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 关联用户ID

        mcauthfield_userid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 关联权限ID

        mcauthfield_permkwkwissionid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 角色名称

        mcauthfield_rolename = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 权限名称

        mcauthfield_permkwkwissionname = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 创建时间

        mcauthfield_createtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 更新时间

        mcauthfield_updatetime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 是否激活

        mcauthfield_isactive = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 描述

        mcauthfield_description = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_userpermkwkwission.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_userpermkwkwission().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_userpermkwkwission.objects.filter(**filter)
        else:
            records = mc_userpermkwkwission.objects.all()
        # 加载界面中下拉框所需数据

        data_mc_userinfo_57999 = []
        for m in mc_userinfo.objects.all():
            mobj = m.toJson()
            data_mc_userinfo_57999.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("username"),
                }
            )
        data_mc_userpermkwkwission_58000 = []
        for m in mc_userpermkwkwission.objects.all():
            mobj = m.toJson()
            data_mc_userpermkwkwission_58000.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("permkwkwissionid"),
                }
            )
        return render(request, "config_busi/userpermkwkwission.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_userpermkwkwission()

        # 关联用户ID

        if mcauthfield_userid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.userid = obj.get("userid")
        # 关联权限ID

        if mcauthfield_permkwkwissionid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.permkwkwissionid = obj.get("permkwkwissionid")
        # 角色名称

        if mcauthfield_rolename["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.rolename = obj.get("rolename")
        # 权限名称

        if mcauthfield_permkwkwissionname["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.permkwkwissionname = obj.get("permkwkwissionname")
        # 创建时间

        if mcauthfield_createtime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.createtime = obj.get("createtime")
        # 更新时间

        if mcauthfield_updatetime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.updatetime = obj.get("updatetime")
        # 是否激活

        if mcauthfield_isactive["mcauthchange"]:

            # BooleanField # 其他情况/待补充

            ins_table_busi.isactive = obj.get("isactive")
        # 描述

        if mcauthfield_description["mcauthchange"]:

            # TextField # 其他情况/待补充

            ins_table_busi.description = obj.get("description")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_userpermkwkwission.objects.get(id=obj.get("_id_upd"))

        # 关联用户ID

        if mcauthfield_userid["mcauthchange"]:

            # SelectField

            ins_table_busi.userid = obj.get("userid")
        # 关联权限ID

        if mcauthfield_permkwkwissionid["mcauthchange"]:

            # SelectField

            ins_table_busi.permkwkwissionid = obj.get("permkwkwissionid")
        # 角色名称

        if mcauthfield_rolename["mcauthchange"]:

            # CharField

            ins_table_busi.rolename = obj.get("rolename")
        # 权限名称

        if mcauthfield_permkwkwissionname["mcauthchange"]:

            # CharField

            ins_table_busi.permkwkwissionname = obj.get("permkwkwissionname")
        # 创建时间

        if mcauthfield_createtime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.createtime = obj.get("createtime")
        # 更新时间

        if mcauthfield_updatetime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.updatetime = obj.get("updatetime")
        # 是否激活

        if mcauthfield_isactive["mcauthchange"]:

            # BooleanField

            ins_table_busi.isactive = obj.get("isactive")
        # 描述

        if mcauthfield_description["mcauthchange"]:

            # TextField

            ins_table_busi.description = obj.get("description")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_userpermkwkwission.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_userpermkwkwission.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/userpermkwkwission")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_userwatchhkwkwistkwkwory(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 用户观看历史表 系统管理员(8417)

    if user_table_id == str(8417):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 关联用户ID

        mcauthfield_userid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 关联视频ID

        mcauthfield_videoid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 观看时间

        mcauthfield_watchtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 观看时长

        mcauthfield_watchduration = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 观看状态如已观看、观看中、暂停、已放弃

        mcauthfield_watchstatus = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 评分可选用户对该视频的评分

        mcauthfield_ratkwkwing = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 评论可选用户对该视频的评论

        mcauthfield_comment = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 点赞状态如已点赞、未点赞

        mcauthfield_likestatus = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 分享状态如已分享、未分享

        mcauthfield_sharestatus = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 收藏状态如已收藏、未收藏

        mcauthfield_favkwkworitestatus = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }
    # 用户观看历史表 用户信息表(8395)

    if user_table_id == str(8395):
        config_user_table = mc_userinfo
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 关联用户ID

        mcauthfield_userid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 关联视频ID

        mcauthfield_videoid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 观看时间

        mcauthfield_watchtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 观看时长

        mcauthfield_watchduration = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 观看状态如已观看、观看中、暂停、已放弃

        mcauthfield_watchstatus = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 评分可选用户对该视频的评分

        mcauthfield_ratkwkwing = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 评论可选用户对该视频的评论

        mcauthfield_comment = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 点赞状态如已点赞、未点赞

        mcauthfield_likestatus = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 分享状态如已分享、未分享

        mcauthfield_sharestatus = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 收藏状态如已收藏、未收藏

        mcauthfield_favkwkworitestatus = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_userwatchhkwkwistkwkwory.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_userwatchhkwkwistkwkwory().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_userwatchhkwkwistkwkwory.objects.filter(**filter)
        else:
            records = mc_userwatchhkwkwistkwkwory.objects.all()
        # 加载界面中下拉框所需数据

        data_mc_userinfo_58007 = []
        for m in mc_userinfo.objects.all():
            mobj = m.toJson()
            data_mc_userinfo_58007.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("username"),
                }
            )
        data_mc_videoinfo_58008 = []
        for m in mc_videoinfo.objects.all():
            mobj = m.toJson()
            data_mc_videoinfo_58008.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("videotitle"),
                }
            )
        return render(request, "config_busi/userwatchhkwkwistkwkwory.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_userwatchhkwkwistkwkwory()

        # 关联用户ID

        if mcauthfield_userid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.userid = obj.get("userid")
        # 关联视频ID

        if mcauthfield_videoid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.videoid = obj.get("videoid")
        # 观看时间

        if mcauthfield_watchtime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.watchtime = obj.get("watchtime")
        # 观看时长

        if mcauthfield_watchduration["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.watchduration = obj.get("watchduration")
        # 观看状态如已观看、观看中、暂停、已放弃

        if mcauthfield_watchstatus["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.watchstatus = obj.get("watchstatus")
        # 评分可选用户对该视频的评分

        if mcauthfield_ratkwkwing["mcauthchange"]:

            # IntegerField # 其他情况/待补充

            ins_table_busi.ratkwkwing = obj.get("ratkwkwing")
        # 评论可选用户对该视频的评论

        if mcauthfield_comment["mcauthchange"]:

            # TextField # 其他情况/待补充

            ins_table_busi.comment = obj.get("comment")
        # 点赞状态如已点赞、未点赞

        if mcauthfield_likestatus["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.likestatus = obj.get("likestatus")
        # 分享状态如已分享、未分享

        if mcauthfield_sharestatus["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.sharestatus = obj.get("sharestatus")
        # 收藏状态如已收藏、未收藏

        if mcauthfield_favkwkworitestatus["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.favkwkworitestatus = obj.get("favkwkworitestatus")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_userwatchhkwkwistkwkwory.objects.get(id=obj.get("_id_upd"))

        # 关联用户ID

        if mcauthfield_userid["mcauthchange"]:

            # SelectField

            ins_table_busi.userid = obj.get("userid")
        # 关联视频ID

        if mcauthfield_videoid["mcauthchange"]:

            # SelectField

            ins_table_busi.videoid = obj.get("videoid")
        # 观看时间

        if mcauthfield_watchtime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.watchtime = obj.get("watchtime")
        # 观看时长

        if mcauthfield_watchduration["mcauthchange"]:

            # CharField

            ins_table_busi.watchduration = obj.get("watchduration")
        # 观看状态如已观看、观看中、暂停、已放弃

        if mcauthfield_watchstatus["mcauthchange"]:

            # CharField

            ins_table_busi.watchstatus = obj.get("watchstatus")
        # 评分可选用户对该视频的评分

        if mcauthfield_ratkwkwing["mcauthchange"]:

            # IntegerField

            ins_table_busi.ratkwkwing = obj.get("ratkwkwing")
        # 评论可选用户对该视频的评论

        if mcauthfield_comment["mcauthchange"]:

            # TextField

            ins_table_busi.comment = obj.get("comment")
        # 点赞状态如已点赞、未点赞

        if mcauthfield_likestatus["mcauthchange"]:

            # CharField

            ins_table_busi.likestatus = obj.get("likestatus")
        # 分享状态如已分享、未分享

        if mcauthfield_sharestatus["mcauthchange"]:

            # CharField

            ins_table_busi.sharestatus = obj.get("sharestatus")
        # 收藏状态如已收藏、未收藏

        if mcauthfield_favkwkworitestatus["mcauthchange"]:

            # CharField

            ins_table_busi.favkwkworitestatus = obj.get("favkwkworitestatus")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_userwatchhkwkwistkwkwory.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_userwatchhkwkwistkwkwory.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/userwatchhkwkwistkwkwory")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_videoauditstatus(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 视频审核状态表 系统管理员(8417)

    if user_table_id == str(8417):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 视频ID关联字段指向视频的ID

        mcauthfield_videoid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 审核状态如待审核、审核通过、审核拒绝

        mcauthfield_status = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 审核员ID关联字段指向审核员的ID

        mcauthfield_reviewerid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 审核时间

        mcauthfield_reviewtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 拒绝原因如果状态为审核拒绝则记录拒绝的具体原因

        mcauthfield_rejectrekwkwason = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 审核备注

        mcauthfield_comment = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 是否最终审核标记该审核是否为最终审核结果

        mcauthfield_kwkwisfkwkwinal = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 创建时间

        mcauthfield_createdat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 更新时间

        mcauthfield_updatedat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }
    # 视频审核状态表 用户信息表(8395)

    if user_table_id == str(8395):
        config_user_table = mc_userinfo
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 视频ID关联字段指向视频的ID

        mcauthfield_videoid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 审核状态如待审核、审核通过、审核拒绝

        mcauthfield_status = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 审核员ID关联字段指向审核员的ID

        mcauthfield_reviewerid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 审核时间

        mcauthfield_reviewtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 拒绝原因如果状态为审核拒绝则记录拒绝的具体原因

        mcauthfield_rejectrekwkwason = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 审核备注

        mcauthfield_comment = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 是否最终审核标记该审核是否为最终审核结果

        mcauthfield_kwkwisfkwkwinal = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 创建时间

        mcauthfield_createdat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 更新时间

        mcauthfield_updatedat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_videoauditstatus.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_videoauditstatus().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_videoauditstatus.objects.filter(**filter)
        else:
            records = mc_videoauditstatus.objects.all()
        # 加载界面中下拉框所需数据

        data_mc_videoinfo_58017 = []
        for m in mc_videoinfo.objects.all():
            mobj = m.toJson()
            data_mc_videoinfo_58017.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("videotitle"),
                }
            )
        data_mc_supermanager_58019 = []
        for m in mc_supermanager.objects.all():
            mobj = m.toJson()
            data_mc_supermanager_58019.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("username"),
                }
            )
        return render(request, "config_busi/videoauditstatus.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_videoauditstatus()

        # 视频ID关联字段指向视频的ID

        if mcauthfield_videoid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.videoid = obj.get("videoid")
        # 审核状态如待审核、审核通过、审核拒绝

        if mcauthfield_status["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.status = obj.get("status")
        # 审核员ID关联字段指向审核员的ID

        if mcauthfield_reviewerid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.reviewerid = obj.get("reviewerid")
        # 审核时间

        if mcauthfield_reviewtime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.reviewtime = obj.get("reviewtime")
        # 拒绝原因如果状态为审核拒绝则记录拒绝的具体原因

        if mcauthfield_rejectrekwkwason["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.rejectrekwkwason = obj.get("rejectrekwkwason")
        # 审核备注

        if mcauthfield_comment["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.comment = obj.get("comment")
        # 是否最终审核标记该审核是否为最终审核结果

        if mcauthfield_kwkwisfkwkwinal["mcauthchange"]:

            # BooleanField # 其他情况/待补充

            ins_table_busi.kwkwisfkwkwinal = obj.get("kwkwisfkwkwinal")
        # 创建时间

        if mcauthfield_createdat["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.createdat = obj.get("createdat")
        # 更新时间

        if mcauthfield_updatedat["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.updatedat = obj.get("updatedat")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_videoauditstatus.objects.get(id=obj.get("_id_upd"))

        # 视频ID关联字段指向视频的ID

        if mcauthfield_videoid["mcauthchange"]:

            # SelectField

            ins_table_busi.videoid = obj.get("videoid")
        # 审核状态如待审核、审核通过、审核拒绝

        if mcauthfield_status["mcauthchange"]:

            # CharField

            ins_table_busi.status = obj.get("status")
        # 审核员ID关联字段指向审核员的ID

        if mcauthfield_reviewerid["mcauthchange"]:

            # SelectField

            ins_table_busi.reviewerid = obj.get("reviewerid")
        # 审核时间

        if mcauthfield_reviewtime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.reviewtime = obj.get("reviewtime")
        # 拒绝原因如果状态为审核拒绝则记录拒绝的具体原因

        if mcauthfield_rejectrekwkwason["mcauthchange"]:

            # CharField

            ins_table_busi.rejectrekwkwason = obj.get("rejectrekwkwason")
        # 审核备注

        if mcauthfield_comment["mcauthchange"]:

            # CharField

            ins_table_busi.comment = obj.get("comment")
        # 是否最终审核标记该审核是否为最终审核结果

        if mcauthfield_kwkwisfkwkwinal["mcauthchange"]:

            # BooleanField

            ins_table_busi.kwkwisfkwkwinal = obj.get("kwkwisfkwkwinal")
        # 创建时间

        if mcauthfield_createdat["mcauthchange"]:

            # DateTimeField

            ins_table_busi.createdat = obj.get("createdat")
        # 更新时间

        if mcauthfield_updatedat["mcauthchange"]:

            # DateTimeField

            ins_table_busi.updatedat = obj.get("updatedat")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_videoauditstatus.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_videoauditstatus.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/videoauditstatus")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_videocoverimage(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 视频封面图片表 系统管理员(8417)

    if user_table_id == str(8417):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 视频ID关联字段指向视频的

        mcauthfield_videoid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 封面图片URL

        mcauthfield_coverimageurl = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 图片格式

        mcauthfield_imagekwkwfkwkwormat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 图片大小单位KB

        mcauthfield_imagesize = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 上传时间

        mcauthfield_uploadtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 创建者ID关联字段指向用户的

        mcauthfield_creatkwkworid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 状态例如有效、无效、待审核

        mcauthfield_status = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 图片描述

        mcauthfield_description = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 是否为默认封面kwTruekwFalse

        mcauthfield_kwkwiskwkwdefault = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }
    # 视频封面图片表 用户信息表(8395)

    if user_table_id == str(8395):
        config_user_table = mc_userinfo
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 视频ID关联字段指向视频的

        mcauthfield_videoid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 封面图片URL

        mcauthfield_coverimageurl = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 图片格式

        mcauthfield_imagekwkwfkwkwormat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 图片大小单位KB

        mcauthfield_imagesize = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 上传时间

        mcauthfield_uploadtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 创建者ID关联字段指向用户的

        mcauthfield_creatkwkworid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 状态例如有效、无效、待审核

        mcauthfield_status = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 图片描述

        mcauthfield_description = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 是否为默认封面kwTruekwFalse

        mcauthfield_kwkwiskwkwdefault = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_videocoverimage.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_videocoverimage().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_videocoverimage.objects.filter(**filter)
        else:
            records = mc_videocoverimage.objects.all()
        # 加载界面中下拉框所需数据

        data_mc_videoinfo_58026 = []
        for m in mc_videoinfo.objects.all():
            mobj = m.toJson()
            data_mc_videoinfo_58026.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("videotitle"),
                }
            )
        data_mc_userinfo_58031 = []
        for m in mc_userinfo.objects.all():
            mobj = m.toJson()
            data_mc_userinfo_58031.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("username"),
                }
            )
        return render(request, "config_busi/videocoverimage.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_videocoverimage()

        # 视频ID关联字段指向视频的

        if mcauthfield_videoid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.videoid = obj.get("videoid")
        # 封面图片URL

        if mcauthfield_coverimageurl["mcauthchange"]:

            # Save FileImageField 若上传了文件

            if "coverimageurl" in request.FILES:
                ins_table_busi.coverimageurl = request.FILES["coverimageurl"]
        # 图片格式

        if mcauthfield_imagekwkwfkwkwormat["mcauthchange"]:

            # Save FileImageField 若上传了文件

            if "imagekwkwfkwkwormat" in request.FILES:
                ins_table_busi.imagekwkwfkwkwormat = request.FILES[
                    "imagekwkwfkwkwormat"
                ]
        # 图片大小单位KB

        if mcauthfield_imagesize["mcauthchange"]:

            # Save FileImageField 若上传了文件

            if "imagesize" in request.FILES:
                ins_table_busi.imagesize = request.FILES["imagesize"]
        # 上传时间

        if mcauthfield_uploadtime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.uploadtime = obj.get("uploadtime")
        # 创建者ID关联字段指向用户的

        if mcauthfield_creatkwkworid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.creatkwkworid = obj.get("creatkwkworid")
        # 状态例如有效、无效、待审核

        if mcauthfield_status["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.status = obj.get("status")
        # 图片描述

        if mcauthfield_description["mcauthchange"]:

            # Save FileImageField 若上传了文件

            if "description" in request.FILES:
                ins_table_busi.description = request.FILES["description"]
        # 是否为默认封面kwTruekwFalse

        if mcauthfield_kwkwiskwkwdefault["mcauthchange"]:

            # BooleanField # 其他情况/待补充

            ins_table_busi.kwkwiskwkwdefault = obj.get("kwkwiskwkwdefault")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_videocoverimage.objects.get(id=obj.get("_id_upd"))

        # 视频ID关联字段指向视频的

        if mcauthfield_videoid["mcauthchange"]:

            # SelectField

            ins_table_busi.videoid = obj.get("videoid")
        # 封面图片URL

        if mcauthfield_coverimageurl["mcauthchange"]:

            # Save File ImageField

            if "coverimageurl" in request.FILES:
                ins_table_busi.coverimageurl = request.FILES["coverimageurl"]
        # 图片格式

        if mcauthfield_imagekwkwfkwkwormat["mcauthchange"]:

            # Save File ImageField

            if "imagekwkwfkwkwormat" in request.FILES:
                ins_table_busi.imagekwkwfkwkwormat = request.FILES[
                    "imagekwkwfkwkwormat"
                ]
        # 图片大小单位KB

        if mcauthfield_imagesize["mcauthchange"]:

            # Save File ImageField

            if "imagesize" in request.FILES:
                ins_table_busi.imagesize = request.FILES["imagesize"]
        # 上传时间

        if mcauthfield_uploadtime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.uploadtime = obj.get("uploadtime")
        # 创建者ID关联字段指向用户的

        if mcauthfield_creatkwkworid["mcauthchange"]:

            # SelectField

            ins_table_busi.creatkwkworid = obj.get("creatkwkworid")
        # 状态例如有效、无效、待审核

        if mcauthfield_status["mcauthchange"]:

            # CharField

            ins_table_busi.status = obj.get("status")
        # 图片描述

        if mcauthfield_description["mcauthchange"]:

            # Save File ImageField

            if "description" in request.FILES:
                ins_table_busi.description = request.FILES["description"]
        # 是否为默认封面kwTruekwFalse

        if mcauthfield_kwkwiskwkwdefault["mcauthchange"]:

            # BooleanField

            ins_table_busi.kwkwiskwkwdefault = obj.get("kwkwiskwkwdefault")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_videocoverimage.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_videocoverimage.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/videocoverimage")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_videomatrixconfig(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 视频矩阵配置表 系统管理员(8417)

    if user_table_id == str(8417):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 视频矩阵名称

        mcauthfield_matrixname = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 描述信息

        mcauthfield_description = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 创建时间

        mcauthfield_createdat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 更新时间

        mcauthfield_updatedat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 视频源ID关联视频源

        mcauthfield_videosourceid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 输出通道ID关联输出通道

        mcauthfield_outputchannelid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 布局配置如1x4

        mcauthfield_layoutconfig = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 是否激活用于控制视频矩阵的启用状态

        mcauthfield_kwkwisactive = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }
    # 视频矩阵配置表 用户信息表(8395)

    if user_table_id == str(8395):
        config_user_table = mc_userinfo
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 视频矩阵名称

        mcauthfield_matrixname = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 描述信息

        mcauthfield_description = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 创建时间

        mcauthfield_createdat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 更新时间

        mcauthfield_updatedat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 视频源ID关联视频源

        mcauthfield_videosourceid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 输出通道ID关联输出通道

        mcauthfield_outputchannelid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 布局配置如1x4

        mcauthfield_layoutconfig = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 是否激活用于控制视频矩阵的启用状态

        mcauthfield_kwkwisactive = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_videomatrixconfig.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_videomatrixconfig().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_videomatrixconfig.objects.filter(**filter)
        else:
            records = mc_videomatrixconfig.objects.all()
        # 加载界面中下拉框所需数据

        data_mc_videoinfo_58039 = []
        for m in mc_videoinfo.objects.all():
            mobj = m.toJson()
            data_mc_videoinfo_58039.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("videotitle"),
                }
            )
        data_mc_videofilestkwkworage_58040 = []
        for m in mc_videofilestkwkworage.objects.all():
            mobj = m.toJson()
            data_mc_videofilestkwkworage_58040.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("filename"),
                }
            )
        return render(request, "config_busi/videomatrixconfig.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_videomatrixconfig()

        # 视频矩阵名称

        if mcauthfield_matrixname["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.matrixname = obj.get("matrixname")
        # 描述信息

        if mcauthfield_description["mcauthchange"]:

            # TextField # 其他情况/待补充

            ins_table_busi.description = obj.get("description")
        # 创建时间

        if mcauthfield_createdat["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.createdat = obj.get("createdat")
        # 更新时间

        if mcauthfield_updatedat["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.updatedat = obj.get("updatedat")
        # 视频源ID关联视频源

        if mcauthfield_videosourceid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.videosourceid = obj.get("videosourceid")
        # 输出通道ID关联输出通道

        if mcauthfield_outputchannelid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.outputchannelid = obj.get("outputchannelid")
        # 布局配置如1x4

        if mcauthfield_layoutconfig["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.layoutconfig = obj.get("layoutconfig")
        # 是否激活用于控制视频矩阵的启用状态

        if mcauthfield_kwkwisactive["mcauthchange"]:

            # BooleanField # 其他情况/待补充

            ins_table_busi.kwkwisactive = obj.get("kwkwisactive")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_videomatrixconfig.objects.get(id=obj.get("_id_upd"))

        # 视频矩阵名称

        if mcauthfield_matrixname["mcauthchange"]:

            # CharField

            ins_table_busi.matrixname = obj.get("matrixname")
        # 描述信息

        if mcauthfield_description["mcauthchange"]:

            # TextField

            ins_table_busi.description = obj.get("description")
        # 创建时间

        if mcauthfield_createdat["mcauthchange"]:

            # DateTimeField

            ins_table_busi.createdat = obj.get("createdat")
        # 更新时间

        if mcauthfield_updatedat["mcauthchange"]:

            # DateTimeField

            ins_table_busi.updatedat = obj.get("updatedat")
        # 视频源ID关联视频源

        if mcauthfield_videosourceid["mcauthchange"]:

            # SelectField

            ins_table_busi.videosourceid = obj.get("videosourceid")
        # 输出通道ID关联输出通道

        if mcauthfield_outputchannelid["mcauthchange"]:

            # SelectField

            ins_table_busi.outputchannelid = obj.get("outputchannelid")
        # 布局配置如1x4

        if mcauthfield_layoutconfig["mcauthchange"]:

            # CharField

            ins_table_busi.layoutconfig = obj.get("layoutconfig")
        # 是否激活用于控制视频矩阵的启用状态

        if mcauthfield_kwkwisactive["mcauthchange"]:

            # BooleanField

            ins_table_busi.kwkwisactive = obj.get("kwkwisactive")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_videomatrixconfig.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_videomatrixconfig.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/videomatrixconfig")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_videomatrixnode(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 视频矩阵节点表 系统管理员(8417)

    if user_table_id == str(8417):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 节点名称

        mcauthfield_nodename = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 关联视频源ID

        mcauthfield_videosourceid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 视频格式

        mcauthfield_videokwkwfkwkwormat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 分辨率

        mcauthfield_resolution = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 状态如在线、离线、维护中

        mcauthfield_status = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 创建时间

        mcauthfield_createtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 更新时间

        mcauthfield_updatetime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 关联父节点ID用于示节点之间的层级关系

        mcauthfield_parentnodeid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 描述信息

        mcauthfield_description = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }
    # 视频矩阵节点表 用户信息表(8395)

    if user_table_id == str(8395):
        config_user_table = mc_userinfo
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 节点名称

        mcauthfield_nodename = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 关联视频源ID

        mcauthfield_videosourceid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 视频格式

        mcauthfield_videokwkwfkwkwormat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 分辨率

        mcauthfield_resolution = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 状态如在线、离线、维护中

        mcauthfield_status = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 创建时间

        mcauthfield_createtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 更新时间

        mcauthfield_updatetime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 关联父节点ID用于示节点之间的层级关系

        mcauthfield_parentnodeid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 描述信息

        mcauthfield_description = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_videomatrixnode.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_videomatrixnode().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_videomatrixnode.objects.filter(**filter)
        else:
            records = mc_videomatrixnode.objects.all()
        # 加载界面中下拉框所需数据

        data_mc_videoinfo_58044 = []
        for m in mc_videoinfo.objects.all():
            mobj = m.toJson()
            data_mc_videoinfo_58044.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("videotitle"),
                }
            )
        data_mc_videomatrixnode_58050 = []
        for m in mc_videomatrixnode.objects.all():
            mobj = m.toJson()
            data_mc_videomatrixnode_58050.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("nodename"),
                }
            )
        return render(request, "config_busi/videomatrixnode.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_videomatrixnode()

        # 节点名称

        if mcauthfield_nodename["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.nodename = obj.get("nodename")
        # 关联视频源ID

        if mcauthfield_videosourceid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.videosourceid = obj.get("videosourceid")
        # 视频格式

        if mcauthfield_videokwkwfkwkwormat["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.videokwkwfkwkwormat = obj.get("videokwkwfkwkwormat")
        # 分辨率

        if mcauthfield_resolution["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.resolution = obj.get("resolution")
        # 状态如在线、离线、维护中

        if mcauthfield_status["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.status = obj.get("status")
        # 创建时间

        if mcauthfield_createtime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.createtime = obj.get("createtime")
        # 更新时间

        if mcauthfield_updatetime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.updatetime = obj.get("updatetime")
        # 关联父节点ID用于示节点之间的层级关系

        if mcauthfield_parentnodeid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.parentnodeid = obj.get("parentnodeid")
        # 描述信息

        if mcauthfield_description["mcauthchange"]:

            # TextField # 其他情况/待补充

            ins_table_busi.description = obj.get("description")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_videomatrixnode.objects.get(id=obj.get("_id_upd"))

        # 节点名称

        if mcauthfield_nodename["mcauthchange"]:

            # CharField

            ins_table_busi.nodename = obj.get("nodename")
        # 关联视频源ID

        if mcauthfield_videosourceid["mcauthchange"]:

            # SelectField

            ins_table_busi.videosourceid = obj.get("videosourceid")
        # 视频格式

        if mcauthfield_videokwkwfkwkwormat["mcauthchange"]:

            # CharField

            ins_table_busi.videokwkwfkwkwormat = obj.get("videokwkwfkwkwormat")
        # 分辨率

        if mcauthfield_resolution["mcauthchange"]:

            # CharField

            ins_table_busi.resolution = obj.get("resolution")
        # 状态如在线、离线、维护中

        if mcauthfield_status["mcauthchange"]:

            # CharField

            ins_table_busi.status = obj.get("status")
        # 创建时间

        if mcauthfield_createtime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.createtime = obj.get("createtime")
        # 更新时间

        if mcauthfield_updatetime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.updatetime = obj.get("updatetime")
        # 关联父节点ID用于示节点之间的层级关系

        if mcauthfield_parentnodeid["mcauthchange"]:

            # SelectField

            ins_table_busi.parentnodeid = obj.get("parentnodeid")
        # 描述信息

        if mcauthfield_description["mcauthchange"]:

            # TextField

            ins_table_busi.description = obj.get("description")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_videomatrixnode.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_videomatrixnode.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/videomatrixnode")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_videomatrixplayreckwkword(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 视频矩阵播放记录表 系统管理员(8417)

    if user_table_id == str(8417):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 视频ID关联视频

        mcauthfield_videoid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 矩阵ID关联视频矩阵

        mcauthfield_matrixid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 播放时间

        mcauthfield_playtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 播放时长秒

        mcauthfield_playduration = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 用户ID关联用户

        mcauthfield_userid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 设备ID关联设备

        mcauthfield_deviceid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 播放状态如成功、失败、中断等

        mcauthfield_playstatus = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 播放请求的IP地址

        mcauthfield_ipaddress = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }
    # 视频矩阵播放记录表 用户信息表(8395)

    if user_table_id == str(8395):
        config_user_table = mc_userinfo
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 视频ID关联视频

        mcauthfield_videoid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 矩阵ID关联视频矩阵

        mcauthfield_matrixid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 播放时间

        mcauthfield_playtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 播放时长秒

        mcauthfield_playduration = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 用户ID关联用户

        mcauthfield_userid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 设备ID关联设备

        mcauthfield_deviceid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 播放状态如成功、失败、中断等

        mcauthfield_playstatus = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 播放请求的IP地址

        mcauthfield_ipaddress = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_videomatrixplayreckwkword.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_videomatrixplayreckwkword().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_videomatrixplayreckwkword.objects.filter(**filter)
        else:
            records = mc_videomatrixplayreckwkword.objects.all()
        # 加载界面中下拉框所需数据

        data_mc_videoinfo_58052 = []
        for m in mc_videoinfo.objects.all():
            mobj = m.toJson()
            data_mc_videoinfo_58052.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("videotitle"),
                }
            )
        data_mc_videomatrixconfig_58053 = []
        for m in mc_videomatrixconfig.objects.all():
            mobj = m.toJson()
            data_mc_videomatrixconfig_58053.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("matrixname"),
                }
            )
        data_mc_userinfo_58056 = []
        for m in mc_userinfo.objects.all():
            mobj = m.toJson()
            data_mc_userinfo_58056.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("username"),
                }
            )
        data_mc_videomatrixplayreckwkword_58057 = []
        for m in mc_videomatrixplayreckwkword.objects.all():
            mobj = m.toJson()
            data_mc_videomatrixplayreckwkword_58057.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("deviceid"),
                }
            )
        return render(request, "config_busi/videomatrixplayreckwkword.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_videomatrixplayreckwkword()

        # 视频ID关联视频

        if mcauthfield_videoid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.videoid = obj.get("videoid")
        # 矩阵ID关联视频矩阵

        if mcauthfield_matrixid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.matrixid = obj.get("matrixid")
        # 播放时间

        if mcauthfield_playtime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.playtime = obj.get("playtime")
        # 播放时长秒

        if mcauthfield_playduration["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.playduration = obj.get("playduration")
        # 用户ID关联用户

        if mcauthfield_userid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.userid = obj.get("userid")
        # 设备ID关联设备

        if mcauthfield_deviceid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.deviceid = obj.get("deviceid")
        # 播放状态如成功、失败、中断等

        if mcauthfield_playstatus["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.playstatus = obj.get("playstatus")
        # 播放请求的IP地址

        if mcauthfield_ipaddress["mcauthchange"]:

            # TextField # 其他情况/待补充

            ins_table_busi.ipaddress = obj.get("ipaddress")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_videomatrixplayreckwkword.objects.get(id=obj.get("_id_upd"))

        # 视频ID关联视频

        if mcauthfield_videoid["mcauthchange"]:

            # SelectField

            ins_table_busi.videoid = obj.get("videoid")
        # 矩阵ID关联视频矩阵

        if mcauthfield_matrixid["mcauthchange"]:

            # SelectField

            ins_table_busi.matrixid = obj.get("matrixid")
        # 播放时间

        if mcauthfield_playtime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.playtime = obj.get("playtime")
        # 播放时长秒

        if mcauthfield_playduration["mcauthchange"]:

            # CharField

            ins_table_busi.playduration = obj.get("playduration")
        # 用户ID关联用户

        if mcauthfield_userid["mcauthchange"]:

            # SelectField

            ins_table_busi.userid = obj.get("userid")
        # 设备ID关联设备

        if mcauthfield_deviceid["mcauthchange"]:

            # SelectField

            ins_table_busi.deviceid = obj.get("deviceid")
        # 播放状态如成功、失败、中断等

        if mcauthfield_playstatus["mcauthchange"]:

            # CharField

            ins_table_busi.playstatus = obj.get("playstatus")
        # 播放请求的IP地址

        if mcauthfield_ipaddress["mcauthchange"]:

            # TextField

            ins_table_busi.ipaddress = obj.get("ipaddress")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_videomatrixplayreckwkword.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_videomatrixplayreckwkword.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/videomatrixplayreckwkword")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_videorelatedcontent(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 视频关联内容表 系统管理员(8417)

    if user_table_id == str(8417):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 关联视频ID

        mcauthfield_videoid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 关联内容ID

        mcauthfield_contentid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 内容类型

        mcauthfield_contenttype = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 关联时间

        mcauthfield_relatedtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 描述

        mcauthfield_description = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 状态

        mcauthfield_status = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 关联创建者ID

        mcauthfield_creatkwkworid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 创建时间

        mcauthfield_creationtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 修改时间

        mcauthfield_modkwkwificationtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 视频名称关联字段视频名假设为VideoTable关联字段为视频名称

        mcauthfield_videotablevideoname = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }
    # 视频关联内容表 用户信息表(8395)

    if user_table_id == str(8395):
        config_user_table = mc_userinfo
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 关联视频ID

        mcauthfield_videoid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 关联内容ID

        mcauthfield_contentid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 内容类型

        mcauthfield_contenttype = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 关联时间

        mcauthfield_relatedtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 描述

        mcauthfield_description = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 状态

        mcauthfield_status = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 关联创建者ID

        mcauthfield_creatkwkworid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 创建时间

        mcauthfield_creationtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 修改时间

        mcauthfield_modkwkwificationtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 视频名称关联字段视频名假设为VideoTable关联字段为视频名称

        mcauthfield_videotablevideoname = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_videorelatedcontent.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_videorelatedcontent().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_videorelatedcontent.objects.filter(**filter)
        else:
            records = mc_videorelatedcontent.objects.all()
        # 加载界面中下拉框所需数据

        data_mc_videoinfo_58060 = []
        for m in mc_videoinfo.objects.all():
            mobj = m.toJson()
            data_mc_videoinfo_58060.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("videotitle"),
                }
            )
        data_mc_videocomment_58061 = []
        for m in mc_videocomment.objects.all():
            mobj = m.toJson()
            data_mc_videocomment_58061.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("content"),
                }
            )
        data_mc_videorelatedcontent_58063 = []
        for m in mc_videorelatedcontent.objects.all():
            mobj = m.toJson()
            data_mc_videorelatedcontent_58063.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("relatedtime"),
                }
            )
        data_mc_userinfo_58066 = []
        for m in mc_userinfo.objects.all():
            mobj = m.toJson()
            data_mc_userinfo_58066.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("username"),
                }
            )
        data_mc_videoinfo_58069 = []
        for m in mc_videoinfo.objects.all():
            mobj = m.toJson()
            data_mc_videoinfo_58069.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("videotitle"),
                }
            )
        return render(request, "config_busi/videorelatedcontent.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_videorelatedcontent()

        # 关联视频ID

        if mcauthfield_videoid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.videoid = obj.get("videoid")
        # 关联内容ID

        if mcauthfield_contentid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.contentid = obj.get("contentid")
        # 内容类型

        if mcauthfield_contenttype["mcauthchange"]:

            # TextField # 其他情况/待补充

            ins_table_busi.contenttype = obj.get("contenttype")
        # 关联时间

        if mcauthfield_relatedtime["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.relatedtime = obj.get("relatedtime")
        # 描述

        if mcauthfield_description["mcauthchange"]:

            # TextField # 其他情况/待补充

            ins_table_busi.description = obj.get("description")
        # 状态

        if mcauthfield_status["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.status = obj.get("status")
        # 关联创建者ID

        if mcauthfield_creatkwkworid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.creatkwkworid = obj.get("creatkwkworid")
        # 创建时间

        if mcauthfield_creationtime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.creationtime = obj.get("creationtime")
        # 修改时间

        if mcauthfield_modkwkwificationtime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.modkwkwificationtime = obj.get("modkwkwificationtime")
        # 视频名称关联字段视频名假设为VideoTable关联字段为视频名称

        if mcauthfield_videotablevideoname["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.videotablevideoname = obj.get("videotablevideoname")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_videorelatedcontent.objects.get(id=obj.get("_id_upd"))

        # 关联视频ID

        if mcauthfield_videoid["mcauthchange"]:

            # SelectField

            ins_table_busi.videoid = obj.get("videoid")
        # 关联内容ID

        if mcauthfield_contentid["mcauthchange"]:

            # SelectField

            ins_table_busi.contentid = obj.get("contentid")
        # 内容类型

        if mcauthfield_contenttype["mcauthchange"]:

            # TextField

            ins_table_busi.contenttype = obj.get("contenttype")
        # 关联时间

        if mcauthfield_relatedtime["mcauthchange"]:

            # SelectField

            ins_table_busi.relatedtime = obj.get("relatedtime")
        # 描述

        if mcauthfield_description["mcauthchange"]:

            # TextField

            ins_table_busi.description = obj.get("description")
        # 状态

        if mcauthfield_status["mcauthchange"]:

            # CharField

            ins_table_busi.status = obj.get("status")
        # 关联创建者ID

        if mcauthfield_creatkwkworid["mcauthchange"]:

            # SelectField

            ins_table_busi.creatkwkworid = obj.get("creatkwkworid")
        # 创建时间

        if mcauthfield_creationtime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.creationtime = obj.get("creationtime")
        # 修改时间

        if mcauthfield_modkwkwificationtime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.modkwkwificationtime = obj.get("modkwkwificationtime")
        # 视频名称关联字段视频名假设为VideoTable关联字段为视频名称

        if mcauthfield_videotablevideoname["mcauthchange"]:

            # SelectField

            ins_table_busi.videotablevideoname = obj.get("videotablevideoname")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_videorelatedcontent.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_videorelatedcontent.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/videorelatedcontent")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_videoerrkwkworlog(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 视频错误日志表 系统管理员(8417)

    if user_table_id == str(8417):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 关联视频ID

        mcauthfield_videoid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 错误类型

        mcauthfield_errkwkwortype = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 错误描述

        mcauthfield_errkwkwordescription = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 错误时间

        mcauthfield_errkwkwortime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 是否已解决

        mcauthfield_resolved = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 解决时间

        mcauthfield_resolvedtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 关联解决人

        mcauthfield_resolvedby = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 设备信息

        mcauthfield_devicekwkwinfo = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 客户端IP

        mcauthfield_clientip = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }
    # 视频错误日志表 用户信息表(8395)

    if user_table_id == str(8395):
        config_user_table = mc_userinfo
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 关联视频ID

        mcauthfield_videoid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 错误类型

        mcauthfield_errkwkwortype = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 错误描述

        mcauthfield_errkwkwordescription = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 错误时间

        mcauthfield_errkwkwortime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 是否已解决

        mcauthfield_resolved = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 解决时间

        mcauthfield_resolvedtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 关联解决人

        mcauthfield_resolvedby = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 设备信息

        mcauthfield_devicekwkwinfo = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 客户端IP

        mcauthfield_clientip = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_videoerrkwkworlog.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_videoerrkwkworlog().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_videoerrkwkworlog.objects.filter(**filter)
        else:
            records = mc_videoerrkwkworlog.objects.all()
        # 加载界面中下拉框所需数据

        data_mc_videoinfo_58070 = []
        for m in mc_videoinfo.objects.all():
            mobj = m.toJson()
            data_mc_videoinfo_58070.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("videotitle"),
                }
            )
        data_mc_supermanager_58076 = []
        for m in mc_supermanager.objects.all():
            mobj = m.toJson()
            data_mc_supermanager_58076.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("username"),
                }
            )
        return render(request, "config_busi/videoerrkwkworlog.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_videoerrkwkworlog()

        # 关联视频ID

        if mcauthfield_videoid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.videoid = obj.get("videoid")
        # 错误类型

        if mcauthfield_errkwkwortype["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.errkwkwortype = obj.get("errkwkwortype")
        # 错误描述

        if mcauthfield_errkwkwordescription["mcauthchange"]:

            # TextField # 其他情况/待补充

            ins_table_busi.errkwkwordescription = obj.get("errkwkwordescription")
        # 错误时间

        if mcauthfield_errkwkwortime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.errkwkwortime = obj.get("errkwkwortime")
        # 是否已解决

        if mcauthfield_resolved["mcauthchange"]:

            # BooleanField # 其他情况/待补充

            ins_table_busi.resolved = obj.get("resolved")
        # 解决时间

        if mcauthfield_resolvedtime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.resolvedtime = obj.get("resolvedtime")
        # 关联解决人

        if mcauthfield_resolvedby["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.resolvedby = obj.get("resolvedby")
        # 设备信息

        if mcauthfield_devicekwkwinfo["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.devicekwkwinfo = obj.get("devicekwkwinfo")
        # 客户端IP

        if mcauthfield_clientip["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.clientip = obj.get("clientip")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_videoerrkwkworlog.objects.get(id=obj.get("_id_upd"))

        # 关联视频ID

        if mcauthfield_videoid["mcauthchange"]:

            # SelectField

            ins_table_busi.videoid = obj.get("videoid")
        # 错误类型

        if mcauthfield_errkwkwortype["mcauthchange"]:

            # CharField

            ins_table_busi.errkwkwortype = obj.get("errkwkwortype")
        # 错误描述

        if mcauthfield_errkwkwordescription["mcauthchange"]:

            # TextField

            ins_table_busi.errkwkwordescription = obj.get("errkwkwordescription")
        # 错误时间

        if mcauthfield_errkwkwortime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.errkwkwortime = obj.get("errkwkwortime")
        # 是否已解决

        if mcauthfield_resolved["mcauthchange"]:

            # BooleanField

            ins_table_busi.resolved = obj.get("resolved")
        # 解决时间

        if mcauthfield_resolvedtime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.resolvedtime = obj.get("resolvedtime")
        # 关联解决人

        if mcauthfield_resolvedby["mcauthchange"]:

            # SelectField

            ins_table_busi.resolvedby = obj.get("resolvedby")
        # 设备信息

        if mcauthfield_devicekwkwinfo["mcauthchange"]:

            # CharField

            ins_table_busi.devicekwkwinfo = obj.get("devicekwkwinfo")
        # 客户端IP

        if mcauthfield_clientip["mcauthchange"]:

            # CharField

            ins_table_busi.clientip = obj.get("clientip")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_videoerrkwkworlog.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_videoerrkwkworlog.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/videoerrkwkworlog")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_videopopularity(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 视频热度统计表 系统管理员(8417)

    if user_table_id == str(8417):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 关联视频ID

        mcauthfield_videoid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 观看次数

        mcauthfield_viewcount = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 点赞次数

        mcauthfield_likecount = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 分享次数

        mcauthfield_sharecount = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 评论次数

        mcauthfield_commentcount = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 热度评分

        mcauthfield_popularitysckwkwore = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 发布时间

        mcauthfield_publkwkwishtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 更新时间

        mcauthfield_updatetime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 关联类别ID

        mcauthfield_categkwkworyid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 关联创作者ID

        mcauthfield_creatkwkworid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }
    # 视频热度统计表 用户信息表(8395)

    if user_table_id == str(8395):
        config_user_table = mc_userinfo
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 关联视频ID

        mcauthfield_videoid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 观看次数

        mcauthfield_viewcount = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 点赞次数

        mcauthfield_likecount = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 分享次数

        mcauthfield_sharecount = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 评论次数

        mcauthfield_commentcount = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 热度评分

        mcauthfield_popularitysckwkwore = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 发布时间

        mcauthfield_publkwkwishtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 更新时间

        mcauthfield_updatetime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 关联类别ID

        mcauthfield_categkwkworyid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 关联创作者ID

        mcauthfield_creatkwkworid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_videopopularity.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_videopopularity().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_videopopularity.objects.filter(**filter)
        else:
            records = mc_videopopularity.objects.all()
        # 加载界面中下拉框所需数据

        data_mc_videoinfo_58079 = []
        for m in mc_videoinfo.objects.all():
            mobj = m.toJson()
            data_mc_videoinfo_58079.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("videotitle"),
                }
            )
        data_mc_videocategkwkwory_58087 = []
        for m in mc_videocategkwkwory.objects.all():
            mobj = m.toJson()
            data_mc_videocategkwkwory_58087.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("name"),
                }
            )
        data_mc_userinfo_58088 = []
        for m in mc_userinfo.objects.all():
            mobj = m.toJson()
            data_mc_userinfo_58088.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("username"),
                }
            )
        return render(request, "config_busi/videopopularity.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_videopopularity()

        # 关联视频ID

        if mcauthfield_videoid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.videoid = obj.get("videoid")
        # 观看次数

        if mcauthfield_viewcount["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.viewcount = obj.get("viewcount")
        # 点赞次数

        if mcauthfield_likecount["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.likecount = obj.get("likecount")
        # 分享次数

        if mcauthfield_sharecount["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.sharecount = obj.get("sharecount")
        # 评论次数

        if mcauthfield_commentcount["mcauthchange"]:

            # TextField # 其他情况/待补充

            ins_table_busi.commentcount = obj.get("commentcount")
        # 热度评分

        if mcauthfield_popularitysckwkwore["mcauthchange"]:

            # IntegerField # 其他情况/待补充

            ins_table_busi.popularitysckwkwore = obj.get("popularitysckwkwore")
        # 发布时间

        if mcauthfield_publkwkwishtime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.publkwkwishtime = obj.get("publkwkwishtime")
        # 更新时间

        if mcauthfield_updatetime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.updatetime = obj.get("updatetime")
        # 关联类别ID

        if mcauthfield_categkwkworyid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.categkwkworyid = obj.get("categkwkworyid")
        # 关联创作者ID

        if mcauthfield_creatkwkworid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.creatkwkworid = obj.get("creatkwkworid")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_videopopularity.objects.get(id=obj.get("_id_upd"))

        # 关联视频ID

        if mcauthfield_videoid["mcauthchange"]:

            # SelectField

            ins_table_busi.videoid = obj.get("videoid")
        # 观看次数

        if mcauthfield_viewcount["mcauthchange"]:

            # CharField

            ins_table_busi.viewcount = obj.get("viewcount")
        # 点赞次数

        if mcauthfield_likecount["mcauthchange"]:

            # CharField

            ins_table_busi.likecount = obj.get("likecount")
        # 分享次数

        if mcauthfield_sharecount["mcauthchange"]:

            # CharField

            ins_table_busi.sharecount = obj.get("sharecount")
        # 评论次数

        if mcauthfield_commentcount["mcauthchange"]:

            # TextField

            ins_table_busi.commentcount = obj.get("commentcount")
        # 热度评分

        if mcauthfield_popularitysckwkwore["mcauthchange"]:

            # IntegerField

            ins_table_busi.popularitysckwkwore = obj.get("popularitysckwkwore")
        # 发布时间

        if mcauthfield_publkwkwishtime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.publkwkwishtime = obj.get("publkwkwishtime")
        # 更新时间

        if mcauthfield_updatetime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.updatetime = obj.get("updatetime")
        # 关联类别ID

        if mcauthfield_categkwkworyid["mcauthchange"]:

            # SelectField

            ins_table_busi.categkwkworyid = obj.get("categkwkworyid")
        # 关联创作者ID

        if mcauthfield_creatkwkworid["mcauthchange"]:

            # SelectField

            ins_table_busi.creatkwkworid = obj.get("creatkwkworid")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_videopopularity.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_videopopularity.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/videopopularity")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_videorecommendationparams(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 视频推荐算法参数表 系统管理员(8417)

    if user_table_id == str(8417):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 算法名称

        mcauthfield_algkwkworithmname = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 参数名称

        mcauthfield_paramname = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 参数值

        mcauthfield_paramvalue = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 参数描述

        mcauthfield_description = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 创建时间

        mcauthfield_createdat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 更新时间

        mcauthfield_updatedat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 是否启用

        mcauthfield_kwkwisactive = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 视频类型ID关联字段指向视频类型

        mcauthfield_videotypeid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }
    # 视频推荐算法参数表 用户信息表(8395)

    if user_table_id == str(8395):
        config_user_table = mc_userinfo
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 算法名称

        mcauthfield_algkwkworithmname = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 参数名称

        mcauthfield_paramname = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 参数值

        mcauthfield_paramvalue = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 参数描述

        mcauthfield_description = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 创建时间

        mcauthfield_createdat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 更新时间

        mcauthfield_updatedat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 是否启用

        mcauthfield_kwkwisactive = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 视频类型ID关联字段指向视频类型

        mcauthfield_videotypeid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_videorecommendationparams.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_videorecommendationparams().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_videorecommendationparams.objects.filter(**filter)
        else:
            records = mc_videorecommendationparams.objects.all()
        # 加载界面中下拉框所需数据

        data_mc_videocategkwkwory_58096 = []
        for m in mc_videocategkwkwory.objects.all():
            mobj = m.toJson()
            data_mc_videocategkwkwory_58096.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("name"),
                }
            )
        return render(request, "config_busi/videorecommendationparams.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_videorecommendationparams()

        # 算法名称

        if mcauthfield_algkwkworithmname["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.algkwkworithmname = obj.get("algkwkworithmname")
        # 参数名称

        if mcauthfield_paramname["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.paramname = obj.get("paramname")
        # 参数值

        if mcauthfield_paramvalue["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.paramvalue = obj.get("paramvalue")
        # 参数描述

        if mcauthfield_description["mcauthchange"]:

            # TextField # 其他情况/待补充

            ins_table_busi.description = obj.get("description")
        # 创建时间

        if mcauthfield_createdat["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.createdat = obj.get("createdat")
        # 更新时间

        if mcauthfield_updatedat["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.updatedat = obj.get("updatedat")
        # 是否启用

        if mcauthfield_kwkwisactive["mcauthchange"]:

            # BooleanField # 其他情况/待补充

            ins_table_busi.kwkwisactive = obj.get("kwkwisactive")
        # 视频类型ID关联字段指向视频类型

        if mcauthfield_videotypeid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.videotypeid = obj.get("videotypeid")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_videorecommendationparams.objects.get(id=obj.get("_id_upd"))

        # 算法名称

        if mcauthfield_algkwkworithmname["mcauthchange"]:

            # CharField

            ins_table_busi.algkwkworithmname = obj.get("algkwkworithmname")
        # 参数名称

        if mcauthfield_paramname["mcauthchange"]:

            # CharField

            ins_table_busi.paramname = obj.get("paramname")
        # 参数值

        if mcauthfield_paramvalue["mcauthchange"]:

            # CharField

            ins_table_busi.paramvalue = obj.get("paramvalue")
        # 参数描述

        if mcauthfield_description["mcauthchange"]:

            # TextField

            ins_table_busi.description = obj.get("description")
        # 创建时间

        if mcauthfield_createdat["mcauthchange"]:

            # DateTimeField

            ins_table_busi.createdat = obj.get("createdat")
        # 更新时间

        if mcauthfield_updatedat["mcauthchange"]:

            # DateTimeField

            ins_table_busi.updatedat = obj.get("updatedat")
        # 是否启用

        if mcauthfield_kwkwisactive["mcauthchange"]:

            # BooleanField

            ins_table_busi.kwkwisactive = obj.get("kwkwisactive")
        # 视频类型ID关联字段指向视频类型

        if mcauthfield_videotypeid["mcauthchange"]:

            # SelectField

            ins_table_busi.videotypeid = obj.get("videotypeid")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_videorecommendationparams.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_videorecommendationparams.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/videorecommendationparams")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_videoadinfo(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 视频广告信息表 系统管理员(8417)

    if user_table_id == str(8417):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 视频广告ID

        mcauthfield_videoadid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 广告标题

        mcauthfield_title = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 广告描述

        mcauthfield_description = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 开始时间

        mcauthfield_starttime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 结束时间

        mcauthfield_endtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 视频链接

        mcauthfield_videourl = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 缩略图链接

        mcauthfield_thumbnailurl = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 广告主ID

        mcauthfield_advertkwkwiserid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 广告分类ID

        mcauthfield_categkwkworyid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 广告状态

        mcauthfield_status = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }
    # 视频广告信息表 用户信息表(8395)

    if user_table_id == str(8395):
        config_user_table = mc_userinfo
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 视频广告ID

        mcauthfield_videoadid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 广告标题

        mcauthfield_title = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 广告描述

        mcauthfield_description = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 开始时间

        mcauthfield_starttime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 结束时间

        mcauthfield_endtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 视频链接

        mcauthfield_videourl = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 缩略图链接

        mcauthfield_thumbnailurl = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 广告主ID

        mcauthfield_advertkwkwiserid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 广告分类ID

        mcauthfield_categkwkworyid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 广告状态

        mcauthfield_status = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_videoadinfo.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_videoadinfo().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_videoadinfo.objects.filter(**filter)
        else:
            records = mc_videoadinfo.objects.all()
        # 加载界面中下拉框所需数据

        return render(request, "config_busi/videoadinfo.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_videoadinfo()

        # 视频广告ID

        if mcauthfield_videoadid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.videoadid = str(uuid.uuid4())
        # 广告标题

        if mcauthfield_title["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.title = obj.get("title")
        # 广告描述

        if mcauthfield_description["mcauthchange"]:

            # TextField # 其他情况/待补充

            ins_table_busi.description = obj.get("description")
        # 开始时间

        if mcauthfield_starttime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.starttime = obj.get("starttime")
        # 结束时间

        if mcauthfield_endtime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.endtime = obj.get("endtime")
        # 视频链接

        if mcauthfield_videourl["mcauthchange"]:

            # URLField # 其他情况/待补充

            ins_table_busi.videourl = obj.get("videourl")
        # 缩略图链接

        if mcauthfield_thumbnailurl["mcauthchange"]:

            # URLField # 其他情况/待补充

            ins_table_busi.thumbnailurl = obj.get("thumbnailurl")
        # 广告主ID

        if mcauthfield_advertkwkwiserid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.advertkwkwiserid = str(uuid.uuid4())
        # 广告分类ID

        if mcauthfield_categkwkworyid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.categkwkworyid = str(uuid.uuid4())
        # 广告状态

        if mcauthfield_status["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.status = obj.get("status")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_videoadinfo.objects.get(id=obj.get("_id_upd"))

        # 视频广告ID

        if mcauthfield_videoadid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.videoadid = str(uuid.uuid4())

            ins_table_busi.videoadid = str(ins_table_busi.videoadid)
        # 广告标题

        if mcauthfield_title["mcauthchange"]:

            # CharField

            ins_table_busi.title = obj.get("title")
        # 广告描述

        if mcauthfield_description["mcauthchange"]:

            # TextField

            ins_table_busi.description = obj.get("description")
        # 开始时间

        if mcauthfield_starttime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.starttime = obj.get("starttime")
        # 结束时间

        if mcauthfield_endtime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.endtime = obj.get("endtime")
        # 视频链接

        if mcauthfield_videourl["mcauthchange"]:

            # URLField

            ins_table_busi.videourl = obj.get("videourl")
        # 缩略图链接

        if mcauthfield_thumbnailurl["mcauthchange"]:

            # URLField

            ins_table_busi.thumbnailurl = obj.get("thumbnailurl")
        # 广告主ID

        if mcauthfield_advertkwkwiserid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.advertkwkwiserid = str(uuid.uuid4())

            ins_table_busi.advertkwkwiserid = str(ins_table_busi.advertkwkwiserid)
        # 广告分类ID

        if mcauthfield_categkwkworyid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.categkwkworyid = str(uuid.uuid4())

            ins_table_busi.categkwkworyid = str(ins_table_busi.categkwkworyid)
        # 广告状态

        if mcauthfield_status["mcauthchange"]:

            # CharField

            ins_table_busi.status = obj.get("status")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_videoadinfo.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_videoadinfo.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/videoadinfo")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_videoadplayreckwkword(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 视频广告播放记录表 系统管理员(8417)

    if user_table_id == str(8417):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 视频广告ID

        mcauthfield_videoadid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 播放时间

        mcauthfield_playtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 播放时长

        mcauthfield_playduration = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 用户ID关联用户

        mcauthfield_userid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 设备类型

        mcauthfield_devicetype = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 地址

        mcauthfield_ipaddressip = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 地理位置

        mcauthfield_location = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 播放状态如成功、失败、中断等

        mcauthfield_playstatus = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }
    # 视频广告播放记录表 用户信息表(8395)

    if user_table_id == str(8395):
        config_user_table = mc_userinfo
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 视频广告ID

        mcauthfield_videoadid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 播放时间

        mcauthfield_playtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 播放时长

        mcauthfield_playduration = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 用户ID关联用户

        mcauthfield_userid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 设备类型

        mcauthfield_devicetype = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 地址

        mcauthfield_ipaddressip = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 地理位置

        mcauthfield_location = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 播放状态如成功、失败、中断等

        mcauthfield_playstatus = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_videoadplayreckwkword.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_videoadplayreckwkword().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_videoadplayreckwkword.objects.filter(**filter)
        else:
            records = mc_videoadplayreckwkword.objects.all()
        # 加载界面中下拉框所需数据

        data_mc_userinfo_58110 = []
        for m in mc_userinfo.objects.all():
            mobj = m.toJson()
            data_mc_userinfo_58110.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("username"),
                }
            )
        return render(request, "config_busi/videoadplayreckwkword.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_videoadplayreckwkword()

        # 视频广告ID

        if mcauthfield_videoadid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.videoadid = str(uuid.uuid4())
        # 播放时间

        if mcauthfield_playtime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.playtime = obj.get("playtime")
        # 播放时长

        if mcauthfield_playduration["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.playduration = obj.get("playduration")
        # 用户ID关联用户

        if mcauthfield_userid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.userid = obj.get("userid")
        # 设备类型

        if mcauthfield_devicetype["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.devicetype = obj.get("devicetype")
        # 地址

        if mcauthfield_ipaddressip["mcauthchange"]:

            # TextField # 其他情况/待补充

            ins_table_busi.ipaddressip = obj.get("ipaddressip")
        # 地理位置

        if mcauthfield_location["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.location = obj.get("location")
        # 播放状态如成功、失败、中断等

        if mcauthfield_playstatus["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.playstatus = obj.get("playstatus")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_videoadplayreckwkword.objects.get(id=obj.get("_id_upd"))

        # 视频广告ID

        if mcauthfield_videoadid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.videoadid = str(uuid.uuid4())

            ins_table_busi.videoadid = str(ins_table_busi.videoadid)
        # 播放时间

        if mcauthfield_playtime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.playtime = obj.get("playtime")
        # 播放时长

        if mcauthfield_playduration["mcauthchange"]:

            # CharField

            ins_table_busi.playduration = obj.get("playduration")
        # 用户ID关联用户

        if mcauthfield_userid["mcauthchange"]:

            # SelectField

            ins_table_busi.userid = obj.get("userid")
        # 设备类型

        if mcauthfield_devicetype["mcauthchange"]:

            # CharField

            ins_table_busi.devicetype = obj.get("devicetype")
        # 地址

        if mcauthfield_ipaddressip["mcauthchange"]:

            # TextField

            ins_table_busi.ipaddressip = obj.get("ipaddressip")
        # 地理位置

        if mcauthfield_location["mcauthchange"]:

            # CharField

            ins_table_busi.location = obj.get("location")
        # 播放状态如成功、失败、中断等

        if mcauthfield_playstatus["mcauthchange"]:

            # CharField

            ins_table_busi.playstatus = obj.get("playstatus")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_videoadplayreckwkword.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_videoadplayreckwkword.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/videoadplayreckwkword")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_videodanmu(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 视频弹幕表 系统管理员(8417)

    if user_table_id == str(8417):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 视频唯一标识符关联视频

        mcauthfield_videoid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 弹幕内容

        mcauthfield_danmucontent = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 发送弹幕的用户唯一标识符关联用户

        mcauthfield_userid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 发送时间

        mcauthfield_sendtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 弹幕颜色

        mcauthfield_colkwkwor = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 字体大小

        mcauthfield_fontsize = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 是否可见用于控制弹幕的显示与隐藏

        mcauthfield_kwkwisvkwkwisible = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 弹幕位置如顶部、底部、滚动等

        mcauthfield_position = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 弹幕显示时长秒

        mcauthfield_duration = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }
    # 视频弹幕表 用户信息表(8395)

    if user_table_id == str(8395):
        config_user_table = mc_userinfo
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 视频唯一标识符关联视频

        mcauthfield_videoid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 弹幕内容

        mcauthfield_danmucontent = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 发送弹幕的用户唯一标识符关联用户

        mcauthfield_userid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 发送时间

        mcauthfield_sendtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 弹幕颜色

        mcauthfield_colkwkwor = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 字体大小

        mcauthfield_fontsize = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 是否可见用于控制弹幕的显示与隐藏

        mcauthfield_kwkwisvkwkwisible = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 弹幕位置如顶部、底部、滚动等

        mcauthfield_position = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 弹幕显示时长秒

        mcauthfield_duration = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_videodanmu.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_videodanmu().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_videodanmu.objects.filter(**filter)
        else:
            records = mc_videodanmu.objects.all()
        # 加载界面中下拉框所需数据

        return render(request, "config_busi/videodanmu.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_videodanmu()

        # 视频唯一标识符关联视频

        if mcauthfield_videoid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.videoid = str(uuid.uuid4())
        # 弹幕内容

        if mcauthfield_danmucontent["mcauthchange"]:

            # TextField # 其他情况/待补充

            ins_table_busi.danmucontent = obj.get("danmucontent")
        # 发送弹幕的用户唯一标识符关联用户

        if mcauthfield_userid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.userid = str(uuid.uuid4())
        # 发送时间

        if mcauthfield_sendtime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.sendtime = obj.get("sendtime")
        # 弹幕颜色

        if mcauthfield_colkwkwor["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.colkwkwor = obj.get("colkwkwor")
        # 字体大小

        if mcauthfield_fontsize["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.fontsize = obj.get("fontsize")
        # 是否可见用于控制弹幕的显示与隐藏

        if mcauthfield_kwkwisvkwkwisible["mcauthchange"]:

            # BooleanField # 其他情况/待补充

            ins_table_busi.kwkwisvkwkwisible = obj.get("kwkwisvkwkwisible")
        # 弹幕位置如顶部、底部、滚动等

        if mcauthfield_position["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.position = obj.get("position")
        # 弹幕显示时长秒

        if mcauthfield_duration["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.duration = obj.get("duration")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_videodanmu.objects.get(id=obj.get("_id_upd"))

        # 视频唯一标识符关联视频

        if mcauthfield_videoid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.videoid = str(uuid.uuid4())

            ins_table_busi.videoid = str(ins_table_busi.videoid)
        # 弹幕内容

        if mcauthfield_danmucontent["mcauthchange"]:

            # TextField

            ins_table_busi.danmucontent = obj.get("danmucontent")
        # 发送弹幕的用户唯一标识符关联用户

        if mcauthfield_userid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.userid = str(uuid.uuid4())

            ins_table_busi.userid = str(ins_table_busi.userid)
        # 发送时间

        if mcauthfield_sendtime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.sendtime = obj.get("sendtime")
        # 弹幕颜色

        if mcauthfield_colkwkwor["mcauthchange"]:

            # CharField

            ins_table_busi.colkwkwor = obj.get("colkwkwor")
        # 字体大小

        if mcauthfield_fontsize["mcauthchange"]:

            # CharField

            ins_table_busi.fontsize = obj.get("fontsize")
        # 是否可见用于控制弹幕的显示与隐藏

        if mcauthfield_kwkwisvkwkwisible["mcauthchange"]:

            # BooleanField

            ins_table_busi.kwkwisvkwkwisible = obj.get("kwkwisvkwkwisible")
        # 弹幕位置如顶部、底部、滚动等

        if mcauthfield_position["mcauthchange"]:

            # CharField

            ins_table_busi.position = obj.get("position")
        # 弹幕显示时长秒

        if mcauthfield_duration["mcauthchange"]:

            # CharField

            ins_table_busi.duration = obj.get("duration")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_videodanmu.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_videodanmu.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/videodanmu")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_videodanmublockwkwkwords(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 视频弹幕屏蔽词表 系统管理员(8417)

    if user_table_id == str(8417):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 屏蔽词

        mcauthfield_wkwkword = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 视频ID关联字段指向视频的ID

        mcauthfield_videoid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 创建者ID关联字段指向用户的ID

        mcauthfield_creatkwkworid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 创建时间

        mcauthfield_createtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 更新时间

        mcauthfield_updatetime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 是否激活用于控制屏蔽词是否生效

        mcauthfield_kwkwisactive = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 屏蔽类型如关键词、正则达式等

        mcauthfield_blocktype = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 描述对屏蔽词的额外说明或备注

        mcauthfield_description = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }
    # 视频弹幕屏蔽词表 用户信息表(8395)

    if user_table_id == str(8395):
        config_user_table = mc_userinfo
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 屏蔽词

        mcauthfield_wkwkword = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 视频ID关联字段指向视频的ID

        mcauthfield_videoid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 创建者ID关联字段指向用户的ID

        mcauthfield_creatkwkworid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 创建时间

        mcauthfield_createtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 更新时间

        mcauthfield_updatetime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 是否激活用于控制屏蔽词是否生效

        mcauthfield_kwkwisactive = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 屏蔽类型如关键词、正则达式等

        mcauthfield_blocktype = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 描述对屏蔽词的额外说明或备注

        mcauthfield_description = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_videodanmublockwkwkwords.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_videodanmublockwkwkwords().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_videodanmublockwkwkwords.objects.filter(**filter)
        else:
            records = mc_videodanmublockwkwkwords.objects.all()
        # 加载界面中下拉框所需数据

        data_mc_videoinfo_58125 = []
        for m in mc_videoinfo.objects.all():
            mobj = m.toJson()
            data_mc_videoinfo_58125.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("videotitle"),
                }
            )
        data_mc_userinfo_58126 = []
        for m in mc_userinfo.objects.all():
            mobj = m.toJson()
            data_mc_userinfo_58126.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("username"),
                }
            )
        return render(request, "config_busi/videodanmublockwkwkwords.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_videodanmublockwkwkwords()

        # 屏蔽词

        if mcauthfield_wkwkword["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.wkwkword = obj.get("wkwkword")
        # 视频ID关联字段指向视频的ID

        if mcauthfield_videoid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.videoid = obj.get("videoid")
        # 创建者ID关联字段指向用户的ID

        if mcauthfield_creatkwkworid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.creatkwkworid = obj.get("creatkwkworid")
        # 创建时间

        if mcauthfield_createtime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.createtime = obj.get("createtime")
        # 更新时间

        if mcauthfield_updatetime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.updatetime = obj.get("updatetime")
        # 是否激活用于控制屏蔽词是否生效

        if mcauthfield_kwkwisactive["mcauthchange"]:

            # BooleanField # 其他情况/待补充

            ins_table_busi.kwkwisactive = obj.get("kwkwisactive")
        # 屏蔽类型如关键词、正则达式等

        if mcauthfield_blocktype["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.blocktype = obj.get("blocktype")
        # 描述对屏蔽词的额外说明或备注

        if mcauthfield_description["mcauthchange"]:

            # TextField # 其他情况/待补充

            ins_table_busi.description = obj.get("description")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_videodanmublockwkwkwords.objects.get(id=obj.get("_id_upd"))

        # 屏蔽词

        if mcauthfield_wkwkword["mcauthchange"]:

            # CharField

            ins_table_busi.wkwkword = obj.get("wkwkword")
        # 视频ID关联字段指向视频的ID

        if mcauthfield_videoid["mcauthchange"]:

            # SelectField

            ins_table_busi.videoid = obj.get("videoid")
        # 创建者ID关联字段指向用户的ID

        if mcauthfield_creatkwkworid["mcauthchange"]:

            # SelectField

            ins_table_busi.creatkwkworid = obj.get("creatkwkworid")
        # 创建时间

        if mcauthfield_createtime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.createtime = obj.get("createtime")
        # 更新时间

        if mcauthfield_updatetime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.updatetime = obj.get("updatetime")
        # 是否激活用于控制屏蔽词是否生效

        if mcauthfield_kwkwisactive["mcauthchange"]:

            # BooleanField

            ins_table_busi.kwkwisactive = obj.get("kwkwisactive")
        # 屏蔽类型如关键词、正则达式等

        if mcauthfield_blocktype["mcauthchange"]:

            # CharField

            ins_table_busi.blocktype = obj.get("blocktype")
        # 描述对屏蔽词的额外说明或备注

        if mcauthfield_description["mcauthchange"]:

            # TextField

            ins_table_busi.description = obj.get("description")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_videodanmublockwkwkwords.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_videodanmublockwkwkwords.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/videodanmublockwkwkwords")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_videomultilkwkwingualsubtitles(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 视频多语言字幕表 系统管理员(8417)

    if user_table_id == str(8417):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 关联视频ID

        mcauthfield_videoid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 语言代码

        mcauthfield_languagecode = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 字幕文本

        mcauthfield_subtitletext = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 开始时间字幕出现时间

        mcauthfield_starttime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 结束时间字幕消失时间

        mcauthfield_endtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 创建时间

        mcauthfield_createdat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 更新时间

        mcauthfield_updatedat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 是否激活用于控制字幕是否显示在视频中

        mcauthfield_kwkwisactive = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 创建者用户ID关联到用户示谁添加了这条字幕

        mcauthfield_userid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }
    # 视频多语言字幕表 用户信息表(8395)

    if user_table_id == str(8395):
        config_user_table = mc_userinfo
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 关联视频ID

        mcauthfield_videoid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 语言代码

        mcauthfield_languagecode = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 字幕文本

        mcauthfield_subtitletext = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 开始时间字幕出现时间

        mcauthfield_starttime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 结束时间字幕消失时间

        mcauthfield_endtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 创建时间

        mcauthfield_createdat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 更新时间

        mcauthfield_updatedat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 是否激活用于控制字幕是否显示在视频中

        mcauthfield_kwkwisactive = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 创建者用户ID关联到用户示谁添加了这条字幕

        mcauthfield_userid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_videomultilkwkwingualsubtitles.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_videomultilkwkwingualsubtitles().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_videomultilkwkwingualsubtitles.objects.filter(**filter)
        else:
            records = mc_videomultilkwkwingualsubtitles.objects.all()
        # 加载界面中下拉框所需数据

        data_mc_videoinfo_58132 = []
        for m in mc_videoinfo.objects.all():
            mobj = m.toJson()
            data_mc_videoinfo_58132.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("videotitle"),
                }
            )
        data_mc_userinfo_58140 = []
        for m in mc_userinfo.objects.all():
            mobj = m.toJson()
            data_mc_userinfo_58140.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("username"),
                }
            )
        return render(
            request, "config_busi/videomultilkwkwingualsubtitles.html", locals()
        )
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_videomultilkwkwingualsubtitles()

        # 关联视频ID

        if mcauthfield_videoid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.videoid = obj.get("videoid")
        # 语言代码

        if mcauthfield_languagecode["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.languagecode = obj.get("languagecode")
        # 字幕文本

        if mcauthfield_subtitletext["mcauthchange"]:

            # TextField # 其他情况/待补充

            ins_table_busi.subtitletext = obj.get("subtitletext")
        # 开始时间字幕出现时间

        if mcauthfield_starttime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.starttime = obj.get("starttime")
        # 结束时间字幕消失时间

        if mcauthfield_endtime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.endtime = obj.get("endtime")
        # 创建时间

        if mcauthfield_createdat["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.createdat = obj.get("createdat")
        # 更新时间

        if mcauthfield_updatedat["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.updatedat = obj.get("updatedat")
        # 是否激活用于控制字幕是否显示在视频中

        if mcauthfield_kwkwisactive["mcauthchange"]:

            # BooleanField # 其他情况/待补充

            ins_table_busi.kwkwisactive = obj.get("kwkwisactive")
        # 创建者用户ID关联到用户示谁添加了这条字幕

        if mcauthfield_userid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.userid = obj.get("userid")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_videomultilkwkwingualsubtitles.objects.get(
            id=obj.get("_id_upd")
        )

        # 关联视频ID

        if mcauthfield_videoid["mcauthchange"]:

            # SelectField

            ins_table_busi.videoid = obj.get("videoid")
        # 语言代码

        if mcauthfield_languagecode["mcauthchange"]:

            # CharField

            ins_table_busi.languagecode = obj.get("languagecode")
        # 字幕文本

        if mcauthfield_subtitletext["mcauthchange"]:

            # TextField

            ins_table_busi.subtitletext = obj.get("subtitletext")
        # 开始时间字幕出现时间

        if mcauthfield_starttime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.starttime = obj.get("starttime")
        # 结束时间字幕消失时间

        if mcauthfield_endtime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.endtime = obj.get("endtime")
        # 创建时间

        if mcauthfield_createdat["mcauthchange"]:

            # DateTimeField

            ins_table_busi.createdat = obj.get("createdat")
        # 更新时间

        if mcauthfield_updatedat["mcauthchange"]:

            # DateTimeField

            ins_table_busi.updatedat = obj.get("updatedat")
        # 是否激活用于控制字幕是否显示在视频中

        if mcauthfield_kwkwisactive["mcauthchange"]:

            # BooleanField

            ins_table_busi.kwkwisactive = obj.get("kwkwisactive")
        # 创建者用户ID关联到用户示谁添加了这条字幕

        if mcauthfield_userid["mcauthchange"]:

            # SelectField

            ins_table_busi.userid = obj.get("userid")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_videomultilkwkwingualsubtitles.objects.get(
            id=obj.get("_id")
        )
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_videomultilkwkwingualsubtitles.objects.get(
            id=obj.get("_id")
        )
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/videomultilkwkwingualsubtitles")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_videotranscodkwkwingtkwkwask(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 视频转码任务表 系统管理员(8417)

    if user_table_id == str(8417):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 任务ID

        mcauthfield_tkwkwaskid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 关联视频ID

        mcauthfield_videoid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 源视频路径

        mcauthfield_sourcepath = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 目标格式

        mcauthfield_targetkwkwfkwkwormat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 任务状态

        mcauthfield_status = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 任务进度

        mcauthfield_progress = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 创建时间

        mcauthfield_createdat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 更新时间

        mcauthfield_updatedat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 关联用户ID

        mcauthfield_userid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 任务优先级

        mcauthfield_prikwkwority = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }
    # 视频转码任务表 用户信息表(8395)

    if user_table_id == str(8395):
        config_user_table = mc_userinfo
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 任务ID

        mcauthfield_tkwkwaskid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 关联视频ID

        mcauthfield_videoid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 源视频路径

        mcauthfield_sourcepath = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 目标格式

        mcauthfield_targetkwkwfkwkwormat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 任务状态

        mcauthfield_status = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 任务进度

        mcauthfield_progress = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 创建时间

        mcauthfield_createdat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 更新时间

        mcauthfield_updatedat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 关联用户ID

        mcauthfield_userid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 任务优先级

        mcauthfield_prikwkwority = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_videotranscodkwkwingtkwkwask.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_videotranscodkwkwingtkwkwask().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_videotranscodkwkwingtkwkwask.objects.filter(**filter)
        else:
            records = mc_videotranscodkwkwingtkwkwask.objects.all()
        # 加载界面中下拉框所需数据

        data_mc_videoinfo_58142 = []
        for m in mc_videoinfo.objects.all():
            mobj = m.toJson()
            data_mc_videoinfo_58142.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("videotitle"),
                }
            )
        data_mc_userinfo_58149 = []
        for m in mc_userinfo.objects.all():
            mobj = m.toJson()
            data_mc_userinfo_58149.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("username"),
                }
            )
        return render(
            request, "config_busi/videotranscodkwkwingtkwkwask.html", locals()
        )
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_videotranscodkwkwingtkwkwask()

        # 任务ID

        if mcauthfield_tkwkwaskid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.tkwkwaskid = str(uuid.uuid4())
        # 关联视频ID

        if mcauthfield_videoid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.videoid = obj.get("videoid")
        # 源视频路径

        if mcauthfield_sourcepath["mcauthchange"]:

            # Save FileFileField 若上传了文件

            if "sourcepath" in request.FILES:
                ins_table_busi.sourcepath = request.FILES["sourcepath"]
        # 目标格式

        if mcauthfield_targetkwkwfkwkwormat["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.targetkwkwfkwkwormat = obj.get("targetkwkwfkwkwormat")
        # 任务状态

        if mcauthfield_status["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.status = obj.get("status")
        # 任务进度

        if mcauthfield_progress["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.progress = obj.get("progress")
        # 创建时间

        if mcauthfield_createdat["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.createdat = obj.get("createdat")
        # 更新时间

        if mcauthfield_updatedat["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.updatedat = obj.get("updatedat")
        # 关联用户ID

        if mcauthfield_userid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.userid = obj.get("userid")
        # 任务优先级

        if mcauthfield_prikwkwority["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.prikwkwority = obj.get("prikwkwority")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_videotranscodkwkwingtkwkwask.objects.get(
            id=obj.get("_id_upd")
        )

        # 任务ID

        if mcauthfield_tkwkwaskid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.tkwkwaskid = str(uuid.uuid4())

            ins_table_busi.tkwkwaskid = str(ins_table_busi.tkwkwaskid)
        # 关联视频ID

        if mcauthfield_videoid["mcauthchange"]:

            # SelectField

            ins_table_busi.videoid = obj.get("videoid")
        # 源视频路径

        if mcauthfield_sourcepath["mcauthchange"]:

            # Save File FileField

            if "sourcepath" in request.FILES:
                ins_table_busi.sourcepath = request.FILES["sourcepath"]
        # 目标格式

        if mcauthfield_targetkwkwfkwkwormat["mcauthchange"]:

            # CharField

            ins_table_busi.targetkwkwfkwkwormat = obj.get("targetkwkwfkwkwormat")
        # 任务状态

        if mcauthfield_status["mcauthchange"]:

            # CharField

            ins_table_busi.status = obj.get("status")
        # 任务进度

        if mcauthfield_progress["mcauthchange"]:

            # CharField

            ins_table_busi.progress = obj.get("progress")
        # 创建时间

        if mcauthfield_createdat["mcauthchange"]:

            # DateTimeField

            ins_table_busi.createdat = obj.get("createdat")
        # 更新时间

        if mcauthfield_updatedat["mcauthchange"]:

            # DateTimeField

            ins_table_busi.updatedat = obj.get("updatedat")
        # 关联用户ID

        if mcauthfield_userid["mcauthchange"]:

            # SelectField

            ins_table_busi.userid = obj.get("userid")
        # 任务优先级

        if mcauthfield_prikwkwority["mcauthchange"]:

            # CharField

            ins_table_busi.prikwkwority = obj.get("prikwkwority")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_videotranscodkwkwingtkwkwask.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_videotranscodkwkwingtkwkwask.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/videotranscodkwkwingtkwkwask")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_videoanalyskwkwismetrics(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 视频分析指标表 系统管理员(8417)

    if user_table_id == str(8417):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 视频ID关联视频

        mcauthfield_videoid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 分析时间

        mcauthfield_analyskwkwistime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 观看次数

        mcauthfield_viewcount = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 点赞次数

        mcauthfield_likecount = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 分享次数

        mcauthfield_sharecount = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 评论次数

        mcauthfield_commentcount = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 跳出率

        mcauthfield_bouncerate = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 平均观看时长

        mcauthfield_averagewatchtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 互动率

        mcauthfield_engagementrate = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }
    # 视频分析指标表 用户信息表(8395)

    if user_table_id == str(8395):
        config_user_table = mc_userinfo
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 视频ID关联视频

        mcauthfield_videoid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 分析时间

        mcauthfield_analyskwkwistime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 观看次数

        mcauthfield_viewcount = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 点赞次数

        mcauthfield_likecount = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 分享次数

        mcauthfield_sharecount = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 评论次数

        mcauthfield_commentcount = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 跳出率

        mcauthfield_bouncerate = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 平均观看时长

        mcauthfield_averagewatchtime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 互动率

        mcauthfield_engagementrate = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_videoanalyskwkwismetrics.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_videoanalyskwkwismetrics().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_videoanalyskwkwismetrics.objects.filter(**filter)
        else:
            records = mc_videoanalyskwkwismetrics.objects.all()
        # 加载界面中下拉框所需数据

        data_mc_videoinfo_58151 = []
        for m in mc_videoinfo.objects.all():
            mobj = m.toJson()
            data_mc_videoinfo_58151.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("videotitle"),
                }
            )
        return render(request, "config_busi/videoanalyskwkwismetrics.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_videoanalyskwkwismetrics()

        # 视频ID关联视频

        if mcauthfield_videoid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.videoid = obj.get("videoid")
        # 分析时间

        if mcauthfield_analyskwkwistime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.analyskwkwistime = obj.get("analyskwkwistime")
        # 观看次数

        if mcauthfield_viewcount["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.viewcount = obj.get("viewcount")
        # 点赞次数

        if mcauthfield_likecount["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.likecount = obj.get("likecount")
        # 分享次数

        if mcauthfield_sharecount["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.sharecount = obj.get("sharecount")
        # 评论次数

        if mcauthfield_commentcount["mcauthchange"]:

            # TextField # 其他情况/待补充

            ins_table_busi.commentcount = obj.get("commentcount")
        # 跳出率

        if mcauthfield_bouncerate["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.bouncerate = obj.get("bouncerate")
        # 平均观看时长

        if mcauthfield_averagewatchtime["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.averagewatchtime = obj.get("averagewatchtime")
        # 互动率

        if mcauthfield_engagementrate["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.engagementrate = obj.get("engagementrate")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_videoanalyskwkwismetrics.objects.get(id=obj.get("_id_upd"))

        # 视频ID关联视频

        if mcauthfield_videoid["mcauthchange"]:

            # SelectField

            ins_table_busi.videoid = obj.get("videoid")
        # 分析时间

        if mcauthfield_analyskwkwistime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.analyskwkwistime = obj.get("analyskwkwistime")
        # 观看次数

        if mcauthfield_viewcount["mcauthchange"]:

            # CharField

            ins_table_busi.viewcount = obj.get("viewcount")
        # 点赞次数

        if mcauthfield_likecount["mcauthchange"]:

            # CharField

            ins_table_busi.likecount = obj.get("likecount")
        # 分享次数

        if mcauthfield_sharecount["mcauthchange"]:

            # CharField

            ins_table_busi.sharecount = obj.get("sharecount")
        # 评论次数

        if mcauthfield_commentcount["mcauthchange"]:

            # TextField

            ins_table_busi.commentcount = obj.get("commentcount")
        # 跳出率

        if mcauthfield_bouncerate["mcauthchange"]:

            # CharField

            ins_table_busi.bouncerate = obj.get("bouncerate")
        # 平均观看时长

        if mcauthfield_averagewatchtime["mcauthchange"]:

            # CharField

            ins_table_busi.averagewatchtime = obj.get("averagewatchtime")
        # 互动率

        if mcauthfield_engagementrate["mcauthchange"]:

            # CharField

            ins_table_busi.engagementrate = obj.get("engagementrate")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_videoanalyskwkwismetrics.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_videoanalyskwkwismetrics.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/videoanalyskwkwismetrics")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_videoqualityassessment(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 视频质量评估表 系统管理员(8417)

    if user_table_id == str(8417):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 关联视频ID

        mcauthfield_videoid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 质量评分

        mcauthfield_qualitysckwkwore = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 评估时间

        mcauthfield_kwkwassessmenttime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 关联评审员ID

        mcauthfield_reviewerid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 帧率

        mcauthfield_framerate = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 分辨率

        mcauthfield_resolution = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 比特率

        mcauthfield_bitrate = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 编码格式

        mcauthfield_encodkwkwingkwkwfkwkwormat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 是否检测到损坏

        mcauthfield_ckwkworruptiondetected = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 相关问题ID

        mcauthfield_relatedkwkwissueid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }
    # 视频质量评估表 用户信息表(8395)

    if user_table_id == str(8395):
        config_user_table = mc_userinfo
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 关联视频ID

        mcauthfield_videoid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 质量评分

        mcauthfield_qualitysckwkwore = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 评估时间

        mcauthfield_kwkwassessmenttime = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 关联评审员ID

        mcauthfield_reviewerid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 帧率

        mcauthfield_framerate = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 分辨率

        mcauthfield_resolution = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 比特率

        mcauthfield_bitrate = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 编码格式

        mcauthfield_encodkwkwingkwkwfkwkwormat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 是否检测到损坏

        mcauthfield_ckwkworruptiondetected = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 相关问题ID

        mcauthfield_relatedkwkwissueid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_videoqualityassessment.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_videoqualityassessment().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_videoqualityassessment.objects.filter(**filter)
        else:
            records = mc_videoqualityassessment.objects.all()
        # 加载界面中下拉框所需数据

        data_mc_videoinfo_58160 = []
        for m in mc_videoinfo.objects.all():
            mobj = m.toJson()
            data_mc_videoinfo_58160.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("videotitle"),
                }
            )
        data_mc_supermanager_58163 = []
        for m in mc_supermanager.objects.all():
            mobj = m.toJson()
            data_mc_supermanager_58163.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("username"),
                }
            )
        return render(request, "config_busi/videoqualityassessment.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_videoqualityassessment()

        # 关联视频ID

        if mcauthfield_videoid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.videoid = obj.get("videoid")
        # 质量评分

        if mcauthfield_qualitysckwkwore["mcauthchange"]:

            # IntegerField # 其他情况/待补充

            ins_table_busi.qualitysckwkwore = obj.get("qualitysckwkwore")
        # 评估时间

        if mcauthfield_kwkwassessmenttime["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.kwkwassessmenttime = obj.get("kwkwassessmenttime")
        # 关联评审员ID

        if mcauthfield_reviewerid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.reviewerid = obj.get("reviewerid")
        # 帧率

        if mcauthfield_framerate["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.framerate = obj.get("framerate")
        # 分辨率

        if mcauthfield_resolution["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.resolution = obj.get("resolution")
        # 比特率

        if mcauthfield_bitrate["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.bitrate = obj.get("bitrate")
        # 编码格式

        if mcauthfield_encodkwkwingkwkwfkwkwormat["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.encodkwkwingkwkwfkwkwormat = obj.get(
                "encodkwkwingkwkwfkwkwormat"
            )
        # 是否检测到损坏

        if mcauthfield_ckwkworruptiondetected["mcauthchange"]:

            # BooleanField # 其他情况/待补充

            ins_table_busi.ckwkworruptiondetected = obj.get("ckwkworruptiondetected")
        # 相关问题ID

        if mcauthfield_relatedkwkwissueid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.relatedkwkwissueid = str(uuid.uuid4())
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_videoqualityassessment.objects.get(id=obj.get("_id_upd"))

        # 关联视频ID

        if mcauthfield_videoid["mcauthchange"]:

            # SelectField

            ins_table_busi.videoid = obj.get("videoid")
        # 质量评分

        if mcauthfield_qualitysckwkwore["mcauthchange"]:

            # IntegerField

            ins_table_busi.qualitysckwkwore = obj.get("qualitysckwkwore")
        # 评估时间

        if mcauthfield_kwkwassessmenttime["mcauthchange"]:

            # DateTimeField

            ins_table_busi.kwkwassessmenttime = obj.get("kwkwassessmenttime")
        # 关联评审员ID

        if mcauthfield_reviewerid["mcauthchange"]:

            # SelectField

            ins_table_busi.reviewerid = obj.get("reviewerid")
        # 帧率

        if mcauthfield_framerate["mcauthchange"]:

            # CharField

            ins_table_busi.framerate = obj.get("framerate")
        # 分辨率

        if mcauthfield_resolution["mcauthchange"]:

            # CharField

            ins_table_busi.resolution = obj.get("resolution")
        # 比特率

        if mcauthfield_bitrate["mcauthchange"]:

            # CharField

            ins_table_busi.bitrate = obj.get("bitrate")
        # 编码格式

        if mcauthfield_encodkwkwingkwkwfkwkwormat["mcauthchange"]:

            # CharField

            ins_table_busi.encodkwkwingkwkwfkwkwormat = obj.get(
                "encodkwkwingkwkwfkwkwormat"
            )
        # 是否检测到损坏

        if mcauthfield_ckwkworruptiondetected["mcauthchange"]:

            # BooleanField

            ins_table_busi.ckwkworruptiondetected = obj.get("ckwkworruptiondetected")
        # 相关问题ID

        if mcauthfield_relatedkwkwissueid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.relatedkwkwissueid = str(uuid.uuid4())

            ins_table_busi.relatedkwkwissueid = str(ins_table_busi.relatedkwkwissueid)
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_videoqualityassessment.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_videoqualityassessment.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/videoqualityassessment")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_videowatermarkinfo(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 视频水印信息表 系统管理员(8417)

    if user_table_id == str(8417):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 视频ID关联视频

        mcauthfield_videoid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 水印文本

        mcauthfield_watermarktext = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 水印位置如左上角、右下角等

        mcauthfield_watermarkposition = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 水印大小如百分比或像素值

        mcauthfield_watermarksize = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 水印透明度0100%

        mcauthfield_watermarkopacity = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 创建时间

        mcauthfield_createdat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 更新时间

        mcauthfield_updatedat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 是否激活用于控制水印是否生效如0为未激活1为激活

        mcauthfield_kwkwisactive = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }
    # 视频水印信息表 用户信息表(8395)

    if user_table_id == str(8395):
        config_user_table = mc_userinfo
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 视频ID关联视频

        mcauthfield_videoid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 水印文本

        mcauthfield_watermarktext = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 水印位置如左上角、右下角等

        mcauthfield_watermarkposition = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 水印大小如百分比或像素值

        mcauthfield_watermarksize = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 水印透明度0100%

        mcauthfield_watermarkopacity = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 创建时间

        mcauthfield_createdat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 更新时间

        mcauthfield_updatedat = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 是否激活用于控制水印是否生效如0为未激活1为激活

        mcauthfield_kwkwisactive = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_videowatermarkinfo.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_videowatermarkinfo().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_videowatermarkinfo.objects.filter(**filter)
        else:
            records = mc_videowatermarkinfo.objects.all()
        # 加载界面中下拉框所需数据

        data_mc_videoinfo_58170 = []
        for m in mc_videoinfo.objects.all():
            mobj = m.toJson()
            data_mc_videoinfo_58170.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("videotitle"),
                }
            )
        return render(request, "config_busi/videowatermarkinfo.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_videowatermarkinfo()

        # 视频ID关联视频

        if mcauthfield_videoid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.videoid = obj.get("videoid")
        # 水印文本

        if mcauthfield_watermarktext["mcauthchange"]:

            # TextField # 其他情况/待补充

            ins_table_busi.watermarktext = obj.get("watermarktext")
        # 水印位置如左上角、右下角等

        if mcauthfield_watermarkposition["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.watermarkposition = obj.get("watermarkposition")
        # 水印大小如百分比或像素值

        if mcauthfield_watermarksize["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.watermarksize = obj.get("watermarksize")
        # 水印透明度0100%

        if mcauthfield_watermarkopacity["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.watermarkopacity = obj.get("watermarkopacity")
        # 创建时间

        if mcauthfield_createdat["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.createdat = obj.get("createdat")
        # 更新时间

        if mcauthfield_updatedat["mcauthchange"]:

            # DateTimeField # 其他情况/待补充

            ins_table_busi.updatedat = obj.get("updatedat")
        # 是否激活用于控制水印是否生效如0为未激活1为激活

        if mcauthfield_kwkwisactive["mcauthchange"]:

            # BooleanField # 其他情况/待补充

            ins_table_busi.kwkwisactive = obj.get("kwkwisactive")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_videowatermarkinfo.objects.get(id=obj.get("_id_upd"))

        # 视频ID关联视频

        if mcauthfield_videoid["mcauthchange"]:

            # SelectField

            ins_table_busi.videoid = obj.get("videoid")
        # 水印文本

        if mcauthfield_watermarktext["mcauthchange"]:

            # TextField

            ins_table_busi.watermarktext = obj.get("watermarktext")
        # 水印位置如左上角、右下角等

        if mcauthfield_watermarkposition["mcauthchange"]:

            # CharField

            ins_table_busi.watermarkposition = obj.get("watermarkposition")
        # 水印大小如百分比或像素值

        if mcauthfield_watermarksize["mcauthchange"]:

            # CharField

            ins_table_busi.watermarksize = obj.get("watermarksize")
        # 水印透明度0100%

        if mcauthfield_watermarkopacity["mcauthchange"]:

            # CharField

            ins_table_busi.watermarkopacity = obj.get("watermarkopacity")
        # 创建时间

        if mcauthfield_createdat["mcauthchange"]:

            # DateTimeField

            ins_table_busi.createdat = obj.get("createdat")
        # 更新时间

        if mcauthfield_updatedat["mcauthchange"]:

            # DateTimeField

            ins_table_busi.updatedat = obj.get("updatedat")
        # 是否激活用于控制水印是否生效如0为未激活1为激活

        if mcauthfield_kwkwisactive["mcauthchange"]:

            # BooleanField

            ins_table_busi.kwkwisactive = obj.get("kwkwisactive")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_videowatermarkinfo.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_videowatermarkinfo.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/videowatermarkinfo")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_videocopyrightinfo(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 视频版权信息表 系统管理员(8417)

    if user_table_id == str(8417):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 关联视频ID

        mcauthfield_videoid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 版权持有人

        mcauthfield_copyrightholder = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 版权年份

        mcauthfield_copyrightyear = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 许可类型

        mcauthfield_licensetype = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 许可状态

        mcauthfield_licensestatus = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 版权描述

        mcauthfield_description = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 创建日期

        mcauthfield_creationdate = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 修改日期

        mcauthfield_modkwkwificationdate = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 相关视频ID

        mcauthfield_relatedvideoid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }
    # 视频版权信息表 用户信息表(8395)

    if user_table_id == str(8395):
        config_user_table = mc_userinfo
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 关联视频ID

        mcauthfield_videoid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 版权持有人

        mcauthfield_copyrightholder = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 版权年份

        mcauthfield_copyrightyear = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 许可类型

        mcauthfield_licensetype = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 许可状态

        mcauthfield_licensestatus = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 版权描述

        mcauthfield_description = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 创建日期

        mcauthfield_creationdate = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 修改日期

        mcauthfield_modkwkwificationdate = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }

        # 相关视频ID

        mcauthfield_relatedvideoid = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_videocopyrightinfo.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_videocopyrightinfo().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_videocopyrightinfo.objects.filter(**filter)
        else:
            records = mc_videocopyrightinfo.objects.all()
        # 加载界面中下拉框所需数据

        data_mc_videoinfo_58178 = []
        for m in mc_videoinfo.objects.all():
            mobj = m.toJson()
            data_mc_videoinfo_58178.append(
                {
                    "value": mobj.get("id"),
                    # 'value':'mobj.get('id'),
                    "label": mobj.get("videotitle"),
                }
            )
        return render(request, "config_busi/videocopyrightinfo.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_videocopyrightinfo()

        # 关联视频ID

        if mcauthfield_videoid["mcauthchange"]:

            # SelectField # 其他情况/待补充

            ins_table_busi.videoid = obj.get("videoid")
        # 版权持有人

        if mcauthfield_copyrightholder["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.copyrightholder = obj.get("copyrightholder")
        # 版权年份

        if mcauthfield_copyrightyear["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.copyrightyear = obj.get("copyrightyear")
        # 许可类型

        if mcauthfield_licensetype["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.licensetype = obj.get("licensetype")
        # 许可状态

        if mcauthfield_licensestatus["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.licensestatus = obj.get("licensestatus")
        # 版权描述

        if mcauthfield_description["mcauthchange"]:

            # TextField # 其他情况/待补充

            ins_table_busi.description = obj.get("description")
        # 创建日期

        if mcauthfield_creationdate["mcauthchange"]:

            # DateField # 其他情况/待补充

            ins_table_busi.creationdate = obj.get("creationdate")
        # 修改日期

        if mcauthfield_modkwkwificationdate["mcauthchange"]:

            # DateField # 其他情况/待补充

            ins_table_busi.modkwkwificationdate = obj.get("modkwkwificationdate")
        # 相关视频ID

        if mcauthfield_relatedvideoid["mcauthchange"]:

            # UUIDField UUIDField

            ins_table_busi.relatedvideoid = str(uuid.uuid4())
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_videocopyrightinfo.objects.get(id=obj.get("_id_upd"))

        # 关联视频ID

        if mcauthfield_videoid["mcauthchange"]:

            # SelectField

            ins_table_busi.videoid = obj.get("videoid")
        # 版权持有人

        if mcauthfield_copyrightholder["mcauthchange"]:

            # CharField

            ins_table_busi.copyrightholder = obj.get("copyrightholder")
        # 版权年份

        if mcauthfield_copyrightyear["mcauthchange"]:

            # CharField

            ins_table_busi.copyrightyear = obj.get("copyrightyear")
        # 许可类型

        if mcauthfield_licensetype["mcauthchange"]:

            # CharField

            ins_table_busi.licensetype = obj.get("licensetype")
        # 许可状态

        if mcauthfield_licensestatus["mcauthchange"]:

            # CharField

            ins_table_busi.licensestatus = obj.get("licensestatus")
        # 版权描述

        if mcauthfield_description["mcauthchange"]:

            # TextField

            ins_table_busi.description = obj.get("description")
        # 创建日期

        if mcauthfield_creationdate["mcauthchange"]:

            # DateField

            ins_table_busi.creationdate = obj.get("creationdate")
        # 修改日期

        if mcauthfield_modkwkwificationdate["mcauthchange"]:

            # DateField

            ins_table_busi.modkwkwificationdate = obj.get("modkwkwificationdate")
        # 相关视频ID

        if mcauthfield_relatedvideoid["mcauthchange"]:

            # UUIDField UUIDField 防止修改时修改UUID
            # ins_table_busi.relatedvideoid = str(uuid.uuid4())

            ins_table_busi.relatedvideoid = str(ins_table_busi.relatedvideoid)
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_videocopyrightinfo.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_videocopyrightinfo.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/videocopyrightinfo")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


@login_required
def view_supermanager(request):
    uesr_table_id = request.COOKIES.get("user_table_id", None)
    if uesr_table_id is None:
        return redirect("/")
    user_table_id = request.COOKIES.get("user_table_id")
    user_id = request.user.id
    username = request.user.username

    # 默认用户表权限以系统管理员为基准

    config_user_table = mc_supermanager

    # 表权限检测

    # 系统管理员 系统管理员(8417)

    if user_table_id == str(8417):
        config_user_table = mc_supermanager
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 管理员姓名

        mcauthfield_username = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }
    # 系统管理员 用户信息表(8395)

    if user_table_id == str(8395):
        config_user_table = mc_userinfo
        has_add = True
        has_upd = True
        has_del = True
        has_view = True
        # 管理员姓名

        mcauthfield_username = {
            "mcisnull": True,
            "mcisblank": True,
            "mcauthview": has_view,
            "mcauthchange": has_upd,
        }
    # 获取登录用户所在用户表记录

    config_user_obj = config_user_table.objects.filter(username=username)
    if len(config_user_obj) == 0:
        return redirect("/")
    if len(config_user_obj) > 1:
        return JsonResponse({"res": "OK", "msg": "用户表存在同名用户,请修复"})
    # 当前登录用户所在用户表的记录

    config_user_obj = config_user_obj[0]
    # 当前登录用户所在用户表的ID,默认使用该ID做筛选和查询

    config_user_id = config_user_obj.id
    if request.method == "GET":
        obj = mydict(request.GET)
        # 对于带参数的get请求
        # records = [m.toJson() for m in mc_supermanager.objects.all()]
        # 默认获取所有数据,如需添加仅当前登录用户查看,则手动添加筛选

        filter = {
            field.name: obj.get(field.name + "_search")
            for field in mc_supermanager().toParams()
            if field.name + "_search" in obj
        }
        if len(filter) > 0:
            records = mc_supermanager.objects.filter(**filter)
        else:
            records = mc_supermanager.objects.all()
        # 加载界面中下拉框所需数据

        return render(request, "config_busi/supermanager.html", locals())
    # 获取post请求参数

    obj = mydict(request.POST)
    # 获取get请求参数

    obj_get = mydict(request.GET)
    optype = obj.get("optype")
    # 若用户有添加数据的权限

    if optype == "add" and has_add:
        ins_table_busi = mc_supermanager()

        # 管理员姓名

        if mcauthfield_username["mcauthchange"]:

            # CharField # 其他情况/待补充

            ins_table_busi.username = obj.get("username")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "upd" and has_upd:
        ins_table_busi = mc_supermanager.objects.get(id=obj.get("_id_upd"))

        # 管理员姓名

        if mcauthfield_username["mcauthchange"]:

            # CharField

            ins_table_busi.username = obj.get("username")
        ins_table_busi.save()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "del" and has_del:
        ins_table_busi = mc_supermanager.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
    if optype == "get" and has_view:
        ins_table_busi = mc_supermanager.objects.get(id=obj.get("_id"))
        res = {"msg": "success", "obj": obj, "ins": ins_table_busi.toJson()}
        return JsonResponse(res)
    # 添加其他接口访问.若是json则直接return JsonResponse(res)
    # 默认刷新当前页面
    # return redirect("/config_busi/supermanager")
    # 获取当前访问url完整路径,附带查询参数

    return redirect(request.get_full_path())


def auto_detect(request):
    if request.method == "GET":
        detect = False

        return render(request, "config_algorithm/auto_detect.html", locals())
    obj = mydict(request.POST)

    if "img" not in request.FILES:
        return HttpResponse("请上传图片")
    img = request.FILES["img"]
    # mc_

    detect = True

    detect_result = "算法结果展示"

    # 保存提交的内容
    # 保存分析的结果
    # 若源码中缺少需要的表和字段.联系 qq952934650

    return render(request, "config_algorithm/auto_detect.html", locals())
