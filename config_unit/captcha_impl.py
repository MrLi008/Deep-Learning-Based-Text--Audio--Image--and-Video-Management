#     -*-    coding: utf-8   -*-
# @File     :       captcah_util.py
# @Time     :       2023/7/17 12:02
# Author    :       摸鱼呀阿凡
# Contact   :       f2095522823@gmail.com
# License   :       MIT LICENSE

import base64

from captcha.conf import settings
from captcha.models import CaptchaStore
from captcha.helpers import captcha_audio_url, captcha_image_url
from captcha.views import captcha_image
from django.utils import timezone


def get_refresh_captcha(request, choose: int = 1):
    """
    获取新的验证码
    :param request
    :param choose 1 or 2
    :return CaptchaItem_url or CaptchaItem_count
    """

    key = CaptchaStore.pick()
    imgurl = captcha_image_url(key).replace("config_unit", "api")
    return {
        "key": key,
        "imgurl": imgurl,
        "captcha_0": imgurl.split("/")[-2],
        "captcha_1": key,
    }


def verify(key: str, code: str) -> str:
    """
    检查输入的验证码是否正确并处理超时和错误情况
    """
    current_time = timezone.now()
    try:
        captcha = CaptchaStore.objects.get(response=code, hashkey=key)

        # 检查验证码是否超时

        if captcha.expiration < current_time:
            captcha.delete()
            return "超时"  # 返回超时提示
        # 验证码正确，删除记录并返回成功

        captcha.delete()
        return "成功"  # 返回成功提示
    except CaptchaStore.DoesNotExist:
        # 清理过期的验证码记录

        CaptchaStore.remove_expired()
        return "错误"  # 返回错误提示
