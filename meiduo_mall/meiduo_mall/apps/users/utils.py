# 自定义用户认证的后端：实现多账号登录
from django.contrib.auth.backends import ModelBackend
import re

from users.models import User


def get_user_by_account(account):
    try:
        if re.match(r'^1[3-9]\d{9}$', account):
            # account == 手机号
            user = User.objects.get(mobile=account)
        else:
            # account == 用户名
            user = User.objects.get(username=account)
    except User.DoesNotExist:
        return None
    else:

        return user

class UsernameMobileBackend(ModelBackend):
    """自定义用户认证后端"""
    def authenticate(self, request, username=None, password=None, **kwargs):
        """重写用户认证的方法"""
        # 查询用户
        user = get_user_by_account(username)

        # 如果可以查询到用户，好需要校验密码是否正确
        if user and user.check_password(password):
            # 返回user
            return user
        else:
            return None