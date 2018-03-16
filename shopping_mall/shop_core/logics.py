# -*- encoding:utf-8 -*-
import os,json
from shop_conf import settings
from shop_core import db_handler
from shop_conf import settings
from shop_core import utils
from shop_core import logger
from .logger import logger  # 这样写才能直接调用logger函数
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
            order_form = choice_goods()
            print(order_form)
            exit_flag = True
        elif flag == 'N':
            exit()
        else:
            utils.print_error('无效输入！')
            continue


def choice_goods():
    goods_dic = sales_list()
    goods_car = []  # 不能用字典会去重
    goods_price = 0
    exit_flag = False
    while not exit_flag:
        choice_name = input("请输入你要买的商品的名称：【退出：q,检查：c】")
        if choice_name == 'q':
            utils.print_info("欢迎再次选购！", goods_car)
            exit_flag = True
        elif choice_name == 'c':
            utils.print_info("购物车商品清单".center(50, '-'))
            utils.print_info(goods_car)
            utils.print_info("商品总价格:" + str(goods_price))
        else:
            for name,price in goods_dic.items():
                if choice_name == name:
                    goods_car.append(choice_name)
                    goods_price = goods_price + int(price)
                    print('\033[1;31;44m%s\033[0m 已经被添加进购物车！' % choice_name)
                    shop_logger = logger('shop')
                    shop_logger.info('%s 已经添加进购物车！！'% choice_name)

    order_form = {goods_car:goods_price}
    return order_form


def payment(account_data, *args, **kwargs):
    atm_main.entrance()
