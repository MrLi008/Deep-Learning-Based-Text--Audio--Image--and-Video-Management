# 用于对标 config_unit 增删改查接口

import requests
from concurrent import futures
from concurrent.futures import ThreadPoolExecutor

url = "http://localhost:9100"


def csrf_token():
    session = requests.Session()
    response = session.get(f"{url}/config_unit/ucsrf")
    response.raise_for_status()
    print(response.json())
    csrf = response.json().get("csrfToken")
    return csrf, session


def register_manager(obj):
    csrf, session = csrf_token()
    response = session.post(
        f"{url}/config_unit/register",
        data={
            "csrfmiddlewaretoken": csrf,
            **obj,
        },
    )
    response.raise_for_status()
    print(response.json())
    

def unit_post(tablename, optype, keys, item: dict):

    csrf, session = csrf_token()
    obj = dict()

    obj["optype"] = optype
    obj["csrfmiddlewaretoken"] = csrf

    for key in keys:
        obj[key] = item.get(key, "")
    print(obj)
    # 设置cookie csrftoken
    session.cookies.update({"csrftoken": csrf})

    response = session.post(f"{url}/config_unit/config_unit/{tablename}", data=obj)
    response.raise_for_status()
    return response.json()


# 并发-有序按顺序返回处理结果，会阻塞
def unit_post_concurrent(tablename, optype, keys, items: list):
    """
    批量提交
    :param tablename:
    :param optype:
    :param keys:
    :param items:
    :return:
    """

    def _unit_post(**kwargs):
        '''
            kwargs: dict
                dict: {"tablename": tablename, "optype": optype, "keys": keys, "item": item}
            
        '''
        keys = kwargs.get("keys")
        optype = kwargs.get("optype")

        obj = dict()

        obj["optype"] = optype
        obj["csrfmiddlewaretoken"] = csrf

        for key in keys:
            obj[key] = kwargs.get("item").get(key, "")
        print(obj)
        # 设置cookie csrftoken
        session.cookies.update({"csrftoken": csrf})

        response = session.post(f"{url}/config_unit/config_unit/{tablename}", data=obj)
        response.raise_for_status()
        return response.json()

    csrf, session = csrf_token()
    with ThreadPoolExecutor(max_workers=5) as executor:
        for future in [
            executor.submit(
                _unit_post, tablename=tablename, optype=optype, keys=keys, item=item
            )
            for item in items
        ]:
            try:
                res = future.result()
            except Exception as e:
                res = None
            yield res


# 并发-无序但知道第几个
def unit_post_concurrent(tablename, optype, keys, items: list):
    """
    批量提交
    :param tablename:
    :param optype:
    :param keys:
    :param items:
    :return:
    """

    def _unit_post(kwargs, index):
        '''
            kwargs: dict
                dict: {"tablename": tablename, "optype": optype, "keys": keys, "item": item}
            index: int
        '''
        keys = kwargs.get("keys")
        optype = kwargs.get("optype")

        obj = dict()

        obj["optype"] = optype
        obj["csrfmiddlewaretoken"] = csrf

        for key in keys:
            obj[key] = kwargs.get("item").get(key, "")
        print(obj)
        # 设置cookie csrftoken
        session.cookies.update({"csrftoken": csrf})

        response = session.post(f"{url}/config_unit/config_unit/{tablename}", data=obj)
        response.raise_for_status()
        return {
            'resp':response.json(), 
            'seqnumber':index
            }

    csrf, session = csrf_token()
    with ThreadPoolExecutor(max_workers=5) as executor:
        futures_list = [
            executor.submit(
                _unit_post,
                {"tablename": tablename, "optype": optype, "keys": keys, "item": item},
                index=index,
            )
            for index, item in enumerate(items)
        ]
        for future in futures.as_completed(futures_list):
            try:
                res = future.result()
            except Exception as e:
                res = None
            yield res





def unit_post_videoinfo_add(item):
    """
    【视频信息表】
    add
    item: add数据
    return: 提交结果
    """
    keys = [
    
        'videoid', # 视频ID【UUIDField】  非外键 
        'videotitle', # 视频标题【CharField】  非外键 
        'videodescription', # 视频描述【TextField】  非外键 
        'uploadtime', # 上传时间【DateTimeField】  非外键 
        'duration', # 视频时长秒【CharField】  非外键 
        'resolution', # 视频分辨率【CharField】  非外键 
        'filetype', # 文件类型【FileField】  非外键 
        'filesize', # 文件大小KBMBGB【FileField】  非外键 
        'creatkwkworid', # 创建者ID关联用户【SelectField】   userinfo  username 【用户名】
        'categkwkworyid', # 类别ID关联视频类别【SelectField】   videocategkwkwory  name 【分类名称】
        
    
    ]
    return unit_post('videoinfo', 'add', keys, item)
    
def unit_post_videoinfo_upd(item):
    """
    【视频信息表】
    upd
    item: upd数据
    return: 提交结果
    """
    keys = [
    
        'videoid', # 视频ID【UUIDField】  非外键 
        'videotitle', # 视频标题【CharField】  非外键 
        'videodescription', # 视频描述【TextField】  非外键 
        'uploadtime', # 上传时间【DateTimeField】  非外键 
        'duration', # 视频时长秒【CharField】  非外键 
        'resolution', # 视频分辨率【CharField】  非外键 
        'filetype', # 文件类型【FileField】  非外键 
        'filesize', # 文件大小KBMBGB【FileField】  非外键 
        'creatkwkworid', # 创建者ID关联用户【SelectField】   userinfo  username 【用户名】
        'categkwkworyid', # 类别ID关联视频类别【SelectField】   videocategkwkwory  name 【分类名称】
        
    
    ]
    return unit_post('videoinfo', 'upd', keys, item)
    
def unit_post_videoinfo_del(item):
    """
    【视频信息表】
    del
    item: del数据
    return: 提交结果
    """
    keys = [
    
        '_id', # 使用记录的ID查询
    
    ]
    return unit_post('videoinfo', 'del', keys, item)
    
def unit_post_videoinfo_get(item):
    """
    【视频信息表】
    get
    item: get数据
    return: 提交结果
    """
    keys = [
    
        '_id', # 使用记录的ID查询
    
    ]
    return unit_post('videoinfo', 'get', keys, item)
    
def unit_post_videoinfo_filter(item):
    """
    【视频信息表】
    filter
    item: filter数据
    return: 提交结果
    """
    keys = [
    
        'videoid', # 视频ID【UUIDField】  非外键 
        'videotitle', # 视频标题【CharField】  非外键 
        'videodescription', # 视频描述【TextField】  非外键 
        'uploadtime', # 上传时间【DateTimeField】  非外键 
        'duration', # 视频时长秒【CharField】  非外键 
        'resolution', # 视频分辨率【CharField】  非外键 
        'filetype', # 文件类型【FileField】  非外键 
        'filesize', # 文件大小KBMBGB【FileField】  非外键 
        'creatkwkworid', # 创建者ID关联用户【SelectField】   userinfo  username 【用户名】
        'categkwkworyid', # 类别ID关联视频类别【SelectField】   videocategkwkwory  name 【分类名称】
        
    
    ]
    return unit_post('videoinfo', 'filter', keys, item)
    
def unit_post_videoinfo_view(item):
    """
    【视频信息表】
    view
    item: view数据
    return: 提交结果
    """
    keys = [
    
        '_id', # 使用记录的ID查询
    
    ]
    return unit_post('videoinfo', 'view', keys, item)
    
def unit_post_videoinfo_go_add(item):
    """
    【视频信息表】
    go_add
    item: go_add数据
    return: 提交结果
    """
    keys = [
    
    {'form':{
        'id':'',
    }}
    
    ]
    return unit_post('videoinfo', 'go_add', keys, item)
    
def unit_post_videoinfo_go_upd(item):
    """
    【视频信息表】
    go_upd
    item: go_upd数据
    return: 提交结果
    """
    keys = [
    
    {'form':{
        'id':'',
    }}
    
    ]
    return unit_post('videoinfo', 'go_upd', keys, item)
    


def unit_post_videocategkwkwory_add(item):
    """
    【视频分类表】
    add
    item: add数据
    return: 提交结果
    """
    keys = [
    
        'name', # 分类名称【CharField】  非外键 
        'description', # 分类描述【TextField】  非外键 
        'parentid', # 父分类ID用于构建分类层级如果为顶级分类则为NULL【UUIDField】  非外键 
        'createtime', # 创建时间【DateTimeField】  非外键 
        'updatetime', # 更新时间【DateTimeField】  非外键 
        'kwkwisactive', # 是否激活用于控制分类是否显示在前端【BooleanField】  非外键 
        'skwkwortorder', # 排序顺序【CharField】  非外键 
        
    
    ]
    return unit_post('videocategkwkwory', 'add', keys, item)
    
def unit_post_videocategkwkwory_upd(item):
    """
    【视频分类表】
    upd
    item: upd数据
    return: 提交结果
    """
    keys = [
    
        'name', # 分类名称【CharField】  非外键 
        'description', # 分类描述【TextField】  非外键 
        'parentid', # 父分类ID用于构建分类层级如果为顶级分类则为NULL【UUIDField】  非外键 
        'createtime', # 创建时间【DateTimeField】  非外键 
        'updatetime', # 更新时间【DateTimeField】  非外键 
        'kwkwisactive', # 是否激活用于控制分类是否显示在前端【BooleanField】  非外键 
        'skwkwortorder', # 排序顺序【CharField】  非外键 
        
    
    ]
    return unit_post('videocategkwkwory', 'upd', keys, item)
    
def unit_post_videocategkwkwory_del(item):
    """
    【视频分类表】
    del
    item: del数据
    return: 提交结果
    """
    keys = [
    
        '_id', # 使用记录的ID查询
    
    ]
    return unit_post('videocategkwkwory', 'del', keys, item)
    
def unit_post_videocategkwkwory_get(item):
    """
    【视频分类表】
    get
    item: get数据
    return: 提交结果
    """
    keys = [
    
        '_id', # 使用记录的ID查询
    
    ]
    return unit_post('videocategkwkwory', 'get', keys, item)
    
def unit_post_videocategkwkwory_filter(item):
    """
    【视频分类表】
    filter
    item: filter数据
    return: 提交结果
    """
    keys = [
    
        'name', # 分类名称【CharField】  非外键 
        'description', # 分类描述【TextField】  非外键 
        'parentid', # 父分类ID用于构建分类层级如果为顶级分类则为NULL【UUIDField】  非外键 
        'createtime', # 创建时间【DateTimeField】  非外键 
        'updatetime', # 更新时间【DateTimeField】  非外键 
        'kwkwisactive', # 是否激活用于控制分类是否显示在前端【BooleanField】  非外键 
        'skwkwortorder', # 排序顺序【CharField】  非外键 
        
    
    ]
    return unit_post('videocategkwkwory', 'filter', keys, item)
    
def unit_post_videocategkwkwory_view(item):
    """
    【视频分类表】
    view
    item: view数据
    return: 提交结果
    """
    keys = [
    
        '_id', # 使用记录的ID查询
    
    ]
    return unit_post('videocategkwkwory', 'view', keys, item)
    
def unit_post_videocategkwkwory_go_add(item):
    """
    【视频分类表】
    go_add
    item: go_add数据
    return: 提交结果
    """
    keys = [
    
    {'form':{
        'id':'',
    }}
    
    ]
    return unit_post('videocategkwkwory', 'go_add', keys, item)
    
def unit_post_videocategkwkwory_go_upd(item):
    """
    【视频分类表】
    go_upd
    item: go_upd数据
    return: 提交结果
    """
    keys = [
    
    {'form':{
        'id':'',
    }}
    
    ]
    return unit_post('videocategkwkwory', 'go_upd', keys, item)
    


def unit_post_videotag_add(item):
    """
    【视频标签表】
    add
    item: add数据
    return: 提交结果
    """
    keys = [
    
        'tagid', # 标签ID【UUIDField】  非外键 
        'tagname', # 标签名称【CharField】  非外键 
        'videoid', # 视频ID关联字段指向视频中的视频ID【SelectField】   videoinfo  videotitle 【视频标题】
        'createtime', # 创建时间【DateTimeField】  非外键 
        'updatetime', # 更新时间【DateTimeField】  非外键 
        'kwkwisactive', # 是否激活用于标记标签是否可用【BooleanField】  非外键 
        'description', # 标签描述【TextField】  非外键 
        'creatkwkworid', # 创建者ID关联字段指向用户中的用户ID【SelectField】   userinfo  username 【用户名】
        
    
    ]
    return unit_post('videotag', 'add', keys, item)
    
def unit_post_videotag_upd(item):
    """
    【视频标签表】
    upd
    item: upd数据
    return: 提交结果
    """
    keys = [
    
        'tagid', # 标签ID【UUIDField】  非外键 
        'tagname', # 标签名称【CharField】  非外键 
        'videoid', # 视频ID关联字段指向视频中的视频ID【SelectField】   videoinfo  videotitle 【视频标题】
        'createtime', # 创建时间【DateTimeField】  非外键 
        'updatetime', # 更新时间【DateTimeField】  非外键 
        'kwkwisactive', # 是否激活用于标记标签是否可用【BooleanField】  非外键 
        'description', # 标签描述【TextField】  非外键 
        'creatkwkworid', # 创建者ID关联字段指向用户中的用户ID【SelectField】   userinfo  username 【用户名】
        
    
    ]
    return unit_post('videotag', 'upd', keys, item)
    
def unit_post_videotag_del(item):
    """
    【视频标签表】
    del
    item: del数据
    return: 提交结果
    """
    keys = [
    
        '_id', # 使用记录的ID查询
    
    ]
    return unit_post('videotag', 'del', keys, item)
    
def unit_post_videotag_get(item):
    """
    【视频标签表】
    get
    item: get数据
    return: 提交结果
    """
    keys = [
    
        '_id', # 使用记录的ID查询
    
    ]
    return unit_post('videotag', 'get', keys, item)
    
def unit_post_videotag_filter(item):
    """
    【视频标签表】
    filter
    item: filter数据
    return: 提交结果
    """
    keys = [
    
        'tagid', # 标签ID【UUIDField】  非外键 
        'tagname', # 标签名称【CharField】  非外键 
        'videoid', # 视频ID关联字段指向视频中的视频ID【SelectField】   videoinfo  videotitle 【视频标题】
        'createtime', # 创建时间【DateTimeField】  非外键 
        'updatetime', # 更新时间【DateTimeField】  非外键 
        'kwkwisactive', # 是否激活用于标记标签是否可用【BooleanField】  非外键 
        'description', # 标签描述【TextField】  非外键 
        'creatkwkworid', # 创建者ID关联字段指向用户中的用户ID【SelectField】   userinfo  username 【用户名】
        
    
    ]
    return unit_post('videotag', 'filter', keys, item)
    
def unit_post_videotag_view(item):
    """
    【视频标签表】
    view
    item: view数据
    return: 提交结果
    """
    keys = [
    
        '_id', # 使用记录的ID查询
    
    ]
    return unit_post('videotag', 'view', keys, item)
    
def unit_post_videotag_go_add(item):
    """
    【视频标签表】
    go_add
    item: go_add数据
    return: 提交结果
    """
    keys = [
    
    {'form':{
        'id':'',
    }}
    
    ]
    return unit_post('videotag', 'go_add', keys, item)
    
def unit_post_videotag_go_upd(item):
    """
    【视频标签表】
    go_upd
    item: go_upd数据
    return: 提交结果
    """
    keys = [
    
    {'form':{
        'id':'',
    }}
    
    ]
    return unit_post('videotag', 'go_upd', keys, item)
    


def unit_post_videofilestkwkworage_add(item):
    """
    【视频文件存储表】
    add
    item: add数据
    return: 提交结果
    """
    keys = [
    
        'videoid', # 视频ID【UUIDField】  非外键 
        'filename', # 文件名【FileField】  非外键 
        'filepath', # 文件存储路径【FileField】  非外键 
        'filesize', # 文件大小单位MB【FileField】  非外键 
        'uploadtime', # 上传时间【DateTimeField】  非外键 
        'duration', # 视频时长单位秒【CharField】  非外键 
        'resolution', # 分辨率例如1920x1080【CharField】  非外键 
        'kwkwfkwkwormat', # 视频格式例如mp4【CharField】  非外键 
        'creatkwkworid', # 创建者ID关联用户【SelectField】   userinfo  username 【用户名】
        'categkwkworyid', # 分类ID关联视频分类【SelectField】   videocategkwkwory  name 【分类名称】
        
    
    ]
    return unit_post('videofilestkwkworage', 'add', keys, item)
    
def unit_post_videofilestkwkworage_upd(item):
    """
    【视频文件存储表】
    upd
    item: upd数据
    return: 提交结果
    """
    keys = [
    
        'videoid', # 视频ID【UUIDField】  非外键 
        'filename', # 文件名【FileField】  非外键 
        'filepath', # 文件存储路径【FileField】  非外键 
        'filesize', # 文件大小单位MB【FileField】  非外键 
        'uploadtime', # 上传时间【DateTimeField】  非外键 
        'duration', # 视频时长单位秒【CharField】  非外键 
        'resolution', # 分辨率例如1920x1080【CharField】  非外键 
        'kwkwfkwkwormat', # 视频格式例如mp4【CharField】  非外键 
        'creatkwkworid', # 创建者ID关联用户【SelectField】   userinfo  username 【用户名】
        'categkwkworyid', # 分类ID关联视频分类【SelectField】   videocategkwkwory  name 【分类名称】
        
    
    ]
    return unit_post('videofilestkwkworage', 'upd', keys, item)
    
def unit_post_videofilestkwkworage_del(item):
    """
    【视频文件存储表】
    del
    item: del数据
    return: 提交结果
    """
    keys = [
    
        '_id', # 使用记录的ID查询
    
    ]
    return unit_post('videofilestkwkworage', 'del', keys, item)
    
