from datetime import datetime
import os
import time

from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.template import loader
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.views import login_required
from .form import *
from .models import *
from sys_user.func import *

# 词云

from a_simulink_unit.generate_wordcloud import generate_wordcloud_base64

# Create your views here.


def index(request):

    return render(request, "config_visual/index.html", locals())


"""

# 系统中所有数据表名/中英文+字段中英文
用于快速创建查询语句和分析
测试通过后删除此段.
__deprected__ mark_appcenter_views_all_tables_and_fields
__deprected__ mark_appcenter_views_all_tables_and__two_field_fields
# 根据需要按照表结构和csv文件依次导入数据库.
"""


def bi(request):
    if request.method == "GET":
        return HttpResponse(
            loader.get_template("config_visual/bi.html").render({}, request)
        )
    obj = mydict(request.POST)
    res = dict()

    # videoinfo(视频信息表)->videoid(视频ID)

    if obj.get("optype") == "videoinfo.videoid_pie":
        res = get_pie(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videoinfo group by videoid order by x desc",
            "视频ID",
        )
    if obj.get("optype") == "videoinfo.videoid_pie_v1":
        res = get_pie_v1(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videoinfo group by videoid",
            "视频ID",
        )
    if obj.get("optype") == "videoinfo.videoid_pie_v2":
        res = get_pie_v2(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videoinfo group by videoid",
            "视频ID",
        )
    if obj.get("optype") == "videoinfo.videoid_line":
        res = get_line(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videoinfo group by videoid",
            "视频ID",
        )
    if obj.get("optype") == "videoinfo.videoid_bar":
        res = get_bar(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videoinfo group by videoid",
            "视频ID",
        )
    if obj.get("optype") == "videoinfo.videoid_bar_v1":
        res = get_bar_v1(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videoinfo group by videoid",
            "视频ID",
        )
    # videoinfo(视频信息表)->videotitle(视频标题)

    if obj.get("optype") == "videoinfo.videotitle_pie":
        res = get_pie(
            "select videotitle x,count(*) y from vm790_bcfe8a202787453d.videoinfo group by videotitle order by x desc",
            "视频标题",
        )
    if obj.get("optype") == "videoinfo.videotitle_pie_v1":
        res = get_pie_v1(
            "select videotitle x,count(*) y from vm790_bcfe8a202787453d.videoinfo group by videotitle",
            "视频标题",
        )
    if obj.get("optype") == "videoinfo.videotitle_pie_v2":
        res = get_pie_v2(
            "select videotitle x,count(*) y from vm790_bcfe8a202787453d.videoinfo group by videotitle",
            "视频标题",
        )
    if obj.get("optype") == "videoinfo.videotitle_line":
        res = get_line(
            "select videotitle x,count(*) y from vm790_bcfe8a202787453d.videoinfo group by videotitle",
            "视频标题",
        )
    if obj.get("optype") == "videoinfo.videotitle_bar":
        res = get_bar(
            "select videotitle x,count(*) y from vm790_bcfe8a202787453d.videoinfo group by videotitle",
            "视频标题",
        )
    if obj.get("optype") == "videoinfo.videotitle_bar_v1":
        res = get_bar_v1(
            "select videotitle x,count(*) y from vm790_bcfe8a202787453d.videoinfo group by videotitle",
            "视频标题",
        )
    if obj.get("optype") == "videoinfo.videodescription_wordcloud":
        textlist = get_data(
            "SELECT videodescription result FROM vm790_bcfe8a202787453d.videoinfo;"
        )
        res = {
            "title": "词云图",
            "imgbs64": generate_wordcloud_base64(
                ",".join([t["result"] for t in textlist])
            ),
        }
    if obj.get("optype") == "videoinfo.uploadtime_line":
        res = get_line(
            "select uploadtime x,count(*) y from vm790_bcfe8a202787453d.videoinfo group by uploadtime order by x",
            "上传时间",
        )
    # videoinfo(视频信息表)->duration(视频时长秒)

    if obj.get("optype") == "videoinfo.duration_pie":
        res = get_pie(
            "select duration x,count(*) y from vm790_bcfe8a202787453d.videoinfo group by duration order by x desc",
            "视频时长秒",
        )
    if obj.get("optype") == "videoinfo.duration_pie_v1":
        res = get_pie_v1(
            "select duration x,count(*) y from vm790_bcfe8a202787453d.videoinfo group by duration",
            "视频时长秒",
        )
    if obj.get("optype") == "videoinfo.duration_pie_v2":
        res = get_pie_v2(
            "select duration x,count(*) y from vm790_bcfe8a202787453d.videoinfo group by duration",
            "视频时长秒",
        )
    if obj.get("optype") == "videoinfo.duration_line":
        res = get_line(
            "select duration x,count(*) y from vm790_bcfe8a202787453d.videoinfo group by duration",
            "视频时长秒",
        )
    if obj.get("optype") == "videoinfo.duration_bar":
        res = get_bar(
            "select duration x,count(*) y from vm790_bcfe8a202787453d.videoinfo group by duration",
            "视频时长秒",
        )
    if obj.get("optype") == "videoinfo.duration_bar_v1":
        res = get_bar_v1(
            "select duration x,count(*) y from vm790_bcfe8a202787453d.videoinfo group by duration",
            "视频时长秒",
        )
    # videoinfo(视频信息表)->resolution(视频分辨率)

    if obj.get("optype") == "videoinfo.resolution_pie":
        res = get_pie(
            "select resolution x,count(*) y from vm790_bcfe8a202787453d.videoinfo group by resolution order by x desc",
            "视频分辨率",
        )
    if obj.get("optype") == "videoinfo.resolution_pie_v1":
        res = get_pie_v1(
            "select resolution x,count(*) y from vm790_bcfe8a202787453d.videoinfo group by resolution",
            "视频分辨率",
        )
    if obj.get("optype") == "videoinfo.resolution_pie_v2":
        res = get_pie_v2(
            "select resolution x,count(*) y from vm790_bcfe8a202787453d.videoinfo group by resolution",
            "视频分辨率",
        )
    if obj.get("optype") == "videoinfo.resolution_line":
        res = get_line(
            "select resolution x,count(*) y from vm790_bcfe8a202787453d.videoinfo group by resolution",
            "视频分辨率",
        )
    if obj.get("optype") == "videoinfo.resolution_bar":
        res = get_bar(
            "select resolution x,count(*) y from vm790_bcfe8a202787453d.videoinfo group by resolution",
            "视频分辨率",
        )
    if obj.get("optype") == "videoinfo.resolution_bar_v1":
        res = get_bar_v1(
            "select resolution x,count(*) y from vm790_bcfe8a202787453d.videoinfo group by resolution",
            "视频分辨率",
        )
    # videoinfo(视频信息表)->filetype(文件类型)

    if obj.get("optype") == "videoinfo.filetype_pie":
        res = get_pie(
            "select filetype x,count(*) y from vm790_bcfe8a202787453d.videoinfo group by filetype order by x desc",
            "文件类型",
        )
    if obj.get("optype") == "videoinfo.filetype_pie_v1":
        res = get_pie_v1(
            "select filetype x,count(*) y from vm790_bcfe8a202787453d.videoinfo group by filetype",
            "文件类型",
        )
    if obj.get("optype") == "videoinfo.filetype_pie_v2":
        res = get_pie_v2(
            "select filetype x,count(*) y from vm790_bcfe8a202787453d.videoinfo group by filetype",
            "文件类型",
        )
    if obj.get("optype") == "videoinfo.filetype_line":
        res = get_line(
            "select filetype x,count(*) y from vm790_bcfe8a202787453d.videoinfo group by filetype",
            "文件类型",
        )
    if obj.get("optype") == "videoinfo.filetype_bar":
        res = get_bar(
            "select filetype x,count(*) y from vm790_bcfe8a202787453d.videoinfo group by filetype",
            "文件类型",
        )
    if obj.get("optype") == "videoinfo.filetype_bar_v1":
        res = get_bar_v1(
            "select filetype x,count(*) y from vm790_bcfe8a202787453d.videoinfo group by filetype",
            "文件类型",
        )
    # videoinfo(视频信息表)->filesize(文件大小KBMBGB)

    if obj.get("optype") == "videoinfo.filesize_pie":
        res = get_pie(
            "select filesize x,count(*) y from vm790_bcfe8a202787453d.videoinfo group by filesize order by x desc",
            "文件大小KBMBGB",
        )
    if obj.get("optype") == "videoinfo.filesize_pie_v1":
        res = get_pie_v1(
            "select filesize x,count(*) y from vm790_bcfe8a202787453d.videoinfo group by filesize",
            "文件大小KBMBGB",
        )
    if obj.get("optype") == "videoinfo.filesize_pie_v2":
        res = get_pie_v2(
            "select filesize x,count(*) y from vm790_bcfe8a202787453d.videoinfo group by filesize",
            "文件大小KBMBGB",
        )
    if obj.get("optype") == "videoinfo.filesize_line":
        res = get_line(
            "select filesize x,count(*) y from vm790_bcfe8a202787453d.videoinfo group by filesize",
            "文件大小KBMBGB",
        )
    if obj.get("optype") == "videoinfo.filesize_bar":
        res = get_bar(
            "select filesize x,count(*) y from vm790_bcfe8a202787453d.videoinfo group by filesize",
            "文件大小KBMBGB",
        )
    if obj.get("optype") == "videoinfo.filesize_bar_v1":
        res = get_bar_v1(
            "select filesize x,count(*) y from vm790_bcfe8a202787453d.videoinfo group by filesize",
            "文件大小KBMBGB",
        )
    # videoinfo(视频信息表)->creatkwkworid(创建者ID关联用户)

    if obj.get("optype") == "videoinfo.creatkwkworid_pie":
        res = get_pie(
            "select creatkwkworid x,count(*) y from vm790_bcfe8a202787453d.videoinfo group by creatkwkworid order by x desc",
            "创建者ID关联用户",
        )
    if obj.get("optype") == "videoinfo.creatkwkworid_pie_v1":
        res = get_pie_v1(
            "select creatkwkworid x,count(*) y from vm790_bcfe8a202787453d.videoinfo group by creatkwkworid",
            "创建者ID关联用户",
        )
    if obj.get("optype") == "videoinfo.creatkwkworid_pie_v2":
        res = get_pie_v2(
            "select creatkwkworid x,count(*) y from vm790_bcfe8a202787453d.videoinfo group by creatkwkworid",
            "创建者ID关联用户",
        )
    if obj.get("optype") == "videoinfo.creatkwkworid_line":
        res = get_line(
            "select creatkwkworid x,count(*) y from vm790_bcfe8a202787453d.videoinfo group by creatkwkworid",
            "创建者ID关联用户",
        )
    if obj.get("optype") == "videoinfo.creatkwkworid_bar":
        res = get_bar(
            "select creatkwkworid x,count(*) y from vm790_bcfe8a202787453d.videoinfo group by creatkwkworid",
            "创建者ID关联用户",
        )
    if obj.get("optype") == "videoinfo.creatkwkworid_bar_v1":
        res = get_bar_v1(
            "select creatkwkworid x,count(*) y from vm790_bcfe8a202787453d.videoinfo group by creatkwkworid",
            "创建者ID关联用户",
        )
    # videoinfo(视频信息表)->categkwkworyid(类别ID关联视频类别)

    if obj.get("optype") == "videoinfo.categkwkworyid_pie":
        res = get_pie(
            "select categkwkworyid x,count(*) y from vm790_bcfe8a202787453d.videoinfo group by categkwkworyid order by x desc",
            "类别ID关联视频类别",
        )
    if obj.get("optype") == "videoinfo.categkwkworyid_pie_v1":
        res = get_pie_v1(
            "select categkwkworyid x,count(*) y from vm790_bcfe8a202787453d.videoinfo group by categkwkworyid",
            "类别ID关联视频类别",
        )
    if obj.get("optype") == "videoinfo.categkwkworyid_pie_v2":
        res = get_pie_v2(
            "select categkwkworyid x,count(*) y from vm790_bcfe8a202787453d.videoinfo group by categkwkworyid",
            "类别ID关联视频类别",
        )
    if obj.get("optype") == "videoinfo.categkwkworyid_line":
        res = get_line(
            "select categkwkworyid x,count(*) y from vm790_bcfe8a202787453d.videoinfo group by categkwkworyid",
            "类别ID关联视频类别",
        )
    if obj.get("optype") == "videoinfo.categkwkworyid_bar":
        res = get_bar(
            "select categkwkworyid x,count(*) y from vm790_bcfe8a202787453d.videoinfo group by categkwkworyid",
            "类别ID关联视频类别",
        )
    if obj.get("optype") == "videoinfo.categkwkworyid_bar_v1":
        res = get_bar_v1(
            "select categkwkworyid x,count(*) y from vm790_bcfe8a202787453d.videoinfo group by categkwkworyid",
            "类别ID关联视频类别",
        )
    # videocategkwkwory(视频分类表)->name(分类名称)

    if obj.get("optype") == "videocategkwkwory.name_pie":
        res = get_pie(
            "select name x,count(*) y from vm790_bcfe8a202787453d.videocategkwkwory group by name order by x desc",
            "分类名称",
        )
    if obj.get("optype") == "videocategkwkwory.name_pie_v1":
        res = get_pie_v1(
            "select name x,count(*) y from vm790_bcfe8a202787453d.videocategkwkwory group by name",
            "分类名称",
        )
    if obj.get("optype") == "videocategkwkwory.name_pie_v2":
        res = get_pie_v2(
            "select name x,count(*) y from vm790_bcfe8a202787453d.videocategkwkwory group by name",
            "分类名称",
        )
    if obj.get("optype") == "videocategkwkwory.name_line":
        res = get_line(
            "select name x,count(*) y from vm790_bcfe8a202787453d.videocategkwkwory group by name",
            "分类名称",
        )
    if obj.get("optype") == "videocategkwkwory.name_bar":
        res = get_bar(
            "select name x,count(*) y from vm790_bcfe8a202787453d.videocategkwkwory group by name",
            "分类名称",
        )
    if obj.get("optype") == "videocategkwkwory.name_bar_v1":
        res = get_bar_v1(
            "select name x,count(*) y from vm790_bcfe8a202787453d.videocategkwkwory group by name",
            "分类名称",
        )
    if obj.get("optype") == "videocategkwkwory.description_wordcloud":
        textlist = get_data(
            "SELECT description result FROM vm790_bcfe8a202787453d.videocategkwkwory;"
        )
        res = {
            "title": "词云图",
            "imgbs64": generate_wordcloud_base64(
                ",".join([t["result"] for t in textlist])
            ),
        }
    # videocategkwkwory(视频分类表)->parentid(父分类ID用于构建分类层级如果为顶级分类则为NULL)

    if obj.get("optype") == "videocategkwkwory.parentid_pie":
        res = get_pie(
            "select parentid x,count(*) y from vm790_bcfe8a202787453d.videocategkwkwory group by parentid order by x desc",
            "父分类ID用于构建分类层级如果为顶级分类则为NULL",
        )
    if obj.get("optype") == "videocategkwkwory.parentid_pie_v1":
        res = get_pie_v1(
            "select parentid x,count(*) y from vm790_bcfe8a202787453d.videocategkwkwory group by parentid",
            "父分类ID用于构建分类层级如果为顶级分类则为NULL",
        )
    if obj.get("optype") == "videocategkwkwory.parentid_pie_v2":
        res = get_pie_v2(
            "select parentid x,count(*) y from vm790_bcfe8a202787453d.videocategkwkwory group by parentid",
            "父分类ID用于构建分类层级如果为顶级分类则为NULL",
        )
    if obj.get("optype") == "videocategkwkwory.parentid_line":
        res = get_line(
            "select parentid x,count(*) y from vm790_bcfe8a202787453d.videocategkwkwory group by parentid",
            "父分类ID用于构建分类层级如果为顶级分类则为NULL",
        )
    if obj.get("optype") == "videocategkwkwory.parentid_bar":
        res = get_bar(
            "select parentid x,count(*) y from vm790_bcfe8a202787453d.videocategkwkwory group by parentid",
            "父分类ID用于构建分类层级如果为顶级分类则为NULL",
        )
    if obj.get("optype") == "videocategkwkwory.parentid_bar_v1":
        res = get_bar_v1(
            "select parentid x,count(*) y from vm790_bcfe8a202787453d.videocategkwkwory group by parentid",
            "父分类ID用于构建分类层级如果为顶级分类则为NULL",
        )
    if obj.get("optype") == "videocategkwkwory.createtime_line":
        res = get_line(
            "select createtime x,count(*) y from vm790_bcfe8a202787453d.videocategkwkwory group by createtime order by x",
            "创建时间",
        )
    if obj.get("optype") == "videocategkwkwory.updatetime_line":
        res = get_line(
            "select updatetime x,count(*) y from vm790_bcfe8a202787453d.videocategkwkwory group by updatetime order by x",
            "更新时间",
        )
    # videocategkwkwory(视频分类表)->kwkwisactive(是否激活用于控制分类是否显示在前端)

    if obj.get("optype") == "videocategkwkwory.kwkwisactive_pie":
        res = get_pie(
            "select kwkwisactive x,count(*) y from vm790_bcfe8a202787453d.videocategkwkwory group by kwkwisactive order by x desc",
            "是否激活用于控制分类是否显示在前端",
        )
    if obj.get("optype") == "videocategkwkwory.kwkwisactive_pie_v1":
        res = get_pie_v1(
            "select kwkwisactive x,count(*) y from vm790_bcfe8a202787453d.videocategkwkwory group by kwkwisactive",
            "是否激活用于控制分类是否显示在前端",
        )
    if obj.get("optype") == "videocategkwkwory.kwkwisactive_pie_v2":
        res = get_pie_v2(
            "select kwkwisactive x,count(*) y from vm790_bcfe8a202787453d.videocategkwkwory group by kwkwisactive",
            "是否激活用于控制分类是否显示在前端",
        )
    if obj.get("optype") == "videocategkwkwory.kwkwisactive_line":
        res = get_line(
            "select kwkwisactive x,count(*) y from vm790_bcfe8a202787453d.videocategkwkwory group by kwkwisactive",
            "是否激活用于控制分类是否显示在前端",
        )
    if obj.get("optype") == "videocategkwkwory.kwkwisactive_bar":
        res = get_bar(
            "select kwkwisactive x,count(*) y from vm790_bcfe8a202787453d.videocategkwkwory group by kwkwisactive",
            "是否激活用于控制分类是否显示在前端",
        )
    if obj.get("optype") == "videocategkwkwory.kwkwisactive_bar_v1":
        res = get_bar_v1(
            "select kwkwisactive x,count(*) y from vm790_bcfe8a202787453d.videocategkwkwory group by kwkwisactive",
            "是否激活用于控制分类是否显示在前端",
        )
    # videocategkwkwory(视频分类表)->skwkwortorder(排序顺序)

    if obj.get("optype") == "videocategkwkwory.skwkwortorder_pie":
        res = get_pie(
            "select skwkwortorder x,count(*) y from vm790_bcfe8a202787453d.videocategkwkwory group by skwkwortorder order by x desc",
            "排序顺序",
        )
    if obj.get("optype") == "videocategkwkwory.skwkwortorder_pie_v1":
        res = get_pie_v1(
            "select skwkwortorder x,count(*) y from vm790_bcfe8a202787453d.videocategkwkwory group by skwkwortorder",
            "排序顺序",
        )
    if obj.get("optype") == "videocategkwkwory.skwkwortorder_pie_v2":
        res = get_pie_v2(
            "select skwkwortorder x,count(*) y from vm790_bcfe8a202787453d.videocategkwkwory group by skwkwortorder",
            "排序顺序",
        )
    if obj.get("optype") == "videocategkwkwory.skwkwortorder_line":
        res = get_line(
            "select skwkwortorder x,count(*) y from vm790_bcfe8a202787453d.videocategkwkwory group by skwkwortorder",
            "排序顺序",
        )
    if obj.get("optype") == "videocategkwkwory.skwkwortorder_bar":
        res = get_bar(
            "select skwkwortorder x,count(*) y from vm790_bcfe8a202787453d.videocategkwkwory group by skwkwortorder",
            "排序顺序",
        )
    if obj.get("optype") == "videocategkwkwory.skwkwortorder_bar_v1":
        res = get_bar_v1(
            "select skwkwortorder x,count(*) y from vm790_bcfe8a202787453d.videocategkwkwory group by skwkwortorder",
            "排序顺序",
        )
    # videotag(视频标签表)->tagid(标签ID)

    if obj.get("optype") == "videotag.tagid_pie":
        res = get_pie(
            "select tagid x,count(*) y from vm790_bcfe8a202787453d.videotag group by tagid order by x desc",
            "标签ID",
        )
    if obj.get("optype") == "videotag.tagid_pie_v1":
        res = get_pie_v1(
            "select tagid x,count(*) y from vm790_bcfe8a202787453d.videotag group by tagid",
            "标签ID",
        )
    if obj.get("optype") == "videotag.tagid_pie_v2":
        res = get_pie_v2(
            "select tagid x,count(*) y from vm790_bcfe8a202787453d.videotag group by tagid",
            "标签ID",
        )
    if obj.get("optype") == "videotag.tagid_line":
        res = get_line(
            "select tagid x,count(*) y from vm790_bcfe8a202787453d.videotag group by tagid",
            "标签ID",
        )
    if obj.get("optype") == "videotag.tagid_bar":
        res = get_bar(
            "select tagid x,count(*) y from vm790_bcfe8a202787453d.videotag group by tagid",
            "标签ID",
        )
    if obj.get("optype") == "videotag.tagid_bar_v1":
        res = get_bar_v1(
            "select tagid x,count(*) y from vm790_bcfe8a202787453d.videotag group by tagid",
            "标签ID",
        )
    # videotag(视频标签表)->tagname(标签名称)

    if obj.get("optype") == "videotag.tagname_pie":
        res = get_pie(
            "select tagname x,count(*) y from vm790_bcfe8a202787453d.videotag group by tagname order by x desc",
            "标签名称",
        )
    if obj.get("optype") == "videotag.tagname_pie_v1":
        res = get_pie_v1(
            "select tagname x,count(*) y from vm790_bcfe8a202787453d.videotag group by tagname",
            "标签名称",
        )
    if obj.get("optype") == "videotag.tagname_pie_v2":
        res = get_pie_v2(
            "select tagname x,count(*) y from vm790_bcfe8a202787453d.videotag group by tagname",
            "标签名称",
        )
    if obj.get("optype") == "videotag.tagname_line":
        res = get_line(
            "select tagname x,count(*) y from vm790_bcfe8a202787453d.videotag group by tagname",
            "标签名称",
        )
    if obj.get("optype") == "videotag.tagname_bar":
        res = get_bar(
            "select tagname x,count(*) y from vm790_bcfe8a202787453d.videotag group by tagname",
            "标签名称",
        )
    if obj.get("optype") == "videotag.tagname_bar_v1":
        res = get_bar_v1(
            "select tagname x,count(*) y from vm790_bcfe8a202787453d.videotag group by tagname",
            "标签名称",
        )
    # videotag(视频标签表)->videoid(视频ID关联字段指向视频中的视频ID)

    if obj.get("optype") == "videotag.videoid_pie":
        res = get_pie(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videotag group by videoid order by x desc",
            "视频ID关联字段指向视频中的视频ID",
        )
    if obj.get("optype") == "videotag.videoid_pie_v1":
        res = get_pie_v1(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videotag group by videoid",
            "视频ID关联字段指向视频中的视频ID",
        )
    if obj.get("optype") == "videotag.videoid_pie_v2":
        res = get_pie_v2(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videotag group by videoid",
            "视频ID关联字段指向视频中的视频ID",
        )
    if obj.get("optype") == "videotag.videoid_line":
        res = get_line(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videotag group by videoid",
            "视频ID关联字段指向视频中的视频ID",
        )
    if obj.get("optype") == "videotag.videoid_bar":
        res = get_bar(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videotag group by videoid",
            "视频ID关联字段指向视频中的视频ID",
        )
    if obj.get("optype") == "videotag.videoid_bar_v1":
        res = get_bar_v1(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videotag group by videoid",
            "视频ID关联字段指向视频中的视频ID",
        )
    if obj.get("optype") == "videotag.createtime_line":
        res = get_line(
            "select createtime x,count(*) y from vm790_bcfe8a202787453d.videotag group by createtime order by x",
            "创建时间",
        )
    if obj.get("optype") == "videotag.updatetime_line":
        res = get_line(
            "select updatetime x,count(*) y from vm790_bcfe8a202787453d.videotag group by updatetime order by x",
            "更新时间",
        )
    # videotag(视频标签表)->kwkwisactive(是否激活用于标记标签是否可用)

    if obj.get("optype") == "videotag.kwkwisactive_pie":
        res = get_pie(
            "select kwkwisactive x,count(*) y from vm790_bcfe8a202787453d.videotag group by kwkwisactive order by x desc",
            "是否激活用于标记标签是否可用",
        )
    if obj.get("optype") == "videotag.kwkwisactive_pie_v1":
        res = get_pie_v1(
            "select kwkwisactive x,count(*) y from vm790_bcfe8a202787453d.videotag group by kwkwisactive",
            "是否激活用于标记标签是否可用",
        )
    if obj.get("optype") == "videotag.kwkwisactive_pie_v2":
        res = get_pie_v2(
            "select kwkwisactive x,count(*) y from vm790_bcfe8a202787453d.videotag group by kwkwisactive",
            "是否激活用于标记标签是否可用",
        )
    if obj.get("optype") == "videotag.kwkwisactive_line":
        res = get_line(
            "select kwkwisactive x,count(*) y from vm790_bcfe8a202787453d.videotag group by kwkwisactive",
            "是否激活用于标记标签是否可用",
        )
    if obj.get("optype") == "videotag.kwkwisactive_bar":
        res = get_bar(
            "select kwkwisactive x,count(*) y from vm790_bcfe8a202787453d.videotag group by kwkwisactive",
            "是否激活用于标记标签是否可用",
        )
    if obj.get("optype") == "videotag.kwkwisactive_bar_v1":
        res = get_bar_v1(
            "select kwkwisactive x,count(*) y from vm790_bcfe8a202787453d.videotag group by kwkwisactive",
            "是否激活用于标记标签是否可用",
        )
    if obj.get("optype") == "videotag.description_wordcloud":
        textlist = get_data(
            "SELECT description result FROM vm790_bcfe8a202787453d.videotag;"
        )
        res = {
            "title": "词云图",
            "imgbs64": generate_wordcloud_base64(
                ",".join([t["result"] for t in textlist])
            ),
        }
    # videotag(视频标签表)->creatkwkworid(创建者ID关联字段指向用户中的用户ID)

    if obj.get("optype") == "videotag.creatkwkworid_pie":
        res = get_pie(
            "select creatkwkworid x,count(*) y from vm790_bcfe8a202787453d.videotag group by creatkwkworid order by x desc",
            "创建者ID关联字段指向用户中的用户ID",
        )
    if obj.get("optype") == "videotag.creatkwkworid_pie_v1":
        res = get_pie_v1(
            "select creatkwkworid x,count(*) y from vm790_bcfe8a202787453d.videotag group by creatkwkworid",
            "创建者ID关联字段指向用户中的用户ID",
        )
    if obj.get("optype") == "videotag.creatkwkworid_pie_v2":
        res = get_pie_v2(
            "select creatkwkworid x,count(*) y from vm790_bcfe8a202787453d.videotag group by creatkwkworid",
            "创建者ID关联字段指向用户中的用户ID",
        )
    if obj.get("optype") == "videotag.creatkwkworid_line":
        res = get_line(
            "select creatkwkworid x,count(*) y from vm790_bcfe8a202787453d.videotag group by creatkwkworid",
            "创建者ID关联字段指向用户中的用户ID",
        )
    if obj.get("optype") == "videotag.creatkwkworid_bar":
        res = get_bar(
            "select creatkwkworid x,count(*) y from vm790_bcfe8a202787453d.videotag group by creatkwkworid",
            "创建者ID关联字段指向用户中的用户ID",
        )
    if obj.get("optype") == "videotag.creatkwkworid_bar_v1":
        res = get_bar_v1(
            "select creatkwkworid x,count(*) y from vm790_bcfe8a202787453d.videotag group by creatkwkworid",
            "创建者ID关联字段指向用户中的用户ID",
        )
    # videofilestkwkworage(视频文件存储表)->videoid(视频ID)

    if obj.get("optype") == "videofilestkwkworage.videoid_pie":
        res = get_pie(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videofilestkwkworage group by videoid order by x desc",
            "视频ID",
        )
    if obj.get("optype") == "videofilestkwkworage.videoid_pie_v1":
        res = get_pie_v1(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videofilestkwkworage group by videoid",
            "视频ID",
        )
    if obj.get("optype") == "videofilestkwkworage.videoid_pie_v2":
        res = get_pie_v2(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videofilestkwkworage group by videoid",
            "视频ID",
        )
    if obj.get("optype") == "videofilestkwkworage.videoid_line":
        res = get_line(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videofilestkwkworage group by videoid",
            "视频ID",
        )
    if obj.get("optype") == "videofilestkwkworage.videoid_bar":
        res = get_bar(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videofilestkwkworage group by videoid",
            "视频ID",
        )
    if obj.get("optype") == "videofilestkwkworage.videoid_bar_v1":
        res = get_bar_v1(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videofilestkwkworage group by videoid",
            "视频ID",
        )
    # videofilestkwkworage(视频文件存储表)->filename(文件名)

    if obj.get("optype") == "videofilestkwkworage.filename_pie":
        res = get_pie(
            "select filename x,count(*) y from vm790_bcfe8a202787453d.videofilestkwkworage group by filename order by x desc",
            "文件名",
        )
    if obj.get("optype") == "videofilestkwkworage.filename_pie_v1":
        res = get_pie_v1(
            "select filename x,count(*) y from vm790_bcfe8a202787453d.videofilestkwkworage group by filename",
            "文件名",
        )
    if obj.get("optype") == "videofilestkwkworage.filename_pie_v2":
        res = get_pie_v2(
            "select filename x,count(*) y from vm790_bcfe8a202787453d.videofilestkwkworage group by filename",
            "文件名",
        )
    if obj.get("optype") == "videofilestkwkworage.filename_line":
        res = get_line(
            "select filename x,count(*) y from vm790_bcfe8a202787453d.videofilestkwkworage group by filename",
            "文件名",
        )
    if obj.get("optype") == "videofilestkwkworage.filename_bar":
        res = get_bar(
            "select filename x,count(*) y from vm790_bcfe8a202787453d.videofilestkwkworage group by filename",
            "文件名",
        )
    if obj.get("optype") == "videofilestkwkworage.filename_bar_v1":
        res = get_bar_v1(
            "select filename x,count(*) y from vm790_bcfe8a202787453d.videofilestkwkworage group by filename",
            "文件名",
        )
    # videofilestkwkworage(视频文件存储表)->filepath(文件存储路径)

    if obj.get("optype") == "videofilestkwkworage.filepath_pie":
        res = get_pie(
            "select filepath x,count(*) y from vm790_bcfe8a202787453d.videofilestkwkworage group by filepath order by x desc",
            "文件存储路径",
        )
    if obj.get("optype") == "videofilestkwkworage.filepath_pie_v1":
        res = get_pie_v1(
            "select filepath x,count(*) y from vm790_bcfe8a202787453d.videofilestkwkworage group by filepath",
            "文件存储路径",
        )
    if obj.get("optype") == "videofilestkwkworage.filepath_pie_v2":
        res = get_pie_v2(
            "select filepath x,count(*) y from vm790_bcfe8a202787453d.videofilestkwkworage group by filepath",
            "文件存储路径",
        )
    if obj.get("optype") == "videofilestkwkworage.filepath_line":
        res = get_line(
            "select filepath x,count(*) y from vm790_bcfe8a202787453d.videofilestkwkworage group by filepath",
            "文件存储路径",
        )
    if obj.get("optype") == "videofilestkwkworage.filepath_bar":
        res = get_bar(
            "select filepath x,count(*) y from vm790_bcfe8a202787453d.videofilestkwkworage group by filepath",
            "文件存储路径",
        )
    if obj.get("optype") == "videofilestkwkworage.filepath_bar_v1":
        res = get_bar_v1(
            "select filepath x,count(*) y from vm790_bcfe8a202787453d.videofilestkwkworage group by filepath",
            "文件存储路径",
        )
    # videofilestkwkworage(视频文件存储表)->filesize(文件大小单位MB)

    if obj.get("optype") == "videofilestkwkworage.filesize_pie":
        res = get_pie(
            "select filesize x,count(*) y from vm790_bcfe8a202787453d.videofilestkwkworage group by filesize order by x desc",
            "文件大小单位MB",
        )
    if obj.get("optype") == "videofilestkwkworage.filesize_pie_v1":
        res = get_pie_v1(
            "select filesize x,count(*) y from vm790_bcfe8a202787453d.videofilestkwkworage group by filesize",
            "文件大小单位MB",
        )
    if obj.get("optype") == "videofilestkwkworage.filesize_pie_v2":
        res = get_pie_v2(
            "select filesize x,count(*) y from vm790_bcfe8a202787453d.videofilestkwkworage group by filesize",
            "文件大小单位MB",
        )
    if obj.get("optype") == "videofilestkwkworage.filesize_line":
        res = get_line(
            "select filesize x,count(*) y from vm790_bcfe8a202787453d.videofilestkwkworage group by filesize",
            "文件大小单位MB",
        )
    if obj.get("optype") == "videofilestkwkworage.filesize_bar":
        res = get_bar(
            "select filesize x,count(*) y from vm790_bcfe8a202787453d.videofilestkwkworage group by filesize",
            "文件大小单位MB",
        )
    if obj.get("optype") == "videofilestkwkworage.filesize_bar_v1":
        res = get_bar_v1(
            "select filesize x,count(*) y from vm790_bcfe8a202787453d.videofilestkwkworage group by filesize",
            "文件大小单位MB",
        )
    if obj.get("optype") == "videofilestkwkworage.uploadtime_line":
        res = get_line(
            "select uploadtime x,count(*) y from vm790_bcfe8a202787453d.videofilestkwkworage group by uploadtime order by x",
            "上传时间",
        )
    # videofilestkwkworage(视频文件存储表)->duration(视频时长单位秒)

    if obj.get("optype") == "videofilestkwkworage.duration_pie":
        res = get_pie(
            "select duration x,count(*) y from vm790_bcfe8a202787453d.videofilestkwkworage group by duration order by x desc",
            "视频时长单位秒",
        )
    if obj.get("optype") == "videofilestkwkworage.duration_pie_v1":
        res = get_pie_v1(
            "select duration x,count(*) y from vm790_bcfe8a202787453d.videofilestkwkworage group by duration",
            "视频时长单位秒",
        )
    if obj.get("optype") == "videofilestkwkworage.duration_pie_v2":
        res = get_pie_v2(
            "select duration x,count(*) y from vm790_bcfe8a202787453d.videofilestkwkworage group by duration",
            "视频时长单位秒",
        )
    if obj.get("optype") == "videofilestkwkworage.duration_line":
        res = get_line(
            "select duration x,count(*) y from vm790_bcfe8a202787453d.videofilestkwkworage group by duration",
            "视频时长单位秒",
        )
    if obj.get("optype") == "videofilestkwkworage.duration_bar":
        res = get_bar(
            "select duration x,count(*) y from vm790_bcfe8a202787453d.videofilestkwkworage group by duration",
            "视频时长单位秒",
        )
    if obj.get("optype") == "videofilestkwkworage.duration_bar_v1":
        res = get_bar_v1(
            "select duration x,count(*) y from vm790_bcfe8a202787453d.videofilestkwkworage group by duration",
            "视频时长单位秒",
        )
    # videofilestkwkworage(视频文件存储表)->resolution(分辨率例如1920x1080)

    if obj.get("optype") == "videofilestkwkworage.resolution_pie":
        res = get_pie(
            "select resolution x,count(*) y from vm790_bcfe8a202787453d.videofilestkwkworage group by resolution order by x desc",
            "分辨率例如1920x1080",
        )
    if obj.get("optype") == "videofilestkwkworage.resolution_pie_v1":
        res = get_pie_v1(
            "select resolution x,count(*) y from vm790_bcfe8a202787453d.videofilestkwkworage group by resolution",
            "分辨率例如1920x1080",
        )
    if obj.get("optype") == "videofilestkwkworage.resolution_pie_v2":
        res = get_pie_v2(
            "select resolution x,count(*) y from vm790_bcfe8a202787453d.videofilestkwkworage group by resolution",
            "分辨率例如1920x1080",
        )
    if obj.get("optype") == "videofilestkwkworage.resolution_line":
        res = get_line(
            "select resolution x,count(*) y from vm790_bcfe8a202787453d.videofilestkwkworage group by resolution",
            "分辨率例如1920x1080",
        )
    if obj.get("optype") == "videofilestkwkworage.resolution_bar":
        res = get_bar(
            "select resolution x,count(*) y from vm790_bcfe8a202787453d.videofilestkwkworage group by resolution",
            "分辨率例如1920x1080",
        )
    if obj.get("optype") == "videofilestkwkworage.resolution_bar_v1":
        res = get_bar_v1(
            "select resolution x,count(*) y from vm790_bcfe8a202787453d.videofilestkwkworage group by resolution",
            "分辨率例如1920x1080",
        )
    # videofilestkwkworage(视频文件存储表)->kwkwfkwkwormat(视频格式例如mp4)

    if obj.get("optype") == "videofilestkwkworage.kwkwfkwkwormat_pie":
        res = get_pie(
            "select kwkwfkwkwormat x,count(*) y from vm790_bcfe8a202787453d.videofilestkwkworage group by kwkwfkwkwormat order by x desc",
            "视频格式例如mp4",
        )
    if obj.get("optype") == "videofilestkwkworage.kwkwfkwkwormat_pie_v1":
        res = get_pie_v1(
            "select kwkwfkwkwormat x,count(*) y from vm790_bcfe8a202787453d.videofilestkwkworage group by kwkwfkwkwormat",
            "视频格式例如mp4",
        )
    if obj.get("optype") == "videofilestkwkworage.kwkwfkwkwormat_pie_v2":
        res = get_pie_v2(
            "select kwkwfkwkwormat x,count(*) y from vm790_bcfe8a202787453d.videofilestkwkworage group by kwkwfkwkwormat",
            "视频格式例如mp4",
        )
    if obj.get("optype") == "videofilestkwkworage.kwkwfkwkwormat_line":
        res = get_line(
            "select kwkwfkwkwormat x,count(*) y from vm790_bcfe8a202787453d.videofilestkwkworage group by kwkwfkwkwormat",
            "视频格式例如mp4",
        )
    if obj.get("optype") == "videofilestkwkworage.kwkwfkwkwormat_bar":
        res = get_bar(
            "select kwkwfkwkwormat x,count(*) y from vm790_bcfe8a202787453d.videofilestkwkworage group by kwkwfkwkwormat",
            "视频格式例如mp4",
        )
    if obj.get("optype") == "videofilestkwkworage.kwkwfkwkwormat_bar_v1":
        res = get_bar_v1(
            "select kwkwfkwkwormat x,count(*) y from vm790_bcfe8a202787453d.videofilestkwkworage group by kwkwfkwkwormat",
            "视频格式例如mp4",
        )
    # videofilestkwkworage(视频文件存储表)->creatkwkworid(创建者ID关联用户)

    if obj.get("optype") == "videofilestkwkworage.creatkwkworid_pie":
        res = get_pie(
            "select creatkwkworid x,count(*) y from vm790_bcfe8a202787453d.videofilestkwkworage group by creatkwkworid order by x desc",
            "创建者ID关联用户",
        )
    if obj.get("optype") == "videofilestkwkworage.creatkwkworid_pie_v1":
        res = get_pie_v1(
            "select creatkwkworid x,count(*) y from vm790_bcfe8a202787453d.videofilestkwkworage group by creatkwkworid",
            "创建者ID关联用户",
        )
    if obj.get("optype") == "videofilestkwkworage.creatkwkworid_pie_v2":
        res = get_pie_v2(
            "select creatkwkworid x,count(*) y from vm790_bcfe8a202787453d.videofilestkwkworage group by creatkwkworid",
            "创建者ID关联用户",
        )
    if obj.get("optype") == "videofilestkwkworage.creatkwkworid_line":
        res = get_line(
            "select creatkwkworid x,count(*) y from vm790_bcfe8a202787453d.videofilestkwkworage group by creatkwkworid",
            "创建者ID关联用户",
        )
    if obj.get("optype") == "videofilestkwkworage.creatkwkworid_bar":
        res = get_bar(
            "select creatkwkworid x,count(*) y from vm790_bcfe8a202787453d.videofilestkwkworage group by creatkwkworid",
            "创建者ID关联用户",
        )
    if obj.get("optype") == "videofilestkwkworage.creatkwkworid_bar_v1":
        res = get_bar_v1(
            "select creatkwkworid x,count(*) y from vm790_bcfe8a202787453d.videofilestkwkworage group by creatkwkworid",
            "创建者ID关联用户",
        )
    # videofilestkwkworage(视频文件存储表)->categkwkworyid(分类ID关联视频分类)

    if obj.get("optype") == "videofilestkwkworage.categkwkworyid_pie":
        res = get_pie(
            "select categkwkworyid x,count(*) y from vm790_bcfe8a202787453d.videofilestkwkworage group by categkwkworyid order by x desc",
            "分类ID关联视频分类",
        )
    if obj.get("optype") == "videofilestkwkworage.categkwkworyid_pie_v1":
        res = get_pie_v1(
            "select categkwkworyid x,count(*) y from vm790_bcfe8a202787453d.videofilestkwkworage group by categkwkworyid",
            "分类ID关联视频分类",
        )
    if obj.get("optype") == "videofilestkwkworage.categkwkworyid_pie_v2":
        res = get_pie_v2(
            "select categkwkworyid x,count(*) y from vm790_bcfe8a202787453d.videofilestkwkworage group by categkwkworyid",
            "分类ID关联视频分类",
        )
    if obj.get("optype") == "videofilestkwkworage.categkwkworyid_line":
        res = get_line(
            "select categkwkworyid x,count(*) y from vm790_bcfe8a202787453d.videofilestkwkworage group by categkwkworyid",
            "分类ID关联视频分类",
        )
    if obj.get("optype") == "videofilestkwkworage.categkwkworyid_bar":
        res = get_bar(
            "select categkwkworyid x,count(*) y from vm790_bcfe8a202787453d.videofilestkwkworage group by categkwkworyid",
            "分类ID关联视频分类",
        )
    if obj.get("optype") == "videofilestkwkworage.categkwkworyid_bar_v1":
        res = get_bar_v1(
            "select categkwkworyid x,count(*) y from vm790_bcfe8a202787453d.videofilestkwkworage group by categkwkworyid",
            "分类ID关联视频分类",
        )
    # videoplayreckwkword(视频播放记录表)->videoid(视频ID关联视频信息)

    if obj.get("optype") == "videoplayreckwkword.videoid_pie":
        res = get_pie(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videoplayreckwkword group by videoid order by x desc",
            "视频ID关联视频信息",
        )
    if obj.get("optype") == "videoplayreckwkword.videoid_pie_v1":
        res = get_pie_v1(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videoplayreckwkword group by videoid",
            "视频ID关联视频信息",
        )
    if obj.get("optype") == "videoplayreckwkword.videoid_pie_v2":
        res = get_pie_v2(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videoplayreckwkword group by videoid",
            "视频ID关联视频信息",
        )
    if obj.get("optype") == "videoplayreckwkword.videoid_line":
        res = get_line(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videoplayreckwkword group by videoid",
            "视频ID关联视频信息",
        )
    if obj.get("optype") == "videoplayreckwkword.videoid_bar":
        res = get_bar(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videoplayreckwkword group by videoid",
            "视频ID关联视频信息",
        )
    if obj.get("optype") == "videoplayreckwkword.videoid_bar_v1":
        res = get_bar_v1(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videoplayreckwkword group by videoid",
            "视频ID关联视频信息",
        )
    # videoplayreckwkword(视频播放记录表)->userid(用户ID关联用户信息)

    if obj.get("optype") == "videoplayreckwkword.userid_pie":
        res = get_pie(
            "select userid x,count(*) y from vm790_bcfe8a202787453d.videoplayreckwkword group by userid order by x desc",
            "用户ID关联用户信息",
        )
    if obj.get("optype") == "videoplayreckwkword.userid_pie_v1":
        res = get_pie_v1(
            "select userid x,count(*) y from vm790_bcfe8a202787453d.videoplayreckwkword group by userid",
            "用户ID关联用户信息",
        )
    if obj.get("optype") == "videoplayreckwkword.userid_pie_v2":
        res = get_pie_v2(
            "select userid x,count(*) y from vm790_bcfe8a202787453d.videoplayreckwkword group by userid",
            "用户ID关联用户信息",
        )
    if obj.get("optype") == "videoplayreckwkword.userid_line":
        res = get_line(
            "select userid x,count(*) y from vm790_bcfe8a202787453d.videoplayreckwkword group by userid",
            "用户ID关联用户信息",
        )
    if obj.get("optype") == "videoplayreckwkword.userid_bar":
        res = get_bar(
            "select userid x,count(*) y from vm790_bcfe8a202787453d.videoplayreckwkword group by userid",
            "用户ID关联用户信息",
        )
    if obj.get("optype") == "videoplayreckwkword.userid_bar_v1":
        res = get_bar_v1(
            "select userid x,count(*) y from vm790_bcfe8a202787453d.videoplayreckwkword group by userid",
            "用户ID关联用户信息",
        )
    if obj.get("optype") == "videoplayreckwkword.playstarttime_line":
        res = get_line(
            "select playstarttime x,count(*) y from vm790_bcfe8a202787453d.videoplayreckwkword group by playstarttime order by x",
            "播放开始时间",
        )
    if obj.get("optype") == "videoplayreckwkword.playendtime_line":
        res = get_line(
            "select playendtime x,count(*) y from vm790_bcfe8a202787453d.videoplayreckwkword group by playendtime order by x",
            "播放结束时间",
        )
    # videoplayreckwkword(视频播放记录表)->playduration(播放时长秒)

    if obj.get("optype") == "videoplayreckwkword.playduration_pie":
        res = get_pie(
            "select playduration x,count(*) y from vm790_bcfe8a202787453d.videoplayreckwkword group by playduration order by x desc",
            "播放时长秒",
        )
    if obj.get("optype") == "videoplayreckwkword.playduration_pie_v1":
        res = get_pie_v1(
            "select playduration x,count(*) y from vm790_bcfe8a202787453d.videoplayreckwkword group by playduration",
            "播放时长秒",
        )
    if obj.get("optype") == "videoplayreckwkword.playduration_pie_v2":
        res = get_pie_v2(
            "select playduration x,count(*) y from vm790_bcfe8a202787453d.videoplayreckwkword group by playduration",
            "播放时长秒",
        )
    if obj.get("optype") == "videoplayreckwkword.playduration_line":
        res = get_line(
            "select playduration x,count(*) y from vm790_bcfe8a202787453d.videoplayreckwkword group by playduration",
            "播放时长秒",
        )
    if obj.get("optype") == "videoplayreckwkword.playduration_bar":
        res = get_bar(
            "select playduration x,count(*) y from vm790_bcfe8a202787453d.videoplayreckwkword group by playduration",
            "播放时长秒",
        )
    if obj.get("optype") == "videoplayreckwkword.playduration_bar_v1":
        res = get_bar_v1(
            "select playduration x,count(*) y from vm790_bcfe8a202787453d.videoplayreckwkword group by playduration",
            "播放时长秒",
        )
    # videoplayreckwkword(视频播放记录表)->playstatus(播放状态如已完成、暂停、中断)

    if obj.get("optype") == "videoplayreckwkword.playstatus_pie":
        res = get_pie(
            "select playstatus x,count(*) y from vm790_bcfe8a202787453d.videoplayreckwkword group by playstatus order by x desc",
            "播放状态如已完成、暂停、中断",
        )
    if obj.get("optype") == "videoplayreckwkword.playstatus_pie_v1":
        res = get_pie_v1(
            "select playstatus x,count(*) y from vm790_bcfe8a202787453d.videoplayreckwkword group by playstatus",
            "播放状态如已完成、暂停、中断",
        )
    if obj.get("optype") == "videoplayreckwkword.playstatus_pie_v2":
        res = get_pie_v2(
            "select playstatus x,count(*) y from vm790_bcfe8a202787453d.videoplayreckwkword group by playstatus",
            "播放状态如已完成、暂停、中断",
        )
    if obj.get("optype") == "videoplayreckwkword.playstatus_line":
        res = get_line(
            "select playstatus x,count(*) y from vm790_bcfe8a202787453d.videoplayreckwkword group by playstatus",
            "播放状态如已完成、暂停、中断",
        )
    if obj.get("optype") == "videoplayreckwkword.playstatus_bar":
        res = get_bar(
            "select playstatus x,count(*) y from vm790_bcfe8a202787453d.videoplayreckwkword group by playstatus",
            "播放状态如已完成、暂停、中断",
        )
    if obj.get("optype") == "videoplayreckwkword.playstatus_bar_v1":
        res = get_bar_v1(
            "select playstatus x,count(*) y from vm790_bcfe8a202787453d.videoplayreckwkword group by playstatus",
            "播放状态如已完成、暂停、中断",
        )
    # videoplayreckwkword(视频播放记录表)->devicetype(设备类型如手机、平板、电脑)

    if obj.get("optype") == "videoplayreckwkword.devicetype_pie":
        res = get_pie(
            "select devicetype x,count(*) y from vm790_bcfe8a202787453d.videoplayreckwkword group by devicetype order by x desc",
            "设备类型如手机、平板、电脑",
        )
    if obj.get("optype") == "videoplayreckwkword.devicetype_pie_v1":
        res = get_pie_v1(
            "select devicetype x,count(*) y from vm790_bcfe8a202787453d.videoplayreckwkword group by devicetype",
            "设备类型如手机、平板、电脑",
        )
    if obj.get("optype") == "videoplayreckwkword.devicetype_pie_v2":
        res = get_pie_v2(
            "select devicetype x,count(*) y from vm790_bcfe8a202787453d.videoplayreckwkword group by devicetype",
            "设备类型如手机、平板、电脑",
        )
    if obj.get("optype") == "videoplayreckwkword.devicetype_line":
        res = get_line(
            "select devicetype x,count(*) y from vm790_bcfe8a202787453d.videoplayreckwkword group by devicetype",
            "设备类型如手机、平板、电脑",
        )
    if obj.get("optype") == "videoplayreckwkword.devicetype_bar":
        res = get_bar(
            "select devicetype x,count(*) y from vm790_bcfe8a202787453d.videoplayreckwkword group by devicetype",
            "设备类型如手机、平板、电脑",
        )
    if obj.get("optype") == "videoplayreckwkword.devicetype_bar_v1":
        res = get_bar_v1(
            "select devicetype x,count(*) y from vm790_bcfe8a202787453d.videoplayreckwkword group by devicetype",
            "设备类型如手机、平板、电脑",
        )
    if obj.get("optype") == "videoplayreckwkword.ipaddress_wordcloud":
        textlist = get_data(
            "SELECT ipaddress result FROM vm790_bcfe8a202787453d.videoplayreckwkword;"
        )
        res = {
            "title": "词云图",
            "imgbs64": generate_wordcloud_base64(
                ",".join([t["result"] for t in textlist])
            ),
        }
    # videoplayreckwkword(视频播放记录表)->location(播放位置可选根据IP解析的地理位置)

    if obj.get("optype") == "videoplayreckwkword.location_pie":
        res = get_pie(
            "select location x,count(*) y from vm790_bcfe8a202787453d.videoplayreckwkword group by location order by x desc",
            "播放位置可选根据IP解析的地理位置",
        )
    if obj.get("optype") == "videoplayreckwkword.location_pie_v1":
        res = get_pie_v1(
            "select location x,count(*) y from vm790_bcfe8a202787453d.videoplayreckwkword group by location",
            "播放位置可选根据IP解析的地理位置",
        )
    if obj.get("optype") == "videoplayreckwkword.location_pie_v2":
        res = get_pie_v2(
            "select location x,count(*) y from vm790_bcfe8a202787453d.videoplayreckwkword group by location",
            "播放位置可选根据IP解析的地理位置",
        )
    if obj.get("optype") == "videoplayreckwkword.location_line":
        res = get_line(
            "select location x,count(*) y from vm790_bcfe8a202787453d.videoplayreckwkword group by location",
            "播放位置可选根据IP解析的地理位置",
        )
    if obj.get("optype") == "videoplayreckwkword.location_bar":
        res = get_bar(
            "select location x,count(*) y from vm790_bcfe8a202787453d.videoplayreckwkword group by location",
            "播放位置可选根据IP解析的地理位置",
        )
    if obj.get("optype") == "videoplayreckwkword.location_bar_v1":
        res = get_bar_v1(
            "select location x,count(*) y from vm790_bcfe8a202787453d.videoplayreckwkword group by location",
            "播放位置可选根据IP解析的地理位置",
        )
    # videocomment(视频评论表)->videoid(关联视频ID)

    if obj.get("optype") == "videocomment.videoid_pie":
        res = get_pie(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videocomment group by videoid order by x desc",
            "关联视频ID",
        )
    if obj.get("optype") == "videocomment.videoid_pie_v1":
        res = get_pie_v1(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videocomment group by videoid",
            "关联视频ID",
        )
    if obj.get("optype") == "videocomment.videoid_pie_v2":
        res = get_pie_v2(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videocomment group by videoid",
            "关联视频ID",
        )
    if obj.get("optype") == "videocomment.videoid_line":
        res = get_line(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videocomment group by videoid",
            "关联视频ID",
        )
    if obj.get("optype") == "videocomment.videoid_bar":
        res = get_bar(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videocomment group by videoid",
            "关联视频ID",
        )
    if obj.get("optype") == "videocomment.videoid_bar_v1":
        res = get_bar_v1(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videocomment group by videoid",
            "关联视频ID",
        )
    # videocomment(视频评论表)->userid(关联用户ID)

    if obj.get("optype") == "videocomment.userid_pie":
        res = get_pie(
            "select userid x,count(*) y from vm790_bcfe8a202787453d.videocomment group by userid order by x desc",
            "关联用户ID",
        )
    if obj.get("optype") == "videocomment.userid_pie_v1":
        res = get_pie_v1(
            "select userid x,count(*) y from vm790_bcfe8a202787453d.videocomment group by userid",
            "关联用户ID",
        )
    if obj.get("optype") == "videocomment.userid_pie_v2":
        res = get_pie_v2(
            "select userid x,count(*) y from vm790_bcfe8a202787453d.videocomment group by userid",
            "关联用户ID",
        )
    if obj.get("optype") == "videocomment.userid_line":
        res = get_line(
            "select userid x,count(*) y from vm790_bcfe8a202787453d.videocomment group by userid",
            "关联用户ID",
        )
    if obj.get("optype") == "videocomment.userid_bar":
        res = get_bar(
            "select userid x,count(*) y from vm790_bcfe8a202787453d.videocomment group by userid",
            "关联用户ID",
        )
    if obj.get("optype") == "videocomment.userid_bar_v1":
        res = get_bar_v1(
            "select userid x,count(*) y from vm790_bcfe8a202787453d.videocomment group by userid",
            "关联用户ID",
        )
    if obj.get("optype") == "videocomment.content_wordcloud":
        textlist = get_data(
            "SELECT content result FROM vm790_bcfe8a202787453d.videocomment;"
        )
        res = {
            "title": "词云图",
            "imgbs64": generate_wordcloud_base64(
                ",".join([t["result"] for t in textlist])
            ),
        }
    if obj.get("optype") == "videocomment.createtime_line":
        res = get_line(
            "select createtime x,count(*) y from vm790_bcfe8a202787453d.videocomment group by createtime order by x",
            "创建时间",
        )
    # videocomment(视频评论表)->likecount(点赞数)

    if obj.get("optype") == "videocomment.likecount_pie":
        res = get_pie(
            "select likecount x,count(*) y from vm790_bcfe8a202787453d.videocomment group by likecount order by x desc",
            "点赞数",
        )
    if obj.get("optype") == "videocomment.likecount_pie_v1":
        res = get_pie_v1(
            "select likecount x,count(*) y from vm790_bcfe8a202787453d.videocomment group by likecount",
            "点赞数",
        )
    if obj.get("optype") == "videocomment.likecount_pie_v2":
        res = get_pie_v2(
            "select likecount x,count(*) y from vm790_bcfe8a202787453d.videocomment group by likecount",
            "点赞数",
        )
    if obj.get("optype") == "videocomment.likecount_line":
        res = get_line(
            "select likecount x,count(*) y from vm790_bcfe8a202787453d.videocomment group by likecount",
            "点赞数",
        )
    if obj.get("optype") == "videocomment.likecount_bar":
        res = get_bar(
            "select likecount x,count(*) y from vm790_bcfe8a202787453d.videocomment group by likecount",
            "点赞数",
        )
    if obj.get("optype") == "videocomment.likecount_bar_v1":
        res = get_bar_v1(
            "select likecount x,count(*) y from vm790_bcfe8a202787453d.videocomment group by likecount",
            "点赞数",
        )
    # videocomment(视频评论表)->replycount(回复数)

    if obj.get("optype") == "videocomment.replycount_pie":
        res = get_pie(
            "select replycount x,count(*) y from vm790_bcfe8a202787453d.videocomment group by replycount order by x desc",
            "回复数",
        )
    if obj.get("optype") == "videocomment.replycount_pie_v1":
        res = get_pie_v1(
            "select replycount x,count(*) y from vm790_bcfe8a202787453d.videocomment group by replycount",
            "回复数",
        )
    if obj.get("optype") == "videocomment.replycount_pie_v2":
        res = get_pie_v2(
            "select replycount x,count(*) y from vm790_bcfe8a202787453d.videocomment group by replycount",
            "回复数",
        )
    if obj.get("optype") == "videocomment.replycount_line":
        res = get_line(
            "select replycount x,count(*) y from vm790_bcfe8a202787453d.videocomment group by replycount",
            "回复数",
        )
    if obj.get("optype") == "videocomment.replycount_bar":
        res = get_bar(
            "select replycount x,count(*) y from vm790_bcfe8a202787453d.videocomment group by replycount",
            "回复数",
        )
    if obj.get("optype") == "videocomment.replycount_bar_v1":
        res = get_bar_v1(
            "select replycount x,count(*) y from vm790_bcfe8a202787453d.videocomment group by replycount",
            "回复数",
        )
    # videocomment(视频评论表)->kwkwiskwkwdeleted(是否已删除)

    if obj.get("optype") == "videocomment.kwkwiskwkwdeleted_pie":
        res = get_pie(
            "select kwkwiskwkwdeleted x,count(*) y from vm790_bcfe8a202787453d.videocomment group by kwkwiskwkwdeleted order by x desc",
            "是否已删除",
        )
    if obj.get("optype") == "videocomment.kwkwiskwkwdeleted_pie_v1":
        res = get_pie_v1(
            "select kwkwiskwkwdeleted x,count(*) y from vm790_bcfe8a202787453d.videocomment group by kwkwiskwkwdeleted",
            "是否已删除",
        )
    if obj.get("optype") == "videocomment.kwkwiskwkwdeleted_pie_v2":
        res = get_pie_v2(
            "select kwkwiskwkwdeleted x,count(*) y from vm790_bcfe8a202787453d.videocomment group by kwkwiskwkwdeleted",
            "是否已删除",
        )
    if obj.get("optype") == "videocomment.kwkwiskwkwdeleted_line":
        res = get_line(
            "select kwkwiskwkwdeleted x,count(*) y from vm790_bcfe8a202787453d.videocomment group by kwkwiskwkwdeleted",
            "是否已删除",
        )
    if obj.get("optype") == "videocomment.kwkwiskwkwdeleted_bar":
        res = get_bar(
            "select kwkwiskwkwdeleted x,count(*) y from vm790_bcfe8a202787453d.videocomment group by kwkwiskwkwdeleted",
            "是否已删除",
        )
    if obj.get("optype") == "videocomment.kwkwiskwkwdeleted_bar_v1":
        res = get_bar_v1(
            "select kwkwiskwkwdeleted x,count(*) y from vm790_bcfe8a202787453d.videocomment group by kwkwiskwkwdeleted",
            "是否已删除",
        )
    # videocomment(视频评论表)->parentid(关联父评论ID)

    if obj.get("optype") == "videocomment.parentid_pie":
        res = get_pie(
            "select parentid x,count(*) y from vm790_bcfe8a202787453d.videocomment group by parentid order by x desc",
            "关联父评论ID",
        )
    if obj.get("optype") == "videocomment.parentid_pie_v1":
        res = get_pie_v1(
            "select parentid x,count(*) y from vm790_bcfe8a202787453d.videocomment group by parentid",
            "关联父评论ID",
        )
    if obj.get("optype") == "videocomment.parentid_pie_v2":
        res = get_pie_v2(
            "select parentid x,count(*) y from vm790_bcfe8a202787453d.videocomment group by parentid",
            "关联父评论ID",
        )
    if obj.get("optype") == "videocomment.parentid_line":
        res = get_line(
            "select parentid x,count(*) y from vm790_bcfe8a202787453d.videocomment group by parentid",
            "关联父评论ID",
        )
    if obj.get("optype") == "videocomment.parentid_bar":
        res = get_bar(
            "select parentid x,count(*) y from vm790_bcfe8a202787453d.videocomment group by parentid",
            "关联父评论ID",
        )
    if obj.get("optype") == "videocomment.parentid_bar_v1":
        res = get_bar_v1(
            "select parentid x,count(*) y from vm790_bcfe8a202787453d.videocomment group by parentid",
            "关联父评论ID",
        )
    # videolike(视频点赞表)->videoid(关联视频ID)

    if obj.get("optype") == "videolike.videoid_pie":
        res = get_pie(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videolike group by videoid order by x desc",
            "关联视频ID",
        )
    if obj.get("optype") == "videolike.videoid_pie_v1":
        res = get_pie_v1(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videolike group by videoid",
            "关联视频ID",
        )
    if obj.get("optype") == "videolike.videoid_pie_v2":
        res = get_pie_v2(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videolike group by videoid",
            "关联视频ID",
        )
    if obj.get("optype") == "videolike.videoid_line":
        res = get_line(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videolike group by videoid",
            "关联视频ID",
        )
    if obj.get("optype") == "videolike.videoid_bar":
        res = get_bar(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videolike group by videoid",
            "关联视频ID",
        )
    if obj.get("optype") == "videolike.videoid_bar_v1":
        res = get_bar_v1(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videolike group by videoid",
            "关联视频ID",
        )
    # videolike(视频点赞表)->userid(关联用户ID)

    if obj.get("optype") == "videolike.userid_pie":
        res = get_pie(
            "select userid x,count(*) y from vm790_bcfe8a202787453d.videolike group by userid order by x desc",
            "关联用户ID",
        )
    if obj.get("optype") == "videolike.userid_pie_v1":
        res = get_pie_v1(
            "select userid x,count(*) y from vm790_bcfe8a202787453d.videolike group by userid",
            "关联用户ID",
        )
    if obj.get("optype") == "videolike.userid_pie_v2":
        res = get_pie_v2(
            "select userid x,count(*) y from vm790_bcfe8a202787453d.videolike group by userid",
            "关联用户ID",
        )
    if obj.get("optype") == "videolike.userid_line":
        res = get_line(
            "select userid x,count(*) y from vm790_bcfe8a202787453d.videolike group by userid",
            "关联用户ID",
        )
    if obj.get("optype") == "videolike.userid_bar":
        res = get_bar(
            "select userid x,count(*) y from vm790_bcfe8a202787453d.videolike group by userid",
            "关联用户ID",
        )
    if obj.get("optype") == "videolike.userid_bar_v1":
        res = get_bar_v1(
            "select userid x,count(*) y from vm790_bcfe8a202787453d.videolike group by userid",
            "关联用户ID",
        )
    if obj.get("optype") == "videolike.liketime_line":
        res = get_line(
            "select liketime x,count(*) y from vm790_bcfe8a202787453d.videolike group by liketime order by x",
            "点赞时间",
        )
    # videolike(视频点赞表)->kwkwisliked(是否点赞1为已点赞0为未点赞用于取消点赞功能)

    if obj.get("optype") == "videolike.kwkwisliked_pie":
        res = get_pie(
            "select kwkwisliked x,count(*) y from vm790_bcfe8a202787453d.videolike group by kwkwisliked order by x desc",
            "是否点赞1为已点赞0为未点赞用于取消点赞功能",
        )
    if obj.get("optype") == "videolike.kwkwisliked_pie_v1":
        res = get_pie_v1(
            "select kwkwisliked x,count(*) y from vm790_bcfe8a202787453d.videolike group by kwkwisliked",
            "是否点赞1为已点赞0为未点赞用于取消点赞功能",
        )
    if obj.get("optype") == "videolike.kwkwisliked_pie_v2":
        res = get_pie_v2(
            "select kwkwisliked x,count(*) y from vm790_bcfe8a202787453d.videolike group by kwkwisliked",
            "是否点赞1为已点赞0为未点赞用于取消点赞功能",
        )
    if obj.get("optype") == "videolike.kwkwisliked_line":
        res = get_line(
            "select kwkwisliked x,count(*) y from vm790_bcfe8a202787453d.videolike group by kwkwisliked",
            "是否点赞1为已点赞0为未点赞用于取消点赞功能",
        )
    if obj.get("optype") == "videolike.kwkwisliked_bar":
        res = get_bar(
            "select kwkwisliked x,count(*) y from vm790_bcfe8a202787453d.videolike group by kwkwisliked",
            "是否点赞1为已点赞0为未点赞用于取消点赞功能",
        )
    if obj.get("optype") == "videolike.kwkwisliked_bar_v1":
        res = get_bar_v1(
            "select kwkwisliked x,count(*) y from vm790_bcfe8a202787453d.videolike group by kwkwisliked",
            "是否点赞1为已点赞0为未点赞用于取消点赞功能",
        )
    if obj.get("optype") == "videolike.ipaddress_wordcloud":
        textlist = get_data(
            "SELECT ipaddress result FROM vm790_bcfe8a202787453d.videolike;"
        )
        res = {
            "title": "词云图",
            "imgbs64": generate_wordcloud_base64(
                ",".join([t["result"] for t in textlist])
            ),
        }
    # videolike(视频点赞表)->liketype(点赞类型如普通点赞、特殊点赞等可用枚举或示)

    if obj.get("optype") == "videolike.liketype_pie":
        res = get_pie(
            "select liketype x,count(*) y from vm790_bcfe8a202787453d.videolike group by liketype order by x desc",
            "点赞类型如普通点赞、特殊点赞等可用枚举或示",
        )
    if obj.get("optype") == "videolike.liketype_pie_v1":
        res = get_pie_v1(
            "select liketype x,count(*) y from vm790_bcfe8a202787453d.videolike group by liketype",
            "点赞类型如普通点赞、特殊点赞等可用枚举或示",
        )
    if obj.get("optype") == "videolike.liketype_pie_v2":
        res = get_pie_v2(
            "select liketype x,count(*) y from vm790_bcfe8a202787453d.videolike group by liketype",
            "点赞类型如普通点赞、特殊点赞等可用枚举或示",
        )
    if obj.get("optype") == "videolike.liketype_line":
        res = get_line(
            "select liketype x,count(*) y from vm790_bcfe8a202787453d.videolike group by liketype",
            "点赞类型如普通点赞、特殊点赞等可用枚举或示",
        )
    if obj.get("optype") == "videolike.liketype_bar":
        res = get_bar(
            "select liketype x,count(*) y from vm790_bcfe8a202787453d.videolike group by liketype",
            "点赞类型如普通点赞、特殊点赞等可用枚举或示",
        )
    if obj.get("optype") == "videolike.liketype_bar_v1":
        res = get_bar_v1(
            "select liketype x,count(*) y from vm790_bcfe8a202787453d.videolike group by liketype",
            "点赞类型如普通点赞、特殊点赞等可用枚举或示",
        )
    # videolike(视频点赞表)->platkwkwfkwkworm(点赞平台如Web、iOS、Android等)

    if obj.get("optype") == "videolike.platkwkwfkwkworm_pie":
        res = get_pie(
            "select platkwkwfkwkworm x,count(*) y from vm790_bcfe8a202787453d.videolike group by platkwkwfkwkworm order by x desc",
            "点赞平台如Web、iOS、Android等",
        )
    if obj.get("optype") == "videolike.platkwkwfkwkworm_pie_v1":
        res = get_pie_v1(
            "select platkwkwfkwkworm x,count(*) y from vm790_bcfe8a202787453d.videolike group by platkwkwfkwkworm",
            "点赞平台如Web、iOS、Android等",
        )
    if obj.get("optype") == "videolike.platkwkwfkwkworm_pie_v2":
        res = get_pie_v2(
            "select platkwkwfkwkworm x,count(*) y from vm790_bcfe8a202787453d.videolike group by platkwkwfkwkworm",
            "点赞平台如Web、iOS、Android等",
        )
    if obj.get("optype") == "videolike.platkwkwfkwkworm_line":
        res = get_line(
            "select platkwkwfkwkworm x,count(*) y from vm790_bcfe8a202787453d.videolike group by platkwkwfkwkworm",
            "点赞平台如Web、iOS、Android等",
        )
    if obj.get("optype") == "videolike.platkwkwfkwkworm_bar":
        res = get_bar(
            "select platkwkwfkwkworm x,count(*) y from vm790_bcfe8a202787453d.videolike group by platkwkwfkwkworm",
            "点赞平台如Web、iOS、Android等",
        )
    if obj.get("optype") == "videolike.platkwkwfkwkworm_bar_v1":
        res = get_bar_v1(
            "select platkwkwfkwkworm x,count(*) y from vm790_bcfe8a202787453d.videolike group by platkwkwfkwkworm",
            "点赞平台如Web、iOS、Android等",
        )
    # videolike(视频点赞表)->deviceid(设备ID可选用于追踪用户设备)

    if obj.get("optype") == "videolike.deviceid_pie":
        res = get_pie(
            "select deviceid x,count(*) y from vm790_bcfe8a202787453d.videolike group by deviceid order by x desc",
            "设备ID可选用于追踪用户设备",
        )
    if obj.get("optype") == "videolike.deviceid_pie_v1":
        res = get_pie_v1(
            "select deviceid x,count(*) y from vm790_bcfe8a202787453d.videolike group by deviceid",
            "设备ID可选用于追踪用户设备",
        )
    if obj.get("optype") == "videolike.deviceid_pie_v2":
        res = get_pie_v2(
            "select deviceid x,count(*) y from vm790_bcfe8a202787453d.videolike group by deviceid",
            "设备ID可选用于追踪用户设备",
        )
    if obj.get("optype") == "videolike.deviceid_line":
        res = get_line(
            "select deviceid x,count(*) y from vm790_bcfe8a202787453d.videolike group by deviceid",
            "设备ID可选用于追踪用户设备",
        )
    if obj.get("optype") == "videolike.deviceid_bar":
        res = get_bar(
            "select deviceid x,count(*) y from vm790_bcfe8a202787453d.videolike group by deviceid",
            "设备ID可选用于追踪用户设备",
        )
    if obj.get("optype") == "videolike.deviceid_bar_v1":
        res = get_bar_v1(
            "select deviceid x,count(*) y from vm790_bcfe8a202787453d.videolike group by deviceid",
            "设备ID可选用于追踪用户设备",
        )
    # videoshare(视频分享表)->videoid(关联视频ID)

    if obj.get("optype") == "videoshare.videoid_pie":
        res = get_pie(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videoshare group by videoid order by x desc",
            "关联视频ID",
        )
    if obj.get("optype") == "videoshare.videoid_pie_v1":
        res = get_pie_v1(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videoshare group by videoid",
            "关联视频ID",
        )
    if obj.get("optype") == "videoshare.videoid_pie_v2":
        res = get_pie_v2(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videoshare group by videoid",
            "关联视频ID",
        )
    if obj.get("optype") == "videoshare.videoid_line":
        res = get_line(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videoshare group by videoid",
            "关联视频ID",
        )
    if obj.get("optype") == "videoshare.videoid_bar":
        res = get_bar(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videoshare group by videoid",
            "关联视频ID",
        )
    if obj.get("optype") == "videoshare.videoid_bar_v1":
        res = get_bar_v1(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videoshare group by videoid",
            "关联视频ID",
        )
    # videoshare(视频分享表)->userid(关联用户ID)

    if obj.get("optype") == "videoshare.userid_pie":
        res = get_pie(
            "select userid x,count(*) y from vm790_bcfe8a202787453d.videoshare group by userid order by x desc",
            "关联用户ID",
        )
    if obj.get("optype") == "videoshare.userid_pie_v1":
        res = get_pie_v1(
            "select userid x,count(*) y from vm790_bcfe8a202787453d.videoshare group by userid",
            "关联用户ID",
        )
    if obj.get("optype") == "videoshare.userid_pie_v2":
        res = get_pie_v2(
            "select userid x,count(*) y from vm790_bcfe8a202787453d.videoshare group by userid",
            "关联用户ID",
        )
    if obj.get("optype") == "videoshare.userid_line":
        res = get_line(
            "select userid x,count(*) y from vm790_bcfe8a202787453d.videoshare group by userid",
            "关联用户ID",
        )
    if obj.get("optype") == "videoshare.userid_bar":
        res = get_bar(
            "select userid x,count(*) y from vm790_bcfe8a202787453d.videoshare group by userid",
            "关联用户ID",
        )
    if obj.get("optype") == "videoshare.userid_bar_v1":
        res = get_bar_v1(
            "select userid x,count(*) y from vm790_bcfe8a202787453d.videoshare group by userid",
            "关联用户ID",
        )
    if obj.get("optype") == "videoshare.sharetime_line":
        res = get_line(
            "select sharetime x,count(*) y from vm790_bcfe8a202787453d.videoshare group by sharetime order by x",
            "分享时间",
        )
    # videoshare(视频分享表)->title(视频标题)

    if obj.get("optype") == "videoshare.title_pie":
        res = get_pie(
            "select title x,count(*) y from vm790_bcfe8a202787453d.videoshare group by title order by x desc",
            "视频标题",
        )
    if obj.get("optype") == "videoshare.title_pie_v1":
        res = get_pie_v1(
            "select title x,count(*) y from vm790_bcfe8a202787453d.videoshare group by title",
            "视频标题",
        )
    if obj.get("optype") == "videoshare.title_pie_v2":
        res = get_pie_v2(
            "select title x,count(*) y from vm790_bcfe8a202787453d.videoshare group by title",
            "视频标题",
        )
    if obj.get("optype") == "videoshare.title_line":
        res = get_line(
            "select title x,count(*) y from vm790_bcfe8a202787453d.videoshare group by title",
            "视频标题",
        )
    if obj.get("optype") == "videoshare.title_bar":
        res = get_bar(
            "select title x,count(*) y from vm790_bcfe8a202787453d.videoshare group by title",
            "视频标题",
        )
    if obj.get("optype") == "videoshare.title_bar_v1":
        res = get_bar_v1(
            "select title x,count(*) y from vm790_bcfe8a202787453d.videoshare group by title",
            "视频标题",
        )
    if obj.get("optype") == "videoshare.description_wordcloud":
        textlist = get_data(
            "SELECT description result FROM vm790_bcfe8a202787453d.videoshare;"
        )
        res = {
            "title": "词云图",
            "imgbs64": generate_wordcloud_base64(
                ",".join([t["result"] for t in textlist])
            ),
        }
    # videoshare(视频分享表)->thumbnailurl(缩略图URL)

    if obj.get("optype") == "videoshare.thumbnailurl_pie":
        res = get_pie(
            "select thumbnailurl x,count(*) y from vm790_bcfe8a202787453d.videoshare group by thumbnailurl order by x desc",
            "缩略图URL",
        )
    if obj.get("optype") == "videoshare.thumbnailurl_pie_v1":
        res = get_pie_v1(
            "select thumbnailurl x,count(*) y from vm790_bcfe8a202787453d.videoshare group by thumbnailurl",
            "缩略图URL",
        )
    if obj.get("optype") == "videoshare.thumbnailurl_pie_v2":
        res = get_pie_v2(
            "select thumbnailurl x,count(*) y from vm790_bcfe8a202787453d.videoshare group by thumbnailurl",
            "缩略图URL",
        )
    if obj.get("optype") == "videoshare.thumbnailurl_line":
        res = get_line(
            "select thumbnailurl x,count(*) y from vm790_bcfe8a202787453d.videoshare group by thumbnailurl",
            "缩略图URL",
        )
    if obj.get("optype") == "videoshare.thumbnailurl_bar":
        res = get_bar(
            "select thumbnailurl x,count(*) y from vm790_bcfe8a202787453d.videoshare group by thumbnailurl",
            "缩略图URL",
        )
    if obj.get("optype") == "videoshare.thumbnailurl_bar_v1":
        res = get_bar_v1(
            "select thumbnailurl x,count(*) y from vm790_bcfe8a202787453d.videoshare group by thumbnailurl",
            "缩略图URL",
        )
    # videoshare(视频分享表)->viewcount(观看次数)

    if obj.get("optype") == "videoshare.viewcount_pie":
        res = get_pie(
            "select viewcount x,count(*) y from vm790_bcfe8a202787453d.videoshare group by viewcount order by x desc",
            "观看次数",
        )
    if obj.get("optype") == "videoshare.viewcount_pie_v1":
        res = get_pie_v1(
            "select viewcount x,count(*) y from vm790_bcfe8a202787453d.videoshare group by viewcount",
            "观看次数",
        )
    if obj.get("optype") == "videoshare.viewcount_pie_v2":
        res = get_pie_v2(
            "select viewcount x,count(*) y from vm790_bcfe8a202787453d.videoshare group by viewcount",
            "观看次数",
        )
    if obj.get("optype") == "videoshare.viewcount_line":
        res = get_line(
            "select viewcount x,count(*) y from vm790_bcfe8a202787453d.videoshare group by viewcount",
            "观看次数",
        )
    if obj.get("optype") == "videoshare.viewcount_bar":
        res = get_bar(
            "select viewcount x,count(*) y from vm790_bcfe8a202787453d.videoshare group by viewcount",
            "观看次数",
        )
    if obj.get("optype") == "videoshare.viewcount_bar_v1":
        res = get_bar_v1(
            "select viewcount x,count(*) y from vm790_bcfe8a202787453d.videoshare group by viewcount",
            "观看次数",
        )
    # videoshare(视频分享表)->likecount(点赞次数)

    if obj.get("optype") == "videoshare.likecount_pie":
        res = get_pie(
            "select likecount x,count(*) y from vm790_bcfe8a202787453d.videoshare group by likecount order by x desc",
            "点赞次数",
        )
    if obj.get("optype") == "videoshare.likecount_pie_v1":
        res = get_pie_v1(
            "select likecount x,count(*) y from vm790_bcfe8a202787453d.videoshare group by likecount",
            "点赞次数",
        )
    if obj.get("optype") == "videoshare.likecount_pie_v2":
        res = get_pie_v2(
            "select likecount x,count(*) y from vm790_bcfe8a202787453d.videoshare group by likecount",
            "点赞次数",
        )
    if obj.get("optype") == "videoshare.likecount_line":
        res = get_line(
            "select likecount x,count(*) y from vm790_bcfe8a202787453d.videoshare group by likecount",
            "点赞次数",
        )
    if obj.get("optype") == "videoshare.likecount_bar":
        res = get_bar(
            "select likecount x,count(*) y from vm790_bcfe8a202787453d.videoshare group by likecount",
            "点赞次数",
        )
    if obj.get("optype") == "videoshare.likecount_bar_v1":
        res = get_bar_v1(
            "select likecount x,count(*) y from vm790_bcfe8a202787453d.videoshare group by likecount",
            "点赞次数",
        )
    if obj.get("optype") == "videoshare.commentcount_wordcloud":
        textlist = get_data(
            "SELECT commentcount result FROM vm790_bcfe8a202787453d.videoshare;"
        )
        res = {
            "title": "词云图",
            "imgbs64": generate_wordcloud_base64(
                ",".join([t["result"] for t in textlist])
            ),
        }
    # videoshare(视频分享表)->sharestatus(分享状态例如已分享、已删除)

    if obj.get("optype") == "videoshare.sharestatus_pie":
        res = get_pie(
            "select sharestatus x,count(*) y from vm790_bcfe8a202787453d.videoshare group by sharestatus order by x desc",
            "分享状态例如已分享、已删除",
        )
    if obj.get("optype") == "videoshare.sharestatus_pie_v1":
        res = get_pie_v1(
            "select sharestatus x,count(*) y from vm790_bcfe8a202787453d.videoshare group by sharestatus",
            "分享状态例如已分享、已删除",
        )
    if obj.get("optype") == "videoshare.sharestatus_pie_v2":
        res = get_pie_v2(
            "select sharestatus x,count(*) y from vm790_bcfe8a202787453d.videoshare group by sharestatus",
            "分享状态例如已分享、已删除",
        )
    if obj.get("optype") == "videoshare.sharestatus_line":
        res = get_line(
            "select sharestatus x,count(*) y from vm790_bcfe8a202787453d.videoshare group by sharestatus",
            "分享状态例如已分享、已删除",
        )
    if obj.get("optype") == "videoshare.sharestatus_bar":
        res = get_bar(
            "select sharestatus x,count(*) y from vm790_bcfe8a202787453d.videoshare group by sharestatus",
            "分享状态例如已分享、已删除",
        )
    if obj.get("optype") == "videoshare.sharestatus_bar_v1":
        res = get_bar_v1(
            "select sharestatus x,count(*) y from vm790_bcfe8a202787453d.videoshare group by sharestatus",
            "分享状态例如已分享、已删除",
        )
    # videoviewduration(视频观看时长统计表)->videoid(关联视频ID)

    if obj.get("optype") == "videoviewduration.videoid_pie":
        res = get_pie(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videoviewduration group by videoid order by x desc",
            "关联视频ID",
        )
    if obj.get("optype") == "videoviewduration.videoid_pie_v1":
        res = get_pie_v1(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videoviewduration group by videoid",
            "关联视频ID",
        )
    if obj.get("optype") == "videoviewduration.videoid_pie_v2":
        res = get_pie_v2(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videoviewduration group by videoid",
            "关联视频ID",
        )
    if obj.get("optype") == "videoviewduration.videoid_line":
        res = get_line(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videoviewduration group by videoid",
            "关联视频ID",
        )
    if obj.get("optype") == "videoviewduration.videoid_bar":
        res = get_bar(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videoviewduration group by videoid",
            "关联视频ID",
        )
    if obj.get("optype") == "videoviewduration.videoid_bar_v1":
        res = get_bar_v1(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videoviewduration group by videoid",
            "关联视频ID",
        )
    # videoviewduration(视频观看时长统计表)->userid(关联用户ID)

    if obj.get("optype") == "videoviewduration.userid_pie":
        res = get_pie(
            "select userid x,count(*) y from vm790_bcfe8a202787453d.videoviewduration group by userid order by x desc",
            "关联用户ID",
        )
    if obj.get("optype") == "videoviewduration.userid_pie_v1":
        res = get_pie_v1(
            "select userid x,count(*) y from vm790_bcfe8a202787453d.videoviewduration group by userid",
            "关联用户ID",
        )
    if obj.get("optype") == "videoviewduration.userid_pie_v2":
        res = get_pie_v2(
            "select userid x,count(*) y from vm790_bcfe8a202787453d.videoviewduration group by userid",
            "关联用户ID",
        )
    if obj.get("optype") == "videoviewduration.userid_line":
        res = get_line(
            "select userid x,count(*) y from vm790_bcfe8a202787453d.videoviewduration group by userid",
            "关联用户ID",
        )
    if obj.get("optype") == "videoviewduration.userid_bar":
        res = get_bar(
            "select userid x,count(*) y from vm790_bcfe8a202787453d.videoviewduration group by userid",
            "关联用户ID",
        )
    if obj.get("optype") == "videoviewduration.userid_bar_v1":
        res = get_bar_v1(
            "select userid x,count(*) y from vm790_bcfe8a202787453d.videoviewduration group by userid",
            "关联用户ID",
        )
    if obj.get("optype") == "videoviewduration.viewstarttime_line":
        res = get_line(
            "select viewstarttime x,count(*) y from vm790_bcfe8a202787453d.videoviewduration group by viewstarttime order by x",
            "观看开始时间",
        )
    if obj.get("optype") == "videoviewduration.viewendtime_line":
        res = get_line(
            "select viewendtime x,count(*) y from vm790_bcfe8a202787453d.videoviewduration group by viewendtime order by x",
            "观看结束时间",
        )
    # videoviewduration(视频观看时长统计表)->duration(观看时长秒)

    if obj.get("optype") == "videoviewduration.duration_pie":
        res = get_pie(
            "select duration x,count(*) y from vm790_bcfe8a202787453d.videoviewduration group by duration order by x desc",
            "观看时长秒",
        )
    if obj.get("optype") == "videoviewduration.duration_pie_v1":
        res = get_pie_v1(
            "select duration x,count(*) y from vm790_bcfe8a202787453d.videoviewduration group by duration",
            "观看时长秒",
        )
    if obj.get("optype") == "videoviewduration.duration_pie_v2":
        res = get_pie_v2(
            "select duration x,count(*) y from vm790_bcfe8a202787453d.videoviewduration group by duration",
            "观看时长秒",
        )
    if obj.get("optype") == "videoviewduration.duration_line":
        res = get_line(
            "select duration x,count(*) y from vm790_bcfe8a202787453d.videoviewduration group by duration",
            "观看时长秒",
        )
    if obj.get("optype") == "videoviewduration.duration_bar":
        res = get_bar(
            "select duration x,count(*) y from vm790_bcfe8a202787453d.videoviewduration group by duration",
            "观看时长秒",
        )
    if obj.get("optype") == "videoviewduration.duration_bar_v1":
        res = get_bar_v1(
            "select duration x,count(*) y from vm790_bcfe8a202787453d.videoviewduration group by duration",
            "观看时长秒",
        )
    # videoviewduration(视频观看时长统计表)->devicetype(设备类型)

    if obj.get("optype") == "videoviewduration.devicetype_pie":
        res = get_pie(
            "select devicetype x,count(*) y from vm790_bcfe8a202787453d.videoviewduration group by devicetype order by x desc",
            "设备类型",
        )
    if obj.get("optype") == "videoviewduration.devicetype_pie_v1":
        res = get_pie_v1(
            "select devicetype x,count(*) y from vm790_bcfe8a202787453d.videoviewduration group by devicetype",
            "设备类型",
        )
    if obj.get("optype") == "videoviewduration.devicetype_pie_v2":
        res = get_pie_v2(
            "select devicetype x,count(*) y from vm790_bcfe8a202787453d.videoviewduration group by devicetype",
            "设备类型",
        )
    if obj.get("optype") == "videoviewduration.devicetype_line":
        res = get_line(
            "select devicetype x,count(*) y from vm790_bcfe8a202787453d.videoviewduration group by devicetype",
            "设备类型",
        )
    if obj.get("optype") == "videoviewduration.devicetype_bar":
        res = get_bar(
            "select devicetype x,count(*) y from vm790_bcfe8a202787453d.videoviewduration group by devicetype",
            "设备类型",
        )
    if obj.get("optype") == "videoviewduration.devicetype_bar_v1":
        res = get_bar_v1(
            "select devicetype x,count(*) y from vm790_bcfe8a202787453d.videoviewduration group by devicetype",
            "设备类型",
        )
    # videoviewduration(视频观看时长统计表)->viewlocation(观看地点)

    if obj.get("optype") == "videoviewduration.viewlocation_pie":
        res = get_pie(
            "select viewlocation x,count(*) y from vm790_bcfe8a202787453d.videoviewduration group by viewlocation order by x desc",
            "观看地点",
        )
    if obj.get("optype") == "videoviewduration.viewlocation_pie_v1":
        res = get_pie_v1(
            "select viewlocation x,count(*) y from vm790_bcfe8a202787453d.videoviewduration group by viewlocation",
            "观看地点",
        )
    if obj.get("optype") == "videoviewduration.viewlocation_pie_v2":
        res = get_pie_v2(
            "select viewlocation x,count(*) y from vm790_bcfe8a202787453d.videoviewduration group by viewlocation",
            "观看地点",
        )
    if obj.get("optype") == "videoviewduration.viewlocation_line":
        res = get_line(
            "select viewlocation x,count(*) y from vm790_bcfe8a202787453d.videoviewduration group by viewlocation",
            "观看地点",
        )
    if obj.get("optype") == "videoviewduration.viewlocation_bar":
        res = get_bar(
            "select viewlocation x,count(*) y from vm790_bcfe8a202787453d.videoviewduration group by viewlocation",
            "观看地点",
        )
    if obj.get("optype") == "videoviewduration.viewlocation_bar_v1":
        res = get_bar_v1(
            "select viewlocation x,count(*) y from vm790_bcfe8a202787453d.videoviewduration group by viewlocation",
            "观看地点",
        )
    # videoviewduration(视频观看时长统计表)->netwkwkworktype(网络类型)

    if obj.get("optype") == "videoviewduration.netwkwkworktype_pie":
        res = get_pie(
            "select netwkwkworktype x,count(*) y from vm790_bcfe8a202787453d.videoviewduration group by netwkwkworktype order by x desc",
            "网络类型",
        )
    if obj.get("optype") == "videoviewduration.netwkwkworktype_pie_v1":
        res = get_pie_v1(
            "select netwkwkworktype x,count(*) y from vm790_bcfe8a202787453d.videoviewduration group by netwkwkworktype",
            "网络类型",
        )
    if obj.get("optype") == "videoviewduration.netwkwkworktype_pie_v2":
        res = get_pie_v2(
            "select netwkwkworktype x,count(*) y from vm790_bcfe8a202787453d.videoviewduration group by netwkwkworktype",
            "网络类型",
        )
    if obj.get("optype") == "videoviewduration.netwkwkworktype_line":
        res = get_line(
            "select netwkwkworktype x,count(*) y from vm790_bcfe8a202787453d.videoviewduration group by netwkwkworktype",
            "网络类型",
        )
    if obj.get("optype") == "videoviewduration.netwkwkworktype_bar":
        res = get_bar(
            "select netwkwkworktype x,count(*) y from vm790_bcfe8a202787453d.videoviewduration group by netwkwkworktype",
            "网络类型",
        )
    if obj.get("optype") == "videoviewduration.netwkwkworktype_bar_v1":
        res = get_bar_v1(
            "select netwkwkworktype x,count(*) y from vm790_bcfe8a202787453d.videoviewduration group by netwkwkworktype",
            "网络类型",
        )
    # videoviewduration(视频观看时长统计表)->kwkwiscompleted(是否观看完成0未完成1已完成)

    if obj.get("optype") == "videoviewduration.kwkwiscompleted_pie":
        res = get_pie(
            "select kwkwiscompleted x,count(*) y from vm790_bcfe8a202787453d.videoviewduration group by kwkwiscompleted order by x desc",
            "是否观看完成0未完成1已完成",
        )
    if obj.get("optype") == "videoviewduration.kwkwiscompleted_pie_v1":
        res = get_pie_v1(
            "select kwkwiscompleted x,count(*) y from vm790_bcfe8a202787453d.videoviewduration group by kwkwiscompleted",
            "是否观看完成0未完成1已完成",
        )
    if obj.get("optype") == "videoviewduration.kwkwiscompleted_pie_v2":
        res = get_pie_v2(
            "select kwkwiscompleted x,count(*) y from vm790_bcfe8a202787453d.videoviewduration group by kwkwiscompleted",
            "是否观看完成0未完成1已完成",
        )
    if obj.get("optype") == "videoviewduration.kwkwiscompleted_line":
        res = get_line(
            "select kwkwiscompleted x,count(*) y from vm790_bcfe8a202787453d.videoviewduration group by kwkwiscompleted",
            "是否观看完成0未完成1已完成",
        )
    if obj.get("optype") == "videoviewduration.kwkwiscompleted_bar":
        res = get_bar(
            "select kwkwiscompleted x,count(*) y from vm790_bcfe8a202787453d.videoviewduration group by kwkwiscompleted",
            "是否观看完成0未完成1已完成",
        )
    if obj.get("optype") == "videoviewduration.kwkwiscompleted_bar_v1":
        res = get_bar_v1(
            "select kwkwiscompleted x,count(*) y from vm790_bcfe8a202787453d.videoviewduration group by kwkwiscompleted",
            "是否观看完成0未完成1已完成",
        )
    # videouploader(视频上传用户表)->userid(关联用户ID)

    if obj.get("optype") == "videouploader.userid_pie":
        res = get_pie(
            "select userid x,count(*) y from vm790_bcfe8a202787453d.videouploader group by userid order by x desc",
            "关联用户ID",
        )
    if obj.get("optype") == "videouploader.userid_pie_v1":
        res = get_pie_v1(
            "select userid x,count(*) y from vm790_bcfe8a202787453d.videouploader group by userid",
            "关联用户ID",
        )
    if obj.get("optype") == "videouploader.userid_pie_v2":
        res = get_pie_v2(
            "select userid x,count(*) y from vm790_bcfe8a202787453d.videouploader group by userid",
            "关联用户ID",
        )
    if obj.get("optype") == "videouploader.userid_line":
        res = get_line(
            "select userid x,count(*) y from vm790_bcfe8a202787453d.videouploader group by userid",
            "关联用户ID",
        )
    if obj.get("optype") == "videouploader.userid_bar":
        res = get_bar(
            "select userid x,count(*) y from vm790_bcfe8a202787453d.videouploader group by userid",
            "关联用户ID",
        )
    if obj.get("optype") == "videouploader.userid_bar_v1":
        res = get_bar_v1(
            "select userid x,count(*) y from vm790_bcfe8a202787453d.videouploader group by userid",
            "关联用户ID",
        )
    # videouploader(视频上传用户表)->username(用户名)

    if obj.get("optype") == "videouploader.username_pie":
        res = get_pie(
            "select username x,count(*) y from vm790_bcfe8a202787453d.videouploader group by username order by x desc",
            "用户名",
        )
    if obj.get("optype") == "videouploader.username_pie_v1":
        res = get_pie_v1(
            "select username x,count(*) y from vm790_bcfe8a202787453d.videouploader group by username",
            "用户名",
        )
    if obj.get("optype") == "videouploader.username_pie_v2":
        res = get_pie_v2(
            "select username x,count(*) y from vm790_bcfe8a202787453d.videouploader group by username",
            "用户名",
        )
    if obj.get("optype") == "videouploader.username_line":
        res = get_line(
            "select username x,count(*) y from vm790_bcfe8a202787453d.videouploader group by username",
            "用户名",
        )
    if obj.get("optype") == "videouploader.username_bar":
        res = get_bar(
            "select username x,count(*) y from vm790_bcfe8a202787453d.videouploader group by username",
            "用户名",
        )
    if obj.get("optype") == "videouploader.username_bar_v1":
        res = get_bar_v1(
            "select username x,count(*) y from vm790_bcfe8a202787453d.videouploader group by username",
            "用户名",
        )
    # videouploader(视频上传用户表)->email(电子邮件)

    if obj.get("optype") == "videouploader.email_pie":
        res = get_pie(
            "select email x,count(*) y from vm790_bcfe8a202787453d.videouploader group by email order by x desc",
            "电子邮件",
        )
    if obj.get("optype") == "videouploader.email_pie_v1":
        res = get_pie_v1(
            "select email x,count(*) y from vm790_bcfe8a202787453d.videouploader group by email",
            "电子邮件",
        )
    if obj.get("optype") == "videouploader.email_pie_v2":
        res = get_pie_v2(
            "select email x,count(*) y from vm790_bcfe8a202787453d.videouploader group by email",
            "电子邮件",
        )
    if obj.get("optype") == "videouploader.email_line":
        res = get_line(
            "select email x,count(*) y from vm790_bcfe8a202787453d.videouploader group by email",
            "电子邮件",
        )
    if obj.get("optype") == "videouploader.email_bar":
        res = get_bar(
            "select email x,count(*) y from vm790_bcfe8a202787453d.videouploader group by email",
            "电子邮件",
        )
    if obj.get("optype") == "videouploader.email_bar_v1":
        res = get_bar_v1(
            "select email x,count(*) y from vm790_bcfe8a202787453d.videouploader group by email",
            "电子邮件",
        )
    # videouploader(视频上传用户表)->phonenumber(电话号码)

    if obj.get("optype") == "videouploader.phonenumber_pie":
        res = get_pie(
            "select phonenumber x,count(*) y from vm790_bcfe8a202787453d.videouploader group by phonenumber order by x desc",
            "电话号码",
        )
    if obj.get("optype") == "videouploader.phonenumber_pie_v1":
        res = get_pie_v1(
            "select phonenumber x,count(*) y from vm790_bcfe8a202787453d.videouploader group by phonenumber",
            "电话号码",
        )
    if obj.get("optype") == "videouploader.phonenumber_pie_v2":
        res = get_pie_v2(
            "select phonenumber x,count(*) y from vm790_bcfe8a202787453d.videouploader group by phonenumber",
            "电话号码",
        )
    if obj.get("optype") == "videouploader.phonenumber_line":
        res = get_line(
            "select phonenumber x,count(*) y from vm790_bcfe8a202787453d.videouploader group by phonenumber",
            "电话号码",
        )
    if obj.get("optype") == "videouploader.phonenumber_bar":
        res = get_bar(
            "select phonenumber x,count(*) y from vm790_bcfe8a202787453d.videouploader group by phonenumber",
            "电话号码",
        )
    if obj.get("optype") == "videouploader.phonenumber_bar_v1":
        res = get_bar_v1(
            "select phonenumber x,count(*) y from vm790_bcfe8a202787453d.videouploader group by phonenumber",
            "电话号码",
        )
    if obj.get("optype") == "videouploader.uploadtime_line":
        res = get_line(
            "select uploadtime x,count(*) y from vm790_bcfe8a202787453d.videouploader group by uploadtime order by x",
            "上传时间",
        )
    # videouploader(视频上传用户表)->videoid(视频ID)

    if obj.get("optype") == "videouploader.videoid_pie":
        res = get_pie(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videouploader group by videoid order by x desc",
            "视频ID",
        )
    if obj.get("optype") == "videouploader.videoid_pie_v1":
        res = get_pie_v1(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videouploader group by videoid",
            "视频ID",
        )
    if obj.get("optype") == "videouploader.videoid_pie_v2":
        res = get_pie_v2(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videouploader group by videoid",
            "视频ID",
        )
    if obj.get("optype") == "videouploader.videoid_line":
        res = get_line(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videouploader group by videoid",
            "视频ID",
        )
    if obj.get("optype") == "videouploader.videoid_bar":
        res = get_bar(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videouploader group by videoid",
            "视频ID",
        )
    if obj.get("optype") == "videouploader.videoid_bar_v1":
        res = get_bar_v1(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videouploader group by videoid",
            "视频ID",
        )
    # videouploader(视频上传用户表)->videotitle(视频标题)

    if obj.get("optype") == "videouploader.videotitle_pie":
        res = get_pie(
            "select videotitle x,count(*) y from vm790_bcfe8a202787453d.videouploader group by videotitle order by x desc",
            "视频标题",
        )
    if obj.get("optype") == "videouploader.videotitle_pie_v1":
        res = get_pie_v1(
            "select videotitle x,count(*) y from vm790_bcfe8a202787453d.videouploader group by videotitle",
            "视频标题",
        )
    if obj.get("optype") == "videouploader.videotitle_pie_v2":
        res = get_pie_v2(
            "select videotitle x,count(*) y from vm790_bcfe8a202787453d.videouploader group by videotitle",
            "视频标题",
        )
    if obj.get("optype") == "videouploader.videotitle_line":
        res = get_line(
            "select videotitle x,count(*) y from vm790_bcfe8a202787453d.videouploader group by videotitle",
            "视频标题",
        )
    if obj.get("optype") == "videouploader.videotitle_bar":
        res = get_bar(
            "select videotitle x,count(*) y from vm790_bcfe8a202787453d.videouploader group by videotitle",
            "视频标题",
        )
    if obj.get("optype") == "videouploader.videotitle_bar_v1":
        res = get_bar_v1(
            "select videotitle x,count(*) y from vm790_bcfe8a202787453d.videouploader group by videotitle",
            "视频标题",
        )
    if obj.get("optype") == "videouploader.videodescription_wordcloud":
        textlist = get_data(
            "SELECT videodescription result FROM vm790_bcfe8a202787453d.videouploader;"
        )
        res = {
            "title": "词云图",
            "imgbs64": generate_wordcloud_base64(
                ",".join([t["result"] for t in textlist])
            ),
        }
    # videouploader(视频上传用户表)->videocategkwkworyid(视频分类ID)

    if obj.get("optype") == "videouploader.videocategkwkworyid_pie":
        res = get_pie(
            "select videocategkwkworyid x,count(*) y from vm790_bcfe8a202787453d.videouploader group by videocategkwkworyid order by x desc",
            "视频分类ID",
        )
    if obj.get("optype") == "videouploader.videocategkwkworyid_pie_v1":
        res = get_pie_v1(
            "select videocategkwkworyid x,count(*) y from vm790_bcfe8a202787453d.videouploader group by videocategkwkworyid",
            "视频分类ID",
        )
    if obj.get("optype") == "videouploader.videocategkwkworyid_pie_v2":
        res = get_pie_v2(
            "select videocategkwkworyid x,count(*) y from vm790_bcfe8a202787453d.videouploader group by videocategkwkworyid",
            "视频分类ID",
        )
    if obj.get("optype") == "videouploader.videocategkwkworyid_line":
        res = get_line(
            "select videocategkwkworyid x,count(*) y from vm790_bcfe8a202787453d.videouploader group by videocategkwkworyid",
            "视频分类ID",
        )
    if obj.get("optype") == "videouploader.videocategkwkworyid_bar":
        res = get_bar(
            "select videocategkwkworyid x,count(*) y from vm790_bcfe8a202787453d.videouploader group by videocategkwkworyid",
            "视频分类ID",
        )
    if obj.get("optype") == "videouploader.videocategkwkworyid_bar_v1":
        res = get_bar_v1(
            "select videocategkwkworyid x,count(*) y from vm790_bcfe8a202787453d.videouploader group by videocategkwkworyid",
            "视频分类ID",
        )
    # videouploader(视频上传用户表)->videostatus(视频状态如审核中、已发布、已删除)

    if obj.get("optype") == "videouploader.videostatus_pie":
        res = get_pie(
            "select videostatus x,count(*) y from vm790_bcfe8a202787453d.videouploader group by videostatus order by x desc",
            "视频状态如审核中、已发布、已删除",
        )
    if obj.get("optype") == "videouploader.videostatus_pie_v1":
        res = get_pie_v1(
            "select videostatus x,count(*) y from vm790_bcfe8a202787453d.videouploader group by videostatus",
            "视频状态如审核中、已发布、已删除",
        )
    if obj.get("optype") == "videouploader.videostatus_pie_v2":
        res = get_pie_v2(
            "select videostatus x,count(*) y from vm790_bcfe8a202787453d.videouploader group by videostatus",
            "视频状态如审核中、已发布、已删除",
        )
    if obj.get("optype") == "videouploader.videostatus_line":
        res = get_line(
            "select videostatus x,count(*) y from vm790_bcfe8a202787453d.videouploader group by videostatus",
            "视频状态如审核中、已发布、已删除",
        )
    if obj.get("optype") == "videouploader.videostatus_bar":
        res = get_bar(
            "select videostatus x,count(*) y from vm790_bcfe8a202787453d.videouploader group by videostatus",
            "视频状态如审核中、已发布、已删除",
        )
    if obj.get("optype") == "videouploader.videostatus_bar_v1":
        res = get_bar_v1(
            "select videostatus x,count(*) y from vm790_bcfe8a202787453d.videouploader group by videostatus",
            "视频状态如审核中、已发布、已删除",
        )
    # userinfo(用户信息表)->userid(用户ID)

    if obj.get("optype") == "userinfo.userid_pie":
        res = get_pie(
            "select userid x,count(*) y from vm790_bcfe8a202787453d.userinfo group by userid order by x desc",
            "用户ID",
        )
    if obj.get("optype") == "userinfo.userid_pie_v1":
        res = get_pie_v1(
            "select userid x,count(*) y from vm790_bcfe8a202787453d.userinfo group by userid",
            "用户ID",
        )
    if obj.get("optype") == "userinfo.userid_pie_v2":
        res = get_pie_v2(
            "select userid x,count(*) y from vm790_bcfe8a202787453d.userinfo group by userid",
            "用户ID",
        )
    if obj.get("optype") == "userinfo.userid_line":
        res = get_line(
            "select userid x,count(*) y from vm790_bcfe8a202787453d.userinfo group by userid",
            "用户ID",
        )
    if obj.get("optype") == "userinfo.userid_bar":
        res = get_bar(
            "select userid x,count(*) y from vm790_bcfe8a202787453d.userinfo group by userid",
            "用户ID",
        )
    if obj.get("optype") == "userinfo.userid_bar_v1":
        res = get_bar_v1(
            "select userid x,count(*) y from vm790_bcfe8a202787453d.userinfo group by userid",
            "用户ID",
        )
    # userinfo(用户信息表)->username(用户名)

    if obj.get("optype") == "userinfo.username_pie":
        res = get_pie(
            "select username x,count(*) y from vm790_bcfe8a202787453d.userinfo group by username order by x desc",
            "用户名",
        )
    if obj.get("optype") == "userinfo.username_pie_v1":
        res = get_pie_v1(
            "select username x,count(*) y from vm790_bcfe8a202787453d.userinfo group by username",
            "用户名",
        )
    if obj.get("optype") == "userinfo.username_pie_v2":
        res = get_pie_v2(
            "select username x,count(*) y from vm790_bcfe8a202787453d.userinfo group by username",
            "用户名",
        )
    if obj.get("optype") == "userinfo.username_line":
        res = get_line(
            "select username x,count(*) y from vm790_bcfe8a202787453d.userinfo group by username",
            "用户名",
        )
    if obj.get("optype") == "userinfo.username_bar":
        res = get_bar(
            "select username x,count(*) y from vm790_bcfe8a202787453d.userinfo group by username",
            "用户名",
        )
    if obj.get("optype") == "userinfo.username_bar_v1":
        res = get_bar_v1(
            "select username x,count(*) y from vm790_bcfe8a202787453d.userinfo group by username",
            "用户名",
        )
    # userinfo(用户信息表)->useremail(用户邮箱)

    if obj.get("optype") == "userinfo.useremail_pie":
        res = get_pie(
            "select useremail x,count(*) y from vm790_bcfe8a202787453d.userinfo group by useremail order by x desc",
            "用户邮箱",
        )
    if obj.get("optype") == "userinfo.useremail_pie_v1":
        res = get_pie_v1(
            "select useremail x,count(*) y from vm790_bcfe8a202787453d.userinfo group by useremail",
            "用户邮箱",
        )
    if obj.get("optype") == "userinfo.useremail_pie_v2":
        res = get_pie_v2(
            "select useremail x,count(*) y from vm790_bcfe8a202787453d.userinfo group by useremail",
            "用户邮箱",
        )
    if obj.get("optype") == "userinfo.useremail_line":
        res = get_line(
            "select useremail x,count(*) y from vm790_bcfe8a202787453d.userinfo group by useremail",
            "用户邮箱",
        )
    if obj.get("optype") == "userinfo.useremail_bar":
        res = get_bar(
            "select useremail x,count(*) y from vm790_bcfe8a202787453d.userinfo group by useremail",
            "用户邮箱",
        )
    if obj.get("optype") == "userinfo.useremail_bar_v1":
        res = get_bar_v1(
            "select useremail x,count(*) y from vm790_bcfe8a202787453d.userinfo group by useremail",
            "用户邮箱",
        )
    # userinfo(用户信息表)->userpkwkwasswkwkword(用户密码)

    if obj.get("optype") == "userinfo.userpkwkwasswkwkword_pie":
        res = get_pie(
            "select userpkwkwasswkwkword x,count(*) y from vm790_bcfe8a202787453d.userinfo group by userpkwkwasswkwkword order by x desc",
            "用户密码",
        )
    if obj.get("optype") == "userinfo.userpkwkwasswkwkword_pie_v1":
        res = get_pie_v1(
            "select userpkwkwasswkwkword x,count(*) y from vm790_bcfe8a202787453d.userinfo group by userpkwkwasswkwkword",
            "用户密码",
        )
    if obj.get("optype") == "userinfo.userpkwkwasswkwkword_pie_v2":
        res = get_pie_v2(
            "select userpkwkwasswkwkword x,count(*) y from vm790_bcfe8a202787453d.userinfo group by userpkwkwasswkwkword",
            "用户密码",
        )
    if obj.get("optype") == "userinfo.userpkwkwasswkwkword_line":
        res = get_line(
            "select userpkwkwasswkwkword x,count(*) y from vm790_bcfe8a202787453d.userinfo group by userpkwkwasswkwkword",
            "用户密码",
        )
    if obj.get("optype") == "userinfo.userpkwkwasswkwkword_bar":
        res = get_bar(
            "select userpkwkwasswkwkword x,count(*) y from vm790_bcfe8a202787453d.userinfo group by userpkwkwasswkwkword",
            "用户密码",
        )
    if obj.get("optype") == "userinfo.userpkwkwasswkwkword_bar_v1":
        res = get_bar_v1(
            "select userpkwkwasswkwkword x,count(*) y from vm790_bcfe8a202787453d.userinfo group by userpkwkwasswkwkword",
            "用户密码",
        )
    # userinfo(用户信息表)->phonenumber(电话号码)

    if obj.get("optype") == "userinfo.phonenumber_pie":
        res = get_pie(
            "select phonenumber x,count(*) y from vm790_bcfe8a202787453d.userinfo group by phonenumber order by x desc",
            "电话号码",
        )
    if obj.get("optype") == "userinfo.phonenumber_pie_v1":
        res = get_pie_v1(
            "select phonenumber x,count(*) y from vm790_bcfe8a202787453d.userinfo group by phonenumber",
            "电话号码",
        )
    if obj.get("optype") == "userinfo.phonenumber_pie_v2":
        res = get_pie_v2(
            "select phonenumber x,count(*) y from vm790_bcfe8a202787453d.userinfo group by phonenumber",
            "电话号码",
        )
    if obj.get("optype") == "userinfo.phonenumber_line":
        res = get_line(
            "select phonenumber x,count(*) y from vm790_bcfe8a202787453d.userinfo group by phonenumber",
            "电话号码",
        )
    if obj.get("optype") == "userinfo.phonenumber_bar":
        res = get_bar(
            "select phonenumber x,count(*) y from vm790_bcfe8a202787453d.userinfo group by phonenumber",
            "电话号码",
        )
    if obj.get("optype") == "userinfo.phonenumber_bar_v1":
        res = get_bar_v1(
            "select phonenumber x,count(*) y from vm790_bcfe8a202787453d.userinfo group by phonenumber",
            "电话号码",
        )
    # userinfo(用户信息表)->gender(性别)

    if obj.get("optype") == "userinfo.gender_pie":
        res = get_pie(
            "select gender x,count(*) y from vm790_bcfe8a202787453d.userinfo group by gender order by x desc",
            "性别",
        )
    if obj.get("optype") == "userinfo.gender_pie_v1":
        res = get_pie_v1(
            "select gender x,count(*) y from vm790_bcfe8a202787453d.userinfo group by gender",
            "性别",
        )
    if obj.get("optype") == "userinfo.gender_pie_v2":
        res = get_pie_v2(
            "select gender x,count(*) y from vm790_bcfe8a202787453d.userinfo group by gender",
            "性别",
        )
    if obj.get("optype") == "userinfo.gender_line":
        res = get_line(
            "select gender x,count(*) y from vm790_bcfe8a202787453d.userinfo group by gender",
            "性别",
        )
    if obj.get("optype") == "userinfo.gender_bar":
        res = get_bar(
            "select gender x,count(*) y from vm790_bcfe8a202787453d.userinfo group by gender",
            "性别",
        )
    if obj.get("optype") == "userinfo.gender_bar_v1":
        res = get_bar_v1(
            "select gender x,count(*) y from vm790_bcfe8a202787453d.userinfo group by gender",
            "性别",
        )
    if obj.get("optype") == "userinfo.birthdate_line":
        res = get_line(
            "select birthdate x,count(*) y from vm790_bcfe8a202787453d.userinfo group by birthdate order by x",
            "出生日期",
        )
    if obj.get("optype") == "userinfo.regkwkwisterdate_line":
        res = get_line(
            "select regkwkwisterdate x,count(*) y from vm790_bcfe8a202787453d.userinfo group by regkwkwisterdate order by x",
            "注册日期",
        )
    # userinfo(用户信息表)->userrole(用户角色)

    if obj.get("optype") == "userinfo.userrole_pie":
        res = get_pie(
            "select userrole x,count(*) y from vm790_bcfe8a202787453d.userinfo group by userrole order by x desc",
            "用户角色",
        )
    if obj.get("optype") == "userinfo.userrole_pie_v1":
        res = get_pie_v1(
            "select userrole x,count(*) y from vm790_bcfe8a202787453d.userinfo group by userrole",
            "用户角色",
        )
    if obj.get("optype") == "userinfo.userrole_pie_v2":
        res = get_pie_v2(
            "select userrole x,count(*) y from vm790_bcfe8a202787453d.userinfo group by userrole",
            "用户角色",
        )
    if obj.get("optype") == "userinfo.userrole_line":
        res = get_line(
            "select userrole x,count(*) y from vm790_bcfe8a202787453d.userinfo group by userrole",
            "用户角色",
        )
    if obj.get("optype") == "userinfo.userrole_bar":
        res = get_bar(
            "select userrole x,count(*) y from vm790_bcfe8a202787453d.userinfo group by userrole",
            "用户角色",
        )
    if obj.get("optype") == "userinfo.userrole_bar_v1":
        res = get_bar_v1(
            "select userrole x,count(*) y from vm790_bcfe8a202787453d.userinfo group by userrole",
            "用户角色",
        )
    if obj.get("optype") == "userinfo.lkwkwastlogkwkwintime_line":
        res = get_line(
            "select lkwkwastlogkwkwintime x,count(*) y from vm790_bcfe8a202787453d.userinfo group by lkwkwastlogkwkwintime order by x",
            "最后登录时间",
        )
    # userpermkwkwission(用户权限表)->userid(关联用户ID)

    if obj.get("optype") == "userpermkwkwission.userid_pie":
        res = get_pie(
            "select userid x,count(*) y from vm790_bcfe8a202787453d.userpermkwkwission group by userid order by x desc",
            "关联用户ID",
        )
    if obj.get("optype") == "userpermkwkwission.userid_pie_v1":
        res = get_pie_v1(
            "select userid x,count(*) y from vm790_bcfe8a202787453d.userpermkwkwission group by userid",
            "关联用户ID",
        )
    if obj.get("optype") == "userpermkwkwission.userid_pie_v2":
        res = get_pie_v2(
            "select userid x,count(*) y from vm790_bcfe8a202787453d.userpermkwkwission group by userid",
            "关联用户ID",
        )
    if obj.get("optype") == "userpermkwkwission.userid_line":
        res = get_line(
            "select userid x,count(*) y from vm790_bcfe8a202787453d.userpermkwkwission group by userid",
            "关联用户ID",
        )
    if obj.get("optype") == "userpermkwkwission.userid_bar":
        res = get_bar(
            "select userid x,count(*) y from vm790_bcfe8a202787453d.userpermkwkwission group by userid",
            "关联用户ID",
        )
    if obj.get("optype") == "userpermkwkwission.userid_bar_v1":
        res = get_bar_v1(
            "select userid x,count(*) y from vm790_bcfe8a202787453d.userpermkwkwission group by userid",
            "关联用户ID",
        )
    # userpermkwkwission(用户权限表)->permkwkwissionid(关联权限ID)

    if obj.get("optype") == "userpermkwkwission.permkwkwissionid_pie":
        res = get_pie(
            "select permkwkwissionid x,count(*) y from vm790_bcfe8a202787453d.userpermkwkwission group by permkwkwissionid order by x desc",
            "关联权限ID",
        )
    if obj.get("optype") == "userpermkwkwission.permkwkwissionid_pie_v1":
        res = get_pie_v1(
            "select permkwkwissionid x,count(*) y from vm790_bcfe8a202787453d.userpermkwkwission group by permkwkwissionid",
            "关联权限ID",
        )
    if obj.get("optype") == "userpermkwkwission.permkwkwissionid_pie_v2":
        res = get_pie_v2(
            "select permkwkwissionid x,count(*) y from vm790_bcfe8a202787453d.userpermkwkwission group by permkwkwissionid",
            "关联权限ID",
        )
    if obj.get("optype") == "userpermkwkwission.permkwkwissionid_line":
        res = get_line(
            "select permkwkwissionid x,count(*) y from vm790_bcfe8a202787453d.userpermkwkwission group by permkwkwissionid",
            "关联权限ID",
        )
    if obj.get("optype") == "userpermkwkwission.permkwkwissionid_bar":
        res = get_bar(
            "select permkwkwissionid x,count(*) y from vm790_bcfe8a202787453d.userpermkwkwission group by permkwkwissionid",
            "关联权限ID",
        )
    if obj.get("optype") == "userpermkwkwission.permkwkwissionid_bar_v1":
        res = get_bar_v1(
            "select permkwkwissionid x,count(*) y from vm790_bcfe8a202787453d.userpermkwkwission group by permkwkwissionid",
            "关联权限ID",
        )
    # userpermkwkwission(用户权限表)->rolename(角色名称)

    if obj.get("optype") == "userpermkwkwission.rolename_pie":
        res = get_pie(
            "select rolename x,count(*) y from vm790_bcfe8a202787453d.userpermkwkwission group by rolename order by x desc",
            "角色名称",
        )
    if obj.get("optype") == "userpermkwkwission.rolename_pie_v1":
        res = get_pie_v1(
            "select rolename x,count(*) y from vm790_bcfe8a202787453d.userpermkwkwission group by rolename",
            "角色名称",
        )
    if obj.get("optype") == "userpermkwkwission.rolename_pie_v2":
        res = get_pie_v2(
            "select rolename x,count(*) y from vm790_bcfe8a202787453d.userpermkwkwission group by rolename",
            "角色名称",
        )
    if obj.get("optype") == "userpermkwkwission.rolename_line":
        res = get_line(
            "select rolename x,count(*) y from vm790_bcfe8a202787453d.userpermkwkwission group by rolename",
            "角色名称",
        )
    if obj.get("optype") == "userpermkwkwission.rolename_bar":
        res = get_bar(
            "select rolename x,count(*) y from vm790_bcfe8a202787453d.userpermkwkwission group by rolename",
            "角色名称",
        )
    if obj.get("optype") == "userpermkwkwission.rolename_bar_v1":
        res = get_bar_v1(
            "select rolename x,count(*) y from vm790_bcfe8a202787453d.userpermkwkwission group by rolename",
            "角色名称",
        )
    # userpermkwkwission(用户权限表)->permkwkwissionname(权限名称)

    if obj.get("optype") == "userpermkwkwission.permkwkwissionname_pie":
        res = get_pie(
            "select permkwkwissionname x,count(*) y from vm790_bcfe8a202787453d.userpermkwkwission group by permkwkwissionname order by x desc",
            "权限名称",
        )
    if obj.get("optype") == "userpermkwkwission.permkwkwissionname_pie_v1":
        res = get_pie_v1(
            "select permkwkwissionname x,count(*) y from vm790_bcfe8a202787453d.userpermkwkwission group by permkwkwissionname",
            "权限名称",
        )
    if obj.get("optype") == "userpermkwkwission.permkwkwissionname_pie_v2":
        res = get_pie_v2(
            "select permkwkwissionname x,count(*) y from vm790_bcfe8a202787453d.userpermkwkwission group by permkwkwissionname",
            "权限名称",
        )
    if obj.get("optype") == "userpermkwkwission.permkwkwissionname_line":
        res = get_line(
            "select permkwkwissionname x,count(*) y from vm790_bcfe8a202787453d.userpermkwkwission group by permkwkwissionname",
            "权限名称",
        )
    if obj.get("optype") == "userpermkwkwission.permkwkwissionname_bar":
        res = get_bar(
            "select permkwkwissionname x,count(*) y from vm790_bcfe8a202787453d.userpermkwkwission group by permkwkwissionname",
            "权限名称",
        )
    if obj.get("optype") == "userpermkwkwission.permkwkwissionname_bar_v1":
        res = get_bar_v1(
            "select permkwkwissionname x,count(*) y from vm790_bcfe8a202787453d.userpermkwkwission group by permkwkwissionname",
            "权限名称",
        )
    if obj.get("optype") == "userpermkwkwission.createtime_line":
        res = get_line(
            "select createtime x,count(*) y from vm790_bcfe8a202787453d.userpermkwkwission group by createtime order by x",
            "创建时间",
        )
    if obj.get("optype") == "userpermkwkwission.updatetime_line":
        res = get_line(
            "select updatetime x,count(*) y from vm790_bcfe8a202787453d.userpermkwkwission group by updatetime order by x",
            "更新时间",
        )
    # userpermkwkwission(用户权限表)->isactive(是否激活)

    if obj.get("optype") == "userpermkwkwission.isactive_pie":
        res = get_pie(
            "select isactive x,count(*) y from vm790_bcfe8a202787453d.userpermkwkwission group by isactive order by x desc",
            "是否激活",
        )
    if obj.get("optype") == "userpermkwkwission.isactive_pie_v1":
        res = get_pie_v1(
            "select isactive x,count(*) y from vm790_bcfe8a202787453d.userpermkwkwission group by isactive",
            "是否激活",
        )
    if obj.get("optype") == "userpermkwkwission.isactive_pie_v2":
        res = get_pie_v2(
            "select isactive x,count(*) y from vm790_bcfe8a202787453d.userpermkwkwission group by isactive",
            "是否激活",
        )
    if obj.get("optype") == "userpermkwkwission.isactive_line":
        res = get_line(
            "select isactive x,count(*) y from vm790_bcfe8a202787453d.userpermkwkwission group by isactive",
            "是否激活",
        )
    if obj.get("optype") == "userpermkwkwission.isactive_bar":
        res = get_bar(
            "select isactive x,count(*) y from vm790_bcfe8a202787453d.userpermkwkwission group by isactive",
            "是否激活",
        )
    if obj.get("optype") == "userpermkwkwission.isactive_bar_v1":
        res = get_bar_v1(
            "select isactive x,count(*) y from vm790_bcfe8a202787453d.userpermkwkwission group by isactive",
            "是否激活",
        )
    if obj.get("optype") == "userpermkwkwission.description_wordcloud":
        textlist = get_data(
            "SELECT description result FROM vm790_bcfe8a202787453d.userpermkwkwission;"
        )
        res = {
            "title": "词云图",
            "imgbs64": generate_wordcloud_base64(
                ",".join([t["result"] for t in textlist])
            ),
        }
    # userwatchhkwkwistkwkwory(用户观看历史表)->userid(关联用户ID)

    if obj.get("optype") == "userwatchhkwkwistkwkwory.userid_pie":
        res = get_pie(
            "select userid x,count(*) y from vm790_bcfe8a202787453d.userwatchhkwkwistkwkwory group by userid order by x desc",
            "关联用户ID",
        )
    if obj.get("optype") == "userwatchhkwkwistkwkwory.userid_pie_v1":
        res = get_pie_v1(
            "select userid x,count(*) y from vm790_bcfe8a202787453d.userwatchhkwkwistkwkwory group by userid",
            "关联用户ID",
        )
    if obj.get("optype") == "userwatchhkwkwistkwkwory.userid_pie_v2":
        res = get_pie_v2(
            "select userid x,count(*) y from vm790_bcfe8a202787453d.userwatchhkwkwistkwkwory group by userid",
            "关联用户ID",
        )
    if obj.get("optype") == "userwatchhkwkwistkwkwory.userid_line":
        res = get_line(
            "select userid x,count(*) y from vm790_bcfe8a202787453d.userwatchhkwkwistkwkwory group by userid",
            "关联用户ID",
        )
    if obj.get("optype") == "userwatchhkwkwistkwkwory.userid_bar":
        res = get_bar(
            "select userid x,count(*) y from vm790_bcfe8a202787453d.userwatchhkwkwistkwkwory group by userid",
            "关联用户ID",
        )
    if obj.get("optype") == "userwatchhkwkwistkwkwory.userid_bar_v1":
        res = get_bar_v1(
            "select userid x,count(*) y from vm790_bcfe8a202787453d.userwatchhkwkwistkwkwory group by userid",
            "关联用户ID",
        )
    # userwatchhkwkwistkwkwory(用户观看历史表)->videoid(关联视频ID)

    if obj.get("optype") == "userwatchhkwkwistkwkwory.videoid_pie":
        res = get_pie(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.userwatchhkwkwistkwkwory group by videoid order by x desc",
            "关联视频ID",
        )
    if obj.get("optype") == "userwatchhkwkwistkwkwory.videoid_pie_v1":
        res = get_pie_v1(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.userwatchhkwkwistkwkwory group by videoid",
            "关联视频ID",
        )
    if obj.get("optype") == "userwatchhkwkwistkwkwory.videoid_pie_v2":
        res = get_pie_v2(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.userwatchhkwkwistkwkwory group by videoid",
            "关联视频ID",
        )
    if obj.get("optype") == "userwatchhkwkwistkwkwory.videoid_line":
        res = get_line(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.userwatchhkwkwistkwkwory group by videoid",
            "关联视频ID",
        )
    if obj.get("optype") == "userwatchhkwkwistkwkwory.videoid_bar":
        res = get_bar(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.userwatchhkwkwistkwkwory group by videoid",
            "关联视频ID",
        )
    if obj.get("optype") == "userwatchhkwkwistkwkwory.videoid_bar_v1":
        res = get_bar_v1(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.userwatchhkwkwistkwkwory group by videoid",
            "关联视频ID",
        )
    if obj.get("optype") == "userwatchhkwkwistkwkwory.watchtime_line":
        res = get_line(
            "select watchtime x,count(*) y from vm790_bcfe8a202787453d.userwatchhkwkwistkwkwory group by watchtime order by x",
            "观看时间",
        )
    # userwatchhkwkwistkwkwory(用户观看历史表)->watchduration(观看时长)

    if obj.get("optype") == "userwatchhkwkwistkwkwory.watchduration_pie":
        res = get_pie(
            "select watchduration x,count(*) y from vm790_bcfe8a202787453d.userwatchhkwkwistkwkwory group by watchduration order by x desc",
            "观看时长",
        )
    if obj.get("optype") == "userwatchhkwkwistkwkwory.watchduration_pie_v1":
        res = get_pie_v1(
            "select watchduration x,count(*) y from vm790_bcfe8a202787453d.userwatchhkwkwistkwkwory group by watchduration",
            "观看时长",
        )
    if obj.get("optype") == "userwatchhkwkwistkwkwory.watchduration_pie_v2":
        res = get_pie_v2(
            "select watchduration x,count(*) y from vm790_bcfe8a202787453d.userwatchhkwkwistkwkwory group by watchduration",
            "观看时长",
        )
    if obj.get("optype") == "userwatchhkwkwistkwkwory.watchduration_line":
        res = get_line(
            "select watchduration x,count(*) y from vm790_bcfe8a202787453d.userwatchhkwkwistkwkwory group by watchduration",
            "观看时长",
        )
    if obj.get("optype") == "userwatchhkwkwistkwkwory.watchduration_bar":
        res = get_bar(
            "select watchduration x,count(*) y from vm790_bcfe8a202787453d.userwatchhkwkwistkwkwory group by watchduration",
            "观看时长",
        )
    if obj.get("optype") == "userwatchhkwkwistkwkwory.watchduration_bar_v1":
        res = get_bar_v1(
            "select watchduration x,count(*) y from vm790_bcfe8a202787453d.userwatchhkwkwistkwkwory group by watchduration",
            "观看时长",
        )
    # userwatchhkwkwistkwkwory(用户观看历史表)->watchstatus(观看状态如已观看、观看中、暂停、已放弃)

    if obj.get("optype") == "userwatchhkwkwistkwkwory.watchstatus_pie":
        res = get_pie(
            "select watchstatus x,count(*) y from vm790_bcfe8a202787453d.userwatchhkwkwistkwkwory group by watchstatus order by x desc",
            "观看状态如已观看、观看中、暂停、已放弃",
        )
    if obj.get("optype") == "userwatchhkwkwistkwkwory.watchstatus_pie_v1":
        res = get_pie_v1(
            "select watchstatus x,count(*) y from vm790_bcfe8a202787453d.userwatchhkwkwistkwkwory group by watchstatus",
            "观看状态如已观看、观看中、暂停、已放弃",
        )
    if obj.get("optype") == "userwatchhkwkwistkwkwory.watchstatus_pie_v2":
        res = get_pie_v2(
            "select watchstatus x,count(*) y from vm790_bcfe8a202787453d.userwatchhkwkwistkwkwory group by watchstatus",
            "观看状态如已观看、观看中、暂停、已放弃",
        )
    if obj.get("optype") == "userwatchhkwkwistkwkwory.watchstatus_line":
        res = get_line(
            "select watchstatus x,count(*) y from vm790_bcfe8a202787453d.userwatchhkwkwistkwkwory group by watchstatus",
            "观看状态如已观看、观看中、暂停、已放弃",
        )
    if obj.get("optype") == "userwatchhkwkwistkwkwory.watchstatus_bar":
        res = get_bar(
            "select watchstatus x,count(*) y from vm790_bcfe8a202787453d.userwatchhkwkwistkwkwory group by watchstatus",
            "观看状态如已观看、观看中、暂停、已放弃",
        )
    if obj.get("optype") == "userwatchhkwkwistkwkwory.watchstatus_bar_v1":
        res = get_bar_v1(
            "select watchstatus x,count(*) y from vm790_bcfe8a202787453d.userwatchhkwkwistkwkwory group by watchstatus",
            "观看状态如已观看、观看中、暂停、已放弃",
        )
    # userwatchhkwkwistkwkwory(用户观看历史表)->ratkwkwing(评分可选用户对该视频的评分)

    if obj.get("optype") == "userwatchhkwkwistkwkwory.ratkwkwing_pie":
        res = get_pie(
            "select ratkwkwing x,count(*) y from vm790_bcfe8a202787453d.userwatchhkwkwistkwkwory group by ratkwkwing order by x desc",
            "评分可选用户对该视频的评分",
        )
    if obj.get("optype") == "userwatchhkwkwistkwkwory.ratkwkwing_pie_v1":
        res = get_pie_v1(
            "select ratkwkwing x,count(*) y from vm790_bcfe8a202787453d.userwatchhkwkwistkwkwory group by ratkwkwing",
            "评分可选用户对该视频的评分",
        )
    if obj.get("optype") == "userwatchhkwkwistkwkwory.ratkwkwing_pie_v2":
        res = get_pie_v2(
            "select ratkwkwing x,count(*) y from vm790_bcfe8a202787453d.userwatchhkwkwistkwkwory group by ratkwkwing",
            "评分可选用户对该视频的评分",
        )
    if obj.get("optype") == "userwatchhkwkwistkwkwory.ratkwkwing_line":
        res = get_line(
            "select ratkwkwing x,count(*) y from vm790_bcfe8a202787453d.userwatchhkwkwistkwkwory group by ratkwkwing",
            "评分可选用户对该视频的评分",
        )
    if obj.get("optype") == "userwatchhkwkwistkwkwory.ratkwkwing_bar":
        res = get_bar(
            "select ratkwkwing x,count(*) y from vm790_bcfe8a202787453d.userwatchhkwkwistkwkwory group by ratkwkwing",
            "评分可选用户对该视频的评分",
        )
    if obj.get("optype") == "userwatchhkwkwistkwkwory.ratkwkwing_bar_v1":
        res = get_bar_v1(
            "select ratkwkwing x,count(*) y from vm790_bcfe8a202787453d.userwatchhkwkwistkwkwory group by ratkwkwing",
            "评分可选用户对该视频的评分",
        )
    if obj.get("optype") == "userwatchhkwkwistkwkwory.comment_wordcloud":
        textlist = get_data(
            "SELECT comment result FROM vm790_bcfe8a202787453d.userwatchhkwkwistkwkwory;"
        )
        res = {
            "title": "词云图",
            "imgbs64": generate_wordcloud_base64(
                ",".join([t["result"] for t in textlist])
            ),
        }
    # userwatchhkwkwistkwkwory(用户观看历史表)->likestatus(点赞状态如已点赞、未点赞)

    if obj.get("optype") == "userwatchhkwkwistkwkwory.likestatus_pie":
        res = get_pie(
            "select likestatus x,count(*) y from vm790_bcfe8a202787453d.userwatchhkwkwistkwkwory group by likestatus order by x desc",
            "点赞状态如已点赞、未点赞",
        )
    if obj.get("optype") == "userwatchhkwkwistkwkwory.likestatus_pie_v1":
        res = get_pie_v1(
            "select likestatus x,count(*) y from vm790_bcfe8a202787453d.userwatchhkwkwistkwkwory group by likestatus",
            "点赞状态如已点赞、未点赞",
        )
    if obj.get("optype") == "userwatchhkwkwistkwkwory.likestatus_pie_v2":
        res = get_pie_v2(
            "select likestatus x,count(*) y from vm790_bcfe8a202787453d.userwatchhkwkwistkwkwory group by likestatus",
            "点赞状态如已点赞、未点赞",
        )
    if obj.get("optype") == "userwatchhkwkwistkwkwory.likestatus_line":
        res = get_line(
            "select likestatus x,count(*) y from vm790_bcfe8a202787453d.userwatchhkwkwistkwkwory group by likestatus",
            "点赞状态如已点赞、未点赞",
        )
    if obj.get("optype") == "userwatchhkwkwistkwkwory.likestatus_bar":
        res = get_bar(
            "select likestatus x,count(*) y from vm790_bcfe8a202787453d.userwatchhkwkwistkwkwory group by likestatus",
            "点赞状态如已点赞、未点赞",
        )
    if obj.get("optype") == "userwatchhkwkwistkwkwory.likestatus_bar_v1":
        res = get_bar_v1(
            "select likestatus x,count(*) y from vm790_bcfe8a202787453d.userwatchhkwkwistkwkwory group by likestatus",
            "点赞状态如已点赞、未点赞",
        )
    # userwatchhkwkwistkwkwory(用户观看历史表)->sharestatus(分享状态如已分享、未分享)

    if obj.get("optype") == "userwatchhkwkwistkwkwory.sharestatus_pie":
        res = get_pie(
            "select sharestatus x,count(*) y from vm790_bcfe8a202787453d.userwatchhkwkwistkwkwory group by sharestatus order by x desc",
            "分享状态如已分享、未分享",
        )
    if obj.get("optype") == "userwatchhkwkwistkwkwory.sharestatus_pie_v1":
        res = get_pie_v1(
            "select sharestatus x,count(*) y from vm790_bcfe8a202787453d.userwatchhkwkwistkwkwory group by sharestatus",
            "分享状态如已分享、未分享",
        )
    if obj.get("optype") == "userwatchhkwkwistkwkwory.sharestatus_pie_v2":
        res = get_pie_v2(
            "select sharestatus x,count(*) y from vm790_bcfe8a202787453d.userwatchhkwkwistkwkwory group by sharestatus",
            "分享状态如已分享、未分享",
        )
    if obj.get("optype") == "userwatchhkwkwistkwkwory.sharestatus_line":
        res = get_line(
            "select sharestatus x,count(*) y from vm790_bcfe8a202787453d.userwatchhkwkwistkwkwory group by sharestatus",
            "分享状态如已分享、未分享",
        )
    if obj.get("optype") == "userwatchhkwkwistkwkwory.sharestatus_bar":
        res = get_bar(
            "select sharestatus x,count(*) y from vm790_bcfe8a202787453d.userwatchhkwkwistkwkwory group by sharestatus",
            "分享状态如已分享、未分享",
        )
    if obj.get("optype") == "userwatchhkwkwistkwkwory.sharestatus_bar_v1":
        res = get_bar_v1(
            "select sharestatus x,count(*) y from vm790_bcfe8a202787453d.userwatchhkwkwistkwkwory group by sharestatus",
            "分享状态如已分享、未分享",
        )
    # userwatchhkwkwistkwkwory(用户观看历史表)->favkwkworitestatus(收藏状态如已收藏、未收藏)

    if obj.get("optype") == "userwatchhkwkwistkwkwory.favkwkworitestatus_pie":
        res = get_pie(
            "select favkwkworitestatus x,count(*) y from vm790_bcfe8a202787453d.userwatchhkwkwistkwkwory group by favkwkworitestatus order by x desc",
            "收藏状态如已收藏、未收藏",
        )
    if obj.get("optype") == "userwatchhkwkwistkwkwory.favkwkworitestatus_pie_v1":
        res = get_pie_v1(
            "select favkwkworitestatus x,count(*) y from vm790_bcfe8a202787453d.userwatchhkwkwistkwkwory group by favkwkworitestatus",
            "收藏状态如已收藏、未收藏",
        )
    if obj.get("optype") == "userwatchhkwkwistkwkwory.favkwkworitestatus_pie_v2":
        res = get_pie_v2(
            "select favkwkworitestatus x,count(*) y from vm790_bcfe8a202787453d.userwatchhkwkwistkwkwory group by favkwkworitestatus",
            "收藏状态如已收藏、未收藏",
        )
    if obj.get("optype") == "userwatchhkwkwistkwkwory.favkwkworitestatus_line":
        res = get_line(
            "select favkwkworitestatus x,count(*) y from vm790_bcfe8a202787453d.userwatchhkwkwistkwkwory group by favkwkworitestatus",
            "收藏状态如已收藏、未收藏",
        )
    if obj.get("optype") == "userwatchhkwkwistkwkwory.favkwkworitestatus_bar":
        res = get_bar(
            "select favkwkworitestatus x,count(*) y from vm790_bcfe8a202787453d.userwatchhkwkwistkwkwory group by favkwkworitestatus",
            "收藏状态如已收藏、未收藏",
        )
    if obj.get("optype") == "userwatchhkwkwistkwkwory.favkwkworitestatus_bar_v1":
        res = get_bar_v1(
            "select favkwkworitestatus x,count(*) y from vm790_bcfe8a202787453d.userwatchhkwkwistkwkwory group by favkwkworitestatus",
            "收藏状态如已收藏、未收藏",
        )
    # videoauditstatus(视频审核状态表)->videoid(视频ID关联字段指向视频的ID)

    if obj.get("optype") == "videoauditstatus.videoid_pie":
        res = get_pie(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videoauditstatus group by videoid order by x desc",
            "视频ID关联字段指向视频的ID",
        )
    if obj.get("optype") == "videoauditstatus.videoid_pie_v1":
        res = get_pie_v1(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videoauditstatus group by videoid",
            "视频ID关联字段指向视频的ID",
        )
    if obj.get("optype") == "videoauditstatus.videoid_pie_v2":
        res = get_pie_v2(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videoauditstatus group by videoid",
            "视频ID关联字段指向视频的ID",
        )
    if obj.get("optype") == "videoauditstatus.videoid_line":
        res = get_line(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videoauditstatus group by videoid",
            "视频ID关联字段指向视频的ID",
        )
    if obj.get("optype") == "videoauditstatus.videoid_bar":
        res = get_bar(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videoauditstatus group by videoid",
            "视频ID关联字段指向视频的ID",
        )
    if obj.get("optype") == "videoauditstatus.videoid_bar_v1":
        res = get_bar_v1(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videoauditstatus group by videoid",
            "视频ID关联字段指向视频的ID",
        )
    # videoauditstatus(视频审核状态表)->status(审核状态如待审核、审核通过、审核拒绝)

    if obj.get("optype") == "videoauditstatus.status_pie":
        res = get_pie(
            "select status x,count(*) y from vm790_bcfe8a202787453d.videoauditstatus group by status order by x desc",
            "审核状态如待审核、审核通过、审核拒绝",
        )
    if obj.get("optype") == "videoauditstatus.status_pie_v1":
        res = get_pie_v1(
            "select status x,count(*) y from vm790_bcfe8a202787453d.videoauditstatus group by status",
            "审核状态如待审核、审核通过、审核拒绝",
        )
    if obj.get("optype") == "videoauditstatus.status_pie_v2":
        res = get_pie_v2(
            "select status x,count(*) y from vm790_bcfe8a202787453d.videoauditstatus group by status",
            "审核状态如待审核、审核通过、审核拒绝",
        )
    if obj.get("optype") == "videoauditstatus.status_line":
        res = get_line(
            "select status x,count(*) y from vm790_bcfe8a202787453d.videoauditstatus group by status",
            "审核状态如待审核、审核通过、审核拒绝",
        )
    if obj.get("optype") == "videoauditstatus.status_bar":
        res = get_bar(
            "select status x,count(*) y from vm790_bcfe8a202787453d.videoauditstatus group by status",
            "审核状态如待审核、审核通过、审核拒绝",
        )
    if obj.get("optype") == "videoauditstatus.status_bar_v1":
        res = get_bar_v1(
            "select status x,count(*) y from vm790_bcfe8a202787453d.videoauditstatus group by status",
            "审核状态如待审核、审核通过、审核拒绝",
        )
    # videoauditstatus(视频审核状态表)->reviewerid(审核员ID关联字段指向审核员的ID)

    if obj.get("optype") == "videoauditstatus.reviewerid_pie":
        res = get_pie(
            "select reviewerid x,count(*) y from vm790_bcfe8a202787453d.videoauditstatus group by reviewerid order by x desc",
            "审核员ID关联字段指向审核员的ID",
        )
    if obj.get("optype") == "videoauditstatus.reviewerid_pie_v1":
        res = get_pie_v1(
            "select reviewerid x,count(*) y from vm790_bcfe8a202787453d.videoauditstatus group by reviewerid",
            "审核员ID关联字段指向审核员的ID",
        )
    if obj.get("optype") == "videoauditstatus.reviewerid_pie_v2":
        res = get_pie_v2(
            "select reviewerid x,count(*) y from vm790_bcfe8a202787453d.videoauditstatus group by reviewerid",
            "审核员ID关联字段指向审核员的ID",
        )
    if obj.get("optype") == "videoauditstatus.reviewerid_line":
        res = get_line(
            "select reviewerid x,count(*) y from vm790_bcfe8a202787453d.videoauditstatus group by reviewerid",
            "审核员ID关联字段指向审核员的ID",
        )
    if obj.get("optype") == "videoauditstatus.reviewerid_bar":
        res = get_bar(
            "select reviewerid x,count(*) y from vm790_bcfe8a202787453d.videoauditstatus group by reviewerid",
            "审核员ID关联字段指向审核员的ID",
        )
    if obj.get("optype") == "videoauditstatus.reviewerid_bar_v1":
        res = get_bar_v1(
            "select reviewerid x,count(*) y from vm790_bcfe8a202787453d.videoauditstatus group by reviewerid",
            "审核员ID关联字段指向审核员的ID",
        )
    if obj.get("optype") == "videoauditstatus.reviewtime_line":
        res = get_line(
            "select reviewtime x,count(*) y from vm790_bcfe8a202787453d.videoauditstatus group by reviewtime order by x",
            "审核时间",
        )
    # videoauditstatus(视频审核状态表)->rejectrekwkwason(拒绝原因如果状态为审核拒绝则记录拒绝的具体原因)

    if obj.get("optype") == "videoauditstatus.rejectrekwkwason_pie":
        res = get_pie(
            "select rejectrekwkwason x,count(*) y from vm790_bcfe8a202787453d.videoauditstatus group by rejectrekwkwason order by x desc",
            "拒绝原因如果状态为审核拒绝则记录拒绝的具体原因",
        )
    if obj.get("optype") == "videoauditstatus.rejectrekwkwason_pie_v1":
        res = get_pie_v1(
            "select rejectrekwkwason x,count(*) y from vm790_bcfe8a202787453d.videoauditstatus group by rejectrekwkwason",
            "拒绝原因如果状态为审核拒绝则记录拒绝的具体原因",
        )
    if obj.get("optype") == "videoauditstatus.rejectrekwkwason_pie_v2":
        res = get_pie_v2(
            "select rejectrekwkwason x,count(*) y from vm790_bcfe8a202787453d.videoauditstatus group by rejectrekwkwason",
            "拒绝原因如果状态为审核拒绝则记录拒绝的具体原因",
        )
    if obj.get("optype") == "videoauditstatus.rejectrekwkwason_line":
        res = get_line(
            "select rejectrekwkwason x,count(*) y from vm790_bcfe8a202787453d.videoauditstatus group by rejectrekwkwason",
            "拒绝原因如果状态为审核拒绝则记录拒绝的具体原因",
        )
    if obj.get("optype") == "videoauditstatus.rejectrekwkwason_bar":
        res = get_bar(
            "select rejectrekwkwason x,count(*) y from vm790_bcfe8a202787453d.videoauditstatus group by rejectrekwkwason",
            "拒绝原因如果状态为审核拒绝则记录拒绝的具体原因",
        )
    if obj.get("optype") == "videoauditstatus.rejectrekwkwason_bar_v1":
        res = get_bar_v1(
            "select rejectrekwkwason x,count(*) y from vm790_bcfe8a202787453d.videoauditstatus group by rejectrekwkwason",
            "拒绝原因如果状态为审核拒绝则记录拒绝的具体原因",
        )
    # videoauditstatus(视频审核状态表)->comment(审核备注)

    if obj.get("optype") == "videoauditstatus.comment_pie":
        res = get_pie(
            "select comment x,count(*) y from vm790_bcfe8a202787453d.videoauditstatus group by comment order by x desc",
            "审核备注",
        )
    if obj.get("optype") == "videoauditstatus.comment_pie_v1":
        res = get_pie_v1(
            "select comment x,count(*) y from vm790_bcfe8a202787453d.videoauditstatus group by comment",
            "审核备注",
        )
    if obj.get("optype") == "videoauditstatus.comment_pie_v2":
        res = get_pie_v2(
            "select comment x,count(*) y from vm790_bcfe8a202787453d.videoauditstatus group by comment",
            "审核备注",
        )
    if obj.get("optype") == "videoauditstatus.comment_line":
        res = get_line(
            "select comment x,count(*) y from vm790_bcfe8a202787453d.videoauditstatus group by comment",
            "审核备注",
        )
    if obj.get("optype") == "videoauditstatus.comment_bar":
        res = get_bar(
            "select comment x,count(*) y from vm790_bcfe8a202787453d.videoauditstatus group by comment",
            "审核备注",
        )
    if obj.get("optype") == "videoauditstatus.comment_bar_v1":
        res = get_bar_v1(
            "select comment x,count(*) y from vm790_bcfe8a202787453d.videoauditstatus group by comment",
            "审核备注",
        )
    # videoauditstatus(视频审核状态表)->kwkwisfkwkwinal(是否最终审核标记该审核是否为最终审核结果)

    if obj.get("optype") == "videoauditstatus.kwkwisfkwkwinal_pie":
        res = get_pie(
            "select kwkwisfkwkwinal x,count(*) y from vm790_bcfe8a202787453d.videoauditstatus group by kwkwisfkwkwinal order by x desc",
            "是否最终审核标记该审核是否为最终审核结果",
        )
    if obj.get("optype") == "videoauditstatus.kwkwisfkwkwinal_pie_v1":
        res = get_pie_v1(
            "select kwkwisfkwkwinal x,count(*) y from vm790_bcfe8a202787453d.videoauditstatus group by kwkwisfkwkwinal",
            "是否最终审核标记该审核是否为最终审核结果",
        )
    if obj.get("optype") == "videoauditstatus.kwkwisfkwkwinal_pie_v2":
        res = get_pie_v2(
            "select kwkwisfkwkwinal x,count(*) y from vm790_bcfe8a202787453d.videoauditstatus group by kwkwisfkwkwinal",
            "是否最终审核标记该审核是否为最终审核结果",
        )
    if obj.get("optype") == "videoauditstatus.kwkwisfkwkwinal_line":
        res = get_line(
            "select kwkwisfkwkwinal x,count(*) y from vm790_bcfe8a202787453d.videoauditstatus group by kwkwisfkwkwinal",
            "是否最终审核标记该审核是否为最终审核结果",
        )
    if obj.get("optype") == "videoauditstatus.kwkwisfkwkwinal_bar":
        res = get_bar(
            "select kwkwisfkwkwinal x,count(*) y from vm790_bcfe8a202787453d.videoauditstatus group by kwkwisfkwkwinal",
            "是否最终审核标记该审核是否为最终审核结果",
        )
    if obj.get("optype") == "videoauditstatus.kwkwisfkwkwinal_bar_v1":
        res = get_bar_v1(
            "select kwkwisfkwkwinal x,count(*) y from vm790_bcfe8a202787453d.videoauditstatus group by kwkwisfkwkwinal",
            "是否最终审核标记该审核是否为最终审核结果",
        )
    if obj.get("optype") == "videoauditstatus.createdat_line":
        res = get_line(
            "select createdat x,count(*) y from vm790_bcfe8a202787453d.videoauditstatus group by createdat order by x",
            "创建时间",
        )
    if obj.get("optype") == "videoauditstatus.updatedat_line":
        res = get_line(
            "select updatedat x,count(*) y from vm790_bcfe8a202787453d.videoauditstatus group by updatedat order by x",
            "更新时间",
        )
    # videocoverimage(视频封面图片表)->videoid(视频ID关联字段指向视频的)

    if obj.get("optype") == "videocoverimage.videoid_pie":
        res = get_pie(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videocoverimage group by videoid order by x desc",
            "视频ID关联字段指向视频的",
        )
    if obj.get("optype") == "videocoverimage.videoid_pie_v1":
        res = get_pie_v1(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videocoverimage group by videoid",
            "视频ID关联字段指向视频的",
        )
    if obj.get("optype") == "videocoverimage.videoid_pie_v2":
        res = get_pie_v2(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videocoverimage group by videoid",
            "视频ID关联字段指向视频的",
        )
    if obj.get("optype") == "videocoverimage.videoid_line":
        res = get_line(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videocoverimage group by videoid",
            "视频ID关联字段指向视频的",
        )
    if obj.get("optype") == "videocoverimage.videoid_bar":
        res = get_bar(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videocoverimage group by videoid",
            "视频ID关联字段指向视频的",
        )
    if obj.get("optype") == "videocoverimage.videoid_bar_v1":
        res = get_bar_v1(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videocoverimage group by videoid",
            "视频ID关联字段指向视频的",
        )
    # videocoverimage(视频封面图片表)->coverimageurl(封面图片URL)

    if obj.get("optype") == "videocoverimage.coverimageurl_pie":
        res = get_pie(
            "select coverimageurl x,count(*) y from vm790_bcfe8a202787453d.videocoverimage group by coverimageurl order by x desc",
            "封面图片URL",
        )
    if obj.get("optype") == "videocoverimage.coverimageurl_pie_v1":
        res = get_pie_v1(
            "select coverimageurl x,count(*) y from vm790_bcfe8a202787453d.videocoverimage group by coverimageurl",
            "封面图片URL",
        )
    if obj.get("optype") == "videocoverimage.coverimageurl_pie_v2":
        res = get_pie_v2(
            "select coverimageurl x,count(*) y from vm790_bcfe8a202787453d.videocoverimage group by coverimageurl",
            "封面图片URL",
        )
    if obj.get("optype") == "videocoverimage.coverimageurl_line":
        res = get_line(
            "select coverimageurl x,count(*) y from vm790_bcfe8a202787453d.videocoverimage group by coverimageurl",
            "封面图片URL",
        )
    if obj.get("optype") == "videocoverimage.coverimageurl_bar":
        res = get_bar(
            "select coverimageurl x,count(*) y from vm790_bcfe8a202787453d.videocoverimage group by coverimageurl",
            "封面图片URL",
        )
    if obj.get("optype") == "videocoverimage.coverimageurl_bar_v1":
        res = get_bar_v1(
            "select coverimageurl x,count(*) y from vm790_bcfe8a202787453d.videocoverimage group by coverimageurl",
            "封面图片URL",
        )
    # videocoverimage(视频封面图片表)->imagekwkwfkwkwormat(图片格式)

    if obj.get("optype") == "videocoverimage.imagekwkwfkwkwormat_pie":
        res = get_pie(
            "select imagekwkwfkwkwormat x,count(*) y from vm790_bcfe8a202787453d.videocoverimage group by imagekwkwfkwkwormat order by x desc",
            "图片格式",
        )
    if obj.get("optype") == "videocoverimage.imagekwkwfkwkwormat_pie_v1":
        res = get_pie_v1(
            "select imagekwkwfkwkwormat x,count(*) y from vm790_bcfe8a202787453d.videocoverimage group by imagekwkwfkwkwormat",
            "图片格式",
        )
    if obj.get("optype") == "videocoverimage.imagekwkwfkwkwormat_pie_v2":
        res = get_pie_v2(
            "select imagekwkwfkwkwormat x,count(*) y from vm790_bcfe8a202787453d.videocoverimage group by imagekwkwfkwkwormat",
            "图片格式",
        )
    if obj.get("optype") == "videocoverimage.imagekwkwfkwkwormat_line":
        res = get_line(
            "select imagekwkwfkwkwormat x,count(*) y from vm790_bcfe8a202787453d.videocoverimage group by imagekwkwfkwkwormat",
            "图片格式",
        )
    if obj.get("optype") == "videocoverimage.imagekwkwfkwkwormat_bar":
        res = get_bar(
            "select imagekwkwfkwkwormat x,count(*) y from vm790_bcfe8a202787453d.videocoverimage group by imagekwkwfkwkwormat",
            "图片格式",
        )
    if obj.get("optype") == "videocoverimage.imagekwkwfkwkwormat_bar_v1":
        res = get_bar_v1(
            "select imagekwkwfkwkwormat x,count(*) y from vm790_bcfe8a202787453d.videocoverimage group by imagekwkwfkwkwormat",
            "图片格式",
        )
    # videocoverimage(视频封面图片表)->imagesize(图片大小单位KB)

    if obj.get("optype") == "videocoverimage.imagesize_pie":
        res = get_pie(
            "select imagesize x,count(*) y from vm790_bcfe8a202787453d.videocoverimage group by imagesize order by x desc",
            "图片大小单位KB",
        )
    if obj.get("optype") == "videocoverimage.imagesize_pie_v1":
        res = get_pie_v1(
            "select imagesize x,count(*) y from vm790_bcfe8a202787453d.videocoverimage group by imagesize",
            "图片大小单位KB",
        )
    if obj.get("optype") == "videocoverimage.imagesize_pie_v2":
        res = get_pie_v2(
            "select imagesize x,count(*) y from vm790_bcfe8a202787453d.videocoverimage group by imagesize",
            "图片大小单位KB",
        )
    if obj.get("optype") == "videocoverimage.imagesize_line":
        res = get_line(
            "select imagesize x,count(*) y from vm790_bcfe8a202787453d.videocoverimage group by imagesize",
            "图片大小单位KB",
        )
    if obj.get("optype") == "videocoverimage.imagesize_bar":
        res = get_bar(
            "select imagesize x,count(*) y from vm790_bcfe8a202787453d.videocoverimage group by imagesize",
            "图片大小单位KB",
        )
    if obj.get("optype") == "videocoverimage.imagesize_bar_v1":
        res = get_bar_v1(
            "select imagesize x,count(*) y from vm790_bcfe8a202787453d.videocoverimage group by imagesize",
            "图片大小单位KB",
        )
    if obj.get("optype") == "videocoverimage.uploadtime_line":
        res = get_line(
            "select uploadtime x,count(*) y from vm790_bcfe8a202787453d.videocoverimage group by uploadtime order by x",
            "上传时间",
        )
    # videocoverimage(视频封面图片表)->creatkwkworid(创建者ID关联字段指向用户的)

    if obj.get("optype") == "videocoverimage.creatkwkworid_pie":
        res = get_pie(
            "select creatkwkworid x,count(*) y from vm790_bcfe8a202787453d.videocoverimage group by creatkwkworid order by x desc",
            "创建者ID关联字段指向用户的",
        )
    if obj.get("optype") == "videocoverimage.creatkwkworid_pie_v1":
        res = get_pie_v1(
            "select creatkwkworid x,count(*) y from vm790_bcfe8a202787453d.videocoverimage group by creatkwkworid",
            "创建者ID关联字段指向用户的",
        )
    if obj.get("optype") == "videocoverimage.creatkwkworid_pie_v2":
        res = get_pie_v2(
            "select creatkwkworid x,count(*) y from vm790_bcfe8a202787453d.videocoverimage group by creatkwkworid",
            "创建者ID关联字段指向用户的",
        )
    if obj.get("optype") == "videocoverimage.creatkwkworid_line":
        res = get_line(
            "select creatkwkworid x,count(*) y from vm790_bcfe8a202787453d.videocoverimage group by creatkwkworid",
            "创建者ID关联字段指向用户的",
        )
    if obj.get("optype") == "videocoverimage.creatkwkworid_bar":
        res = get_bar(
            "select creatkwkworid x,count(*) y from vm790_bcfe8a202787453d.videocoverimage group by creatkwkworid",
            "创建者ID关联字段指向用户的",
        )
    if obj.get("optype") == "videocoverimage.creatkwkworid_bar_v1":
        res = get_bar_v1(
            "select creatkwkworid x,count(*) y from vm790_bcfe8a202787453d.videocoverimage group by creatkwkworid",
            "创建者ID关联字段指向用户的",
        )
    # videocoverimage(视频封面图片表)->status(状态例如有效、无效、待审核)

    if obj.get("optype") == "videocoverimage.status_pie":
        res = get_pie(
            "select status x,count(*) y from vm790_bcfe8a202787453d.videocoverimage group by status order by x desc",
            "状态例如有效、无效、待审核",
        )
    if obj.get("optype") == "videocoverimage.status_pie_v1":
        res = get_pie_v1(
            "select status x,count(*) y from vm790_bcfe8a202787453d.videocoverimage group by status",
            "状态例如有效、无效、待审核",
        )
    if obj.get("optype") == "videocoverimage.status_pie_v2":
        res = get_pie_v2(
            "select status x,count(*) y from vm790_bcfe8a202787453d.videocoverimage group by status",
            "状态例如有效、无效、待审核",
        )
    if obj.get("optype") == "videocoverimage.status_line":
        res = get_line(
            "select status x,count(*) y from vm790_bcfe8a202787453d.videocoverimage group by status",
            "状态例如有效、无效、待审核",
        )
    if obj.get("optype") == "videocoverimage.status_bar":
        res = get_bar(
            "select status x,count(*) y from vm790_bcfe8a202787453d.videocoverimage group by status",
            "状态例如有效、无效、待审核",
        )
    if obj.get("optype") == "videocoverimage.status_bar_v1":
        res = get_bar_v1(
            "select status x,count(*) y from vm790_bcfe8a202787453d.videocoverimage group by status",
            "状态例如有效、无效、待审核",
        )
    # videocoverimage(视频封面图片表)->description(图片描述)

    if obj.get("optype") == "videocoverimage.description_pie":
        res = get_pie(
            "select description x,count(*) y from vm790_bcfe8a202787453d.videocoverimage group by description order by x desc",
            "图片描述",
        )
    if obj.get("optype") == "videocoverimage.description_pie_v1":
        res = get_pie_v1(
            "select description x,count(*) y from vm790_bcfe8a202787453d.videocoverimage group by description",
            "图片描述",
        )
    if obj.get("optype") == "videocoverimage.description_pie_v2":
        res = get_pie_v2(
            "select description x,count(*) y from vm790_bcfe8a202787453d.videocoverimage group by description",
            "图片描述",
        )
    if obj.get("optype") == "videocoverimage.description_line":
        res = get_line(
            "select description x,count(*) y from vm790_bcfe8a202787453d.videocoverimage group by description",
            "图片描述",
        )
    if obj.get("optype") == "videocoverimage.description_bar":
        res = get_bar(
            "select description x,count(*) y from vm790_bcfe8a202787453d.videocoverimage group by description",
            "图片描述",
        )
    if obj.get("optype") == "videocoverimage.description_bar_v1":
        res = get_bar_v1(
            "select description x,count(*) y from vm790_bcfe8a202787453d.videocoverimage group by description",
            "图片描述",
        )
    # videocoverimage(视频封面图片表)->kwkwiskwkwdefault(是否为默认封面kwTruekwFalse)

    if obj.get("optype") == "videocoverimage.kwkwiskwkwdefault_pie":
        res = get_pie(
            "select kwkwiskwkwdefault x,count(*) y from vm790_bcfe8a202787453d.videocoverimage group by kwkwiskwkwdefault order by x desc",
            "是否为默认封面kwTruekwFalse",
        )
    if obj.get("optype") == "videocoverimage.kwkwiskwkwdefault_pie_v1":
        res = get_pie_v1(
            "select kwkwiskwkwdefault x,count(*) y from vm790_bcfe8a202787453d.videocoverimage group by kwkwiskwkwdefault",
            "是否为默认封面kwTruekwFalse",
        )
    if obj.get("optype") == "videocoverimage.kwkwiskwkwdefault_pie_v2":
        res = get_pie_v2(
            "select kwkwiskwkwdefault x,count(*) y from vm790_bcfe8a202787453d.videocoverimage group by kwkwiskwkwdefault",
            "是否为默认封面kwTruekwFalse",
        )
    if obj.get("optype") == "videocoverimage.kwkwiskwkwdefault_line":
        res = get_line(
            "select kwkwiskwkwdefault x,count(*) y from vm790_bcfe8a202787453d.videocoverimage group by kwkwiskwkwdefault",
            "是否为默认封面kwTruekwFalse",
        )
    if obj.get("optype") == "videocoverimage.kwkwiskwkwdefault_bar":
        res = get_bar(
            "select kwkwiskwkwdefault x,count(*) y from vm790_bcfe8a202787453d.videocoverimage group by kwkwiskwkwdefault",
            "是否为默认封面kwTruekwFalse",
        )
    if obj.get("optype") == "videocoverimage.kwkwiskwkwdefault_bar_v1":
        res = get_bar_v1(
            "select kwkwiskwkwdefault x,count(*) y from vm790_bcfe8a202787453d.videocoverimage group by kwkwiskwkwdefault",
            "是否为默认封面kwTruekwFalse",
        )
    # videomatrixconfig(视频矩阵配置表)->matrixname(视频矩阵名称)

    if obj.get("optype") == "videomatrixconfig.matrixname_pie":
        res = get_pie(
            "select matrixname x,count(*) y from vm790_bcfe8a202787453d.videomatrixconfig group by matrixname order by x desc",
            "视频矩阵名称",
        )
    if obj.get("optype") == "videomatrixconfig.matrixname_pie_v1":
        res = get_pie_v1(
            "select matrixname x,count(*) y from vm790_bcfe8a202787453d.videomatrixconfig group by matrixname",
            "视频矩阵名称",
        )
    if obj.get("optype") == "videomatrixconfig.matrixname_pie_v2":
        res = get_pie_v2(
            "select matrixname x,count(*) y from vm790_bcfe8a202787453d.videomatrixconfig group by matrixname",
            "视频矩阵名称",
        )
    if obj.get("optype") == "videomatrixconfig.matrixname_line":
        res = get_line(
            "select matrixname x,count(*) y from vm790_bcfe8a202787453d.videomatrixconfig group by matrixname",
            "视频矩阵名称",
        )
    if obj.get("optype") == "videomatrixconfig.matrixname_bar":
        res = get_bar(
            "select matrixname x,count(*) y from vm790_bcfe8a202787453d.videomatrixconfig group by matrixname",
            "视频矩阵名称",
        )
    if obj.get("optype") == "videomatrixconfig.matrixname_bar_v1":
        res = get_bar_v1(
            "select matrixname x,count(*) y from vm790_bcfe8a202787453d.videomatrixconfig group by matrixname",
            "视频矩阵名称",
        )
    if obj.get("optype") == "videomatrixconfig.description_wordcloud":
        textlist = get_data(
            "SELECT description result FROM vm790_bcfe8a202787453d.videomatrixconfig;"
        )
        res = {
            "title": "词云图",
            "imgbs64": generate_wordcloud_base64(
                ",".join([t["result"] for t in textlist])
            ),
        }
    if obj.get("optype") == "videomatrixconfig.createdat_line":
        res = get_line(
            "select createdat x,count(*) y from vm790_bcfe8a202787453d.videomatrixconfig group by createdat order by x",
            "创建时间",
        )
    if obj.get("optype") == "videomatrixconfig.updatedat_line":
        res = get_line(
            "select updatedat x,count(*) y from vm790_bcfe8a202787453d.videomatrixconfig group by updatedat order by x",
            "更新时间",
        )
    # videomatrixconfig(视频矩阵配置表)->videosourceid(视频源ID关联视频源)

    if obj.get("optype") == "videomatrixconfig.videosourceid_pie":
        res = get_pie(
            "select videosourceid x,count(*) y from vm790_bcfe8a202787453d.videomatrixconfig group by videosourceid order by x desc",
            "视频源ID关联视频源",
        )
    if obj.get("optype") == "videomatrixconfig.videosourceid_pie_v1":
        res = get_pie_v1(
            "select videosourceid x,count(*) y from vm790_bcfe8a202787453d.videomatrixconfig group by videosourceid",
            "视频源ID关联视频源",
        )
    if obj.get("optype") == "videomatrixconfig.videosourceid_pie_v2":
        res = get_pie_v2(
            "select videosourceid x,count(*) y from vm790_bcfe8a202787453d.videomatrixconfig group by videosourceid",
            "视频源ID关联视频源",
        )
    if obj.get("optype") == "videomatrixconfig.videosourceid_line":
        res = get_line(
            "select videosourceid x,count(*) y from vm790_bcfe8a202787453d.videomatrixconfig group by videosourceid",
            "视频源ID关联视频源",
        )
    if obj.get("optype") == "videomatrixconfig.videosourceid_bar":
        res = get_bar(
            "select videosourceid x,count(*) y from vm790_bcfe8a202787453d.videomatrixconfig group by videosourceid",
            "视频源ID关联视频源",
        )
    if obj.get("optype") == "videomatrixconfig.videosourceid_bar_v1":
        res = get_bar_v1(
            "select videosourceid x,count(*) y from vm790_bcfe8a202787453d.videomatrixconfig group by videosourceid",
            "视频源ID关联视频源",
        )
    # videomatrixconfig(视频矩阵配置表)->outputchannelid(输出通道ID关联输出通道)

    if obj.get("optype") == "videomatrixconfig.outputchannelid_pie":
        res = get_pie(
            "select outputchannelid x,count(*) y from vm790_bcfe8a202787453d.videomatrixconfig group by outputchannelid order by x desc",
            "输出通道ID关联输出通道",
        )
    if obj.get("optype") == "videomatrixconfig.outputchannelid_pie_v1":
        res = get_pie_v1(
            "select outputchannelid x,count(*) y from vm790_bcfe8a202787453d.videomatrixconfig group by outputchannelid",
            "输出通道ID关联输出通道",
        )
    if obj.get("optype") == "videomatrixconfig.outputchannelid_pie_v2":
        res = get_pie_v2(
            "select outputchannelid x,count(*) y from vm790_bcfe8a202787453d.videomatrixconfig group by outputchannelid",
            "输出通道ID关联输出通道",
        )
    if obj.get("optype") == "videomatrixconfig.outputchannelid_line":
        res = get_line(
            "select outputchannelid x,count(*) y from vm790_bcfe8a202787453d.videomatrixconfig group by outputchannelid",
            "输出通道ID关联输出通道",
        )
    if obj.get("optype") == "videomatrixconfig.outputchannelid_bar":
        res = get_bar(
            "select outputchannelid x,count(*) y from vm790_bcfe8a202787453d.videomatrixconfig group by outputchannelid",
            "输出通道ID关联输出通道",
        )
    if obj.get("optype") == "videomatrixconfig.outputchannelid_bar_v1":
        res = get_bar_v1(
            "select outputchannelid x,count(*) y from vm790_bcfe8a202787453d.videomatrixconfig group by outputchannelid",
            "输出通道ID关联输出通道",
        )
    # videomatrixconfig(视频矩阵配置表)->layoutconfig(布局配置如1x4)

    if obj.get("optype") == "videomatrixconfig.layoutconfig_pie":
        res = get_pie(
            "select layoutconfig x,count(*) y from vm790_bcfe8a202787453d.videomatrixconfig group by layoutconfig order by x desc",
            "布局配置如1x4",
        )
    if obj.get("optype") == "videomatrixconfig.layoutconfig_pie_v1":
        res = get_pie_v1(
            "select layoutconfig x,count(*) y from vm790_bcfe8a202787453d.videomatrixconfig group by layoutconfig",
            "布局配置如1x4",
        )
    if obj.get("optype") == "videomatrixconfig.layoutconfig_pie_v2":
        res = get_pie_v2(
            "select layoutconfig x,count(*) y from vm790_bcfe8a202787453d.videomatrixconfig group by layoutconfig",
            "布局配置如1x4",
        )
    if obj.get("optype") == "videomatrixconfig.layoutconfig_line":
        res = get_line(
            "select layoutconfig x,count(*) y from vm790_bcfe8a202787453d.videomatrixconfig group by layoutconfig",
            "布局配置如1x4",
        )
    if obj.get("optype") == "videomatrixconfig.layoutconfig_bar":
        res = get_bar(
            "select layoutconfig x,count(*) y from vm790_bcfe8a202787453d.videomatrixconfig group by layoutconfig",
            "布局配置如1x4",
        )
    if obj.get("optype") == "videomatrixconfig.layoutconfig_bar_v1":
        res = get_bar_v1(
            "select layoutconfig x,count(*) y from vm790_bcfe8a202787453d.videomatrixconfig group by layoutconfig",
            "布局配置如1x4",
        )
    # videomatrixconfig(视频矩阵配置表)->kwkwisactive(是否激活用于控制视频矩阵的启用状态)

    if obj.get("optype") == "videomatrixconfig.kwkwisactive_pie":
        res = get_pie(
            "select kwkwisactive x,count(*) y from vm790_bcfe8a202787453d.videomatrixconfig group by kwkwisactive order by x desc",
            "是否激活用于控制视频矩阵的启用状态",
        )
    if obj.get("optype") == "videomatrixconfig.kwkwisactive_pie_v1":
        res = get_pie_v1(
            "select kwkwisactive x,count(*) y from vm790_bcfe8a202787453d.videomatrixconfig group by kwkwisactive",
            "是否激活用于控制视频矩阵的启用状态",
        )
    if obj.get("optype") == "videomatrixconfig.kwkwisactive_pie_v2":
        res = get_pie_v2(
            "select kwkwisactive x,count(*) y from vm790_bcfe8a202787453d.videomatrixconfig group by kwkwisactive",
            "是否激活用于控制视频矩阵的启用状态",
        )
    if obj.get("optype") == "videomatrixconfig.kwkwisactive_line":
        res = get_line(
            "select kwkwisactive x,count(*) y from vm790_bcfe8a202787453d.videomatrixconfig group by kwkwisactive",
            "是否激活用于控制视频矩阵的启用状态",
        )
    if obj.get("optype") == "videomatrixconfig.kwkwisactive_bar":
        res = get_bar(
            "select kwkwisactive x,count(*) y from vm790_bcfe8a202787453d.videomatrixconfig group by kwkwisactive",
            "是否激活用于控制视频矩阵的启用状态",
        )
    if obj.get("optype") == "videomatrixconfig.kwkwisactive_bar_v1":
        res = get_bar_v1(
            "select kwkwisactive x,count(*) y from vm790_bcfe8a202787453d.videomatrixconfig group by kwkwisactive",
            "是否激活用于控制视频矩阵的启用状态",
        )
    # videomatrixnode(视频矩阵节点表)->nodename(节点名称)

    if obj.get("optype") == "videomatrixnode.nodename_pie":
        res = get_pie(
            "select nodename x,count(*) y from vm790_bcfe8a202787453d.videomatrixnode group by nodename order by x desc",
            "节点名称",
        )
    if obj.get("optype") == "videomatrixnode.nodename_pie_v1":
        res = get_pie_v1(
            "select nodename x,count(*) y from vm790_bcfe8a202787453d.videomatrixnode group by nodename",
            "节点名称",
        )
    if obj.get("optype") == "videomatrixnode.nodename_pie_v2":
        res = get_pie_v2(
            "select nodename x,count(*) y from vm790_bcfe8a202787453d.videomatrixnode group by nodename",
            "节点名称",
        )
    if obj.get("optype") == "videomatrixnode.nodename_line":
        res = get_line(
            "select nodename x,count(*) y from vm790_bcfe8a202787453d.videomatrixnode group by nodename",
            "节点名称",
        )
    if obj.get("optype") == "videomatrixnode.nodename_bar":
        res = get_bar(
            "select nodename x,count(*) y from vm790_bcfe8a202787453d.videomatrixnode group by nodename",
            "节点名称",
        )
    if obj.get("optype") == "videomatrixnode.nodename_bar_v1":
        res = get_bar_v1(
            "select nodename x,count(*) y from vm790_bcfe8a202787453d.videomatrixnode group by nodename",
            "节点名称",
        )
    # videomatrixnode(视频矩阵节点表)->videosourceid(关联视频源ID)

    if obj.get("optype") == "videomatrixnode.videosourceid_pie":
        res = get_pie(
            "select videosourceid x,count(*) y from vm790_bcfe8a202787453d.videomatrixnode group by videosourceid order by x desc",
            "关联视频源ID",
        )
    if obj.get("optype") == "videomatrixnode.videosourceid_pie_v1":
        res = get_pie_v1(
            "select videosourceid x,count(*) y from vm790_bcfe8a202787453d.videomatrixnode group by videosourceid",
            "关联视频源ID",
        )
    if obj.get("optype") == "videomatrixnode.videosourceid_pie_v2":
        res = get_pie_v2(
            "select videosourceid x,count(*) y from vm790_bcfe8a202787453d.videomatrixnode group by videosourceid",
            "关联视频源ID",
        )
    if obj.get("optype") == "videomatrixnode.videosourceid_line":
        res = get_line(
            "select videosourceid x,count(*) y from vm790_bcfe8a202787453d.videomatrixnode group by videosourceid",
            "关联视频源ID",
        )
    if obj.get("optype") == "videomatrixnode.videosourceid_bar":
        res = get_bar(
            "select videosourceid x,count(*) y from vm790_bcfe8a202787453d.videomatrixnode group by videosourceid",
            "关联视频源ID",
        )
    if obj.get("optype") == "videomatrixnode.videosourceid_bar_v1":
        res = get_bar_v1(
            "select videosourceid x,count(*) y from vm790_bcfe8a202787453d.videomatrixnode group by videosourceid",
            "关联视频源ID",
        )
    # videomatrixnode(视频矩阵节点表)->videokwkwfkwkwormat(视频格式)

    if obj.get("optype") == "videomatrixnode.videokwkwfkwkwormat_pie":
        res = get_pie(
            "select videokwkwfkwkwormat x,count(*) y from vm790_bcfe8a202787453d.videomatrixnode group by videokwkwfkwkwormat order by x desc",
            "视频格式",
        )
    if obj.get("optype") == "videomatrixnode.videokwkwfkwkwormat_pie_v1":
        res = get_pie_v1(
            "select videokwkwfkwkwormat x,count(*) y from vm790_bcfe8a202787453d.videomatrixnode group by videokwkwfkwkwormat",
            "视频格式",
        )
    if obj.get("optype") == "videomatrixnode.videokwkwfkwkwormat_pie_v2":
        res = get_pie_v2(
            "select videokwkwfkwkwormat x,count(*) y from vm790_bcfe8a202787453d.videomatrixnode group by videokwkwfkwkwormat",
            "视频格式",
        )
    if obj.get("optype") == "videomatrixnode.videokwkwfkwkwormat_line":
        res = get_line(
            "select videokwkwfkwkwormat x,count(*) y from vm790_bcfe8a202787453d.videomatrixnode group by videokwkwfkwkwormat",
            "视频格式",
        )
    if obj.get("optype") == "videomatrixnode.videokwkwfkwkwormat_bar":
        res = get_bar(
            "select videokwkwfkwkwormat x,count(*) y from vm790_bcfe8a202787453d.videomatrixnode group by videokwkwfkwkwormat",
            "视频格式",
        )
    if obj.get("optype") == "videomatrixnode.videokwkwfkwkwormat_bar_v1":
        res = get_bar_v1(
            "select videokwkwfkwkwormat x,count(*) y from vm790_bcfe8a202787453d.videomatrixnode group by videokwkwfkwkwormat",
            "视频格式",
        )
    # videomatrixnode(视频矩阵节点表)->resolution(分辨率)

    if obj.get("optype") == "videomatrixnode.resolution_pie":
        res = get_pie(
            "select resolution x,count(*) y from vm790_bcfe8a202787453d.videomatrixnode group by resolution order by x desc",
            "分辨率",
        )
    if obj.get("optype") == "videomatrixnode.resolution_pie_v1":
        res = get_pie_v1(
            "select resolution x,count(*) y from vm790_bcfe8a202787453d.videomatrixnode group by resolution",
            "分辨率",
        )
    if obj.get("optype") == "videomatrixnode.resolution_pie_v2":
        res = get_pie_v2(
            "select resolution x,count(*) y from vm790_bcfe8a202787453d.videomatrixnode group by resolution",
            "分辨率",
        )
    if obj.get("optype") == "videomatrixnode.resolution_line":
        res = get_line(
            "select resolution x,count(*) y from vm790_bcfe8a202787453d.videomatrixnode group by resolution",
            "分辨率",
        )
    if obj.get("optype") == "videomatrixnode.resolution_bar":
        res = get_bar(
            "select resolution x,count(*) y from vm790_bcfe8a202787453d.videomatrixnode group by resolution",
            "分辨率",
        )
    if obj.get("optype") == "videomatrixnode.resolution_bar_v1":
        res = get_bar_v1(
            "select resolution x,count(*) y from vm790_bcfe8a202787453d.videomatrixnode group by resolution",
            "分辨率",
        )
    # videomatrixnode(视频矩阵节点表)->status(状态如在线、离线、维护中)

    if obj.get("optype") == "videomatrixnode.status_pie":
        res = get_pie(
            "select status x,count(*) y from vm790_bcfe8a202787453d.videomatrixnode group by status order by x desc",
            "状态如在线、离线、维护中",
        )
    if obj.get("optype") == "videomatrixnode.status_pie_v1":
        res = get_pie_v1(
            "select status x,count(*) y from vm790_bcfe8a202787453d.videomatrixnode group by status",
            "状态如在线、离线、维护中",
        )
    if obj.get("optype") == "videomatrixnode.status_pie_v2":
        res = get_pie_v2(
            "select status x,count(*) y from vm790_bcfe8a202787453d.videomatrixnode group by status",
            "状态如在线、离线、维护中",
        )
    if obj.get("optype") == "videomatrixnode.status_line":
        res = get_line(
            "select status x,count(*) y from vm790_bcfe8a202787453d.videomatrixnode group by status",
            "状态如在线、离线、维护中",
        )
    if obj.get("optype") == "videomatrixnode.status_bar":
        res = get_bar(
            "select status x,count(*) y from vm790_bcfe8a202787453d.videomatrixnode group by status",
            "状态如在线、离线、维护中",
        )
    if obj.get("optype") == "videomatrixnode.status_bar_v1":
        res = get_bar_v1(
            "select status x,count(*) y from vm790_bcfe8a202787453d.videomatrixnode group by status",
            "状态如在线、离线、维护中",
        )
    if obj.get("optype") == "videomatrixnode.createtime_line":
        res = get_line(
            "select createtime x,count(*) y from vm790_bcfe8a202787453d.videomatrixnode group by createtime order by x",
            "创建时间",
        )
    if obj.get("optype") == "videomatrixnode.updatetime_line":
        res = get_line(
            "select updatetime x,count(*) y from vm790_bcfe8a202787453d.videomatrixnode group by updatetime order by x",
            "更新时间",
        )
    # videomatrixnode(视频矩阵节点表)->parentnodeid(关联父节点ID用于示节点之间的层级关系)

    if obj.get("optype") == "videomatrixnode.parentnodeid_pie":
        res = get_pie(
            "select parentnodeid x,count(*) y from vm790_bcfe8a202787453d.videomatrixnode group by parentnodeid order by x desc",
            "关联父节点ID用于示节点之间的层级关系",
        )
    if obj.get("optype") == "videomatrixnode.parentnodeid_pie_v1":
        res = get_pie_v1(
            "select parentnodeid x,count(*) y from vm790_bcfe8a202787453d.videomatrixnode group by parentnodeid",
            "关联父节点ID用于示节点之间的层级关系",
        )
    if obj.get("optype") == "videomatrixnode.parentnodeid_pie_v2":
        res = get_pie_v2(
            "select parentnodeid x,count(*) y from vm790_bcfe8a202787453d.videomatrixnode group by parentnodeid",
            "关联父节点ID用于示节点之间的层级关系",
        )
    if obj.get("optype") == "videomatrixnode.parentnodeid_line":
        res = get_line(
            "select parentnodeid x,count(*) y from vm790_bcfe8a202787453d.videomatrixnode group by parentnodeid",
            "关联父节点ID用于示节点之间的层级关系",
        )
    if obj.get("optype") == "videomatrixnode.parentnodeid_bar":
        res = get_bar(
            "select parentnodeid x,count(*) y from vm790_bcfe8a202787453d.videomatrixnode group by parentnodeid",
            "关联父节点ID用于示节点之间的层级关系",
        )
    if obj.get("optype") == "videomatrixnode.parentnodeid_bar_v1":
        res = get_bar_v1(
            "select parentnodeid x,count(*) y from vm790_bcfe8a202787453d.videomatrixnode group by parentnodeid",
            "关联父节点ID用于示节点之间的层级关系",
        )
    if obj.get("optype") == "videomatrixnode.description_wordcloud":
        textlist = get_data(
            "SELECT description result FROM vm790_bcfe8a202787453d.videomatrixnode;"
        )
        res = {
            "title": "词云图",
            "imgbs64": generate_wordcloud_base64(
                ",".join([t["result"] for t in textlist])
            ),
        }
    # videomatrixplayreckwkword(视频矩阵播放记录表)->videoid(视频ID关联视频)

    if obj.get("optype") == "videomatrixplayreckwkword.videoid_pie":
        res = get_pie(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videomatrixplayreckwkword group by videoid order by x desc",
            "视频ID关联视频",
        )
    if obj.get("optype") == "videomatrixplayreckwkword.videoid_pie_v1":
        res = get_pie_v1(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videomatrixplayreckwkword group by videoid",
            "视频ID关联视频",
        )
    if obj.get("optype") == "videomatrixplayreckwkword.videoid_pie_v2":
        res = get_pie_v2(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videomatrixplayreckwkword group by videoid",
            "视频ID关联视频",
        )
    if obj.get("optype") == "videomatrixplayreckwkword.videoid_line":
        res = get_line(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videomatrixplayreckwkword group by videoid",
            "视频ID关联视频",
        )
    if obj.get("optype") == "videomatrixplayreckwkword.videoid_bar":
        res = get_bar(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videomatrixplayreckwkword group by videoid",
            "视频ID关联视频",
        )
    if obj.get("optype") == "videomatrixplayreckwkword.videoid_bar_v1":
        res = get_bar_v1(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videomatrixplayreckwkword group by videoid",
            "视频ID关联视频",
        )
    # videomatrixplayreckwkword(视频矩阵播放记录表)->matrixid(矩阵ID关联视频矩阵)

    if obj.get("optype") == "videomatrixplayreckwkword.matrixid_pie":
        res = get_pie(
            "select matrixid x,count(*) y from vm790_bcfe8a202787453d.videomatrixplayreckwkword group by matrixid order by x desc",
            "矩阵ID关联视频矩阵",
        )
    if obj.get("optype") == "videomatrixplayreckwkword.matrixid_pie_v1":
        res = get_pie_v1(
            "select matrixid x,count(*) y from vm790_bcfe8a202787453d.videomatrixplayreckwkword group by matrixid",
            "矩阵ID关联视频矩阵",
        )
    if obj.get("optype") == "videomatrixplayreckwkword.matrixid_pie_v2":
        res = get_pie_v2(
            "select matrixid x,count(*) y from vm790_bcfe8a202787453d.videomatrixplayreckwkword group by matrixid",
            "矩阵ID关联视频矩阵",
        )
    if obj.get("optype") == "videomatrixplayreckwkword.matrixid_line":
        res = get_line(
            "select matrixid x,count(*) y from vm790_bcfe8a202787453d.videomatrixplayreckwkword group by matrixid",
            "矩阵ID关联视频矩阵",
        )
    if obj.get("optype") == "videomatrixplayreckwkword.matrixid_bar":
        res = get_bar(
            "select matrixid x,count(*) y from vm790_bcfe8a202787453d.videomatrixplayreckwkword group by matrixid",
            "矩阵ID关联视频矩阵",
        )
    if obj.get("optype") == "videomatrixplayreckwkword.matrixid_bar_v1":
        res = get_bar_v1(
            "select matrixid x,count(*) y from vm790_bcfe8a202787453d.videomatrixplayreckwkword group by matrixid",
            "矩阵ID关联视频矩阵",
        )
    if obj.get("optype") == "videomatrixplayreckwkword.playtime_line":
        res = get_line(
            "select playtime x,count(*) y from vm790_bcfe8a202787453d.videomatrixplayreckwkword group by playtime order by x",
            "播放时间",
        )
    # videomatrixplayreckwkword(视频矩阵播放记录表)->playduration(播放时长秒)

    if obj.get("optype") == "videomatrixplayreckwkword.playduration_pie":
        res = get_pie(
            "select playduration x,count(*) y from vm790_bcfe8a202787453d.videomatrixplayreckwkword group by playduration order by x desc",
            "播放时长秒",
        )
    if obj.get("optype") == "videomatrixplayreckwkword.playduration_pie_v1":
        res = get_pie_v1(
            "select playduration x,count(*) y from vm790_bcfe8a202787453d.videomatrixplayreckwkword group by playduration",
            "播放时长秒",
        )
    if obj.get("optype") == "videomatrixplayreckwkword.playduration_pie_v2":
        res = get_pie_v2(
            "select playduration x,count(*) y from vm790_bcfe8a202787453d.videomatrixplayreckwkword group by playduration",
            "播放时长秒",
        )
    if obj.get("optype") == "videomatrixplayreckwkword.playduration_line":
        res = get_line(
            "select playduration x,count(*) y from vm790_bcfe8a202787453d.videomatrixplayreckwkword group by playduration",
            "播放时长秒",
        )
    if obj.get("optype") == "videomatrixplayreckwkword.playduration_bar":
        res = get_bar(
            "select playduration x,count(*) y from vm790_bcfe8a202787453d.videomatrixplayreckwkword group by playduration",
            "播放时长秒",
        )
    if obj.get("optype") == "videomatrixplayreckwkword.playduration_bar_v1":
        res = get_bar_v1(
            "select playduration x,count(*) y from vm790_bcfe8a202787453d.videomatrixplayreckwkword group by playduration",
            "播放时长秒",
        )
    # videomatrixplayreckwkword(视频矩阵播放记录表)->userid(用户ID关联用户)

    if obj.get("optype") == "videomatrixplayreckwkword.userid_pie":
        res = get_pie(
            "select userid x,count(*) y from vm790_bcfe8a202787453d.videomatrixplayreckwkword group by userid order by x desc",
            "用户ID关联用户",
        )
    if obj.get("optype") == "videomatrixplayreckwkword.userid_pie_v1":
        res = get_pie_v1(
            "select userid x,count(*) y from vm790_bcfe8a202787453d.videomatrixplayreckwkword group by userid",
            "用户ID关联用户",
        )
    if obj.get("optype") == "videomatrixplayreckwkword.userid_pie_v2":
        res = get_pie_v2(
            "select userid x,count(*) y from vm790_bcfe8a202787453d.videomatrixplayreckwkword group by userid",
            "用户ID关联用户",
        )
    if obj.get("optype") == "videomatrixplayreckwkword.userid_line":
        res = get_line(
            "select userid x,count(*) y from vm790_bcfe8a202787453d.videomatrixplayreckwkword group by userid",
            "用户ID关联用户",
        )
    if obj.get("optype") == "videomatrixplayreckwkword.userid_bar":
        res = get_bar(
            "select userid x,count(*) y from vm790_bcfe8a202787453d.videomatrixplayreckwkword group by userid",
            "用户ID关联用户",
        )
    if obj.get("optype") == "videomatrixplayreckwkword.userid_bar_v1":
        res = get_bar_v1(
            "select userid x,count(*) y from vm790_bcfe8a202787453d.videomatrixplayreckwkword group by userid",
            "用户ID关联用户",
        )
    # videomatrixplayreckwkword(视频矩阵播放记录表)->deviceid(设备ID关联设备)

    if obj.get("optype") == "videomatrixplayreckwkword.deviceid_pie":
        res = get_pie(
            "select deviceid x,count(*) y from vm790_bcfe8a202787453d.videomatrixplayreckwkword group by deviceid order by x desc",
            "设备ID关联设备",
        )
    if obj.get("optype") == "videomatrixplayreckwkword.deviceid_pie_v1":
        res = get_pie_v1(
            "select deviceid x,count(*) y from vm790_bcfe8a202787453d.videomatrixplayreckwkword group by deviceid",
            "设备ID关联设备",
        )
    if obj.get("optype") == "videomatrixplayreckwkword.deviceid_pie_v2":
        res = get_pie_v2(
            "select deviceid x,count(*) y from vm790_bcfe8a202787453d.videomatrixplayreckwkword group by deviceid",
            "设备ID关联设备",
        )
    if obj.get("optype") == "videomatrixplayreckwkword.deviceid_line":
        res = get_line(
            "select deviceid x,count(*) y from vm790_bcfe8a202787453d.videomatrixplayreckwkword group by deviceid",
            "设备ID关联设备",
        )
    if obj.get("optype") == "videomatrixplayreckwkword.deviceid_bar":
        res = get_bar(
            "select deviceid x,count(*) y from vm790_bcfe8a202787453d.videomatrixplayreckwkword group by deviceid",
            "设备ID关联设备",
        )
    if obj.get("optype") == "videomatrixplayreckwkword.deviceid_bar_v1":
        res = get_bar_v1(
            "select deviceid x,count(*) y from vm790_bcfe8a202787453d.videomatrixplayreckwkword group by deviceid",
            "设备ID关联设备",
        )
    # videomatrixplayreckwkword(视频矩阵播放记录表)->playstatus(播放状态如成功、失败、中断等)

    if obj.get("optype") == "videomatrixplayreckwkword.playstatus_pie":
        res = get_pie(
            "select playstatus x,count(*) y from vm790_bcfe8a202787453d.videomatrixplayreckwkword group by playstatus order by x desc",
            "播放状态如成功、失败、中断等",
        )
    if obj.get("optype") == "videomatrixplayreckwkword.playstatus_pie_v1":
        res = get_pie_v1(
            "select playstatus x,count(*) y from vm790_bcfe8a202787453d.videomatrixplayreckwkword group by playstatus",
            "播放状态如成功、失败、中断等",
        )
    if obj.get("optype") == "videomatrixplayreckwkword.playstatus_pie_v2":
        res = get_pie_v2(
            "select playstatus x,count(*) y from vm790_bcfe8a202787453d.videomatrixplayreckwkword group by playstatus",
            "播放状态如成功、失败、中断等",
        )
    if obj.get("optype") == "videomatrixplayreckwkword.playstatus_line":
        res = get_line(
            "select playstatus x,count(*) y from vm790_bcfe8a202787453d.videomatrixplayreckwkword group by playstatus",
            "播放状态如成功、失败、中断等",
        )
    if obj.get("optype") == "videomatrixplayreckwkword.playstatus_bar":
        res = get_bar(
            "select playstatus x,count(*) y from vm790_bcfe8a202787453d.videomatrixplayreckwkword group by playstatus",
            "播放状态如成功、失败、中断等",
        )
    if obj.get("optype") == "videomatrixplayreckwkword.playstatus_bar_v1":
        res = get_bar_v1(
            "select playstatus x,count(*) y from vm790_bcfe8a202787453d.videomatrixplayreckwkword group by playstatus",
            "播放状态如成功、失败、中断等",
        )
    if obj.get("optype") == "videomatrixplayreckwkword.ipaddress_wordcloud":
        textlist = get_data(
            "SELECT ipaddress result FROM vm790_bcfe8a202787453d.videomatrixplayreckwkword;"
        )
        res = {
            "title": "词云图",
            "imgbs64": generate_wordcloud_base64(
                ",".join([t["result"] for t in textlist])
            ),
        }
    # videorelatedcontent(视频关联内容表)->videoid(关联视频ID)

    if obj.get("optype") == "videorelatedcontent.videoid_pie":
        res = get_pie(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videorelatedcontent group by videoid order by x desc",
            "关联视频ID",
        )
    if obj.get("optype") == "videorelatedcontent.videoid_pie_v1":
        res = get_pie_v1(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videorelatedcontent group by videoid",
            "关联视频ID",
        )
    if obj.get("optype") == "videorelatedcontent.videoid_pie_v2":
        res = get_pie_v2(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videorelatedcontent group by videoid",
            "关联视频ID",
        )
    if obj.get("optype") == "videorelatedcontent.videoid_line":
        res = get_line(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videorelatedcontent group by videoid",
            "关联视频ID",
        )
    if obj.get("optype") == "videorelatedcontent.videoid_bar":
        res = get_bar(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videorelatedcontent group by videoid",
            "关联视频ID",
        )
    if obj.get("optype") == "videorelatedcontent.videoid_bar_v1":
        res = get_bar_v1(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videorelatedcontent group by videoid",
            "关联视频ID",
        )
    # videorelatedcontent(视频关联内容表)->contentid(关联内容ID)

    if obj.get("optype") == "videorelatedcontent.contentid_pie":
        res = get_pie(
            "select contentid x,count(*) y from vm790_bcfe8a202787453d.videorelatedcontent group by contentid order by x desc",
            "关联内容ID",
        )
    if obj.get("optype") == "videorelatedcontent.contentid_pie_v1":
        res = get_pie_v1(
            "select contentid x,count(*) y from vm790_bcfe8a202787453d.videorelatedcontent group by contentid",
            "关联内容ID",
        )
    if obj.get("optype") == "videorelatedcontent.contentid_pie_v2":
        res = get_pie_v2(
            "select contentid x,count(*) y from vm790_bcfe8a202787453d.videorelatedcontent group by contentid",
            "关联内容ID",
        )
    if obj.get("optype") == "videorelatedcontent.contentid_line":
        res = get_line(
            "select contentid x,count(*) y from vm790_bcfe8a202787453d.videorelatedcontent group by contentid",
            "关联内容ID",
        )
    if obj.get("optype") == "videorelatedcontent.contentid_bar":
        res = get_bar(
            "select contentid x,count(*) y from vm790_bcfe8a202787453d.videorelatedcontent group by contentid",
            "关联内容ID",
        )
    if obj.get("optype") == "videorelatedcontent.contentid_bar_v1":
        res = get_bar_v1(
            "select contentid x,count(*) y from vm790_bcfe8a202787453d.videorelatedcontent group by contentid",
            "关联内容ID",
        )
    if obj.get("optype") == "videorelatedcontent.contenttype_wordcloud":
        textlist = get_data(
            "SELECT contenttype result FROM vm790_bcfe8a202787453d.videorelatedcontent;"
        )
        res = {
            "title": "词云图",
            "imgbs64": generate_wordcloud_base64(
                ",".join([t["result"] for t in textlist])
            ),
        }
    # videorelatedcontent(视频关联内容表)->relatedtime(关联时间)

    if obj.get("optype") == "videorelatedcontent.relatedtime_pie":
        res = get_pie(
            "select relatedtime x,count(*) y from vm790_bcfe8a202787453d.videorelatedcontent group by relatedtime order by x desc",
            "关联时间",
        )
    if obj.get("optype") == "videorelatedcontent.relatedtime_pie_v1":
        res = get_pie_v1(
            "select relatedtime x,count(*) y from vm790_bcfe8a202787453d.videorelatedcontent group by relatedtime",
            "关联时间",
        )
    if obj.get("optype") == "videorelatedcontent.relatedtime_pie_v2":
        res = get_pie_v2(
            "select relatedtime x,count(*) y from vm790_bcfe8a202787453d.videorelatedcontent group by relatedtime",
            "关联时间",
        )
    if obj.get("optype") == "videorelatedcontent.relatedtime_line":
        res = get_line(
            "select relatedtime x,count(*) y from vm790_bcfe8a202787453d.videorelatedcontent group by relatedtime",
            "关联时间",
        )
    if obj.get("optype") == "videorelatedcontent.relatedtime_bar":
        res = get_bar(
            "select relatedtime x,count(*) y from vm790_bcfe8a202787453d.videorelatedcontent group by relatedtime",
            "关联时间",
        )
    if obj.get("optype") == "videorelatedcontent.relatedtime_bar_v1":
        res = get_bar_v1(
            "select relatedtime x,count(*) y from vm790_bcfe8a202787453d.videorelatedcontent group by relatedtime",
            "关联时间",
        )
    if obj.get("optype") == "videorelatedcontent.description_wordcloud":
        textlist = get_data(
            "SELECT description result FROM vm790_bcfe8a202787453d.videorelatedcontent;"
        )
        res = {
            "title": "词云图",
            "imgbs64": generate_wordcloud_base64(
                ",".join([t["result"] for t in textlist])
            ),
        }
    # videorelatedcontent(视频关联内容表)->status(状态)

    if obj.get("optype") == "videorelatedcontent.status_pie":
        res = get_pie(
            "select status x,count(*) y from vm790_bcfe8a202787453d.videorelatedcontent group by status order by x desc",
            "状态",
        )
    if obj.get("optype") == "videorelatedcontent.status_pie_v1":
        res = get_pie_v1(
            "select status x,count(*) y from vm790_bcfe8a202787453d.videorelatedcontent group by status",
            "状态",
        )
    if obj.get("optype") == "videorelatedcontent.status_pie_v2":
        res = get_pie_v2(
            "select status x,count(*) y from vm790_bcfe8a202787453d.videorelatedcontent group by status",
            "状态",
        )
    if obj.get("optype") == "videorelatedcontent.status_line":
        res = get_line(
            "select status x,count(*) y from vm790_bcfe8a202787453d.videorelatedcontent group by status",
            "状态",
        )
    if obj.get("optype") == "videorelatedcontent.status_bar":
        res = get_bar(
            "select status x,count(*) y from vm790_bcfe8a202787453d.videorelatedcontent group by status",
            "状态",
        )
    if obj.get("optype") == "videorelatedcontent.status_bar_v1":
        res = get_bar_v1(
            "select status x,count(*) y from vm790_bcfe8a202787453d.videorelatedcontent group by status",
            "状态",
        )
    # videorelatedcontent(视频关联内容表)->creatkwkworid(关联创建者ID)

    if obj.get("optype") == "videorelatedcontent.creatkwkworid_pie":
        res = get_pie(
            "select creatkwkworid x,count(*) y from vm790_bcfe8a202787453d.videorelatedcontent group by creatkwkworid order by x desc",
            "关联创建者ID",
        )
    if obj.get("optype") == "videorelatedcontent.creatkwkworid_pie_v1":
        res = get_pie_v1(
            "select creatkwkworid x,count(*) y from vm790_bcfe8a202787453d.videorelatedcontent group by creatkwkworid",
            "关联创建者ID",
        )
    if obj.get("optype") == "videorelatedcontent.creatkwkworid_pie_v2":
        res = get_pie_v2(
            "select creatkwkworid x,count(*) y from vm790_bcfe8a202787453d.videorelatedcontent group by creatkwkworid",
            "关联创建者ID",
        )
    if obj.get("optype") == "videorelatedcontent.creatkwkworid_line":
        res = get_line(
            "select creatkwkworid x,count(*) y from vm790_bcfe8a202787453d.videorelatedcontent group by creatkwkworid",
            "关联创建者ID",
        )
    if obj.get("optype") == "videorelatedcontent.creatkwkworid_bar":
        res = get_bar(
            "select creatkwkworid x,count(*) y from vm790_bcfe8a202787453d.videorelatedcontent group by creatkwkworid",
            "关联创建者ID",
        )
    if obj.get("optype") == "videorelatedcontent.creatkwkworid_bar_v1":
        res = get_bar_v1(
            "select creatkwkworid x,count(*) y from vm790_bcfe8a202787453d.videorelatedcontent group by creatkwkworid",
            "关联创建者ID",
        )
    if obj.get("optype") == "videorelatedcontent.creationtime_line":
        res = get_line(
            "select creationtime x,count(*) y from vm790_bcfe8a202787453d.videorelatedcontent group by creationtime order by x",
            "创建时间",
        )
    if obj.get("optype") == "videorelatedcontent.modkwkwificationtime_line":
        res = get_line(
            "select modkwkwificationtime x,count(*) y from vm790_bcfe8a202787453d.videorelatedcontent group by modkwkwificationtime order by x",
            "修改时间",
        )
    # videorelatedcontent(视频关联内容表)->videotablevideoname(视频名称关联字段视频名假设为VideoTable关联字段为视频名称)

    if obj.get("optype") == "videorelatedcontent.videotablevideoname_pie":
        res = get_pie(
            "select videotablevideoname x,count(*) y from vm790_bcfe8a202787453d.videorelatedcontent group by videotablevideoname order by x desc",
            "视频名称关联字段视频名假设为VideoTable关联字段为视频名称",
        )
    if obj.get("optype") == "videorelatedcontent.videotablevideoname_pie_v1":
        res = get_pie_v1(
            "select videotablevideoname x,count(*) y from vm790_bcfe8a202787453d.videorelatedcontent group by videotablevideoname",
            "视频名称关联字段视频名假设为VideoTable关联字段为视频名称",
        )
    if obj.get("optype") == "videorelatedcontent.videotablevideoname_pie_v2":
        res = get_pie_v2(
            "select videotablevideoname x,count(*) y from vm790_bcfe8a202787453d.videorelatedcontent group by videotablevideoname",
            "视频名称关联字段视频名假设为VideoTable关联字段为视频名称",
        )
    if obj.get("optype") == "videorelatedcontent.videotablevideoname_line":
        res = get_line(
            "select videotablevideoname x,count(*) y from vm790_bcfe8a202787453d.videorelatedcontent group by videotablevideoname",
            "视频名称关联字段视频名假设为VideoTable关联字段为视频名称",
        )
    if obj.get("optype") == "videorelatedcontent.videotablevideoname_bar":
        res = get_bar(
            "select videotablevideoname x,count(*) y from vm790_bcfe8a202787453d.videorelatedcontent group by videotablevideoname",
            "视频名称关联字段视频名假设为VideoTable关联字段为视频名称",
        )
    if obj.get("optype") == "videorelatedcontent.videotablevideoname_bar_v1":
        res = get_bar_v1(
            "select videotablevideoname x,count(*) y from vm790_bcfe8a202787453d.videorelatedcontent group by videotablevideoname",
            "视频名称关联字段视频名假设为VideoTable关联字段为视频名称",
        )
    # videoerrkwkworlog(视频错误日志表)->videoid(关联视频ID)

    if obj.get("optype") == "videoerrkwkworlog.videoid_pie":
        res = get_pie(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videoerrkwkworlog group by videoid order by x desc",
            "关联视频ID",
        )
    if obj.get("optype") == "videoerrkwkworlog.videoid_pie_v1":
        res = get_pie_v1(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videoerrkwkworlog group by videoid",
            "关联视频ID",
        )
    if obj.get("optype") == "videoerrkwkworlog.videoid_pie_v2":
        res = get_pie_v2(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videoerrkwkworlog group by videoid",
            "关联视频ID",
        )
    if obj.get("optype") == "videoerrkwkworlog.videoid_line":
        res = get_line(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videoerrkwkworlog group by videoid",
            "关联视频ID",
        )
    if obj.get("optype") == "videoerrkwkworlog.videoid_bar":
        res = get_bar(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videoerrkwkworlog group by videoid",
            "关联视频ID",
        )
    if obj.get("optype") == "videoerrkwkworlog.videoid_bar_v1":
        res = get_bar_v1(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videoerrkwkworlog group by videoid",
            "关联视频ID",
        )
    # videoerrkwkworlog(视频错误日志表)->errkwkwortype(错误类型)

    if obj.get("optype") == "videoerrkwkworlog.errkwkwortype_pie":
        res = get_pie(
            "select errkwkwortype x,count(*) y from vm790_bcfe8a202787453d.videoerrkwkworlog group by errkwkwortype order by x desc",
            "错误类型",
        )
    if obj.get("optype") == "videoerrkwkworlog.errkwkwortype_pie_v1":
        res = get_pie_v1(
            "select errkwkwortype x,count(*) y from vm790_bcfe8a202787453d.videoerrkwkworlog group by errkwkwortype",
            "错误类型",
        )
    if obj.get("optype") == "videoerrkwkworlog.errkwkwortype_pie_v2":
        res = get_pie_v2(
            "select errkwkwortype x,count(*) y from vm790_bcfe8a202787453d.videoerrkwkworlog group by errkwkwortype",
            "错误类型",
        )
    if obj.get("optype") == "videoerrkwkworlog.errkwkwortype_line":
        res = get_line(
            "select errkwkwortype x,count(*) y from vm790_bcfe8a202787453d.videoerrkwkworlog group by errkwkwortype",
            "错误类型",
        )
    if obj.get("optype") == "videoerrkwkworlog.errkwkwortype_bar":
        res = get_bar(
            "select errkwkwortype x,count(*) y from vm790_bcfe8a202787453d.videoerrkwkworlog group by errkwkwortype",
            "错误类型",
        )
    if obj.get("optype") == "videoerrkwkworlog.errkwkwortype_bar_v1":
        res = get_bar_v1(
            "select errkwkwortype x,count(*) y from vm790_bcfe8a202787453d.videoerrkwkworlog group by errkwkwortype",
            "错误类型",
        )
    if obj.get("optype") == "videoerrkwkworlog.errkwkwordescription_wordcloud":
        textlist = get_data(
            "SELECT errkwkwordescription result FROM vm790_bcfe8a202787453d.videoerrkwkworlog;"
        )
        res = {
            "title": "词云图",
            "imgbs64": generate_wordcloud_base64(
                ",".join([t["result"] for t in textlist])
            ),
        }
    if obj.get("optype") == "videoerrkwkworlog.errkwkwortime_line":
        res = get_line(
            "select errkwkwortime x,count(*) y from vm790_bcfe8a202787453d.videoerrkwkworlog group by errkwkwortime order by x",
            "错误时间",
        )
    # videoerrkwkworlog(视频错误日志表)->resolved(是否已解决)

    if obj.get("optype") == "videoerrkwkworlog.resolved_pie":
        res = get_pie(
            "select resolved x,count(*) y from vm790_bcfe8a202787453d.videoerrkwkworlog group by resolved order by x desc",
            "是否已解决",
        )
    if obj.get("optype") == "videoerrkwkworlog.resolved_pie_v1":
        res = get_pie_v1(
            "select resolved x,count(*) y from vm790_bcfe8a202787453d.videoerrkwkworlog group by resolved",
            "是否已解决",
        )
    if obj.get("optype") == "videoerrkwkworlog.resolved_pie_v2":
        res = get_pie_v2(
            "select resolved x,count(*) y from vm790_bcfe8a202787453d.videoerrkwkworlog group by resolved",
            "是否已解决",
        )
    if obj.get("optype") == "videoerrkwkworlog.resolved_line":
        res = get_line(
            "select resolved x,count(*) y from vm790_bcfe8a202787453d.videoerrkwkworlog group by resolved",
            "是否已解决",
        )
    if obj.get("optype") == "videoerrkwkworlog.resolved_bar":
        res = get_bar(
            "select resolved x,count(*) y from vm790_bcfe8a202787453d.videoerrkwkworlog group by resolved",
            "是否已解决",
        )
    if obj.get("optype") == "videoerrkwkworlog.resolved_bar_v1":
        res = get_bar_v1(
            "select resolved x,count(*) y from vm790_bcfe8a202787453d.videoerrkwkworlog group by resolved",
            "是否已解决",
        )
    if obj.get("optype") == "videoerrkwkworlog.resolvedtime_line":
        res = get_line(
            "select resolvedtime x,count(*) y from vm790_bcfe8a202787453d.videoerrkwkworlog group by resolvedtime order by x",
            "解决时间",
        )
    # videoerrkwkworlog(视频错误日志表)->resolvedby(关联解决人)

    if obj.get("optype") == "videoerrkwkworlog.resolvedby_pie":
        res = get_pie(
            "select resolvedby x,count(*) y from vm790_bcfe8a202787453d.videoerrkwkworlog group by resolvedby order by x desc",
            "关联解决人",
        )
    if obj.get("optype") == "videoerrkwkworlog.resolvedby_pie_v1":
        res = get_pie_v1(
            "select resolvedby x,count(*) y from vm790_bcfe8a202787453d.videoerrkwkworlog group by resolvedby",
            "关联解决人",
        )
    if obj.get("optype") == "videoerrkwkworlog.resolvedby_pie_v2":
        res = get_pie_v2(
            "select resolvedby x,count(*) y from vm790_bcfe8a202787453d.videoerrkwkworlog group by resolvedby",
            "关联解决人",
        )
    if obj.get("optype") == "videoerrkwkworlog.resolvedby_line":
        res = get_line(
            "select resolvedby x,count(*) y from vm790_bcfe8a202787453d.videoerrkwkworlog group by resolvedby",
            "关联解决人",
        )
    if obj.get("optype") == "videoerrkwkworlog.resolvedby_bar":
        res = get_bar(
            "select resolvedby x,count(*) y from vm790_bcfe8a202787453d.videoerrkwkworlog group by resolvedby",
            "关联解决人",
        )
    if obj.get("optype") == "videoerrkwkworlog.resolvedby_bar_v1":
        res = get_bar_v1(
            "select resolvedby x,count(*) y from vm790_bcfe8a202787453d.videoerrkwkworlog group by resolvedby",
            "关联解决人",
        )
    # videoerrkwkworlog(视频错误日志表)->devicekwkwinfo(设备信息)

    if obj.get("optype") == "videoerrkwkworlog.devicekwkwinfo_pie":
        res = get_pie(
            "select devicekwkwinfo x,count(*) y from vm790_bcfe8a202787453d.videoerrkwkworlog group by devicekwkwinfo order by x desc",
            "设备信息",
        )
    if obj.get("optype") == "videoerrkwkworlog.devicekwkwinfo_pie_v1":
        res = get_pie_v1(
            "select devicekwkwinfo x,count(*) y from vm790_bcfe8a202787453d.videoerrkwkworlog group by devicekwkwinfo",
            "设备信息",
        )
    if obj.get("optype") == "videoerrkwkworlog.devicekwkwinfo_pie_v2":
        res = get_pie_v2(
            "select devicekwkwinfo x,count(*) y from vm790_bcfe8a202787453d.videoerrkwkworlog group by devicekwkwinfo",
            "设备信息",
        )
    if obj.get("optype") == "videoerrkwkworlog.devicekwkwinfo_line":
        res = get_line(
            "select devicekwkwinfo x,count(*) y from vm790_bcfe8a202787453d.videoerrkwkworlog group by devicekwkwinfo",
            "设备信息",
        )
    if obj.get("optype") == "videoerrkwkworlog.devicekwkwinfo_bar":
        res = get_bar(
            "select devicekwkwinfo x,count(*) y from vm790_bcfe8a202787453d.videoerrkwkworlog group by devicekwkwinfo",
            "设备信息",
        )
    if obj.get("optype") == "videoerrkwkworlog.devicekwkwinfo_bar_v1":
        res = get_bar_v1(
            "select devicekwkwinfo x,count(*) y from vm790_bcfe8a202787453d.videoerrkwkworlog group by devicekwkwinfo",
            "设备信息",
        )
    # videoerrkwkworlog(视频错误日志表)->clientip(客户端IP)

    if obj.get("optype") == "videoerrkwkworlog.clientip_pie":
        res = get_pie(
            "select clientip x,count(*) y from vm790_bcfe8a202787453d.videoerrkwkworlog group by clientip order by x desc",
            "客户端IP",
        )
    if obj.get("optype") == "videoerrkwkworlog.clientip_pie_v1":
        res = get_pie_v1(
            "select clientip x,count(*) y from vm790_bcfe8a202787453d.videoerrkwkworlog group by clientip",
            "客户端IP",
        )
    if obj.get("optype") == "videoerrkwkworlog.clientip_pie_v2":
        res = get_pie_v2(
            "select clientip x,count(*) y from vm790_bcfe8a202787453d.videoerrkwkworlog group by clientip",
            "客户端IP",
        )
    if obj.get("optype") == "videoerrkwkworlog.clientip_line":
        res = get_line(
            "select clientip x,count(*) y from vm790_bcfe8a202787453d.videoerrkwkworlog group by clientip",
            "客户端IP",
        )
    if obj.get("optype") == "videoerrkwkworlog.clientip_bar":
        res = get_bar(
            "select clientip x,count(*) y from vm790_bcfe8a202787453d.videoerrkwkworlog group by clientip",
            "客户端IP",
        )
    if obj.get("optype") == "videoerrkwkworlog.clientip_bar_v1":
        res = get_bar_v1(
            "select clientip x,count(*) y from vm790_bcfe8a202787453d.videoerrkwkworlog group by clientip",
            "客户端IP",
        )
    # videopopularity(视频热度统计表)->videoid(关联视频ID)

    if obj.get("optype") == "videopopularity.videoid_pie":
        res = get_pie(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videopopularity group by videoid order by x desc",
            "关联视频ID",
        )
    if obj.get("optype") == "videopopularity.videoid_pie_v1":
        res = get_pie_v1(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videopopularity group by videoid",
            "关联视频ID",
        )
    if obj.get("optype") == "videopopularity.videoid_pie_v2":
        res = get_pie_v2(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videopopularity group by videoid",
            "关联视频ID",
        )
    if obj.get("optype") == "videopopularity.videoid_line":
        res = get_line(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videopopularity group by videoid",
            "关联视频ID",
        )
    if obj.get("optype") == "videopopularity.videoid_bar":
        res = get_bar(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videopopularity group by videoid",
            "关联视频ID",
        )
    if obj.get("optype") == "videopopularity.videoid_bar_v1":
        res = get_bar_v1(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videopopularity group by videoid",
            "关联视频ID",
        )
    # videopopularity(视频热度统计表)->viewcount(观看次数)

    if obj.get("optype") == "videopopularity.viewcount_pie":
        res = get_pie(
            "select viewcount x,count(*) y from vm790_bcfe8a202787453d.videopopularity group by viewcount order by x desc",
            "观看次数",
        )
    if obj.get("optype") == "videopopularity.viewcount_pie_v1":
        res = get_pie_v1(
            "select viewcount x,count(*) y from vm790_bcfe8a202787453d.videopopularity group by viewcount",
            "观看次数",
        )
    if obj.get("optype") == "videopopularity.viewcount_pie_v2":
        res = get_pie_v2(
            "select viewcount x,count(*) y from vm790_bcfe8a202787453d.videopopularity group by viewcount",
            "观看次数",
        )
    if obj.get("optype") == "videopopularity.viewcount_line":
        res = get_line(
            "select viewcount x,count(*) y from vm790_bcfe8a202787453d.videopopularity group by viewcount",
            "观看次数",
        )
    if obj.get("optype") == "videopopularity.viewcount_bar":
        res = get_bar(
            "select viewcount x,count(*) y from vm790_bcfe8a202787453d.videopopularity group by viewcount",
            "观看次数",
        )
    if obj.get("optype") == "videopopularity.viewcount_bar_v1":
        res = get_bar_v1(
            "select viewcount x,count(*) y from vm790_bcfe8a202787453d.videopopularity group by viewcount",
            "观看次数",
        )
    # videopopularity(视频热度统计表)->likecount(点赞次数)

    if obj.get("optype") == "videopopularity.likecount_pie":
        res = get_pie(
            "select likecount x,count(*) y from vm790_bcfe8a202787453d.videopopularity group by likecount order by x desc",
            "点赞次数",
        )
    if obj.get("optype") == "videopopularity.likecount_pie_v1":
        res = get_pie_v1(
            "select likecount x,count(*) y from vm790_bcfe8a202787453d.videopopularity group by likecount",
            "点赞次数",
        )
    if obj.get("optype") == "videopopularity.likecount_pie_v2":
        res = get_pie_v2(
            "select likecount x,count(*) y from vm790_bcfe8a202787453d.videopopularity group by likecount",
            "点赞次数",
        )
    if obj.get("optype") == "videopopularity.likecount_line":
        res = get_line(
            "select likecount x,count(*) y from vm790_bcfe8a202787453d.videopopularity group by likecount",
            "点赞次数",
        )
    if obj.get("optype") == "videopopularity.likecount_bar":
        res = get_bar(
            "select likecount x,count(*) y from vm790_bcfe8a202787453d.videopopularity group by likecount",
            "点赞次数",
        )
    if obj.get("optype") == "videopopularity.likecount_bar_v1":
        res = get_bar_v1(
            "select likecount x,count(*) y from vm790_bcfe8a202787453d.videopopularity group by likecount",
            "点赞次数",
        )
    # videopopularity(视频热度统计表)->sharecount(分享次数)

    if obj.get("optype") == "videopopularity.sharecount_pie":
        res = get_pie(
            "select sharecount x,count(*) y from vm790_bcfe8a202787453d.videopopularity group by sharecount order by x desc",
            "分享次数",
        )
    if obj.get("optype") == "videopopularity.sharecount_pie_v1":
        res = get_pie_v1(
            "select sharecount x,count(*) y from vm790_bcfe8a202787453d.videopopularity group by sharecount",
            "分享次数",
        )
    if obj.get("optype") == "videopopularity.sharecount_pie_v2":
        res = get_pie_v2(
            "select sharecount x,count(*) y from vm790_bcfe8a202787453d.videopopularity group by sharecount",
            "分享次数",
        )
    if obj.get("optype") == "videopopularity.sharecount_line":
        res = get_line(
            "select sharecount x,count(*) y from vm790_bcfe8a202787453d.videopopularity group by sharecount",
            "分享次数",
        )
    if obj.get("optype") == "videopopularity.sharecount_bar":
        res = get_bar(
            "select sharecount x,count(*) y from vm790_bcfe8a202787453d.videopopularity group by sharecount",
            "分享次数",
        )
    if obj.get("optype") == "videopopularity.sharecount_bar_v1":
        res = get_bar_v1(
            "select sharecount x,count(*) y from vm790_bcfe8a202787453d.videopopularity group by sharecount",
            "分享次数",
        )
    if obj.get("optype") == "videopopularity.commentcount_wordcloud":
        textlist = get_data(
            "SELECT commentcount result FROM vm790_bcfe8a202787453d.videopopularity;"
        )
        res = {
            "title": "词云图",
            "imgbs64": generate_wordcloud_base64(
                ",".join([t["result"] for t in textlist])
            ),
        }
    # videopopularity(视频热度统计表)->popularitysckwkwore(热度评分)

    if obj.get("optype") == "videopopularity.popularitysckwkwore_pie":
        res = get_pie(
            "select popularitysckwkwore x,count(*) y from vm790_bcfe8a202787453d.videopopularity group by popularitysckwkwore order by x desc",
            "热度评分",
        )
    if obj.get("optype") == "videopopularity.popularitysckwkwore_pie_v1":
        res = get_pie_v1(
            "select popularitysckwkwore x,count(*) y from vm790_bcfe8a202787453d.videopopularity group by popularitysckwkwore",
            "热度评分",
        )
    if obj.get("optype") == "videopopularity.popularitysckwkwore_pie_v2":
        res = get_pie_v2(
            "select popularitysckwkwore x,count(*) y from vm790_bcfe8a202787453d.videopopularity group by popularitysckwkwore",
            "热度评分",
        )
    if obj.get("optype") == "videopopularity.popularitysckwkwore_line":
        res = get_line(
            "select popularitysckwkwore x,count(*) y from vm790_bcfe8a202787453d.videopopularity group by popularitysckwkwore",
            "热度评分",
        )
    if obj.get("optype") == "videopopularity.popularitysckwkwore_bar":
        res = get_bar(
            "select popularitysckwkwore x,count(*) y from vm790_bcfe8a202787453d.videopopularity group by popularitysckwkwore",
            "热度评分",
        )
    if obj.get("optype") == "videopopularity.popularitysckwkwore_bar_v1":
        res = get_bar_v1(
            "select popularitysckwkwore x,count(*) y from vm790_bcfe8a202787453d.videopopularity group by popularitysckwkwore",
            "热度评分",
        )
    if obj.get("optype") == "videopopularity.publkwkwishtime_line":
        res = get_line(
            "select publkwkwishtime x,count(*) y from vm790_bcfe8a202787453d.videopopularity group by publkwkwishtime order by x",
            "发布时间",
        )
    if obj.get("optype") == "videopopularity.updatetime_line":
        res = get_line(
            "select updatetime x,count(*) y from vm790_bcfe8a202787453d.videopopularity group by updatetime order by x",
            "更新时间",
        )
    # videopopularity(视频热度统计表)->categkwkworyid(关联类别ID)

    if obj.get("optype") == "videopopularity.categkwkworyid_pie":
        res = get_pie(
            "select categkwkworyid x,count(*) y from vm790_bcfe8a202787453d.videopopularity group by categkwkworyid order by x desc",
            "关联类别ID",
        )
    if obj.get("optype") == "videopopularity.categkwkworyid_pie_v1":
        res = get_pie_v1(
            "select categkwkworyid x,count(*) y from vm790_bcfe8a202787453d.videopopularity group by categkwkworyid",
            "关联类别ID",
        )
    if obj.get("optype") == "videopopularity.categkwkworyid_pie_v2":
        res = get_pie_v2(
            "select categkwkworyid x,count(*) y from vm790_bcfe8a202787453d.videopopularity group by categkwkworyid",
            "关联类别ID",
        )
    if obj.get("optype") == "videopopularity.categkwkworyid_line":
        res = get_line(
            "select categkwkworyid x,count(*) y from vm790_bcfe8a202787453d.videopopularity group by categkwkworyid",
            "关联类别ID",
        )
    if obj.get("optype") == "videopopularity.categkwkworyid_bar":
        res = get_bar(
            "select categkwkworyid x,count(*) y from vm790_bcfe8a202787453d.videopopularity group by categkwkworyid",
            "关联类别ID",
        )
    if obj.get("optype") == "videopopularity.categkwkworyid_bar_v1":
        res = get_bar_v1(
            "select categkwkworyid x,count(*) y from vm790_bcfe8a202787453d.videopopularity group by categkwkworyid",
            "关联类别ID",
        )
    # videopopularity(视频热度统计表)->creatkwkworid(关联创作者ID)

    if obj.get("optype") == "videopopularity.creatkwkworid_pie":
        res = get_pie(
            "select creatkwkworid x,count(*) y from vm790_bcfe8a202787453d.videopopularity group by creatkwkworid order by x desc",
            "关联创作者ID",
        )
    if obj.get("optype") == "videopopularity.creatkwkworid_pie_v1":
        res = get_pie_v1(
            "select creatkwkworid x,count(*) y from vm790_bcfe8a202787453d.videopopularity group by creatkwkworid",
            "关联创作者ID",
        )
    if obj.get("optype") == "videopopularity.creatkwkworid_pie_v2":
        res = get_pie_v2(
            "select creatkwkworid x,count(*) y from vm790_bcfe8a202787453d.videopopularity group by creatkwkworid",
            "关联创作者ID",
        )
    if obj.get("optype") == "videopopularity.creatkwkworid_line":
        res = get_line(
            "select creatkwkworid x,count(*) y from vm790_bcfe8a202787453d.videopopularity group by creatkwkworid",
            "关联创作者ID",
        )
    if obj.get("optype") == "videopopularity.creatkwkworid_bar":
        res = get_bar(
            "select creatkwkworid x,count(*) y from vm790_bcfe8a202787453d.videopopularity group by creatkwkworid",
            "关联创作者ID",
        )
    if obj.get("optype") == "videopopularity.creatkwkworid_bar_v1":
        res = get_bar_v1(
            "select creatkwkworid x,count(*) y from vm790_bcfe8a202787453d.videopopularity group by creatkwkworid",
            "关联创作者ID",
        )
    # videorecommendationparams(视频推荐算法参数表)->algkwkworithmname(算法名称)

    if obj.get("optype") == "videorecommendationparams.algkwkworithmname_pie":
        res = get_pie(
            "select algkwkworithmname x,count(*) y from vm790_bcfe8a202787453d.videorecommendationparams group by algkwkworithmname order by x desc",
            "算法名称",
        )
    if obj.get("optype") == "videorecommendationparams.algkwkworithmname_pie_v1":
        res = get_pie_v1(
            "select algkwkworithmname x,count(*) y from vm790_bcfe8a202787453d.videorecommendationparams group by algkwkworithmname",
            "算法名称",
        )
    if obj.get("optype") == "videorecommendationparams.algkwkworithmname_pie_v2":
        res = get_pie_v2(
            "select algkwkworithmname x,count(*) y from vm790_bcfe8a202787453d.videorecommendationparams group by algkwkworithmname",
            "算法名称",
        )
    if obj.get("optype") == "videorecommendationparams.algkwkworithmname_line":
        res = get_line(
            "select algkwkworithmname x,count(*) y from vm790_bcfe8a202787453d.videorecommendationparams group by algkwkworithmname",
            "算法名称",
        )
    if obj.get("optype") == "videorecommendationparams.algkwkworithmname_bar":
        res = get_bar(
            "select algkwkworithmname x,count(*) y from vm790_bcfe8a202787453d.videorecommendationparams group by algkwkworithmname",
            "算法名称",
        )
    if obj.get("optype") == "videorecommendationparams.algkwkworithmname_bar_v1":
        res = get_bar_v1(
            "select algkwkworithmname x,count(*) y from vm790_bcfe8a202787453d.videorecommendationparams group by algkwkworithmname",
            "算法名称",
        )
    # videorecommendationparams(视频推荐算法参数表)->paramname(参数名称)

    if obj.get("optype") == "videorecommendationparams.paramname_pie":
        res = get_pie(
            "select paramname x,count(*) y from vm790_bcfe8a202787453d.videorecommendationparams group by paramname order by x desc",
            "参数名称",
        )
    if obj.get("optype") == "videorecommendationparams.paramname_pie_v1":
        res = get_pie_v1(
            "select paramname x,count(*) y from vm790_bcfe8a202787453d.videorecommendationparams group by paramname",
            "参数名称",
        )
    if obj.get("optype") == "videorecommendationparams.paramname_pie_v2":
        res = get_pie_v2(
            "select paramname x,count(*) y from vm790_bcfe8a202787453d.videorecommendationparams group by paramname",
            "参数名称",
        )
    if obj.get("optype") == "videorecommendationparams.paramname_line":
        res = get_line(
            "select paramname x,count(*) y from vm790_bcfe8a202787453d.videorecommendationparams group by paramname",
            "参数名称",
        )
    if obj.get("optype") == "videorecommendationparams.paramname_bar":
        res = get_bar(
            "select paramname x,count(*) y from vm790_bcfe8a202787453d.videorecommendationparams group by paramname",
            "参数名称",
        )
    if obj.get("optype") == "videorecommendationparams.paramname_bar_v1":
        res = get_bar_v1(
            "select paramname x,count(*) y from vm790_bcfe8a202787453d.videorecommendationparams group by paramname",
            "参数名称",
        )
    # videorecommendationparams(视频推荐算法参数表)->paramvalue(参数值)

    if obj.get("optype") == "videorecommendationparams.paramvalue_pie":
        res = get_pie(
            "select paramvalue x,count(*) y from vm790_bcfe8a202787453d.videorecommendationparams group by paramvalue order by x desc",
            "参数值",
        )
    if obj.get("optype") == "videorecommendationparams.paramvalue_pie_v1":
        res = get_pie_v1(
            "select paramvalue x,count(*) y from vm790_bcfe8a202787453d.videorecommendationparams group by paramvalue",
            "参数值",
        )
    if obj.get("optype") == "videorecommendationparams.paramvalue_pie_v2":
        res = get_pie_v2(
            "select paramvalue x,count(*) y from vm790_bcfe8a202787453d.videorecommendationparams group by paramvalue",
            "参数值",
        )
    if obj.get("optype") == "videorecommendationparams.paramvalue_line":
        res = get_line(
            "select paramvalue x,count(*) y from vm790_bcfe8a202787453d.videorecommendationparams group by paramvalue",
            "参数值",
        )
    if obj.get("optype") == "videorecommendationparams.paramvalue_bar":
        res = get_bar(
            "select paramvalue x,count(*) y from vm790_bcfe8a202787453d.videorecommendationparams group by paramvalue",
            "参数值",
        )
    if obj.get("optype") == "videorecommendationparams.paramvalue_bar_v1":
        res = get_bar_v1(
            "select paramvalue x,count(*) y from vm790_bcfe8a202787453d.videorecommendationparams group by paramvalue",
            "参数值",
        )
    if obj.get("optype") == "videorecommendationparams.description_wordcloud":
        textlist = get_data(
            "SELECT description result FROM vm790_bcfe8a202787453d.videorecommendationparams;"
        )
        res = {
            "title": "词云图",
            "imgbs64": generate_wordcloud_base64(
                ",".join([t["result"] for t in textlist])
            ),
        }
    if obj.get("optype") == "videorecommendationparams.createdat_line":
        res = get_line(
            "select createdat x,count(*) y from vm790_bcfe8a202787453d.videorecommendationparams group by createdat order by x",
            "创建时间",
        )
    if obj.get("optype") == "videorecommendationparams.updatedat_line":
        res = get_line(
            "select updatedat x,count(*) y from vm790_bcfe8a202787453d.videorecommendationparams group by updatedat order by x",
            "更新时间",
        )
    # videorecommendationparams(视频推荐算法参数表)->kwkwisactive(是否启用)

    if obj.get("optype") == "videorecommendationparams.kwkwisactive_pie":
        res = get_pie(
            "select kwkwisactive x,count(*) y from vm790_bcfe8a202787453d.videorecommendationparams group by kwkwisactive order by x desc",
            "是否启用",
        )
    if obj.get("optype") == "videorecommendationparams.kwkwisactive_pie_v1":
        res = get_pie_v1(
            "select kwkwisactive x,count(*) y from vm790_bcfe8a202787453d.videorecommendationparams group by kwkwisactive",
            "是否启用",
        )
    if obj.get("optype") == "videorecommendationparams.kwkwisactive_pie_v2":
        res = get_pie_v2(
            "select kwkwisactive x,count(*) y from vm790_bcfe8a202787453d.videorecommendationparams group by kwkwisactive",
            "是否启用",
        )
    if obj.get("optype") == "videorecommendationparams.kwkwisactive_line":
        res = get_line(
            "select kwkwisactive x,count(*) y from vm790_bcfe8a202787453d.videorecommendationparams group by kwkwisactive",
            "是否启用",
        )
    if obj.get("optype") == "videorecommendationparams.kwkwisactive_bar":
        res = get_bar(
            "select kwkwisactive x,count(*) y from vm790_bcfe8a202787453d.videorecommendationparams group by kwkwisactive",
            "是否启用",
        )
    if obj.get("optype") == "videorecommendationparams.kwkwisactive_bar_v1":
        res = get_bar_v1(
            "select kwkwisactive x,count(*) y from vm790_bcfe8a202787453d.videorecommendationparams group by kwkwisactive",
            "是否启用",
        )
    # videorecommendationparams(视频推荐算法参数表)->videotypeid(视频类型ID关联字段指向视频类型)

    if obj.get("optype") == "videorecommendationparams.videotypeid_pie":
        res = get_pie(
            "select videotypeid x,count(*) y from vm790_bcfe8a202787453d.videorecommendationparams group by videotypeid order by x desc",
            "视频类型ID关联字段指向视频类型",
        )
    if obj.get("optype") == "videorecommendationparams.videotypeid_pie_v1":
        res = get_pie_v1(
            "select videotypeid x,count(*) y from vm790_bcfe8a202787453d.videorecommendationparams group by videotypeid",
            "视频类型ID关联字段指向视频类型",
        )
    if obj.get("optype") == "videorecommendationparams.videotypeid_pie_v2":
        res = get_pie_v2(
            "select videotypeid x,count(*) y from vm790_bcfe8a202787453d.videorecommendationparams group by videotypeid",
            "视频类型ID关联字段指向视频类型",
        )
    if obj.get("optype") == "videorecommendationparams.videotypeid_line":
        res = get_line(
            "select videotypeid x,count(*) y from vm790_bcfe8a202787453d.videorecommendationparams group by videotypeid",
            "视频类型ID关联字段指向视频类型",
        )
    if obj.get("optype") == "videorecommendationparams.videotypeid_bar":
        res = get_bar(
            "select videotypeid x,count(*) y from vm790_bcfe8a202787453d.videorecommendationparams group by videotypeid",
            "视频类型ID关联字段指向视频类型",
        )
    if obj.get("optype") == "videorecommendationparams.videotypeid_bar_v1":
        res = get_bar_v1(
            "select videotypeid x,count(*) y from vm790_bcfe8a202787453d.videorecommendationparams group by videotypeid",
            "视频类型ID关联字段指向视频类型",
        )
    # videoadinfo(视频广告信息表)->videoadid(视频广告ID)

    if obj.get("optype") == "videoadinfo.videoadid_pie":
        res = get_pie(
            "select videoadid x,count(*) y from vm790_bcfe8a202787453d.videoadinfo group by videoadid order by x desc",
            "视频广告ID",
        )
    if obj.get("optype") == "videoadinfo.videoadid_pie_v1":
        res = get_pie_v1(
            "select videoadid x,count(*) y from vm790_bcfe8a202787453d.videoadinfo group by videoadid",
            "视频广告ID",
        )
    if obj.get("optype") == "videoadinfo.videoadid_pie_v2":
        res = get_pie_v2(
            "select videoadid x,count(*) y from vm790_bcfe8a202787453d.videoadinfo group by videoadid",
            "视频广告ID",
        )
    if obj.get("optype") == "videoadinfo.videoadid_line":
        res = get_line(
            "select videoadid x,count(*) y from vm790_bcfe8a202787453d.videoadinfo group by videoadid",
            "视频广告ID",
        )
    if obj.get("optype") == "videoadinfo.videoadid_bar":
        res = get_bar(
            "select videoadid x,count(*) y from vm790_bcfe8a202787453d.videoadinfo group by videoadid",
            "视频广告ID",
        )
    if obj.get("optype") == "videoadinfo.videoadid_bar_v1":
        res = get_bar_v1(
            "select videoadid x,count(*) y from vm790_bcfe8a202787453d.videoadinfo group by videoadid",
            "视频广告ID",
        )
    # videoadinfo(视频广告信息表)->title(广告标题)

    if obj.get("optype") == "videoadinfo.title_pie":
        res = get_pie(
            "select title x,count(*) y from vm790_bcfe8a202787453d.videoadinfo group by title order by x desc",
            "广告标题",
        )
    if obj.get("optype") == "videoadinfo.title_pie_v1":
        res = get_pie_v1(
            "select title x,count(*) y from vm790_bcfe8a202787453d.videoadinfo group by title",
            "广告标题",
        )
    if obj.get("optype") == "videoadinfo.title_pie_v2":
        res = get_pie_v2(
            "select title x,count(*) y from vm790_bcfe8a202787453d.videoadinfo group by title",
            "广告标题",
        )
    if obj.get("optype") == "videoadinfo.title_line":
        res = get_line(
            "select title x,count(*) y from vm790_bcfe8a202787453d.videoadinfo group by title",
            "广告标题",
        )
    if obj.get("optype") == "videoadinfo.title_bar":
        res = get_bar(
            "select title x,count(*) y from vm790_bcfe8a202787453d.videoadinfo group by title",
            "广告标题",
        )
    if obj.get("optype") == "videoadinfo.title_bar_v1":
        res = get_bar_v1(
            "select title x,count(*) y from vm790_bcfe8a202787453d.videoadinfo group by title",
            "广告标题",
        )
    if obj.get("optype") == "videoadinfo.description_wordcloud":
        textlist = get_data(
            "SELECT description result FROM vm790_bcfe8a202787453d.videoadinfo;"
        )
        res = {
            "title": "词云图",
            "imgbs64": generate_wordcloud_base64(
                ",".join([t["result"] for t in textlist])
            ),
        }
    if obj.get("optype") == "videoadinfo.starttime_line":
        res = get_line(
            "select starttime x,count(*) y from vm790_bcfe8a202787453d.videoadinfo group by starttime order by x",
            "开始时间",
        )
    if obj.get("optype") == "videoadinfo.endtime_line":
        res = get_line(
            "select endtime x,count(*) y from vm790_bcfe8a202787453d.videoadinfo group by endtime order by x",
            "结束时间",
        )
    # videoadinfo(视频广告信息表)->videourl(视频链接)

    if obj.get("optype") == "videoadinfo.videourl_pie":
        res = get_pie(
            "select videourl x,count(*) y from vm790_bcfe8a202787453d.videoadinfo group by videourl order by x desc",
            "视频链接",
        )
    if obj.get("optype") == "videoadinfo.videourl_pie_v1":
        res = get_pie_v1(
            "select videourl x,count(*) y from vm790_bcfe8a202787453d.videoadinfo group by videourl",
            "视频链接",
        )
    if obj.get("optype") == "videoadinfo.videourl_pie_v2":
        res = get_pie_v2(
            "select videourl x,count(*) y from vm790_bcfe8a202787453d.videoadinfo group by videourl",
            "视频链接",
        )
    if obj.get("optype") == "videoadinfo.videourl_line":
        res = get_line(
            "select videourl x,count(*) y from vm790_bcfe8a202787453d.videoadinfo group by videourl",
            "视频链接",
        )
    if obj.get("optype") == "videoadinfo.videourl_bar":
        res = get_bar(
            "select videourl x,count(*) y from vm790_bcfe8a202787453d.videoadinfo group by videourl",
            "视频链接",
        )
    if obj.get("optype") == "videoadinfo.videourl_bar_v1":
        res = get_bar_v1(
            "select videourl x,count(*) y from vm790_bcfe8a202787453d.videoadinfo group by videourl",
            "视频链接",
        )
    # videoadinfo(视频广告信息表)->thumbnailurl(缩略图链接)

    if obj.get("optype") == "videoadinfo.thumbnailurl_pie":
        res = get_pie(
            "select thumbnailurl x,count(*) y from vm790_bcfe8a202787453d.videoadinfo group by thumbnailurl order by x desc",
            "缩略图链接",
        )
    if obj.get("optype") == "videoadinfo.thumbnailurl_pie_v1":
        res = get_pie_v1(
            "select thumbnailurl x,count(*) y from vm790_bcfe8a202787453d.videoadinfo group by thumbnailurl",
            "缩略图链接",
        )
    if obj.get("optype") == "videoadinfo.thumbnailurl_pie_v2":
        res = get_pie_v2(
            "select thumbnailurl x,count(*) y from vm790_bcfe8a202787453d.videoadinfo group by thumbnailurl",
            "缩略图链接",
        )
    if obj.get("optype") == "videoadinfo.thumbnailurl_line":
        res = get_line(
            "select thumbnailurl x,count(*) y from vm790_bcfe8a202787453d.videoadinfo group by thumbnailurl",
            "缩略图链接",
        )
    if obj.get("optype") == "videoadinfo.thumbnailurl_bar":
        res = get_bar(
            "select thumbnailurl x,count(*) y from vm790_bcfe8a202787453d.videoadinfo group by thumbnailurl",
            "缩略图链接",
        )
    if obj.get("optype") == "videoadinfo.thumbnailurl_bar_v1":
        res = get_bar_v1(
            "select thumbnailurl x,count(*) y from vm790_bcfe8a202787453d.videoadinfo group by thumbnailurl",
            "缩略图链接",
        )
    # videoadinfo(视频广告信息表)->advertkwkwiserid(广告主ID)

    if obj.get("optype") == "videoadinfo.advertkwkwiserid_pie":
        res = get_pie(
            "select advertkwkwiserid x,count(*) y from vm790_bcfe8a202787453d.videoadinfo group by advertkwkwiserid order by x desc",
            "广告主ID",
        )
    if obj.get("optype") == "videoadinfo.advertkwkwiserid_pie_v1":
        res = get_pie_v1(
            "select advertkwkwiserid x,count(*) y from vm790_bcfe8a202787453d.videoadinfo group by advertkwkwiserid",
            "广告主ID",
        )
    if obj.get("optype") == "videoadinfo.advertkwkwiserid_pie_v2":
        res = get_pie_v2(
            "select advertkwkwiserid x,count(*) y from vm790_bcfe8a202787453d.videoadinfo group by advertkwkwiserid",
            "广告主ID",
        )
    if obj.get("optype") == "videoadinfo.advertkwkwiserid_line":
        res = get_line(
            "select advertkwkwiserid x,count(*) y from vm790_bcfe8a202787453d.videoadinfo group by advertkwkwiserid",
            "广告主ID",
        )
    if obj.get("optype") == "videoadinfo.advertkwkwiserid_bar":
        res = get_bar(
            "select advertkwkwiserid x,count(*) y from vm790_bcfe8a202787453d.videoadinfo group by advertkwkwiserid",
            "广告主ID",
        )
    if obj.get("optype") == "videoadinfo.advertkwkwiserid_bar_v1":
        res = get_bar_v1(
            "select advertkwkwiserid x,count(*) y from vm790_bcfe8a202787453d.videoadinfo group by advertkwkwiserid",
            "广告主ID",
        )
    # videoadinfo(视频广告信息表)->categkwkworyid(广告分类ID)

    if obj.get("optype") == "videoadinfo.categkwkworyid_pie":
        res = get_pie(
            "select categkwkworyid x,count(*) y from vm790_bcfe8a202787453d.videoadinfo group by categkwkworyid order by x desc",
            "广告分类ID",
        )
    if obj.get("optype") == "videoadinfo.categkwkworyid_pie_v1":
        res = get_pie_v1(
            "select categkwkworyid x,count(*) y from vm790_bcfe8a202787453d.videoadinfo group by categkwkworyid",
            "广告分类ID",
        )
    if obj.get("optype") == "videoadinfo.categkwkworyid_pie_v2":
        res = get_pie_v2(
            "select categkwkworyid x,count(*) y from vm790_bcfe8a202787453d.videoadinfo group by categkwkworyid",
            "广告分类ID",
        )
    if obj.get("optype") == "videoadinfo.categkwkworyid_line":
        res = get_line(
            "select categkwkworyid x,count(*) y from vm790_bcfe8a202787453d.videoadinfo group by categkwkworyid",
            "广告分类ID",
        )
    if obj.get("optype") == "videoadinfo.categkwkworyid_bar":
        res = get_bar(
            "select categkwkworyid x,count(*) y from vm790_bcfe8a202787453d.videoadinfo group by categkwkworyid",
            "广告分类ID",
        )
    if obj.get("optype") == "videoadinfo.categkwkworyid_bar_v1":
        res = get_bar_v1(
            "select categkwkworyid x,count(*) y from vm790_bcfe8a202787453d.videoadinfo group by categkwkworyid",
            "广告分类ID",
        )
    # videoadinfo(视频广告信息表)->status(广告状态)

    if obj.get("optype") == "videoadinfo.status_pie":
        res = get_pie(
            "select status x,count(*) y from vm790_bcfe8a202787453d.videoadinfo group by status order by x desc",
            "广告状态",
        )
    if obj.get("optype") == "videoadinfo.status_pie_v1":
        res = get_pie_v1(
            "select status x,count(*) y from vm790_bcfe8a202787453d.videoadinfo group by status",
            "广告状态",
        )
    if obj.get("optype") == "videoadinfo.status_pie_v2":
        res = get_pie_v2(
            "select status x,count(*) y from vm790_bcfe8a202787453d.videoadinfo group by status",
            "广告状态",
        )
    if obj.get("optype") == "videoadinfo.status_line":
        res = get_line(
            "select status x,count(*) y from vm790_bcfe8a202787453d.videoadinfo group by status",
            "广告状态",
        )
    if obj.get("optype") == "videoadinfo.status_bar":
        res = get_bar(
            "select status x,count(*) y from vm790_bcfe8a202787453d.videoadinfo group by status",
            "广告状态",
        )
    if obj.get("optype") == "videoadinfo.status_bar_v1":
        res = get_bar_v1(
            "select status x,count(*) y from vm790_bcfe8a202787453d.videoadinfo group by status",
            "广告状态",
        )
    # videoadplayreckwkword(视频广告播放记录表)->videoadid(视频广告ID)

    if obj.get("optype") == "videoadplayreckwkword.videoadid_pie":
        res = get_pie(
            "select videoadid x,count(*) y from vm790_bcfe8a202787453d.videoadplayreckwkword group by videoadid order by x desc",
            "视频广告ID",
        )
    if obj.get("optype") == "videoadplayreckwkword.videoadid_pie_v1":
        res = get_pie_v1(
            "select videoadid x,count(*) y from vm790_bcfe8a202787453d.videoadplayreckwkword group by videoadid",
            "视频广告ID",
        )
    if obj.get("optype") == "videoadplayreckwkword.videoadid_pie_v2":
        res = get_pie_v2(
            "select videoadid x,count(*) y from vm790_bcfe8a202787453d.videoadplayreckwkword group by videoadid",
            "视频广告ID",
        )
    if obj.get("optype") == "videoadplayreckwkword.videoadid_line":
        res = get_line(
            "select videoadid x,count(*) y from vm790_bcfe8a202787453d.videoadplayreckwkword group by videoadid",
            "视频广告ID",
        )
    if obj.get("optype") == "videoadplayreckwkword.videoadid_bar":
        res = get_bar(
            "select videoadid x,count(*) y from vm790_bcfe8a202787453d.videoadplayreckwkword group by videoadid",
            "视频广告ID",
        )
    if obj.get("optype") == "videoadplayreckwkword.videoadid_bar_v1":
        res = get_bar_v1(
            "select videoadid x,count(*) y from vm790_bcfe8a202787453d.videoadplayreckwkword group by videoadid",
            "视频广告ID",
        )
    if obj.get("optype") == "videoadplayreckwkword.playtime_line":
        res = get_line(
            "select playtime x,count(*) y from vm790_bcfe8a202787453d.videoadplayreckwkword group by playtime order by x",
            "播放时间",
        )
    # videoadplayreckwkword(视频广告播放记录表)->playduration(播放时长)

    if obj.get("optype") == "videoadplayreckwkword.playduration_pie":
        res = get_pie(
            "select playduration x,count(*) y from vm790_bcfe8a202787453d.videoadplayreckwkword group by playduration order by x desc",
            "播放时长",
        )
    if obj.get("optype") == "videoadplayreckwkword.playduration_pie_v1":
        res = get_pie_v1(
            "select playduration x,count(*) y from vm790_bcfe8a202787453d.videoadplayreckwkword group by playduration",
            "播放时长",
        )
    if obj.get("optype") == "videoadplayreckwkword.playduration_pie_v2":
        res = get_pie_v2(
            "select playduration x,count(*) y from vm790_bcfe8a202787453d.videoadplayreckwkword group by playduration",
            "播放时长",
        )
    if obj.get("optype") == "videoadplayreckwkword.playduration_line":
        res = get_line(
            "select playduration x,count(*) y from vm790_bcfe8a202787453d.videoadplayreckwkword group by playduration",
            "播放时长",
        )
    if obj.get("optype") == "videoadplayreckwkword.playduration_bar":
        res = get_bar(
            "select playduration x,count(*) y from vm790_bcfe8a202787453d.videoadplayreckwkword group by playduration",
            "播放时长",
        )
    if obj.get("optype") == "videoadplayreckwkword.playduration_bar_v1":
        res = get_bar_v1(
            "select playduration x,count(*) y from vm790_bcfe8a202787453d.videoadplayreckwkword group by playduration",
            "播放时长",
        )
    # videoadplayreckwkword(视频广告播放记录表)->userid(用户ID关联用户)

    if obj.get("optype") == "videoadplayreckwkword.userid_pie":
        res = get_pie(
            "select userid x,count(*) y from vm790_bcfe8a202787453d.videoadplayreckwkword group by userid order by x desc",
            "用户ID关联用户",
        )
    if obj.get("optype") == "videoadplayreckwkword.userid_pie_v1":
        res = get_pie_v1(
            "select userid x,count(*) y from vm790_bcfe8a202787453d.videoadplayreckwkword group by userid",
            "用户ID关联用户",
        )
    if obj.get("optype") == "videoadplayreckwkword.userid_pie_v2":
        res = get_pie_v2(
            "select userid x,count(*) y from vm790_bcfe8a202787453d.videoadplayreckwkword group by userid",
            "用户ID关联用户",
        )
    if obj.get("optype") == "videoadplayreckwkword.userid_line":
        res = get_line(
            "select userid x,count(*) y from vm790_bcfe8a202787453d.videoadplayreckwkword group by userid",
            "用户ID关联用户",
        )
    if obj.get("optype") == "videoadplayreckwkword.userid_bar":
        res = get_bar(
            "select userid x,count(*) y from vm790_bcfe8a202787453d.videoadplayreckwkword group by userid",
            "用户ID关联用户",
        )
    if obj.get("optype") == "videoadplayreckwkword.userid_bar_v1":
        res = get_bar_v1(
            "select userid x,count(*) y from vm790_bcfe8a202787453d.videoadplayreckwkword group by userid",
            "用户ID关联用户",
        )
    # videoadplayreckwkword(视频广告播放记录表)->devicetype(设备类型)

    if obj.get("optype") == "videoadplayreckwkword.devicetype_pie":
        res = get_pie(
            "select devicetype x,count(*) y from vm790_bcfe8a202787453d.videoadplayreckwkword group by devicetype order by x desc",
            "设备类型",
        )
    if obj.get("optype") == "videoadplayreckwkword.devicetype_pie_v1":
        res = get_pie_v1(
            "select devicetype x,count(*) y from vm790_bcfe8a202787453d.videoadplayreckwkword group by devicetype",
            "设备类型",
        )
    if obj.get("optype") == "videoadplayreckwkword.devicetype_pie_v2":
        res = get_pie_v2(
            "select devicetype x,count(*) y from vm790_bcfe8a202787453d.videoadplayreckwkword group by devicetype",
            "设备类型",
        )
    if obj.get("optype") == "videoadplayreckwkword.devicetype_line":
        res = get_line(
            "select devicetype x,count(*) y from vm790_bcfe8a202787453d.videoadplayreckwkword group by devicetype",
            "设备类型",
        )
    if obj.get("optype") == "videoadplayreckwkword.devicetype_bar":
        res = get_bar(
            "select devicetype x,count(*) y from vm790_bcfe8a202787453d.videoadplayreckwkword group by devicetype",
            "设备类型",
        )
    if obj.get("optype") == "videoadplayreckwkword.devicetype_bar_v1":
        res = get_bar_v1(
            "select devicetype x,count(*) y from vm790_bcfe8a202787453d.videoadplayreckwkword group by devicetype",
            "设备类型",
        )
    if obj.get("optype") == "videoadplayreckwkword.ipaddressip_wordcloud":
        textlist = get_data(
            "SELECT ipaddressip result FROM vm790_bcfe8a202787453d.videoadplayreckwkword;"
        )
        res = {
            "title": "词云图",
            "imgbs64": generate_wordcloud_base64(
                ",".join([t["result"] for t in textlist])
            ),
        }
    # videoadplayreckwkword(视频广告播放记录表)->location(地理位置)

    if obj.get("optype") == "videoadplayreckwkword.location_pie":
        res = get_pie(
            "select location x,count(*) y from vm790_bcfe8a202787453d.videoadplayreckwkword group by location order by x desc",
            "地理位置",
        )
    if obj.get("optype") == "videoadplayreckwkword.location_pie_v1":
        res = get_pie_v1(
            "select location x,count(*) y from vm790_bcfe8a202787453d.videoadplayreckwkword group by location",
            "地理位置",
        )
    if obj.get("optype") == "videoadplayreckwkword.location_pie_v2":
        res = get_pie_v2(
            "select location x,count(*) y from vm790_bcfe8a202787453d.videoadplayreckwkword group by location",
            "地理位置",
        )
    if obj.get("optype") == "videoadplayreckwkword.location_line":
        res = get_line(
            "select location x,count(*) y from vm790_bcfe8a202787453d.videoadplayreckwkword group by location",
            "地理位置",
        )
    if obj.get("optype") == "videoadplayreckwkword.location_bar":
        res = get_bar(
            "select location x,count(*) y from vm790_bcfe8a202787453d.videoadplayreckwkword group by location",
            "地理位置",
        )
    if obj.get("optype") == "videoadplayreckwkword.location_bar_v1":
        res = get_bar_v1(
            "select location x,count(*) y from vm790_bcfe8a202787453d.videoadplayreckwkword group by location",
            "地理位置",
        )
    # videoadplayreckwkword(视频广告播放记录表)->playstatus(播放状态如成功、失败、中断等)

    if obj.get("optype") == "videoadplayreckwkword.playstatus_pie":
        res = get_pie(
            "select playstatus x,count(*) y from vm790_bcfe8a202787453d.videoadplayreckwkword group by playstatus order by x desc",
            "播放状态如成功、失败、中断等",
        )
    if obj.get("optype") == "videoadplayreckwkword.playstatus_pie_v1":
        res = get_pie_v1(
            "select playstatus x,count(*) y from vm790_bcfe8a202787453d.videoadplayreckwkword group by playstatus",
            "播放状态如成功、失败、中断等",
        )
    if obj.get("optype") == "videoadplayreckwkword.playstatus_pie_v2":
        res = get_pie_v2(
            "select playstatus x,count(*) y from vm790_bcfe8a202787453d.videoadplayreckwkword group by playstatus",
            "播放状态如成功、失败、中断等",
        )
    if obj.get("optype") == "videoadplayreckwkword.playstatus_line":
        res = get_line(
            "select playstatus x,count(*) y from vm790_bcfe8a202787453d.videoadplayreckwkword group by playstatus",
            "播放状态如成功、失败、中断等",
        )
    if obj.get("optype") == "videoadplayreckwkword.playstatus_bar":
        res = get_bar(
            "select playstatus x,count(*) y from vm790_bcfe8a202787453d.videoadplayreckwkword group by playstatus",
            "播放状态如成功、失败、中断等",
        )
    if obj.get("optype") == "videoadplayreckwkword.playstatus_bar_v1":
        res = get_bar_v1(
            "select playstatus x,count(*) y from vm790_bcfe8a202787453d.videoadplayreckwkword group by playstatus",
            "播放状态如成功、失败、中断等",
        )
    # videodanmu(视频弹幕表)->videoid(视频唯一标识符关联视频)

    if obj.get("optype") == "videodanmu.videoid_pie":
        res = get_pie(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videodanmu group by videoid order by x desc",
            "视频唯一标识符关联视频",
        )
    if obj.get("optype") == "videodanmu.videoid_pie_v1":
        res = get_pie_v1(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videodanmu group by videoid",
            "视频唯一标识符关联视频",
        )
    if obj.get("optype") == "videodanmu.videoid_pie_v2":
        res = get_pie_v2(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videodanmu group by videoid",
            "视频唯一标识符关联视频",
        )
    if obj.get("optype") == "videodanmu.videoid_line":
        res = get_line(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videodanmu group by videoid",
            "视频唯一标识符关联视频",
        )
    if obj.get("optype") == "videodanmu.videoid_bar":
        res = get_bar(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videodanmu group by videoid",
            "视频唯一标识符关联视频",
        )
    if obj.get("optype") == "videodanmu.videoid_bar_v1":
        res = get_bar_v1(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videodanmu group by videoid",
            "视频唯一标识符关联视频",
        )
    if obj.get("optype") == "videodanmu.danmucontent_wordcloud":
        textlist = get_data(
            "SELECT danmucontent result FROM vm790_bcfe8a202787453d.videodanmu;"
        )
        res = {
            "title": "词云图",
            "imgbs64": generate_wordcloud_base64(
                ",".join([t["result"] for t in textlist])
            ),
        }
    # videodanmu(视频弹幕表)->userid(发送弹幕的用户唯一标识符关联用户)

    if obj.get("optype") == "videodanmu.userid_pie":
        res = get_pie(
            "select userid x,count(*) y from vm790_bcfe8a202787453d.videodanmu group by userid order by x desc",
            "发送弹幕的用户唯一标识符关联用户",
        )
    if obj.get("optype") == "videodanmu.userid_pie_v1":
        res = get_pie_v1(
            "select userid x,count(*) y from vm790_bcfe8a202787453d.videodanmu group by userid",
            "发送弹幕的用户唯一标识符关联用户",
        )
    if obj.get("optype") == "videodanmu.userid_pie_v2":
        res = get_pie_v2(
            "select userid x,count(*) y from vm790_bcfe8a202787453d.videodanmu group by userid",
            "发送弹幕的用户唯一标识符关联用户",
        )
    if obj.get("optype") == "videodanmu.userid_line":
        res = get_line(
            "select userid x,count(*) y from vm790_bcfe8a202787453d.videodanmu group by userid",
            "发送弹幕的用户唯一标识符关联用户",
        )
    if obj.get("optype") == "videodanmu.userid_bar":
        res = get_bar(
            "select userid x,count(*) y from vm790_bcfe8a202787453d.videodanmu group by userid",
            "发送弹幕的用户唯一标识符关联用户",
        )
    if obj.get("optype") == "videodanmu.userid_bar_v1":
        res = get_bar_v1(
            "select userid x,count(*) y from vm790_bcfe8a202787453d.videodanmu group by userid",
            "发送弹幕的用户唯一标识符关联用户",
        )
    if obj.get("optype") == "videodanmu.sendtime_line":
        res = get_line(
            "select sendtime x,count(*) y from vm790_bcfe8a202787453d.videodanmu group by sendtime order by x",
            "发送时间",
        )
    # videodanmu(视频弹幕表)->colkwkwor(弹幕颜色)

    if obj.get("optype") == "videodanmu.colkwkwor_pie":
        res = get_pie(
            "select colkwkwor x,count(*) y from vm790_bcfe8a202787453d.videodanmu group by colkwkwor order by x desc",
            "弹幕颜色",
        )
    if obj.get("optype") == "videodanmu.colkwkwor_pie_v1":
        res = get_pie_v1(
            "select colkwkwor x,count(*) y from vm790_bcfe8a202787453d.videodanmu group by colkwkwor",
            "弹幕颜色",
        )
    if obj.get("optype") == "videodanmu.colkwkwor_pie_v2":
        res = get_pie_v2(
            "select colkwkwor x,count(*) y from vm790_bcfe8a202787453d.videodanmu group by colkwkwor",
            "弹幕颜色",
        )
    if obj.get("optype") == "videodanmu.colkwkwor_line":
        res = get_line(
            "select colkwkwor x,count(*) y from vm790_bcfe8a202787453d.videodanmu group by colkwkwor",
            "弹幕颜色",
        )
    if obj.get("optype") == "videodanmu.colkwkwor_bar":
        res = get_bar(
            "select colkwkwor x,count(*) y from vm790_bcfe8a202787453d.videodanmu group by colkwkwor",
            "弹幕颜色",
        )
    if obj.get("optype") == "videodanmu.colkwkwor_bar_v1":
        res = get_bar_v1(
            "select colkwkwor x,count(*) y from vm790_bcfe8a202787453d.videodanmu group by colkwkwor",
            "弹幕颜色",
        )
    # videodanmu(视频弹幕表)->fontsize(字体大小)

    if obj.get("optype") == "videodanmu.fontsize_pie":
        res = get_pie(
            "select fontsize x,count(*) y from vm790_bcfe8a202787453d.videodanmu group by fontsize order by x desc",
            "字体大小",
        )
    if obj.get("optype") == "videodanmu.fontsize_pie_v1":
        res = get_pie_v1(
            "select fontsize x,count(*) y from vm790_bcfe8a202787453d.videodanmu group by fontsize",
            "字体大小",
        )
    if obj.get("optype") == "videodanmu.fontsize_pie_v2":
        res = get_pie_v2(
            "select fontsize x,count(*) y from vm790_bcfe8a202787453d.videodanmu group by fontsize",
            "字体大小",
        )
    if obj.get("optype") == "videodanmu.fontsize_line":
        res = get_line(
            "select fontsize x,count(*) y from vm790_bcfe8a202787453d.videodanmu group by fontsize",
            "字体大小",
        )
    if obj.get("optype") == "videodanmu.fontsize_bar":
        res = get_bar(
            "select fontsize x,count(*) y from vm790_bcfe8a202787453d.videodanmu group by fontsize",
            "字体大小",
        )
    if obj.get("optype") == "videodanmu.fontsize_bar_v1":
        res = get_bar_v1(
            "select fontsize x,count(*) y from vm790_bcfe8a202787453d.videodanmu group by fontsize",
            "字体大小",
        )
    # videodanmu(视频弹幕表)->kwkwisvkwkwisible(是否可见用于控制弹幕的显示与隐藏)

    if obj.get("optype") == "videodanmu.kwkwisvkwkwisible_pie":
        res = get_pie(
            "select kwkwisvkwkwisible x,count(*) y from vm790_bcfe8a202787453d.videodanmu group by kwkwisvkwkwisible order by x desc",
            "是否可见用于控制弹幕的显示与隐藏",
        )
    if obj.get("optype") == "videodanmu.kwkwisvkwkwisible_pie_v1":
        res = get_pie_v1(
            "select kwkwisvkwkwisible x,count(*) y from vm790_bcfe8a202787453d.videodanmu group by kwkwisvkwkwisible",
            "是否可见用于控制弹幕的显示与隐藏",
        )
    if obj.get("optype") == "videodanmu.kwkwisvkwkwisible_pie_v2":
        res = get_pie_v2(
            "select kwkwisvkwkwisible x,count(*) y from vm790_bcfe8a202787453d.videodanmu group by kwkwisvkwkwisible",
            "是否可见用于控制弹幕的显示与隐藏",
        )
    if obj.get("optype") == "videodanmu.kwkwisvkwkwisible_line":
        res = get_line(
            "select kwkwisvkwkwisible x,count(*) y from vm790_bcfe8a202787453d.videodanmu group by kwkwisvkwkwisible",
            "是否可见用于控制弹幕的显示与隐藏",
        )
    if obj.get("optype") == "videodanmu.kwkwisvkwkwisible_bar":
        res = get_bar(
            "select kwkwisvkwkwisible x,count(*) y from vm790_bcfe8a202787453d.videodanmu group by kwkwisvkwkwisible",
            "是否可见用于控制弹幕的显示与隐藏",
        )
    if obj.get("optype") == "videodanmu.kwkwisvkwkwisible_bar_v1":
        res = get_bar_v1(
            "select kwkwisvkwkwisible x,count(*) y from vm790_bcfe8a202787453d.videodanmu group by kwkwisvkwkwisible",
            "是否可见用于控制弹幕的显示与隐藏",
        )
    # videodanmu(视频弹幕表)->position(弹幕位置如顶部、底部、滚动等)

    if obj.get("optype") == "videodanmu.position_pie":
        res = get_pie(
            "select position x,count(*) y from vm790_bcfe8a202787453d.videodanmu group by position order by x desc",
            "弹幕位置如顶部、底部、滚动等",
        )
    if obj.get("optype") == "videodanmu.position_pie_v1":
        res = get_pie_v1(
            "select position x,count(*) y from vm790_bcfe8a202787453d.videodanmu group by position",
            "弹幕位置如顶部、底部、滚动等",
        )
    if obj.get("optype") == "videodanmu.position_pie_v2":
        res = get_pie_v2(
            "select position x,count(*) y from vm790_bcfe8a202787453d.videodanmu group by position",
            "弹幕位置如顶部、底部、滚动等",
        )
    if obj.get("optype") == "videodanmu.position_line":
        res = get_line(
            "select position x,count(*) y from vm790_bcfe8a202787453d.videodanmu group by position",
            "弹幕位置如顶部、底部、滚动等",
        )
    if obj.get("optype") == "videodanmu.position_bar":
        res = get_bar(
            "select position x,count(*) y from vm790_bcfe8a202787453d.videodanmu group by position",
            "弹幕位置如顶部、底部、滚动等",
        )
    if obj.get("optype") == "videodanmu.position_bar_v1":
        res = get_bar_v1(
            "select position x,count(*) y from vm790_bcfe8a202787453d.videodanmu group by position",
            "弹幕位置如顶部、底部、滚动等",
        )
    # videodanmu(视频弹幕表)->duration(弹幕显示时长秒)

    if obj.get("optype") == "videodanmu.duration_pie":
        res = get_pie(
            "select duration x,count(*) y from vm790_bcfe8a202787453d.videodanmu group by duration order by x desc",
            "弹幕显示时长秒",
        )
    if obj.get("optype") == "videodanmu.duration_pie_v1":
        res = get_pie_v1(
            "select duration x,count(*) y from vm790_bcfe8a202787453d.videodanmu group by duration",
            "弹幕显示时长秒",
        )
    if obj.get("optype") == "videodanmu.duration_pie_v2":
        res = get_pie_v2(
            "select duration x,count(*) y from vm790_bcfe8a202787453d.videodanmu group by duration",
            "弹幕显示时长秒",
        )
    if obj.get("optype") == "videodanmu.duration_line":
        res = get_line(
            "select duration x,count(*) y from vm790_bcfe8a202787453d.videodanmu group by duration",
            "弹幕显示时长秒",
        )
    if obj.get("optype") == "videodanmu.duration_bar":
        res = get_bar(
            "select duration x,count(*) y from vm790_bcfe8a202787453d.videodanmu group by duration",
            "弹幕显示时长秒",
        )
    if obj.get("optype") == "videodanmu.duration_bar_v1":
        res = get_bar_v1(
            "select duration x,count(*) y from vm790_bcfe8a202787453d.videodanmu group by duration",
            "弹幕显示时长秒",
        )
    # videodanmublockwkwkwords(视频弹幕屏蔽词表)->wkwkword(屏蔽词)

    if obj.get("optype") == "videodanmublockwkwkwords.wkwkword_pie":
        res = get_pie(
            "select wkwkword x,count(*) y from vm790_bcfe8a202787453d.videodanmublockwkwkwords group by wkwkword order by x desc",
            "屏蔽词",
        )
    if obj.get("optype") == "videodanmublockwkwkwords.wkwkword_pie_v1":
        res = get_pie_v1(
            "select wkwkword x,count(*) y from vm790_bcfe8a202787453d.videodanmublockwkwkwords group by wkwkword",
            "屏蔽词",
        )
    if obj.get("optype") == "videodanmublockwkwkwords.wkwkword_pie_v2":
        res = get_pie_v2(
            "select wkwkword x,count(*) y from vm790_bcfe8a202787453d.videodanmublockwkwkwords group by wkwkword",
            "屏蔽词",
        )
    if obj.get("optype") == "videodanmublockwkwkwords.wkwkword_line":
        res = get_line(
            "select wkwkword x,count(*) y from vm790_bcfe8a202787453d.videodanmublockwkwkwords group by wkwkword",
            "屏蔽词",
        )
    if obj.get("optype") == "videodanmublockwkwkwords.wkwkword_bar":
        res = get_bar(
            "select wkwkword x,count(*) y from vm790_bcfe8a202787453d.videodanmublockwkwkwords group by wkwkword",
            "屏蔽词",
        )
    if obj.get("optype") == "videodanmublockwkwkwords.wkwkword_bar_v1":
        res = get_bar_v1(
            "select wkwkword x,count(*) y from vm790_bcfe8a202787453d.videodanmublockwkwkwords group by wkwkword",
            "屏蔽词",
        )
    # videodanmublockwkwkwords(视频弹幕屏蔽词表)->videoid(视频ID关联字段指向视频的ID)

    if obj.get("optype") == "videodanmublockwkwkwords.videoid_pie":
        res = get_pie(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videodanmublockwkwkwords group by videoid order by x desc",
            "视频ID关联字段指向视频的ID",
        )
    if obj.get("optype") == "videodanmublockwkwkwords.videoid_pie_v1":
        res = get_pie_v1(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videodanmublockwkwkwords group by videoid",
            "视频ID关联字段指向视频的ID",
        )
    if obj.get("optype") == "videodanmublockwkwkwords.videoid_pie_v2":
        res = get_pie_v2(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videodanmublockwkwkwords group by videoid",
            "视频ID关联字段指向视频的ID",
        )
    if obj.get("optype") == "videodanmublockwkwkwords.videoid_line":
        res = get_line(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videodanmublockwkwkwords group by videoid",
            "视频ID关联字段指向视频的ID",
        )
    if obj.get("optype") == "videodanmublockwkwkwords.videoid_bar":
        res = get_bar(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videodanmublockwkwkwords group by videoid",
            "视频ID关联字段指向视频的ID",
        )
    if obj.get("optype") == "videodanmublockwkwkwords.videoid_bar_v1":
        res = get_bar_v1(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videodanmublockwkwkwords group by videoid",
            "视频ID关联字段指向视频的ID",
        )
    # videodanmublockwkwkwords(视频弹幕屏蔽词表)->creatkwkworid(创建者ID关联字段指向用户的ID)

    if obj.get("optype") == "videodanmublockwkwkwords.creatkwkworid_pie":
        res = get_pie(
            "select creatkwkworid x,count(*) y from vm790_bcfe8a202787453d.videodanmublockwkwkwords group by creatkwkworid order by x desc",
            "创建者ID关联字段指向用户的ID",
        )
    if obj.get("optype") == "videodanmublockwkwkwords.creatkwkworid_pie_v1":
        res = get_pie_v1(
            "select creatkwkworid x,count(*) y from vm790_bcfe8a202787453d.videodanmublockwkwkwords group by creatkwkworid",
            "创建者ID关联字段指向用户的ID",
        )
    if obj.get("optype") == "videodanmublockwkwkwords.creatkwkworid_pie_v2":
        res = get_pie_v2(
            "select creatkwkworid x,count(*) y from vm790_bcfe8a202787453d.videodanmublockwkwkwords group by creatkwkworid",
            "创建者ID关联字段指向用户的ID",
        )
    if obj.get("optype") == "videodanmublockwkwkwords.creatkwkworid_line":
        res = get_line(
            "select creatkwkworid x,count(*) y from vm790_bcfe8a202787453d.videodanmublockwkwkwords group by creatkwkworid",
            "创建者ID关联字段指向用户的ID",
        )
    if obj.get("optype") == "videodanmublockwkwkwords.creatkwkworid_bar":
        res = get_bar(
            "select creatkwkworid x,count(*) y from vm790_bcfe8a202787453d.videodanmublockwkwkwords group by creatkwkworid",
            "创建者ID关联字段指向用户的ID",
        )
    if obj.get("optype") == "videodanmublockwkwkwords.creatkwkworid_bar_v1":
        res = get_bar_v1(
            "select creatkwkworid x,count(*) y from vm790_bcfe8a202787453d.videodanmublockwkwkwords group by creatkwkworid",
            "创建者ID关联字段指向用户的ID",
        )
    if obj.get("optype") == "videodanmublockwkwkwords.createtime_line":
        res = get_line(
            "select createtime x,count(*) y from vm790_bcfe8a202787453d.videodanmublockwkwkwords group by createtime order by x",
            "创建时间",
        )
    if obj.get("optype") == "videodanmublockwkwkwords.updatetime_line":
        res = get_line(
            "select updatetime x,count(*) y from vm790_bcfe8a202787453d.videodanmublockwkwkwords group by updatetime order by x",
            "更新时间",
        )
    # videodanmublockwkwkwords(视频弹幕屏蔽词表)->kwkwisactive(是否激活用于控制屏蔽词是否生效)

    if obj.get("optype") == "videodanmublockwkwkwords.kwkwisactive_pie":
        res = get_pie(
            "select kwkwisactive x,count(*) y from vm790_bcfe8a202787453d.videodanmublockwkwkwords group by kwkwisactive order by x desc",
            "是否激活用于控制屏蔽词是否生效",
        )
    if obj.get("optype") == "videodanmublockwkwkwords.kwkwisactive_pie_v1":
        res = get_pie_v1(
            "select kwkwisactive x,count(*) y from vm790_bcfe8a202787453d.videodanmublockwkwkwords group by kwkwisactive",
            "是否激活用于控制屏蔽词是否生效",
        )
    if obj.get("optype") == "videodanmublockwkwkwords.kwkwisactive_pie_v2":
        res = get_pie_v2(
            "select kwkwisactive x,count(*) y from vm790_bcfe8a202787453d.videodanmublockwkwkwords group by kwkwisactive",
            "是否激活用于控制屏蔽词是否生效",
        )
    if obj.get("optype") == "videodanmublockwkwkwords.kwkwisactive_line":
        res = get_line(
            "select kwkwisactive x,count(*) y from vm790_bcfe8a202787453d.videodanmublockwkwkwords group by kwkwisactive",
            "是否激活用于控制屏蔽词是否生效",
        )
    if obj.get("optype") == "videodanmublockwkwkwords.kwkwisactive_bar":
        res = get_bar(
            "select kwkwisactive x,count(*) y from vm790_bcfe8a202787453d.videodanmublockwkwkwords group by kwkwisactive",
            "是否激活用于控制屏蔽词是否生效",
        )
    if obj.get("optype") == "videodanmublockwkwkwords.kwkwisactive_bar_v1":
        res = get_bar_v1(
            "select kwkwisactive x,count(*) y from vm790_bcfe8a202787453d.videodanmublockwkwkwords group by kwkwisactive",
            "是否激活用于控制屏蔽词是否生效",
        )
    # videodanmublockwkwkwords(视频弹幕屏蔽词表)->blocktype(屏蔽类型如关键词、正则达式等)

    if obj.get("optype") == "videodanmublockwkwkwords.blocktype_pie":
        res = get_pie(
            "select blocktype x,count(*) y from vm790_bcfe8a202787453d.videodanmublockwkwkwords group by blocktype order by x desc",
            "屏蔽类型如关键词、正则达式等",
        )
    if obj.get("optype") == "videodanmublockwkwkwords.blocktype_pie_v1":
        res = get_pie_v1(
            "select blocktype x,count(*) y from vm790_bcfe8a202787453d.videodanmublockwkwkwords group by blocktype",
            "屏蔽类型如关键词、正则达式等",
        )
    if obj.get("optype") == "videodanmublockwkwkwords.blocktype_pie_v2":
        res = get_pie_v2(
            "select blocktype x,count(*) y from vm790_bcfe8a202787453d.videodanmublockwkwkwords group by blocktype",
            "屏蔽类型如关键词、正则达式等",
        )
    if obj.get("optype") == "videodanmublockwkwkwords.blocktype_line":
        res = get_line(
            "select blocktype x,count(*) y from vm790_bcfe8a202787453d.videodanmublockwkwkwords group by blocktype",
            "屏蔽类型如关键词、正则达式等",
        )
    if obj.get("optype") == "videodanmublockwkwkwords.blocktype_bar":
        res = get_bar(
            "select blocktype x,count(*) y from vm790_bcfe8a202787453d.videodanmublockwkwkwords group by blocktype",
            "屏蔽类型如关键词、正则达式等",
        )
    if obj.get("optype") == "videodanmublockwkwkwords.blocktype_bar_v1":
        res = get_bar_v1(
            "select blocktype x,count(*) y from vm790_bcfe8a202787453d.videodanmublockwkwkwords group by blocktype",
            "屏蔽类型如关键词、正则达式等",
        )
    if obj.get("optype") == "videodanmublockwkwkwords.description_wordcloud":
        textlist = get_data(
            "SELECT description result FROM vm790_bcfe8a202787453d.videodanmublockwkwkwords;"
        )
        res = {
            "title": "词云图",
            "imgbs64": generate_wordcloud_base64(
                ",".join([t["result"] for t in textlist])
            ),
        }
    # videomultilkwkwingualsubtitles(视频多语言字幕表)->videoid(关联视频ID)

    if obj.get("optype") == "videomultilkwkwingualsubtitles.videoid_pie":
        res = get_pie(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videomultilkwkwingualsubtitles group by videoid order by x desc",
            "关联视频ID",
        )
    if obj.get("optype") == "videomultilkwkwingualsubtitles.videoid_pie_v1":
        res = get_pie_v1(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videomultilkwkwingualsubtitles group by videoid",
            "关联视频ID",
        )
    if obj.get("optype") == "videomultilkwkwingualsubtitles.videoid_pie_v2":
        res = get_pie_v2(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videomultilkwkwingualsubtitles group by videoid",
            "关联视频ID",
        )
    if obj.get("optype") == "videomultilkwkwingualsubtitles.videoid_line":
        res = get_line(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videomultilkwkwingualsubtitles group by videoid",
            "关联视频ID",
        )
    if obj.get("optype") == "videomultilkwkwingualsubtitles.videoid_bar":
        res = get_bar(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videomultilkwkwingualsubtitles group by videoid",
            "关联视频ID",
        )
    if obj.get("optype") == "videomultilkwkwingualsubtitles.videoid_bar_v1":
        res = get_bar_v1(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videomultilkwkwingualsubtitles group by videoid",
            "关联视频ID",
        )
    # videomultilkwkwingualsubtitles(视频多语言字幕表)->languagecode(语言代码)

    if obj.get("optype") == "videomultilkwkwingualsubtitles.languagecode_pie":
        res = get_pie(
            "select languagecode x,count(*) y from vm790_bcfe8a202787453d.videomultilkwkwingualsubtitles group by languagecode order by x desc",
            "语言代码",
        )
    if obj.get("optype") == "videomultilkwkwingualsubtitles.languagecode_pie_v1":
        res = get_pie_v1(
            "select languagecode x,count(*) y from vm790_bcfe8a202787453d.videomultilkwkwingualsubtitles group by languagecode",
            "语言代码",
        )
    if obj.get("optype") == "videomultilkwkwingualsubtitles.languagecode_pie_v2":
        res = get_pie_v2(
            "select languagecode x,count(*) y from vm790_bcfe8a202787453d.videomultilkwkwingualsubtitles group by languagecode",
            "语言代码",
        )
    if obj.get("optype") == "videomultilkwkwingualsubtitles.languagecode_line":
        res = get_line(
            "select languagecode x,count(*) y from vm790_bcfe8a202787453d.videomultilkwkwingualsubtitles group by languagecode",
            "语言代码",
        )
    if obj.get("optype") == "videomultilkwkwingualsubtitles.languagecode_bar":
        res = get_bar(
            "select languagecode x,count(*) y from vm790_bcfe8a202787453d.videomultilkwkwingualsubtitles group by languagecode",
            "语言代码",
        )
    if obj.get("optype") == "videomultilkwkwingualsubtitles.languagecode_bar_v1":
        res = get_bar_v1(
            "select languagecode x,count(*) y from vm790_bcfe8a202787453d.videomultilkwkwingualsubtitles group by languagecode",
            "语言代码",
        )
    if obj.get("optype") == "videomultilkwkwingualsubtitles.subtitletext_wordcloud":
        textlist = get_data(
            "SELECT subtitletext result FROM vm790_bcfe8a202787453d.videomultilkwkwingualsubtitles;"
        )
        res = {
            "title": "词云图",
            "imgbs64": generate_wordcloud_base64(
                ",".join([t["result"] for t in textlist])
            ),
        }
    if obj.get("optype") == "videomultilkwkwingualsubtitles.starttime_line":
        res = get_line(
            "select starttime x,count(*) y from vm790_bcfe8a202787453d.videomultilkwkwingualsubtitles group by starttime order by x",
            "开始时间字幕出现时间",
        )
    if obj.get("optype") == "videomultilkwkwingualsubtitles.endtime_line":
        res = get_line(
            "select endtime x,count(*) y from vm790_bcfe8a202787453d.videomultilkwkwingualsubtitles group by endtime order by x",
            "结束时间字幕消失时间",
        )
    if obj.get("optype") == "videomultilkwkwingualsubtitles.createdat_line":
        res = get_line(
            "select createdat x,count(*) y from vm790_bcfe8a202787453d.videomultilkwkwingualsubtitles group by createdat order by x",
            "创建时间",
        )
    if obj.get("optype") == "videomultilkwkwingualsubtitles.updatedat_line":
        res = get_line(
            "select updatedat x,count(*) y from vm790_bcfe8a202787453d.videomultilkwkwingualsubtitles group by updatedat order by x",
            "更新时间",
        )
    # videomultilkwkwingualsubtitles(视频多语言字幕表)->kwkwisactive(是否激活用于控制字幕是否显示在视频中)

    if obj.get("optype") == "videomultilkwkwingualsubtitles.kwkwisactive_pie":
        res = get_pie(
            "select kwkwisactive x,count(*) y from vm790_bcfe8a202787453d.videomultilkwkwingualsubtitles group by kwkwisactive order by x desc",
            "是否激活用于控制字幕是否显示在视频中",
        )
    if obj.get("optype") == "videomultilkwkwingualsubtitles.kwkwisactive_pie_v1":
        res = get_pie_v1(
            "select kwkwisactive x,count(*) y from vm790_bcfe8a202787453d.videomultilkwkwingualsubtitles group by kwkwisactive",
            "是否激活用于控制字幕是否显示在视频中",
        )
    if obj.get("optype") == "videomultilkwkwingualsubtitles.kwkwisactive_pie_v2":
        res = get_pie_v2(
            "select kwkwisactive x,count(*) y from vm790_bcfe8a202787453d.videomultilkwkwingualsubtitles group by kwkwisactive",
            "是否激活用于控制字幕是否显示在视频中",
        )
    if obj.get("optype") == "videomultilkwkwingualsubtitles.kwkwisactive_line":
        res = get_line(
            "select kwkwisactive x,count(*) y from vm790_bcfe8a202787453d.videomultilkwkwingualsubtitles group by kwkwisactive",
            "是否激活用于控制字幕是否显示在视频中",
        )
    if obj.get("optype") == "videomultilkwkwingualsubtitles.kwkwisactive_bar":
        res = get_bar(
            "select kwkwisactive x,count(*) y from vm790_bcfe8a202787453d.videomultilkwkwingualsubtitles group by kwkwisactive",
            "是否激活用于控制字幕是否显示在视频中",
        )
    if obj.get("optype") == "videomultilkwkwingualsubtitles.kwkwisactive_bar_v1":
        res = get_bar_v1(
            "select kwkwisactive x,count(*) y from vm790_bcfe8a202787453d.videomultilkwkwingualsubtitles group by kwkwisactive",
            "是否激活用于控制字幕是否显示在视频中",
        )
    # videomultilkwkwingualsubtitles(视频多语言字幕表)->userid(创建者用户ID关联到用户示谁添加了这条字幕)

    if obj.get("optype") == "videomultilkwkwingualsubtitles.userid_pie":
        res = get_pie(
            "select userid x,count(*) y from vm790_bcfe8a202787453d.videomultilkwkwingualsubtitles group by userid order by x desc",
            "创建者用户ID关联到用户示谁添加了这条字幕",
        )
    if obj.get("optype") == "videomultilkwkwingualsubtitles.userid_pie_v1":
        res = get_pie_v1(
            "select userid x,count(*) y from vm790_bcfe8a202787453d.videomultilkwkwingualsubtitles group by userid",
            "创建者用户ID关联到用户示谁添加了这条字幕",
        )
    if obj.get("optype") == "videomultilkwkwingualsubtitles.userid_pie_v2":
        res = get_pie_v2(
            "select userid x,count(*) y from vm790_bcfe8a202787453d.videomultilkwkwingualsubtitles group by userid",
            "创建者用户ID关联到用户示谁添加了这条字幕",
        )
    if obj.get("optype") == "videomultilkwkwingualsubtitles.userid_line":
        res = get_line(
            "select userid x,count(*) y from vm790_bcfe8a202787453d.videomultilkwkwingualsubtitles group by userid",
            "创建者用户ID关联到用户示谁添加了这条字幕",
        )
    if obj.get("optype") == "videomultilkwkwingualsubtitles.userid_bar":
        res = get_bar(
            "select userid x,count(*) y from vm790_bcfe8a202787453d.videomultilkwkwingualsubtitles group by userid",
            "创建者用户ID关联到用户示谁添加了这条字幕",
        )
    if obj.get("optype") == "videomultilkwkwingualsubtitles.userid_bar_v1":
        res = get_bar_v1(
            "select userid x,count(*) y from vm790_bcfe8a202787453d.videomultilkwkwingualsubtitles group by userid",
            "创建者用户ID关联到用户示谁添加了这条字幕",
        )
    # videotranscodkwkwingtkwkwask(视频转码任务表)->tkwkwaskid(任务ID)

    if obj.get("optype") == "videotranscodkwkwingtkwkwask.tkwkwaskid_pie":
        res = get_pie(
            "select tkwkwaskid x,count(*) y from vm790_bcfe8a202787453d.videotranscodkwkwingtkwkwask group by tkwkwaskid order by x desc",
            "任务ID",
        )
    if obj.get("optype") == "videotranscodkwkwingtkwkwask.tkwkwaskid_pie_v1":
        res = get_pie_v1(
            "select tkwkwaskid x,count(*) y from vm790_bcfe8a202787453d.videotranscodkwkwingtkwkwask group by tkwkwaskid",
            "任务ID",
        )
    if obj.get("optype") == "videotranscodkwkwingtkwkwask.tkwkwaskid_pie_v2":
        res = get_pie_v2(
            "select tkwkwaskid x,count(*) y from vm790_bcfe8a202787453d.videotranscodkwkwingtkwkwask group by tkwkwaskid",
            "任务ID",
        )
    if obj.get("optype") == "videotranscodkwkwingtkwkwask.tkwkwaskid_line":
        res = get_line(
            "select tkwkwaskid x,count(*) y from vm790_bcfe8a202787453d.videotranscodkwkwingtkwkwask group by tkwkwaskid",
            "任务ID",
        )
    if obj.get("optype") == "videotranscodkwkwingtkwkwask.tkwkwaskid_bar":
        res = get_bar(
            "select tkwkwaskid x,count(*) y from vm790_bcfe8a202787453d.videotranscodkwkwingtkwkwask group by tkwkwaskid",
            "任务ID",
        )
    if obj.get("optype") == "videotranscodkwkwingtkwkwask.tkwkwaskid_bar_v1":
        res = get_bar_v1(
            "select tkwkwaskid x,count(*) y from vm790_bcfe8a202787453d.videotranscodkwkwingtkwkwask group by tkwkwaskid",
            "任务ID",
        )
    # videotranscodkwkwingtkwkwask(视频转码任务表)->videoid(关联视频ID)

    if obj.get("optype") == "videotranscodkwkwingtkwkwask.videoid_pie":
        res = get_pie(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videotranscodkwkwingtkwkwask group by videoid order by x desc",
            "关联视频ID",
        )
    if obj.get("optype") == "videotranscodkwkwingtkwkwask.videoid_pie_v1":
        res = get_pie_v1(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videotranscodkwkwingtkwkwask group by videoid",
            "关联视频ID",
        )
    if obj.get("optype") == "videotranscodkwkwingtkwkwask.videoid_pie_v2":
        res = get_pie_v2(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videotranscodkwkwingtkwkwask group by videoid",
            "关联视频ID",
        )
    if obj.get("optype") == "videotranscodkwkwingtkwkwask.videoid_line":
        res = get_line(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videotranscodkwkwingtkwkwask group by videoid",
            "关联视频ID",
        )
    if obj.get("optype") == "videotranscodkwkwingtkwkwask.videoid_bar":
        res = get_bar(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videotranscodkwkwingtkwkwask group by videoid",
            "关联视频ID",
        )
    if obj.get("optype") == "videotranscodkwkwingtkwkwask.videoid_bar_v1":
        res = get_bar_v1(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videotranscodkwkwingtkwkwask group by videoid",
            "关联视频ID",
        )
    # videotranscodkwkwingtkwkwask(视频转码任务表)->sourcepath(源视频路径)

    if obj.get("optype") == "videotranscodkwkwingtkwkwask.sourcepath_pie":
        res = get_pie(
            "select sourcepath x,count(*) y from vm790_bcfe8a202787453d.videotranscodkwkwingtkwkwask group by sourcepath order by x desc",
            "源视频路径",
        )
    if obj.get("optype") == "videotranscodkwkwingtkwkwask.sourcepath_pie_v1":
        res = get_pie_v1(
            "select sourcepath x,count(*) y from vm790_bcfe8a202787453d.videotranscodkwkwingtkwkwask group by sourcepath",
            "源视频路径",
        )
    if obj.get("optype") == "videotranscodkwkwingtkwkwask.sourcepath_pie_v2":
        res = get_pie_v2(
            "select sourcepath x,count(*) y from vm790_bcfe8a202787453d.videotranscodkwkwingtkwkwask group by sourcepath",
            "源视频路径",
        )
    if obj.get("optype") == "videotranscodkwkwingtkwkwask.sourcepath_line":
        res = get_line(
            "select sourcepath x,count(*) y from vm790_bcfe8a202787453d.videotranscodkwkwingtkwkwask group by sourcepath",
            "源视频路径",
        )
    if obj.get("optype") == "videotranscodkwkwingtkwkwask.sourcepath_bar":
        res = get_bar(
            "select sourcepath x,count(*) y from vm790_bcfe8a202787453d.videotranscodkwkwingtkwkwask group by sourcepath",
            "源视频路径",
        )
    if obj.get("optype") == "videotranscodkwkwingtkwkwask.sourcepath_bar_v1":
        res = get_bar_v1(
            "select sourcepath x,count(*) y from vm790_bcfe8a202787453d.videotranscodkwkwingtkwkwask group by sourcepath",
            "源视频路径",
        )
    # videotranscodkwkwingtkwkwask(视频转码任务表)->targetkwkwfkwkwormat(目标格式)

    if obj.get("optype") == "videotranscodkwkwingtkwkwask.targetkwkwfkwkwormat_pie":
        res = get_pie(
            "select targetkwkwfkwkwormat x,count(*) y from vm790_bcfe8a202787453d.videotranscodkwkwingtkwkwask group by targetkwkwfkwkwormat order by x desc",
            "目标格式",
        )
    if obj.get("optype") == "videotranscodkwkwingtkwkwask.targetkwkwfkwkwormat_pie_v1":
        res = get_pie_v1(
            "select targetkwkwfkwkwormat x,count(*) y from vm790_bcfe8a202787453d.videotranscodkwkwingtkwkwask group by targetkwkwfkwkwormat",
            "目标格式",
        )
    if obj.get("optype") == "videotranscodkwkwingtkwkwask.targetkwkwfkwkwormat_pie_v2":
        res = get_pie_v2(
            "select targetkwkwfkwkwormat x,count(*) y from vm790_bcfe8a202787453d.videotranscodkwkwingtkwkwask group by targetkwkwfkwkwormat",
            "目标格式",
        )
    if obj.get("optype") == "videotranscodkwkwingtkwkwask.targetkwkwfkwkwormat_line":
        res = get_line(
            "select targetkwkwfkwkwormat x,count(*) y from vm790_bcfe8a202787453d.videotranscodkwkwingtkwkwask group by targetkwkwfkwkwormat",
            "目标格式",
        )
    if obj.get("optype") == "videotranscodkwkwingtkwkwask.targetkwkwfkwkwormat_bar":
        res = get_bar(
            "select targetkwkwfkwkwormat x,count(*) y from vm790_bcfe8a202787453d.videotranscodkwkwingtkwkwask group by targetkwkwfkwkwormat",
            "目标格式",
        )
    if obj.get("optype") == "videotranscodkwkwingtkwkwask.targetkwkwfkwkwormat_bar_v1":
        res = get_bar_v1(
            "select targetkwkwfkwkwormat x,count(*) y from vm790_bcfe8a202787453d.videotranscodkwkwingtkwkwask group by targetkwkwfkwkwormat",
            "目标格式",
        )
    # videotranscodkwkwingtkwkwask(视频转码任务表)->status(任务状态)

    if obj.get("optype") == "videotranscodkwkwingtkwkwask.status_pie":
        res = get_pie(
            "select status x,count(*) y from vm790_bcfe8a202787453d.videotranscodkwkwingtkwkwask group by status order by x desc",
            "任务状态",
        )
    if obj.get("optype") == "videotranscodkwkwingtkwkwask.status_pie_v1":
        res = get_pie_v1(
            "select status x,count(*) y from vm790_bcfe8a202787453d.videotranscodkwkwingtkwkwask group by status",
            "任务状态",
        )
    if obj.get("optype") == "videotranscodkwkwingtkwkwask.status_pie_v2":
        res = get_pie_v2(
            "select status x,count(*) y from vm790_bcfe8a202787453d.videotranscodkwkwingtkwkwask group by status",
            "任务状态",
        )
    if obj.get("optype") == "videotranscodkwkwingtkwkwask.status_line":
        res = get_line(
            "select status x,count(*) y from vm790_bcfe8a202787453d.videotranscodkwkwingtkwkwask group by status",
            "任务状态",
        )
    if obj.get("optype") == "videotranscodkwkwingtkwkwask.status_bar":
        res = get_bar(
            "select status x,count(*) y from vm790_bcfe8a202787453d.videotranscodkwkwingtkwkwask group by status",
            "任务状态",
        )
    if obj.get("optype") == "videotranscodkwkwingtkwkwask.status_bar_v1":
        res = get_bar_v1(
            "select status x,count(*) y from vm790_bcfe8a202787453d.videotranscodkwkwingtkwkwask group by status",
            "任务状态",
        )
    # videotranscodkwkwingtkwkwask(视频转码任务表)->progress(任务进度)

    if obj.get("optype") == "videotranscodkwkwingtkwkwask.progress_pie":
        res = get_pie(
            "select progress x,count(*) y from vm790_bcfe8a202787453d.videotranscodkwkwingtkwkwask group by progress order by x desc",
            "任务进度",
        )
    if obj.get("optype") == "videotranscodkwkwingtkwkwask.progress_pie_v1":
        res = get_pie_v1(
            "select progress x,count(*) y from vm790_bcfe8a202787453d.videotranscodkwkwingtkwkwask group by progress",
            "任务进度",
        )
    if obj.get("optype") == "videotranscodkwkwingtkwkwask.progress_pie_v2":
        res = get_pie_v2(
            "select progress x,count(*) y from vm790_bcfe8a202787453d.videotranscodkwkwingtkwkwask group by progress",
            "任务进度",
        )
    if obj.get("optype") == "videotranscodkwkwingtkwkwask.progress_line":
        res = get_line(
            "select progress x,count(*) y from vm790_bcfe8a202787453d.videotranscodkwkwingtkwkwask group by progress",
            "任务进度",
        )
    if obj.get("optype") == "videotranscodkwkwingtkwkwask.progress_bar":
        res = get_bar(
            "select progress x,count(*) y from vm790_bcfe8a202787453d.videotranscodkwkwingtkwkwask group by progress",
            "任务进度",
        )
    if obj.get("optype") == "videotranscodkwkwingtkwkwask.progress_bar_v1":
        res = get_bar_v1(
            "select progress x,count(*) y from vm790_bcfe8a202787453d.videotranscodkwkwingtkwkwask group by progress",
            "任务进度",
        )
    if obj.get("optype") == "videotranscodkwkwingtkwkwask.createdat_line":
        res = get_line(
            "select createdat x,count(*) y from vm790_bcfe8a202787453d.videotranscodkwkwingtkwkwask group by createdat order by x",
            "创建时间",
        )
    if obj.get("optype") == "videotranscodkwkwingtkwkwask.updatedat_line":
        res = get_line(
            "select updatedat x,count(*) y from vm790_bcfe8a202787453d.videotranscodkwkwingtkwkwask group by updatedat order by x",
            "更新时间",
        )
    # videotranscodkwkwingtkwkwask(视频转码任务表)->userid(关联用户ID)

    if obj.get("optype") == "videotranscodkwkwingtkwkwask.userid_pie":
        res = get_pie(
            "select userid x,count(*) y from vm790_bcfe8a202787453d.videotranscodkwkwingtkwkwask group by userid order by x desc",
            "关联用户ID",
        )
    if obj.get("optype") == "videotranscodkwkwingtkwkwask.userid_pie_v1":
        res = get_pie_v1(
            "select userid x,count(*) y from vm790_bcfe8a202787453d.videotranscodkwkwingtkwkwask group by userid",
            "关联用户ID",
        )
    if obj.get("optype") == "videotranscodkwkwingtkwkwask.userid_pie_v2":
        res = get_pie_v2(
            "select userid x,count(*) y from vm790_bcfe8a202787453d.videotranscodkwkwingtkwkwask group by userid",
            "关联用户ID",
        )
    if obj.get("optype") == "videotranscodkwkwingtkwkwask.userid_line":
        res = get_line(
            "select userid x,count(*) y from vm790_bcfe8a202787453d.videotranscodkwkwingtkwkwask group by userid",
            "关联用户ID",
        )
    if obj.get("optype") == "videotranscodkwkwingtkwkwask.userid_bar":
        res = get_bar(
            "select userid x,count(*) y from vm790_bcfe8a202787453d.videotranscodkwkwingtkwkwask group by userid",
            "关联用户ID",
        )
    if obj.get("optype") == "videotranscodkwkwingtkwkwask.userid_bar_v1":
        res = get_bar_v1(
            "select userid x,count(*) y from vm790_bcfe8a202787453d.videotranscodkwkwingtkwkwask group by userid",
            "关联用户ID",
        )
    # videotranscodkwkwingtkwkwask(视频转码任务表)->prikwkwority(任务优先级)

    if obj.get("optype") == "videotranscodkwkwingtkwkwask.prikwkwority_pie":
        res = get_pie(
            "select prikwkwority x,count(*) y from vm790_bcfe8a202787453d.videotranscodkwkwingtkwkwask group by prikwkwority order by x desc",
            "任务优先级",
        )
    if obj.get("optype") == "videotranscodkwkwingtkwkwask.prikwkwority_pie_v1":
        res = get_pie_v1(
            "select prikwkwority x,count(*) y from vm790_bcfe8a202787453d.videotranscodkwkwingtkwkwask group by prikwkwority",
            "任务优先级",
        )
    if obj.get("optype") == "videotranscodkwkwingtkwkwask.prikwkwority_pie_v2":
        res = get_pie_v2(
            "select prikwkwority x,count(*) y from vm790_bcfe8a202787453d.videotranscodkwkwingtkwkwask group by prikwkwority",
            "任务优先级",
        )
    if obj.get("optype") == "videotranscodkwkwingtkwkwask.prikwkwority_line":
        res = get_line(
            "select prikwkwority x,count(*) y from vm790_bcfe8a202787453d.videotranscodkwkwingtkwkwask group by prikwkwority",
            "任务优先级",
        )
    if obj.get("optype") == "videotranscodkwkwingtkwkwask.prikwkwority_bar":
        res = get_bar(
            "select prikwkwority x,count(*) y from vm790_bcfe8a202787453d.videotranscodkwkwingtkwkwask group by prikwkwority",
            "任务优先级",
        )
    if obj.get("optype") == "videotranscodkwkwingtkwkwask.prikwkwority_bar_v1":
        res = get_bar_v1(
            "select prikwkwority x,count(*) y from vm790_bcfe8a202787453d.videotranscodkwkwingtkwkwask group by prikwkwority",
            "任务优先级",
        )
    # videoanalyskwkwismetrics(视频分析指标表)->videoid(视频ID关联视频)

    if obj.get("optype") == "videoanalyskwkwismetrics.videoid_pie":
        res = get_pie(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videoanalyskwkwismetrics group by videoid order by x desc",
            "视频ID关联视频",
        )
    if obj.get("optype") == "videoanalyskwkwismetrics.videoid_pie_v1":
        res = get_pie_v1(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videoanalyskwkwismetrics group by videoid",
            "视频ID关联视频",
        )
    if obj.get("optype") == "videoanalyskwkwismetrics.videoid_pie_v2":
        res = get_pie_v2(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videoanalyskwkwismetrics group by videoid",
            "视频ID关联视频",
        )
    if obj.get("optype") == "videoanalyskwkwismetrics.videoid_line":
        res = get_line(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videoanalyskwkwismetrics group by videoid",
            "视频ID关联视频",
        )
    if obj.get("optype") == "videoanalyskwkwismetrics.videoid_bar":
        res = get_bar(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videoanalyskwkwismetrics group by videoid",
            "视频ID关联视频",
        )
    if obj.get("optype") == "videoanalyskwkwismetrics.videoid_bar_v1":
        res = get_bar_v1(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videoanalyskwkwismetrics group by videoid",
            "视频ID关联视频",
        )
    if obj.get("optype") == "videoanalyskwkwismetrics.analyskwkwistime_line":
        res = get_line(
            "select analyskwkwistime x,count(*) y from vm790_bcfe8a202787453d.videoanalyskwkwismetrics group by analyskwkwistime order by x",
            "分析时间",
        )
    # videoanalyskwkwismetrics(视频分析指标表)->viewcount(观看次数)

    if obj.get("optype") == "videoanalyskwkwismetrics.viewcount_pie":
        res = get_pie(
            "select viewcount x,count(*) y from vm790_bcfe8a202787453d.videoanalyskwkwismetrics group by viewcount order by x desc",
            "观看次数",
        )
    if obj.get("optype") == "videoanalyskwkwismetrics.viewcount_pie_v1":
        res = get_pie_v1(
            "select viewcount x,count(*) y from vm790_bcfe8a202787453d.videoanalyskwkwismetrics group by viewcount",
            "观看次数",
        )
    if obj.get("optype") == "videoanalyskwkwismetrics.viewcount_pie_v2":
        res = get_pie_v2(
            "select viewcount x,count(*) y from vm790_bcfe8a202787453d.videoanalyskwkwismetrics group by viewcount",
            "观看次数",
        )
    if obj.get("optype") == "videoanalyskwkwismetrics.viewcount_line":
        res = get_line(
            "select viewcount x,count(*) y from vm790_bcfe8a202787453d.videoanalyskwkwismetrics group by viewcount",
            "观看次数",
        )
    if obj.get("optype") == "videoanalyskwkwismetrics.viewcount_bar":
        res = get_bar(
            "select viewcount x,count(*) y from vm790_bcfe8a202787453d.videoanalyskwkwismetrics group by viewcount",
            "观看次数",
        )
    if obj.get("optype") == "videoanalyskwkwismetrics.viewcount_bar_v1":
        res = get_bar_v1(
            "select viewcount x,count(*) y from vm790_bcfe8a202787453d.videoanalyskwkwismetrics group by viewcount",
            "观看次数",
        )
    # videoanalyskwkwismetrics(视频分析指标表)->likecount(点赞次数)

    if obj.get("optype") == "videoanalyskwkwismetrics.likecount_pie":
        res = get_pie(
            "select likecount x,count(*) y from vm790_bcfe8a202787453d.videoanalyskwkwismetrics group by likecount order by x desc",
            "点赞次数",
        )
    if obj.get("optype") == "videoanalyskwkwismetrics.likecount_pie_v1":
        res = get_pie_v1(
            "select likecount x,count(*) y from vm790_bcfe8a202787453d.videoanalyskwkwismetrics group by likecount",
            "点赞次数",
        )
    if obj.get("optype") == "videoanalyskwkwismetrics.likecount_pie_v2":
        res = get_pie_v2(
            "select likecount x,count(*) y from vm790_bcfe8a202787453d.videoanalyskwkwismetrics group by likecount",
            "点赞次数",
        )
    if obj.get("optype") == "videoanalyskwkwismetrics.likecount_line":
        res = get_line(
            "select likecount x,count(*) y from vm790_bcfe8a202787453d.videoanalyskwkwismetrics group by likecount",
            "点赞次数",
        )
    if obj.get("optype") == "videoanalyskwkwismetrics.likecount_bar":
        res = get_bar(
            "select likecount x,count(*) y from vm790_bcfe8a202787453d.videoanalyskwkwismetrics group by likecount",
            "点赞次数",
        )
    if obj.get("optype") == "videoanalyskwkwismetrics.likecount_bar_v1":
        res = get_bar_v1(
            "select likecount x,count(*) y from vm790_bcfe8a202787453d.videoanalyskwkwismetrics group by likecount",
            "点赞次数",
        )
    # videoanalyskwkwismetrics(视频分析指标表)->sharecount(分享次数)

    if obj.get("optype") == "videoanalyskwkwismetrics.sharecount_pie":
        res = get_pie(
            "select sharecount x,count(*) y from vm790_bcfe8a202787453d.videoanalyskwkwismetrics group by sharecount order by x desc",
            "分享次数",
        )
    if obj.get("optype") == "videoanalyskwkwismetrics.sharecount_pie_v1":
        res = get_pie_v1(
            "select sharecount x,count(*) y from vm790_bcfe8a202787453d.videoanalyskwkwismetrics group by sharecount",
            "分享次数",
        )
    if obj.get("optype") == "videoanalyskwkwismetrics.sharecount_pie_v2":
        res = get_pie_v2(
            "select sharecount x,count(*) y from vm790_bcfe8a202787453d.videoanalyskwkwismetrics group by sharecount",
            "分享次数",
        )
    if obj.get("optype") == "videoanalyskwkwismetrics.sharecount_line":
        res = get_line(
            "select sharecount x,count(*) y from vm790_bcfe8a202787453d.videoanalyskwkwismetrics group by sharecount",
            "分享次数",
        )
    if obj.get("optype") == "videoanalyskwkwismetrics.sharecount_bar":
        res = get_bar(
            "select sharecount x,count(*) y from vm790_bcfe8a202787453d.videoanalyskwkwismetrics group by sharecount",
            "分享次数",
        )
    if obj.get("optype") == "videoanalyskwkwismetrics.sharecount_bar_v1":
        res = get_bar_v1(
            "select sharecount x,count(*) y from vm790_bcfe8a202787453d.videoanalyskwkwismetrics group by sharecount",
            "分享次数",
        )
    if obj.get("optype") == "videoanalyskwkwismetrics.commentcount_wordcloud":
        textlist = get_data(
            "SELECT commentcount result FROM vm790_bcfe8a202787453d.videoanalyskwkwismetrics;"
        )
        res = {
            "title": "词云图",
            "imgbs64": generate_wordcloud_base64(
                ",".join([t["result"] for t in textlist])
            ),
        }
    # videoanalyskwkwismetrics(视频分析指标表)->bouncerate(跳出率)

    if obj.get("optype") == "videoanalyskwkwismetrics.bouncerate_pie":
        res = get_pie(
            "select bouncerate x,count(*) y from vm790_bcfe8a202787453d.videoanalyskwkwismetrics group by bouncerate order by x desc",
            "跳出率",
        )
    if obj.get("optype") == "videoanalyskwkwismetrics.bouncerate_pie_v1":
        res = get_pie_v1(
            "select bouncerate x,count(*) y from vm790_bcfe8a202787453d.videoanalyskwkwismetrics group by bouncerate",
            "跳出率",
        )
    if obj.get("optype") == "videoanalyskwkwismetrics.bouncerate_pie_v2":
        res = get_pie_v2(
            "select bouncerate x,count(*) y from vm790_bcfe8a202787453d.videoanalyskwkwismetrics group by bouncerate",
            "跳出率",
        )
    if obj.get("optype") == "videoanalyskwkwismetrics.bouncerate_line":
        res = get_line(
            "select bouncerate x,count(*) y from vm790_bcfe8a202787453d.videoanalyskwkwismetrics group by bouncerate",
            "跳出率",
        )
    if obj.get("optype") == "videoanalyskwkwismetrics.bouncerate_bar":
        res = get_bar(
            "select bouncerate x,count(*) y from vm790_bcfe8a202787453d.videoanalyskwkwismetrics group by bouncerate",
            "跳出率",
        )
    if obj.get("optype") == "videoanalyskwkwismetrics.bouncerate_bar_v1":
        res = get_bar_v1(
            "select bouncerate x,count(*) y from vm790_bcfe8a202787453d.videoanalyskwkwismetrics group by bouncerate",
            "跳出率",
        )
    # videoanalyskwkwismetrics(视频分析指标表)->averagewatchtime(平均观看时长)

    if obj.get("optype") == "videoanalyskwkwismetrics.averagewatchtime_pie":
        res = get_pie(
            "select averagewatchtime x,count(*) y from vm790_bcfe8a202787453d.videoanalyskwkwismetrics group by averagewatchtime order by x desc",
            "平均观看时长",
        )
    if obj.get("optype") == "videoanalyskwkwismetrics.averagewatchtime_pie_v1":
        res = get_pie_v1(
            "select averagewatchtime x,count(*) y from vm790_bcfe8a202787453d.videoanalyskwkwismetrics group by averagewatchtime",
            "平均观看时长",
        )
    if obj.get("optype") == "videoanalyskwkwismetrics.averagewatchtime_pie_v2":
        res = get_pie_v2(
            "select averagewatchtime x,count(*) y from vm790_bcfe8a202787453d.videoanalyskwkwismetrics group by averagewatchtime",
            "平均观看时长",
        )
    if obj.get("optype") == "videoanalyskwkwismetrics.averagewatchtime_line":
        res = get_line(
            "select averagewatchtime x,count(*) y from vm790_bcfe8a202787453d.videoanalyskwkwismetrics group by averagewatchtime",
            "平均观看时长",
        )
    if obj.get("optype") == "videoanalyskwkwismetrics.averagewatchtime_bar":
        res = get_bar(
            "select averagewatchtime x,count(*) y from vm790_bcfe8a202787453d.videoanalyskwkwismetrics group by averagewatchtime",
            "平均观看时长",
        )
    if obj.get("optype") == "videoanalyskwkwismetrics.averagewatchtime_bar_v1":
        res = get_bar_v1(
            "select averagewatchtime x,count(*) y from vm790_bcfe8a202787453d.videoanalyskwkwismetrics group by averagewatchtime",
            "平均观看时长",
        )
    # videoanalyskwkwismetrics(视频分析指标表)->engagementrate(互动率)

    if obj.get("optype") == "videoanalyskwkwismetrics.engagementrate_pie":
        res = get_pie(
            "select engagementrate x,count(*) y from vm790_bcfe8a202787453d.videoanalyskwkwismetrics group by engagementrate order by x desc",
            "互动率",
        )
    if obj.get("optype") == "videoanalyskwkwismetrics.engagementrate_pie_v1":
        res = get_pie_v1(
            "select engagementrate x,count(*) y from vm790_bcfe8a202787453d.videoanalyskwkwismetrics group by engagementrate",
            "互动率",
        )
    if obj.get("optype") == "videoanalyskwkwismetrics.engagementrate_pie_v2":
        res = get_pie_v2(
            "select engagementrate x,count(*) y from vm790_bcfe8a202787453d.videoanalyskwkwismetrics group by engagementrate",
            "互动率",
        )
    if obj.get("optype") == "videoanalyskwkwismetrics.engagementrate_line":
        res = get_line(
            "select engagementrate x,count(*) y from vm790_bcfe8a202787453d.videoanalyskwkwismetrics group by engagementrate",
            "互动率",
        )
    if obj.get("optype") == "videoanalyskwkwismetrics.engagementrate_bar":
        res = get_bar(
            "select engagementrate x,count(*) y from vm790_bcfe8a202787453d.videoanalyskwkwismetrics group by engagementrate",
            "互动率",
        )
    if obj.get("optype") == "videoanalyskwkwismetrics.engagementrate_bar_v1":
        res = get_bar_v1(
            "select engagementrate x,count(*) y from vm790_bcfe8a202787453d.videoanalyskwkwismetrics group by engagementrate",
            "互动率",
        )
    # videoqualityassessment(视频质量评估表)->videoid(关联视频ID)

    if obj.get("optype") == "videoqualityassessment.videoid_pie":
        res = get_pie(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videoqualityassessment group by videoid order by x desc",
            "关联视频ID",
        )
    if obj.get("optype") == "videoqualityassessment.videoid_pie_v1":
        res = get_pie_v1(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videoqualityassessment group by videoid",
            "关联视频ID",
        )
    if obj.get("optype") == "videoqualityassessment.videoid_pie_v2":
        res = get_pie_v2(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videoqualityassessment group by videoid",
            "关联视频ID",
        )
    if obj.get("optype") == "videoqualityassessment.videoid_line":
        res = get_line(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videoqualityassessment group by videoid",
            "关联视频ID",
        )
    if obj.get("optype") == "videoqualityassessment.videoid_bar":
        res = get_bar(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videoqualityassessment group by videoid",
            "关联视频ID",
        )
    if obj.get("optype") == "videoqualityassessment.videoid_bar_v1":
        res = get_bar_v1(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videoqualityassessment group by videoid",
            "关联视频ID",
        )
    # videoqualityassessment(视频质量评估表)->qualitysckwkwore(质量评分)

    if obj.get("optype") == "videoqualityassessment.qualitysckwkwore_pie":
        res = get_pie(
            "select qualitysckwkwore x,count(*) y from vm790_bcfe8a202787453d.videoqualityassessment group by qualitysckwkwore order by x desc",
            "质量评分",
        )
    if obj.get("optype") == "videoqualityassessment.qualitysckwkwore_pie_v1":
        res = get_pie_v1(
            "select qualitysckwkwore x,count(*) y from vm790_bcfe8a202787453d.videoqualityassessment group by qualitysckwkwore",
            "质量评分",
        )
    if obj.get("optype") == "videoqualityassessment.qualitysckwkwore_pie_v2":
        res = get_pie_v2(
            "select qualitysckwkwore x,count(*) y from vm790_bcfe8a202787453d.videoqualityassessment group by qualitysckwkwore",
            "质量评分",
        )
    if obj.get("optype") == "videoqualityassessment.qualitysckwkwore_line":
        res = get_line(
            "select qualitysckwkwore x,count(*) y from vm790_bcfe8a202787453d.videoqualityassessment group by qualitysckwkwore",
            "质量评分",
        )
    if obj.get("optype") == "videoqualityassessment.qualitysckwkwore_bar":
        res = get_bar(
            "select qualitysckwkwore x,count(*) y from vm790_bcfe8a202787453d.videoqualityassessment group by qualitysckwkwore",
            "质量评分",
        )
    if obj.get("optype") == "videoqualityassessment.qualitysckwkwore_bar_v1":
        res = get_bar_v1(
            "select qualitysckwkwore x,count(*) y from vm790_bcfe8a202787453d.videoqualityassessment group by qualitysckwkwore",
            "质量评分",
        )
    if obj.get("optype") == "videoqualityassessment.kwkwassessmenttime_line":
        res = get_line(
            "select kwkwassessmenttime x,count(*) y from vm790_bcfe8a202787453d.videoqualityassessment group by kwkwassessmenttime order by x",
            "评估时间",
        )
    # videoqualityassessment(视频质量评估表)->reviewerid(关联评审员ID)

    if obj.get("optype") == "videoqualityassessment.reviewerid_pie":
        res = get_pie(
            "select reviewerid x,count(*) y from vm790_bcfe8a202787453d.videoqualityassessment group by reviewerid order by x desc",
            "关联评审员ID",
        )
    if obj.get("optype") == "videoqualityassessment.reviewerid_pie_v1":
        res = get_pie_v1(
            "select reviewerid x,count(*) y from vm790_bcfe8a202787453d.videoqualityassessment group by reviewerid",
            "关联评审员ID",
        )
    if obj.get("optype") == "videoqualityassessment.reviewerid_pie_v2":
        res = get_pie_v2(
            "select reviewerid x,count(*) y from vm790_bcfe8a202787453d.videoqualityassessment group by reviewerid",
            "关联评审员ID",
        )
    if obj.get("optype") == "videoqualityassessment.reviewerid_line":
        res = get_line(
            "select reviewerid x,count(*) y from vm790_bcfe8a202787453d.videoqualityassessment group by reviewerid",
            "关联评审员ID",
        )
    if obj.get("optype") == "videoqualityassessment.reviewerid_bar":
        res = get_bar(
            "select reviewerid x,count(*) y from vm790_bcfe8a202787453d.videoqualityassessment group by reviewerid",
            "关联评审员ID",
        )
    if obj.get("optype") == "videoqualityassessment.reviewerid_bar_v1":
        res = get_bar_v1(
            "select reviewerid x,count(*) y from vm790_bcfe8a202787453d.videoqualityassessment group by reviewerid",
            "关联评审员ID",
        )
    # videoqualityassessment(视频质量评估表)->framerate(帧率)

    if obj.get("optype") == "videoqualityassessment.framerate_pie":
        res = get_pie(
            "select framerate x,count(*) y from vm790_bcfe8a202787453d.videoqualityassessment group by framerate order by x desc",
            "帧率",
        )
    if obj.get("optype") == "videoqualityassessment.framerate_pie_v1":
        res = get_pie_v1(
            "select framerate x,count(*) y from vm790_bcfe8a202787453d.videoqualityassessment group by framerate",
            "帧率",
        )
    if obj.get("optype") == "videoqualityassessment.framerate_pie_v2":
        res = get_pie_v2(
            "select framerate x,count(*) y from vm790_bcfe8a202787453d.videoqualityassessment group by framerate",
            "帧率",
        )
    if obj.get("optype") == "videoqualityassessment.framerate_line":
        res = get_line(
            "select framerate x,count(*) y from vm790_bcfe8a202787453d.videoqualityassessment group by framerate",
            "帧率",
        )
    if obj.get("optype") == "videoqualityassessment.framerate_bar":
        res = get_bar(
            "select framerate x,count(*) y from vm790_bcfe8a202787453d.videoqualityassessment group by framerate",
            "帧率",
        )
    if obj.get("optype") == "videoqualityassessment.framerate_bar_v1":
        res = get_bar_v1(
            "select framerate x,count(*) y from vm790_bcfe8a202787453d.videoqualityassessment group by framerate",
            "帧率",
        )
    # videoqualityassessment(视频质量评估表)->resolution(分辨率)

    if obj.get("optype") == "videoqualityassessment.resolution_pie":
        res = get_pie(
            "select resolution x,count(*) y from vm790_bcfe8a202787453d.videoqualityassessment group by resolution order by x desc",
            "分辨率",
        )
    if obj.get("optype") == "videoqualityassessment.resolution_pie_v1":
        res = get_pie_v1(
            "select resolution x,count(*) y from vm790_bcfe8a202787453d.videoqualityassessment group by resolution",
            "分辨率",
        )
    if obj.get("optype") == "videoqualityassessment.resolution_pie_v2":
        res = get_pie_v2(
            "select resolution x,count(*) y from vm790_bcfe8a202787453d.videoqualityassessment group by resolution",
            "分辨率",
        )
    if obj.get("optype") == "videoqualityassessment.resolution_line":
        res = get_line(
            "select resolution x,count(*) y from vm790_bcfe8a202787453d.videoqualityassessment group by resolution",
            "分辨率",
        )
    if obj.get("optype") == "videoqualityassessment.resolution_bar":
        res = get_bar(
            "select resolution x,count(*) y from vm790_bcfe8a202787453d.videoqualityassessment group by resolution",
            "分辨率",
        )
    if obj.get("optype") == "videoqualityassessment.resolution_bar_v1":
        res = get_bar_v1(
            "select resolution x,count(*) y from vm790_bcfe8a202787453d.videoqualityassessment group by resolution",
            "分辨率",
        )
    # videoqualityassessment(视频质量评估表)->bitrate(比特率)

    if obj.get("optype") == "videoqualityassessment.bitrate_pie":
        res = get_pie(
            "select bitrate x,count(*) y from vm790_bcfe8a202787453d.videoqualityassessment group by bitrate order by x desc",
            "比特率",
        )
    if obj.get("optype") == "videoqualityassessment.bitrate_pie_v1":
        res = get_pie_v1(
            "select bitrate x,count(*) y from vm790_bcfe8a202787453d.videoqualityassessment group by bitrate",
            "比特率",
        )
    if obj.get("optype") == "videoqualityassessment.bitrate_pie_v2":
        res = get_pie_v2(
            "select bitrate x,count(*) y from vm790_bcfe8a202787453d.videoqualityassessment group by bitrate",
            "比特率",
        )
    if obj.get("optype") == "videoqualityassessment.bitrate_line":
        res = get_line(
            "select bitrate x,count(*) y from vm790_bcfe8a202787453d.videoqualityassessment group by bitrate",
            "比特率",
        )
    if obj.get("optype") == "videoqualityassessment.bitrate_bar":
        res = get_bar(
            "select bitrate x,count(*) y from vm790_bcfe8a202787453d.videoqualityassessment group by bitrate",
            "比特率",
        )
    if obj.get("optype") == "videoqualityassessment.bitrate_bar_v1":
        res = get_bar_v1(
            "select bitrate x,count(*) y from vm790_bcfe8a202787453d.videoqualityassessment group by bitrate",
            "比特率",
        )
    # videoqualityassessment(视频质量评估表)->encodkwkwingkwkwfkwkwormat(编码格式)

    if obj.get("optype") == "videoqualityassessment.encodkwkwingkwkwfkwkwormat_pie":
        res = get_pie(
            "select encodkwkwingkwkwfkwkwormat x,count(*) y from vm790_bcfe8a202787453d.videoqualityassessment group by encodkwkwingkwkwfkwkwormat order by x desc",
            "编码格式",
        )
    if obj.get("optype") == "videoqualityassessment.encodkwkwingkwkwfkwkwormat_pie_v1":
        res = get_pie_v1(
            "select encodkwkwingkwkwfkwkwormat x,count(*) y from vm790_bcfe8a202787453d.videoqualityassessment group by encodkwkwingkwkwfkwkwormat",
            "编码格式",
        )
    if obj.get("optype") == "videoqualityassessment.encodkwkwingkwkwfkwkwormat_pie_v2":
        res = get_pie_v2(
            "select encodkwkwingkwkwfkwkwormat x,count(*) y from vm790_bcfe8a202787453d.videoqualityassessment group by encodkwkwingkwkwfkwkwormat",
            "编码格式",
        )
    if obj.get("optype") == "videoqualityassessment.encodkwkwingkwkwfkwkwormat_line":
        res = get_line(
            "select encodkwkwingkwkwfkwkwormat x,count(*) y from vm790_bcfe8a202787453d.videoqualityassessment group by encodkwkwingkwkwfkwkwormat",
            "编码格式",
        )
    if obj.get("optype") == "videoqualityassessment.encodkwkwingkwkwfkwkwormat_bar":
        res = get_bar(
            "select encodkwkwingkwkwfkwkwormat x,count(*) y from vm790_bcfe8a202787453d.videoqualityassessment group by encodkwkwingkwkwfkwkwormat",
            "编码格式",
        )
    if obj.get("optype") == "videoqualityassessment.encodkwkwingkwkwfkwkwormat_bar_v1":
        res = get_bar_v1(
            "select encodkwkwingkwkwfkwkwormat x,count(*) y from vm790_bcfe8a202787453d.videoqualityassessment group by encodkwkwingkwkwfkwkwormat",
            "编码格式",
        )
    # videoqualityassessment(视频质量评估表)->ckwkworruptiondetected(是否检测到损坏)

    if obj.get("optype") == "videoqualityassessment.ckwkworruptiondetected_pie":
        res = get_pie(
            "select ckwkworruptiondetected x,count(*) y from vm790_bcfe8a202787453d.videoqualityassessment group by ckwkworruptiondetected order by x desc",
            "是否检测到损坏",
        )
    if obj.get("optype") == "videoqualityassessment.ckwkworruptiondetected_pie_v1":
        res = get_pie_v1(
            "select ckwkworruptiondetected x,count(*) y from vm790_bcfe8a202787453d.videoqualityassessment group by ckwkworruptiondetected",
            "是否检测到损坏",
        )
    if obj.get("optype") == "videoqualityassessment.ckwkworruptiondetected_pie_v2":
        res = get_pie_v2(
            "select ckwkworruptiondetected x,count(*) y from vm790_bcfe8a202787453d.videoqualityassessment group by ckwkworruptiondetected",
            "是否检测到损坏",
        )
    if obj.get("optype") == "videoqualityassessment.ckwkworruptiondetected_line":
        res = get_line(
            "select ckwkworruptiondetected x,count(*) y from vm790_bcfe8a202787453d.videoqualityassessment group by ckwkworruptiondetected",
            "是否检测到损坏",
        )
    if obj.get("optype") == "videoqualityassessment.ckwkworruptiondetected_bar":
        res = get_bar(
            "select ckwkworruptiondetected x,count(*) y from vm790_bcfe8a202787453d.videoqualityassessment group by ckwkworruptiondetected",
            "是否检测到损坏",
        )
    if obj.get("optype") == "videoqualityassessment.ckwkworruptiondetected_bar_v1":
        res = get_bar_v1(
            "select ckwkworruptiondetected x,count(*) y from vm790_bcfe8a202787453d.videoqualityassessment group by ckwkworruptiondetected",
            "是否检测到损坏",
        )
    # videoqualityassessment(视频质量评估表)->relatedkwkwissueid(相关问题ID)

    if obj.get("optype") == "videoqualityassessment.relatedkwkwissueid_pie":
        res = get_pie(
            "select relatedkwkwissueid x,count(*) y from vm790_bcfe8a202787453d.videoqualityassessment group by relatedkwkwissueid order by x desc",
            "相关问题ID",
        )
    if obj.get("optype") == "videoqualityassessment.relatedkwkwissueid_pie_v1":
        res = get_pie_v1(
            "select relatedkwkwissueid x,count(*) y from vm790_bcfe8a202787453d.videoqualityassessment group by relatedkwkwissueid",
            "相关问题ID",
        )
    if obj.get("optype") == "videoqualityassessment.relatedkwkwissueid_pie_v2":
        res = get_pie_v2(
            "select relatedkwkwissueid x,count(*) y from vm790_bcfe8a202787453d.videoqualityassessment group by relatedkwkwissueid",
            "相关问题ID",
        )
    if obj.get("optype") == "videoqualityassessment.relatedkwkwissueid_line":
        res = get_line(
            "select relatedkwkwissueid x,count(*) y from vm790_bcfe8a202787453d.videoqualityassessment group by relatedkwkwissueid",
            "相关问题ID",
        )
    if obj.get("optype") == "videoqualityassessment.relatedkwkwissueid_bar":
        res = get_bar(
            "select relatedkwkwissueid x,count(*) y from vm790_bcfe8a202787453d.videoqualityassessment group by relatedkwkwissueid",
            "相关问题ID",
        )
    if obj.get("optype") == "videoqualityassessment.relatedkwkwissueid_bar_v1":
        res = get_bar_v1(
            "select relatedkwkwissueid x,count(*) y from vm790_bcfe8a202787453d.videoqualityassessment group by relatedkwkwissueid",
            "相关问题ID",
        )
    # videowatermarkinfo(视频水印信息表)->videoid(视频ID关联视频)

    if obj.get("optype") == "videowatermarkinfo.videoid_pie":
        res = get_pie(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videowatermarkinfo group by videoid order by x desc",
            "视频ID关联视频",
        )
    if obj.get("optype") == "videowatermarkinfo.videoid_pie_v1":
        res = get_pie_v1(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videowatermarkinfo group by videoid",
            "视频ID关联视频",
        )
    if obj.get("optype") == "videowatermarkinfo.videoid_pie_v2":
        res = get_pie_v2(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videowatermarkinfo group by videoid",
            "视频ID关联视频",
        )
    if obj.get("optype") == "videowatermarkinfo.videoid_line":
        res = get_line(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videowatermarkinfo group by videoid",
            "视频ID关联视频",
        )
    if obj.get("optype") == "videowatermarkinfo.videoid_bar":
        res = get_bar(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videowatermarkinfo group by videoid",
            "视频ID关联视频",
        )
    if obj.get("optype") == "videowatermarkinfo.videoid_bar_v1":
        res = get_bar_v1(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videowatermarkinfo group by videoid",
            "视频ID关联视频",
        )
    if obj.get("optype") == "videowatermarkinfo.watermarktext_wordcloud":
        textlist = get_data(
            "SELECT watermarktext result FROM vm790_bcfe8a202787453d.videowatermarkinfo;"
        )
        res = {
            "title": "词云图",
            "imgbs64": generate_wordcloud_base64(
                ",".join([t["result"] for t in textlist])
            ),
        }
    # videowatermarkinfo(视频水印信息表)->watermarkposition(水印位置如左上角、右下角等)

    if obj.get("optype") == "videowatermarkinfo.watermarkposition_pie":
        res = get_pie(
            "select watermarkposition x,count(*) y from vm790_bcfe8a202787453d.videowatermarkinfo group by watermarkposition order by x desc",
            "水印位置如左上角、右下角等",
        )
    if obj.get("optype") == "videowatermarkinfo.watermarkposition_pie_v1":
        res = get_pie_v1(
            "select watermarkposition x,count(*) y from vm790_bcfe8a202787453d.videowatermarkinfo group by watermarkposition",
            "水印位置如左上角、右下角等",
        )
    if obj.get("optype") == "videowatermarkinfo.watermarkposition_pie_v2":
        res = get_pie_v2(
            "select watermarkposition x,count(*) y from vm790_bcfe8a202787453d.videowatermarkinfo group by watermarkposition",
            "水印位置如左上角、右下角等",
        )
    if obj.get("optype") == "videowatermarkinfo.watermarkposition_line":
        res = get_line(
            "select watermarkposition x,count(*) y from vm790_bcfe8a202787453d.videowatermarkinfo group by watermarkposition",
            "水印位置如左上角、右下角等",
        )
    if obj.get("optype") == "videowatermarkinfo.watermarkposition_bar":
        res = get_bar(
            "select watermarkposition x,count(*) y from vm790_bcfe8a202787453d.videowatermarkinfo group by watermarkposition",
            "水印位置如左上角、右下角等",
        )
    if obj.get("optype") == "videowatermarkinfo.watermarkposition_bar_v1":
        res = get_bar_v1(
            "select watermarkposition x,count(*) y from vm790_bcfe8a202787453d.videowatermarkinfo group by watermarkposition",
            "水印位置如左上角、右下角等",
        )
    # videowatermarkinfo(视频水印信息表)->watermarksize(水印大小如百分比或像素值)

    if obj.get("optype") == "videowatermarkinfo.watermarksize_pie":
        res = get_pie(
            "select watermarksize x,count(*) y from vm790_bcfe8a202787453d.videowatermarkinfo group by watermarksize order by x desc",
            "水印大小如百分比或像素值",
        )
    if obj.get("optype") == "videowatermarkinfo.watermarksize_pie_v1":
        res = get_pie_v1(
            "select watermarksize x,count(*) y from vm790_bcfe8a202787453d.videowatermarkinfo group by watermarksize",
            "水印大小如百分比或像素值",
        )
    if obj.get("optype") == "videowatermarkinfo.watermarksize_pie_v2":
        res = get_pie_v2(
            "select watermarksize x,count(*) y from vm790_bcfe8a202787453d.videowatermarkinfo group by watermarksize",
            "水印大小如百分比或像素值",
        )
    if obj.get("optype") == "videowatermarkinfo.watermarksize_line":
        res = get_line(
            "select watermarksize x,count(*) y from vm790_bcfe8a202787453d.videowatermarkinfo group by watermarksize",
            "水印大小如百分比或像素值",
        )
    if obj.get("optype") == "videowatermarkinfo.watermarksize_bar":
        res = get_bar(
            "select watermarksize x,count(*) y from vm790_bcfe8a202787453d.videowatermarkinfo group by watermarksize",
            "水印大小如百分比或像素值",
        )
    if obj.get("optype") == "videowatermarkinfo.watermarksize_bar_v1":
        res = get_bar_v1(
            "select watermarksize x,count(*) y from vm790_bcfe8a202787453d.videowatermarkinfo group by watermarksize",
            "水印大小如百分比或像素值",
        )
    # videowatermarkinfo(视频水印信息表)->watermarkopacity(水印透明度0100%)

    if obj.get("optype") == "videowatermarkinfo.watermarkopacity_pie":
        res = get_pie(
            "select watermarkopacity x,count(*) y from vm790_bcfe8a202787453d.videowatermarkinfo group by watermarkopacity order by x desc",
            "水印透明度0100%",
        )
    if obj.get("optype") == "videowatermarkinfo.watermarkopacity_pie_v1":
        res = get_pie_v1(
            "select watermarkopacity x,count(*) y from vm790_bcfe8a202787453d.videowatermarkinfo group by watermarkopacity",
            "水印透明度0100%",
        )
    if obj.get("optype") == "videowatermarkinfo.watermarkopacity_pie_v2":
        res = get_pie_v2(
            "select watermarkopacity x,count(*) y from vm790_bcfe8a202787453d.videowatermarkinfo group by watermarkopacity",
            "水印透明度0100%",
        )
    if obj.get("optype") == "videowatermarkinfo.watermarkopacity_line":
        res = get_line(
            "select watermarkopacity x,count(*) y from vm790_bcfe8a202787453d.videowatermarkinfo group by watermarkopacity",
            "水印透明度0100%",
        )
    if obj.get("optype") == "videowatermarkinfo.watermarkopacity_bar":
        res = get_bar(
            "select watermarkopacity x,count(*) y from vm790_bcfe8a202787453d.videowatermarkinfo group by watermarkopacity",
            "水印透明度0100%",
        )
    if obj.get("optype") == "videowatermarkinfo.watermarkopacity_bar_v1":
        res = get_bar_v1(
            "select watermarkopacity x,count(*) y from vm790_bcfe8a202787453d.videowatermarkinfo group by watermarkopacity",
            "水印透明度0100%",
        )
    if obj.get("optype") == "videowatermarkinfo.createdat_line":
        res = get_line(
            "select createdat x,count(*) y from vm790_bcfe8a202787453d.videowatermarkinfo group by createdat order by x",
            "创建时间",
        )
    if obj.get("optype") == "videowatermarkinfo.updatedat_line":
        res = get_line(
            "select updatedat x,count(*) y from vm790_bcfe8a202787453d.videowatermarkinfo group by updatedat order by x",
            "更新时间",
        )
    # videowatermarkinfo(视频水印信息表)->kwkwisactive(是否激活用于控制水印是否生效如0为未激活1为激活)

    if obj.get("optype") == "videowatermarkinfo.kwkwisactive_pie":
        res = get_pie(
            "select kwkwisactive x,count(*) y from vm790_bcfe8a202787453d.videowatermarkinfo group by kwkwisactive order by x desc",
            "是否激活用于控制水印是否生效如0为未激活1为激活",
        )
    if obj.get("optype") == "videowatermarkinfo.kwkwisactive_pie_v1":
        res = get_pie_v1(
            "select kwkwisactive x,count(*) y from vm790_bcfe8a202787453d.videowatermarkinfo group by kwkwisactive",
            "是否激活用于控制水印是否生效如0为未激活1为激活",
        )
    if obj.get("optype") == "videowatermarkinfo.kwkwisactive_pie_v2":
        res = get_pie_v2(
            "select kwkwisactive x,count(*) y from vm790_bcfe8a202787453d.videowatermarkinfo group by kwkwisactive",
            "是否激活用于控制水印是否生效如0为未激活1为激活",
        )
    if obj.get("optype") == "videowatermarkinfo.kwkwisactive_line":
        res = get_line(
            "select kwkwisactive x,count(*) y from vm790_bcfe8a202787453d.videowatermarkinfo group by kwkwisactive",
            "是否激活用于控制水印是否生效如0为未激活1为激活",
        )
    if obj.get("optype") == "videowatermarkinfo.kwkwisactive_bar":
        res = get_bar(
            "select kwkwisactive x,count(*) y from vm790_bcfe8a202787453d.videowatermarkinfo group by kwkwisactive",
            "是否激活用于控制水印是否生效如0为未激活1为激活",
        )
    if obj.get("optype") == "videowatermarkinfo.kwkwisactive_bar_v1":
        res = get_bar_v1(
            "select kwkwisactive x,count(*) y from vm790_bcfe8a202787453d.videowatermarkinfo group by kwkwisactive",
            "是否激活用于控制水印是否生效如0为未激活1为激活",
        )
    # videocopyrightinfo(视频版权信息表)->videoid(关联视频ID)

    if obj.get("optype") == "videocopyrightinfo.videoid_pie":
        res = get_pie(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videocopyrightinfo group by videoid order by x desc",
            "关联视频ID",
        )
    if obj.get("optype") == "videocopyrightinfo.videoid_pie_v1":
        res = get_pie_v1(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videocopyrightinfo group by videoid",
            "关联视频ID",
        )
    if obj.get("optype") == "videocopyrightinfo.videoid_pie_v2":
        res = get_pie_v2(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videocopyrightinfo group by videoid",
            "关联视频ID",
        )
    if obj.get("optype") == "videocopyrightinfo.videoid_line":
        res = get_line(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videocopyrightinfo group by videoid",
            "关联视频ID",
        )
    if obj.get("optype") == "videocopyrightinfo.videoid_bar":
        res = get_bar(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videocopyrightinfo group by videoid",
            "关联视频ID",
        )
    if obj.get("optype") == "videocopyrightinfo.videoid_bar_v1":
        res = get_bar_v1(
            "select videoid x,count(*) y from vm790_bcfe8a202787453d.videocopyrightinfo group by videoid",
            "关联视频ID",
        )
    # videocopyrightinfo(视频版权信息表)->copyrightholder(版权持有人)

    if obj.get("optype") == "videocopyrightinfo.copyrightholder_pie":
        res = get_pie(
            "select copyrightholder x,count(*) y from vm790_bcfe8a202787453d.videocopyrightinfo group by copyrightholder order by x desc",
            "版权持有人",
        )
    if obj.get("optype") == "videocopyrightinfo.copyrightholder_pie_v1":
        res = get_pie_v1(
            "select copyrightholder x,count(*) y from vm790_bcfe8a202787453d.videocopyrightinfo group by copyrightholder",
            "版权持有人",
        )
    if obj.get("optype") == "videocopyrightinfo.copyrightholder_pie_v2":
        res = get_pie_v2(
            "select copyrightholder x,count(*) y from vm790_bcfe8a202787453d.videocopyrightinfo group by copyrightholder",
            "版权持有人",
        )
    if obj.get("optype") == "videocopyrightinfo.copyrightholder_line":
        res = get_line(
            "select copyrightholder x,count(*) y from vm790_bcfe8a202787453d.videocopyrightinfo group by copyrightholder",
            "版权持有人",
        )
    if obj.get("optype") == "videocopyrightinfo.copyrightholder_bar":
        res = get_bar(
            "select copyrightholder x,count(*) y from vm790_bcfe8a202787453d.videocopyrightinfo group by copyrightholder",
            "版权持有人",
        )
    if obj.get("optype") == "videocopyrightinfo.copyrightholder_bar_v1":
        res = get_bar_v1(
            "select copyrightholder x,count(*) y from vm790_bcfe8a202787453d.videocopyrightinfo group by copyrightholder",
            "版权持有人",
        )
    # videocopyrightinfo(视频版权信息表)->copyrightyear(版权年份)

    if obj.get("optype") == "videocopyrightinfo.copyrightyear_pie":
        res = get_pie(
            "select copyrightyear x,count(*) y from vm790_bcfe8a202787453d.videocopyrightinfo group by copyrightyear order by x desc",
            "版权年份",
        )
    if obj.get("optype") == "videocopyrightinfo.copyrightyear_pie_v1":
        res = get_pie_v1(
            "select copyrightyear x,count(*) y from vm790_bcfe8a202787453d.videocopyrightinfo group by copyrightyear",
            "版权年份",
        )
    if obj.get("optype") == "videocopyrightinfo.copyrightyear_pie_v2":
        res = get_pie_v2(
            "select copyrightyear x,count(*) y from vm790_bcfe8a202787453d.videocopyrightinfo group by copyrightyear",
            "版权年份",
        )
    if obj.get("optype") == "videocopyrightinfo.copyrightyear_line":
        res = get_line(
            "select copyrightyear x,count(*) y from vm790_bcfe8a202787453d.videocopyrightinfo group by copyrightyear",
            "版权年份",
        )
    if obj.get("optype") == "videocopyrightinfo.copyrightyear_bar":
        res = get_bar(
            "select copyrightyear x,count(*) y from vm790_bcfe8a202787453d.videocopyrightinfo group by copyrightyear",
            "版权年份",
        )
    if obj.get("optype") == "videocopyrightinfo.copyrightyear_bar_v1":
        res = get_bar_v1(
            "select copyrightyear x,count(*) y from vm790_bcfe8a202787453d.videocopyrightinfo group by copyrightyear",
            "版权年份",
        )
    # videocopyrightinfo(视频版权信息表)->licensetype(许可类型)

    if obj.get("optype") == "videocopyrightinfo.licensetype_pie":
        res = get_pie(
            "select licensetype x,count(*) y from vm790_bcfe8a202787453d.videocopyrightinfo group by licensetype order by x desc",
            "许可类型",
        )
    if obj.get("optype") == "videocopyrightinfo.licensetype_pie_v1":
        res = get_pie_v1(
            "select licensetype x,count(*) y from vm790_bcfe8a202787453d.videocopyrightinfo group by licensetype",
            "许可类型",
        )
    if obj.get("optype") == "videocopyrightinfo.licensetype_pie_v2":
        res = get_pie_v2(
            "select licensetype x,count(*) y from vm790_bcfe8a202787453d.videocopyrightinfo group by licensetype",
            "许可类型",
        )
    if obj.get("optype") == "videocopyrightinfo.licensetype_line":
        res = get_line(
            "select licensetype x,count(*) y from vm790_bcfe8a202787453d.videocopyrightinfo group by licensetype",
            "许可类型",
        )
    if obj.get("optype") == "videocopyrightinfo.licensetype_bar":
        res = get_bar(
            "select licensetype x,count(*) y from vm790_bcfe8a202787453d.videocopyrightinfo group by licensetype",
            "许可类型",
        )
    if obj.get("optype") == "videocopyrightinfo.licensetype_bar_v1":
        res = get_bar_v1(
            "select licensetype x,count(*) y from vm790_bcfe8a202787453d.videocopyrightinfo group by licensetype",
            "许可类型",
        )
    # videocopyrightinfo(视频版权信息表)->licensestatus(许可状态)

    if obj.get("optype") == "videocopyrightinfo.licensestatus_pie":
        res = get_pie(
            "select licensestatus x,count(*) y from vm790_bcfe8a202787453d.videocopyrightinfo group by licensestatus order by x desc",
            "许可状态",
        )
    if obj.get("optype") == "videocopyrightinfo.licensestatus_pie_v1":
        res = get_pie_v1(
            "select licensestatus x,count(*) y from vm790_bcfe8a202787453d.videocopyrightinfo group by licensestatus",
            "许可状态",
        )
    if obj.get("optype") == "videocopyrightinfo.licensestatus_pie_v2":
        res = get_pie_v2(
            "select licensestatus x,count(*) y from vm790_bcfe8a202787453d.videocopyrightinfo group by licensestatus",
            "许可状态",
        )
    if obj.get("optype") == "videocopyrightinfo.licensestatus_line":
        res = get_line(
            "select licensestatus x,count(*) y from vm790_bcfe8a202787453d.videocopyrightinfo group by licensestatus",
            "许可状态",
        )
    if obj.get("optype") == "videocopyrightinfo.licensestatus_bar":
        res = get_bar(
            "select licensestatus x,count(*) y from vm790_bcfe8a202787453d.videocopyrightinfo group by licensestatus",
            "许可状态",
        )
    if obj.get("optype") == "videocopyrightinfo.licensestatus_bar_v1":
        res = get_bar_v1(
            "select licensestatus x,count(*) y from vm790_bcfe8a202787453d.videocopyrightinfo group by licensestatus",
            "许可状态",
        )
    if obj.get("optype") == "videocopyrightinfo.description_wordcloud":
        textlist = get_data(
            "SELECT description result FROM vm790_bcfe8a202787453d.videocopyrightinfo;"
        )
        res = {
            "title": "词云图",
            "imgbs64": generate_wordcloud_base64(
                ",".join([t["result"] for t in textlist])
            ),
        }
    if obj.get("optype") == "videocopyrightinfo.creationdate_line":
        res = get_line(
            "select creationdate x,count(*) y from vm790_bcfe8a202787453d.videocopyrightinfo group by creationdate order by x",
            "创建日期",
        )
    if obj.get("optype") == "videocopyrightinfo.modkwkwificationdate_line":
        res = get_line(
            "select modkwkwificationdate x,count(*) y from vm790_bcfe8a202787453d.videocopyrightinfo group by modkwkwificationdate order by x",
            "修改日期",
        )
    # videocopyrightinfo(视频版权信息表)->relatedvideoid(相关视频ID)

    if obj.get("optype") == "videocopyrightinfo.relatedvideoid_pie":
        res = get_pie(
            "select relatedvideoid x,count(*) y from vm790_bcfe8a202787453d.videocopyrightinfo group by relatedvideoid order by x desc",
            "相关视频ID",
        )
    if obj.get("optype") == "videocopyrightinfo.relatedvideoid_pie_v1":
        res = get_pie_v1(
            "select relatedvideoid x,count(*) y from vm790_bcfe8a202787453d.videocopyrightinfo group by relatedvideoid",
            "相关视频ID",
        )
    if obj.get("optype") == "videocopyrightinfo.relatedvideoid_pie_v2":
        res = get_pie_v2(
            "select relatedvideoid x,count(*) y from vm790_bcfe8a202787453d.videocopyrightinfo group by relatedvideoid",
            "相关视频ID",
        )
    if obj.get("optype") == "videocopyrightinfo.relatedvideoid_line":
        res = get_line(
            "select relatedvideoid x,count(*) y from vm790_bcfe8a202787453d.videocopyrightinfo group by relatedvideoid",
            "相关视频ID",
        )
    if obj.get("optype") == "videocopyrightinfo.relatedvideoid_bar":
        res = get_bar(
            "select relatedvideoid x,count(*) y from vm790_bcfe8a202787453d.videocopyrightinfo group by relatedvideoid",
            "相关视频ID",
        )
    if obj.get("optype") == "videocopyrightinfo.relatedvideoid_bar_v1":
        res = get_bar_v1(
            "select relatedvideoid x,count(*) y from vm790_bcfe8a202787453d.videocopyrightinfo group by relatedvideoid",
            "相关视频ID",
        )
    # supermanager(系统管理员)->username(管理员姓名)

    if obj.get("optype") == "supermanager.username_pie":
        res = get_pie(
            "select username x,count(*) y from vm790_bcfe8a202787453d.supermanager group by username order by x desc",
            "管理员姓名",
        )
    if obj.get("optype") == "supermanager.username_pie_v1":
        res = get_pie_v1(
            "select username x,count(*) y from vm790_bcfe8a202787453d.supermanager group by username",
            "管理员姓名",
        )
    if obj.get("optype") == "supermanager.username_pie_v2":
        res = get_pie_v2(
            "select username x,count(*) y from vm790_bcfe8a202787453d.supermanager group by username",
            "管理员姓名",
        )
    if obj.get("optype") == "supermanager.username_line":
        res = get_line(
            "select username x,count(*) y from vm790_bcfe8a202787453d.supermanager group by username",
            "管理员姓名",
        )
    if obj.get("optype") == "supermanager.username_bar":
        res = get_bar(
            "select username x,count(*) y from vm790_bcfe8a202787453d.supermanager group by username",
            "管理员姓名",
        )
    if obj.get("optype") == "supermanager.username_bar_v1":
        res = get_bar_v1(
            "select username x,count(*) y from vm790_bcfe8a202787453d.supermanager group by username",
            "管理员姓名",
        )
    assert "title" in res
    return JsonResponse(res)


# __config_visual_views


def bi_level_2(request):
    if request.method == "GET":
        return HttpResponse(
            loader.get_template("config_visual/bi_level_2.html").render({}, request)
        )
    obj = mydict(request.POST)
    res = dict()

    return JsonResponse(res)


def bi_new(request):
    if request.method == "GET":
        return HttpResponse(loader.get_template("config_visual/bi_new.html").render())
    obj = mydict(request.POST)
    res = dict()

    # __mark_appcenter_views_all__level_new_bi

    return JsonResponse(res)


def view_videoinfo(request):
    if request.method == "GET":
        return render(request, "config_visual/bi__tpvideoinfo.html", locals())


def view_videocategkwkwory(request):
    if request.method == "GET":
        return render(request, "config_visual/bi__tpvideocategkwkwory.html", locals())


def view_videotag(request):
    if request.method == "GET":
        return render(request, "config_visual/bi__tpvideotag.html", locals())


def view_videofilestkwkworage(request):
    if request.method == "GET":
        return render(
            request, "config_visual/bi__tpvideofilestkwkworage.html", locals()
        )


def view_videoplayreckwkword(request):
    if request.method == "GET":
        return render(request, "config_visual/bi__tpvideoplayreckwkword.html", locals())


def view_videocomment(request):
    if request.method == "GET":
        return render(request, "config_visual/bi__tpvideocomment.html", locals())


def view_videolike(request):
    if request.method == "GET":
        return render(request, "config_visual/bi__tpvideolike.html", locals())


def view_videoshare(request):
    if request.method == "GET":
        return render(request, "config_visual/bi__tpvideoshare.html", locals())


def view_videoviewduration(request):
    if request.method == "GET":
        return render(request, "config_visual/bi__tpvideoviewduration.html", locals())


def view_videouploader(request):
    if request.method == "GET":
        return render(request, "config_visual/bi__tpvideouploader.html", locals())


def view_userinfo(request):
    if request.method == "GET":
        return render(request, "config_visual/bi__tpuserinfo.html", locals())


def view_userpermkwkwission(request):
    if request.method == "GET":
        return render(request, "config_visual/bi__tpuserpermkwkwission.html", locals())


def view_userwatchhkwkwistkwkwory(request):
    if request.method == "GET":
        return render(
            request, "config_visual/bi__tpuserwatchhkwkwistkwkwory.html", locals()
        )


def view_videoauditstatus(request):
    if request.method == "GET":
        return render(request, "config_visual/bi__tpvideoauditstatus.html", locals())


def view_videocoverimage(request):
    if request.method == "GET":
        return render(request, "config_visual/bi__tpvideocoverimage.html", locals())


def view_videomatrixconfig(request):
    if request.method == "GET":
        return render(request, "config_visual/bi__tpvideomatrixconfig.html", locals())


def view_videomatrixnode(request):
    if request.method == "GET":
        return render(request, "config_visual/bi__tpvideomatrixnode.html", locals())


def view_videomatrixplayreckwkword(request):
    if request.method == "GET":
        return render(
            request, "config_visual/bi__tpvideomatrixplayreckwkword.html", locals()
        )


def view_videorelatedcontent(request):
    if request.method == "GET":
        return render(request, "config_visual/bi__tpvideorelatedcontent.html", locals())


def view_videoerrkwkworlog(request):
    if request.method == "GET":
        return render(request, "config_visual/bi__tpvideoerrkwkworlog.html", locals())


def view_videopopularity(request):
    if request.method == "GET":
        return render(request, "config_visual/bi__tpvideopopularity.html", locals())


def view_videorecommendationparams(request):
    if request.method == "GET":
        return render(
            request, "config_visual/bi__tpvideorecommendationparams.html", locals()
        )


def view_videoadinfo(request):
    if request.method == "GET":
        return render(request, "config_visual/bi__tpvideoadinfo.html", locals())


def view_videoadplayreckwkword(request):
    if request.method == "GET":
        return render(
            request, "config_visual/bi__tpvideoadplayreckwkword.html", locals()
        )


def view_videodanmu(request):
    if request.method == "GET":
        return render(request, "config_visual/bi__tpvideodanmu.html", locals())


def view_videodanmublockwkwkwords(request):
    if request.method == "GET":
        return render(
            request, "config_visual/bi__tpvideodanmublockwkwkwords.html", locals()
        )


def view_videomultilkwkwingualsubtitles(request):
    if request.method == "GET":
        return render(
            request, "config_visual/bi__tpvideomultilkwkwingualsubtitles.html", locals()
        )


def view_videotranscodkwkwingtkwkwask(request):
    if request.method == "GET":
        return render(
            request, "config_visual/bi__tpvideotranscodkwkwingtkwkwask.html", locals()
        )


def view_videoanalyskwkwismetrics(request):
    if request.method == "GET":
        return render(
            request, "config_visual/bi__tpvideoanalyskwkwismetrics.html", locals()
        )


def view_videoqualityassessment(request):
    if request.method == "GET":
        return render(
            request, "config_visual/bi__tpvideoqualityassessment.html", locals()
        )


def view_videowatermarkinfo(request):
    if request.method == "GET":
        return render(request, "config_visual/bi__tpvideowatermarkinfo.html", locals())


def view_videocopyrightinfo(request):
    if request.method == "GET":
        return render(request, "config_visual/bi__tpvideocopyrightinfo.html", locals())


def view_supermanager(request):
    if request.method == "GET":
        return render(request, "config_visual/bi__tpsupermanager.html", locals())
