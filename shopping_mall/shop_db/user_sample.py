import json
import time, datetime

enroll_date = time.strftime('%Y-%m-%d')  # 转化为格式化的时间字符串
# datetime时间计算
expire_date = datetime.datetime.now() + datetime.timedelta(days=1000)
expire_date = expire_date.strftime('%Y-%m-%d')

user_dic = {
    'username': 'hqs',
    'password': 'abc',
    'enroll_date': enroll_date,
    'expire_date': expire_date,
    'status': 0,  # 0 = normal, 1 = locked, 2 = disabled
    'laset_login_time': time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())  # locltime本地时间
}