def unit_post_videofilestkwkworage_get(item):
    """
    【视频文件存储表】
    get
    item: get数据
    return: 提交结果
    """
    keys = [
    
        '_id', # 使用记录的ID查询
    
    ]
    return unit_post('videofilestkwkworage', 'get', keys, item)
    
def unit_post_videofilestkwkworage_filter(item):
    """
    【视频文件存储表】
    filter
    item: filter数据
    return: 提交结果
    """
    keys = [
    
        'videoid', # 视频ID【UUIDField】  非外键 
        'filename', # 文件名【FileField】  非外键 
        'filepath', # 文件存储路径【FileField】  非外键 
        'filesize', # 文件大小单位MB【FileField】  非外键 
        'uploadtime', # 上传时间【DateTimeField】  非外键 
        'duration', # 视频时长单位秒【CharField】  非外键 
        'resolution', # 分辨率例如1920x1080【CharField】  非外键 
        'kwkwfkwkwormat', # 视频格式例如mp4【CharField】  非外键 
        'creatkwkworid', # 创建者ID关联用户【SelectField】   userinfo  username 【用户名】
        'categkwkworyid', # 分类ID关联视频分类【SelectField】   videocategkwkwory  name 【分类名称】
        
    
    ]
    return unit_post('videofilestkwkworage', 'filter', keys, item)
    
def unit_post_videofilestkwkworage_view(item):
    """
    【视频文件存储表】
    view
    item: view数据
    return: 提交结果
    """
    keys = [
    
        '_id', # 使用记录的ID查询
    
    ]
    return unit_post('videofilestkwkworage', 'view', keys, item)
    
def unit_post_videofilestkwkworage_go_add(item):
    """
    【视频文件存储表】
    go_add
    item: go_add数据
    return: 提交结果
    """
    keys = [
    
    {'form':{
        'id':'',
    }}
    
    ]
    return unit_post('videofilestkwkworage', 'go_add', keys, item)
    
def unit_post_videofilestkwkworage_go_upd(item):
    """
    【视频文件存储表】
    go_upd
    item: go_upd数据
    return: 提交结果
    """
    keys = [
    
    {'form':{
        'id':'',
    }}
    
    ]
    return unit_post('videofilestkwkworage', 'go_upd', keys, item)
    


def unit_post_videoplayreckwkword_add(item):
    """
    【视频播放记录表】
    add
    item: add数据
    return: 提交结果
    """
    keys = [
    
        'videoid', # 视频ID关联视频信息【SelectField】   videoinfo  videotitle 【视频标题】
        'userid', # 用户ID关联用户信息【SelectField】   userinfo  username 【用户名】
        'playstarttime', # 播放开始时间【DateTimeField】  非外键 
        'playendtime', # 播放结束时间【DateTimeField】  非外键 
        'playduration', # 播放时长秒【CharField】  非外键 
        'playstatus', # 播放状态如已完成、暂停、中断【CharField】  非外键 
        'devicetype', # 设备类型如手机、平板、电脑【CharField】  非外键 
        'ipaddress', # IP地址【TextField】  非外键 
        'location', # 播放位置可选根据IP解析的地理位置【CharField】  非外键 
        
    
    ]
    return unit_post('videoplayreckwkword', 'add', keys, item)
    
def unit_post_videoplayreckwkword_upd(item):
    """
    【视频播放记录表】
    upd
    item: upd数据
    return: 提交结果
    """
    keys = [
    
        'videoid', # 视频ID关联视频信息【SelectField】   videoinfo  videotitle 【视频标题】
        'userid', # 用户ID关联用户信息【SelectField】   userinfo  username 【用户名】
        'playstarttime', # 播放开始时间【DateTimeField】  非外键 
        'playendtime', # 播放结束时间【DateTimeField】  非外键 
        'playduration', # 播放时长秒【CharField】  非外键 
        'playstatus', # 播放状态如已完成、暂停、中断【CharField】  非外键 
        'devicetype', # 设备类型如手机、平板、电脑【CharField】  非外键 
        'ipaddress', # IP地址【TextField】  非外键 
        'location', # 播放位置可选根据IP解析的地理位置【CharField】  非外键 
        
    
    ]
    return unit_post('videoplayreckwkword', 'upd', keys, item)
    
def unit_post_videoplayreckwkword_del(item):
    """
    【视频播放记录表】
    del
    item: del数据
    return: 提交结果
    """
    keys = [
    
        '_id', # 使用记录的ID查询
    
    ]
    return unit_post('videoplayreckwkword', 'del', keys, item)
    
def unit_post_videoplayreckwkword_get(item):
    """
    【视频播放记录表】
    get
    item: get数据
    return: 提交结果
    """
    keys = [
    
        '_id', # 使用记录的ID查询
    
    ]
    return unit_post('videoplayreckwkword', 'get', keys, item)
    
def unit_post_videoplayreckwkword_filter(item):
    """
    【视频播放记录表】
    filter
    item: filter数据
    return: 提交结果
    """
    keys = [
    
        'videoid', # 视频ID关联视频信息【SelectField】   videoinfo  videotitle 【视频标题】
        'userid', # 用户ID关联用户信息【SelectField】   userinfo  username 【用户名】
        'playstarttime', # 播放开始时间【DateTimeField】  非外键 
        'playendtime', # 播放结束时间【DateTimeField】  非外键 
        'playduration', # 播放时长秒【CharField】  非外键 
        'playstatus', # 播放状态如已完成、暂停、中断【CharField】  非外键 
        'devicetype', # 设备类型如手机、平板、电脑【CharField】  非外键 
        'ipaddress', # IP地址【TextField】  非外键 
        'location', # 播放位置可选根据IP解析的地理位置【CharField】  非外键 
        
    
    ]
    return unit_post('videoplayreckwkword', 'filter', keys, item)
    
def unit_post_videoplayreckwkword_view(item):
    """
    【视频播放记录表】
    view
    item: view数据
    return: 提交结果
    """
    keys = [
    
        '_id', # 使用记录的ID查询
    
    ]
    return unit_post('videoplayreckwkword', 'view', keys, item)
    
def unit_post_videoplayreckwkword_go_add(item):
    """
    【视频播放记录表】
    go_add
    item: go_add数据
    return: 提交结果
    """
    keys = [
    
    {'form':{
        'id':'',
    }}
    
    ]
    return unit_post('videoplayreckwkword', 'go_add', keys, item)
    
def unit_post_videoplayreckwkword_go_upd(item):
    """
    【视频播放记录表】
    go_upd
    item: go_upd数据
    return: 提交结果
    """
    keys = [
    
    {'form':{
        'id':'',
    }}
    
    ]
    return unit_post('videoplayreckwkword', 'go_upd', keys, item)
    


def unit_post_videocomment_add(item):
    """
    【视频评论表】
    add
    item: add数据
    return: 提交结果
    """
    keys = [
    
        'videoid', # 关联视频ID【SelectField】   videoinfo  videotitle 【视频标题】
        'userid', # 关联用户ID【SelectField】   userinfo  username 【用户名】
        'content', # 评论内容【TextField】  非外键 
        'createtime', # 创建时间【DateTimeField】  非外键 
        'likecount', # 点赞数【CharField】  非外键 
        'replycount', # 回复数【CharField】  非外键 
        'kwkwiskwkwdeleted', # 是否已删除【BooleanField】  非外键 
        'parentid', # 关联父评论ID【SelectField】   videocomment  content 【评论内容】
        
    
    ]
    return unit_post('videocomment', 'add', keys, item)
    
def unit_post_videocomment_upd(item):
    """
    【视频评论表】
    upd
    item: upd数据
    return: 提交结果
    """
    keys = [
    
        'videoid', # 关联视频ID【SelectField】   videoinfo  videotitle 【视频标题】
        'userid', # 关联用户ID【SelectField】   userinfo  username 【用户名】
        'content', # 评论内容【TextField】  非外键 
        'createtime', # 创建时间【DateTimeField】  非外键 
        'likecount', # 点赞数【CharField】  非外键 
        'replycount', # 回复数【CharField】  非外键 
        'kwkwiskwkwdeleted', # 是否已删除【BooleanField】  非外键 
        'parentid', # 关联父评论ID【SelectField】   videocomment  content 【评论内容】
        
    
    ]
    return unit_post('videocomment', 'upd', keys, item)
    
def unit_post_videocomment_del(item):
    """
    【视频评论表】
    del
    item: del数据
    return: 提交结果
    """
    keys = [
    
        '_id', # 使用记录的ID查询
    
    ]
    return unit_post('videocomment', 'del', keys, item)
    
def unit_post_videocomment_get(item):
    """
    【视频评论表】
    get
    item: get数据
    return: 提交结果
    """
    keys = [
    
        '_id', # 使用记录的ID查询
    
    ]
    return unit_post('videocomment', 'get', keys, item)
    
def unit_post_videocomment_filter(item):
    """
    【视频评论表】
    filter
    item: filter数据
    return: 提交结果
    """
    keys = [
    
        'videoid', # 关联视频ID【SelectField】   videoinfo  videotitle 【视频标题】
        'userid', # 关联用户ID【SelectField】   userinfo  username 【用户名】
        'content', # 评论内容【TextField】  非外键 
        'createtime', # 创建时间【DateTimeField】  非外键 
        'likecount', # 点赞数【CharField】  非外键 
        'replycount', # 回复数【CharField】  非外键 
        'kwkwiskwkwdeleted', # 是否已删除【BooleanField】  非外键 
        'parentid', # 关联父评论ID【SelectField】   videocomment  content 【评论内容】
        
    
    ]
    return unit_post('videocomment', 'filter', keys, item)
    
def unit_post_videocomment_view(item):
    """
    【视频评论表】
    view
    item: view数据
    return: 提交结果
    """
    keys = [
    
        '_id', # 使用记录的ID查询
    
    ]
    return unit_post('videocomment', 'view', keys, item)
    
def unit_post_videocomment_go_add(item):
    """
    【视频评论表】
    go_add
    item: go_add数据
    return: 提交结果
    """
    keys = [
    
    {'form':{
        'id':'',
    }}
    
    ]
    return unit_post('videocomment', 'go_add', keys, item)
    
def unit_post_videocomment_go_upd(item):
    """
    【视频评论表】
    go_upd
    item: go_upd数据
    return: 提交结果
    """
    keys = [
    
    {'form':{
        'id':'',
    }}
    
    ]
    return unit_post('videocomment', 'go_upd', keys, item)
    


def unit_post_videolike_add(item):
    """
    【视频点赞表】
    add
    item: add数据
    return: 提交结果
    """
    keys = [
    
        'videoid', # 关联视频ID【SelectField】   videoinfo  videotitle 【视频标题】
        'userid', # 关联用户ID【SelectField】   userinfo  username 【用户名】
        'liketime', # 点赞时间【DateTimeField】  非外键 
        'kwkwisliked', # 是否点赞1为已点赞0为未点赞用于取消点赞功能【BooleanField】  非外键 
        'ipaddress', # 点赞时的IP地址【TextField】  非外键 
        'liketype', # 点赞类型如普通点赞、特殊点赞等可用枚举或示【CharField】  非外键 
        'platkwkwfkwkworm', # 点赞平台如Web、iOS、Android等【CharField】  非外键 
        'deviceid', # 设备ID可选用于追踪用户设备【UUIDField】  非外键 
        
    
    ]
    return unit_post('videolike', 'add', keys, item)
    
def unit_post_videolike_upd(item):
    """
    【视频点赞表】
    upd
    item: upd数据
    return: 提交结果
    """
    keys = [
    
        'videoid', # 关联视频ID【SelectField】   videoinfo  videotitle 【视频标题】
        'userid', # 关联用户ID【SelectField】   userinfo  username 【用户名】
        'liketime', # 点赞时间【DateTimeField】  非外键 
        'kwkwisliked', # 是否点赞1为已点赞0为未点赞用于取消点赞功能【BooleanField】  非外键 
        'ipaddress', # 点赞时的IP地址【TextField】  非外键 
        'liketype', # 点赞类型如普通点赞、特殊点赞等可用枚举或示【CharField】  非外键 
        'platkwkwfkwkworm', # 点赞平台如Web、iOS、Android等【CharField】  非外键 
        'deviceid', # 设备ID可选用于追踪用户设备【UUIDField】  非外键 
        
    
    ]
    return unit_post('videolike', 'upd', keys, item)
    
def unit_post_videolike_del(item):
    """
    【视频点赞表】
    del
    item: del数据
    return: 提交结果
    """
    keys = [
    
        '_id', # 使用记录的ID查询
    
    ]
    return unit_post('videolike', 'del', keys, item)
    
def unit_post_videolike_get(item):
    """
    【视频点赞表】
    get
    item: get数据
    return: 提交结果
    """
    keys = [
    
        '_id', # 使用记录的ID查询
    
    ]
    return unit_post('videolike', 'get', keys, item)
    
def unit_post_videolike_filter(item):
    """
    【视频点赞表】
    filter
    item: filter数据
    return: 提交结果
    """
    keys = [
    
        'videoid', # 关联视频ID【SelectField】   videoinfo  videotitle 【视频标题】
        'userid', # 关联用户ID【SelectField】   userinfo  username 【用户名】
        'liketime', # 点赞时间【DateTimeField】  非外键 
        'kwkwisliked', # 是否点赞1为已点赞0为未点赞用于取消点赞功能【BooleanField】  非外键 
        'ipaddress', # 点赞时的IP地址【TextField】  非外键 
        'liketype', # 点赞类型如普通点赞、特殊点赞等可用枚举或示【CharField】  非外键 
        'platkwkwfkwkworm', # 点赞平台如Web、iOS、Android等【CharField】  非外键 
        'deviceid', # 设备ID可选用于追踪用户设备【UUIDField】  非外键 
        
    
    ]
    return unit_post('videolike', 'filter', keys, item)
    
def unit_post_videolike_view(item):
    """
    【视频点赞表】
    view
    item: view数据
    return: 提交结果
    """
    keys = [
    
        '_id', # 使用记录的ID查询
    
    ]
    return unit_post('videolike', 'view', keys, item)
    
def unit_post_videolike_go_add(item):
    """
    【视频点赞表】
    go_add
    item: go_add数据
    return: 提交结果
    """
    keys = [
    
    {'form':{
        'id':'',
    }}
    
    ]
    return unit_post('videolike', 'go_add', keys, item)
    
def unit_post_videolike_go_upd(item):
    """
    【视频点赞表】
    go_upd
    item: go_upd数据
    return: 提交结果
    """
    keys = [
    
    {'form':{
        'id':'',
    }}
    
    ]
    return unit_post('videolike', 'go_upd', keys, item)
    


def unit_post_videoshare_add(item):
    """
    【视频分享表】
    add
    item: add数据
    return: 提交结果
    """
    keys = [
    
        'id', # 视频分享ID【UUIDField】  非外键 
        'videoid', # 关联视频ID【SelectField】   videoinfo  videotitle 【视频标题】
        'userid', # 关联用户ID【SelectField】   userinfo  username 【用户名】
        'sharetime', # 分享时间【DateTimeField】  非外键 
        'title', # 视频标题【CharField】  非外键 
        'description', # 视频描述【TextField】  非外键 
        'thumbnailurl', # 缩略图URL【URLField】  非外键 
        'viewcount', # 观看次数【CharField】  非外键 
        'likecount', # 点赞次数【CharField】  非外键 
        'commentcount', # 评论次数【TextField】  非外键 
        'sharestatus', # 分享状态例如已分享、已删除【CharField】  非外键 
        
    
    ]
    return unit_post('videoshare', 'add', keys, item)
    
def unit_post_videoshare_upd(item):
    """
    【视频分享表】
    upd
    item: upd数据
    return: 提交结果
    """
    keys = [
    
        'id', # 视频分享ID【UUIDField】  非外键 
        'videoid', # 关联视频ID【SelectField】   videoinfo  videotitle 【视频标题】
        'userid', # 关联用户ID【SelectField】   userinfo  username 【用户名】
        'sharetime', # 分享时间【DateTimeField】  非外键 
        'title', # 视频标题【CharField】  非外键 
        'description', # 视频描述【TextField】  非外键 
        'thumbnailurl', # 缩略图URL【URLField】  非外键 
        'viewcount', # 观看次数【CharField】  非外键 
        'likecount', # 点赞次数【CharField】  非外键 
        'commentcount', # 评论次数【TextField】  非外键 
        'sharestatus', # 分享状态例如已分享、已删除【CharField】  非外键 
        
    
    ]
    return unit_post('videoshare', 'upd', keys, item)
    
def unit_post_videoshare_del(item):
    """
    【视频分享表】
    del
    item: del数据
    return: 提交结果
    """
    keys = [
    
        '_id', # 使用记录的ID查询
    
    ]
    return unit_post('videoshare', 'del', keys, item)
    
def unit_post_videoshare_get(item):
    """
    【视频分享表】
    get
    item: get数据
    return: 提交结果
    """
    keys = [
    
        '_id', # 使用记录的ID查询
    
    ]
    return unit_post('videoshare', 'get', keys, item)
    
def unit_post_videoshare_filter(item):
    """
    【视频分享表】
    filter
    item: filter数据
    return: 提交结果
    """
    keys = [
    
        'id', # 视频分享ID【UUIDField】  非外键 
        'videoid', # 关联视频ID【SelectField】   videoinfo  videotitle 【视频标题】
        'userid', # 关联用户ID【SelectField】   userinfo  username 【用户名】
        'sharetime', # 分享时间【DateTimeField】  非外键 
        'title', # 视频标题【CharField】  非外键 
        'description', # 视频描述【TextField】  非外键 
        'thumbnailurl', # 缩略图URL【URLField】  非外键 
        'viewcount', # 观看次数【CharField】  非外键 
        'likecount', # 点赞次数【CharField】  非外键 
        'commentcount', # 评论次数【TextField】  非外键 
        'sharestatus', # 分享状态例如已分享、已删除【CharField】  非外键 
        
    
    ]
    return unit_post('videoshare', 'filter', keys, item)
    
