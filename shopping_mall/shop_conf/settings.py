# -*- encoding:utf-8 -*-
import os
import logging

# /Users/.../atm_shopmall/shopping_mall
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__))) # 根目录


GOODS_PATH = "%s/shop_db/goods" % BASE_DIR  # 商品目录

# /Users/.../atm_shopmall/atm/shopping_mall/accounts
USER_PATH = "%s/shop_db/users" % BASE_DIR  # 账户目录

# 日志等级：DEBUG\INFO\WARNING\ERRPR\CRITICAL
LOG_LEVEL = logging.INFO

LOG_TYPES = {
    'transaction': 'transaction.log',  # 交易日志
    'access': 'access.log'   # 操作日志
}

LOG_PATH = os.path.join(BASE_DIR, 'shop_log')

LOG_FORMAT = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

