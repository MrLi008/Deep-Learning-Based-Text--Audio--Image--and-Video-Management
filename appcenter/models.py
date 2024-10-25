from django.db import models


# Create your models here.


class MyModal(models.Model):
    class Meta:
        abstract = True

    def toParams(self):
        """
        遍历属性名
        :return:
        """
        return self._meta.fields

    def toImplement(self):
        """用于接口开发"""
        return "<br/>".join(
            [f"{field.name}, {field.verbose_name}" for field in self._meta.fields]
        )

    def toParams_zh(self):
        return [field.verbose_name for field in self._meta.fields]

    def toParams_en(self):
        return [field.name for field in self._meta.fields]

    def toVue(self):
        res = {field.name: getattr(self, field.name, "") for field in self.toParams()}
        if res["id"] == "":
            del res["id"]
        return res

    def toValues(self):
        """
        遍历值
        :return:
        """
        return [getattr(self, field.name) for field in self._meta.fields]

    def toJson(self):
        return {
            field.name: value for field, value in zip(self.toParams(), self.toValues())
        }

    def toMeta(self):
        return {
            "table": {
                "mctablenameen": self._meta.db_table,
                "mctablenamezh": self._meta.verbose_name,
            },
            "field": self.toParams(),
            "field_count": len(self.toParams()),
        }


class mc_videoinfo(MyModal):
    id = models.BigAutoField(primary_key=True)
    videoid = models.CharField(
        max_length=200,
        verbose_name="视频ID",
        auto_created=True,
        null=True,
        blank=True,
        unique=False,
    )
    videotitle = models.CharField(
        verbose_name="视频标题",
        max_length=915,
        null=True,
        blank=True,
        unique=False,
    )
    videodescription = models.TextField(
        verbose_name="视频描述",
        null=True,
        blank=True,
        unique=False,
    )
    uploadtime = models.DateTimeField(
        verbose_name="上传时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    duration = models.CharField(
        verbose_name="视频时长秒",
        max_length=720,
        null=True,
        blank=True,
        unique=False,
    )
    resolution = models.CharField(
        verbose_name="视频分辨率",
        max_length=760,
        null=True,
        blank=True,
        unique=False,
    )
    filetype = models.FileField(
        verbose_name="文件类型",
        upload_to="57905",
        null=True,
        blank=True,
        unique=False,
    )
    filesize = models.FileField(
        verbose_name="文件大小KBMBGB",
        upload_to="57906",
        null=True,
        blank=True,
        unique=False,
    )
    creatkwkworid = models.CharField(
        verbose_name="创建者ID关联用户",
        max_length=515,
        null=True,
        blank=True,
        unique=False,
    )
    categkwkworyid = models.CharField(
        verbose_name="类别ID关联视频类别",
        max_length=675,
        null=True,
        blank=True,
        unique=False,
    )

    def toJson(self):
        res = super().toJson()

        if self.filetype:
            res["filetype"] = {
                "name": self.filetype.name,
                "url": self.filetype.url,
            }
        else:
            res["filetype"] = None

        if self.filesize:
            res["filesize"] = {
                "name": self.filesize.name,
                "url": self.filesize.url,
            }
        else:
            res["filesize"] = None

        if self.videoid:
            res["videoid"] = str(self.videoid)
            # 可在此补充对外键内容的关联查询，因性能要求暂时去掉了，如果需要的话直接在这儿加就行,具体方法查看开发说明文档

        if self.uploadtime:
            res["uploadtime"] = str(self.uploadtime)
            # 可在此补充对外键内容的关联查询，因性能要求暂时去掉了，如果需要的话直接在这儿加就行,具体方法查看开发说明文档

        return res

    class Meta:
        managed = True
        db_table = "videoinfo"
        verbose_name = "视频信息表"
        verbose_name_plural = verbose_name


class mc_videocategkwkwory(MyModal):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(
        verbose_name="分类名称",
        max_length=790,
        null=True,
        blank=True,
        unique=False,
    )
    description = models.TextField(
        verbose_name="分类描述",
        null=True,
        blank=True,
        unique=False,
    )
    parentid = models.CharField(
        max_length=200,
        verbose_name="父分类ID用于构建分类层级如果为顶级分类则为NULL",
        auto_created=True,
        null=True,
        blank=True,
        unique=False,
    )
    createtime = models.DateTimeField(
        verbose_name="创建时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    updatetime = models.DateTimeField(
        verbose_name="更新时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    kwkwisactive = models.BooleanField(
        verbose_name="是否激活用于控制分类是否显示在前端",
        null=True,
        blank=True,
        unique=False,
    )
    skwkwortorder = models.CharField(
        verbose_name="排序顺序",
        max_length=750,
        null=True,
        blank=True,
        unique=False,
    )

    def toJson(self):
        res = super().toJson()

        if self.parentid:
            res["parentid"] = str(self.parentid)
            # 可在此补充对外键内容的关联查询，因性能要求暂时去掉了，如果需要的话直接在这儿加就行,具体方法查看开发说明文档

        if self.createtime:
            res["createtime"] = str(self.createtime)
            # 可在此补充对外键内容的关联查询，因性能要求暂时去掉了，如果需要的话直接在这儿加就行,具体方法查看开发说明文档

        if self.updatetime:
            res["updatetime"] = str(self.updatetime)
            # 可在此补充对外键内容的关联查询，因性能要求暂时去掉了，如果需要的话直接在这儿加就行,具体方法查看开发说明文档

        return res

    class Meta:
        managed = True
        db_table = "videocategkwkwory"
        verbose_name = "视频分类表"
        verbose_name_plural = verbose_name


class mc_videotag(MyModal):
    id = models.BigAutoField(primary_key=True)
    tagid = models.CharField(
        max_length=200,
        verbose_name="标签ID",
        auto_created=True,
        null=True,
        blank=True,
        unique=False,
    )
    tagname = models.CharField(
        verbose_name="标签名称",
        max_length=975,
        null=True,
        blank=True,
        unique=False,
    )
    videoid = models.CharField(
        verbose_name="视频ID关联字段指向视频中的视频ID",
        max_length=540,
        null=True,
        blank=True,
        unique=False,
    )
    createtime = models.DateTimeField(
        verbose_name="创建时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    updatetime = models.DateTimeField(
        verbose_name="更新时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    kwkwisactive = models.BooleanField(
        verbose_name="是否激活用于标记标签是否可用",
        null=True,
        blank=True,
        unique=False,
    )
    description = models.TextField(
        verbose_name="标签描述",
        null=True,
        blank=True,
        unique=False,
    )
    creatkwkworid = models.CharField(
        verbose_name="创建者ID关联字段指向用户中的用户ID",
        max_length=430,
        null=True,
        blank=True,
        unique=False,
    )

    def toJson(self):
        res = super().toJson()

        if self.tagid:
            res["tagid"] = str(self.tagid)
            # 可在此补充对外键内容的关联查询，因性能要求暂时去掉了，如果需要的话直接在这儿加就行,具体方法查看开发说明文档

        if self.createtime:
            res["createtime"] = str(self.createtime)
            # 可在此补充对外键内容的关联查询，因性能要求暂时去掉了，如果需要的话直接在这儿加就行,具体方法查看开发说明文档

        if self.updatetime:
            res["updatetime"] = str(self.updatetime)
            # 可在此补充对外键内容的关联查询，因性能要求暂时去掉了，如果需要的话直接在这儿加就行,具体方法查看开发说明文档

        return res

    class Meta:
        managed = True
        db_table = "videotag"
        verbose_name = "视频标签表"
        verbose_name_plural = verbose_name


