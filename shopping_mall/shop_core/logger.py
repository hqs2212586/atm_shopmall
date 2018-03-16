# -*- encoding:utf-8 -*-
import logging, os
from shop_conf import settings


def logger(log_type):  # access or  transaction or shop
    # create logger
    logger = logging.getLogger(log_type)
    logger.setLevel(settings.LOG_LEVEL)

    log_file = os.path.join(settings.LOG_PATH, settings.LOG_TYPES[log_type])
    fh = logging.FileHandler(log_file)   # 向文件输出日志，并且会打开文件
    fh.setLevel(settings.LOG_LEVEL)  # 设置统一的日志级别
    formatter = settings.LOG_FORMAT

    # add formatter to ch and fh
    fh.setFormatter(formatter)

    logger.addHandler(fh)

    return logger  # 返回内存对象

