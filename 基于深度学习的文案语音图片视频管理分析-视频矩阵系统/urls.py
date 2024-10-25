"""
URL configuration for 基于深度学习的文案语音图片视频管理分析-视频矩阵系统 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns
from django.urls import path, include, re_path
from .settings import MEDIA_ROOT, MEDIA_URL

from captcha.views import captcha_image
from config_unit.views import refresh_view
from sys_user.views import admin_logout_view

urlpatterns = [
    path("admin/logout/", admin_logout_view, name="logout"),
    path("admin/", admin.site.urls),
    path("captcha/", include("captcha.urls")),
    # 用于系统用户登录注册功能合集
    path("", include("sys_user.urls")),
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(MEDIA_URL, document_root=MEDIA_ROOT)

urlpatterns += [
    path("appcenter/", include("appcenter.urls")),
    path("config_busi/", include("config_busi.urls")),
    path("config_visual/", include("config_visual.urls")),
    # Implement For Vue Or Other
    path("config_unit/", include("config_unit.urls")),
    # 预览验证码
    re_path(
        "captcha/image/(?P<key>\w+)/$",
        captcha_image,
        name="captcha-image",
    ),
    # 刷新验证码
    path("captcha/refresh/", refresh_view, name="views_refresh"),
]
