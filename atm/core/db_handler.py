# -*- encoding:utf-8 -*-
import os, time, json
from conf import settings  # 程序入口是atm_server.py


def find_all_account():
    """获取db/accounts下用户名列表"""
    account_data_path = settings.DB_PATH
    account_list = os.listdir(account_data_path)  # 查看目录下所有用户文件,列表形式返回
    all_account = []
    if account_list != []:
        for accountid_file in account_list:
            all_account.append(accountid_file.split('.')[0])  # json文件只取账户名
    return all_account


def load_account_data(account):
    """根据account id找到对应的账户文件，并加载"""
    account_file = os.path.join(settings.DB_PATH, "%s.json" % account)
    if os.path.isfile(account_file):  # 判断文件是否存在
        f = open(account_file)
        data = json.load(f)  # json dict字典
        f.close()
        return {'status': 0, 'data': data}
        # return {'status': 0, 'data': data}
    else:
        return {'status': -1, 'error': "account file does not exist."}


def save_db(account_data):
    """根据account_data找到对应的账户文件，把内存里的用户数据保存到硬盘"""
    account_file = os.path.join(settings.DB_PATH, "%s.json" % account_data['id'])   # account_file='/Users/.../atm_shopmall/atm/db/accounts/1234.json'
    if os.path.isfile(account_file):   # 判断账户文件是否存在
        f = open("%s.new" % account_file, "w")  # 创建文件对象
        data = json.dump(account_data, f)  # # dump不仅将数据变为字符串还直接写入文件，但是只能存入文件对象中
        f.close()
        os.rename("%s.new" % account_file, account_file)
        return {'status': 0, 'data': data}
    else:
        return {'status':-1,'error': "account file does not exist."}


def create_db(account_data):
    """为新用户创建账户文件，并把内存的数据保存到硬盘"""
    account_file = os.path.join(settings.DB_PATH, "%s.json" % account_data['id'])
    if os.path.isfile(account_file):
        return {'status': -1, 'error':"account file is existed."}
    else:
        f = open("%s" % account_file, "w")  # 创建新文件不用改名
        data = json.dump(account_data, f)
        f.close()
        return {'status': 0, 'data': data}


