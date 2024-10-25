from django.urls import path, re_path, include
from captcha.views import captcha_image

from . import views

urlpatterns = [
    # 查看接口文档
    path("", views.index_view, name="config_unit_views"),
    # 登录注册接口
    path("login", views.login_view, name="views_login"),
    path("logout", views.logout_view, name="views_logout"),
    path("register", views.register, name="views_register"),
    path("index", views.index_view, name="views_index"),
    # 下载打包文件
    re_path(
        r"config_unit/media/(?P<path>.*?).zip$", views.serve_media, name="serve_media"
    ),
    # 用于业务表,用户表,访问权限查询
    path("submit", views.submit_view, name="submit_view"),
    path(
        "config_unit/table_busi", views.table_busi, name="config_unit_views_table_busi"
    ),
    path(
        "config_unit/table_user", views.table_user, name="config_unit_views_table_user"
    ),
    path(
        "config_unit/auth_table", views.auth_table, name="config_unit_views_auth_table"
    ),
    re_path(
        "config_unit/common_form/(?P<tablename>.+)$",
        views.common_form,
        name="config_unit_views_common_form",
    ),
    # 预览验证码
    re_path(
        "captcha/image/(?P<key>\w+)/$",
        captcha_image,
        name="captcha-image",
    ),
    # 刷新验证码
    path("captcha/refresh/", views.refresh_view, name="views_refresh"),
    # 数据接口 所有跨表改数据部分,均以发起表作为基准
    re_path(
        r"config_unit/(?P<tablename>.+)$", views.config_unit, name="config_unit_views"
    ),
    path("ucsrf", views.ucsrf, name="views_ucsrf"),
]