class mc_videofilestkwkworage(MyModal):
    id = models.BigAutoField(primary_key=True)
    videoid = models.CharField(
        max_length=200,
        verbose_name="视频ID",
        auto_created=True,
        null=True,
        blank=True,
        unique=False,
    )
    filename = models.FileField(
        verbose_name="文件名",
        upload_to="57925",
        null=True,
        blank=True,
        unique=False,
    )
    filepath = models.FileField(
        verbose_name="文件存储路径",
        upload_to="57926",
        null=True,
        blank=True,
        unique=False,
    )
    filesize = models.FileField(
        verbose_name="文件大小单位MB",
        upload_to="57927",
        null=True,
        blank=True,
        unique=False,
    )
    uploadtime = models.DateTimeField(
        verbose_name="上传时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    duration = models.CharField(
        verbose_name="视频时长单位秒",
        max_length=550,
        null=True,
        blank=True,
        unique=False,
    )
    resolution = models.CharField(
        verbose_name="分辨率例如1920x1080",
        max_length=630,
        null=True,
        blank=True,
        unique=False,
    )
    kwkwfkwkwormat = models.CharField(
        verbose_name="视频格式例如mp4",
        max_length=600,
        null=True,
        blank=True,
        unique=False,
    )
    creatkwkworid = models.CharField(
        verbose_name="创建者ID关联用户",
        max_length=890,
        null=True,
        blank=True,
        unique=False,
    )
    categkwkworyid = models.CharField(
        verbose_name="分类ID关联视频分类",
        max_length=900,
        null=True,
        blank=True,
        unique=False,
    )

    def toJson(self):
        res = super().toJson()

        if self.filename:
            res["filename"] = {
                "name": self.filename.name,
                "url": self.filename.url,
            }
        else:
            res["filename"] = None

        if self.filepath:
            res["filepath"] = {
                "name": self.filepath.name,
                "url": self.filepath.url,
            }
        else:
            res["filepath"] = None

        if self.filesize:
            res["filesize"] = {
                "name": self.filesize.name,
                "url": self.filesize.url,
            }
        else:
            res["filesize"] = None

        if self.videoid:
            res["videoid"] = str(self.videoid)
            # 可在此补充对外键内容的关联查询，因性能要求暂时去掉了，如果需要的话直接在这儿加就行,具体方法查看开发说明文档

        if self.uploadtime:
            res["uploadtime"] = str(self.uploadtime)
            # 可在此补充对外键内容的关联查询，因性能要求暂时去掉了，如果需要的话直接在这儿加就行,具体方法查看开发说明文档

        return res

    class Meta:
        managed = True
        db_table = "videofilestkwkworage"
        verbose_name = "视频文件存储表"
        verbose_name_plural = verbose_name


class mc_videoplayreckwkword(MyModal):
    id = models.BigAutoField(primary_key=True)
    videoid = models.CharField(
        verbose_name="视频ID关联视频信息",
        max_length=835,
        null=True,
        blank=True,
        unique=False,
    )
    userid = models.CharField(
        verbose_name="用户ID关联用户信息",
        max_length=805,
        null=True,
        blank=True,
        unique=False,
    )
    playstarttime = models.DateTimeField(
        verbose_name="播放开始时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    playendtime = models.DateTimeField(
        verbose_name="播放结束时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    playduration = models.CharField(
        verbose_name="播放时长秒",
        max_length=710,
        null=True,
        blank=True,
        unique=False,
    )
    playstatus = models.CharField(
        verbose_name="播放状态如已完成、暂停、中断",
        max_length=565,
        null=True,
        blank=True,
        unique=False,
    )
    devicetype = models.CharField(
        verbose_name="设备类型如手机、平板、电脑",
        max_length=785,
        null=True,
        blank=True,
        unique=False,
    )
    ipaddress = models.TextField(
        verbose_name="IP地址",
        null=True,
        blank=True,
        unique=False,
    )
    location = models.CharField(
        verbose_name="播放位置可选根据IP解析的地理位置",
        max_length=515,
        null=True,
        blank=True,
        unique=False,
    )

    def toJson(self):
        res = super().toJson()

        if self.playstarttime:
            res["playstarttime"] = str(self.playstarttime)
            # 可在此补充对外键内容的关联查询，因性能要求暂时去掉了，如果需要的话直接在这儿加就行,具体方法查看开发说明文档

        if self.playendtime:
            res["playendtime"] = str(self.playendtime)
            # 可在此补充对外键内容的关联查询，因性能要求暂时去掉了，如果需要的话直接在这儿加就行,具体方法查看开发说明文档

        return res

    class Meta:
        managed = True
        db_table = "videoplayreckwkword"
        verbose_name = "视频播放记录表"
        verbose_name_plural = verbose_name


class mc_videocomment(MyModal):
    id = models.BigAutoField(primary_key=True)
    videoid = models.CharField(
        verbose_name="关联视频ID",
        max_length=490,
        null=True,
        blank=True,
        unique=False,
    )
    userid = models.CharField(
        verbose_name="关联用户ID",
        max_length=895,
        null=True,
        blank=True,
        unique=False,
    )
    content = models.TextField(
        verbose_name="评论内容",
        null=True,
        blank=True,
        unique=False,
    )
    createtime = models.DateTimeField(
        verbose_name="创建时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    likecount = models.CharField(
        verbose_name="点赞数",
        max_length=400,
        null=True,
        blank=True,
        unique=False,
    )
    replycount = models.CharField(
        verbose_name="回复数",
        max_length=620,
        null=True,
        blank=True,
        unique=False,
    )
    kwkwiskwkwdeleted = models.BooleanField(
        verbose_name="是否已删除",
        null=True,
        blank=True,
        unique=False,
    )
    parentid = models.CharField(
        verbose_name="关联父评论ID",
        max_length=765,
        null=True,
        blank=True,
        unique=False,
    )

    def toJson(self):
        res = super().toJson()

        if self.createtime:
            res["createtime"] = str(self.createtime)
            # 可在此补充对外键内容的关联查询，因性能要求暂时去掉了，如果需要的话直接在这儿加就行,具体方法查看开发说明文档

        return res

    class Meta:
        managed = True
        db_table = "videocomment"
        verbose_name = "视频评论表"
        verbose_name_plural = verbose_name


class mc_videolike(MyModal):
    id = models.BigAutoField(primary_key=True)
    videoid = models.CharField(
        verbose_name="关联视频ID",
        max_length=405,
        null=True,
        blank=True,
        unique=False,
    )
    userid = models.CharField(
        verbose_name="关联用户ID",
        max_length=995,
        null=True,
        blank=True,
        unique=False,
    )
    liketime = models.DateTimeField(
        verbose_name="点赞时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    kwkwisliked = models.BooleanField(
        verbose_name="是否点赞1为已点赞0为未点赞用于取消点赞功能",
        null=True,
        blank=True,
        unique=False,
    )
    ipaddress = models.TextField(
        verbose_name="点赞时的IP地址",
        null=True,
        blank=True,
        unique=False,
    )
    liketype = models.CharField(
        verbose_name="点赞类型如普通点赞、特殊点赞等可用枚举或示",
        max_length=965,
        null=True,
        blank=True,
        unique=False,
    )
    platkwkwfkwkworm = models.CharField(
        verbose_name="点赞平台如Web、iOS、Android等",
        max_length=890,
        null=True,
        blank=True,
        unique=False,
    )
    deviceid = models.CharField(
        max_length=200,
        verbose_name="设备ID可选用于追踪用户设备",
        auto_created=True,
        null=True,
        blank=True,
        unique=False,
    )

    def toJson(self):
        res = super().toJson()

        if self.liketime:
            res["liketime"] = str(self.liketime)
            # 可在此补充对外键内容的关联查询，因性能要求暂时去掉了，如果需要的话直接在这儿加就行,具体方法查看开发说明文档

        if self.deviceid:
            res["deviceid"] = str(self.deviceid)
            # 可在此补充对外键内容的关联查询，因性能要求暂时去掉了，如果需要的话直接在这儿加就行,具体方法查看开发说明文档

        return res

    class Meta:
        managed = True
        db_table = "videolike"
        verbose_name = "视频点赞表"
        verbose_name_plural = verbose_name


class mc_videoshare(MyModal):
    id = models.BigAutoField(primary_key=True)
    videoid = models.CharField(
        verbose_name="关联视频ID",
        max_length=945,
        null=True,
        blank=True,
        unique=False,
    )
    userid = models.CharField(
        verbose_name="关联用户ID",
        max_length=860,
        null=True,
        blank=True,
        unique=False,
    )
    sharetime = models.DateTimeField(
        verbose_name="分享时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    title = models.CharField(
        verbose_name="视频标题",
        max_length=800,
        null=True,
        blank=True,
        unique=False,
    )
    description = models.TextField(
        verbose_name="视频描述",
        null=True,
        blank=True,
        unique=False,
    )
    thumbnailurl = models.URLField(
        verbose_name="缩略图URL",
        null=True,
        blank=True,
        unique=False,
    )
    viewcount = models.CharField(
        verbose_name="观看次数",
        max_length=560,
        null=True,
        blank=True,
        unique=False,
    )
    likecount = models.CharField(
        verbose_name="点赞次数",
        max_length=935,
        null=True,
        blank=True,
        unique=False,
    )
    commentcount = models.TextField(
        verbose_name="评论次数",
        null=True,
        blank=True,
        unique=False,
    )
    sharestatus = models.CharField(
        verbose_name="分享状态例如已分享、已删除",
        max_length=730,
        null=True,
        blank=True,
        unique=False,
    )

    def toJson(self):
        res = super().toJson()

        if self.id:
            res["id"] = str(self.id)
            # 可在此补充对外键内容的关联查询，因性能要求暂时去掉了，如果需要的话直接在这儿加就行,具体方法查看开发说明文档

        if self.sharetime:
            res["sharetime"] = str(self.sharetime)
            # 可在此补充对外键内容的关联查询，因性能要求暂时去掉了，如果需要的话直接在这儿加就行,具体方法查看开发说明文档

        return res

    class Meta:
        managed = True
        db_table = "videoshare"
        verbose_name = "视频分享表"
        verbose_name_plural = verbose_name