def unit_post_videoshare_view(item):
    """
    【视频分享表】
    view
    item: view数据
    return: 提交结果
    """
    keys = [
    
        '_id', # 使用记录的ID查询
    
    ]
    return unit_post('videoshare', 'view', keys, item)
    
def unit_post_videoshare_go_add(item):
    """
    【视频分享表】
    go_add
    item: go_add数据
    return: 提交结果
    """
    keys = [
    
    {'form':{
        'id':'',
    }}
    
    ]
    return unit_post('videoshare', 'go_add', keys, item)
    
def unit_post_videoshare_go_upd(item):
    """
    【视频分享表】
    go_upd
    item: go_upd数据
    return: 提交结果
    """
    keys = [
    
    {'form':{
        'id':'',
    }}
    
    ]
    return unit_post('videoshare', 'go_upd', keys, item)
    


def unit_post_videoviewduration_add(item):
    """
    【视频观看时长统计表】
    add
    item: add数据
    return: 提交结果
    """
    keys = [
    
        'videoid', # 关联视频ID【SelectField】   videoinfo  videotitle 【视频标题】
        'userid', # 关联用户ID【SelectField】   userinfo  username 【用户名】
        'viewstarttime', # 观看开始时间【DateTimeField】  非外键 
        'viewendtime', # 观看结束时间【DateTimeField】  非外键 
        'duration', # 观看时长秒【CharField】  非外键 
        'devicetype', # 设备类型【CharField】  非外键 
        'viewlocation', # 观看地点【CharField】  非外键 
        'netwkwkworktype', # 网络类型【CharField】  非外键 
        'kwkwiscompleted', # 是否观看完成0未完成1已完成【BooleanField】  非外键 
        
    
    ]
    return unit_post('videoviewduration', 'add', keys, item)
    
def unit_post_videoviewduration_upd(item):
    """
    【视频观看时长统计表】
    upd
    item: upd数据
    return: 提交结果
    """
    keys = [
    
        'videoid', # 关联视频ID【SelectField】   videoinfo  videotitle 【视频标题】
        'userid', # 关联用户ID【SelectField】   userinfo  username 【用户名】
        'viewstarttime', # 观看开始时间【DateTimeField】  非外键 
        'viewendtime', # 观看结束时间【DateTimeField】  非外键 
        'duration', # 观看时长秒【CharField】  非外键 
        'devicetype', # 设备类型【CharField】  非外键 
        'viewlocation', # 观看地点【CharField】  非外键 
        'netwkwkworktype', # 网络类型【CharField】  非外键 
        'kwkwiscompleted', # 是否观看完成0未完成1已完成【BooleanField】  非外键 
        
    
    ]
    return unit_post('videoviewduration', 'upd', keys, item)
    
def unit_post_videoviewduration_del(item):
    """
    【视频观看时长统计表】
    del
    item: del数据
    return: 提交结果
    """
    keys = [
    
        '_id', # 使用记录的ID查询
    
    ]
    return unit_post('videoviewduration', 'del', keys, item)
    
def unit_post_videoviewduration_get(item):
    """
    【视频观看时长统计表】
    get
    item: get数据
    return: 提交结果
    """
    keys = [
    
        '_id', # 使用记录的ID查询
    
    ]
    return unit_post('videoviewduration', 'get', keys, item)
    
def unit_post_videoviewduration_filter(item):
    """
    【视频观看时长统计表】
    filter
    item: filter数据
    return: 提交结果
    """
    keys = [
    
        'videoid', # 关联视频ID【SelectField】   videoinfo  videotitle 【视频标题】
        'userid', # 关联用户ID【SelectField】   userinfo  username 【用户名】
        'viewstarttime', # 观看开始时间【DateTimeField】  非外键 
        'viewendtime', # 观看结束时间【DateTimeField】  非外键 
        'duration', # 观看时长秒【CharField】  非外键 
        'devicetype', # 设备类型【CharField】  非外键 
        'viewlocation', # 观看地点【CharField】  非外键 
        'netwkwkworktype', # 网络类型【CharField】  非外键 
        'kwkwiscompleted', # 是否观看完成0未完成1已完成【BooleanField】  非外键 
        
    
    ]
    return unit_post('videoviewduration', 'filter', keys, item)
    
def unit_post_videoviewduration_view(item):
    """
    【视频观看时长统计表】
    view
    item: view数据
    return: 提交结果
    """
    keys = [
    
        '_id', # 使用记录的ID查询
    
    ]
    return unit_post('videoviewduration', 'view', keys, item)
    
def unit_post_videoviewduration_go_add(item):
    """
    【视频观看时长统计表】
    go_add
    item: go_add数据
    return: 提交结果
    """
    keys = [
    
    {'form':{
        'id':'',
    }}
    
    ]
    return unit_post('videoviewduration', 'go_add', keys, item)
    
def unit_post_videoviewduration_go_upd(item):
    """
    【视频观看时长统计表】
    go_upd
    item: go_upd数据
    return: 提交结果
    """
    keys = [
    
    {'form':{
        'id':'',
    }}
    
    ]
    return unit_post('videoviewduration', 'go_upd', keys, item)
    


def unit_post_videouploader_add(item):
    """
    【视频上传用户表】
    add
    item: add数据
    return: 提交结果
    """
    keys = [
    
        'userid', # 关联用户ID【SelectField】   userinfo  username 【用户名】
        'username', # 用户名【CharField】  非外键 
        'email', # 电子邮件【CharField】  非外键 
        'phonenumber', # 电话号码【CharField】  非外键 
        'uploadtime', # 上传时间【DateTimeField】  非外键 
        'videoid', # 视频ID【UUIDField】  非外键 
        'videotitle', # 视频标题【CharField】  非外键 
        'videodescription', # 视频描述【TextField】  非外键 
        'videocategkwkworyid', # 视频分类ID【UUIDField】  非外键 
        'videostatus', # 视频状态如审核中、已发布、已删除【CharField】  非外键 
        
    
    ]
    return unit_post('videouploader', 'add', keys, item)
    
def unit_post_videouploader_upd(item):
    """
    【视频上传用户表】
    upd
    item: upd数据
    return: 提交结果
    """
    keys = [
    
        'userid', # 关联用户ID【SelectField】   userinfo  username 【用户名】
        'username', # 用户名【CharField】  非外键 
        'email', # 电子邮件【CharField】  非外键 
        'phonenumber', # 电话号码【CharField】  非外键 
        'uploadtime', # 上传时间【DateTimeField】  非外键 
        'videoid', # 视频ID【UUIDField】  非外键 
        'videotitle', # 视频标题【CharField】  非外键 
        'videodescription', # 视频描述【TextField】  非外键 
        'videocategkwkworyid', # 视频分类ID【UUIDField】  非外键 
        'videostatus', # 视频状态如审核中、已发布、已删除【CharField】  非外键 
        
    
    ]
    return unit_post('videouploader', 'upd', keys, item)
    
def unit_post_videouploader_del(item):
    """
    【视频上传用户表】
    del
    item: del数据
    return: 提交结果
    """
    keys = [
    
        '_id', # 使用记录的ID查询
    
    ]
    return unit_post('videouploader', 'del', keys, item)
    
def unit_post_videouploader_get(item):
    """
    【视频上传用户表】
    get
    item: get数据
    return: 提交结果
    """
    keys = [
    
        '_id', # 使用记录的ID查询
    
    ]
    return unit_post('videouploader', 'get', keys, item)
    
def unit_post_videouploader_filter(item):
    """
    【视频上传用户表】
    filter
    item: filter数据
    return: 提交结果
    """
    keys = [
    
        'userid', # 关联用户ID【SelectField】   userinfo  username 【用户名】
        'username', # 用户名【CharField】  非外键 
        'email', # 电子邮件【CharField】  非外键 
        'phonenumber', # 电话号码【CharField】  非外键 
        'uploadtime', # 上传时间【DateTimeField】  非外键 
        'videoid', # 视频ID【UUIDField】  非外键 
        'videotitle', # 视频标题【CharField】  非外键 
        'videodescription', # 视频描述【TextField】  非外键 
        'videocategkwkworyid', # 视频分类ID【UUIDField】  非外键 
        'videostatus', # 视频状态如审核中、已发布、已删除【CharField】  非外键 
        
    
    ]
    return unit_post('videouploader', 'filter', keys, item)
    
def unit_post_videouploader_view(item):
    """
    【视频上传用户表】
    view
    item: view数据
    return: 提交结果
    """
    keys = [
    
        '_id', # 使用记录的ID查询
    
    ]
    return unit_post('videouploader', 'view', keys, item)
    
def unit_post_videouploader_go_add(item):
    """
    【视频上传用户表】
    go_add
    item: go_add数据
    return: 提交结果
    """
    keys = [
    
    {'form':{
        'id':'',
    }}
    
    ]
    return unit_post('videouploader', 'go_add', keys, item)
    
def unit_post_videouploader_go_upd(item):
    """
    【视频上传用户表】
    go_upd
    item: go_upd数据
    return: 提交结果
    """
    keys = [
    
    {'form':{
        'id':'',
    }}
    
    ]
    return unit_post('videouploader', 'go_upd', keys, item)
    


def unit_post_userinfo_add(item):
    """
    【用户信息表】
    add
    item: add数据
    return: 提交结果
    """
    keys = [
    
        'userid', # 用户ID【UUIDField】  非外键 
        'username', # 用户名【CharField】  非外键 
        'useremail', # 用户邮箱【EmailField】  非外键 
        'userpkwkwasswkwkword', # 用户密码【CharField】  非外键 
        'phonenumber', # 电话号码【CharField】  非外键 
        'gender', # 性别【CharField】  非外键 
        'birthdate', # 出生日期【DateField】  非外键 
        'regkwkwisterdate', # 注册日期【DateField】  非外键 
        'userrole', # 用户角色【CharField】  非外键 
        'lkwkwastlogkwkwintime', # 最后登录时间【DateTimeField】  非外键 
        
    
    ]
    return unit_post('userinfo', 'add', keys, item)
    
def unit_post_userinfo_upd(item):
    """
    【用户信息表】
    upd
    item: upd数据
    return: 提交结果
    """
    keys = [
    
        'userid', # 用户ID【UUIDField】  非外键 
        'username', # 用户名【CharField】  非外键 
        'useremail', # 用户邮箱【EmailField】  非外键 
        'userpkwkwasswkwkword', # 用户密码【CharField】  非外键 
        'phonenumber', # 电话号码【CharField】  非外键 
        'gender', # 性别【CharField】  非外键 
        'birthdate', # 出生日期【DateField】  非外键 
        'regkwkwisterdate', # 注册日期【DateField】  非外键 
        'userrole', # 用户角色【CharField】  非外键 
        'lkwkwastlogkwkwintime', # 最后登录时间【DateTimeField】  非外键 
        
    
    ]
    return unit_post('userinfo', 'upd', keys, item)
    
def unit_post_userinfo_del(item):
    """
    【用户信息表】
    del
    item: del数据
    return: 提交结果
    """
    keys = [
    
        '_id', # 使用记录的ID查询
    
    ]
    return unit_post('userinfo', 'del', keys, item)
    
def unit_post_userinfo_get(item):
    """
    【用户信息表】
    get
    item: get数据
    return: 提交结果
    """
    keys = [
    
        '_id', # 使用记录的ID查询
    
    ]
    return unit_post('userinfo', 'get', keys, item)
    
def unit_post_userinfo_filter(item):
    """
    【用户信息表】
    filter
    item: filter数据
    return: 提交结果
    """
    keys = [
    
        'userid', # 用户ID【UUIDField】  非外键 
        'username', # 用户名【CharField】  非外键 
        'useremail', # 用户邮箱【EmailField】  非外键 
        'userpkwkwasswkwkword', # 用户密码【CharField】  非外键 
        'phonenumber', # 电话号码【CharField】  非外键 
        'gender', # 性别【CharField】  非外键 
        'birthdate', # 出生日期【DateField】  非外键 
        'regkwkwisterdate', # 注册日期【DateField】  非外键 
        'userrole', # 用户角色【CharField】  非外键 
        'lkwkwastlogkwkwintime', # 最后登录时间【DateTimeField】  非外键 
        
    
    ]
    return unit_post('userinfo', 'filter', keys, item)
    
def unit_post_userinfo_view(item):
    """
    【用户信息表】
    view
    item: view数据
    return: 提交结果
    """
    keys = [
    
        '_id', # 使用记录的ID查询
    
    ]
    return unit_post('userinfo', 'view', keys, item)
    
def unit_post_userinfo_go_add(item):
    """
    【用户信息表】
    go_add
    item: go_add数据
    return: 提交结果
    """
    keys = [
    
    {'form':{
        'id':'',
    }}
    
    ]
    return unit_post('userinfo', 'go_add', keys, item)
    
def unit_post_userinfo_go_upd(item):
    """
    【用户信息表】
    go_upd
    item: go_upd数据
    return: 提交结果
    """
    keys = [
    
    {'form':{
        'id':'',
    }}
    
    ]
    return unit_post('userinfo', 'go_upd', keys, item)
    


def unit_post_userpermkwkwission_add(item):
    """
    【用户权限表】
    add
    item: add数据
    return: 提交结果
    """
    keys = [
    
        'userid', # 关联用户ID【SelectField】   userinfo  username 【用户名】
        'permkwkwissionid', # 关联权限ID【SelectField】   userpermkwkwission  permkwkwissionid 【关联权限ID】
        'rolename', # 角色名称【CharField】  非外键 
        'permkwkwissionname', # 权限名称【CharField】  非外键 
        'createtime', # 创建时间【DateTimeField】  非外键 
        'updatetime', # 更新时间【DateTimeField】  非外键 
        'isactive', # 是否激活【BooleanField】  非外键 
        'description', # 描述【TextField】  非外键 
        
    
    ]
    return unit_post('userpermkwkwission', 'add', keys, item)
    
def unit_post_userpermkwkwission_upd(item):
    """
    【用户权限表】
    upd
    item: upd数据
    return: 提交结果
    """
    keys = [
    
        'userid', # 关联用户ID【SelectField】   userinfo  username 【用户名】
        'permkwkwissionid', # 关联权限ID【SelectField】   userpermkwkwission  permkwkwissionid 【关联权限ID】
        'rolename', # 角色名称【CharField】  非外键 
        'permkwkwissionname', # 权限名称【CharField】  非外键 
        'createtime', # 创建时间【DateTimeField】  非外键 
        'updatetime', # 更新时间【DateTimeField】  非外键 
        'isactive', # 是否激活【BooleanField】  非外键 
        'description', # 描述【TextField】  非外键 
        
    
    ]
    return unit_post('userpermkwkwission', 'upd', keys, item)
    
def unit_post_userpermkwkwission_del(item):
    """
    【用户权限表】
    del
    item: del数据
    return: 提交结果
    """
    keys = [
    
        '_id', # 使用记录的ID查询
    
    ]
    return unit_post('userpermkwkwission', 'del', keys, item)
    
def unit_post_userpermkwkwission_get(item):
    """
    【用户权限表】
    get
    item: get数据
    return: 提交结果
    """
    keys = [
    
        '_id', # 使用记录的ID查询
    
    ]
    return unit_post('userpermkwkwission', 'get', keys, item)
    
def unit_post_userpermkwkwission_filter(item):
    """
    【用户权限表】
    filter
    item: filter数据
    return: 提交结果
    """
    keys = [
    
        'userid', # 关联用户ID【SelectField】   userinfo  username 【用户名】
        'permkwkwissionid', # 关联权限ID【SelectField】   userpermkwkwission  permkwkwissionid 【关联权限ID】
        'rolename', # 角色名称【CharField】  非外键 
        'permkwkwissionname', # 权限名称【CharField】  非外键 
        'createtime', # 创建时间【DateTimeField】  非外键 
        'updatetime', # 更新时间【DateTimeField】  非外键 
        'isactive', # 是否激活【BooleanField】  非外键 
        'description', # 描述【TextField】  非外键 
        
    
    ]
    return unit_post('userpermkwkwission', 'filter', keys, item)
    
def unit_post_userpermkwkwission_view(item):
    """
    【用户权限表】
    view
    item: view数据
    return: 提交结果
    """
    keys = [
    
        '_id', # 使用记录的ID查询
    
    ]
    return unit_post('userpermkwkwission', 'view', keys, item)
    
def unit_post_userpermkwkwission_go_add(item):
    """
    【用户权限表】
    go_add
    item: go_add数据
    return: 提交结果
    """
    keys = [
    
    {'form':{
        'id':'',
    }}
    
    ]
    return unit_post('userpermkwkwission', 'go_add', keys, item)
    
def unit_post_userpermkwkwission_go_upd(item):
    """
    【用户权限表】
    go_upd
    item: go_upd数据
    return: 提交结果
    """
    keys = [
    
    {'form':{
        'id':'',
    }}
    
    ]
    return unit_post('userpermkwkwission', 'go_upd', keys, item)
    


def unit_post_userwatchhkwkwistkwkwory_add(item):
    """
    【用户观看历史表】
    add
    item: add数据
    return: 提交结果
    """
    keys = [
    
        'userid', # 关联用户ID【SelectField】   userinfo  username 【用户名】
        'videoid', # 关联视频ID【SelectField】   videoinfo  videotitle 【视频标题】
        'watchtime', # 观看时间【DateTimeField】  非外键 
        'watchduration', # 观看时长【CharField】  非外键 
        'watchstatus', # 观看状态如已观看、观看中、暂停、已放弃【CharField】  非外键 
        'ratkwkwing', # 评分可选用户对该视频的评分【IntegerField】  非外键 
        'comment', # 评论可选用户对该视频的评论【TextField】  非外键 
        'likestatus', # 点赞状态如已点赞、未点赞【CharField】  非外键 
        'sharestatus', # 分享状态如已分享、未分享【CharField】  非外键 
        'favkwkworitestatus', # 收藏状态如已收藏、未收藏【CharField】  非外键 
        
    
    ]
    return unit_post('userwatchhkwkwistkwkwory', 'add', keys, item)
    
