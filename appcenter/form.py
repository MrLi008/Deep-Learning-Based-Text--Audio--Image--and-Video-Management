from django import forms

from captcha.fields import CaptchaField


class mc_videoinfo_form(forms.Form):
    """
    # For Table: 视频信息表
    """

    videoid = forms.UUIDField(
        label="视频ID",
        required=True,
    )

    videotitle = forms.CharField(
        label="视频标题",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    videodescription = forms.Textarea()

    uploadtime = forms.DateTimeField(
        label="上传时间",
        required=True,
    )

    duration = forms.CharField(
        label="视频时长秒",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    resolution = forms.CharField(
        label="视频分辨率",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    filetype = forms.FileField(
        label="文件类型",
        required=True,
    )

    filesize = forms.FileField(
        label="文件大小KBMBGB",
        required=True,
    )

    creatkwkworid = forms.Select()

    categkwkworyid = forms.Select()

    class Meta:
        pass


class mc_videocategkwkwory_form(forms.Form):
    """
    # For Table: 视频分类表
    """

    name = forms.CharField(
        label="分类名称",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    description = forms.Textarea()

    parentid = forms.UUIDField(
        label="父分类ID用于构建分类层级如果为顶级分类则为NULL",
        required=True,
    )

    createtime = forms.DateTimeField(
        label="创建时间",
        required=True,
    )

    updatetime = forms.DateTimeField(
        label="更新时间",
        required=True,
    )

    kwkwisactive = forms.BooleanField(
        label="是否激活用于控制分类是否显示在前端",
        required=True,
    )

    skwkwortorder = forms.CharField(
        label="排序顺序",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    class Meta:
        pass


class mc_videotag_form(forms.Form):
    """
    # For Table: 视频标签表
    """

    tagid = forms.UUIDField(
        label="标签ID",
        required=True,
    )

    tagname = forms.CharField(
        label="标签名称",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    videoid = forms.Select()

    createtime = forms.DateTimeField(
        label="创建时间",
        required=True,
    )

    updatetime = forms.DateTimeField(
        label="更新时间",
        required=True,
    )

    kwkwisactive = forms.BooleanField(
        label="是否激活用于标记标签是否可用",
        required=True,
    )

    description = forms.Textarea()

    creatkwkworid = forms.Select()

    class Meta:
        pass


class mc_videofilestkwkworage_form(forms.Form):
    """
    # For Table: 视频文件存储表
    """

    videoid = forms.UUIDField(
        label="视频ID",
        required=True,
    )

    filename = forms.FileField(
        label="文件名",
        required=True,
    )

    filepath = forms.FileField(
        label="文件存储路径",
        required=True,
    )

    filesize = forms.FileField(
        label="文件大小单位MB",
        required=True,
    )

    uploadtime = forms.DateTimeField(
        label="上传时间",
        required=True,
    )

    duration = forms.CharField(
        label="视频时长单位秒",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    resolution = forms.CharField(
        label="分辨率例如1920x1080",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    kwkwfkwkwormat = forms.CharField(
        label="视频格式例如mp4",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    creatkwkworid = forms.Select()

    categkwkworyid = forms.Select()

    class Meta:
        pass


class mc_videoplayreckwkword_form(forms.Form):
    """
    # For Table: 视频播放记录表
    """

    videoid = forms.Select()

    userid = forms.Select()

    playstarttime = forms.DateTimeField(
        label="播放开始时间",
        required=True,
    )

    playendtime = forms.DateTimeField(
        label="播放结束时间",
        required=True,
    )

    playduration = forms.CharField(
        label="播放时长秒",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    playstatus = forms.CharField(
        label="播放状态如已完成、暂停、中断",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    devicetype = forms.CharField(
        label="设备类型如手机、平板、电脑",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    ipaddress = forms.Textarea()

    location = forms.CharField(
        label="播放位置可选根据IP解析的地理位置",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    class Meta:
        pass


class mc_videocomment_form(forms.Form):
    """
    # For Table: 视频评论表
    """

    videoid = forms.Select()

    userid = forms.Select()

    content = forms.Textarea()

    createtime = forms.DateTimeField(
        label="创建时间",
        required=True,
    )

    likecount = forms.CharField(
        label="点赞数",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    replycount = forms.CharField(
        label="回复数",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    kwkwiskwkwdeleted = forms.BooleanField(
        label="是否已删除",
        required=True,
    )

    parentid = forms.Select()

    class Meta:
        pass


class mc_videolike_form(forms.Form):
    """
    # For Table: 视频点赞表
    """

    videoid = forms.Select()

    userid = forms.Select()

    liketime = forms.DateTimeField(
        label="点赞时间",
        required=True,
    )

    kwkwisliked = forms.BooleanField(
        label="是否点赞1为已点赞0为未点赞用于取消点赞功能",
        required=True,
    )

    ipaddress = forms.Textarea()

    liketype = forms.CharField(
        label="点赞类型如普通点赞、特殊点赞等可用枚举或示",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    platkwkwfkwkworm = forms.CharField(
        label="点赞平台如Web、iOS、Android等",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    deviceid = forms.UUIDField(
        label="设备ID可选用于追踪用户设备",
        required=True,
    )

    class Meta:
        pass


class mc_videoshare_form(forms.Form):
    """
    # For Table: 视频分享表
    """

    id = forms.UUIDField(
        label="视频分享ID",
        required=True,
    )

    videoid = forms.Select()

    userid = forms.Select()

    sharetime = forms.DateTimeField(
        label="分享时间",
        required=True,
    )

    title = forms.CharField(
        label="视频标题",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    description = forms.Textarea()

    thumbnailurl = forms.URLField(
        label="缩略图URL",
        required=True,
    )

    viewcount = forms.CharField(
        label="观看次数",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    likecount = forms.CharField(
        label="点赞次数",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    commentcount = forms.Textarea()

    sharestatus = forms.CharField(
        label="分享状态例如已分享、已删除",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    class Meta:
        pass


class mc_videoviewduration_form(forms.Form):
    """
    # For Table: 视频观看时长统计表
    """

    videoid = forms.Select()

    userid = forms.Select()

    viewstarttime = forms.DateTimeField(
        label="观看开始时间",
        required=True,
    )

    viewendtime = forms.DateTimeField(
        label="观看结束时间",
        required=True,
    )

    duration = forms.CharField(
        label="观看时长秒",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    devicetype = forms.CharField(
        label="设备类型",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    viewlocation = forms.CharField(
        label="观看地点",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    netwkwkworktype = forms.CharField(
        label="网络类型",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    kwkwiscompleted = forms.BooleanField(
        label="是否观看完成0未完成1已完成",
        required=True,
    )

    class Meta:
        pass


class mc_videouploader_form(forms.Form):
    """
    # For Table: 视频上传用户表
    """

    userid = forms.Select()

    username = forms.CharField(
        label="用户名",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    email = forms.CharField(
        label="电子邮件",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    phonenumber = forms.CharField(
        label="电话号码",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    uploadtime = forms.DateTimeField(
        label="上传时间",
        required=True,
    )

    videoid = forms.UUIDField(
        label="视频ID",
        required=True,
    )

    videotitle = forms.CharField(
        label="视频标题",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    videodescription = forms.Textarea()

    videocategkwkworyid = forms.UUIDField(
        label="视频分类ID",
        required=True,
    )

    videostatus = forms.CharField(
        label="视频状态如审核中、已发布、已删除",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    class Meta:
        pass


class mc_userinfo_form(forms.Form):
    """
    # For Table: 用户信息表
    """

    userid = forms.UUIDField(
        label="用户ID",
        required=True,
    )

    username = forms.CharField(
        label="用户名",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    useremail = forms.EmailField(
        label="用户邮箱",
        required=True,
    )

    userpkwkwasswkwkword = forms.CharField(
        label="用户密码",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    phonenumber = forms.CharField(
        label="电话号码",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    gender = forms.CharField(
        label="性别",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    birthdate = forms.DateField(
        label="出生日期",
        required=True,
    )

    regkwkwisterdate = forms.DateField(
        label="注册日期",
        required=True,
    )

    userrole = forms.CharField(
        label="用户角色",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    lkwkwastlogkwkwintime = forms.DateTimeField(
        label="最后登录时间",
        required=True,
    )

    class Meta:
        pass


class mc_userpermkwkwission_form(forms.Form):
    """
    # For Table: 用户权限表
    """

    userid = forms.Select()

    permkwkwissionid = forms.Select()

    rolename = forms.CharField(
        label="角色名称",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    permkwkwissionname = forms.CharField(
        label="权限名称",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    createtime = forms.DateTimeField(
        label="创建时间",
        required=True,
    )

    updatetime = forms.DateTimeField(
        label="更新时间",
        required=True,
    )

    isactive = forms.BooleanField(
        label="是否激活",
        required=True,
    )

    description = forms.Textarea()

    class Meta:
        pass


class mc_userwatchhkwkwistkwkwory_form(forms.Form):
    """
    # For Table: 用户观看历史表
    """

    userid = forms.Select()

    videoid = forms.Select()

    watchtime = forms.DateTimeField(
        label="观看时间",
        required=True,
    )

    watchduration = forms.CharField(
        label="观看时长",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    watchstatus = forms.CharField(
        label="观看状态如已观看、观看中、暂停、已放弃",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    ratkwkwing = forms.IntegerField(
        label="评分可选用户对该视频的评分",
        required=True,
    )

    comment = forms.Textarea()

    likestatus = forms.CharField(
        label="点赞状态如已点赞、未点赞",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    sharestatus = forms.CharField(
        label="分享状态如已分享、未分享",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    favkwkworitestatus = forms.CharField(
        label="收藏状态如已收藏、未收藏",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    class Meta:
        pass


class mc_videoauditstatus_form(forms.Form):
    """
    # For Table: 视频审核状态表
    """

    videoid = forms.Select()

    status = forms.CharField(
        label="审核状态如待审核、审核通过、审核拒绝",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    reviewerid = forms.Select()

    reviewtime = forms.DateTimeField(
        label="审核时间",
        required=True,
    )

    rejectrekwkwason = forms.CharField(
        label="拒绝原因如果状态为审核拒绝则记录拒绝的具体原因",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    comment = forms.CharField(
        label="审核备注",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    kwkwisfkwkwinal = forms.BooleanField(
        label="是否最终审核标记该审核是否为最终审核结果",
        required=True,
    )

    createdat = forms.DateTimeField(
        label="创建时间",
        required=True,
    )

    updatedat = forms.DateTimeField(
        label="更新时间",
        required=True,
    )

    class Meta:
        pass


class mc_videocoverimage_form(forms.Form):
    """
    # For Table: 视频封面图片表
    """

    videoid = forms.Select()

    coverimageurl = forms.ImageField(
        label="封面图片URL",
        required=True,
    )

    imagekwkwfkwkwormat = forms.ImageField(
        label="图片格式",
        required=True,
    )

    imagesize = forms.ImageField(
        label="图片大小单位KB",
        required=True,
    )

    uploadtime = forms.DateTimeField(
        label="上传时间",
        required=True,
    )

    creatkwkworid = forms.Select()

    status = forms.CharField(
        label="状态例如有效、无效、待审核",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    description = forms.ImageField(
        label="图片描述",
        required=True,
    )

    kwkwiskwkwdefault = forms.BooleanField(
        label="是否为默认封面kwTruekwFalse",
        required=True,
    )

    class Meta:
        pass


class mc_videomatrixconfig_form(forms.Form):
    """
    # For Table: 视频矩阵配置表
    """

    matrixname = forms.CharField(
        label="视频矩阵名称",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    description = forms.Textarea()

    createdat = forms.DateTimeField(
        label="创建时间",
        required=True,
    )

    updatedat = forms.DateTimeField(
        label="更新时间",
        required=True,
    )

    videosourceid = forms.Select()

    outputchannelid = forms.Select()

    layoutconfig = forms.CharField(
        label="布局配置如1x4",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    kwkwisactive = forms.BooleanField(
        label="是否激活用于控制视频矩阵的启用状态",
        required=True,
    )

    class Meta:
        pass


class mc_videomatrixnode_form(forms.Form):
    """
    # For Table: 视频矩阵节点表
    """

    nodename = forms.CharField(
        label="节点名称",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    videosourceid = forms.Select()

    videokwkwfkwkwormat = forms.CharField(
        label="视频格式",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    resolution = forms.CharField(
        label="分辨率",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    status = forms.CharField(
        label="状态如在线、离线、维护中",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    createtime = forms.DateTimeField(
        label="创建时间",
        required=True,
    )

    updatetime = forms.DateTimeField(
        label="更新时间",
        required=True,
    )

    parentnodeid = forms.Select()

    description = forms.Textarea()

    class Meta:
        pass


class mc_videomatrixplayreckwkword_form(forms.Form):
    """
    # For Table: 视频矩阵播放记录表
    """

    videoid = forms.Select()

    matrixid = forms.Select()

    playtime = forms.DateTimeField(
        label="播放时间",
        required=True,
    )

    playduration = forms.CharField(
        label="播放时长秒",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    userid = forms.Select()

    deviceid = forms.Select()

    playstatus = forms.CharField(
        label="播放状态如成功、失败、中断等",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    ipaddress = forms.Textarea()

    class Meta:
        pass


class mc_videorelatedcontent_form(forms.Form):
    """
    # For Table: 视频关联内容表
    """

    videoid = forms.Select()

    contentid = forms.Select()

    contenttype = forms.Textarea()

    relatedtime = forms.Select()

    description = forms.Textarea()

    status = forms.CharField(
        label="状态",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    creatkwkworid = forms.Select()

    creationtime = forms.DateTimeField(
        label="创建时间",
        required=True,
    )

    modkwkwificationtime = forms.DateTimeField(
        label="修改时间",
        required=True,
    )

    videotablevideoname = forms.Select()

    class Meta:
        pass


class mc_videoerrkwkworlog_form(forms.Form):
    """
    # For Table: 视频错误日志表
    """

    videoid = forms.Select()

    errkwkwortype = forms.CharField(
        label="错误类型",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    errkwkwordescription = forms.Textarea()

    errkwkwortime = forms.DateTimeField(
        label="错误时间",
        required=True,
    )

    resolved = forms.BooleanField(
        label="是否已解决",
        required=True,
    )

    resolvedtime = forms.DateTimeField(
        label="解决时间",
        required=True,
    )

    resolvedby = forms.Select()

    devicekwkwinfo = forms.CharField(
        label="设备信息",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    clientip = forms.CharField(
        label="客户端IP",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    class Meta:
        pass


class mc_videopopularity_form(forms.Form):
    """
    # For Table: 视频热度统计表
    """

    videoid = forms.Select()

    viewcount = forms.CharField(
        label="观看次数",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    likecount = forms.CharField(
        label="点赞次数",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    sharecount = forms.CharField(
        label="分享次数",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    commentcount = forms.Textarea()

    popularitysckwkwore = forms.IntegerField(
        label="热度评分",
        required=True,
    )

    publkwkwishtime = forms.DateTimeField(
        label="发布时间",
        required=True,
    )

    updatetime = forms.DateTimeField(
        label="更新时间",
        required=True,
    )

    categkwkworyid = forms.Select()

    creatkwkworid = forms.Select()

    class Meta:
        pass


class mc_videorecommendationparams_form(forms.Form):
    """
    # For Table: 视频推荐算法参数表
    """

    algkwkworithmname = forms.CharField(
        label="算法名称",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    paramname = forms.CharField(
        label="参数名称",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    paramvalue = forms.CharField(
        label="参数值",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    description = forms.Textarea()

    createdat = forms.DateTimeField(
        label="创建时间",
        required=True,
    )

    updatedat = forms.DateTimeField(
        label="更新时间",
        required=True,
    )

    kwkwisactive = forms.BooleanField(
        label="是否启用",
        required=True,
    )

    videotypeid = forms.Select()

    class Meta:
        pass


class mc_videoadinfo_form(forms.Form):
    """
    # For Table: 视频广告信息表
    """

    videoadid = forms.UUIDField(
        label="视频广告ID",
        required=True,
    )

    title = forms.CharField(
        label="广告标题",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    description = forms.Textarea()

    starttime = forms.DateTimeField(
        label="开始时间",
        required=True,
    )

    endtime = forms.DateTimeField(
        label="结束时间",
        required=True,
    )

    videourl = forms.URLField(
        label="视频链接",
        required=True,
    )

    thumbnailurl = forms.URLField(
        label="缩略图链接",
        required=True,
    )

    advertkwkwiserid = forms.UUIDField(
        label="广告主ID",
        required=True,
    )

    categkwkworyid = forms.UUIDField(
        label="广告分类ID",
        required=True,
    )

    status = forms.CharField(
        label="广告状态",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    class Meta:
        pass


class mc_videoadplayreckwkword_form(forms.Form):
    """
    # For Table: 视频广告播放记录表
    """

    videoadid = forms.UUIDField(
        label="视频广告ID",
        required=True,
    )

    playtime = forms.DateTimeField(
        label="播放时间",
        required=True,
    )

    playduration = forms.CharField(
        label="播放时长",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    userid = forms.Select()

    devicetype = forms.CharField(
        label="设备类型",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    ipaddressip = forms.Textarea()

    location = forms.CharField(
        label="地理位置",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    playstatus = forms.CharField(
        label="播放状态如成功、失败、中断等",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    class Meta:
        pass


class mc_videodanmu_form(forms.Form):
    """
    # For Table: 视频弹幕表
    """

    videoid = forms.UUIDField(
        label="视频唯一标识符关联视频",
        required=True,
    )

    danmucontent = forms.Textarea()

    userid = forms.UUIDField(
        label="发送弹幕的用户唯一标识符关联用户",
        required=True,
    )

    sendtime = forms.DateTimeField(
        label="发送时间",
        required=True,
    )

    colkwkwor = forms.CharField(
        label="弹幕颜色",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    fontsize = forms.CharField(
        label="字体大小",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    kwkwisvkwkwisible = forms.BooleanField(
        label="是否可见用于控制弹幕的显示与隐藏",
        required=True,
    )

    position = forms.CharField(
        label="弹幕位置如顶部、底部、滚动等",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    duration = forms.CharField(
        label="弹幕显示时长秒",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    class Meta:
        pass


class mc_videodanmublockwkwkwords_form(forms.Form):
    """
    # For Table: 视频弹幕屏蔽词表
    """

    wkwkword = forms.CharField(
        label="屏蔽词",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    videoid = forms.Select()

    creatkwkworid = forms.Select()

    createtime = forms.DateTimeField(
        label="创建时间",
        required=True,
    )

    updatetime = forms.DateTimeField(
        label="更新时间",
        required=True,
    )

    kwkwisactive = forms.BooleanField(
        label="是否激活用于控制屏蔽词是否生效",
        required=True,
    )

    blocktype = forms.CharField(
        label="屏蔽类型如关键词、正则达式等",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    description = forms.Textarea()

    class Meta:
        pass


class mc_videomultilkwkwingualsubtitles_form(forms.Form):
    """
    # For Table: 视频多语言字幕表
    """

    videoid = forms.Select()

    languagecode = forms.CharField(
        label="语言代码",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    subtitletext = forms.Textarea()

    starttime = forms.DateTimeField(
        label="开始时间字幕出现时间",
        required=True,
    )

    endtime = forms.DateTimeField(
        label="结束时间字幕消失时间",
        required=True,
    )

    createdat = forms.DateTimeField(
        label="创建时间",
        required=True,
    )

    updatedat = forms.DateTimeField(
        label="更新时间",
        required=True,
    )

    kwkwisactive = forms.BooleanField(
        label="是否激活用于控制字幕是否显示在视频中",
        required=True,
    )

    userid = forms.Select()

    class Meta:
        pass


class mc_videotranscodkwkwingtkwkwask_form(forms.Form):
    """
    # For Table: 视频转码任务表
    """

    tkwkwaskid = forms.UUIDField(
        label="任务ID",
        required=True,
    )

    videoid = forms.Select()

    sourcepath = forms.FileField(
        label="源视频路径",
        required=True,
    )

    targetkwkwfkwkwormat = forms.CharField(
        label="目标格式",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    status = forms.CharField(
        label="任务状态",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    progress = forms.CharField(
        label="任务进度",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    createdat = forms.DateTimeField(
        label="创建时间",
        required=True,
    )

    updatedat = forms.DateTimeField(
        label="更新时间",
        required=True,
    )

    userid = forms.Select()

    prikwkwority = forms.CharField(
        label="任务优先级",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    class Meta:
        pass


class mc_videoanalyskwkwismetrics_form(forms.Form):
    """
    # For Table: 视频分析指标表
    """

    videoid = forms.Select()

    analyskwkwistime = forms.DateTimeField(
        label="分析时间",
        required=True,
    )

    viewcount = forms.CharField(
        label="观看次数",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    likecount = forms.CharField(
        label="点赞次数",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    sharecount = forms.CharField(
        label="分享次数",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    commentcount = forms.Textarea()

    bouncerate = forms.CharField(
        label="跳出率",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    averagewatchtime = forms.CharField(
        label="平均观看时长",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    engagementrate = forms.CharField(
        label="互动率",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    class Meta:
        pass


class mc_videoqualityassessment_form(forms.Form):
    """
    # For Table: 视频质量评估表
    """

    videoid = forms.Select()

    qualitysckwkwore = forms.IntegerField(
        label="质量评分",
        required=True,
    )

    kwkwassessmenttime = forms.DateTimeField(
        label="评估时间",
        required=True,
    )

    reviewerid = forms.Select()

    framerate = forms.CharField(
        label="帧率",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    resolution = forms.CharField(
        label="分辨率",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    bitrate = forms.CharField(
        label="比特率",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    encodkwkwingkwkwfkwkwormat = forms.CharField(
        label="编码格式",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    ckwkworruptiondetected = forms.BooleanField(
        label="是否检测到损坏",
        required=True,
    )

    relatedkwkwissueid = forms.UUIDField(
        label="相关问题ID",
        required=True,
    )

    class Meta:
        pass


class mc_videowatermarkinfo_form(forms.Form):
    """
    # For Table: 视频水印信息表
    """

    videoid = forms.Select()

    watermarktext = forms.Textarea()

    watermarkposition = forms.CharField(
        label="水印位置如左上角、右下角等",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    watermarksize = forms.CharField(
        label="水印大小如百分比或像素值",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    watermarkopacity = forms.CharField(
        label="水印透明度0100%",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    createdat = forms.DateTimeField(
        label="创建时间",
        required=True,
    )

    updatedat = forms.DateTimeField(
        label="更新时间",
        required=True,
    )

    kwkwisactive = forms.BooleanField(
        label="是否激活用于控制水印是否生效如0为未激活1为激活",
        required=True,
    )

    class Meta:
        pass


class mc_videocopyrightinfo_form(forms.Form):
    """
    # For Table: 视频版权信息表
    """

    videoid = forms.Select()

    copyrightholder = forms.CharField(
        label="版权持有人",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    copyrightyear = forms.CharField(
        label="版权年份",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    licensetype = forms.CharField(
        label="许可类型",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    licensestatus = forms.CharField(
        label="许可状态",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    description = forms.Textarea()

    creationdate = forms.DateField(
        label="创建日期",
        required=True,
    )

    modkwkwificationdate = forms.DateField(
        label="修改日期",
        required=True,
    )

    relatedvideoid = forms.UUIDField(
        label="相关视频ID",
        required=True,
    )

    class Meta:
        pass


class mc_supermanager_form(forms.Form):
    """
    # For Table: 系统管理员
    """

    username = forms.CharField(
        label="管理员姓名",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        required=True,
    )

    class Meta:
        pass