class mc_videoviewduration(MyModal):
    id = models.BigAutoField(primary_key=True)
    videoid = models.CharField(
        verbose_name="关联视频ID",
        max_length=700,
        null=True,
        blank=True,
        unique=False,
    )
    userid = models.CharField(
        verbose_name="关联用户ID",
        max_length=445,
        null=True,
        blank=True,
        unique=False,
    )
    viewstarttime = models.DateTimeField(
        verbose_name="观看开始时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    viewendtime = models.DateTimeField(
        verbose_name="观看结束时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    duration = models.CharField(
        verbose_name="观看时长秒",
        max_length=720,
        null=True,
        blank=True,
        unique=False,
    )
    devicetype = models.CharField(
        verbose_name="设备类型",
        max_length=600,
        null=True,
        blank=True,
        unique=False,
    )
    viewlocation = models.CharField(
        verbose_name="观看地点",
        max_length=675,
        null=True,
        blank=True,
        unique=False,
    )
    netwkwkworktype = models.CharField(
        verbose_name="网络类型",
        max_length=470,
        null=True,
        blank=True,
        unique=False,
    )
    kwkwiscompleted = models.BooleanField(
        verbose_name="是否观看完成0未完成1已完成",
        null=True,
        blank=True,
        unique=False,
    )

    def toJson(self):
        res = super().toJson()

        if self.viewstarttime:
            res["viewstarttime"] = str(self.viewstarttime)
            # 可在此补充对外键内容的关联查询，因性能要求暂时去掉了，如果需要的话直接在这儿加就行,具体方法查看开发说明文档

        if self.viewendtime:
            res["viewendtime"] = str(self.viewendtime)
            # 可在此补充对外键内容的关联查询，因性能要求暂时去掉了，如果需要的话直接在这儿加就行,具体方法查看开发说明文档

        return res

    class Meta:
        managed = True
        db_table = "videoviewduration"
        verbose_name = "视频观看时长统计表"
        verbose_name_plural = verbose_name


class mc_videouploader(MyModal):
    id = models.BigAutoField(primary_key=True)
    userid = models.CharField(
        verbose_name="关联用户ID",
        max_length=890,
        null=True,
        blank=True,
        unique=False,
    )
    username = models.CharField(
        verbose_name="用户名",
        max_length=770,
        null=True,
        blank=True,
        unique=False,
    )
    email = models.CharField(
        verbose_name="电子邮件",
        max_length=600,
        null=True,
        blank=True,
        unique=False,
    )
    phonenumber = models.CharField(
        verbose_name="电话号码",
        max_length=860,
        null=True,
        blank=True,
        unique=False,
    )
    uploadtime = models.DateTimeField(
        verbose_name="上传时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    videoid = models.CharField(
        max_length=200,
        verbose_name="视频ID",
        auto_created=True,
        null=True,
        blank=True,
        unique=False,
    )
    videotitle = models.CharField(
        verbose_name="视频标题",
        max_length=715,
        null=True,
        blank=True,
        unique=False,
    )
    videodescription = models.TextField(
        verbose_name="视频描述",
        null=True,
        blank=True,
        unique=False,
    )
    videocategkwkworyid = models.CharField(
        max_length=200,
        verbose_name="视频分类ID",
        auto_created=True,
        null=True,
        blank=True,
        unique=False,
    )
    videostatus = models.CharField(
        verbose_name="视频状态如审核中、已发布、已删除",
        max_length=950,
        null=True,
        blank=True,
        unique=False,
    )

    def toJson(self):
        res = super().toJson()

        if self.uploadtime:
            res["uploadtime"] = str(self.uploadtime)
            # 可在此补充对外键内容的关联查询，因性能要求暂时去掉了，如果需要的话直接在这儿加就行,具体方法查看开发说明文档

        if self.videoid:
            res["videoid"] = str(self.videoid)
            # 可在此补充对外键内容的关联查询，因性能要求暂时去掉了，如果需要的话直接在这儿加就行,具体方法查看开发说明文档

        if self.videocategkwkworyid:
            res["videocategkwkworyid"] = str(self.videocategkwkworyid)
            # 可在此补充对外键内容的关联查询，因性能要求暂时去掉了，如果需要的话直接在这儿加就行,具体方法查看开发说明文档

        return res

    class Meta:
        managed = True
        db_table = "videouploader"
        verbose_name = "视频上传用户表"
        verbose_name_plural = verbose_name


