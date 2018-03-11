# -*- encoding:utf-8 -*-
from core.transaction import make_transaction
from core import utils
from core.utils import print_warning


def view_account_info(account_data, *args, **kwargs):
    """查看状态状态"""
    trans_logger = kwargs.get("transaction_logger")
    print("ACCOUNT_INFO".center(50, '-'))
    for k, v in account_data['data'].items():
        if k not in ('password',):
            print("%15s: %s" % (k, v))
    print("END".center(50, '-'))


def with_draw(account_data, *args, **kwargs):
    """取现"""
    trans_logger = kwargs.get("transaction_logger")
    current_balance = ''' ---------BALANCE INFO---------
        Credit :      %s
        Balance :     %s''' % (account_data['data']['credit'], account_data['data']['balance'])
    print(current_balance)
    back_flag = False
    while not back_flag:
        withdraw_amount = input("请输入取现金额：[b：返回]").strip()   # 取款金额
        if len(withdraw_amount) > 0 and withdraw_amount.isdigit():
            withdraw_amount = int(withdraw_amount)
            if (account_data['data']['balance'] / 2) >= withdraw_amount:   # balance一次只能取一半
                transaction_result = make_transaction(trans_logger, account_data, 'withdraw', withdraw_amount)   # 交易完成状态：'status':0
                if transaction_result['status'] == 0:
                    print('''New Balance:%s ''' % (account_data['data']['balance']))
                else:
                    print(transaction_result)
            else:
                print_warning("可取余额不足，可提现%s"% ( int(account_data['data']['balance'] / 2)))

        if withdraw_amount == 'b':
            back_flag = True


def transfer(account_data, *args, **kwargs):
    """转账"""
    trans_logger = kwargs.get("transaction_logger")
    current_balance = ''' ---------BALANCE INFO---------
        Balance :     %s''' % (account_data['data']['balance'])
    print(current_balance)

    from .db_handler import load_account_data
    n = 0
    while n < 3:
        goal_acc = input("请输入要转账银行卡id：")
        goal_data = load_account_data(goal_acc)
        n += 1
        if goal_data['status'] == 0:
            back_flag = False
            while not back_flag:
                transfer_amount = input("\033[33;1m请输入要转账的金额：\033[0m").strip()  # 转账金额
                if len(transfer_amount) > 0 and transfer_amount.isdigit():
                    transfer_amount = int(transfer_amount)
                    if (account_data['data']['balance'] / 2) >= transfer_amount:  # balance转账限制
                        transaction_result = make_transaction(trans_logger, account_data, 'transfer', transfer_amount)
                        transaction_goal_result = make_transaction(trans_logger, goal_data, 'repay', transfer_amount)
                        if transaction_result['status'] == 0 and transaction_goal_result ==0:
                            print('''\033[42;1mNew Balance:%s\033[0m''' % (account_data['data']['balance']))
                            n = 3
                        else:
                            print(transaction_result,transaction_goal_result)


def pay_back(account_data, *args, **kwargs):
    """还款"""
    trans_logger = kwargs.get("transaction_logger")
    current_balance = ''' ---------BALANCE INFO---------
        Credit :      %s
        Balance :     %s''' % (account_data['data']['credit'], account_data['data']['balance'])
    print(current_balance)
    repay_amount = input("\033[33;1m请输入要还款的金额：\033[0m").strip()
    if len(repay_amount) > 0 and repay_amount.isdigit():
        repay_amount = int(repay_amount)
        transaction_result = make_transaction(trans_logger, account_data, 'repay', repay_amount)
        if transaction_result['status'] == 0:
            print('''\033[42;1mNew Balance:%s\033[0m''' % (account_data['data']['balance']))
        else:
            print(transaction_result)


def consume(account_data, *args, **kwargs):
    """消费"""
    trans_logger = kwargs.get("transaction_logger")
    current_balance = ''' ---------BALANCE INFO---------
            Credit :      %s
            Balance :     %s''' % (account_data['data']['credit'], account_data['data']['balance'])
    print(current_balance)
    back_flag = False
    while not back_flag:
        consume_amount = args.strip()  # 取款金额
        if len(consume_amount) > 0 and consume_amount.isdigit():
            consume_amount = int(consume_amount)
            if (account_data['data']['balance'] ) >= consume_amount:
                transaction_result = make_transaction(trans_logger, account_data, 'consume',
                                                      consume_amount)  # 交易完成状态：'status':0
                if transaction_result['status'] == 0:
                    print('''New Balance:%s ''' % (account_data['data']['balance']))
                else:
                    print(transaction_result)
            else:
                print_warning("可取余额不足，可提现%s" % (int(account_data['data']['balance'] / 2)))

        if consume_amount == 'b':
            back_flag = True