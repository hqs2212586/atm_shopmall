# -*- encoding:utf-8 -*-
import os
import logging

# /Users/.../atm_shopmall/atm
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 根目录

# /Users/.../atm_shopmall/atm/db/accounts
DB_PATH = "%s/db/accounts" % BASE_DIR  # 账户目录

# 日志等级：DEBUG\INFO\WARNING\ERRPR\CRITICAL
LOG_LEVEL = logging.INFO

LOG_TYPES = {
    'transaction': 'transactions.log',  # 交易日志
    'access': 'access.log'    # 操作日志
}
# /Users/.../atm_shopmall/atm/log
LOG_PATH = os.path.join(BASE_DIR, 'log')

LOG_FORMAT = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

# 设置手续费
TRANSACTION_TYPE = {
    'repay': {'action': 'plus', 'interest': 0},   # 还款无手续费
    'withdraw': {'action': 'minus', 'interest': 0.05},  # 取现手续费5%
    'transfer': {'action': 'minus', 'interest': 0.05},  # 转账手续费5%
    'consume': {'action': 'minus', 'interest': 0}  # 消费无手续费
}