def unit_post_userwatchhkwkwistkwkwory_upd(item):
    """
    【用户观看历史表】
    upd
    item: upd数据
    return: 提交结果
    """
    keys = [
    
        'userid', # 关联用户ID【SelectField】   userinfo  username 【用户名】
        'videoid', # 关联视频ID【SelectField】   videoinfo  videotitle 【视频标题】
        'watchtime', # 观看时间【DateTimeField】  非外键 
        'watchduration', # 观看时长【CharField】  非外键 
        'watchstatus', # 观看状态如已观看、观看中、暂停、已放弃【CharField】  非外键 
        'ratkwkwing', # 评分可选用户对该视频的评分【IntegerField】  非外键 
        'comment', # 评论可选用户对该视频的评论【TextField】  非外键 
        'likestatus', # 点赞状态如已点赞、未点赞【CharField】  非外键 
        'sharestatus', # 分享状态如已分享、未分享【CharField】  非外键 
        'favkwkworitestatus', # 收藏状态如已收藏、未收藏【CharField】  非外键 
        
    
    ]
    return unit_post('userwatchhkwkwistkwkwory', 'upd', keys, item)
    
def unit_post_userwatchhkwkwistkwkwory_del(item):
    """
    【用户观看历史表】
    del
    item: del数据
    return: 提交结果
    """
    keys = [
    
        '_id', # 使用记录的ID查询
    
    ]
    return unit_post('userwatchhkwkwistkwkwory', 'del', keys, item)
    
def unit_post_userwatchhkwkwistkwkwory_get(item):
    """
    【用户观看历史表】
    get
    item: get数据
    return: 提交结果
    """
    keys = [
    
        '_id', # 使用记录的ID查询
    
    ]
    return unit_post('userwatchhkwkwistkwkwory', 'get', keys, item)
    
def unit_post_userwatchhkwkwistkwkwory_filter(item):
    """
    【用户观看历史表】
    filter
    item: filter数据
    return: 提交结果
    """
    keys = [
    
        'userid', # 关联用户ID【SelectField】   userinfo  username 【用户名】
        'videoid', # 关联视频ID【SelectField】   videoinfo  videotitle 【视频标题】
        'watchtime', # 观看时间【DateTimeField】  非外键 
        'watchduration', # 观看时长【CharField】  非外键 
        'watchstatus', # 观看状态如已观看、观看中、暂停、已放弃【CharField】  非外键 
        'ratkwkwing', # 评分可选用户对该视频的评分【IntegerField】  非外键 
        'comment', # 评论可选用户对该视频的评论【TextField】  非外键 
        'likestatus', # 点赞状态如已点赞、未点赞【CharField】  非外键 
        'sharestatus', # 分享状态如已分享、未分享【CharField】  非外键 
        'favkwkworitestatus', # 收藏状态如已收藏、未收藏【CharField】  非外键 
        
    
    ]
    return unit_post('userwatchhkwkwistkwkwory', 'filter', keys, item)
    
def unit_post_userwatchhkwkwistkwkwory_view(item):
    """
    【用户观看历史表】
    view
    item: view数据
    return: 提交结果
    """
    keys = [
    
        '_id', # 使用记录的ID查询
    
    ]
    return unit_post('userwatchhkwkwistkwkwory', 'view', keys, item)
    
def unit_post_userwatchhkwkwistkwkwory_go_add(item):
    """
    【用户观看历史表】
    go_add
    item: go_add数据
    return: 提交结果
    """
    keys = [
    
    {'form':{
        'id':'',
    }}
    
    ]
    return unit_post('userwatchhkwkwistkwkwory', 'go_add', keys, item)
    
def unit_post_userwatchhkwkwistkwkwory_go_upd(item):
    """
    【用户观看历史表】
    go_upd
    item: go_upd数据
    return: 提交结果
    """
    keys = [
    
    {'form':{
        'id':'',
    }}
    
    ]
    return unit_post('userwatchhkwkwistkwkwory', 'go_upd', keys, item)
    


def unit_post_videoauditstatus_add(item):
    """
    【视频审核状态表】
    add
    item: add数据
    return: 提交结果
    """
    keys = [
    
        'videoid', # 视频ID关联字段指向视频的ID【SelectField】   videoinfo  videotitle 【视频标题】
        'status', # 审核状态如待审核、审核通过、审核拒绝【CharField】  非外键 
        'reviewerid', # 审核员ID关联字段指向审核员的ID【SelectField】   supermanager  username 【管理员姓名】
        'reviewtime', # 审核时间【DateTimeField】  非外键 
        'rejectrekwkwason', # 拒绝原因如果状态为审核拒绝则记录拒绝的具体原因【CharField】  非外键 
        'comment', # 审核备注【CharField】  非外键 
        'kwkwisfkwkwinal', # 是否最终审核标记该审核是否为最终审核结果【BooleanField】  非外键 
        'createdat', # 创建时间【DateTimeField】  非外键 
        'updatedat', # 更新时间【DateTimeField】  非外键 
        
    
    ]
    return unit_post('videoauditstatus', 'add', keys, item)
    
def unit_post_videoauditstatus_upd(item):
    """
    【视频审核状态表】
    upd
    item: upd数据
    return: 提交结果
    """
    keys = [
    
        'videoid', # 视频ID关联字段指向视频的ID【SelectField】   videoinfo  videotitle 【视频标题】
        'status', # 审核状态如待审核、审核通过、审核拒绝【CharField】  非外键 
        'reviewerid', # 审核员ID关联字段指向审核员的ID【SelectField】   supermanager  username 【管理员姓名】
        'reviewtime', # 审核时间【DateTimeField】  非外键 
        'rejectrekwkwason', # 拒绝原因如果状态为审核拒绝则记录拒绝的具体原因【CharField】  非外键 
        'comment', # 审核备注【CharField】  非外键 
        'kwkwisfkwkwinal', # 是否最终审核标记该审核是否为最终审核结果【BooleanField】  非外键 
        'createdat', # 创建时间【DateTimeField】  非外键 
        'updatedat', # 更新时间【DateTimeField】  非外键 
        
    
    ]
    return unit_post('videoauditstatus', 'upd', keys, item)
    
def unit_post_videoauditstatus_del(item):
    """
    【视频审核状态表】
    del
    item: del数据
    return: 提交结果
    """
    keys = [
    
        '_id', # 使用记录的ID查询
    
    ]
    return unit_post('videoauditstatus', 'del', keys, item)
    
def unit_post_videoauditstatus_get(item):
    """
    【视频审核状态表】
    get
    item: get数据
    return: 提交结果
    """
    keys = [
    
        '_id', # 使用记录的ID查询
    
    ]
    return unit_post('videoauditstatus', 'get', keys, item)
    
def unit_post_videoauditstatus_filter(item):
    """
    【视频审核状态表】
    filter
    item: filter数据
    return: 提交结果
    """
    keys = [
    
        'videoid', # 视频ID关联字段指向视频的ID【SelectField】   videoinfo  videotitle 【视频标题】
        'status', # 审核状态如待审核、审核通过、审核拒绝【CharField】  非外键 
        'reviewerid', # 审核员ID关联字段指向审核员的ID【SelectField】   supermanager  username 【管理员姓名】
        'reviewtime', # 审核时间【DateTimeField】  非外键 
        'rejectrekwkwason', # 拒绝原因如果状态为审核拒绝则记录拒绝的具体原因【CharField】  非外键 
        'comment', # 审核备注【CharField】  非外键 
        'kwkwisfkwkwinal', # 是否最终审核标记该审核是否为最终审核结果【BooleanField】  非外键 
        'createdat', # 创建时间【DateTimeField】  非外键 
        'updatedat', # 更新时间【DateTimeField】  非外键 
        
    
    ]
    return unit_post('videoauditstatus', 'filter', keys, item)
    
def unit_post_videoauditstatus_view(item):
    """
    【视频审核状态表】
    view
    item: view数据
    return: 提交结果
    """
    keys = [
    
        '_id', # 使用记录的ID查询
    
    ]
    return unit_post('videoauditstatus', 'view', keys, item)
    
def unit_post_videoauditstatus_go_add(item):
    """
    【视频审核状态表】
    go_add
    item: go_add数据
    return: 提交结果
    """
    keys = [
    
    {'form':{
        'id':'',
    }}
    
    ]
    return unit_post('videoauditstatus', 'go_add', keys, item)
    
def unit_post_videoauditstatus_go_upd(item):
    """
    【视频审核状态表】
    go_upd
    item: go_upd数据
    return: 提交结果
    """
    keys = [
    
    {'form':{
        'id':'',
    }}
    
    ]
    return unit_post('videoauditstatus', 'go_upd', keys, item)
    


def unit_post_videocoverimage_add(item):
    """
    【视频封面图片表】
    add
    item: add数据
    return: 提交结果
    """
    keys = [
    
        'videoid', # 视频ID关联字段指向视频的【SelectField】   videoinfo  videotitle 【视频标题】
        'coverimageurl', # 封面图片URL【ImageField】  非外键 
        'imagekwkwfkwkwormat', # 图片格式【ImageField】  非外键 
        'imagesize', # 图片大小单位KB【ImageField】  非外键 
        'uploadtime', # 上传时间【DateTimeField】  非外键 
        'creatkwkworid', # 创建者ID关联字段指向用户的【SelectField】   userinfo  username 【用户名】
        'status', # 状态例如有效、无效、待审核【CharField】  非外键 
        'description', # 图片描述【ImageField】  非外键 
        'kwkwiskwkwdefault', # 是否为默认封面kwTruekwFalse【BooleanField】  非外键 
        
    
    ]
    return unit_post('videocoverimage', 'add', keys, item)
    
def unit_post_videocoverimage_upd(item):
    """
    【视频封面图片表】
    upd
    item: upd数据
    return: 提交结果
    """
    keys = [
    
        'videoid', # 视频ID关联字段指向视频的【SelectField】   videoinfo  videotitle 【视频标题】
        'coverimageurl', # 封面图片URL【ImageField】  非外键 
        'imagekwkwfkwkwormat', # 图片格式【ImageField】  非外键 
        'imagesize', # 图片大小单位KB【ImageField】  非外键 
        'uploadtime', # 上传时间【DateTimeField】  非外键 
        'creatkwkworid', # 创建者ID关联字段指向用户的【SelectField】   userinfo  username 【用户名】
        'status', # 状态例如有效、无效、待审核【CharField】  非外键 
        'description', # 图片描述【ImageField】  非外键 
        'kwkwiskwkwdefault', # 是否为默认封面kwTruekwFalse【BooleanField】  非外键 
        
    
    ]
    return unit_post('videocoverimage', 'upd', keys, item)
    
def unit_post_videocoverimage_del(item):
    """
    【视频封面图片表】
    del
    item: del数据
    return: 提交结果
    """
    keys = [
    
        '_id', # 使用记录的ID查询
    
    ]
    return unit_post('videocoverimage', 'del', keys, item)
    
def unit_post_videocoverimage_get(item):
    """
    【视频封面图片表】
    get
    item: get数据
    return: 提交结果
    """
    keys = [
    
        '_id', # 使用记录的ID查询
    
    ]
    return unit_post('videocoverimage', 'get', keys, item)
    
def unit_post_videocoverimage_filter(item):
    """
    【视频封面图片表】
    filter
    item: filter数据
    return: 提交结果
    """
    keys = [
    
        'videoid', # 视频ID关联字段指向视频的【SelectField】   videoinfo  videotitle 【视频标题】
        'coverimageurl', # 封面图片URL【ImageField】  非外键 
        'imagekwkwfkwkwormat', # 图片格式【ImageField】  非外键 
        'imagesize', # 图片大小单位KB【ImageField】  非外键 
        'uploadtime', # 上传时间【DateTimeField】  非外键 
        'creatkwkworid', # 创建者ID关联字段指向用户的【SelectField】   userinfo  username 【用户名】
        'status', # 状态例如有效、无效、待审核【CharField】  非外键 
        'description', # 图片描述【ImageField】  非外键 
        'kwkwiskwkwdefault', # 是否为默认封面kwTruekwFalse【BooleanField】  非外键 
        
    
    ]
    return unit_post('videocoverimage', 'filter', keys, item)
    
def unit_post_videocoverimage_view(item):
    """
    【视频封面图片表】
    view
    item: view数据
    return: 提交结果
    """
    keys = [
    
        '_id', # 使用记录的ID查询
    
    ]
    return unit_post('videocoverimage', 'view', keys, item)
    
def unit_post_videocoverimage_go_add(item):
    """
    【视频封面图片表】
    go_add
    item: go_add数据
    return: 提交结果
    """
    keys = [
    
    {'form':{
        'id':'',
    }}
    
    ]
    return unit_post('videocoverimage', 'go_add', keys, item)
    
def unit_post_videocoverimage_go_upd(item):
    """
    【视频封面图片表】
    go_upd
    item: go_upd数据
    return: 提交结果
    """
    keys = [
    
    {'form':{
        'id':'',
    }}
    
    ]
    return unit_post('videocoverimage', 'go_upd', keys, item)
    


def unit_post_videomatrixconfig_add(item):
    """
    【视频矩阵配置表】
    add
    item: add数据
    return: 提交结果
    """
    keys = [
    
        'matrixname', # 视频矩阵名称【CharField】  非外键 
        'description', # 描述信息【TextField】  非外键 
        'createdat', # 创建时间【DateTimeField】  非外键 
        'updatedat', # 更新时间【DateTimeField】  非外键 
        'videosourceid', # 视频源ID关联视频源【SelectField】   videoinfo  videotitle 【视频标题】
        'outputchannelid', # 输出通道ID关联输出通道【SelectField】   videofilestkwkworage  filename 【文件名】
        'layoutconfig', # 布局配置如1x4【CharField】  非外键 
        'kwkwisactive', # 是否激活用于控制视频矩阵的启用状态【BooleanField】  非外键 
        
    
    ]
    return unit_post('videomatrixconfig', 'add', keys, item)
    
def unit_post_videomatrixconfig_upd(item):
    """
    【视频矩阵配置表】
    upd
    item: upd数据
    return: 提交结果
    """
    keys = [
    
        'matrixname', # 视频矩阵名称【CharField】  非外键 
        'description', # 描述信息【TextField】  非外键 
        'createdat', # 创建时间【DateTimeField】  非外键 
        'updatedat', # 更新时间【DateTimeField】  非外键 
        'videosourceid', # 视频源ID关联视频源【SelectField】   videoinfo  videotitle 【视频标题】
        'outputchannelid', # 输出通道ID关联输出通道【SelectField】   videofilestkwkworage  filename 【文件名】
        'layoutconfig', # 布局配置如1x4【CharField】  非外键 
        'kwkwisactive', # 是否激活用于控制视频矩阵的启用状态【BooleanField】  非外键 
        
    
    ]
    return unit_post('videomatrixconfig', 'upd', keys, item)
    
def unit_post_videomatrixconfig_del(item):
    """
    【视频矩阵配置表】
    del
    item: del数据
    return: 提交结果
    """
    keys = [
    
        '_id', # 使用记录的ID查询
    
    ]
    return unit_post('videomatrixconfig', 'del', keys, item)
    
def unit_post_videomatrixconfig_get(item):
    """
    【视频矩阵配置表】
    get
    item: get数据
    return: 提交结果
    """
    keys = [
    
        '_id', # 使用记录的ID查询
    
    ]
    return unit_post('videomatrixconfig', 'get', keys, item)
    
def unit_post_videomatrixconfig_filter(item):
    """
    【视频矩阵配置表】
    filter
    item: filter数据
    return: 提交结果
    """
    keys = [
    
        'matrixname', # 视频矩阵名称【CharField】  非外键 
        'description', # 描述信息【TextField】  非外键 
        'createdat', # 创建时间【DateTimeField】  非外键 
        'updatedat', # 更新时间【DateTimeField】  非外键 
        'videosourceid', # 视频源ID关联视频源【SelectField】   videoinfo  videotitle 【视频标题】
        'outputchannelid', # 输出通道ID关联输出通道【SelectField】   videofilestkwkworage  filename 【文件名】
        'layoutconfig', # 布局配置如1x4【CharField】  非外键 
        'kwkwisactive', # 是否激活用于控制视频矩阵的启用状态【BooleanField】  非外键 
        
    
    ]
    return unit_post('videomatrixconfig', 'filter', keys, item)
    
def unit_post_videomatrixconfig_view(item):
    """
    【视频矩阵配置表】
    view
    item: view数据
    return: 提交结果
    """
    keys = [
    
        '_id', # 使用记录的ID查询
    
    ]
    return unit_post('videomatrixconfig', 'view', keys, item)
    
def unit_post_videomatrixconfig_go_add(item):
    """
    【视频矩阵配置表】
    go_add
    item: go_add数据
    return: 提交结果
    """
    keys = [
    
    {'form':{
        'id':'',
    }}
    
    ]
    return unit_post('videomatrixconfig', 'go_add', keys, item)
    
def unit_post_videomatrixconfig_go_upd(item):
    """
    【视频矩阵配置表】
    go_upd
    item: go_upd数据
    return: 提交结果
    """
    keys = [
    
    {'form':{
        'id':'',
    }}
    
    ]
    return unit_post('videomatrixconfig', 'go_upd', keys, item)
    


