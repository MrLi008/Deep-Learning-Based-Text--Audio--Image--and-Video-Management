from django.contrib import admin

from django.forms.widgets import Select

# Register your models here.

admin.site.site_header = "基于深度学习的文案语音图片视频管理分析-视频矩阵系统"
admin.site.site_title = "基于深度学习的文案语音图片视频管理分析-视频矩阵系统"
admin.site.index_title = "基于深度学习的文案语音图片视频管理分析-视频矩阵系统"

from .models import *


class mc_videoinfo_admin(admin.ModelAdmin):
    list_display = [
        "videodescription",
        "duration",
        "uploadtime",
        "videotitle",
        "categkwkworyid_showmsg",
        "filetype",
        "filesize",
        "resolution",
        "creatkwkworid_showmsg",
        "videoid",
    ]
    fields = [
        "videodescription",
        "creatkwkworid",
        "duration",
        "uploadtime",
        "videotitle",
        "filetype",
        "filesize",
        "resolution",
        "videoid",
        "categkwkworyid",
    ]

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request=request, obj=obj, change=change, **kwargs)

        # :TODO
        form.base_fields["creatkwkworid"].widget = Select(
            choices=[("", "未选择")]
            + [
                (
                    item.id,
                    # (item.id,
                    str(item.id) + ":" + str(item.username),
                )
                for item in mc_userinfo.objects.all()
            ]
        )

        # :TODO
        form.base_fields["categkwkworyid"].widget = Select(
            choices=[("", "未选择")]
            + [
                (
                    item.id,
                    # (item.id,
                    str(item.id) + ":" + str(item.name),
                )
                for item in mc_videocategkwkwory.objects.all()
            ]
        )

        return form

    def creatkwkworid_showmsg(self, obj):
        showmsg_id = obj.creatkwkworid
        try:
            label = mc_userinfo.objects.get(id=showmsg_id).username
        except Exception as e:
            label = "查找失败"
        return f"{showmsg_id}:{label}"

    creatkwkworid_showmsg.short_description = "创建者ID关联用户"

    def categkwkworyid_showmsg(self, obj):
        showmsg_id = obj.categkwkworyid
        try:
            label = mc_videocategkwkwory.objects.get(id=showmsg_id).name
        except Exception as e:
            label = "查找失败"
        return f"{showmsg_id}:{label}"

    categkwkworyid_showmsg.short_description = "类别ID关联视频类别"


admin.site.register(mc_videoinfo, mc_videoinfo_admin)


class mc_videocategkwkwory_admin(admin.ModelAdmin):
    list_display = [
        "kwkwisactive",
        "parentid",
        "createtime",
        "description",
        "name",
        "skwkwortorder",
        "updatetime",
    ]
    fields = [
        "kwkwisactive",
        "parentid",
        "createtime",
        "description",
        "name",
        "skwkwortorder",
        "updatetime",
    ]


admin.site.register(mc_videocategkwkwory, mc_videocategkwkwory_admin)


class mc_videotag_admin(admin.ModelAdmin):
    list_display = [
        "tagname",
        "kwkwisactive",
        "createtime",
        "description",
        "updatetime",
        "creatkwkworid_showmsg",
        "tagid",
        "videoid_showmsg",
    ]
    fields = [
        "tagname",
        "kwkwisactive",
        "creatkwkworid",
        "createtime",
        "description",
        "updatetime",
        "tagid",
        "videoid",
    ]

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request=request, obj=obj, change=change, **kwargs)

        # :TODO
        form.base_fields["videoid"].widget = Select(
            choices=[("", "未选择")]
            + [
                (
                    item.id,
                    # (item.id,
                    str(item.id) + ":" + str(item.videotitle),
                )
                for item in mc_videoinfo.objects.all()
            ]
        )

        # :TODO
        form.base_fields["creatkwkworid"].widget = Select(
            choices=[("", "未选择")]
            + [
                (
                    item.id,
                    # (item.id,
                    str(item.id) + ":" + str(item.username),
                )
                for item in mc_userinfo.objects.all()
            ]
        )

        return form

    def videoid_showmsg(self, obj):
        showmsg_id = obj.videoid
        try:
            label = mc_videoinfo.objects.get(id=showmsg_id).videotitle
        except Exception as e:
            label = "查找失败"
        return f"{showmsg_id}:{label}"

    videoid_showmsg.short_description = "视频ID关联字段指向视频中的视频ID"

    def creatkwkworid_showmsg(self, obj):
        showmsg_id = obj.creatkwkworid
        try:
            label = mc_userinfo.objects.get(id=showmsg_id).username
        except Exception as e:
            label = "查找失败"
        return f"{showmsg_id}:{label}"

    creatkwkworid_showmsg.short_description = "创建者ID关联字段指向用户中的用户ID"


admin.site.register(mc_videotag, mc_videotag_admin)


class mc_videofilestkwkworage_admin(admin.ModelAdmin):
    list_display = [
        "filename",
        "kwkwfkwkwormat",
        "duration",
        "uploadtime",
        "categkwkworyid_showmsg",
        "filesize",
        "resolution",
        "creatkwkworid_showmsg",
        "filepath",
        "videoid",
    ]
    fields = [
        "filename",
        "kwkwfkwkwormat",
        "creatkwkworid",
        "duration",
        "uploadtime",
        "filesize",
        "resolution",
        "filepath",
        "videoid",
        "categkwkworyid",
    ]

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request=request, obj=obj, change=change, **kwargs)

        # :TODO
        form.base_fields["creatkwkworid"].widget = Select(
            choices=[("", "未选择")]
            + [
                (
                    item.id,
                    # (item.id,
                    str(item.id) + ":" + str(item.username),
                )
                for item in mc_userinfo.objects.all()
            ]
        )

        # :TODO
        form.base_fields["categkwkworyid"].widget = Select(
            choices=[("", "未选择")]
            + [
                (
                    item.id,
                    # (item.id,
                    str(item.id) + ":" + str(item.name),
                )
                for item in mc_videocategkwkwory.objects.all()
            ]
        )

        return form

    def creatkwkworid_showmsg(self, obj):
        showmsg_id = obj.creatkwkworid
        try:
            label = mc_userinfo.objects.get(id=showmsg_id).username
        except Exception as e:
            label = "查找失败"
        return f"{showmsg_id}:{label}"

    creatkwkworid_showmsg.short_description = "创建者ID关联用户"

    def categkwkworyid_showmsg(self, obj):
        showmsg_id = obj.categkwkworyid
        try:
            label = mc_videocategkwkwory.objects.get(id=showmsg_id).name
        except Exception as e:
            label = "查找失败"
        return f"{showmsg_id}:{label}"

    categkwkworyid_showmsg.short_description = "分类ID关联视频分类"


admin.site.register(mc_videofilestkwkworage, mc_videofilestkwkworage_admin)


