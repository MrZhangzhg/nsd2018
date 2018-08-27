from dbconn import Session, Departments, Employees

# hr = Departments(dep_name='hr')
# print(hr.dep_id)    # 此时还没有在数据库中创建记录，所以是None
# print(hr.dep_name)
#
# session = Session()  # 建立到数据库的会话连接
# session.add(hr)      # 真正向数据库写入记录

# op = Departments(dep_id=2, dep_name='运维部')
# session = Session()
# session.add(op)

# dev = Departments(dep_id=3, dep_name='开发部')
# qa = Departments(dep_id=4, dep_name='测试部')
# session = Session()
# session.add_all([dev, qa])

bob = Employees(emp_id=1, emp_name='Bob', gender='male', birth_date='1995-08-23', email='bob@tedu.cn', dep_id='1')
john = Employees(emp_id=2, emp_name='John', gender='male', birth_date='1992-06-2', email='john@tedu.cn', dep_id='1')
alice = Employees(emp_id=3, emp_name='Alice', gender='female', birth_date='1997-02-2', email='alice@tedu.cn', dep_id='2')
jane = Employees(emp_id=4, emp_name='Jane', gender='female', birth_date='1988-09-23', email='jane@tedu.cn', dep_id='2')
tom = Employees(emp_id=5, emp_name='Tom', gender='male', birth_date='1994-04-6', email='tom@tedu.cn', dep_id='3')

session = Session()
session.add_all([bob, john, alice, jane, tom])
session.commit()
session.close()
