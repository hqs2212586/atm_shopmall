# -*- encoding:utf-8 -*-
import os, time, json
from shop_conf import settings


def find_all_account():
    """获取shop_db/users下用户名列表"""
    account_data_path = settings.USER_PATH
    account_list = os.listdir(account_data_path)  # 查看目录下所有用户文件,列表形式返回
    all_account = []
    if account_list != []:
        for accountid_file in account_list:
            all_account.append(accountid_file.split('.')[0])  # json文件只取账户名
    return all_account


def load_account_data(account):
    """根据username找到对应的账户文件，并加载"""
    account_file = os.path.join(settings.USER_PATH, "%s.json" % account)
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
    account_file = os.path.join(settings.USER_PATH, "%s.json" % account_data['username'])
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
    account_file = os.path.join(settings.USER_PATH, "%s.json" % account_data['username'])
    if os.path.isfile(account_file):
        return {'status': -1, 'error':"account file is existed."}
    else:
        f = open("%s" % account_file, "w")  # 创建新文件不用改名
        data = json.dump(account_data, f)
        f.close()
        return {'status': 0, 'data': data}


def load_goods_data(goods):
    goods_file = os.path.join(settings.GOODS_PATH, "%s.json" % goods)
    if os.path.isfile(goods_file):  # 判断文件是否存在
        f = open(goods_file)
        data = json.load(f)  # json dict字典
        f.close()
        return data