class mc_videoplayreckwkword_admin(admin.ModelAdmin):
    list_display = [
        "userid_showmsg",
        "playendtime",
        "playstarttime",
        "playstatus",
        "devicetype",
        "ipaddress",
        "playduration",
        "videoid_showmsg",
        "location",
    ]
    fields = [
        "playendtime",
        "playstarttime",
        "playstatus",
        "userid",
        "devicetype",
        "ipaddress",
        "playduration",
        "videoid",
        "location",
    ]

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request=request, obj=obj, change=change, **kwargs)

        # :TODO
        form.base_fields["videoid"].widget = Select(
            choices=[("", "未选择")]
            + [
                (
                    item.id,
                    # (item.id,
                    str(item.id) + ":" + str(item.videotitle),
                )
                for item in mc_videoinfo.objects.all()
            ]
        )

        # :TODO
        form.base_fields["userid"].widget = Select(
            choices=[("", "未选择")]
            + [
                (
                    item.id,
                    # (item.id,
                    str(item.id) + ":" + str(item.username),
                )
                for item in mc_userinfo.objects.all()
            ]
        )

        return form

    def videoid_showmsg(self, obj):
        showmsg_id = obj.videoid
        try:
            label = mc_videoinfo.objects.get(id=showmsg_id).videotitle
        except Exception as e:
            label = "查找失败"
        return f"{showmsg_id}:{label}"

    videoid_showmsg.short_description = "视频ID关联视频信息"

    def userid_showmsg(self, obj):
        showmsg_id = obj.userid
        try:
            label = mc_userinfo.objects.get(id=showmsg_id).username
        except Exception as e:
            label = "查找失败"
        return f"{showmsg_id}:{label}"

    userid_showmsg.short_description = "用户ID关联用户信息"


admin.site.register(mc_videoplayreckwkword, mc_videoplayreckwkword_admin)


class mc_videocomment_admin(admin.ModelAdmin):
    list_display = [
        "userid_showmsg",
        "replycount",
        "content",
        "parentid_showmsg",
        "createtime",
        "kwkwiskwkwdeleted",
        "videoid_showmsg",
        "likecount",
    ]
    fields = [
        "replycount",
        "userid",
        "parentid",
        "createtime",
        "kwkwiskwkwdeleted",
        "likecount",
        "videoid",
        "content",
    ]

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request=request, obj=obj, change=change, **kwargs)

        # :TODO
        form.base_fields["videoid"].widget = Select(
            choices=[("", "未选择")]
            + [
                (
                    item.id,
                    # (item.id,
                    str(item.id) + ":" + str(item.videotitle),
                )
                for item in mc_videoinfo.objects.all()
            ]
        )

        # :TODO
        form.base_fields["userid"].widget = Select(
            choices=[("", "未选择")]
            + [
                (
                    item.id,
                    # (item.id,
                    str(item.id) + ":" + str(item.username),
                )
                for item in mc_userinfo.objects.all()
            ]
        )

        # :TODO
        form.base_fields["parentid"].widget = Select(
            choices=[("", "未选择")]
            + [
                (
                    item.id,
                    # (item.id,
                    str(item.id) + ":" + str(item.content),
                )
                for item in mc_videocomment.objects.all()
            ]
        )

        return form

    def videoid_showmsg(self, obj):
        showmsg_id = obj.videoid
        try:
            label = mc_videoinfo.objects.get(id=showmsg_id).videotitle
        except Exception as e:
            label = "查找失败"
        return f"{showmsg_id}:{label}"

    videoid_showmsg.short_description = "关联视频ID"

    def userid_showmsg(self, obj):
        showmsg_id = obj.userid
        try:
            label = mc_userinfo.objects.get(id=showmsg_id).username
        except Exception as e:
            label = "查找失败"
        return f"{showmsg_id}:{label}"

    userid_showmsg.short_description = "关联用户ID"

    def parentid_showmsg(self, obj):
        showmsg_id = obj.parentid
        try:
            label = mc_videocomment.objects.get(id=showmsg_id).content
        except Exception as e:
            label = "查找失败"
        return f"{showmsg_id}:{label}"

    parentid_showmsg.short_description = "关联父评论ID"


admin.site.register(mc_videocomment, mc_videocomment_admin)


class mc_videolike_admin(admin.ModelAdmin):
    list_display = [
        "userid_showmsg",
        "liketime",
        "deviceid",
        "ipaddress",
        "liketype",
        "platkwkwfkwkworm",
        "videoid_showmsg",
        "kwkwisliked",
    ]
    fields = [
        "kwkwisliked",
        "userid",
        "liketime",
        "ipaddress",
        "liketype",
        "platkwkwfkwkworm",
        "deviceid",
        "videoid",
    ]

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request=request, obj=obj, change=change, **kwargs)

        # :TODO
        form.base_fields["videoid"].widget = Select(
            choices=[("", "未选择")]
            + [
                (
                    item.id,
                    # (item.id,
                    str(item.id) + ":" + str(item.videotitle),
                )
                for item in mc_videoinfo.objects.all()
            ]
        )

        # :TODO
        form.base_fields["userid"].widget = Select(
            choices=[("", "未选择")]
            + [
                (
                    item.id,
                    # (item.id,
                    str(item.id) + ":" + str(item.username),
                )
                for item in mc_userinfo.objects.all()
            ]
        )

        return form

    def videoid_showmsg(self, obj):
        showmsg_id = obj.videoid
        try:
            label = mc_videoinfo.objects.get(id=showmsg_id).videotitle
        except Exception as e:
            label = "查找失败"
        return f"{showmsg_id}:{label}"

    videoid_showmsg.short_description = "关联视频ID"

    def userid_showmsg(self, obj):
        showmsg_id = obj.userid
        try:
            label = mc_userinfo.objects.get(id=showmsg_id).username
        except Exception as e:
            label = "查找失败"
        return f"{showmsg_id}:{label}"

    userid_showmsg.short_description = "关联用户ID"


admin.site.register(mc_videolike, mc_videolike_admin)


class mc_videoshare_admin(admin.ModelAdmin):
    list_display = [
        "viewcount",
        "sharetime",
        "title",
        "userid_showmsg",
        "id",
        "commentcount",
        "description",
        "thumbnailurl",
        "videoid_showmsg",
        "sharestatus",
        "likecount",
    ]
    fields = [
        "sharetime",
        "title",
        "sharestatus",
        "userid",
        "commentcount",
        "description",
        "thumbnailurl",
        "viewcount",
        "videoid",
        "likecount",
    ]

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request=request, obj=obj, change=change, **kwargs)

        # :TODO
        form.base_fields["videoid"].widget = Select(
            choices=[("", "未选择")]
            + [
                (
                    item.id,
                    # (item.id,
                    str(item.id) + ":" + str(item.videotitle),
                )
                for item in mc_videoinfo.objects.all()
            ]
        )

        # :TODO
        form.base_fields["userid"].widget = Select(
            choices=[("", "未选择")]
            + [
                (
                    item.id,
                    # (item.id,
                    str(item.id) + ":" + str(item.username),
                )
                for item in mc_userinfo.objects.all()
            ]
        )

        return form

    def videoid_showmsg(self, obj):
        showmsg_id = obj.videoid
        try:
            label = mc_videoinfo.objects.get(id=showmsg_id).videotitle
        except Exception as e:
            label = "查找失败"
        return f"{showmsg_id}:{label}"

    videoid_showmsg.short_description = "关联视频ID"

    def userid_showmsg(self, obj):
        showmsg_id = obj.userid
        try:
            label = mc_userinfo.objects.get(id=showmsg_id).username
        except Exception as e:
            label = "查找失败"
        return f"{showmsg_id}:{label}"

    userid_showmsg.short_description = "关联用户ID"


