
# 用户操作信用卡
import os, sys

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# '/Users/huangqiushi/PycharmProjects/atm_shopmall/atm'
sys.path.append(base_dir)  # 添加到环境变量
# print(sys.path)

from core import main
if __name__ == '__main__':
    main.entrance()