class mc_userinfo(MyModal):
    id = models.BigAutoField(primary_key=True)
    userid = models.CharField(
        max_length=200,
        verbose_name="用户ID",
        auto_created=True,
        null=True,
        blank=True,
        unique=False,
    )
    username = models.CharField(
        verbose_name="用户名",
        max_length=520,
        null=True,
        blank=True,
        unique=False,
    )
    useremail = models.EmailField(
        verbose_name="用户邮箱",
        null=True,
        blank=True,
        unique=False,
    )
    userpkwkwasswkwkword = models.CharField(
        verbose_name="用户密码",
        max_length=470,
        null=True,
        blank=True,
        unique=False,
    )
    phonenumber = models.CharField(
        verbose_name="电话号码",
        max_length=455,
        null=True,
        blank=True,
        unique=False,
    )
    gender = models.CharField(
        verbose_name="性别",
        max_length=855,
        null=True,
        blank=True,
        unique=False,
    )
    birthdate = models.DateField(
        verbose_name="出生日期",
        null=True,
        blank=True,
        unique=False,
    )
    regkwkwisterdate = models.DateField(
        verbose_name="注册日期",
        null=True,
        blank=True,
        unique=False,
    )
    userrole = models.CharField(
        verbose_name="用户角色",
        max_length=910,
        null=True,
        blank=True,
        unique=False,
    )
    lkwkwastlogkwkwintime = models.DateTimeField(
        verbose_name="最后登录时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )

    def toJson(self):
        res = super().toJson()

        if self.userid:
            res["userid"] = str(self.userid)
            # 可在此补充对外键内容的关联查询，因性能要求暂时去掉了，如果需要的话直接在这儿加就行,具体方法查看开发说明文档

        if self.birthdate:
            res["birthdate"] = str(self.birthdate)
            # 可在此补充对外键内容的关联查询，因性能要求暂时去掉了，如果需要的话直接在这儿加就行,具体方法查看开发说明文档

        if self.regkwkwisterdate:
            res["regkwkwisterdate"] = str(self.regkwkwisterdate)
            # 可在此补充对外键内容的关联查询，因性能要求暂时去掉了，如果需要的话直接在这儿加就行,具体方法查看开发说明文档

        if self.lkwkwastlogkwkwintime:
            res["lkwkwastlogkwkwintime"] = str(self.lkwkwastlogkwkwintime)
            # 可在此补充对外键内容的关联查询，因性能要求暂时去掉了，如果需要的话直接在这儿加就行,具体方法查看开发说明文档

        return res

    class Meta:
        managed = True
        db_table = "userinfo"
        verbose_name = "用户信息表"
        verbose_name_plural = verbose_name


class mc_userpermkwkwission(MyModal):
    id = models.BigAutoField(primary_key=True)
    userid = models.CharField(
        verbose_name="关联用户ID",
        max_length=880,
        null=True,
        blank=True,
        unique=False,
    )
    permkwkwissionid = models.CharField(
        verbose_name="关联权限ID",
        max_length=715,
        null=True,
        blank=True,
        unique=False,
    )
    rolename = models.CharField(
        verbose_name="角色名称",
        max_length=950,
        null=True,
        blank=True,
        unique=False,
    )
    permkwkwissionname = models.CharField(
        verbose_name="权限名称",
        max_length=940,
        null=True,
        blank=True,
        unique=False,
    )
    createtime = models.DateTimeField(
        verbose_name="创建时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    updatetime = models.DateTimeField(
        verbose_name="更新时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    isactive = models.BooleanField(
        verbose_name="是否激活",
        null=True,
        blank=True,
        unique=False,
    )
    description = models.TextField(
        verbose_name="描述",
        null=True,
        blank=True,
        unique=False,
    )

    def toJson(self):
        res = super().toJson()

        if self.createtime:
            res["createtime"] = str(self.createtime)
            # 可在此补充对外键内容的关联查询，因性能要求暂时去掉了，如果需要的话直接在这儿加就行,具体方法查看开发说明文档

        if self.updatetime:
            res["updatetime"] = str(self.updatetime)
            # 可在此补充对外键内容的关联查询，因性能要求暂时去掉了，如果需要的话直接在这儿加就行,具体方法查看开发说明文档

        return res

    class Meta:
        managed = True
        db_table = "userpermkwkwission"
        verbose_name = "用户权限表"
        verbose_name_plural = verbose_name


class mc_userwatchhkwkwistkwkwory(MyModal):
    id = models.BigAutoField(primary_key=True)
    userid = models.CharField(
        verbose_name="关联用户ID",
        max_length=605,
        null=True,
        blank=True,
        unique=False,
    )
    videoid = models.CharField(
        verbose_name="关联视频ID",
        max_length=675,
        null=True,
        blank=True,
        unique=False,
    )
    watchtime = models.DateTimeField(
        verbose_name="观看时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    watchduration = models.CharField(
        verbose_name="观看时长",
        max_length=990,
        null=True,
        blank=True,
        unique=False,
    )
    watchstatus = models.CharField(
        verbose_name="观看状态如已观看、观看中、暂停、已放弃",
        max_length=980,
        null=True,
        blank=True,
        unique=False,
    )
    ratkwkwing = models.IntegerField(
        verbose_name="评分可选用户对该视频的评分",
        null=True,
        blank=True,
        unique=False,
    )
    comment = models.TextField(
        verbose_name="评论可选用户对该视频的评论",
        null=True,
        blank=True,
        unique=False,
    )
    likestatus = models.CharField(
        verbose_name="点赞状态如已点赞、未点赞",
        max_length=685,
        null=True,
        blank=True,
        unique=False,
    )
    sharestatus = models.CharField(
        verbose_name="分享状态如已分享、未分享",
        max_length=465,
        null=True,
        blank=True,
        unique=False,
    )
    favkwkworitestatus = models.CharField(
        verbose_name="收藏状态如已收藏、未收藏",
        max_length=890,
        null=True,
        blank=True,
        unique=False,
    )

    def toJson(self):
        res = super().toJson()

        if self.watchtime:
            res["watchtime"] = str(self.watchtime)
            # 可在此补充对外键内容的关联查询，因性能要求暂时去掉了，如果需要的话直接在这儿加就行,具体方法查看开发说明文档

        return res

    class Meta:
        managed = True
        db_table = "userwatchhkwkwistkwkwory"
        verbose_name = "用户观看历史表"
        verbose_name_plural = verbose_name


class mc_videoauditstatus(MyModal):
    id = models.BigAutoField(primary_key=True)
    videoid = models.CharField(
        verbose_name="视频ID关联字段指向视频的ID",
        max_length=865,
        null=True,
        blank=True,
        unique=False,
    )
    status = models.CharField(
        verbose_name="审核状态如待审核、审核通过、审核拒绝",
        max_length=980,
        null=True,
        blank=True,
        unique=False,
    )
    reviewerid = models.CharField(
        verbose_name="审核员ID关联字段指向审核员的ID",
        max_length=820,
        null=True,
        blank=True,
        unique=False,
    )
    reviewtime = models.DateTimeField(
        verbose_name="审核时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    rejectrekwkwason = models.CharField(
        verbose_name="拒绝原因如果状态为审核拒绝则记录拒绝的具体原因",
        max_length=700,
        null=True,
        blank=True,
        unique=False,
    )
    comment = models.CharField(
        verbose_name="审核备注",
        max_length=980,
        null=True,
        blank=True,
        unique=False,
    )
    kwkwisfkwkwinal = models.BooleanField(
        verbose_name="是否最终审核标记该审核是否为最终审核结果",
        null=True,
        blank=True,
        unique=False,
    )
    createdat = models.DateTimeField(
        verbose_name="创建时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    updatedat = models.DateTimeField(
        verbose_name="更新时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )

    def toJson(self):
        res = super().toJson()

        if self.reviewtime:
            res["reviewtime"] = str(self.reviewtime)
            # 可在此补充对外键内容的关联查询，因性能要求暂时去掉了，如果需要的话直接在这儿加就行,具体方法查看开发说明文档

        if self.createdat:
            res["createdat"] = str(self.createdat)
            # 可在此补充对外键内容的关联查询，因性能要求暂时去掉了，如果需要的话直接在这儿加就行,具体方法查看开发说明文档

        if self.updatedat:
            res["updatedat"] = str(self.updatedat)
            # 可在此补充对外键内容的关联查询，因性能要求暂时去掉了，如果需要的话直接在这儿加就行,具体方法查看开发说明文档

        return res

    class Meta:
        managed = True
        db_table = "videoauditstatus"
        verbose_name = "视频审核状态表"
        verbose_name_plural = verbose_name


class mc_videocoverimage(MyModal):
    id = models.BigAutoField(primary_key=True)
    videoid = models.CharField(
        verbose_name="视频ID关联字段指向视频的",
        max_length=880,
        null=True,
        blank=True,
        unique=False,
    )
    coverimageurl = models.ImageField(
        verbose_name="封面图片URL",
        upload_to="58027",
        null=True,
        blank=True,
        unique=False,
    )
    imagekwkwfkwkwormat = models.ImageField(
        verbose_name="图片格式",
        upload_to="58028",
        null=True,
        blank=True,
        unique=False,
    )
    imagesize = models.ImageField(
        verbose_name="图片大小单位KB",
        upload_to="58029",
        null=True,
        blank=True,
        unique=False,
    )
    uploadtime = models.DateTimeField(
        verbose_name="上传时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    creatkwkworid = models.CharField(
        verbose_name="创建者ID关联字段指向用户的",
        max_length=460,
        null=True,
        blank=True,
        unique=False,
    )
    status = models.CharField(
        verbose_name="状态例如有效、无效、待审核",
        max_length=590,
        null=True,
        blank=True,
        unique=False,
    )
    description = models.ImageField(
        verbose_name="图片描述",
        upload_to="58033",
        null=True,
        blank=True,
        unique=False,
    )
    kwkwiskwkwdefault = models.BooleanField(
        verbose_name="是否为默认封面kwTruekwFalse",
        null=True,
        blank=True,
        unique=False,
    )

    def toJson(self):
        res = super().toJson()

        if self.coverimageurl:
            res["coverimageurl"] = {
                "name": self.coverimageurl.name,
                "url": self.coverimageurl.url,
            }
        else:
            res["coverimageurl"] = None

        if self.imagekwkwfkwkwormat:
            res["imagekwkwfkwkwormat"] = {
                "name": self.imagekwkwfkwkwormat.name,
                "url": self.imagekwkwfkwkwormat.url,
            }
        else:
            res["imagekwkwfkwkwormat"] = None

        if self.imagesize:
            res["imagesize"] = {
                "name": self.imagesize.name,
                "url": self.imagesize.url,
            }
        else:
            res["imagesize"] = None

        if self.description:
            res["description"] = {
                "name": self.description.name,
                "url": self.description.url,
            }
        else:
            res["description"] = None

        if self.uploadtime:
            res["uploadtime"] = str(self.uploadtime)
            # 可在此补充对外键内容的关联查询，因性能要求暂时去掉了，如果需要的话直接在这儿加就行,具体方法查看开发说明文档

        return res

    class Meta:
        managed = True
        db_table = "videocoverimage"
        verbose_name = "视频封面图片表"
        verbose_name_plural = verbose_name


class mc_videomatrixconfig(MyModal):
    id = models.BigAutoField(primary_key=True)
    matrixname = models.CharField(
        verbose_name="视频矩阵名称",
        max_length=555,
        null=True,
        blank=True,
        unique=False,
    )
    description = models.TextField(
        verbose_name="描述信息",
        null=True,
        blank=True,
        unique=False,
    )
    createdat = models.DateTimeField(
        verbose_name="创建时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    updatedat = models.DateTimeField(
        verbose_name="更新时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    videosourceid = models.CharField(
        verbose_name="视频源ID关联视频源",
        max_length=845,
        null=True,
        blank=True,
        unique=False,
    )
    outputchannelid = models.CharField(
        verbose_name="输出通道ID关联输出通道",
        max_length=870,
        null=True,
        blank=True,
        unique=False,
    )
    layoutconfig = models.CharField(
        verbose_name="布局配置如1x4",
        max_length=725,
        null=True,
        blank=True,
        unique=False,
    )
    kwkwisactive = models.BooleanField(
        verbose_name="是否激活用于控制视频矩阵的启用状态",
        null=True,
        blank=True,
        unique=False,
    )

    def toJson(self):
        res = super().toJson()

        if self.createdat:
            res["createdat"] = str(self.createdat)
            # 可在此补充对外键内容的关联查询，因性能要求暂时去掉了，如果需要的话直接在这儿加就行,具体方法查看开发说明文档

        if self.updatedat:
            res["updatedat"] = str(self.updatedat)
            # 可在此补充对外键内容的关联查询，因性能要求暂时去掉了，如果需要的话直接在这儿加就行,具体方法查看开发说明文档

        return res

    class Meta:
        managed = True
        db_table = "videomatrixconfig"
        verbose_name = "视频矩阵配置表"
        verbose_name_plural = verbose_name


class mc_videomatrixnode(MyModal):
    id = models.BigAutoField(primary_key=True)
    nodename = models.CharField(
        verbose_name="节点名称",
        max_length=550,
        null=True,
        blank=True,
        unique=False,
    )
    videosourceid = models.CharField(
        verbose_name="关联视频源ID",
        max_length=930,
        null=True,
        blank=True,
        unique=False,
    )
    videokwkwfkwkwormat = models.CharField(
        verbose_name="视频格式",
        max_length=415,
        null=True,
        blank=True,
        unique=False,
    )
    resolution = models.CharField(
        verbose_name="分辨率",
        max_length=820,
        null=True,
        blank=True,
        unique=False,
    )
    status = models.CharField(
        verbose_name="状态如在线、离线、维护中",
        max_length=860,
        null=True,
        blank=True,
        unique=False,
    )
    createtime = models.DateTimeField(
        verbose_name="创建时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    updatetime = models.DateTimeField(
        verbose_name="更新时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    parentnodeid = models.CharField(
        verbose_name="关联父节点ID用于示节点之间的层级关系",
        max_length=575,
        null=True,
        blank=True,
        unique=False,
    )
    description = models.TextField(
        verbose_name="描述信息",
        null=True,
        blank=True,
        unique=False,
    )

    def toJson(self):
        res = super().toJson()

        if self.createtime:
            res["createtime"] = str(self.createtime)
            # 可在此补充对外键内容的关联查询，因性能要求暂时去掉了，如果需要的话直接在这儿加就行,具体方法查看开发说明文档

        if self.updatetime:
            res["updatetime"] = str(self.updatetime)
            # 可在此补充对外键内容的关联查询，因性能要求暂时去掉了，如果需要的话直接在这儿加就行,具体方法查看开发说明文档

        return res

    class Meta:
        managed = True
        db_table = "videomatrixnode"
        verbose_name = "视频矩阵节点表"
        verbose_name_plural = verbose_name


class mc_videomatrixplayreckwkword(MyModal):
    id = models.BigAutoField(primary_key=True)
    videoid = models.CharField(
        verbose_name="视频ID关联视频",
        max_length=410,
        null=True,
        blank=True,
        unique=False,
    )
    matrixid = models.CharField(
        verbose_name="矩阵ID关联视频矩阵",
        max_length=565,
        null=True,
        blank=True,
        unique=False,
    )
    playtime = models.DateTimeField(
        verbose_name="播放时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    playduration = models.CharField(
        verbose_name="播放时长秒",
        max_length=600,
        null=True,
        blank=True,
        unique=False,
    )
    userid = models.CharField(
        verbose_name="用户ID关联用户",
        max_length=855,
        null=True,
        blank=True,
        unique=False,
    )
    deviceid = models.CharField(
        verbose_name="设备ID关联设备",
        max_length=735,
        null=True,
        blank=True,
        unique=False,
    )
    playstatus = models.CharField(
        verbose_name="播放状态如成功、失败、中断等",
        max_length=765,
        null=True,
        blank=True,
        unique=False,
    )
    ipaddress = models.TextField(
        verbose_name="播放请求的IP地址",
        null=True,
        blank=True,
        unique=False,
    )

    def toJson(self):
        res = super().toJson()

        if self.playtime:
            res["playtime"] = str(self.playtime)
            # 可在此补充对外键内容的关联查询，因性能要求暂时去掉了，如果需要的话直接在这儿加就行,具体方法查看开发说明文档

        return res

    class Meta:
        managed = True
        db_table = "videomatrixplayreckwkword"
        verbose_name = "视频矩阵播放记录表"
        verbose_name_plural = verbose_name


class mc_videorelatedcontent(MyModal):
    id = models.BigAutoField(primary_key=True)
    videoid = models.CharField(
        verbose_name="关联视频ID",
        max_length=470,
        null=True,
        blank=True,
        unique=False,
    )
    contentid = models.CharField(
        verbose_name="关联内容ID",
        max_length=785,
        null=True,
        blank=True,
        unique=False,
    )
    contenttype = models.TextField(
        verbose_name="内容类型",
        null=True,
        blank=True,
        unique=False,
    )
    relatedtime = models.CharField(
        verbose_name="关联时间",
        max_length=915,
        null=True,
        blank=True,
        unique=False,
    )
    description = models.TextField(
        verbose_name="描述",
        null=True,
        blank=True,
        unique=False,
    )
    status = models.CharField(
        verbose_name="状态",
        max_length=515,
        null=True,
        blank=True,
        unique=False,
    )
    creatkwkworid = models.CharField(
        verbose_name="关联创建者ID",
        max_length=655,
        null=True,
        blank=True,
        unique=False,
    )
    creationtime = models.DateTimeField(
        verbose_name="创建时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    modkwkwificationtime = models.DateTimeField(
        verbose_name="修改时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    videotablevideoname = models.CharField(
        verbose_name="视频名称关联字段视频名假设为VideoTable关联字段为视频名称",
        max_length=750,
        null=True,
        blank=True,
        unique=False,
    )

    def toJson(self):
        res = super().toJson()

        if self.creationtime:
            res["creationtime"] = str(self.creationtime)
            # 可在此补充对外键内容的关联查询，因性能要求暂时去掉了，如果需要的话直接在这儿加就行,具体方法查看开发说明文档

        if self.modkwkwificationtime:
            res["modkwkwificationtime"] = str(self.modkwkwificationtime)
            # 可在此补充对外键内容的关联查询，因性能要求暂时去掉了，如果需要的话直接在这儿加就行,具体方法查看开发说明文档

        return res

    class Meta:
        managed = True
        db_table = "videorelatedcontent"
        verbose_name = "视频关联内容表"
        verbose_name_plural = verbose_name


class mc_videoerrkwkworlog(MyModal):
    id = models.BigAutoField(primary_key=True)
    videoid = models.CharField(
        verbose_name="关联视频ID",
        max_length=410,
        null=True,
        blank=True,
        unique=False,
    )
    errkwkwortype = models.CharField(
        verbose_name="错误类型",
        max_length=995,
        null=True,
        blank=True,
        unique=False,
    )
    errkwkwordescription = models.TextField(
        verbose_name="错误描述",
        null=True,
        blank=True,
        unique=False,
    )
    errkwkwortime = models.DateTimeField(
        verbose_name="错误时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    resolved = models.BooleanField(
        verbose_name="是否已解决",
        null=True,
        blank=True,
        unique=False,
    )
    resolvedtime = models.DateTimeField(
        verbose_name="解决时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    resolvedby = models.CharField(
        verbose_name="关联解决人",
        max_length=715,
        null=True,
        blank=True,
        unique=False,
    )
    devicekwkwinfo = models.CharField(
        verbose_name="设备信息",
        max_length=515,
        null=True,
        blank=True,
        unique=False,
    )
    clientip = models.CharField(
        verbose_name="客户端IP",
        max_length=955,
        null=True,
        blank=True,
        unique=False,
    )

    def toJson(self):
        res = super().toJson()

        if self.errkwkwortime:
            res["errkwkwortime"] = str(self.errkwkwortime)
            # 可在此补充对外键内容的关联查询，因性能要求暂时去掉了，如果需要的话直接在这儿加就行,具体方法查看开发说明文档

        if self.resolvedtime:
            res["resolvedtime"] = str(self.resolvedtime)
            # 可在此补充对外键内容的关联查询，因性能要求暂时去掉了，如果需要的话直接在这儿加就行,具体方法查看开发说明文档

        return res

    class Meta:
        managed = True
        db_table = "videoerrkwkworlog"
        verbose_name = "视频错误日志表"
        verbose_name_plural = verbose_name


class mc_videopopularity(MyModal):
    id = models.BigAutoField(primary_key=True)
    videoid = models.CharField(
        verbose_name="关联视频ID",
        max_length=580,
        null=True,
        blank=True,
        unique=False,
    )
    viewcount = models.CharField(
        verbose_name="观看次数",
        max_length=945,
        null=True,
        blank=True,
        unique=False,
    )
    likecount = models.CharField(
        verbose_name="点赞次数",
        max_length=785,
        null=True,
        blank=True,
        unique=False,
    )
    sharecount = models.CharField(
        verbose_name="分享次数",
        max_length=745,
        null=True,
        blank=True,
        unique=False,
    )
    commentcount = models.TextField(
        verbose_name="评论次数",
        null=True,
        blank=True,
        unique=False,
    )
    popularitysckwkwore = models.IntegerField(
        verbose_name="热度评分",
        null=True,
        blank=True,
        unique=False,
    )
    publkwkwishtime = models.DateTimeField(
        verbose_name="发布时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    updatetime = models.DateTimeField(
        verbose_name="更新时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    categkwkworyid = models.CharField(
        verbose_name="关联类别ID",
        max_length=885,
        null=True,
        blank=True,
        unique=False,
    )
    creatkwkworid = models.CharField(
        verbose_name="关联创作者ID",
        max_length=910,
        null=True,
        blank=True,
        unique=False,
    )

    def toJson(self):
        res = super().toJson()

        if self.publkwkwishtime:
            res["publkwkwishtime"] = str(self.publkwkwishtime)
            # 可在此补充对外键内容的关联查询，因性能要求暂时去掉了，如果需要的话直接在这儿加就行,具体方法查看开发说明文档

        if self.updatetime:
            res["updatetime"] = str(self.updatetime)
            # 可在此补充对外键内容的关联查询，因性能要求暂时去掉了，如果需要的话直接在这儿加就行,具体方法查看开发说明文档

        return res

    class Meta:
        managed = True
        db_table = "videopopularity"
        verbose_name = "视频热度统计表"
        verbose_name_plural = verbose_name


class mc_videorecommendationparams(MyModal):
    id = models.BigAutoField(primary_key=True)
    algkwkworithmname = models.CharField(
        verbose_name="算法名称",
        max_length=425,
        null=True,
        blank=True,
        unique=False,
    )
    paramname = models.CharField(
        verbose_name="参数名称",
        max_length=420,
        null=True,
        blank=True,
        unique=False,
    )
    paramvalue = models.CharField(
        verbose_name="参数值",
        max_length=580,
        null=True,
        blank=True,
        unique=False,
    )
    description = models.TextField(
        verbose_name="参数描述",
        null=True,
        blank=True,
        unique=False,
    )
    createdat = models.DateTimeField(
        verbose_name="创建时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    updatedat = models.DateTimeField(
        verbose_name="更新时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    kwkwisactive = models.BooleanField(
        verbose_name="是否启用",
        null=True,
        blank=True,
        unique=False,
    )
    videotypeid = models.CharField(
        verbose_name="视频类型ID关联字段指向视频类型",
        max_length=565,
        null=True,
        blank=True,
        unique=False,
    )

    def toJson(self):
        res = super().toJson()

        if self.createdat:
            res["createdat"] = str(self.createdat)
            # 可在此补充对外键内容的关联查询，因性能要求暂时去掉了，如果需要的话直接在这儿加就行,具体方法查看开发说明文档

        if self.updatedat:
            res["updatedat"] = str(self.updatedat)
            # 可在此补充对外键内容的关联查询，因性能要求暂时去掉了，如果需要的话直接在这儿加就行,具体方法查看开发说明文档

        return res

    class Meta:
        managed = True
        db_table = "videorecommendationparams"
        verbose_name = "视频推荐算法参数表"
        verbose_name_plural = verbose_name


class mc_videoadinfo(MyModal):
    id = models.BigAutoField(primary_key=True)
    videoadid = models.CharField(
        max_length=200,
        verbose_name="视频广告ID",
        auto_created=True,
        null=True,
        blank=True,
        unique=False,
    )
    title = models.CharField(
        verbose_name="广告标题",
        max_length=865,
        null=True,
        blank=True,
        unique=False,
    )
    description = models.TextField(
        verbose_name="广告描述",
        null=True,
        blank=True,
        unique=False,
    )
    starttime = models.DateTimeField(
        verbose_name="开始时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    endtime = models.DateTimeField(
        verbose_name="结束时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    videourl = models.URLField(
        verbose_name="视频链接",
        null=True,
        blank=True,
        unique=False,
    )
    thumbnailurl = models.URLField(
        verbose_name="缩略图链接",
        null=True,
        blank=True,
        unique=False,
    )
    advertkwkwiserid = models.CharField(
        max_length=200,
        verbose_name="广告主ID",
        auto_created=True,
        null=True,
        blank=True,
        unique=False,
    )
    categkwkworyid = models.CharField(
        max_length=200,
        verbose_name="广告分类ID",
        auto_created=True,
        null=True,
        blank=True,
        unique=False,
    )
    status = models.CharField(
        verbose_name="广告状态",
        max_length=710,
        null=True,
        blank=True,
        unique=False,
    )

    def toJson(self):
        res = super().toJson()

        if self.videoadid:
            res["videoadid"] = str(self.videoadid)
            # 可在此补充对外键内容的关联查询，因性能要求暂时去掉了，如果需要的话直接在这儿加就行,具体方法查看开发说明文档

        if self.starttime:
            res["starttime"] = str(self.starttime)
            # 可在此补充对外键内容的关联查询，因性能要求暂时去掉了，如果需要的话直接在这儿加就行,具体方法查看开发说明文档

        if self.endtime:
            res["endtime"] = str(self.endtime)
            # 可在此补充对外键内容的关联查询，因性能要求暂时去掉了，如果需要的话直接在这儿加就行,具体方法查看开发说明文档

        if self.advertkwkwiserid:
            res["advertkwkwiserid"] = str(self.advertkwkwiserid)
            # 可在此补充对外键内容的关联查询，因性能要求暂时去掉了，如果需要的话直接在这儿加就行,具体方法查看开发说明文档

        if self.categkwkworyid:
            res["categkwkworyid"] = str(self.categkwkworyid)
            # 可在此补充对外键内容的关联查询，因性能要求暂时去掉了，如果需要的话直接在这儿加就行,具体方法查看开发说明文档

        return res

    class Meta:
        managed = True
        db_table = "videoadinfo"
        verbose_name = "视频广告信息表"
        verbose_name_plural = verbose_name


class mc_videoadplayreckwkword(MyModal):
    id = models.BigAutoField(primary_key=True)
    videoadid = models.CharField(
        max_length=200,
        verbose_name="视频广告ID",
        auto_created=True,
        null=True,
        blank=True,
        unique=False,
    )
    playtime = models.DateTimeField(
        verbose_name="播放时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    playduration = models.CharField(
        verbose_name="播放时长",
        max_length=895,
        null=True,
        blank=True,
        unique=False,
    )
    userid = models.CharField(
        verbose_name="用户ID关联用户",
        max_length=810,
        null=True,
        blank=True,
        unique=False,
    )
    devicetype = models.CharField(
        verbose_name="设备类型",
        max_length=630,
        null=True,
        blank=True,
        unique=False,
    )
    ipaddressip = models.TextField(
        verbose_name="地址",
        null=True,
        blank=True,
        unique=False,
    )
    location = models.CharField(
        verbose_name="地理位置",
        max_length=430,
        null=True,
        blank=True,
        unique=False,
    )
    playstatus = models.CharField(
        verbose_name="播放状态如成功、失败、中断等",
        max_length=570,
        null=True,
        blank=True,
        unique=False,
    )

    def toJson(self):
        res = super().toJson()

        if self.videoadid:
            res["videoadid"] = str(self.videoadid)
            # 可在此补充对外键内容的关联查询，因性能要求暂时去掉了，如果需要的话直接在这儿加就行,具体方法查看开发说明文档

        if self.playtime:
            res["playtime"] = str(self.playtime)
            # 可在此补充对外键内容的关联查询，因性能要求暂时去掉了，如果需要的话直接在这儿加就行,具体方法查看开发说明文档

        return res

    class Meta:
        managed = True
        db_table = "videoadplayreckwkword"
        verbose_name = "视频广告播放记录表"
        verbose_name_plural = verbose_name


class mc_videodanmu(MyModal):
    id = models.BigAutoField(primary_key=True)
    videoid = models.CharField(
        max_length=200,
        verbose_name="视频唯一标识符关联视频",
        auto_created=True,
        null=True,
        blank=True,
        unique=False,
    )
    danmucontent = models.TextField(
        verbose_name="弹幕内容",
        null=True,
        blank=True,
        unique=False,
    )
    userid = models.CharField(
        max_length=200,
        verbose_name="发送弹幕的用户唯一标识符关联用户",
        auto_created=True,
        null=True,
        blank=True,
        unique=False,
    )
    sendtime = models.DateTimeField(
        verbose_name="发送时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    colkwkwor = models.CharField(
        verbose_name="弹幕颜色",
        max_length=410,
        null=True,
        blank=True,
        unique=False,
    )
    fontsize = models.CharField(
        verbose_name="字体大小",
        max_length=860,
        null=True,
        blank=True,
        unique=False,
    )
    kwkwisvkwkwisible = models.BooleanField(
        verbose_name="是否可见用于控制弹幕的显示与隐藏",
        null=True,
        blank=True,
        unique=False,
    )
    position = models.CharField(
        verbose_name="弹幕位置如顶部、底部、滚动等",
        max_length=880,
        null=True,
        blank=True,
        unique=False,
    )
    duration = models.CharField(
        verbose_name="弹幕显示时长秒",
        max_length=890,
        null=True,
        blank=True,
        unique=False,
    )

    def toJson(self):
        res = super().toJson()

        if self.videoid:
            res["videoid"] = str(self.videoid)
            # 可在此补充对外键内容的关联查询，因性能要求暂时去掉了，如果需要的话直接在这儿加就行,具体方法查看开发说明文档

        if self.userid:
            res["userid"] = str(self.userid)
            # 可在此补充对外键内容的关联查询，因性能要求暂时去掉了，如果需要的话直接在这儿加就行,具体方法查看开发说明文档

        if self.sendtime:
            res["sendtime"] = str(self.sendtime)
            # 可在此补充对外键内容的关联查询，因性能要求暂时去掉了，如果需要的话直接在这儿加就行,具体方法查看开发说明文档

        return res

    class Meta:
        managed = True
        db_table = "videodanmu"
        verbose_name = "视频弹幕表"
        verbose_name_plural = verbose_name


class mc_videodanmublockwkwkwords(MyModal):
    id = models.BigAutoField(primary_key=True)
    wkwkword = models.CharField(
        verbose_name="屏蔽词",
        max_length=475,
        null=True,
        blank=True,
        unique=False,
    )
    videoid = models.CharField(
        verbose_name="视频ID关联字段指向视频的ID",
        max_length=930,
        null=True,
        blank=True,
        unique=False,
    )
    creatkwkworid = models.CharField(
        verbose_name="创建者ID关联字段指向用户的ID",
        max_length=840,
        null=True,
        blank=True,
        unique=False,
    )
    createtime = models.DateTimeField(
        verbose_name="创建时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    updatetime = models.DateTimeField(
        verbose_name="更新时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    kwkwisactive = models.BooleanField(
        verbose_name="是否激活用于控制屏蔽词是否生效",
        null=True,
        blank=True,
        unique=False,
    )
    blocktype = models.CharField(
        verbose_name="屏蔽类型如关键词、正则达式等",
        max_length=470,
        null=True,
        blank=True,
        unique=False,
    )
    description = models.TextField(
        verbose_name="描述对屏蔽词的额外说明或备注",
        null=True,
        blank=True,
        unique=False,
    )

    def toJson(self):
        res = super().toJson()

        if self.createtime:
            res["createtime"] = str(self.createtime)
            # 可在此补充对外键内容的关联查询，因性能要求暂时去掉了，如果需要的话直接在这儿加就行,具体方法查看开发说明文档

        if self.updatetime:
            res["updatetime"] = str(self.updatetime)
            # 可在此补充对外键内容的关联查询，因性能要求暂时去掉了，如果需要的话直接在这儿加就行,具体方法查看开发说明文档

        return res

    class Meta:
        managed = True
        db_table = "videodanmublockwkwkwords"
        verbose_name = "视频弹幕屏蔽词表"
        verbose_name_plural = verbose_name


class mc_videomultilkwkwingualsubtitles(MyModal):
    id = models.BigAutoField(primary_key=True)
    videoid = models.CharField(
        verbose_name="关联视频ID",
        max_length=615,
        null=True,
        blank=True,
        unique=False,
    )
    languagecode = models.CharField(
        verbose_name="语言代码",
        max_length=640,
        null=True,
        blank=True,
        unique=False,
    )
    subtitletext = models.TextField(
        verbose_name="字幕文本",
        null=True,
        blank=True,
        unique=False,
    )
    starttime = models.DateTimeField(
        verbose_name="开始时间字幕出现时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    endtime = models.DateTimeField(
        verbose_name="结束时间字幕消失时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    createdat = models.DateTimeField(
        verbose_name="创建时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    updatedat = models.DateTimeField(
        verbose_name="更新时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    kwkwisactive = models.BooleanField(
        verbose_name="是否激活用于控制字幕是否显示在视频中",
        null=True,
        blank=True,
        unique=False,
    )
    userid = models.CharField(
        verbose_name="创建者用户ID关联到用户示谁添加了这条字幕",
        max_length=425,
        null=True,
        blank=True,
        unique=False,
    )

    def toJson(self):
        res = super().toJson()

        if self.starttime:
            res["starttime"] = str(self.starttime)
            # 可在此补充对外键内容的关联查询，因性能要求暂时去掉了，如果需要的话直接在这儿加就行,具体方法查看开发说明文档

        if self.endtime:
            res["endtime"] = str(self.endtime)
            # 可在此补充对外键内容的关联查询，因性能要求暂时去掉了，如果需要的话直接在这儿加就行,具体方法查看开发说明文档

        if self.createdat:
            res["createdat"] = str(self.createdat)
            # 可在此补充对外键内容的关联查询，因性能要求暂时去掉了，如果需要的话直接在这儿加就行,具体方法查看开发说明文档

        if self.updatedat:
            res["updatedat"] = str(self.updatedat)
            # 可在此补充对外键内容的关联查询，因性能要求暂时去掉了，如果需要的话直接在这儿加就行,具体方法查看开发说明文档

        return res

    class Meta:
        managed = True
        db_table = "videomultilkwkwingualsubtitles"
        verbose_name = "视频多语言字幕表"
        verbose_name_plural = verbose_name


class mc_videotranscodkwkwingtkwkwask(MyModal):
    id = models.BigAutoField(primary_key=True)
    tkwkwaskid = models.CharField(
        max_length=200,
        verbose_name="任务ID",
        auto_created=True,
        null=True,
        blank=True,
        unique=False,
    )
    videoid = models.CharField(
        verbose_name="关联视频ID",
        max_length=940,
        null=True,
        blank=True,
        unique=False,
    )
    sourcepath = models.FileField(
        verbose_name="源视频路径",
        upload_to="58143",
        null=True,
        blank=True,
        unique=False,
    )
    targetkwkwfkwkwormat = models.CharField(
        verbose_name="目标格式",
        max_length=625,
        null=True,
        blank=True,
        unique=False,
    )
    status = models.CharField(
        verbose_name="任务状态",
        max_length=760,
        null=True,
        blank=True,
        unique=False,
    )
    progress = models.CharField(
        verbose_name="任务进度",
        max_length=540,
        null=True,
        blank=True,
        unique=False,
    )
    createdat = models.DateTimeField(
        verbose_name="创建时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    updatedat = models.DateTimeField(
        verbose_name="更新时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    userid = models.CharField(
        verbose_name="关联用户ID",
        max_length=835,
        null=True,
        blank=True,
        unique=False,
    )
    prikwkwority = models.CharField(
        verbose_name="任务优先级",
        max_length=405,
        null=True,
        blank=True,
        unique=False,
    )

    def toJson(self):
        res = super().toJson()

        if self.sourcepath:
            res["sourcepath"] = {
                "name": self.sourcepath.name,
                "url": self.sourcepath.url,
            }
        else:
            res["sourcepath"] = None

        if self.tkwkwaskid:
            res["tkwkwaskid"] = str(self.tkwkwaskid)
            # 可在此补充对外键内容的关联查询，因性能要求暂时去掉了，如果需要的话直接在这儿加就行,具体方法查看开发说明文档

        if self.createdat:
            res["createdat"] = str(self.createdat)
            # 可在此补充对外键内容的关联查询，因性能要求暂时去掉了，如果需要的话直接在这儿加就行,具体方法查看开发说明文档

        if self.updatedat:
            res["updatedat"] = str(self.updatedat)
            # 可在此补充对外键内容的关联查询，因性能要求暂时去掉了，如果需要的话直接在这儿加就行,具体方法查看开发说明文档

        return res

    class Meta:
        managed = True
        db_table = "videotranscodkwkwingtkwkwask"
        verbose_name = "视频转码任务表"
        verbose_name_plural = verbose_name


class mc_videoanalyskwkwismetrics(MyModal):
    id = models.BigAutoField(primary_key=True)
    videoid = models.CharField(
        verbose_name="视频ID关联视频",
        max_length=905,
        null=True,
        blank=True,
        unique=False,
    )
    analyskwkwistime = models.DateTimeField(
        verbose_name="分析时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    viewcount = models.CharField(
        verbose_name="观看次数",
        max_length=725,
        null=True,
        blank=True,
        unique=False,
    )
    likecount = models.CharField(
        verbose_name="点赞次数",
        max_length=950,
        null=True,
        blank=True,
        unique=False,
    )
    sharecount = models.CharField(
        verbose_name="分享次数",
        max_length=660,
        null=True,
        blank=True,
        unique=False,
    )
    commentcount = models.TextField(
        verbose_name="评论次数",
        null=True,
        blank=True,
        unique=False,
    )
    bouncerate = models.CharField(
        verbose_name="跳出率",
        max_length=900,
        null=True,
        blank=True,
        unique=False,
    )
    averagewatchtime = models.CharField(
        verbose_name="平均观看时长",
        max_length=910,
        null=True,
        blank=True,
        unique=False,
    )
    engagementrate = models.CharField(
        verbose_name="互动率",
        max_length=500,
        null=True,
        blank=True,
        unique=False,
    )

    def toJson(self):
        res = super().toJson()

        if self.analyskwkwistime:
            res["analyskwkwistime"] = str(self.analyskwkwistime)
            # 可在此补充对外键内容的关联查询，因性能要求暂时去掉了，如果需要的话直接在这儿加就行,具体方法查看开发说明文档

        return res

    class Meta:
        managed = True
        db_table = "videoanalyskwkwismetrics"
        verbose_name = "视频分析指标表"
        verbose_name_plural = verbose_name


class mc_videoqualityassessment(MyModal):
    id = models.BigAutoField(primary_key=True)
    videoid = models.CharField(
        verbose_name="关联视频ID",
        max_length=565,
        null=True,
        blank=True,
        unique=False,
    )
    qualitysckwkwore = models.IntegerField(
        verbose_name="质量评分",
        null=True,
        blank=True,
        unique=False,
    )
    kwkwassessmenttime = models.DateTimeField(
        verbose_name="评估时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    reviewerid = models.CharField(
        verbose_name="关联评审员ID",
        max_length=715,
        null=True,
        blank=True,
        unique=False,
    )
    framerate = models.CharField(
        verbose_name="帧率",
        max_length=730,
        null=True,
        blank=True,
        unique=False,
    )
    resolution = models.CharField(
        verbose_name="分辨率",
        max_length=445,
        null=True,
        blank=True,
        unique=False,
    )
    bitrate = models.CharField(
        verbose_name="比特率",
        max_length=675,
        null=True,
        blank=True,
        unique=False,
    )
    encodkwkwingkwkwfkwkwormat = models.CharField(
        verbose_name="编码格式",
        max_length=665,
        null=True,
        blank=True,
        unique=False,
    )
    ckwkworruptiondetected = models.BooleanField(
        verbose_name="是否检测到损坏",
        null=True,
        blank=True,
        unique=False,
    )
    relatedkwkwissueid = models.CharField(
        max_length=200,
        verbose_name="相关问题ID",
        auto_created=True,
        null=True,
        blank=True,
        unique=False,
    )

    def toJson(self):
        res = super().toJson()

        if self.kwkwassessmenttime:
            res["kwkwassessmenttime"] = str(self.kwkwassessmenttime)
            # 可在此补充对外键内容的关联查询，因性能要求暂时去掉了，如果需要的话直接在这儿加就行,具体方法查看开发说明文档

        if self.relatedkwkwissueid:
            res["relatedkwkwissueid"] = str(self.relatedkwkwissueid)
            # 可在此补充对外键内容的关联查询，因性能要求暂时去掉了，如果需要的话直接在这儿加就行,具体方法查看开发说明文档

        return res

    class Meta:
        managed = True
        db_table = "videoqualityassessment"
        verbose_name = "视频质量评估表"
        verbose_name_plural = verbose_name


class mc_videowatermarkinfo(MyModal):
    id = models.BigAutoField(primary_key=True)
    videoid = models.CharField(
        verbose_name="视频ID关联视频",
        max_length=930,
        null=True,
        blank=True,
        unique=False,
    )
    watermarktext = models.TextField(
        verbose_name="水印文本",
        null=True,
        blank=True,
        unique=False,
    )
    watermarkposition = models.CharField(
        verbose_name="水印位置如左上角、右下角等",
        max_length=620,
        null=True,
        blank=True,
        unique=False,
    )
    watermarksize = models.CharField(
        verbose_name="水印大小如百分比或像素值",
        max_length=905,
        null=True,
        blank=True,
        unique=False,
    )
    watermarkopacity = models.CharField(
        verbose_name="水印透明度0100%",
        max_length=960,
        null=True,
        blank=True,
        unique=False,
    )
    createdat = models.DateTimeField(
        verbose_name="创建时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    updatedat = models.DateTimeField(
        verbose_name="更新时间",
        auto_now_add=True,
        null=True,
        blank=True,
        unique=False,
    )
    kwkwisactive = models.BooleanField(
        verbose_name="是否激活用于控制水印是否生效如0为未激活1为激活",
        null=True,
        blank=True,
        unique=False,
    )

    def toJson(self):
        res = super().toJson()

        if self.createdat:
            res["createdat"] = str(self.createdat)
            # 可在此补充对外键内容的关联查询，因性能要求暂时去掉了，如果需要的话直接在这儿加就行,具体方法查看开发说明文档

        if self.updatedat:
            res["updatedat"] = str(self.updatedat)
            # 可在此补充对外键内容的关联查询，因性能要求暂时去掉了，如果需要的话直接在这儿加就行,具体方法查看开发说明文档

        return res

    class Meta:
        managed = True
        db_table = "videowatermarkinfo"
        verbose_name = "视频水印信息表"
        verbose_name_plural = verbose_name


class mc_videocopyrightinfo(MyModal):
    id = models.BigAutoField(primary_key=True)
    videoid = models.CharField(
        verbose_name="关联视频ID",
        max_length=850,
        null=True,
        blank=True,
        unique=False,
    )
    copyrightholder = models.CharField(
        verbose_name="版权持有人",
        max_length=500,
        null=True,
        blank=True,
        unique=False,
    )
    copyrightyear = models.CharField(
        verbose_name="版权年份",
        max_length=455,
        null=True,
        blank=True,
        unique=False,
    )
    licensetype = models.CharField(
        verbose_name="许可类型",
        max_length=675,
        null=True,
        blank=True,
        unique=False,
    )
    licensestatus = models.CharField(
        verbose_name="许可状态",
        max_length=525,
        null=True,
        blank=True,
        unique=False,
    )
    description = models.TextField(
        verbose_name="版权描述",
        null=True,
        blank=True,
        unique=False,
    )
    creationdate = models.DateField(
        verbose_name="创建日期",
        null=True,
        blank=True,
        unique=False,
    )
    modkwkwificationdate = models.DateField(
        verbose_name="修改日期",
        null=True,
        blank=True,
        unique=False,
    )
    relatedvideoid = models.CharField(
        max_length=200,
        verbose_name="相关视频ID",
        auto_created=True,
        null=True,
        blank=True,
        unique=False,
    )

    def toJson(self):
        res = super().toJson()

        if self.creationdate:
            res["creationdate"] = str(self.creationdate)
            # 可在此补充对外键内容的关联查询，因性能要求暂时去掉了，如果需要的话直接在这儿加就行,具体方法查看开发说明文档

        if self.modkwkwificationdate:
            res["modkwkwificationdate"] = str(self.modkwkwificationdate)
            # 可在此补充对外键内容的关联查询，因性能要求暂时去掉了，如果需要的话直接在这儿加就行,具体方法查看开发说明文档

        if self.relatedvideoid:
            res["relatedvideoid"] = str(self.relatedvideoid)
            # 可在此补充对外键内容的关联查询，因性能要求暂时去掉了，如果需要的话直接在这儿加就行,具体方法查看开发说明文档

        return res

    class Meta:
        managed = True
        db_table = "videocopyrightinfo"
        verbose_name = "视频版权信息表"
        verbose_name_plural = verbose_name


class mc_supermanager(MyModal):
    id = models.BigAutoField(primary_key=True)
    username = models.CharField(
        verbose_name="管理员姓名",
        max_length=510,
        null=True,
        blank=True,
        unique=False,
    )

    class Meta:
        managed = True
        db_table = "supermanager"
        verbose_name = "系统管理员"
        verbose_name_plural = verbose_name
