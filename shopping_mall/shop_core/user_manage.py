
import os
from .logger import logger
from shop_core import db_handler
from shop_db import user_sample
from shop_core import utils


def register_account():
    """注册用户"""
    count = 0
    all_account_list = db_handler.find_all_account()  # 所有用户
    while count < 3:
        account = input("\033[32;1m Please input username:\033[0m")
        count += 1
        if account in all_account_list:
            print("[%s] 已经被注册过了！" % account)
        else:
            password = input("\033[32;1m password:\033[0m")
            account_data = user_sample.user_dic
            account_data['username'] = account
            account_data['password'] = password
            db_handler.create_db(account_data)   # 创建新用户
            # 日志
            access_logger = logger('access')
            access_logger.info('%s registered successful!!' % account)
            print('\033[32;1maccount [%s] registered successfull\033[0m' % account)
            count = 3


def reset_passwd():
    """重置密码"""
    account = input("\033[32;1m Please input the account which need to reset passwd:\033[0m")
    all_account_list = db_handler.find_all_account()
    if account not in all_account_list:
        utils.print_error('[%s] has not been registered yet!')
    else:
        account_data = db_handler.load_account_data(account)['data']
        account_data['password'] = user_sample.user_dic['password']
        db_handler.save_db(account_data)
        # 日志
        access_logger = logger('access')
        access_logger.warning('%s reset password successful!' % account)
        print('\033[32;1maccount [%s] reset password successfull\033[0m' % account)


def freeze():
    """冻结账户（不允许登录）"""
    account = input("\033[32;1m Please input freeze account:\033[0m")
    all_account_list = db_handler.find_all_account()
    if account not in all_account_list:
        utils.print_error("%s is not in account list!" % account)
    else:
        account_data = db_handler.load_account_data(account)['data']
        account_data['status'] = 1  # 这个地方待定（locked）
        db_handler.save_db(account_data)
        # 日志
        access_logger = logger('access')
        access_logger.warning('freeze %s successful!' % account)
        print('\033[32;1maccount [%s] freeze successfull\033[0m' % account)


def unfreeze():
    """解冻账户"""
    account = input("\033[32;1m Please input account:\033[0m")
    all_account_list = db_handler.find_all_account()
    if account not in all_account_list:
        utils.print_error('No account [%s]' % account)
    else:
        account_data = db_handler.load_account_data(account)['data']
        account_data['status'] = 0  # 不判断，设置状态为正常
        db_handler.save_db(account_data)
        # 日志
        access_logger = logger('access')
        access_logger.warning('unfreeze %s successful!' % account)
        print('\033[32;1maccount [%s] unfreeze successfull\033[0m' % account)


def entrance():
    """ATM管理"""
    menu_title = "\033[31;m User Management Action Menu \033[0m".center(50,'-')
    menu_list = """\033[32;1m
    1.注册用户    2.重置密码
    3.冻结用户    4.解冻用户
    q.退出\033[0m
    """
    menu = menu_title + menu_list + '-' * 44
    menu_dict = {
        '1':register_account,
        '2':reset_passwd,
        '3':freeze,
        '4':unfreeze
    }
    exit_flag = False
    while not exit_flag:
        print(menu)
        user_option = input('>> ').strip()
        if user_option in menu_dict:
            menu_dict[user_option]()  # 调用函数
        elif user_option == 'q':
            exit()
        else:
            print("请输入正确的选项编号！")
