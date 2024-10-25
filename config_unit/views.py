import codecs
import json
import os
from django.http import FileResponse, JsonResponse
from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import login_required
from django.contrib.auth import login as django_default_login
from django.conf import settings
from django.contrib.auth.models import User
from sys_user.form import *
from sys_user.func import *
from config_unit.models import all_tables, gl
from config_unit.form import all_tables_form
from config_unit.captcha_impl import get_refresh_captcha, captcha_image
from appcenter.models import *


# Create your views here.


def index_view(request):
    if request.method == "GET":
        # 默认接口前缀配置

        config_unit = ""
        # config_unit = "/config_unit"
        # 主页默认配置信息

        tables = all_tables

        return render(request, "config_unit/index.html", locals())
    return JsonResponse({"status": "error", "msg": "请求错误"})


def refresh_view(request):
    code = get_refresh_captcha(request)
    return JsonResponse({"code": code, "msg": "验证码刷新成功", "res": "ok"})


def register(request):
    try:
        obj = json.loads(request.body)
        isok = True
    except Exception as e:
        pass
    try:
        obj = mydict(request.POST)
        isok = True
    except Exception as e:
        pass
    registerform = RegisterForm(obj)
    if not registerform.is_valid():
        return JsonResponse({"status": "error", "msg": "表单验证失败"})
    username = registerform.cleaned_data.get("username")
    password1 = registerform.cleaned_data.get("password1")
    password2 = registerform.cleaned_data.get("password2")

    user = User.objects.filter(username=username)
    if user:
        return JsonResponse({"status": "error", "msg": "用户名已存在"})
    if password1 != password2:
        return JsonResponse({"status": "error", "msg": "密码不一致"})
    user = User.objects.create_user(
        username=username,
        password=password1,
        email=registerform.cleaned_data.get("email"),
        is_superuser=True,
    )
    
    mc_supermanager(username=username).save()
    user.set_password(password1)
    user.save()
    return JsonResponse({"res": "OK", "msg": "注册成功"})


def logout_view(request):
    logout(request)

    response = redirect("/")
    response.delete_cookie("username")
    return response


def login_view(request):
    if request.method == "GET":
        return JsonResponse({"res": "Not Allowed", "msg": "请求错误"})
    # post

    try:
        obj = json.loads(request.body)
        isok = True
    except Exception as e:
        pass
    try:
        obj = mydict(request.POST)
        isok = True
    except Exception as e:
        pass
    loginform = LoginForm(obj)
    print(loginform)
    if not loginform.is_valid():
        return JsonResponse({"res": "error", "msg": "表单验证失败"})
    username = loginform.cleaned_data.get("username")
    password = loginform.cleaned_data.get("password")
    # 与数据库中的用户名和密码比对，django默认保存密码是以哈希形式存储，并不是明文密码，这里的password验证默认调用的是User类的check_password方法，以哈希值比较。

    user = authenticate(request, username=username, password=password)
    # 验证如果用户不为空

    if user is None:
        # 返回登录失败信息

        return JsonResponse({"res": "error", "message": "用户名或密码错误"})
    # login方法登录

    django_default_login(request, user)

    response = JsonResponse(
        {
            "res": "OK",
            "msg": "登录成功",
            "token": 1,
            "userid": request.user.id,
            "username": request.user.username,
        }
    )
    response.set_cookie("username", username)
    response.set_cookie("token", 1)
    response.set_cookie("userid", request.user.id)
    return response


def serve_media(request, path):
    """访问media内文件

    Args:
        request (RequestHandle): 请求
        path (路径): XXX.xxx

    Raises:
        Http404: 未找到文件

    Returns:
        filestream: 文件流
    """
    # 构建文件的绝对路径

    file_path = "media/" + path + ".zip"
    # file_path = os.path.join(settings.MEDIA_ROOT, file_path)

    file_path = file_path.replace("\\", "/")
    print(file_path)

    # 检查文件是否存在

    if os.path.exists(file_path):
        # 在打开文件之前添加安全性检查
        # safe_path = os.path.normpath(file_path).replace('\\', '/')
        # if not os.path.commonprefix((safe_path, settings.MEDIA_ROOT)) == settings.MEDIA_ROOT.replace('\\', '/'):
        #     # 路径不在 MEDIA_ROOT 内，拒绝服务
        #     print('safe_path: ',safe_path)
        #     print(os.path.commonprefix((safe_path, settings.MEDIA_ROOT)))
        #     print('MEDIA_ROOT:', settings.MEDIA_ROOT.replace('\\', '/'))
        #     raise Http404
        # 创建一个响应对象，设置适当的 Content-Disposition 头部

        response = FileResponse(file_path, filename=file_path)
        response["Content-Type"] = "application/octet-stream"
        response["Content-Disposition"] = (
            'attachment; filename="' + os.path.basename(file_path) + '"'
        )
        return response
    # 如果文件不存在，返回 404 错误

    from django.http import Http404

    raise Http404


