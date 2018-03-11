# -*- encoding: utf-8 -*-
# 管理商城用户账号信息
import sys, os

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(base_dir)  # 添加到环境变量
# print(sys.path)

from shop_core import user_manage

if __name__ == '__main__':
    user_manage.entrance()