# -*- encoding:utf-8 -*-
from .auth import authenticate
from .utils import print_error
from .logger import logger
from core import logics

transaction_logger = logger("transaction")  # 交易
access_logger = logger("access")  # 操作

features = [
    ('账户信息', logics.view_account_info),
    ('取款', logics.with_draw),
    ('还款', logics.pay_back)
]


def controller(user_obj):
    """功能分配"""
    while True:
        for index, feature in enumerate(features):
            print(index, feature[0])
        choice = input("ATM>>:").strip()
        if not choice: continue   # 没输入就继续
        if choice.isdigit():
            choice = int(choice)
            if choice < len(features) and choice >= 0:
                features[choice][1](user_obj, transaction_logger=transaction_logger, access_loger=access_logger)
        if choice == 'exit':
            exit("Bye.")


def entrance():
    """ATM程序交互入口"""
    user_obj = { # object
        'is_authenticated': False, # 用户是否已认证
        'data': None
    }

    retry_count = 0
    while user_obj['is_authenticated'] is not True: # 未认证
        account = input("account:").strip()
        password = input("password:").strip()
        auth_data = authenticate(account, password)  # 验证
        if auth_data:   # not None means passed the authentication
            # 拿到账户数据 auth_data
            user_obj['is_authenticated'] = True  # 其他函数直接可以通过user_obj就能知道，用户是否登录
            user_obj['data'] = auth_data  # 由None改为账户数据
            print("welcome")
            access_logger.info("user %s just logged in" %user_obj['data']['id'])

            controller(user_obj)
        else:  # None的情况
            print_error("Wrong username or password!")
        retry_count += 1

        if retry_count == 3:
            msg = "user %s tried wrong password reached 3 times" %account
            print_error(msg)
            access_logger.info(msg)
            break
