from dbconn import Departments, Employees, Session

session = Session()
# hr = Departments(dep_name='人事部')
# print(hr.dep_name)
# print(hr.dep_id)   # 因为没有真正写数据库，所以dep_id是None
# session.add(hr)
# session.commit()
# print(hr.dep_id)   # commit至数据库后，dep_id有值了
#############################
# ops = Departments(dep_id=2, dep_name='运维部')
# dev = Departments(dep_id=3, dep_name='开发部')
# session.add_all([ops, dev])
#############################
wyc = Employees(
    name='王亚超',
    gender='男',
    birth_date='1993-5-8',
    phone='13322334455',
    email='wyc@qq.com',
    dep_id=1
)
cyj = Employees(
    name='陈雅津',
    gender='女',
    birth_date='2000-1-15',
    phone='13367895432',
    email='cyj@163.com',
    dep_id=1
)
hjx = Employees(
    name='花俊秀',
    gender='男',
    birth_date='1999-3-10',
    phone='18812345678',
    email='hjx@qq.com',
    dep_id='2'
)
htq = Employees(
    name='黄天强',
    gender='男',
    birth_date='1995-5-20',
    phone='15078986655',
    email='htq@163.com',
    dep_id=3
)
session.add_all([wyc, cyj, hjx, htq])

session.commit()
session.close()