def unit_post_videomatrixnode_add(item):
    """
    【视频矩阵节点表】
    add
    item: add数据
    return: 提交结果
    """
    keys = [
    
        'nodename', # 节点名称【CharField】  非外键 
        'videosourceid', # 关联视频源ID【SelectField】   videoinfo  videotitle 【视频标题】
        'videokwkwfkwkwormat', # 视频格式【CharField】  非外键 
        'resolution', # 分辨率【CharField】  非外键 
        'status', # 状态如在线、离线、维护中【CharField】  非外键 
        'createtime', # 创建时间【DateTimeField】  非外键 
        'updatetime', # 更新时间【DateTimeField】  非外键 
        'parentnodeid', # 关联父节点ID用于示节点之间的层级关系【SelectField】   videomatrixnode  nodename 【节点名称】
        'description', # 描述信息【TextField】  非外键 
        
    
    ]
    return unit_post('videomatrixnode', 'add', keys, item)
    
def unit_post_videomatrixnode_upd(item):
    """
    【视频矩阵节点表】
    upd
    item: upd数据
    return: 提交结果
    """
    keys = [
    
        'nodename', # 节点名称【CharField】  非外键 
        'videosourceid', # 关联视频源ID【SelectField】   videoinfo  videotitle 【视频标题】
        'videokwkwfkwkwormat', # 视频格式【CharField】  非外键 
        'resolution', # 分辨率【CharField】  非外键 
        'status', # 状态如在线、离线、维护中【CharField】  非外键 
        'createtime', # 创建时间【DateTimeField】  非外键 
        'updatetime', # 更新时间【DateTimeField】  非外键 
        'parentnodeid', # 关联父节点ID用于示节点之间的层级关系【SelectField】   videomatrixnode  nodename 【节点名称】
        'description', # 描述信息【TextField】  非外键 
        
    
    ]
    return unit_post('videomatrixnode', 'upd', keys, item)
    
def unit_post_videomatrixnode_del(item):
    """
    【视频矩阵节点表】
    del
    item: del数据
    return: 提交结果
    """
    keys = [
    
        '_id', # 使用记录的ID查询
    
    ]
    return unit_post('videomatrixnode', 'del', keys, item)
    
def unit_post_videomatrixnode_get(item):
    """
    【视频矩阵节点表】
    get
    item: get数据
    return: 提交结果
    """
    keys = [
    
        '_id', # 使用记录的ID查询
    
    ]
    return unit_post('videomatrixnode', 'get', keys, item)
    
def unit_post_videomatrixnode_filter(item):
    """
    【视频矩阵节点表】
    filter
    item: filter数据
    return: 提交结果
    """
    keys = [
    
        'nodename', # 节点名称【CharField】  非外键 
        'videosourceid', # 关联视频源ID【SelectField】   videoinfo  videotitle 【视频标题】
        'videokwkwfkwkwormat', # 视频格式【CharField】  非外键 
        'resolution', # 分辨率【CharField】  非外键 
        'status', # 状态如在线、离线、维护中【CharField】  非外键 
        'createtime', # 创建时间【DateTimeField】  非外键 
        'updatetime', # 更新时间【DateTimeField】  非外键 
        'parentnodeid', # 关联父节点ID用于示节点之间的层级关系【SelectField】   videomatrixnode  nodename 【节点名称】
        'description', # 描述信息【TextField】  非外键 
        
    
    ]
    return unit_post('videomatrixnode', 'filter', keys, item)
    
def unit_post_videomatrixnode_view(item):
    """
    【视频矩阵节点表】
    view
    item: view数据
    return: 提交结果
    """
    keys = [
    
        '_id', # 使用记录的ID查询
    
    ]
    return unit_post('videomatrixnode', 'view', keys, item)
    
def unit_post_videomatrixnode_go_add(item):
    """
    【视频矩阵节点表】
    go_add
    item: go_add数据
    return: 提交结果
    """
    keys = [
    
    {'form':{
        'id':'',
    }}
    
    ]
    return unit_post('videomatrixnode', 'go_add', keys, item)
    
def unit_post_videomatrixnode_go_upd(item):
    """
    【视频矩阵节点表】
    go_upd
    item: go_upd数据
    return: 提交结果
    """
    keys = [
    
    {'form':{
        'id':'',
    }}
    
    ]
    return unit_post('videomatrixnode', 'go_upd', keys, item)
    


def unit_post_videomatrixplayreckwkword_add(item):
    """
    【视频矩阵播放记录表】
    add
    item: add数据
    return: 提交结果
    """
    keys = [
    
        'videoid', # 视频ID关联视频【SelectField】   videoinfo  videotitle 【视频标题】
        'matrixid', # 矩阵ID关联视频矩阵【SelectField】   videomatrixconfig  matrixname 【视频矩阵名称】
        'playtime', # 播放时间【DateTimeField】  非外键 
        'playduration', # 播放时长秒【CharField】  非外键 
        'userid', # 用户ID关联用户【SelectField】   userinfo  username 【用户名】
        'deviceid', # 设备ID关联设备【SelectField】   videomatrixplayreckwkword  deviceid 【设备ID关联设备】
        'playstatus', # 播放状态如成功、失败、中断等【CharField】  非外键 
        'ipaddress', # 播放请求的IP地址【TextField】  非外键 
        
    
    ]
    return unit_post('videomatrixplayreckwkword', 'add', keys, item)
    
def unit_post_videomatrixplayreckwkword_upd(item):
    """
    【视频矩阵播放记录表】
    upd
    item: upd数据
    return: 提交结果
    """
    keys = [
    
        'videoid', # 视频ID关联视频【SelectField】   videoinfo  videotitle 【视频标题】
        'matrixid', # 矩阵ID关联视频矩阵【SelectField】   videomatrixconfig  matrixname 【视频矩阵名称】
        'playtime', # 播放时间【DateTimeField】  非外键 
        'playduration', # 播放时长秒【CharField】  非外键 
        'userid', # 用户ID关联用户【SelectField】   userinfo  username 【用户名】
        'deviceid', # 设备ID关联设备【SelectField】   videomatrixplayreckwkword  deviceid 【设备ID关联设备】
        'playstatus', # 播放状态如成功、失败、中断等【CharField】  非外键 
        'ipaddress', # 播放请求的IP地址【TextField】  非外键 
        
    
    ]
    return unit_post('videomatrixplayreckwkword', 'upd', keys, item)
    
def unit_post_videomatrixplayreckwkword_del(item):
    """
    【视频矩阵播放记录表】
    del
    item: del数据
    return: 提交结果
    """
    keys = [
    
        '_id', # 使用记录的ID查询
    
    ]
    return unit_post('videomatrixplayreckwkword', 'del', keys, item)
    
def unit_post_videomatrixplayreckwkword_get(item):
    """
    【视频矩阵播放记录表】
    get
    item: get数据
    return: 提交结果
    """
    keys = [
    
        '_id', # 使用记录的ID查询
    
    ]
    return unit_post('videomatrixplayreckwkword', 'get', keys, item)
    
def unit_post_videomatrixplayreckwkword_filter(item):
    """
    【视频矩阵播放记录表】
    filter
    item: filter数据
    return: 提交结果
    """
    keys = [
    
        'videoid', # 视频ID关联视频【SelectField】   videoinfo  videotitle 【视频标题】
        'matrixid', # 矩阵ID关联视频矩阵【SelectField】   videomatrixconfig  matrixname 【视频矩阵名称】
        'playtime', # 播放时间【DateTimeField】  非外键 
        'playduration', # 播放时长秒【CharField】  非外键 
        'userid', # 用户ID关联用户【SelectField】   userinfo  username 【用户名】
        'deviceid', # 设备ID关联设备【SelectField】   videomatrixplayreckwkword  deviceid 【设备ID关联设备】
        'playstatus', # 播放状态如成功、失败、中断等【CharField】  非外键 
        'ipaddress', # 播放请求的IP地址【TextField】  非外键 
        
    
    ]
    return unit_post('videomatrixplayreckwkword', 'filter', keys, item)
    
def unit_post_videomatrixplayreckwkword_view(item):
    """
    【视频矩阵播放记录表】
    view
    item: view数据
    return: 提交结果
    """
    keys = [
    
        '_id', # 使用记录的ID查询
    
    ]
    return unit_post('videomatrixplayreckwkword', 'view', keys, item)
    
def unit_post_videomatrixplayreckwkword_go_add(item):
    """
    【视频矩阵播放记录表】
    go_add
    item: go_add数据
    return: 提交结果
    """
    keys = [
    
    {'form':{
        'id':'',
    }}
    
    ]
    return unit_post('videomatrixplayreckwkword', 'go_add', keys, item)
    
def unit_post_videomatrixplayreckwkword_go_upd(item):
    """
    【视频矩阵播放记录表】
    go_upd
    item: go_upd数据
    return: 提交结果
    """
    keys = [
    
    {'form':{
        'id':'',
    }}
    
    ]
    return unit_post('videomatrixplayreckwkword', 'go_upd', keys, item)
    


def unit_post_videorelatedcontent_add(item):
    """
    【视频关联内容表】
    add
    item: add数据
    return: 提交结果
    """
    keys = [
    
        'videoid', # 关联视频ID【SelectField】   videoinfo  videotitle 【视频标题】
        'contentid', # 关联内容ID【SelectField】   videocomment  content 【评论内容】
        'contenttype', # 内容类型【TextField】  非外键 
        'relatedtime', # 关联时间【SelectField】   videorelatedcontent  relatedtime 【关联时间】
        'description', # 描述【TextField】  非外键 
        'status', # 状态【CharField】  非外键 
        'creatkwkworid', # 关联创建者ID【SelectField】   userinfo  username 【用户名】
        'creationtime', # 创建时间【DateTimeField】  非外键 
        'modkwkwificationtime', # 修改时间【DateTimeField】  非外键 
        'videotablevideoname', # 视频名称关联字段视频名假设为VideoTable关联字段为视频名称【SelectField】   videoinfo  videotitle 【视频标题】
        
    
    ]
    return unit_post('videorelatedcontent', 'add', keys, item)
    
def unit_post_videorelatedcontent_upd(item):
    """
    【视频关联内容表】
    upd
    item: upd数据
    return: 提交结果
    """
    keys = [
    
        'videoid', # 关联视频ID【SelectField】   videoinfo  videotitle 【视频标题】
        'contentid', # 关联内容ID【SelectField】   videocomment  content 【评论内容】
        'contenttype', # 内容类型【TextField】  非外键 
        'relatedtime', # 关联时间【SelectField】   videorelatedcontent  relatedtime 【关联时间】
        'description', # 描述【TextField】  非外键 
        'status', # 状态【CharField】  非外键 
        'creatkwkworid', # 关联创建者ID【SelectField】   userinfo  username 【用户名】
        'creationtime', # 创建时间【DateTimeField】  非外键 
        'modkwkwificationtime', # 修改时间【DateTimeField】  非外键 
        'videotablevideoname', # 视频名称关联字段视频名假设为VideoTable关联字段为视频名称【SelectField】   videoinfo  videotitle 【视频标题】
        
    
    ]
    return unit_post('videorelatedcontent', 'upd', keys, item)
    
def unit_post_videorelatedcontent_del(item):
    """
    【视频关联内容表】
    del
    item: del数据
    return: 提交结果
    """
    keys = [
    
        '_id', # 使用记录的ID查询
    
    ]
    return unit_post('videorelatedcontent', 'del', keys, item)
    
def unit_post_videorelatedcontent_get(item):
    """
    【视频关联内容表】
    get
    item: get数据
    return: 提交结果
    """
    keys = [
    
        '_id', # 使用记录的ID查询
    
    ]
    return unit_post('videorelatedcontent', 'get', keys, item)
    
def unit_post_videorelatedcontent_filter(item):
    """
    【视频关联内容表】
    filter
    item: filter数据
    return: 提交结果
    """
    keys = [
    
        'videoid', # 关联视频ID【SelectField】   videoinfo  videotitle 【视频标题】
        'contentid', # 关联内容ID【SelectField】   videocomment  content 【评论内容】
        'contenttype', # 内容类型【TextField】  非外键 
        'relatedtime', # 关联时间【SelectField】   videorelatedcontent  relatedtime 【关联时间】
        'description', # 描述【TextField】  非外键 
        'status', # 状态【CharField】  非外键 
        'creatkwkworid', # 关联创建者ID【SelectField】   userinfo  username 【用户名】
        'creationtime', # 创建时间【DateTimeField】  非外键 
        'modkwkwificationtime', # 修改时间【DateTimeField】  非外键 
        'videotablevideoname', # 视频名称关联字段视频名假设为VideoTable关联字段为视频名称【SelectField】   videoinfo  videotitle 【视频标题】
        
    
    ]
    return unit_post('videorelatedcontent', 'filter', keys, item)
    
def unit_post_videorelatedcontent_view(item):
    """
    【视频关联内容表】
    view
    item: view数据
    return: 提交结果
    """
    keys = [
    
        '_id', # 使用记录的ID查询
    
    ]
    return unit_post('videorelatedcontent', 'view', keys, item)
    
def unit_post_videorelatedcontent_go_add(item):
    """
    【视频关联内容表】
    go_add
    item: go_add数据
    return: 提交结果
    """
    keys = [
    
    {'form':{
        'id':'',
    }}
    
    ]
    return unit_post('videorelatedcontent', 'go_add', keys, item)
    
def unit_post_videorelatedcontent_go_upd(item):
    """
    【视频关联内容表】
    go_upd
    item: go_upd数据
    return: 提交结果
    """
    keys = [
    
    {'form':{
        'id':'',
    }}
    
    ]
    return unit_post('videorelatedcontent', 'go_upd', keys, item)
    


def unit_post_videoerrkwkworlog_add(item):
    """
    【视频错误日志表】
    add
    item: add数据
    return: 提交结果
    """
    keys = [
    
        'videoid', # 关联视频ID【SelectField】   videoinfo  videotitle 【视频标题】
        'errkwkwortype', # 错误类型【CharField】  非外键 
        'errkwkwordescription', # 错误描述【TextField】  非外键 
        'errkwkwortime', # 错误时间【DateTimeField】  非外键 
        'resolved', # 是否已解决【BooleanField】  非外键 
        'resolvedtime', # 解决时间【DateTimeField】  非外键 
        'resolvedby', # 关联解决人【SelectField】   supermanager  username 【管理员姓名】
        'devicekwkwinfo', # 设备信息【CharField】  非外键 
        'clientip', # 客户端IP【CharField】  非外键 
        
    
    ]
    return unit_post('videoerrkwkworlog', 'add', keys, item)
    
def unit_post_videoerrkwkworlog_upd(item):
    """
    【视频错误日志表】
    upd
    item: upd数据
    return: 提交结果
    """
    keys = [
    
        'videoid', # 关联视频ID【SelectField】   videoinfo  videotitle 【视频标题】
        'errkwkwortype', # 错误类型【CharField】  非外键 
        'errkwkwordescription', # 错误描述【TextField】  非外键 
        'errkwkwortime', # 错误时间【DateTimeField】  非外键 
        'resolved', # 是否已解决【BooleanField】  非外键 
        'resolvedtime', # 解决时间【DateTimeField】  非外键 
        'resolvedby', # 关联解决人【SelectField】   supermanager  username 【管理员姓名】
        'devicekwkwinfo', # 设备信息【CharField】  非外键 
        'clientip', # 客户端IP【CharField】  非外键 
        
    
    ]
    return unit_post('videoerrkwkworlog', 'upd', keys, item)
    
def unit_post_videoerrkwkworlog_del(item):
    """
    【视频错误日志表】
    del
    item: del数据
    return: 提交结果
    """
    keys = [
    
        '_id', # 使用记录的ID查询
    
    ]
    return unit_post('videoerrkwkworlog', 'del', keys, item)
    
def unit_post_videoerrkwkworlog_get(item):
    """
    【视频错误日志表】
    get
    item: get数据
    return: 提交结果
    """
    keys = [
    
        '_id', # 使用记录的ID查询
    
    ]
    return unit_post('videoerrkwkworlog', 'get', keys, item)
    
def unit_post_videoerrkwkworlog_filter(item):
    """
    【视频错误日志表】
    filter
    item: filter数据
    return: 提交结果
    """
    keys = [
    
        'videoid', # 关联视频ID【SelectField】   videoinfo  videotitle 【视频标题】
        'errkwkwortype', # 错误类型【CharField】  非外键 
        'errkwkwordescription', # 错误描述【TextField】  非外键 
        'errkwkwortime', # 错误时间【DateTimeField】  非外键 
        'resolved', # 是否已解决【BooleanField】  非外键 
        'resolvedtime', # 解决时间【DateTimeField】  非外键 
        'resolvedby', # 关联解决人【SelectField】   supermanager  username 【管理员姓名】
        'devicekwkwinfo', # 设备信息【CharField】  非外键 
        'clientip', # 客户端IP【CharField】  非外键 
        
    
    ]
    return unit_post('videoerrkwkworlog', 'filter', keys, item)
    
def unit_post_videoerrkwkworlog_view(item):
    """
    【视频错误日志表】
    view
    item: view数据
    return: 提交结果
    """
    keys = [
    
        '_id', # 使用记录的ID查询
    
    ]
    return unit_post('videoerrkwkworlog', 'view', keys, item)
    
def unit_post_videoerrkwkworlog_go_add(item):
    """
    【视频错误日志表】
    go_add
    item: go_add数据
    return: 提交结果
    """
    keys = [
    
    {'form':{
        'id':'',
    }}
    
    ]
    return unit_post('videoerrkwkworlog', 'go_add', keys, item)
    
def unit_post_videoerrkwkworlog_go_upd(item):
    """
    【视频错误日志表】
    go_upd
    item: go_upd数据
    return: 提交结果
    """
    keys = [
    
    {'form':{
        'id':'',
    }}
    
    ]
    return unit_post('videoerrkwkworlog', 'go_upd', keys, item)
    


