from dbconn import Department, Employee, Salary, Session

session = Session()
dep_dev = Department(dep_name='development')
dep_hr = Department(dep_name='人事部')
dep_op = Department(dep_name='运维部')
dep_fn = Department(dep_id=2, dep_name='财务部')
# print(dep_dev.dep_name)
# print(dep_dev)
# print(dep_dev.dep_id)
# session.add(dep_dev)
# session.add_all([dep_hr, dep_op])
# session.add(dep_fn)
wh = Employee(
    emp_name='王贺',
    gender='male',
    birth_date='1993-1-1',
    phone='17788990022',
    email='wh@163.com',
    dep_id=1
)
lj = Employee(
    emp_name='李俊',
    gender='male',
    birth_date='1995-10-1',
    phone='13355667788',
    email='lijun@163.com',
    dep_id=4
)
zzh = Employee(
    emp_name='赵子浩',
    gender='male',
    birth_date='1999-5-4',
    phone='13556789987',
    email='zzh@qq.com',
    dep_id=4
)
# session.add_all([wh, lj, zzh])
wh20181001 = Salary(emp_id=1, date='2018-10-01', basic=15000, awards=5000)
session.add(wh20181001)
session.commit()
session.close()
