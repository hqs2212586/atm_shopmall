# -*- encoding:utf-8 -*-
import os
import logging

# /Users/huangqiushi/PycharmProjects/atm_shopmall/atm
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 根目录

# /Users/huangqiushi/PycharmProjects/atm_shopmall/atm/db/accounts
DB_PATH = "%s/db/accounts" % BASE_DIR  # 账户目录

LOG_LEVEL = logging.INFO
LOG_TYPES = {
    'transaction': 'transactions.log',
    'access': 'access.log'
}
# /Users/huangqiushi/PycharmProjects/atm_shopmall/atm/log
LOG_PATH = os.path.join(BASE_DIR, 'log')

LOG_FORMAT = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

TRANSACTION_TYPE = {
    'repay': {'action': 'plus', 'interest': 0},   # 还款无手续费
    'withdraw': {'action': 'minus', 'interest': 0.05},  # 取现手续费5%
    'transfer': {'action': 'minus', 'interest': 0.05},  # 转账手续费
    'consume': {'action': 'minus', 'interest': 0}  # 消费无手续费
}
