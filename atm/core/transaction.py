# -*- encoding:utf-8 -*-

from conf import settings
from .db_handler import save_db


def make_transaction(logger, user_obj, tran_type, amount, **kwargs):
    """
    处理所有的交易
    :param account_data: 用户账户数据
    :param tran_type: 交易类型
    :param amount: 交易数量
    :param kwargs: mainly for logging usage
    :return: 
    """
    amount = float(amount)
    if tran_type in settings.TRANSATION_TYPE:
        interest = amount * settings.TRANSACTION_TYPE[tran_type]['interest'] # 算出利息
        old_balance = user_obj['data']['balance']
        if settings.TRANSACTION_TYPE[tran_type]['action'] == 'plus':
            new_balance = old_balance + amount + interest
        elif settings.TRANSACTION_TYPE[tran_type]['action'] == 'minus':
            new_balance = old_balance - amount - interest
            # check credit
            if new_balance < 0:  # 余额不足
                print('''\033[31;1mYour credit [%s] is not enough for this transaction [-%s],
                your current balance is [%s]''' %(user_obj['data']['credit'], (amount + interest), old_balance))
                return {'status': 1, 'error': '交易失败，余额不足'}

        user_obj['data']['balance'] = new_balance  # 把新余额存到用户内存账户数据里
        save_db(user_obj['data'])   # 数据要同时更新到硬盘账户文件中

        logger.info("account:%s   action:%s   amount:%s  interest:%s   balance:%s" %
                    (user_obj['data']['id'], tran_type, amount, interest, new_balance) )
        return {'status': 0, 'msg': '交易操作成功'}
    else:
        print("\033[31;1mTransaction type [%s] is not exist!\033[0m" % tran_type)
        return {'status': 1, 'error': '交易失败，Transaction type [%s] is not exist!' % tran_type}
