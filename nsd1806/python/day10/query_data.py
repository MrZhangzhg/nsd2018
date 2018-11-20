from dbconn import Departments, Session, Employees

session = Session()

# query1 = session.query(Departments)  # 只是SQL语句
# print(query1)
# for dep in query1:    # 当取数据时，才会真正查询数据库
#     print(dep)   # 打印出部门类的每个实例
#     print('%s -> %s' % (dep.dep_id, dep.dep_name))
#########################################################
#
# query2 = session.query(Departments.dep_id, Departments.dep_name)
# print(query2)  # 只是SQL语句
# for dep in query2:   # 查询的结果是元组组成的列表
#     print(dep)
# for dep_id, dep_name in query2:
#     print('%s -> %s' % (dep_id, dep_name))
#########################################################
#
# query3 = session.query(Departments.dep_name.label('部门'))
# print(query3)
# for dep in query3:
#     print(dep.部门)
#########################################################
#
# query4 = session.query(Departments).order_by(Departments.dep_id)
# print(query4)
# for dep in query4:
#     print(dep)
#     print('%s -> %s' % (dep.dep_id, dep.dep_name))
#########################################################
#
# query5 = session.query(Departments).order_by(Departments.dep_id)[1:3]
# print(query5)   # 因为取切片了，所以query4不是SQL语句
# for dep in query5:
#     print(dep)
#     print('%s -> %s' % (dep.dep_id, dep.dep_name))
#########################################################
#
# query6 = session.query(Departments).filter(Departments.dep_id==3)
# print(query6)  # SQL语句
# for dep in query6:
#     print(dep.dep_id, dep.dep_name)
#########################################################
#
# query7 = session.query(Departments).filter(Departments.dep_id>=2)\
#     .filter(Departments.dep_id<=4)
# print(query7)
#########################################################
#
# query8 = session.query(Departments)\
#     .filter(Departments.dep_name.in_(['人事部', '财务部']))
# for dep in query8:
#     print(dep.dep_id, dep.dep_name)
#########################################################
#
# query9 = session.query(Departments)\
#     .filter(~Departments.dep_name.in_(['人事部', '财务部']))
# for dep in query9:
#     print(dep.dep_id, dep.dep_name)
#########################################################
#
# from sqlalchemy import and_, or_
#
# query10 = session.query(Departments)\
#     .filter(and_(Departments.dep_id>=2, Departments.dep_id<=4))
# query11 = session.query(Departments)\
#     .filter(or_(Departments.dep_id==2, Departments.dep_id==4))
# for dep in query10:
#     print(dep.dep_id, dep.dep_name)
# print('-' * 30)
# for dep in query11:
#     print(dep.dep_id, dep.dep_name)
#########################################################
#
# query12 = session.query(Departments)
# print(query12)
# print('-' * 30)
# print(query12.all())   # all返回全部数据
# print('-' * 30)
# print(query12.first())   # 返回第一条记录
# query13 = session.query(Departments.dep_id, Departments.dep_name)\
#     .filter(Departments.dep_id>4)
# print(query13.one())   # one必须只有一条记录，否则抛出异常
# print(query13.scalar())   # 返回one的第一个记录
#########################################################
#
# query14 = session.query(Departments)
# print(query14.count())
#########################################################
#
# zmg = Employees(
#     emp_id=20,
#     emp_name='赵明钢',
#     gender='男',
#     birth_date='1998-10-8',
#     phone='13355667788',
#     email='zmg@163.com',
#     dep_id=2
# )
# zjh = Employees(
#     emp_id=25,
#     emp_name='张佳豪',
#     gender='男',
#     birth_date='1996-6-18',
#     phone='13455627798',
#     email='zjh@qq.com',
#     dep_id=5
# )
# session.add_all([zmg, zjh])
# session.commit()
#########################################################
# query括号中先写Employees.emp_name，join的括号中就要写Departments
# query括号中先写Departments.dep_name，join的括号中就要写Employees
query15 = session.query(Employees.emp_name, Departments.dep_name)\
    .join(Departments, Employees.dep_id==Departments.dep_id)
print(query15.all())