def config_unit(request, tablename):
    # 检查权限

    has_add = True
    has_upd = True
    has_del = True
    has_view = True

    if request.method == "GET":
        return JsonResponse({"res": "Not Allowed", "msg": "请求错误"})
    # 对于无参数的post请求此处会报异常
    # obj = mydict(request.POST)

    if len(request.body) == 0:
        return JsonResponse({"res": "Not Allowed", "msg": "optype不存在"})
    isok = False
    try:

        obj = json.loads(request.body)
        isok = True
    except Exception as e:
        pass
    try:
        obj = mydict(request.POST)
        isok = True
    except Exception as e:
        pass
    if not isok:
        return JsonResponse({"res": "Not Allowed", "msg": "参数解析失败"})
    if "optype" not in obj:
        return JsonResponse({"res": "Not Allowed", "msg": "optype不存在"})
    optype = obj.get("optype")

    # 根据表名获取数据

    tableins = gl.get(tablename)
    tablemeta = all_tables.get(tablename)
    if tableins is None:
        print(gl.keys())
        return JsonResponse({"res": "Not Allowed", "msg": "表名错误:" + tablename})
    if tablemeta is None:
        return JsonResponse({"res": "Not Allowed", "msg": "表名错误:" + tablename})
    if optype == "add" and has_add:
        ins_table_busi = tableins()
        for fieldname in tablemeta.get("field"):
            if fieldname == "id":
                continue
            if fieldname not in obj:
                continue
            setattr(ins_table_busi, fieldname, obj.get(fieldname, ""))
        try:
            ins_table_busi.save()
        except Exception as e:
            print(e)
            return JsonResponse({"res": "error", "msg": f"添加失败-{e}"})
        res = {
            "res": "OK",
            "msg": "success",
            "obj": obj,
            "ins": ins_table_busi.toJson(),
        }
    if optype == "upd" and has_upd:
        ins_table_busi = tableins.objects.get(id=obj.get("_id_upd"))

        for fieldname in tablemeta.get("field"):
            if fieldname == "id":
                continue
            if fieldname not in obj:
                continue
            setattr(ins_table_busi, fieldname, obj.get(fieldname))
        ins_table_busi.save()
        res = {
            "res": "OK",
            "msg": "success",
            "obj": obj,
            "ins": ins_table_busi.toJson(),
        }
    if optype == "del" and has_del:
        ins_table_busi = tableins.objects.get(id=obj.get("_id"))
        ins_table_busi.delete()
        res = {
            "res": "OK",
            "msg": "success",
            "obj": obj,
            "ins": ins_table_busi.toJson(),
        }
    if optype == "get" and has_view:
        ins_table_busi = tableins.objects.get(id=obj.get("_id"))
        res = {
            "res": "OK",
            "msg": "success",
            "obj": obj,
            "ins": ins_table_busi.toJson(),
        }
    if optype == "filter" and has_view:
        condition = {
            param: obj.get(param) for param in tableins().toParams_en() if param in obj
        }
        ins_table_busis = [m.toJson() for m in tableins.objects.filter(**condition)]
        res = {
            "res": "OK",
            "msg": "success",
            "obj": obj,
            "ins": ins_table_busis,
        }
    # 获取记录的详细数据，默认只获取第一层，如需深入获取外键信息可去models.py中修改toJson()函数

    if optype == "view" and has_view:
        ins_table_busi = tableins.objects.get(id=obj.get("_id"))
        res = {
            "res": "OK",
            "msg": "success",
            "obj": obj,
            "ins": ins_table_busi.toJson(),
        }
    # 用于渲染新增form表单/页面

    if optype == "go_add" and has_add:

        ins_table_busi = tableins()
        res = {
            "res": "OK",
            "msg": "success",
            "obj": obj,
            "ins": ins_table_busi.toJson(),
        }
    # 用于渲染修改form表单/页面，并将数据回显

    if optype == "go_upd" and has_add:
        ins_table_busi = tableins.objects.get(id=obj.get("form").get("id"))
        res = {
            "res": "OK",
            "msg": "success",
            "obj": obj,
            "ins": ins_table_busi.toJson(),
        }
    return JsonResponse(res)


