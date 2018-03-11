# -*- encoding:utf-8 -*-
# 管理接口，包括添加账户、查看用户额度、冻结账户
# 信用卡管理接口(系统管理员)

import os, sys


base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)  # 添加到环境变量
# print(sys.path)

from core import user_manage
if __name__ == '__main__':
    user_manage.entrance()