admin.site.register(mc_videoshare, mc_videoshare_admin)


class mc_videoviewduration_admin(admin.ModelAdmin):
    list_display = [
        "viewstarttime",
        "userid_showmsg",
        "viewendtime",
        "duration",
        "devicetype",
        "viewlocation",
        "kwkwiscompleted",
        "netwkwkworktype",
        "videoid_showmsg",
    ]
    fields = [
        "viewstarttime",
        "viewendtime",
        "duration",
        "userid",
        "devicetype",
        "viewlocation",
        "kwkwiscompleted",
        "netwkwkworktype",
        "videoid",
    ]

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request=request, obj=obj, change=change, **kwargs)

        # :TODO
        form.base_fields["videoid"].widget = Select(
            choices=[("", "未选择")]
            + [
                (
                    item.id,
                    # (item.id,
                    str(item.id) + ":" + str(item.videotitle),
                )
                for item in mc_videoinfo.objects.all()
            ]
        )

        # :TODO
        form.base_fields["userid"].widget = Select(
            choices=[("", "未选择")]
            + [
                (
                    item.id,
                    # (item.id,
                    str(item.id) + ":" + str(item.username),
                )
                for item in mc_userinfo.objects.all()
            ]
        )

        return form

    def videoid_showmsg(self, obj):
        showmsg_id = obj.videoid
        try:
            label = mc_videoinfo.objects.get(id=showmsg_id).videotitle
        except Exception as e:
            label = "查找失败"
        return f"{showmsg_id}:{label}"

    videoid_showmsg.short_description = "关联视频ID"

    def userid_showmsg(self, obj):
        showmsg_id = obj.userid
        try:
            label = mc_userinfo.objects.get(id=showmsg_id).username
        except Exception as e:
            label = "查找失败"
        return f"{showmsg_id}:{label}"

    userid_showmsg.short_description = "关联用户ID"


admin.site.register(mc_videoviewduration, mc_videoviewduration_admin)


class mc_videouploader_admin(admin.ModelAdmin):
    list_display = [
        "userid_showmsg",
        "videodescription",
        "videocategkwkworyid",
        "uploadtime",
        "videotitle",
        "videostatus",
        "email",
        "videoid",
        "phonenumber",
        "username",
    ]
    fields = [
        "videodescription",
        "videocategkwkworyid",
        "uploadtime",
        "userid",
        "videotitle",
        "videostatus",
        "email",
        "videoid",
        "phonenumber",
        "username",
    ]

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request=request, obj=obj, change=change, **kwargs)

        # :TODO
        form.base_fields["userid"].widget = Select(
            choices=[("", "未选择")]
            + [
                (
                    item.id,
                    # (item.id,
                    str(item.id) + ":" + str(item.username),
                )
                for item in mc_userinfo.objects.all()
            ]
        )

        return form

    def userid_showmsg(self, obj):
        showmsg_id = obj.userid
        try:
            label = mc_userinfo.objects.get(id=showmsg_id).username
        except Exception as e:
            label = "查找失败"
        return f"{showmsg_id}:{label}"

    userid_showmsg.short_description = "关联用户ID"


admin.site.register(mc_videouploader, mc_videouploader_admin)


class mc_userinfo_admin(admin.ModelAdmin):
    list_display = [
        "useremail",
        "gender",
        "lkwkwastlogkwkwintime",
        "userrole",
        "regkwkwisterdate",
        "userid",
        "birthdate",
        "userpkwkwasswkwkword",
        "phonenumber",
        "username",
    ]
    fields = [
        "useremail",
        "gender",
        "lkwkwastlogkwkwintime",
        "userrole",
        "regkwkwisterdate",
        "userid",
        "birthdate",
        "userpkwkwasswkwkword",
        "phonenumber",
        "username",
    ]


admin.site.register(mc_userinfo, mc_userinfo_admin)


class mc_userpermkwkwission_admin(admin.ModelAdmin):
    list_display = [
        "userid_showmsg",
        "rolename",
        "permkwkwissionname",
        "createtime",
        "permkwkwissionid_showmsg",
        "description",
        "updatetime",
        "isactive",
    ]
    fields = [
        "rolename",
        "permkwkwissionid",
        "userid",
        "permkwkwissionname",
        "createtime",
        "description",
        "updatetime",
        "isactive",
    ]

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request=request, obj=obj, change=change, **kwargs)

        # :TODO
        form.base_fields["userid"].widget = Select(
            choices=[("", "未选择")]
            + [
                (
                    item.id,
                    # (item.id,
                    str(item.id) + ":" + str(item.username),
                )
                for item in mc_userinfo.objects.all()
            ]
        )

        # :TODO
        form.base_fields["permkwkwissionid"].widget = Select(
            choices=[("", "未选择")]
            + [
                (
                    item.id,
                    # (item.id,
                    str(item.id) + ":" + str(item.permkwkwissionid),
                )
                for item in mc_userpermkwkwission.objects.all()
            ]
        )

        return form

    def userid_showmsg(self, obj):
        showmsg_id = obj.userid
        try:
            label = mc_userinfo.objects.get(id=showmsg_id).username
        except Exception as e:
            label = "查找失败"
        return f"{showmsg_id}:{label}"

    userid_showmsg.short_description = "关联用户ID"

    def permkwkwissionid_showmsg(self, obj):
        showmsg_id = obj.permkwkwissionid
        try:
            label = mc_userpermkwkwission.objects.get(id=showmsg_id).permkwkwissionid
        except Exception as e:
            label = "查找失败"
        return f"{showmsg_id}:{label}"

    permkwkwissionid_showmsg.short_description = "关联权限ID"


admin.site.register(mc_userpermkwkwission, mc_userpermkwkwission_admin)


class mc_userwatchhkwkwistkwkwory_admin(admin.ModelAdmin):
    list_display = [
        "watchtime",
        "likestatus",
        "userid_showmsg",
        "watchduration",
        "watchstatus",
        "favkwkworitestatus",
        "ratkwkwing",
        "videoid_showmsg",
        "sharestatus",
        "comment",
    ]
    fields = [
        "watchtime",
        "likestatus",
        "userid",
        "watchduration",
        "watchstatus",
        "favkwkworitestatus",
        "ratkwkwing",
        "videoid",
        "comment",
        "sharestatus",
    ]

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request=request, obj=obj, change=change, **kwargs)

        # :TODO
        form.base_fields["userid"].widget = Select(
            choices=[("", "未选择")]
            + [
                (
                    item.id,
                    # (item.id,
                    str(item.id) + ":" + str(item.username),
                )
                for item in mc_userinfo.objects.all()
            ]
        )

        # :TODO
        form.base_fields["videoid"].widget = Select(
            choices=[("", "未选择")]
            + [
                (
                    item.id,
                    # (item.id,
                    str(item.id) + ":" + str(item.videotitle),
                )
                for item in mc_videoinfo.objects.all()
            ]
        )

        return form

    def userid_showmsg(self, obj):
        showmsg_id = obj.userid
        try:
            label = mc_userinfo.objects.get(id=showmsg_id).username
        except Exception as e:
            label = "查找失败"
        return f"{showmsg_id}:{label}"

    userid_showmsg.short_description = "关联用户ID"

    def videoid_showmsg(self, obj):
        showmsg_id = obj.videoid
        try:
            label = mc_videoinfo.objects.get(id=showmsg_id).videotitle
        except Exception as e:
            label = "查找失败"
        return f"{showmsg_id}:{label}"

    videoid_showmsg.short_description = "关联视频ID"


