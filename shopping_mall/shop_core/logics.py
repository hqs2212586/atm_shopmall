# -*- encoding:utf-8 -*-
import os,json
from shop_conf import settings
from shop_core import db_handler
from shop_conf import settings
from shop_core import utils
from shop_core import logger
from shop_core.transaction import make_transaction

# atm下的库
from core import main as atm_main
from core import db_handler as atm_handler
from core import logger as atm_logger
from core import logics as atm_logics


def sales_list():
    """获取shop_db/goods下商品列表"""
    goods_data_path = settings.GOODS_PATH
    goods_list = os.listdir(goods_data_path)  # 查看目录下所有商品文件
    all_goods = []
    if goods_list != []:
        for goods_file in goods_list:
            all_goods.append(goods_file.split('.')[0])  # 商品文件名
        goods_dic = {}
        for goods in all_goods:
            goods_data = db_handler.load_goods_data(goods)
            goods_dic[goods_data['name']] = goods_data['price']
        return goods_dic
            # {'macbook': '15000', 'iphone8': '6888'}
    else:
        utils.print_error("没有商品！")


def goods_menu():
    """商品清单"""
    goods_dic = sales_list()
    menu_title = "\033[31;m 商品清单 \033[0m".center(50, '-')
    def menu_body():
        #label = 0
        for k, v in goods_dic.items():
            # raw = str(label, k, v)
            raw = k + ' : ' + v
            print(raw.ljust(50,'-'))
            # label += 1
    print(menu_title)
    menu_body()


def shopping():
    """商品添加进购物车"""
    exit_flag = False
    while not exit_flag:
        flag = input('是否确认加入购物车？(Y/N)').strip()
        if flag == 'Y':
            exit_flag = True
        elif flag == 'N':
            exit()
        else:
            utils.print_error('无效输入！')
            continue
        price = choice_goods()
    return


def choice_goods():
    goods_dic = sales_list()
    bought_goods_list = []
    exit_flag = False
    while not exit_flag:
        choice_name = input("请输入你要买的商品的名称：【退出：q,检查：c】")
        for i in goods_dic.keys:
            if choice_name == i:
                bought_goods_list.append(choice_name)
                bought_goods_price = int(goods_dic[choice_name])  # 价格
                print('\033[1;31;44m%s\033[0m 已经被添加进购物车！' % choice_name)
                access_logger = logger('access')
                access_logger.info('%s 已经添加进购物车！！'% choice_name)
                bought_goods_price += bought_goods_price
            elif choice_name == 'q':
                utils.print_info("欢迎再次选购！", bought_goods_list)
                exit_flag = True
            elif choice_name == 'c':
                utils.print_info("购物侧商品清单".center(50, '-'))
                for i in bought_goods_list: print(i)
                utils.print_info("商品总价格",bought_goods_price)
            else:
                utils.print_error("请输入正确的商品名称！！")
    goods_car = [bought_goods_list, bought_goods_price]
    return goods_car


def payment(account_data, *args, **kwargs):
    atm_main.entrance()