def table_busi(request):
    if request.method == "GET":
        return JsonResponse({"res": "Not Allowed", "msg": "请求错误"})
    ins = dict()

    ins["videoinfo"] = mymeta(mc_videoinfo)

    ins["videocategkwkwory"] = mymeta(mc_videocategkwkwory)

    ins["videotag"] = mymeta(mc_videotag)

    ins["videofilestkwkworage"] = mymeta(mc_videofilestkwkworage)

    ins["videoplayreckwkword"] = mymeta(mc_videoplayreckwkword)

    ins["videocomment"] = mymeta(mc_videocomment)

    ins["videolike"] = mymeta(mc_videolike)

    ins["videoshare"] = mymeta(mc_videoshare)

    ins["videoviewduration"] = mymeta(mc_videoviewduration)

    ins["videouploader"] = mymeta(mc_videouploader)

    ins["userinfo"] = mymeta(mc_userinfo)

    ins["userpermkwkwission"] = mymeta(mc_userpermkwkwission)

    ins["userwatchhkwkwistkwkwory"] = mymeta(mc_userwatchhkwkwistkwkwory)

    ins["videoauditstatus"] = mymeta(mc_videoauditstatus)

    ins["videocoverimage"] = mymeta(mc_videocoverimage)

    ins["videomatrixconfig"] = mymeta(mc_videomatrixconfig)

    ins["videomatrixnode"] = mymeta(mc_videomatrixnode)

    ins["videomatrixplayreckwkword"] = mymeta(mc_videomatrixplayreckwkword)

    ins["videorelatedcontent"] = mymeta(mc_videorelatedcontent)

    ins["videoerrkwkworlog"] = mymeta(mc_videoerrkwkworlog)

    ins["videopopularity"] = mymeta(mc_videopopularity)

    ins["videorecommendationparams"] = mymeta(mc_videorecommendationparams)

    ins["videoadinfo"] = mymeta(mc_videoadinfo)

    ins["videoadplayreckwkword"] = mymeta(mc_videoadplayreckwkword)

    ins["videodanmu"] = mymeta(mc_videodanmu)

    ins["videodanmublockwkwkwords"] = mymeta(mc_videodanmublockwkwkwords)

    ins["videomultilkwkwingualsubtitles"] = mymeta(mc_videomultilkwkwingualsubtitles)

    ins["videotranscodkwkwingtkwkwask"] = mymeta(mc_videotranscodkwkwingtkwkwask)

    ins["videoanalyskwkwismetrics"] = mymeta(mc_videoanalyskwkwismetrics)

    ins["videoqualityassessment"] = mymeta(mc_videoqualityassessment)

    ins["videowatermarkinfo"] = mymeta(mc_videowatermarkinfo)

    ins["videocopyrightinfo"] = mymeta(mc_videocopyrightinfo)

    ins["supermanager"] = mymeta(mc_supermanager)

    res = {"res": "OK", "msg": "success", "obj": {}, "ins": ins}

    return JsonResponse(res)


def table_user(request):
    if request.method == "GET":
        return JsonResponse({"res": "Not Allowed", "msg": "请求错误"})
    ins = dict()

    ins["userinfo"] = mymeta(mc_userinfo)

    ins["supermanager"] = mymeta(mc_supermanager)

    res = {"res": "OK", "msg": "success", "obj": {}, "ins": ins}

    return JsonResponse(res)