admin.site.register(mc_userwatchhkwkwistkwkwory, mc_userwatchhkwkwistkwkwory_admin)


class mc_videoauditstatus_admin(admin.ModelAdmin):
    list_display = [
        "kwkwisfkwkwinal",
        "updatedat",
        "createdat",
        "reviewtime",
        "videoid_showmsg",
        "comment",
        "rejectrekwkwason",
        "reviewerid_showmsg",
        "status",
    ]
    fields = [
        "kwkwisfkwkwinal",
        "updatedat",
        "createdat",
        "reviewtime",
        "reviewerid",
        "videoid",
        "comment",
        "rejectrekwkwason",
        "status",
    ]

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request=request, obj=obj, change=change, **kwargs)

        # :TODO
        form.base_fields["videoid"].widget = Select(
            choices=[("", "未选择")]
            + [
                (
                    item.id,
                    # (item.id,
                    str(item.id) + ":" + str(item.videotitle),
                )
                for item in mc_videoinfo.objects.all()
            ]
        )

        # :TODO
        form.base_fields["reviewerid"].widget = Select(
            choices=[("", "未选择")]
            + [
                (
                    item.id,
                    # (item.id,
                    str(item.id) + ":" + str(item.username),
                )
                for item in mc_supermanager.objects.all()
            ]
        )

        return form

    def videoid_showmsg(self, obj):
        showmsg_id = obj.videoid
        try:
            label = mc_videoinfo.objects.get(id=showmsg_id).videotitle
        except Exception as e:
            label = "查找失败"
        return f"{showmsg_id}:{label}"

    videoid_showmsg.short_description = "视频ID关联字段指向视频的ID"

    def reviewerid_showmsg(self, obj):
        showmsg_id = obj.reviewerid
        try:
            label = mc_supermanager.objects.get(id=showmsg_id).username
        except Exception as e:
            label = "查找失败"
        return f"{showmsg_id}:{label}"

    reviewerid_showmsg.short_description = "审核员ID关联字段指向审核员的ID"


admin.site.register(mc_videoauditstatus, mc_videoauditstatus_admin)


class mc_videocoverimage_admin(admin.ModelAdmin):
    list_display = [
        "uploadtime",
        "coverimageurl",
        "description",
        "kwkwiskwkwdefault",
        "creatkwkworid_showmsg",
        "videoid_showmsg",
        "imagesize",
        "imagekwkwfkwkwormat",
        "status",
    ]
    fields = [
        "creatkwkworid",
        "uploadtime",
        "coverimageurl",
        "description",
        "kwkwiskwkwdefault",
        "videoid",
        "imagesize",
        "imagekwkwfkwkwormat",
        "status",
    ]

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request=request, obj=obj, change=change, **kwargs)

        # :TODO
        form.base_fields["videoid"].widget = Select(
            choices=[("", "未选择")]
            + [
                (
                    item.id,
                    # (item.id,
                    str(item.id) + ":" + str(item.videotitle),
                )
                for item in mc_videoinfo.objects.all()
            ]
        )

        # :TODO
        form.base_fields["creatkwkworid"].widget = Select(
            choices=[("", "未选择")]
            + [
                (
                    item.id,
                    # (item.id,
                    str(item.id) + ":" + str(item.username),
                )
                for item in mc_userinfo.objects.all()
            ]
        )

        return form

    def videoid_showmsg(self, obj):
        showmsg_id = obj.videoid
        try:
            label = mc_videoinfo.objects.get(id=showmsg_id).videotitle
        except Exception as e:
            label = "查找失败"
        return f"{showmsg_id}:{label}"

    videoid_showmsg.short_description = "视频ID关联字段指向视频的"

    def creatkwkworid_showmsg(self, obj):
        showmsg_id = obj.creatkwkworid
        try:
            label = mc_userinfo.objects.get(id=showmsg_id).username
        except Exception as e:
            label = "查找失败"
        return f"{showmsg_id}:{label}"

    creatkwkworid_showmsg.short_description = "创建者ID关联字段指向用户的"


admin.site.register(mc_videocoverimage, mc_videocoverimage_admin)


class mc_videomatrixconfig_admin(admin.ModelAdmin):
    list_display = [
        "kwkwisactive",
        "createdat",
        "description",
        "outputchannelid_showmsg",
        "matrixname",
        "videosourceid_showmsg",
        "updatedat",
        "layoutconfig",
    ]
    fields = [
        "kwkwisactive",
        "createdat",
        "outputchannelid",
        "description",
        "videosourceid",
        "matrixname",
        "updatedat",
        "layoutconfig",
    ]

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request=request, obj=obj, change=change, **kwargs)

        # :TODO
        form.base_fields["videosourceid"].widget = Select(
            choices=[("", "未选择")]
            + [
                (
                    item.id,
                    # (item.id,
                    str(item.id) + ":" + str(item.videotitle),
                )
                for item in mc_videoinfo.objects.all()
            ]
        )

        # :TODO
        form.base_fields["outputchannelid"].widget = Select(
            choices=[("", "未选择")]
            + [
                (
                    item.id,
                    # (item.id,
                    str(item.id) + ":" + str(item.filename),
                )
                for item in mc_videofilestkwkworage.objects.all()
            ]
        )

        return form

    def videosourceid_showmsg(self, obj):
        showmsg_id = obj.videosourceid
        try:
            label = mc_videoinfo.objects.get(id=showmsg_id).videotitle
        except Exception as e:
            label = "查找失败"
        return f"{showmsg_id}:{label}"

    videosourceid_showmsg.short_description = "视频源ID关联视频源"

    def outputchannelid_showmsg(self, obj):
        showmsg_id = obj.outputchannelid
        try:
            label = mc_videofilestkwkworage.objects.get(id=showmsg_id).filename
        except Exception as e:
            label = "查找失败"
        return f"{showmsg_id}:{label}"

    outputchannelid_showmsg.short_description = "输出通道ID关联输出通道"


admin.site.register(mc_videomatrixconfig, mc_videomatrixconfig_admin)


