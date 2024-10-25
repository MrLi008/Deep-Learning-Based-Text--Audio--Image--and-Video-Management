"""
ASGI config for ____ project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault(
    "DJANGO_SETTINGS_MODULE",
    "基于深度学习的文案语音图片视频管理分析-视频矩阵系统.settings",
)

application = get_asgi_application()
