
# 商城运行主程序

import os, sys

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # abspath绝对路径
# '/Users/huangqiushi/PycharmProjects/atm_shopmall/shopping_mall'
sys.path.append(base_dir)

atm_base_dir = __file__
for i in range(3):
    atm_base_dir = os.path.dirname(atm_base_dir)
# print(atm_base_dir)
atm_dir = '%s/atm' % atm_base_dir
sys.path.append(atm_dir)  # 添加atm路径到系统路径中

from shop_core import main

if __name__ == '__main__':
    main.entrance()