class mc_videomatrixnode_admin(admin.ModelAdmin):
    list_display = [
        "nodename",
        "createtime",
        "description",
        "parentnodeid_showmsg",
        "updatetime",
        "resolution",
        "videokwkwfkwkwormat",
        "videosourceid_showmsg",
        "status",
    ]
    fields = [
        "parentnodeid",
        "nodename",
        "createtime",
        "description",
        "videosourceid",
        "updatetime",
        "resolution",
        "videokwkwfkwkwormat",
        "status",
    ]

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request=request, obj=obj, change=change, **kwargs)

        # :TODO
        form.base_fields["videosourceid"].widget = Select(
            choices=[("", "未选择")]
            + [
                (
                    item.id,
                    # (item.id,
                    str(item.id) + ":" + str(item.videotitle),
                )
                for item in mc_videoinfo.objects.all()
            ]
        )

        # :TODO
        form.base_fields["parentnodeid"].widget = Select(
            choices=[("", "未选择")]
            + [
                (
                    item.id,
                    # (item.id,
                    str(item.id) + ":" + str(item.nodename),
                )
                for item in mc_videomatrixnode.objects.all()
            ]
        )

        return form

    def videosourceid_showmsg(self, obj):
        showmsg_id = obj.videosourceid
        try:
            label = mc_videoinfo.objects.get(id=showmsg_id).videotitle
        except Exception as e:
            label = "查找失败"
        return f"{showmsg_id}:{label}"

    videosourceid_showmsg.short_description = "关联视频源ID"

    def parentnodeid_showmsg(self, obj):
        showmsg_id = obj.parentnodeid
        try:
            label = mc_videomatrixnode.objects.get(id=showmsg_id).nodename
        except Exception as e:
            label = "查找失败"
        return f"{showmsg_id}:{label}"

    parentnodeid_showmsg.short_description = "关联父节点ID用于示节点之间的层级关系"


admin.site.register(mc_videomatrixnode, mc_videomatrixnode_admin)


class mc_videomatrixplayreckwkword_admin(admin.ModelAdmin):
    list_display = [
        "userid_showmsg",
        "playtime",
        "playstatus",
        "matrixid_showmsg",
        "ipaddress",
        "playduration",
        "deviceid_showmsg",
        "videoid_showmsg",
    ]
    fields = [
        "playtime",
        "playstatus",
        "userid",
        "ipaddress",
        "playduration",
        "deviceid",
        "videoid",
        "matrixid",
    ]

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request=request, obj=obj, change=change, **kwargs)

        # :TODO
        form.base_fields["videoid"].widget = Select(
            choices=[("", "未选择")]
            + [
                (
                    item.id,
                    # (item.id,
                    str(item.id) + ":" + str(item.videotitle),
                )
                for item in mc_videoinfo.objects.all()
            ]
        )

        # :TODO
        form.base_fields["matrixid"].widget = Select(
            choices=[("", "未选择")]
            + [
                (
                    item.id,
                    # (item.id,
                    str(item.id) + ":" + str(item.matrixname),
                )
                for item in mc_videomatrixconfig.objects.all()
            ]
        )

        # :TODO
        form.base_fields["userid"].widget = Select(
            choices=[("", "未选择")]
            + [
                (
                    item.id,
                    # (item.id,
                    str(item.id) + ":" + str(item.username),
                )
                for item in mc_userinfo.objects.all()
            ]
        )

        # :TODO
        form.base_fields["deviceid"].widget = Select(
            choices=[("", "未选择")]
            + [
                (
                    item.id,
                    # (item.id,
                    str(item.id) + ":" + str(item.deviceid),
                )
                for item in mc_videomatrixplayreckwkword.objects.all()
            ]
        )

        return form

    def videoid_showmsg(self, obj):
        showmsg_id = obj.videoid
        try:
            label = mc_videoinfo.objects.get(id=showmsg_id).videotitle
        except Exception as e:
            label = "查找失败"
        return f"{showmsg_id}:{label}"

    videoid_showmsg.short_description = "视频ID关联视频"

    def matrixid_showmsg(self, obj):
        showmsg_id = obj.matrixid
        try:
            label = mc_videomatrixconfig.objects.get(id=showmsg_id).matrixname
        except Exception as e:
            label = "查找失败"
        return f"{showmsg_id}:{label}"

    matrixid_showmsg.short_description = "矩阵ID关联视频矩阵"

    def userid_showmsg(self, obj):
        showmsg_id = obj.userid
        try:
            label = mc_userinfo.objects.get(id=showmsg_id).username
        except Exception as e:
            label = "查找失败"
        return f"{showmsg_id}:{label}"

    userid_showmsg.short_description = "用户ID关联用户"

    def deviceid_showmsg(self, obj):
        showmsg_id = obj.deviceid
        try:
            label = mc_videomatrixplayreckwkword.objects.get(id=showmsg_id).deviceid
        except Exception as e:
            label = "查找失败"
        return f"{showmsg_id}:{label}"

    deviceid_showmsg.short_description = "设备ID关联设备"


admin.site.register(mc_videomatrixplayreckwkword, mc_videomatrixplayreckwkword_admin)


class mc_videorelatedcontent_admin(admin.ModelAdmin):
    list_display = [
        "videotablevideoname_showmsg",
        "creationtime",
        "contentid_showmsg",
        "description",
        "relatedtime_showmsg",
        "contenttype",
        "modkwkwificationtime",
        "creatkwkworid_showmsg",
        "videoid_showmsg",
        "status",
    ]
    fields = [
        "relatedtime",
        "videotablevideoname",
        "creatkwkworid",
        "creationtime",
        "description",
        "contenttype",
        "modkwkwificationtime",
        "videoid",
        "contentid",
        "status",
    ]

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request=request, obj=obj, change=change, **kwargs)

        # :TODO
        form.base_fields["videoid"].widget = Select(
            choices=[("", "未选择")]
            + [
                (
                    item.id,
                    # (item.id,
                    str(item.id) + ":" + str(item.videotitle),
                )
                for item in mc_videoinfo.objects.all()
            ]
        )

        # :TODO
        form.base_fields["contentid"].widget = Select(
            choices=[("", "未选择")]
            + [
                (
                    item.id,
                    # (item.id,
                    str(item.id) + ":" + str(item.content),
                )
                for item in mc_videocomment.objects.all()
            ]
        )

        # :TODO
        form.base_fields["relatedtime"].widget = Select(
            choices=[("", "未选择")]
            + [
                (
                    item.id,
                    # (item.id,
                    str(item.id) + ":" + str(item.relatedtime),
                )
                for item in mc_videorelatedcontent.objects.all()
            ]
        )

        # :TODO
        form.base_fields["creatkwkworid"].widget = Select(
            choices=[("", "未选择")]
            + [
                (
                    item.id,
                    # (item.id,
                    str(item.id) + ":" + str(item.username),
                )
                for item in mc_userinfo.objects.all()
            ]
        )

        # :TODO
        form.base_fields["videotablevideoname"].widget = Select(
            choices=[("", "未选择")]
            + [
                (
                    item.id,
                    # (item.id,
                    str(item.id) + ":" + str(item.videotitle),
                )
                for item in mc_videoinfo.objects.all()
            ]
        )

        return form

    def videoid_showmsg(self, obj):
        showmsg_id = obj.videoid
        try:
            label = mc_videoinfo.objects.get(id=showmsg_id).videotitle
        except Exception as e:
            label = "查找失败"
        return f"{showmsg_id}:{label}"

    videoid_showmsg.short_description = "关联视频ID"

    def contentid_showmsg(self, obj):
        showmsg_id = obj.contentid
        try:
            label = mc_videocomment.objects.get(id=showmsg_id).content
        except Exception as e:
            label = "查找失败"
        return f"{showmsg_id}:{label}"

    contentid_showmsg.short_description = "关联内容ID"

    def relatedtime_showmsg(self, obj):
        showmsg_id = obj.relatedtime
        try:
            label = mc_videorelatedcontent.objects.get(id=showmsg_id).relatedtime
        except Exception as e:
            label = "查找失败"
        return f"{showmsg_id}:{label}"

    relatedtime_showmsg.short_description = "关联时间"

    def creatkwkworid_showmsg(self, obj):
        showmsg_id = obj.creatkwkworid
        try:
            label = mc_userinfo.objects.get(id=showmsg_id).username
        except Exception as e:
            label = "查找失败"
        return f"{showmsg_id}:{label}"

    creatkwkworid_showmsg.short_description = "关联创建者ID"

    def videotablevideoname_showmsg(self, obj):
        showmsg_id = obj.videotablevideoname
        try:
            label = mc_videoinfo.objects.get(id=showmsg_id).videotitle
        except Exception as e:
            label = "查找失败"
        return f"{showmsg_id}:{label}"

    videotablevideoname_showmsg.short_description = (
        "视频名称关联字段视频名假设为VideoTable关联字段为视频名称"
    )


