from django.urls import path, re_path

from . import views

urlpatterns = [
    path("", views.index, name="config_visual_view_index"),
    path("bi", views.bi, name="config_visual_view_bi"),
    path("bi_level_2", views.bi_level_2, name="config_visual_view_bi_level_2"),
    path("bi_new", views.bi_new, name="config_visual_view_bi_new"),
    path("bi_v1", views.bi, name="config_visual_view_bi_v1"),
    path("bi_v2", views.bi, name="config_visual_view_bi_v2"),
    path("bi_v3", views.bi, name="config_visual_view_bi_v3"),
    path("bi_v4", views.bi, name="config_visual_view_bi_v4"),
    path("bi_v5", views.bi, name="config_visual_view_bi_v5"),
    #
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tpvideoinfo",
        views.view_videoinfo,
        name="bi_tpvideoinfo",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tpvideocategkwkwory",
        views.view_videocategkwkwory,
        name="bi_tpvideocategkwkwory",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tpvideotag",
        views.view_videotag,
        name="bi_tpvideotag",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tpvideofilestkwkworage",
        views.view_videofilestkwkworage,
        name="bi_tpvideofilestkwkworage",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tpvideoplayreckwkword",
        views.view_videoplayreckwkword,
        name="bi_tpvideoplayreckwkword",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tpvideocomment",
        views.view_videocomment,
        name="bi_tpvideocomment",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tpvideolike",
        views.view_videolike,
        name="bi_tpvideolike",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tpvideoshare",
        views.view_videoshare,
        name="bi_tpvideoshare",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tpvideoviewduration",
        views.view_videoviewduration,
        name="bi_tpvideoviewduration",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tpvideouploader",
        views.view_videouploader,
        name="bi_tpvideouploader",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tpuserinfo",
        views.view_userinfo,
        name="bi_tpuserinfo",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tpuserpermkwkwission",
        views.view_userpermkwkwission,
        name="bi_tpuserpermkwkwission",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tpuserwatchhkwkwistkwkwory",
        views.view_userwatchhkwkwistkwkwory,
        name="bi_tpuserwatchhkwkwistkwkwory",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tpvideoauditstatus",
        views.view_videoauditstatus,
        name="bi_tpvideoauditstatus",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tpvideocoverimage",
        views.view_videocoverimage,
        name="bi_tpvideocoverimage",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tpvideomatrixconfig",
        views.view_videomatrixconfig,
        name="bi_tpvideomatrixconfig",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tpvideomatrixnode",
        views.view_videomatrixnode,
        name="bi_tpvideomatrixnode",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tpvideomatrixplayreckwkword",
        views.view_videomatrixplayreckwkword,
        name="bi_tpvideomatrixplayreckwkword",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tpvideorelatedcontent",
        views.view_videorelatedcontent,
        name="bi_tpvideorelatedcontent",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tpvideoerrkwkworlog",
        views.view_videoerrkwkworlog,
        name="bi_tpvideoerrkwkworlog",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tpvideopopularity",
        views.view_videopopularity,
        name="bi_tpvideopopularity",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tpvideorecommendationparams",
        views.view_videorecommendationparams,
        name="bi_tpvideorecommendationparams",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tpvideoadinfo",
        views.view_videoadinfo,
        name="bi_tpvideoadinfo",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tpvideoadplayreckwkword",
        views.view_videoadplayreckwkword,
        name="bi_tpvideoadplayreckwkword",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tpvideodanmu",
        views.view_videodanmu,
        name="bi_tpvideodanmu",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tpvideodanmublockwkwkwords",
        views.view_videodanmublockwkwkwords,
        name="bi_tpvideodanmublockwkwkwords",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tpvideomultilkwkwingualsubtitles",
        views.view_videomultilkwkwingualsubtitles,
        name="bi_tpvideomultilkwkwingualsubtitles",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tpvideotranscodkwkwingtkwkwask",
        views.view_videotranscodkwkwingtkwkwask,
        name="bi_tpvideotranscodkwkwingtkwkwask",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tpvideoanalyskwkwismetrics",
        views.view_videoanalyskwkwismetrics,
        name="bi_tpvideoanalyskwkwismetrics",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tpvideoqualityassessment",
        views.view_videoqualityassessment,
        name="bi_tpvideoqualityassessment",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tpvideowatermarkinfo",
        views.view_videowatermarkinfo,
        name="bi_tpvideowatermarkinfo",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tpvideocopyrightinfo",
        views.view_videocopyrightinfo,
        name="bi_tpvideocopyrightinfo",
    ),
    # config_visual_urls pattern 添加 每个表对应的bi文件的url
    path(
        "bi_tpsupermanager",
        views.view_supermanager,
        name="bi_tpsupermanager",
    ),
]
