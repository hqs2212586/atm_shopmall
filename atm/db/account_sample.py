import json, time, datetime


enroll_date = time.strftime('%Y-%m-%d')  # 转化为格式化的时间字符串
# datetime时间计算
expire_date = datetime.datetime.now() + datetime.timedelta(days=1000)
# expire_date = datetime.datetime.now().replace(year=expire_year+10).strftime('%Y-%m-%d')   加十年
expire_date = expire_date.strftime('%Y-%m-%d')

acc_dic = {
    'id': 1234,
    'password': 'abc',
    'credit': 15000,
    'balance': 15000,
    'enroll_date': enroll_date,
    'expire_date': expire_date,
    'pay_day': 22,
    'status': 0  # 0 = normal, 1 = locked, 2 = disabled
}