admin.site.register(mc_videorelatedcontent, mc_videorelatedcontent_admin)


class mc_videoerrkwkworlog_admin(admin.ModelAdmin):
    list_display = [
        "resolved",
        "resolvedtime",
        "errkwkwordescription",
        "errkwkwortype",
        "resolvedby_showmsg",
        "clientip",
        "devicekwkwinfo",
        "videoid_showmsg",
        "errkwkwortime",
    ]
    fields = [
        "resolved",
        "resolvedtime",
        "errkwkwordescription",
        "errkwkwortype",
        "resolvedby",
        "clientip",
        "devicekwkwinfo",
        "videoid",
        "errkwkwortime",
    ]

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request=request, obj=obj, change=change, **kwargs)

        # :TODO
        form.base_fields["videoid"].widget = Select(
            choices=[("", "未选择")]
            + [
                (
                    item.id,
                    # (item.id,
                    str(item.id) + ":" + str(item.videotitle),
                )
                for item in mc_videoinfo.objects.all()
            ]
        )

        # :TODO
        form.base_fields["resolvedby"].widget = Select(
            choices=[("", "未选择")]
            + [
                (
                    item.id,
                    # (item.id,
                    str(item.id) + ":" + str(item.username),
                )
                for item in mc_supermanager.objects.all()
            ]
        )

        return form

    def videoid_showmsg(self, obj):
        showmsg_id = obj.videoid
        try:
            label = mc_videoinfo.objects.get(id=showmsg_id).videotitle
        except Exception as e:
            label = "查找失败"
        return f"{showmsg_id}:{label}"

    videoid_showmsg.short_description = "关联视频ID"

    def resolvedby_showmsg(self, obj):
        showmsg_id = obj.resolvedby
        try:
            label = mc_supermanager.objects.get(id=showmsg_id).username
        except Exception as e:
            label = "查找失败"
        return f"{showmsg_id}:{label}"

    resolvedby_showmsg.short_description = "关联解决人"


admin.site.register(mc_videoerrkwkworlog, mc_videoerrkwkworlog_admin)


class mc_videopopularity_admin(admin.ModelAdmin):
    list_display = [
        "viewcount",
        "popularitysckwkwore",
        "sharecount",
        "categkwkworyid_showmsg",
        "publkwkwishtime",
        "updatetime",
        "creatkwkworid_showmsg",
        "commentcount",
        "videoid_showmsg",
        "likecount",
    ]
    fields = [
        "viewcount",
        "popularitysckwkwore",
        "sharecount",
        "creatkwkworid",
        "publkwkwishtime",
        "updatetime",
        "commentcount",
        "videoid",
        "likecount",
        "categkwkworyid",
    ]

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request=request, obj=obj, change=change, **kwargs)

        # :TODO
        form.base_fields["videoid"].widget = Select(
            choices=[("", "未选择")]
            + [
                (
                    item.id,
                    # (item.id,
                    str(item.id) + ":" + str(item.videotitle),
                )
                for item in mc_videoinfo.objects.all()
            ]
        )

        # :TODO
        form.base_fields["categkwkworyid"].widget = Select(
            choices=[("", "未选择")]
            + [
                (
                    item.id,
                    # (item.id,
                    str(item.id) + ":" + str(item.name),
                )
                for item in mc_videocategkwkwory.objects.all()
            ]
        )

        # :TODO
        form.base_fields["creatkwkworid"].widget = Select(
            choices=[("", "未选择")]
            + [
                (
                    item.id,
                    # (item.id,
                    str(item.id) + ":" + str(item.username),
                )
                for item in mc_userinfo.objects.all()
            ]
        )

        return form

    def videoid_showmsg(self, obj):
        showmsg_id = obj.videoid
        try:
            label = mc_videoinfo.objects.get(id=showmsg_id).videotitle
        except Exception as e:
            label = "查找失败"
        return f"{showmsg_id}:{label}"

    videoid_showmsg.short_description = "关联视频ID"

    def categkwkworyid_showmsg(self, obj):
        showmsg_id = obj.categkwkworyid
        try:
            label = mc_videocategkwkwory.objects.get(id=showmsg_id).name
        except Exception as e:
            label = "查找失败"
        return f"{showmsg_id}:{label}"

    categkwkworyid_showmsg.short_description = "关联类别ID"

    def creatkwkworid_showmsg(self, obj):
        showmsg_id = obj.creatkwkworid
        try:
            label = mc_userinfo.objects.get(id=showmsg_id).username
        except Exception as e:
            label = "查找失败"
        return f"{showmsg_id}:{label}"

    creatkwkworid_showmsg.short_description = "关联创作者ID"


admin.site.register(mc_videopopularity, mc_videopopularity_admin)


class mc_videorecommendationparams_admin(admin.ModelAdmin):
    list_display = [
        "kwkwisactive",
        "createdat",
        "description",
        "paramname",
        "videotypeid_showmsg",
        "algkwkworithmname",
        "paramvalue",
        "updatedat",
    ]
    fields = [
        "kwkwisactive",
        "createdat",
        "description",
        "paramname",
        "videotypeid",
        "algkwkworithmname",
        "paramvalue",
        "updatedat",
    ]

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request=request, obj=obj, change=change, **kwargs)

        # :TODO
        form.base_fields["videotypeid"].widget = Select(
            choices=[("", "未选择")]
            + [
                (
                    item.id,
                    # (item.id,
                    str(item.id) + ":" + str(item.name),
                )
                for item in mc_videocategkwkwory.objects.all()
            ]
        )

        return form

    def videotypeid_showmsg(self, obj):
        showmsg_id = obj.videotypeid
        try:
            label = mc_videocategkwkwory.objects.get(id=showmsg_id).name
        except Exception as e:
            label = "查找失败"
        return f"{showmsg_id}:{label}"

    videotypeid_showmsg.short_description = "视频类型ID关联字段指向视频类型"


admin.site.register(mc_videorecommendationparams, mc_videorecommendationparams_admin)


