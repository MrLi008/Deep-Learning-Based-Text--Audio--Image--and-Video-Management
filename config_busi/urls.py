from django.urls import path, re_path

from . import views

urlpatterns = [
    path("", views.index, name="config_busi_view_index"),
    # 如果用到预测算法,图像识别等单页面展示效果的算法去掉下方注释
    path("auto_detect", views.auto_detect, name="config_busi_view_auto_detect"),
    path("videoinfo", views.view_videoinfo, name="config_busi_view_videoinfo"),
    path(
        "videocategkwkwory",
        views.view_videocategkwkwory,
        name="config_busi_view_videocategkwkwory",
    ),
    path("videotag", views.view_videotag, name="config_busi_view_videotag"),
    path(
        "videofilestkwkworage",
        views.view_videofilestkwkworage,
        name="config_busi_view_videofilestkwkworage",
    ),
    path(
        "videoplayreckwkword",
        views.view_videoplayreckwkword,
        name="config_busi_view_videoplayreckwkword",
    ),
    path("videocomment", views.view_videocomment, name="config_busi_view_videocomment"),
    path("videolike", views.view_videolike, name="config_busi_view_videolike"),
    path("videoshare", views.view_videoshare, name="config_busi_view_videoshare"),
    path(
        "videoviewduration",
        views.view_videoviewduration,
        name="config_busi_view_videoviewduration",
    ),
    path(
        "videouploader", views.view_videouploader, name="config_busi_view_videouploader"
    ),
    path("userinfo", views.view_userinfo, name="config_busi_view_userinfo"),
    path(
        "userpermkwkwission",
        views.view_userpermkwkwission,
        name="config_busi_view_userpermkwkwission",
    ),
    path(
        "userwatchhkwkwistkwkwory",
        views.view_userwatchhkwkwistkwkwory,
        name="config_busi_view_userwatchhkwkwistkwkwory",
    ),
    path(
        "videoauditstatus",
        views.view_videoauditstatus,
        name="config_busi_view_videoauditstatus",
    ),
    path(
        "videocoverimage",
        views.view_videocoverimage,
        name="config_busi_view_videocoverimage",
    ),
    path(
        "videomatrixconfig",
        views.view_videomatrixconfig,
        name="config_busi_view_videomatrixconfig",
    ),
    path(
        "videomatrixnode",
        views.view_videomatrixnode,
        name="config_busi_view_videomatrixnode",
    ),
    path(
        "videomatrixplayreckwkword",
        views.view_videomatrixplayreckwkword,
        name="config_busi_view_videomatrixplayreckwkword",
    ),
    path(
        "videorelatedcontent",
        views.view_videorelatedcontent,
        name="config_busi_view_videorelatedcontent",
    ),
    path(
        "videoerrkwkworlog",
        views.view_videoerrkwkworlog,
        name="config_busi_view_videoerrkwkworlog",
    ),
    path(
        "videopopularity",
        views.view_videopopularity,
        name="config_busi_view_videopopularity",
    ),
    path(
        "videorecommendationparams",
        views.view_videorecommendationparams,
        name="config_busi_view_videorecommendationparams",
    ),
    path("videoadinfo", views.view_videoadinfo, name="config_busi_view_videoadinfo"),
    path(
        "videoadplayreckwkword",
        views.view_videoadplayreckwkword,
        name="config_busi_view_videoadplayreckwkword",
    ),
    path("videodanmu", views.view_videodanmu, name="config_busi_view_videodanmu"),
    path(
        "videodanmublockwkwkwords",
        views.view_videodanmublockwkwkwords,
        name="config_busi_view_videodanmublockwkwkwords",
    ),
    path(
        "videomultilkwkwingualsubtitles",
        views.view_videomultilkwkwingualsubtitles,
        name="config_busi_view_videomultilkwkwingualsubtitles",
    ),
    path(
        "videotranscodkwkwingtkwkwask",
        views.view_videotranscodkwkwingtkwkwask,
        name="config_busi_view_videotranscodkwkwingtkwkwask",
    ),
    path(
        "videoanalyskwkwismetrics",
        views.view_videoanalyskwkwismetrics,
        name="config_busi_view_videoanalyskwkwismetrics",
    ),
    path(
        "videoqualityassessment",
        views.view_videoqualityassessment,
        name="config_busi_view_videoqualityassessment",
    ),
    path(
        "videowatermarkinfo",
        views.view_videowatermarkinfo,
        name="config_busi_view_videowatermarkinfo",
    ),
    path(
        "videocopyrightinfo",
        views.view_videocopyrightinfo,
        name="config_busi_view_videocopyrightinfo",
    ),
    path("supermanager", views.view_supermanager, name="config_busi_view_supermanager"),
]