def unit_post_videopopularity_add(item):
    """
    【视频热度统计表】
    add
    item: add数据
    return: 提交结果
    """
    keys = [
    
        'videoid', # 关联视频ID【SelectField】   videoinfo  videotitle 【视频标题】
        'viewcount', # 观看次数【CharField】  非外键 
        'likecount', # 点赞次数【CharField】  非外键 
        'sharecount', # 分享次数【CharField】  非外键 
        'commentcount', # 评论次数【TextField】  非外键 
        'popularitysckwkwore', # 热度评分【IntegerField】  非外键 
        'publkwkwishtime', # 发布时间【DateTimeField】  非外键 
        'updatetime', # 更新时间【DateTimeField】  非外键 
        'categkwkworyid', # 关联类别ID【SelectField】   videocategkwkwory  name 【分类名称】
        'creatkwkworid', # 关联创作者ID【SelectField】   userinfo  username 【用户名】
        
    
    ]
    return unit_post('videopopularity', 'add', keys, item)
    
def unit_post_videopopularity_upd(item):
    """
    【视频热度统计表】
    upd
    item: upd数据
    return: 提交结果
    """
    keys = [
    
        'videoid', # 关联视频ID【SelectField】   videoinfo  videotitle 【视频标题】
        'viewcount', # 观看次数【CharField】  非外键 
        'likecount', # 点赞次数【CharField】  非外键 
        'sharecount', # 分享次数【CharField】  非外键 
        'commentcount', # 评论次数【TextField】  非外键 
        'popularitysckwkwore', # 热度评分【IntegerField】  非外键 
        'publkwkwishtime', # 发布时间【DateTimeField】  非外键 
        'updatetime', # 更新时间【DateTimeField】  非外键 
        'categkwkworyid', # 关联类别ID【SelectField】   videocategkwkwory  name 【分类名称】
        'creatkwkworid', # 关联创作者ID【SelectField】   userinfo  username 【用户名】
        
    
    ]
    return unit_post('videopopularity', 'upd', keys, item)
    
def unit_post_videopopularity_del(item):
    """
    【视频热度统计表】
    del
    item: del数据
    return: 提交结果
    """
    keys = [
    
        '_id', # 使用记录的ID查询
    
    ]
    return unit_post('videopopularity', 'del', keys, item)
    
def unit_post_videopopularity_get(item):
    """
    【视频热度统计表】
    get
    item: get数据
    return: 提交结果
    """
    keys = [
    
        '_id', # 使用记录的ID查询
    
    ]
    return unit_post('videopopularity', 'get', keys, item)
    
def unit_post_videopopularity_filter(item):
    """
    【视频热度统计表】
    filter
    item: filter数据
    return: 提交结果
    """
    keys = [
    
        'videoid', # 关联视频ID【SelectField】   videoinfo  videotitle 【视频标题】
        'viewcount', # 观看次数【CharField】  非外键 
        'likecount', # 点赞次数【CharField】  非外键 
        'sharecount', # 分享次数【CharField】  非外键 
        'commentcount', # 评论次数【TextField】  非外键 
        'popularitysckwkwore', # 热度评分【IntegerField】  非外键 
        'publkwkwishtime', # 发布时间【DateTimeField】  非外键 
        'updatetime', # 更新时间【DateTimeField】  非外键 
        'categkwkworyid', # 关联类别ID【SelectField】   videocategkwkwory  name 【分类名称】
        'creatkwkworid', # 关联创作者ID【SelectField】   userinfo  username 【用户名】
        
    
    ]
    return unit_post('videopopularity', 'filter', keys, item)
    
def unit_post_videopopularity_view(item):
    """
    【视频热度统计表】
    view
    item: view数据
    return: 提交结果
    """
    keys = [
    
        '_id', # 使用记录的ID查询
    
    ]
    return unit_post('videopopularity', 'view', keys, item)
    
def unit_post_videopopularity_go_add(item):
    """
    【视频热度统计表】
    go_add
    item: go_add数据
    return: 提交结果
    """
    keys = [
    
    {'form':{
        'id':'',
    }}
    
    ]
    return unit_post('videopopularity', 'go_add', keys, item)
    
def unit_post_videopopularity_go_upd(item):
    """
    【视频热度统计表】
    go_upd
    item: go_upd数据
    return: 提交结果
    """
    keys = [
    
    {'form':{
        'id':'',
    }}
    
    ]
    return unit_post('videopopularity', 'go_upd', keys, item)
    


def unit_post_videorecommendationparams_add(item):
    """
    【视频推荐算法参数表】
    add
    item: add数据
    return: 提交结果
    """
    keys = [
    
        'algkwkworithmname', # 算法名称【CharField】  非外键 
        'paramname', # 参数名称【CharField】  非外键 
        'paramvalue', # 参数值【CharField】  非外键 
        'description', # 参数描述【TextField】  非外键 
        'createdat', # 创建时间【DateTimeField】  非外键 
        'updatedat', # 更新时间【DateTimeField】  非外键 
        'kwkwisactive', # 是否启用【BooleanField】  非外键 
        'videotypeid', # 视频类型ID关联字段指向视频类型【SelectField】   videocategkwkwory  name 【分类名称】
        
    
    ]
    return unit_post('videorecommendationparams', 'add', keys, item)
    
def unit_post_videorecommendationparams_upd(item):
    """
    【视频推荐算法参数表】
    upd
    item: upd数据
    return: 提交结果
    """
    keys = [
    
        'algkwkworithmname', # 算法名称【CharField】  非外键 
        'paramname', # 参数名称【CharField】  非外键 
        'paramvalue', # 参数值【CharField】  非外键 
        'description', # 参数描述【TextField】  非外键 
        'createdat', # 创建时间【DateTimeField】  非外键 
        'updatedat', # 更新时间【DateTimeField】  非外键 
        'kwkwisactive', # 是否启用【BooleanField】  非外键 
        'videotypeid', # 视频类型ID关联字段指向视频类型【SelectField】   videocategkwkwory  name 【分类名称】
        
    
    ]
    return unit_post('videorecommendationparams', 'upd', keys, item)
    
def unit_post_videorecommendationparams_del(item):
    """
    【视频推荐算法参数表】
    del
    item: del数据
    return: 提交结果
    """
    keys = [
    
        '_id', # 使用记录的ID查询
    
    ]
    return unit_post('videorecommendationparams', 'del', keys, item)
    
def unit_post_videorecommendationparams_get(item):
    """
    【视频推荐算法参数表】
    get
    item: get数据
    return: 提交结果
    """
    keys = [
    
        '_id', # 使用记录的ID查询
    
    ]
    return unit_post('videorecommendationparams', 'get', keys, item)
    
def unit_post_videorecommendationparams_filter(item):
    """
    【视频推荐算法参数表】
    filter
    item: filter数据
    return: 提交结果
    """
    keys = [
    
        'algkwkworithmname', # 算法名称【CharField】  非外键 
        'paramname', # 参数名称【CharField】  非外键 
        'paramvalue', # 参数值【CharField】  非外键 
        'description', # 参数描述【TextField】  非外键 
        'createdat', # 创建时间【DateTimeField】  非外键 
        'updatedat', # 更新时间【DateTimeField】  非外键 
        'kwkwisactive', # 是否启用【BooleanField】  非外键 
        'videotypeid', # 视频类型ID关联字段指向视频类型【SelectField】   videocategkwkwory  name 【分类名称】
        
    
    ]
    return unit_post('videorecommendationparams', 'filter', keys, item)
    
def unit_post_videorecommendationparams_view(item):
    """
    【视频推荐算法参数表】
    view
    item: view数据
    return: 提交结果
    """
    keys = [
    
        '_id', # 使用记录的ID查询
    
    ]
    return unit_post('videorecommendationparams', 'view', keys, item)
    
def unit_post_videorecommendationparams_go_add(item):
    """
    【视频推荐算法参数表】
    go_add
    item: go_add数据
    return: 提交结果
    """
    keys = [
    
    {'form':{
        'id':'',
    }}
    
    ]
    return unit_post('videorecommendationparams', 'go_add', keys, item)
    
def unit_post_videorecommendationparams_go_upd(item):
    """
    【视频推荐算法参数表】
    go_upd
    item: go_upd数据
    return: 提交结果
    """
    keys = [
    
    {'form':{
        'id':'',
    }}
    
    ]
    return unit_post('videorecommendationparams', 'go_upd', keys, item)
    


def unit_post_videoadinfo_add(item):
    """
    【视频广告信息表】
    add
    item: add数据
    return: 提交结果
    """
    keys = [
    
        'videoadid', # 视频广告ID【UUIDField】  非外键 
        'title', # 广告标题【CharField】  非外键 
        'description', # 广告描述【TextField】  非外键 
        'starttime', # 开始时间【DateTimeField】  非外键 
        'endtime', # 结束时间【DateTimeField】  非外键 
        'videourl', # 视频链接【URLField】  非外键 
        'thumbnailurl', # 缩略图链接【URLField】  非外键 
        'advertkwkwiserid', # 广告主ID【UUIDField】  非外键 
        'categkwkworyid', # 广告分类ID【UUIDField】  非外键 
        'status', # 广告状态【CharField】  非外键 
        
    
    ]
    return unit_post('videoadinfo', 'add', keys, item)
    
def unit_post_videoadinfo_upd(item):
    """
    【视频广告信息表】
    upd
    item: upd数据
    return: 提交结果
    """
    keys = [
    
        'videoadid', # 视频广告ID【UUIDField】  非外键 
        'title', # 广告标题【CharField】  非外键 
        'description', # 广告描述【TextField】  非外键 
        'starttime', # 开始时间【DateTimeField】  非外键 
        'endtime', # 结束时间【DateTimeField】  非外键 
        'videourl', # 视频链接【URLField】  非外键 
        'thumbnailurl', # 缩略图链接【URLField】  非外键 
        'advertkwkwiserid', # 广告主ID【UUIDField】  非外键 
        'categkwkworyid', # 广告分类ID【UUIDField】  非外键 
        'status', # 广告状态【CharField】  非外键 
        
    
    ]
    return unit_post('videoadinfo', 'upd', keys, item)
    
def unit_post_videoadinfo_del(item):
    """
    【视频广告信息表】
    del
    item: del数据
    return: 提交结果
    """
    keys = [
    
        '_id', # 使用记录的ID查询
    
    ]
    return unit_post('videoadinfo', 'del', keys, item)
    
def unit_post_videoadinfo_get(item):
    """
    【视频广告信息表】
    get
    item: get数据
    return: 提交结果
    """
    keys = [
    
        '_id', # 使用记录的ID查询
    
    ]
    return unit_post('videoadinfo', 'get', keys, item)
    
def unit_post_videoadinfo_filter(item):
    """
    【视频广告信息表】
    filter
    item: filter数据
    return: 提交结果
    """
    keys = [
    
        'videoadid', # 视频广告ID【UUIDField】  非外键 
        'title', # 广告标题【CharField】  非外键 
        'description', # 广告描述【TextField】  非外键 
        'starttime', # 开始时间【DateTimeField】  非外键 
        'endtime', # 结束时间【DateTimeField】  非外键 
        'videourl', # 视频链接【URLField】  非外键 
        'thumbnailurl', # 缩略图链接【URLField】  非外键 
        'advertkwkwiserid', # 广告主ID【UUIDField】  非外键 
        'categkwkworyid', # 广告分类ID【UUIDField】  非外键 
        'status', # 广告状态【CharField】  非外键 
        
    
    ]
    return unit_post('videoadinfo', 'filter', keys, item)
    
def unit_post_videoadinfo_view(item):
    """
    【视频广告信息表】
    view
    item: view数据
    return: 提交结果
    """
    keys = [
    
        '_id', # 使用记录的ID查询
    
    ]
    return unit_post('videoadinfo', 'view', keys, item)
    
def unit_post_videoadinfo_go_add(item):
    """
    【视频广告信息表】
    go_add
    item: go_add数据
    return: 提交结果
    """
    keys = [
    
    {'form':{
        'id':'',
    }}
    
    ]
    return unit_post('videoadinfo', 'go_add', keys, item)
    
def unit_post_videoadinfo_go_upd(item):
    """
    【视频广告信息表】
    go_upd
    item: go_upd数据
    return: 提交结果
    """
    keys = [
    
    {'form':{
        'id':'',
    }}
    
    ]
    return unit_post('videoadinfo', 'go_upd', keys, item)
    


def unit_post_videoadplayreckwkword_add(item):
    """
    【视频广告播放记录表】
    add
    item: add数据
    return: 提交结果
    """
    keys = [
    
        'videoadid', # 视频广告ID【UUIDField】  非外键 
        'playtime', # 播放时间【DateTimeField】  非外键 
        'playduration', # 播放时长【CharField】  非外键 
        'userid', # 用户ID关联用户【SelectField】   userinfo  username 【用户名】
        'devicetype', # 设备类型【CharField】  非外键 
        'ipaddressip', # 地址【TextField】  非外键 
        'location', # 地理位置【CharField】  非外键 
        'playstatus', # 播放状态如成功、失败、中断等【CharField】  非外键 
        
    
    ]
    return unit_post('videoadplayreckwkword', 'add', keys, item)
    
def unit_post_videoadplayreckwkword_upd(item):
    """
    【视频广告播放记录表】
    upd
    item: upd数据
    return: 提交结果
    """
    keys = [
    
        'videoadid', # 视频广告ID【UUIDField】  非外键 
        'playtime', # 播放时间【DateTimeField】  非外键 
        'playduration', # 播放时长【CharField】  非外键 
        'userid', # 用户ID关联用户【SelectField】   userinfo  username 【用户名】
        'devicetype', # 设备类型【CharField】  非外键 
        'ipaddressip', # 地址【TextField】  非外键 
        'location', # 地理位置【CharField】  非外键 
        'playstatus', # 播放状态如成功、失败、中断等【CharField】  非外键 
        
    
    ]
    return unit_post('videoadplayreckwkword', 'upd', keys, item)
    
def unit_post_videoadplayreckwkword_del(item):
    """
    【视频广告播放记录表】
    del
    item: del数据
    return: 提交结果
    """
    keys = [
    
        '_id', # 使用记录的ID查询
    
    ]
    return unit_post('videoadplayreckwkword', 'del', keys, item)
    
def unit_post_videoadplayreckwkword_get(item):
    """
    【视频广告播放记录表】
    get
    item: get数据
    return: 提交结果
    """
    keys = [
    
        '_id', # 使用记录的ID查询
    
    ]
    return unit_post('videoadplayreckwkword', 'get', keys, item)
    
def unit_post_videoadplayreckwkword_filter(item):
    """
    【视频广告播放记录表】
    filter
    item: filter数据
    return: 提交结果
    """
    keys = [
    
        'videoadid', # 视频广告ID【UUIDField】  非外键 
        'playtime', # 播放时间【DateTimeField】  非外键 
        'playduration', # 播放时长【CharField】  非外键 
        'userid', # 用户ID关联用户【SelectField】   userinfo  username 【用户名】
        'devicetype', # 设备类型【CharField】  非外键 
        'ipaddressip', # 地址【TextField】  非外键 
        'location', # 地理位置【CharField】  非外键 
        'playstatus', # 播放状态如成功、失败、中断等【CharField】  非外键 
        
    
    ]
    return unit_post('videoadplayreckwkword', 'filter', keys, item)
    
def unit_post_videoadplayreckwkword_view(item):
    """
    【视频广告播放记录表】
    view
    item: view数据
    return: 提交结果
    """
    keys = [
    
        '_id', # 使用记录的ID查询
    
    ]
    return unit_post('videoadplayreckwkword', 'view', keys, item)
    
def unit_post_videoadplayreckwkword_go_add(item):
    """
    【视频广告播放记录表】
    go_add
    item: go_add数据
    return: 提交结果
    """
    keys = [
    
    {'form':{
        'id':'',
    }}
    
    ]
    return unit_post('videoadplayreckwkword', 'go_add', keys, item)
    
def unit_post_videoadplayreckwkword_go_upd(item):
    """
    【视频广告播放记录表】
    go_upd
    item: go_upd数据
    return: 提交结果
    """
    keys = [
    
    {'form':{
        'id':'',
    }}
    
    ]
    return unit_post('videoadplayreckwkword', 'go_upd', keys, item)
    


def unit_post_videodanmu_add(item):
    """
    【视频弹幕表】
    add
    item: add数据
    return: 提交结果
    """
    keys = [
    
        'videoid', # 视频唯一标识符关联视频【UUIDField】  非外键 
        'danmucontent', # 弹幕内容【TextField】  非外键 
        'userid', # 发送弹幕的用户唯一标识符关联用户【UUIDField】  非外键 
        'sendtime', # 发送时间【DateTimeField】  非外键 
        'colkwkwor', # 弹幕颜色【CharField】  非外键 
        'fontsize', # 字体大小【CharField】  非外键 
        'kwkwisvkwkwisible', # 是否可见用于控制弹幕的显示与隐藏【BooleanField】  非外键 
        'position', # 弹幕位置如顶部、底部、滚动等【CharField】  非外键 
        'duration', # 弹幕显示时长秒【CharField】  非外键 
        
    
    ]
    return unit_post('videodanmu', 'add', keys, item)
    
def unit_post_videodanmu_upd(item):
    """
    【视频弹幕表】
    upd
    item: upd数据
    return: 提交结果
    """
    keys = [
    
        'videoid', # 视频唯一标识符关联视频【UUIDField】  非外键 
        'danmucontent', # 弹幕内容【TextField】  非外键 
        'userid', # 发送弹幕的用户唯一标识符关联用户【UUIDField】  非外键 
        'sendtime', # 发送时间【DateTimeField】  非外键 
        'colkwkwor', # 弹幕颜色【CharField】  非外键 
        'fontsize', # 字体大小【CharField】  非外键 
        'kwkwisvkwkwisible', # 是否可见用于控制弹幕的显示与隐藏【BooleanField】  非外键 
        'position', # 弹幕位置如顶部、底部、滚动等【CharField】  非外键 
        'duration', # 弹幕显示时长秒【CharField】  非外键 
        
    
    ]
    return unit_post('videodanmu', 'upd', keys, item)
    