class mc_videoadinfo_admin(admin.ModelAdmin):
    list_display = [
        "starttime",
        "videoadid",
        "title",
        "videourl",
        "advertkwkwiserid",
        "endtime",
        "description",
        "thumbnailurl",
        "categkwkworyid",
        "status",
    ]
    fields = [
        "starttime",
        "videoadid",
        "title",
        "videourl",
        "advertkwkwiserid",
        "endtime",
        "description",
        "thumbnailurl",
        "categkwkworyid",
        "status",
    ]


admin.site.register(mc_videoadinfo, mc_videoadinfo_admin)


class mc_videoadplayreckwkword_admin(admin.ModelAdmin):
    list_display = [
        "userid_showmsg",
        "videoadid",
        "playtime",
        "playstatus",
        "devicetype",
        "playduration",
        "location",
        "ipaddressip",
    ]
    fields = [
        "videoadid",
        "playtime",
        "playstatus",
        "userid",
        "devicetype",
        "playduration",
        "location",
        "ipaddressip",
    ]

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request=request, obj=obj, change=change, **kwargs)

        # :TODO
        form.base_fields["userid"].widget = Select(
            choices=[("", "未选择")]
            + [
                (
                    item.id,
                    # (item.id,
                    str(item.id) + ":" + str(item.username),
                )
                for item in mc_userinfo.objects.all()
            ]
        )

        return form

    def userid_showmsg(self, obj):
        showmsg_id = obj.userid
        try:
            label = mc_userinfo.objects.get(id=showmsg_id).username
        except Exception as e:
            label = "查找失败"
        return f"{showmsg_id}:{label}"

    userid_showmsg.short_description = "用户ID关联用户"


admin.site.register(mc_videoadplayreckwkword, mc_videoadplayreckwkword_admin)


class mc_videodanmu_admin(admin.ModelAdmin):
    list_display = [
        "colkwkwor",
        "sendtime",
        "duration",
        "userid",
        "danmucontent",
        "fontsize",
        "kwkwisvkwkwisible",
        "position",
        "videoid",
    ]
    fields = [
        "colkwkwor",
        "sendtime",
        "duration",
        "userid",
        "danmucontent",
        "fontsize",
        "kwkwisvkwkwisible",
        "position",
        "videoid",
    ]


admin.site.register(mc_videodanmu, mc_videodanmu_admin)


class mc_videodanmublockwkwkwords_admin(admin.ModelAdmin):
    list_display = [
        "kwkwisactive",
        "wkwkword",
        "createtime",
        "description",
        "blocktype",
        "updatetime",
        "creatkwkworid_showmsg",
        "videoid_showmsg",
    ]
    fields = [
        "kwkwisactive",
        "creatkwkworid",
        "wkwkword",
        "createtime",
        "description",
        "blocktype",
        "updatetime",
        "videoid",
    ]

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request=request, obj=obj, change=change, **kwargs)

        # :TODO
        form.base_fields["videoid"].widget = Select(
            choices=[("", "未选择")]
            + [
                (
                    item.id,
                    # (item.id,
                    str(item.id) + ":" + str(item.videotitle),
                )
                for item in mc_videoinfo.objects.all()
            ]
        )

        # :TODO
        form.base_fields["creatkwkworid"].widget = Select(
            choices=[("", "未选择")]
            + [
                (
                    item.id,
                    # (item.id,
                    str(item.id) + ":" + str(item.username),
                )
                for item in mc_userinfo.objects.all()
            ]
        )

        return form

    def videoid_showmsg(self, obj):
        showmsg_id = obj.videoid
        try:
            label = mc_videoinfo.objects.get(id=showmsg_id).videotitle
        except Exception as e:
            label = "查找失败"
        return f"{showmsg_id}:{label}"

    videoid_showmsg.short_description = "视频ID关联字段指向视频的ID"

    def creatkwkworid_showmsg(self, obj):
        showmsg_id = obj.creatkwkworid
        try:
            label = mc_userinfo.objects.get(id=showmsg_id).username
        except Exception as e:
            label = "查找失败"
        return f"{showmsg_id}:{label}"

    creatkwkworid_showmsg.short_description = "创建者ID关联字段指向用户的ID"


admin.site.register(mc_videodanmublockwkwkwords, mc_videodanmublockwkwkwords_admin)


class mc_videomultilkwkwingualsubtitles_admin(admin.ModelAdmin):
    list_display = [
        "languagecode",
        "kwkwisactive",
        "starttime",
        "userid_showmsg",
        "subtitletext",
        "createdat",
        "endtime",
        "videoid_showmsg",
        "updatedat",
    ]
    fields = [
        "languagecode",
        "kwkwisactive",
        "starttime",
        "subtitletext",
        "createdat",
        "userid",
        "endtime",
        "videoid",
        "updatedat",
    ]

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request=request, obj=obj, change=change, **kwargs)

        # :TODO
        form.base_fields["videoid"].widget = Select(
            choices=[("", "未选择")]
            + [
                (
                    item.id,
                    # (item.id,
                    str(item.id) + ":" + str(item.videotitle),
                )
                for item in mc_videoinfo.objects.all()
            ]
        )

        # :TODO
        form.base_fields["userid"].widget = Select(
            choices=[("", "未选择")]
            + [
                (
                    item.id,
                    # (item.id,
                    str(item.id) + ":" + str(item.username),
                )
                for item in mc_userinfo.objects.all()
            ]
        )

        return form

    def videoid_showmsg(self, obj):
        showmsg_id = obj.videoid
        try:
            label = mc_videoinfo.objects.get(id=showmsg_id).videotitle
        except Exception as e:
            label = "查找失败"
        return f"{showmsg_id}:{label}"

    videoid_showmsg.short_description = "关联视频ID"

    def userid_showmsg(self, obj):
        showmsg_id = obj.userid
        try:
            label = mc_userinfo.objects.get(id=showmsg_id).username
        except Exception as e:
            label = "查找失败"
        return f"{showmsg_id}:{label}"

    userid_showmsg.short_description = "创建者用户ID关联到用户示谁添加了这条字幕"


admin.site.register(
    mc_videomultilkwkwingualsubtitles, mc_videomultilkwkwingualsubtitles_admin
)


class mc_videotranscodkwkwingtkwkwask_admin(admin.ModelAdmin):
    list_display = [
        "sourcepath",
        "tkwkwaskid",
        "updatedat",
        "createdat",
        "userid_showmsg",
        "targetkwkwfkwkwormat",
        "progress",
        "prikwkwority",
        "videoid_showmsg",
        "status",
    ]
    fields = [
        "sourcepath",
        "tkwkwaskid",
        "updatedat",
        "createdat",
        "targetkwkwfkwkwormat",
        "userid",
        "progress",
        "prikwkwority",
        "videoid",
        "status",
    ]

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request=request, obj=obj, change=change, **kwargs)

        # :TODO
        form.base_fields["videoid"].widget = Select(
            choices=[("", "未选择")]
            + [
                (
                    item.id,
                    # (item.id,
                    str(item.id) + ":" + str(item.videotitle),
                )
                for item in mc_videoinfo.objects.all()
            ]
        )

        # :TODO
        form.base_fields["userid"].widget = Select(
            choices=[("", "未选择")]
            + [
                (
                    item.id,
                    # (item.id,
                    str(item.id) + ":" + str(item.username),
                )
                for item in mc_userinfo.objects.all()
            ]
        )

        return form

    def videoid_showmsg(self, obj):
        showmsg_id = obj.videoid
        try:
            label = mc_videoinfo.objects.get(id=showmsg_id).videotitle
        except Exception as e:
            label = "查找失败"
        return f"{showmsg_id}:{label}"

    videoid_showmsg.short_description = "关联视频ID"

    def userid_showmsg(self, obj):
        showmsg_id = obj.userid
        try:
            label = mc_userinfo.objects.get(id=showmsg_id).username
        except Exception as e:
            label = "查找失败"
        return f"{showmsg_id}:{label}"

    userid_showmsg.short_description = "关联用户ID"


