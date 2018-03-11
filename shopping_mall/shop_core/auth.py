# -*- encoding:utf-8 -*-

from .db_handler import load_account_data
from .utils import print_error


def authenticate(account, password):
    """对用户信息进行验证"""
    account_data = load_account_data(account)
    if account_data['status'] == 0:  # 0代表账户文件加载成功
        account_data = account_data['data']  # 赋值，真正的用户数据
        if account_data['status'] == 0:
            if password == account_data['password']:  # 密码相同认证成功
                return account_data  # 返回账户数据（如有操作可以在内存直接修改）
            else:
                return None
        else:
            print_error("账户已经锁定")
            return None
    else:
        return None