def auth_table(request):
    if request.method == "GET":
        return JsonResponse({"res": "Not Allowed", "msg": "请求错误"})
    ins = dict()

    ins["8385,8395"] = (mymeta(mc_videoinfo), mymeta(mc_userinfo))

    ins["8385,8417"] = (mymeta(mc_videoinfo), mymeta(mc_supermanager))

    ins["8386,8395"] = (mymeta(mc_videocategkwkwory), mymeta(mc_userinfo))

    ins["8386,8417"] = (mymeta(mc_videocategkwkwory), mymeta(mc_supermanager))

    ins["8387,8395"] = (mymeta(mc_videotag), mymeta(mc_userinfo))

    ins["8387,8417"] = (mymeta(mc_videotag), mymeta(mc_supermanager))

    ins["8388,8395"] = (mymeta(mc_videofilestkwkworage), mymeta(mc_userinfo))

    ins["8388,8417"] = (mymeta(mc_videofilestkwkworage), mymeta(mc_supermanager))

    ins["8389,8395"] = (mymeta(mc_videoplayreckwkword), mymeta(mc_userinfo))

    ins["8389,8417"] = (mymeta(mc_videoplayreckwkword), mymeta(mc_supermanager))

    ins["8390,8395"] = (mymeta(mc_videocomment), mymeta(mc_userinfo))

    ins["8390,8417"] = (mymeta(mc_videocomment), mymeta(mc_supermanager))

    ins["8391,8395"] = (mymeta(mc_videolike), mymeta(mc_userinfo))

    ins["8391,8417"] = (mymeta(mc_videolike), mymeta(mc_supermanager))

    ins["8392,8395"] = (mymeta(mc_videoshare), mymeta(mc_userinfo))

    ins["8392,8417"] = (mymeta(mc_videoshare), mymeta(mc_supermanager))

    ins["8393,8395"] = (mymeta(mc_videoviewduration), mymeta(mc_userinfo))

    ins["8393,8417"] = (mymeta(mc_videoviewduration), mymeta(mc_supermanager))

    ins["8394,8395"] = (mymeta(mc_videouploader), mymeta(mc_userinfo))

    ins["8394,8417"] = (mymeta(mc_videouploader), mymeta(mc_supermanager))

    ins["8395,8395"] = (mymeta(mc_userinfo), mymeta(mc_userinfo))

    ins["8395,8417"] = (mymeta(mc_userinfo), mymeta(mc_supermanager))

    ins["8396,8395"] = (mymeta(mc_userpermkwkwission), mymeta(mc_userinfo))

    ins["8396,8417"] = (mymeta(mc_userpermkwkwission), mymeta(mc_supermanager))

    ins["8397,8395"] = (mymeta(mc_userwatchhkwkwistkwkwory), mymeta(mc_userinfo))

    ins["8397,8417"] = (mymeta(mc_userwatchhkwkwistkwkwory), mymeta(mc_supermanager))

    ins["8398,8395"] = (mymeta(mc_videoauditstatus), mymeta(mc_userinfo))

    ins["8398,8417"] = (mymeta(mc_videoauditstatus), mymeta(mc_supermanager))

    ins["8399,8395"] = (mymeta(mc_videocoverimage), mymeta(mc_userinfo))

    ins["8399,8417"] = (mymeta(mc_videocoverimage), mymeta(mc_supermanager))

    ins["8400,8395"] = (mymeta(mc_videomatrixconfig), mymeta(mc_userinfo))

    ins["8400,8417"] = (mymeta(mc_videomatrixconfig), mymeta(mc_supermanager))

    ins["8401,8395"] = (mymeta(mc_videomatrixnode), mymeta(mc_userinfo))

    ins["8401,8417"] = (mymeta(mc_videomatrixnode), mymeta(mc_supermanager))

    ins["8402,8395"] = (mymeta(mc_videomatrixplayreckwkword), mymeta(mc_userinfo))

    ins["8402,8417"] = (mymeta(mc_videomatrixplayreckwkword), mymeta(mc_supermanager))

    ins["8403,8395"] = (mymeta(mc_videorelatedcontent), mymeta(mc_userinfo))

    ins["8403,8417"] = (mymeta(mc_videorelatedcontent), mymeta(mc_supermanager))

    ins["8404,8395"] = (mymeta(mc_videoerrkwkworlog), mymeta(mc_userinfo))

    ins["8404,8417"] = (mymeta(mc_videoerrkwkworlog), mymeta(mc_supermanager))

    ins["8405,8395"] = (mymeta(mc_videopopularity), mymeta(mc_userinfo))

    ins["8405,8417"] = (mymeta(mc_videopopularity), mymeta(mc_supermanager))

    ins["8406,8395"] = (mymeta(mc_videorecommendationparams), mymeta(mc_userinfo))

    ins["8406,8417"] = (mymeta(mc_videorecommendationparams), mymeta(mc_supermanager))

    ins["8407,8395"] = (mymeta(mc_videoadinfo), mymeta(mc_userinfo))

    ins["8407,8417"] = (mymeta(mc_videoadinfo), mymeta(mc_supermanager))

    ins["8408,8395"] = (mymeta(mc_videoadplayreckwkword), mymeta(mc_userinfo))

    ins["8408,8417"] = (mymeta(mc_videoadplayreckwkword), mymeta(mc_supermanager))

    ins["8409,8395"] = (mymeta(mc_videodanmu), mymeta(mc_userinfo))

    ins["8409,8417"] = (mymeta(mc_videodanmu), mymeta(mc_supermanager))

    ins["8410,8395"] = (mymeta(mc_videodanmublockwkwkwords), mymeta(mc_userinfo))

    ins["8410,8417"] = (mymeta(mc_videodanmublockwkwkwords), mymeta(mc_supermanager))

    ins["8411,8395"] = (mymeta(mc_videomultilkwkwingualsubtitles), mymeta(mc_userinfo))

    ins["8411,8417"] = (
        mymeta(mc_videomultilkwkwingualsubtitles),
        mymeta(mc_supermanager),
    )

    ins["8412,8395"] = (mymeta(mc_videotranscodkwkwingtkwkwask), mymeta(mc_userinfo))

    ins["8412,8417"] = (
        mymeta(mc_videotranscodkwkwingtkwkwask),
        mymeta(mc_supermanager),
    )

    ins["8413,8395"] = (mymeta(mc_videoanalyskwkwismetrics), mymeta(mc_userinfo))

    ins["8413,8417"] = (mymeta(mc_videoanalyskwkwismetrics), mymeta(mc_supermanager))

    ins["8414,8395"] = (mymeta(mc_videoqualityassessment), mymeta(mc_userinfo))

    ins["8414,8417"] = (mymeta(mc_videoqualityassessment), mymeta(mc_supermanager))

    ins["8415,8395"] = (mymeta(mc_videowatermarkinfo), mymeta(mc_userinfo))

    ins["8415,8417"] = (mymeta(mc_videowatermarkinfo), mymeta(mc_supermanager))

    ins["8416,8395"] = (mymeta(mc_videocopyrightinfo), mymeta(mc_userinfo))

    ins["8416,8417"] = (mymeta(mc_videocopyrightinfo), mymeta(mc_supermanager))

    ins["8417,8395"] = (mymeta(mc_supermanager), mymeta(mc_userinfo))

    ins["8417,8417"] = (mymeta(mc_supermanager), mymeta(mc_supermanager))

    res = {"res": "OK", "msg": "success", "obj": {}, "ins": ins}

    return JsonResponse(res)