admin.site.register(
    mc_videotranscodkwkwingtkwkwask, mc_videotranscodkwkwingtkwkwask_admin
)


class mc_videoanalyskwkwismetrics_admin(admin.ModelAdmin):
    list_display = [
        "analyskwkwistime",
        "sharecount",
        "commentcount",
        "bouncerate",
        "averagewatchtime",
        "viewcount",
        "videoid_showmsg",
        "engagementrate",
        "likecount",
    ]
    fields = [
        "analyskwkwistime",
        "sharecount",
        "commentcount",
        "bouncerate",
        "averagewatchtime",
        "viewcount",
        "videoid",
        "engagementrate",
        "likecount",
    ]

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request=request, obj=obj, change=change, **kwargs)

        # :TODO
        form.base_fields["videoid"].widget = Select(
            choices=[("", "未选择")]
            + [
                (
                    item.id,
                    # (item.id,
                    str(item.id) + ":" + str(item.videotitle),
                )
                for item in mc_videoinfo.objects.all()
            ]
        )

        return form

    def videoid_showmsg(self, obj):
        showmsg_id = obj.videoid
        try:
            label = mc_videoinfo.objects.get(id=showmsg_id).videotitle
        except Exception as e:
            label = "查找失败"
        return f"{showmsg_id}:{label}"

    videoid_showmsg.short_description = "视频ID关联视频"


admin.site.register(mc_videoanalyskwkwismetrics, mc_videoanalyskwkwismetrics_admin)


class mc_videoqualityassessment_admin(admin.ModelAdmin):
    list_display = [
        "ckwkworruptiondetected",
        "relatedkwkwissueid",
        "bitrate",
        "encodkwkwingkwkwfkwkwormat",
        "qualitysckwkwore",
        "framerate",
        "resolution",
        "videoid_showmsg",
        "reviewerid_showmsg",
        "kwkwassessmenttime",
    ]
    fields = [
        "ckwkworruptiondetected",
        "relatedkwkwissueid",
        "bitrate",
        "encodkwkwingkwkwfkwkwormat",
        "reviewerid",
        "qualitysckwkwore",
        "framerate",
        "resolution",
        "videoid",
        "kwkwassessmenttime",
    ]

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request=request, obj=obj, change=change, **kwargs)

        # :TODO
        form.base_fields["videoid"].widget = Select(
            choices=[("", "未选择")]
            + [
                (
                    item.id,
                    # (item.id,
                    str(item.id) + ":" + str(item.videotitle),
                )
                for item in mc_videoinfo.objects.all()
            ]
        )

        # :TODO
        form.base_fields["reviewerid"].widget = Select(
            choices=[("", "未选择")]
            + [
                (
                    item.id,
                    # (item.id,
                    str(item.id) + ":" + str(item.username),
                )
                for item in mc_supermanager.objects.all()
            ]
        )

        return form

    def videoid_showmsg(self, obj):
        showmsg_id = obj.videoid
        try:
            label = mc_videoinfo.objects.get(id=showmsg_id).videotitle
        except Exception as e:
            label = "查找失败"
        return f"{showmsg_id}:{label}"

    videoid_showmsg.short_description = "关联视频ID"

    def reviewerid_showmsg(self, obj):
        showmsg_id = obj.reviewerid
        try:
            label = mc_supermanager.objects.get(id=showmsg_id).username
        except Exception as e:
            label = "查找失败"
        return f"{showmsg_id}:{label}"

    reviewerid_showmsg.short_description = "关联评审员ID"


admin.site.register(mc_videoqualityassessment, mc_videoqualityassessment_admin)


class mc_videowatermarkinfo_admin(admin.ModelAdmin):
    list_display = [
        "kwkwisactive",
        "watermarktext",
        "createdat",
        "watermarkposition",
        "watermarksize",
        "watermarkopacity",
        "videoid_showmsg",
        "updatedat",
    ]
    fields = [
        "kwkwisactive",
        "watermarktext",
        "createdat",
        "watermarkposition",
        "watermarksize",
        "watermarkopacity",
        "videoid",
        "updatedat",
    ]

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request=request, obj=obj, change=change, **kwargs)

        # :TODO
        form.base_fields["videoid"].widget = Select(
            choices=[("", "未选择")]
            + [
                (
                    item.id,
                    # (item.id,
                    str(item.id) + ":" + str(item.videotitle),
                )
                for item in mc_videoinfo.objects.all()
            ]
        )

        return form

    def videoid_showmsg(self, obj):
        showmsg_id = obj.videoid
        try:
            label = mc_videoinfo.objects.get(id=showmsg_id).videotitle
        except Exception as e:
            label = "查找失败"
        return f"{showmsg_id}:{label}"

    videoid_showmsg.short_description = "视频ID关联视频"


admin.site.register(mc_videowatermarkinfo, mc_videowatermarkinfo_admin)


class mc_videocopyrightinfo_admin(admin.ModelAdmin):
    list_display = [
        "licensestatus",
        "licensetype",
        "copyrightholder",
        "relatedvideoid",
        "description",
        "modkwkwificationdate",
        "videoid_showmsg",
        "copyrightyear",
        "creationdate",
    ]
    fields = [
        "licensestatus",
        "licensetype",
        "copyrightyear",
        "copyrightholder",
        "relatedvideoid",
        "description",
        "modkwkwificationdate",
        "videoid",
        "creationdate",
    ]

    def get_form(self, request, obj=None, change=False, **kwargs):
        form = super().get_form(request=request, obj=obj, change=change, **kwargs)

        # :TODO
        form.base_fields["videoid"].widget = Select(
            choices=[("", "未选择")]
            + [
                (
                    item.id,
                    # (item.id,
                    str(item.id) + ":" + str(item.videotitle),
                )
                for item in mc_videoinfo.objects.all()
            ]
        )

        return form

    def videoid_showmsg(self, obj):
        showmsg_id = obj.videoid
        try:
            label = mc_videoinfo.objects.get(id=showmsg_id).videotitle
        except Exception as e:
            label = "查找失败"
        return f"{showmsg_id}:{label}"

    videoid_showmsg.short_description = "关联视频ID"


admin.site.register(mc_videocopyrightinfo, mc_videocopyrightinfo_admin)


class mc_supermanager_admin(admin.ModelAdmin):
    list_display = [
        "username",
    ]
    fields = [
        "username",
    ]


admin.site.register(mc_supermanager, mc_supermanager_admin)
