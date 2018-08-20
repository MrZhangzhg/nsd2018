import time

t1 = time.localtime()  # 返回九元组
time.gmtime()  # 0时区的九元组
time.time()  # 返回时间戳，常用
time.mktime(t1)  # 把九元组转换成时间戳
time.sleep(1)
time.asctime()  # 默认返回当前的UTC时间
time.ctime()    # 默认返回当前的UTC时间，常用
time.ctime(0)  # 时间戳作为参数
time.asctime(t1)
time.strftime('%Y-%m-%d %H:%M:%S')  # 常用
time.strptime('2018-08-20', '%Y-%m-%d')  # 转九元组


from datetime import datetime, timedelta
t1 = datetime.now()
t1.year
t1.month
t2 = datetime.today()  # 类似于datetime.now，只是参数不一样
datetime.strptime('2018-8-20', '%Y-%m-%d')  # 返回datetime对象

dt = timedelta(days=100)
t1 - dt
t1 + dt
















