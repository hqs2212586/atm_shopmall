# -*- encoding:utf-8 -*-
from .auth import authenticate
from .utils import print_error
from .logger import logger
from core import logics
from .user_manage import freeze

transaction_logger = logger("transaction")  # 交易
access_logger = logger("access")  # 操作

features = [
    ('账户信息', logics.view_account_info),
    ('取款', logics.with_draw),
    ('还款', logics.pay_back),
    ('转账', logics.transfer),
    ('消费', logics.consume)
]


def controller(user_obj):
    """功能分配"""
    while True:
        for index, feature in enumerate(features):
            print(index, feature[0])
        choice = input("ATM>>: [退出:exit]").strip()
        if not choice: continue   # 没输入就继续
        if choice.isdigit():
            choice = int(choice)
            if choice < len(features) and choice >= 0:
                features[choice][1](user_obj, transaction_logger=transaction_logger, access_logger=access_logger)
        if choice == 'exit':
            exit("Bye.")


def entrance():
    """ATM程序交互入口"""
    user_obj = {  # object
        'is_authenticated': False,  # 用户是否已认证
        'data': None
    }
    retry_count = 0
    while user_obj['is_authenticated'] is not True:  # 未认证
        account = input("\033[32;1m account:\033[0m").strip()
        password = input("\033[32;1m password:\033[0m").strip()
        auth_data = authenticate(account, password)  # 验证
        if auth_data:   # not None means passed the authentication
            # 拿到账户数据 auth_data
            user_obj['is_authenticated'] = True  # 其他函数直接可以通过user_obj就能知道，用户是否登录
            user_obj['data'] = auth_data  # 由None改为账户数据
            print("welcome")
            access_logger.info("user %s just logged in" % user_obj['data']['id'])

            controller(user_obj)
        else:  # None的情况
            print_error("Wrong username or password!")
        retry_count += 1

        if retry_count == 3:  # 尝试3次失败
            msg = "user %s tried wrong password reached 3 times" % account
            freeze(account)
            print_error(msg)
            access_logger.info(msg)
            break