def unit_post_videodanmu_del(item):
    """
    【视频弹幕表】
    del
    item: del数据
    return: 提交结果
    """
    keys = [
    
        '_id', # 使用记录的ID查询
    
    ]
    return unit_post('videodanmu', 'del', keys, item)
    
def unit_post_videodanmu_get(item):
    """
    【视频弹幕表】
    get
    item: get数据
    return: 提交结果
    """
    keys = [
    
        '_id', # 使用记录的ID查询
    
    ]
    return unit_post('videodanmu', 'get', keys, item)
    
def unit_post_videodanmu_filter(item):
    """
    【视频弹幕表】
    filter
    item: filter数据
    return: 提交结果
    """
    keys = [
    
        'videoid', # 视频唯一标识符关联视频【UUIDField】  非外键 
        'danmucontent', # 弹幕内容【TextField】  非外键 
        'userid', # 发送弹幕的用户唯一标识符关联用户【UUIDField】  非外键 
        'sendtime', # 发送时间【DateTimeField】  非外键 
        'colkwkwor', # 弹幕颜色【CharField】  非外键 
        'fontsize', # 字体大小【CharField】  非外键 
        'kwkwisvkwkwisible', # 是否可见用于控制弹幕的显示与隐藏【BooleanField】  非外键 
        'position', # 弹幕位置如顶部、底部、滚动等【CharField】  非外键 
        'duration', # 弹幕显示时长秒【CharField】  非外键 
        
    
    ]
    return unit_post('videodanmu', 'filter', keys, item)
    
def unit_post_videodanmu_view(item):
    """
    【视频弹幕表】
    view
    item: view数据
    return: 提交结果
    """
    keys = [
    
        '_id', # 使用记录的ID查询
    
    ]
    return unit_post('videodanmu', 'view', keys, item)
    
def unit_post_videodanmu_go_add(item):
    """
    【视频弹幕表】
    go_add
    item: go_add数据
    return: 提交结果
    """
    keys = [
    
    {'form':{
        'id':'',
    }}
    
    ]
    return unit_post('videodanmu', 'go_add', keys, item)
    
def unit_post_videodanmu_go_upd(item):
    """
    【视频弹幕表】
    go_upd
    item: go_upd数据
    return: 提交结果
    """
    keys = [
    
    {'form':{
        'id':'',
    }}
    
    ]
    return unit_post('videodanmu', 'go_upd', keys, item)
    


def unit_post_videodanmublockwkwkwords_add(item):
    """
    【视频弹幕屏蔽词表】
    add
    item: add数据
    return: 提交结果
    """
    keys = [
    
        'wkwkword', # 屏蔽词【CharField】  非外键 
        'videoid', # 视频ID关联字段指向视频的ID【SelectField】   videoinfo  videotitle 【视频标题】
        'creatkwkworid', # 创建者ID关联字段指向用户的ID【SelectField】   userinfo  username 【用户名】
        'createtime', # 创建时间【DateTimeField】  非外键 
        'updatetime', # 更新时间【DateTimeField】  非外键 
        'kwkwisactive', # 是否激活用于控制屏蔽词是否生效【BooleanField】  非外键 
        'blocktype', # 屏蔽类型如关键词、正则达式等【CharField】  非外键 
        'description', # 描述对屏蔽词的额外说明或备注【TextField】  非外键 
        
    
    ]
    return unit_post('videodanmublockwkwkwords', 'add', keys, item)
    
def unit_post_videodanmublockwkwkwords_upd(item):
    """
    【视频弹幕屏蔽词表】
    upd
    item: upd数据
    return: 提交结果
    """
    keys = [
    
        'wkwkword', # 屏蔽词【CharField】  非外键 
        'videoid', # 视频ID关联字段指向视频的ID【SelectField】   videoinfo  videotitle 【视频标题】
        'creatkwkworid', # 创建者ID关联字段指向用户的ID【SelectField】   userinfo  username 【用户名】
        'createtime', # 创建时间【DateTimeField】  非外键 
        'updatetime', # 更新时间【DateTimeField】  非外键 
        'kwkwisactive', # 是否激活用于控制屏蔽词是否生效【BooleanField】  非外键 
        'blocktype', # 屏蔽类型如关键词、正则达式等【CharField】  非外键 
        'description', # 描述对屏蔽词的额外说明或备注【TextField】  非外键 
        
    
    ]
    return unit_post('videodanmublockwkwkwords', 'upd', keys, item)
    
def unit_post_videodanmublockwkwkwords_del(item):
    """
    【视频弹幕屏蔽词表】
    del
    item: del数据
    return: 提交结果
    """
    keys = [
    
        '_id', # 使用记录的ID查询
    
    ]
    return unit_post('videodanmublockwkwkwords', 'del', keys, item)
    
def unit_post_videodanmublockwkwkwords_get(item):
    """
    【视频弹幕屏蔽词表】
    get
    item: get数据
    return: 提交结果
    """
    keys = [
    
        '_id', # 使用记录的ID查询
    
    ]
    return unit_post('videodanmublockwkwkwords', 'get', keys, item)
    
def unit_post_videodanmublockwkwkwords_filter(item):
    """
    【视频弹幕屏蔽词表】
    filter
    item: filter数据
    return: 提交结果
    """
    keys = [
    
        'wkwkword', # 屏蔽词【CharField】  非外键 
        'videoid', # 视频ID关联字段指向视频的ID【SelectField】   videoinfo  videotitle 【视频标题】
        'creatkwkworid', # 创建者ID关联字段指向用户的ID【SelectField】   userinfo  username 【用户名】
        'createtime', # 创建时间【DateTimeField】  非外键 
        'updatetime', # 更新时间【DateTimeField】  非外键 
        'kwkwisactive', # 是否激活用于控制屏蔽词是否生效【BooleanField】  非外键 
        'blocktype', # 屏蔽类型如关键词、正则达式等【CharField】  非外键 
        'description', # 描述对屏蔽词的额外说明或备注【TextField】  非外键 
        
    
    ]
    return unit_post('videodanmublockwkwkwords', 'filter', keys, item)
    
def unit_post_videodanmublockwkwkwords_view(item):
    """
    【视频弹幕屏蔽词表】
    view
    item: view数据
    return: 提交结果
    """
    keys = [
    
        '_id', # 使用记录的ID查询
    
    ]
    return unit_post('videodanmublockwkwkwords', 'view', keys, item)
    
def unit_post_videodanmublockwkwkwords_go_add(item):
    """
    【视频弹幕屏蔽词表】
    go_add
    item: go_add数据
    return: 提交结果
    """
    keys = [
    
    {'form':{
        'id':'',
    }}
    
    ]
    return unit_post('videodanmublockwkwkwords', 'go_add', keys, item)
    
def unit_post_videodanmublockwkwkwords_go_upd(item):
    """
    【视频弹幕屏蔽词表】
    go_upd
    item: go_upd数据
    return: 提交结果
    """
    keys = [
    
    {'form':{
        'id':'',
    }}
    
    ]
    return unit_post('videodanmublockwkwkwords', 'go_upd', keys, item)
    


def unit_post_videomultilkwkwingualsubtitles_add(item):
    """
    【视频多语言字幕表】
    add
    item: add数据
    return: 提交结果
    """
    keys = [
    
        'videoid', # 关联视频ID【SelectField】   videoinfo  videotitle 【视频标题】
        'languagecode', # 语言代码【CharField】  非外键 
        'subtitletext', # 字幕文本【TextField】  非外键 
        'starttime', # 开始时间字幕出现时间【DateTimeField】  非外键 
        'endtime', # 结束时间字幕消失时间【DateTimeField】  非外键 
        'createdat', # 创建时间【DateTimeField】  非外键 
        'updatedat', # 更新时间【DateTimeField】  非外键 
        'kwkwisactive', # 是否激活用于控制字幕是否显示在视频中【BooleanField】  非外键 
        'userid', # 创建者用户ID关联到用户示谁添加了这条字幕【SelectField】   userinfo  username 【用户名】
        
    
    ]
    return unit_post('videomultilkwkwingualsubtitles', 'add', keys, item)
    
def unit_post_videomultilkwkwingualsubtitles_upd(item):
    """
    【视频多语言字幕表】
    upd
    item: upd数据
    return: 提交结果
    """
    keys = [
    
        'videoid', # 关联视频ID【SelectField】   videoinfo  videotitle 【视频标题】
        'languagecode', # 语言代码【CharField】  非外键 
        'subtitletext', # 字幕文本【TextField】  非外键 
        'starttime', # 开始时间字幕出现时间【DateTimeField】  非外键 
        'endtime', # 结束时间字幕消失时间【DateTimeField】  非外键 
        'createdat', # 创建时间【DateTimeField】  非外键 
        'updatedat', # 更新时间【DateTimeField】  非外键 
        'kwkwisactive', # 是否激活用于控制字幕是否显示在视频中【BooleanField】  非外键 
        'userid', # 创建者用户ID关联到用户示谁添加了这条字幕【SelectField】   userinfo  username 【用户名】
        
    
    ]
    return unit_post('videomultilkwkwingualsubtitles', 'upd', keys, item)
    
def unit_post_videomultilkwkwingualsubtitles_del(item):
    """
    【视频多语言字幕表】
    del
    item: del数据
    return: 提交结果
    """
    keys = [
    
        '_id', # 使用记录的ID查询
    
    ]
    return unit_post('videomultilkwkwingualsubtitles', 'del', keys, item)
    
def unit_post_videomultilkwkwingualsubtitles_get(item):
    """
    【视频多语言字幕表】
    get
    item: get数据
    return: 提交结果
    """
    keys = [
    
        '_id', # 使用记录的ID查询
    
    ]
    return unit_post('videomultilkwkwingualsubtitles', 'get', keys, item)
    
def unit_post_videomultilkwkwingualsubtitles_filter(item):
    """
    【视频多语言字幕表】
    filter
    item: filter数据
    return: 提交结果
    """
    keys = [
    
        'videoid', # 关联视频ID【SelectField】   videoinfo  videotitle 【视频标题】
        'languagecode', # 语言代码【CharField】  非外键 
        'subtitletext', # 字幕文本【TextField】  非外键 
        'starttime', # 开始时间字幕出现时间【DateTimeField】  非外键 
        'endtime', # 结束时间字幕消失时间【DateTimeField】  非外键 
        'createdat', # 创建时间【DateTimeField】  非外键 
        'updatedat', # 更新时间【DateTimeField】  非外键 
        'kwkwisactive', # 是否激活用于控制字幕是否显示在视频中【BooleanField】  非外键 
        'userid', # 创建者用户ID关联到用户示谁添加了这条字幕【SelectField】   userinfo  username 【用户名】
        
    
    ]
    return unit_post('videomultilkwkwingualsubtitles', 'filter', keys, item)
    
def unit_post_videomultilkwkwingualsubtitles_view(item):
    """
    【视频多语言字幕表】
    view
    item: view数据
    return: 提交结果
    """
    keys = [
    
        '_id', # 使用记录的ID查询
    
    ]
    return unit_post('videomultilkwkwingualsubtitles', 'view', keys, item)
    
def unit_post_videomultilkwkwingualsubtitles_go_add(item):
    """
    【视频多语言字幕表】
    go_add
    item: go_add数据
    return: 提交结果
    """
    keys = [
    
    {'form':{
        'id':'',
    }}
    
    ]
    return unit_post('videomultilkwkwingualsubtitles', 'go_add', keys, item)
    
def unit_post_videomultilkwkwingualsubtitles_go_upd(item):
    """
    【视频多语言字幕表】
    go_upd
    item: go_upd数据
    return: 提交结果
    """
    keys = [
    
    {'form':{
        'id':'',
    }}
    
    ]
    return unit_post('videomultilkwkwingualsubtitles', 'go_upd', keys, item)
    


def unit_post_videotranscodkwkwingtkwkwask_add(item):
    """
    【视频转码任务表】
    add
    item: add数据
    return: 提交结果
    """
    keys = [
    
        'tkwkwaskid', # 任务ID【UUIDField】  非外键 
        'videoid', # 关联视频ID【SelectField】   videoinfo  videotitle 【视频标题】
        'sourcepath', # 源视频路径【FileField】  非外键 
        'targetkwkwfkwkwormat', # 目标格式【CharField】  非外键 
        'status', # 任务状态【CharField】  非外键 
        'progress', # 任务进度【CharField】  非外键 
        'createdat', # 创建时间【DateTimeField】  非外键 
        'updatedat', # 更新时间【DateTimeField】  非外键 
        'userid', # 关联用户ID【SelectField】   userinfo  username 【用户名】
        'prikwkwority', # 任务优先级【CharField】  非外键 
        
    
    ]
    return unit_post('videotranscodkwkwingtkwkwask', 'add', keys, item)
    
def unit_post_videotranscodkwkwingtkwkwask_upd(item):
    """
    【视频转码任务表】
    upd
    item: upd数据
    return: 提交结果
    """
    keys = [
    
        'tkwkwaskid', # 任务ID【UUIDField】  非外键 
        'videoid', # 关联视频ID【SelectField】   videoinfo  videotitle 【视频标题】
        'sourcepath', # 源视频路径【FileField】  非外键 
        'targetkwkwfkwkwormat', # 目标格式【CharField】  非外键 
        'status', # 任务状态【CharField】  非外键 
        'progress', # 任务进度【CharField】  非外键 
        'createdat', # 创建时间【DateTimeField】  非外键 
        'updatedat', # 更新时间【DateTimeField】  非外键 
        'userid', # 关联用户ID【SelectField】   userinfo  username 【用户名】
        'prikwkwority', # 任务优先级【CharField】  非外键 
        
    
    ]
    return unit_post('videotranscodkwkwingtkwkwask', 'upd', keys, item)
    
def unit_post_videotranscodkwkwingtkwkwask_del(item):
    """
    【视频转码任务表】
    del
    item: del数据
    return: 提交结果
    """
    keys = [
    
        '_id', # 使用记录的ID查询
    
    ]
    return unit_post('videotranscodkwkwingtkwkwask', 'del', keys, item)
    
def unit_post_videotranscodkwkwingtkwkwask_get(item):
    """
    【视频转码任务表】
    get
    item: get数据
    return: 提交结果
    """
    keys = [
    
        '_id', # 使用记录的ID查询
    
    ]
    return unit_post('videotranscodkwkwingtkwkwask', 'get', keys, item)
    
def unit_post_videotranscodkwkwingtkwkwask_filter(item):
    """
    【视频转码任务表】
    filter
    item: filter数据
    return: 提交结果
    """
    keys = [
    
        'tkwkwaskid', # 任务ID【UUIDField】  非外键 
        'videoid', # 关联视频ID【SelectField】   videoinfo  videotitle 【视频标题】
        'sourcepath', # 源视频路径【FileField】  非外键 
        'targetkwkwfkwkwormat', # 目标格式【CharField】  非外键 
        'status', # 任务状态【CharField】  非外键 
        'progress', # 任务进度【CharField】  非外键 
        'createdat', # 创建时间【DateTimeField】  非外键 
        'updatedat', # 更新时间【DateTimeField】  非外键 
        'userid', # 关联用户ID【SelectField】   userinfo  username 【用户名】
        'prikwkwority', # 任务优先级【CharField】  非外键 
        
    
    ]
    return unit_post('videotranscodkwkwingtkwkwask', 'filter', keys, item)
    
def unit_post_videotranscodkwkwingtkwkwask_view(item):
    """
    【视频转码任务表】
    view
    item: view数据
    return: 提交结果
    """
    keys = [
    
        '_id', # 使用记录的ID查询
    
    ]
    return unit_post('videotranscodkwkwingtkwkwask', 'view', keys, item)
    
def unit_post_videotranscodkwkwingtkwkwask_go_add(item):
    """
    【视频转码任务表】
    go_add
    item: go_add数据
    return: 提交结果
    """
    keys = [
    
    {'form':{
        'id':'',
    }}
    
    ]
    return unit_post('videotranscodkwkwingtkwkwask', 'go_add', keys, item)
    
def unit_post_videotranscodkwkwingtkwkwask_go_upd(item):
    """
    【视频转码任务表】
    go_upd
    item: go_upd数据
    return: 提交结果
    """
    keys = [
    
    {'form':{
        'id':'',
    }}
    
    ]
    return unit_post('videotranscodkwkwingtkwkwask', 'go_upd', keys, item)
    


def unit_post_videoanalyskwkwismetrics_add(item):
    """
    【视频分析指标表】
    add
    item: add数据
    return: 提交结果
    """
    keys = [
    
        'videoid', # 视频ID关联视频【SelectField】   videoinfo  videotitle 【视频标题】
        'analyskwkwistime', # 分析时间【DateTimeField】  非外键 
        'viewcount', # 观看次数【CharField】  非外键 
        'likecount', # 点赞次数【CharField】  非外键 
        'sharecount', # 分享次数【CharField】  非外键 
        'commentcount', # 评论次数【TextField】  非外键 
        'bouncerate', # 跳出率【CharField】  非外键 
        'averagewatchtime', # 平均观看时长【CharField】  非外键 
        'engagementrate', # 互动率【CharField】  非外键 
        
    
    ]
    return unit_post('videoanalyskwkwismetrics', 'add', keys, item)
    
def unit_post_videoanalyskwkwismetrics_upd(item):
    """
    【视频分析指标表】
    upd
    item: upd数据
    return: 提交结果
    """
    keys = [
    
        'videoid', # 视频ID关联视频【SelectField】   videoinfo  videotitle 【视频标题】
        'analyskwkwistime', # 分析时间【DateTimeField】  非外键 
        'viewcount', # 观看次数【CharField】  非外键 
        'likecount', # 点赞次数【CharField】  非外键 
        'sharecount', # 分享次数【CharField】  非外键 
        'commentcount', # 评论次数【TextField】  非外键 
        'bouncerate', # 跳出率【CharField】  非外键 
        'averagewatchtime', # 平均观看时长【CharField】  非外键 
        'engagementrate', # 互动率【CharField】  非外键 
        
    
    ]
    return unit_post('videoanalyskwkwismetrics', 'upd', keys, item)
    