def common_form(request, tablename):
    if request.method == "GET":
        return JsonResponse({"res": "Not Allowed", "msg": "请求错误"})
    tableins = gl.get(tablename)
    tablemeta = all_tables.get(tablename)

    obj = json.loads(request.body)

    optype = obj.get("optype")
    if optype == "add":
        formins = all_tables_form.get(tablename)
        res = {"res": "OK", "msg": "success", "obj": {}, "ins": formins().as_p()}
    if optype == "upd":
        formins = all_tables_form.get(tablename)
        myform = formins(tableins.objects.get(id=obj.get("id")))
        res = {"res": "OK", "msg": "success", "obj": {}, "ins": myform.as_p()}
    return JsonResponse(res)


def submit_view(request):
    if request.method == "GET":
        return JsonResponse({"res": "Not Allowed", "msg": "请求错误"})
    obj = json.loads(request.body)

    tablename = obj.get("tablename")
    if tablename == "supermanager":
        return JsonResponse({"res": "Not Allowed", "msg": "禁止在此创建系统管理员"})
    tableins = gl.get(tablename)
    tablemeta = all_tables.get(tablename)
    form = obj["form"]
    print(form)
    if "id" not in form or form["id"] is None:
        ins = tableins()
        for k, v in obj.get("form").items():
            if v is None:
                continue
            setattr(ins, k, v)
        ins.save()
        obj["optype"] = "add"
        res = {"res": "OK", "msg": "success", "ins": ins.toJson(), "obj": obj}
    else:
        ins = tableins.objects.get(id=obj.get("form").get("id"))
        for k, v in obj.get("form").items():
            setattr(ins, k, v)
        ins.save()
        obj["optype"] = "upd"
        res = {"res": "OK", "msg": "success", "ins": ins.toJson(), "obj": obj}
    return JsonResponse(res)


from django.views.decorators.csrf import get_token


def ucsrf(request):
    return JsonResponse({"csrfToken": get_token(request)})
