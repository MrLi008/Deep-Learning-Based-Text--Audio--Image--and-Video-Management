"""
WSGI config for 基于深度学习的文案语音图片视频管理分析-视频矩阵系统 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "基于深度学习的文案语音图片视频管理分析-视频矩阵系统.settings",
)

application = get_wsgi_application()
