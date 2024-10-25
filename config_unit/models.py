from django.db import models
from appcenter.models import *
from config_visual.models import *
from sys_user.models import *
from sys_user.func import *

all_tables = dict()
gl = dict()

# Create your models here.

all_tables = {
    "videoinfo": mymeta(mc_videoinfo),
    "videocategkwkwory": mymeta(mc_videocategkwkwory),
    "videotag": mymeta(mc_videotag),
    "videofilestkwkworage": mymeta(mc_videofilestkwkworage),
    "videoplayreckwkword": mymeta(mc_videoplayreckwkword),
    "videocomment": mymeta(mc_videocomment),
    "videolike": mymeta(mc_videolike),
    "videoshare": mymeta(mc_videoshare),
    "videoviewduration": mymeta(mc_videoviewduration),
    "videouploader": mymeta(mc_videouploader),
    "userinfo": mymeta(mc_userinfo),
    "userpermkwkwission": mymeta(mc_userpermkwkwission),
    "userwatchhkwkwistkwkwory": mymeta(mc_userwatchhkwkwistkwkwory),
    "videoauditstatus": mymeta(mc_videoauditstatus),
    "videocoverimage": mymeta(mc_videocoverimage),
    "videomatrixconfig": mymeta(mc_videomatrixconfig),
    "videomatrixnode": mymeta(mc_videomatrixnode),
    "videomatrixplayreckwkword": mymeta(mc_videomatrixplayreckwkword),
    "videorelatedcontent": mymeta(mc_videorelatedcontent),
    "videoerrkwkworlog": mymeta(mc_videoerrkwkworlog),
    "videopopularity": mymeta(mc_videopopularity),
    "videorecommendationparams": mymeta(mc_videorecommendationparams),
    "videoadinfo": mymeta(mc_videoadinfo),
    "videoadplayreckwkword": mymeta(mc_videoadplayreckwkword),
    "videodanmu": mymeta(mc_videodanmu),
    "videodanmublockwkwkwords": mymeta(mc_videodanmublockwkwkwords),
    "videomultilkwkwingualsubtitles": mymeta(mc_videomultilkwkwingualsubtitles),
    "videotranscodkwkwingtkwkwask": mymeta(mc_videotranscodkwkwingtkwkwask),
    "videoanalyskwkwismetrics": mymeta(mc_videoanalyskwkwismetrics),
    "videoqualityassessment": mymeta(mc_videoqualityassessment),
    "videowatermarkinfo": mymeta(mc_videowatermarkinfo),
    "videocopyrightinfo": mymeta(mc_videocopyrightinfo),
    "supermanager": mymeta(mc_supermanager),
}

# 所有用户表

all_tables_user = {
    "userinfo": mymeta(mc_userinfo),
    "supermanager": mymeta(mc_supermanager),
}
gl = {
    "videoinfo": mc_videoinfo,
    "videocategkwkwory": mc_videocategkwkwory,
    "videotag": mc_videotag,
    "videofilestkwkworage": mc_videofilestkwkworage,
    "videoplayreckwkword": mc_videoplayreckwkword,
    "videocomment": mc_videocomment,
    "videolike": mc_videolike,
    "videoshare": mc_videoshare,
    "videoviewduration": mc_videoviewduration,
    "videouploader": mc_videouploader,
    "userinfo": mc_userinfo,
    "userpermkwkwission": mc_userpermkwkwission,
    "userwatchhkwkwistkwkwory": mc_userwatchhkwkwistkwkwory,
    "videoauditstatus": mc_videoauditstatus,
    "videocoverimage": mc_videocoverimage,
    "videomatrixconfig": mc_videomatrixconfig,
    "videomatrixnode": mc_videomatrixnode,
    "videomatrixplayreckwkword": mc_videomatrixplayreckwkword,
    "videorelatedcontent": mc_videorelatedcontent,
    "videoerrkwkworlog": mc_videoerrkwkworlog,
    "videopopularity": mc_videopopularity,
    "videorecommendationparams": mc_videorecommendationparams,
    "videoadinfo": mc_videoadinfo,
    "videoadplayreckwkword": mc_videoadplayreckwkword,
    "videodanmu": mc_videodanmu,
    "videodanmublockwkwkwords": mc_videodanmublockwkwkwords,
    "videomultilkwkwingualsubtitles": mc_videomultilkwkwingualsubtitles,
    "videotranscodkwkwingtkwkwask": mc_videotranscodkwkwingtkwkwask,
    "videoanalyskwkwismetrics": mc_videoanalyskwkwismetrics,
    "videoqualityassessment": mc_videoqualityassessment,
    "videowatermarkinfo": mc_videowatermarkinfo,
    "videocopyrightinfo": mc_videocopyrightinfo,
    "supermanager": mc_supermanager,
}