def unit_post_videoanalyskwkwismetrics_del(item):
    """
    【视频分析指标表】
    del
    item: del数据
    return: 提交结果
    """
    keys = [
    
        '_id', # 使用记录的ID查询
    
    ]
    return unit_post('videoanalyskwkwismetrics', 'del', keys, item)
    
def unit_post_videoanalyskwkwismetrics_get(item):
    """
    【视频分析指标表】
    get
    item: get数据
    return: 提交结果
    """
    keys = [
    
        '_id', # 使用记录的ID查询
    
    ]
    return unit_post('videoanalyskwkwismetrics', 'get', keys, item)
    
def unit_post_videoanalyskwkwismetrics_filter(item):
    """
    【视频分析指标表】
    filter
    item: filter数据
    return: 提交结果
    """
    keys = [
    
        'videoid', # 视频ID关联视频【SelectField】   videoinfo  videotitle 【视频标题】
        'analyskwkwistime', # 分析时间【DateTimeField】  非外键 
        'viewcount', # 观看次数【CharField】  非外键 
        'likecount', # 点赞次数【CharField】  非外键 
        'sharecount', # 分享次数【CharField】  非外键 
        'commentcount', # 评论次数【TextField】  非外键 
        'bouncerate', # 跳出率【CharField】  非外键 
        'averagewatchtime', # 平均观看时长【CharField】  非外键 
        'engagementrate', # 互动率【CharField】  非外键 
        
    
    ]
    return unit_post('videoanalyskwkwismetrics', 'filter', keys, item)
    
def unit_post_videoanalyskwkwismetrics_view(item):
    """
    【视频分析指标表】
    view
    item: view数据
    return: 提交结果
    """
    keys = [
    
        '_id', # 使用记录的ID查询
    
    ]
    return unit_post('videoanalyskwkwismetrics', 'view', keys, item)
    
def unit_post_videoanalyskwkwismetrics_go_add(item):
    """
    【视频分析指标表】
    go_add
    item: go_add数据
    return: 提交结果
    """
    keys = [
    
    {'form':{
        'id':'',
    }}
    
    ]
    return unit_post('videoanalyskwkwismetrics', 'go_add', keys, item)
    
def unit_post_videoanalyskwkwismetrics_go_upd(item):
    """
    【视频分析指标表】
    go_upd
    item: go_upd数据
    return: 提交结果
    """
    keys = [
    
    {'form':{
        'id':'',
    }}
    
    ]
    return unit_post('videoanalyskwkwismetrics', 'go_upd', keys, item)
    


def unit_post_videoqualityassessment_add(item):
    """
    【视频质量评估表】
    add
    item: add数据
    return: 提交结果
    """
    keys = [
    
        'videoid', # 关联视频ID【SelectField】   videoinfo  videotitle 【视频标题】
        'qualitysckwkwore', # 质量评分【IntegerField】  非外键 
        'kwkwassessmenttime', # 评估时间【DateTimeField】  非外键 
        'reviewerid', # 关联评审员ID【SelectField】   supermanager  username 【管理员姓名】
        'framerate', # 帧率【CharField】  非外键 
        'resolution', # 分辨率【CharField】  非外键 
        'bitrate', # 比特率【CharField】  非外键 
        'encodkwkwingkwkwfkwkwormat', # 编码格式【CharField】  非外键 
        'ckwkworruptiondetected', # 是否检测到损坏【BooleanField】  非外键 
        'relatedkwkwissueid', # 相关问题ID【UUIDField】  非外键 
        
    
    ]
    return unit_post('videoqualityassessment', 'add', keys, item)
    
def unit_post_videoqualityassessment_upd(item):
    """
    【视频质量评估表】
    upd
    item: upd数据
    return: 提交结果
    """
    keys = [
    
        'videoid', # 关联视频ID【SelectField】   videoinfo  videotitle 【视频标题】
        'qualitysckwkwore', # 质量评分【IntegerField】  非外键 
        'kwkwassessmenttime', # 评估时间【DateTimeField】  非外键 
        'reviewerid', # 关联评审员ID【SelectField】   supermanager  username 【管理员姓名】
        'framerate', # 帧率【CharField】  非外键 
        'resolution', # 分辨率【CharField】  非外键 
        'bitrate', # 比特率【CharField】  非外键 
        'encodkwkwingkwkwfkwkwormat', # 编码格式【CharField】  非外键 
        'ckwkworruptiondetected', # 是否检测到损坏【BooleanField】  非外键 
        'relatedkwkwissueid', # 相关问题ID【UUIDField】  非外键 
        
    
    ]
    return unit_post('videoqualityassessment', 'upd', keys, item)
    
def unit_post_videoqualityassessment_del(item):
    """
    【视频质量评估表】
    del
    item: del数据
    return: 提交结果
    """
    keys = [
    
        '_id', # 使用记录的ID查询
    
    ]
    return unit_post('videoqualityassessment', 'del', keys, item)
    
def unit_post_videoqualityassessment_get(item):
    """
    【视频质量评估表】
    get
    item: get数据
    return: 提交结果
    """
    keys = [
    
        '_id', # 使用记录的ID查询
    
    ]
    return unit_post('videoqualityassessment', 'get', keys, item)
    
def unit_post_videoqualityassessment_filter(item):
    """
    【视频质量评估表】
    filter
    item: filter数据
    return: 提交结果
    """
    keys = [
    
        'videoid', # 关联视频ID【SelectField】   videoinfo  videotitle 【视频标题】
        'qualitysckwkwore', # 质量评分【IntegerField】  非外键 
        'kwkwassessmenttime', # 评估时间【DateTimeField】  非外键 
        'reviewerid', # 关联评审员ID【SelectField】   supermanager  username 【管理员姓名】
        'framerate', # 帧率【CharField】  非外键 
        'resolution', # 分辨率【CharField】  非外键 
        'bitrate', # 比特率【CharField】  非外键 
        'encodkwkwingkwkwfkwkwormat', # 编码格式【CharField】  非外键 
        'ckwkworruptiondetected', # 是否检测到损坏【BooleanField】  非外键 
        'relatedkwkwissueid', # 相关问题ID【UUIDField】  非外键 
        
    
    ]
    return unit_post('videoqualityassessment', 'filter', keys, item)
    
def unit_post_videoqualityassessment_view(item):
    """
    【视频质量评估表】
    view
    item: view数据
    return: 提交结果
    """
    keys = [
    
        '_id', # 使用记录的ID查询
    
    ]
    return unit_post('videoqualityassessment', 'view', keys, item)
    
def unit_post_videoqualityassessment_go_add(item):
    """
    【视频质量评估表】
    go_add
    item: go_add数据
    return: 提交结果
    """
    keys = [
    
    {'form':{
        'id':'',
    }}
    
    ]
    return unit_post('videoqualityassessment', 'go_add', keys, item)
    
def unit_post_videoqualityassessment_go_upd(item):
    """
    【视频质量评估表】
    go_upd
    item: go_upd数据
    return: 提交结果
    """
    keys = [
    
    {'form':{
        'id':'',
    }}
    
    ]
    return unit_post('videoqualityassessment', 'go_upd', keys, item)
    


def unit_post_videowatermarkinfo_add(item):
    """
    【视频水印信息表】
    add
    item: add数据
    return: 提交结果
    """
    keys = [
    
        'videoid', # 视频ID关联视频【SelectField】   videoinfo  videotitle 【视频标题】
        'watermarktext', # 水印文本【TextField】  非外键 
        'watermarkposition', # 水印位置如左上角、右下角等【CharField】  非外键 
        'watermarksize', # 水印大小如百分比或像素值【CharField】  非外键 
        'watermarkopacity', # 水印透明度0100%【CharField】  非外键 
        'createdat', # 创建时间【DateTimeField】  非外键 
        'updatedat', # 更新时间【DateTimeField】  非外键 
        'kwkwisactive', # 是否激活用于控制水印是否生效如0为未激活1为激活【BooleanField】  非外键 
        
    
    ]
    return unit_post('videowatermarkinfo', 'add', keys, item)
    
def unit_post_videowatermarkinfo_upd(item):
    """
    【视频水印信息表】
    upd
    item: upd数据
    return: 提交结果
    """
    keys = [
    
        'videoid', # 视频ID关联视频【SelectField】   videoinfo  videotitle 【视频标题】
        'watermarktext', # 水印文本【TextField】  非外键 
        'watermarkposition', # 水印位置如左上角、右下角等【CharField】  非外键 
        'watermarksize', # 水印大小如百分比或像素值【CharField】  非外键 
        'watermarkopacity', # 水印透明度0100%【CharField】  非外键 
        'createdat', # 创建时间【DateTimeField】  非外键 
        'updatedat', # 更新时间【DateTimeField】  非外键 
        'kwkwisactive', # 是否激活用于控制水印是否生效如0为未激活1为激活【BooleanField】  非外键 
        
    
    ]
    return unit_post('videowatermarkinfo', 'upd', keys, item)
    
def unit_post_videowatermarkinfo_del(item):
    """
    【视频水印信息表】
    del
    item: del数据
    return: 提交结果
    """
    keys = [
    
        '_id', # 使用记录的ID查询
    
    ]
    return unit_post('videowatermarkinfo', 'del', keys, item)
    
def unit_post_videowatermarkinfo_get(item):
    """
    【视频水印信息表】
    get
    item: get数据
    return: 提交结果
    """
    keys = [
    
        '_id', # 使用记录的ID查询
    
    ]
    return unit_post('videowatermarkinfo', 'get', keys, item)
    
def unit_post_videowatermarkinfo_filter(item):
    """
    【视频水印信息表】
    filter
    item: filter数据
    return: 提交结果
    """
    keys = [
    
        'videoid', # 视频ID关联视频【SelectField】   videoinfo  videotitle 【视频标题】
        'watermarktext', # 水印文本【TextField】  非外键 
        'watermarkposition', # 水印位置如左上角、右下角等【CharField】  非外键 
        'watermarksize', # 水印大小如百分比或像素值【CharField】  非外键 
        'watermarkopacity', # 水印透明度0100%【CharField】  非外键 
        'createdat', # 创建时间【DateTimeField】  非外键 
        'updatedat', # 更新时间【DateTimeField】  非外键 
        'kwkwisactive', # 是否激活用于控制水印是否生效如0为未激活1为激活【BooleanField】  非外键 
        
    
    ]
    return unit_post('videowatermarkinfo', 'filter', keys, item)
    
def unit_post_videowatermarkinfo_view(item):
    """
    【视频水印信息表】
    view
    item: view数据
    return: 提交结果
    """
    keys = [
    
        '_id', # 使用记录的ID查询
    
    ]
    return unit_post('videowatermarkinfo', 'view', keys, item)
    
def unit_post_videowatermarkinfo_go_add(item):
    """
    【视频水印信息表】
    go_add
    item: go_add数据
    return: 提交结果
    """
    keys = [
    
    {'form':{
        'id':'',
    }}
    
    ]
    return unit_post('videowatermarkinfo', 'go_add', keys, item)
    
def unit_post_videowatermarkinfo_go_upd(item):
    """
    【视频水印信息表】
    go_upd
    item: go_upd数据
    return: 提交结果
    """
    keys = [
    
    {'form':{
        'id':'',
    }}
    
    ]
    return unit_post('videowatermarkinfo', 'go_upd', keys, item)
    


def unit_post_videocopyrightinfo_add(item):
    """
    【视频版权信息表】
    add
    item: add数据
    return: 提交结果
    """
    keys = [
    
        'videoid', # 关联视频ID【SelectField】   videoinfo  videotitle 【视频标题】
        'copyrightholder', # 版权持有人【CharField】  非外键 
        'copyrightyear', # 版权年份【CharField】  非外键 
        'licensetype', # 许可类型【CharField】  非外键 
        'licensestatus', # 许可状态【CharField】  非外键 
        'description', # 版权描述【TextField】  非外键 
        'creationdate', # 创建日期【DateField】  非外键 
        'modkwkwificationdate', # 修改日期【DateField】  非外键 
        'relatedvideoid', # 相关视频ID【UUIDField】  非外键 
        
    
    ]
    return unit_post('videocopyrightinfo', 'add', keys, item)
    
def unit_post_videocopyrightinfo_upd(item):
    """
    【视频版权信息表】
    upd
    item: upd数据
    return: 提交结果
    """
    keys = [
    
        'videoid', # 关联视频ID【SelectField】   videoinfo  videotitle 【视频标题】
        'copyrightholder', # 版权持有人【CharField】  非外键 
        'copyrightyear', # 版权年份【CharField】  非外键 
        'licensetype', # 许可类型【CharField】  非外键 
        'licensestatus', # 许可状态【CharField】  非外键 
        'description', # 版权描述【TextField】  非外键 
        'creationdate', # 创建日期【DateField】  非外键 
        'modkwkwificationdate', # 修改日期【DateField】  非外键 
        'relatedvideoid', # 相关视频ID【UUIDField】  非外键 
        
    
    ]
    return unit_post('videocopyrightinfo', 'upd', keys, item)
    
def unit_post_videocopyrightinfo_del(item):
    """
    【视频版权信息表】
    del
    item: del数据
    return: 提交结果
    """
    keys = [
    
        '_id', # 使用记录的ID查询
    
    ]
    return unit_post('videocopyrightinfo', 'del', keys, item)
    
def unit_post_videocopyrightinfo_get(item):
    """
    【视频版权信息表】
    get
    item: get数据
    return: 提交结果
    """
    keys = [
    
        '_id', # 使用记录的ID查询
    
    ]
    return unit_post('videocopyrightinfo', 'get', keys, item)
    
def unit_post_videocopyrightinfo_filter(item):
    """
    【视频版权信息表】
    filter
    item: filter数据
    return: 提交结果
    """
    keys = [
    
        'videoid', # 关联视频ID【SelectField】   videoinfo  videotitle 【视频标题】
        'copyrightholder', # 版权持有人【CharField】  非外键 
        'copyrightyear', # 版权年份【CharField】  非外键 
        'licensetype', # 许可类型【CharField】  非外键 
        'licensestatus', # 许可状态【CharField】  非外键 
        'description', # 版权描述【TextField】  非外键 
        'creationdate', # 创建日期【DateField】  非外键 
        'modkwkwificationdate', # 修改日期【DateField】  非外键 
        'relatedvideoid', # 相关视频ID【UUIDField】  非外键 
        
    
    ]
    return unit_post('videocopyrightinfo', 'filter', keys, item)
    
def unit_post_videocopyrightinfo_view(item):
    """
    【视频版权信息表】
    view
    item: view数据
    return: 提交结果
    """
    keys = [
    
        '_id', # 使用记录的ID查询
    
    ]
    return unit_post('videocopyrightinfo', 'view', keys, item)
    
def unit_post_videocopyrightinfo_go_add(item):
    """
    【视频版权信息表】
    go_add
    item: go_add数据
    return: 提交结果
    """
    keys = [
    
    {'form':{
        'id':'',
    }}
    
    ]
    return unit_post('videocopyrightinfo', 'go_add', keys, item)
    
def unit_post_videocopyrightinfo_go_upd(item):
    """
    【视频版权信息表】
    go_upd
    item: go_upd数据
    return: 提交结果
    """
    keys = [
    
    {'form':{
        'id':'',
    }}
    
    ]
    return unit_post('videocopyrightinfo', 'go_upd', keys, item)
    


def unit_post_supermanager_add(item):
    """
    【系统管理员】
    add
    item: add数据
    return: 提交结果
    """
    keys = [
    
        'username', # 管理员姓名【CharField】  非外键 
        
    
    ]
    return unit_post('supermanager', 'add', keys, item)
    
def unit_post_supermanager_upd(item):
    """
    【系统管理员】
    upd
    item: upd数据
    return: 提交结果
    """
    keys = [
    
        'username', # 管理员姓名【CharField】  非外键 
        
    
    ]
    return unit_post('supermanager', 'upd', keys, item)
    
def unit_post_supermanager_del(item):
    """
    【系统管理员】
    del
    item: del数据
    return: 提交结果
    """
    keys = [
    
        '_id', # 使用记录的ID查询
    
    ]
    return unit_post('supermanager', 'del', keys, item)
    
def unit_post_supermanager_get(item):
    """
    【系统管理员】
    get
    item: get数据
    return: 提交结果
    """
    keys = [
    
        '_id', # 使用记录的ID查询
    
    ]
    return unit_post('supermanager', 'get', keys, item)
    
def unit_post_supermanager_filter(item):
    """
    【系统管理员】
    filter
    item: filter数据
    return: 提交结果
    """
    keys = [
    
        'username', # 管理员姓名【CharField】  非外键 
        
    
    ]
    return unit_post('supermanager', 'filter', keys, item)
    
def unit_post_supermanager_view(item):
    """
    【系统管理员】
    view
    item: view数据
    return: 提交结果
    """
    keys = [
    
        '_id', # 使用记录的ID查询
    
    ]
    return unit_post('supermanager', 'view', keys, item)
    
def unit_post_supermanager_go_add(item):
    """
    【系统管理员】
    go_add
    item: go_add数据
    return: 提交结果
    """
    keys = [
    
    {'form':{
        'id':'',
    }}
    
    ]
    return unit_post('supermanager', 'go_add', keys, item)
    
def unit_post_supermanager_go_upd(item):
    """
    【系统管理员】
    go_upd
    item: go_upd数据
    return: 提交结果
    """
    keys = [
    
    {'form':{
        'id':'',
    }}
    
    ]
    return unit_post('supermanager', 'go_upd', keys, item)
    

