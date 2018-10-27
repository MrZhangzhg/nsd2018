from dbconn import Employees, Departments, Session

session = Session()
# query1 = session.query(Departments)
# print(query1)  # query1只是个sql语句，不真正连接数据库，只有取数据时才连接
# for dep in query1:
#     print(dep)  # 返回的是Departments的实例
#     print(dep.dep_id, dep.dep_name)
#     print('-' * 30)
##########################################
# query2 = session.query(Employees.name, Employees.phone)
# print(query2)
# for item in query2:
#     print(item)  # 因为只查询一部分属性，所以返回值是属性构成的元组
# for name, phone in query2:
#     print('%s: %s' % (name, phone))
##########################################
# query3 = session.query(Departments.dep_name.label('部门'))
# print(query3)
# for dep in query3:
#     print(dep.部门)
##########################################
# query4 = session.query(Departments).order_by(Departments.dep_id)
# print(query4)
# for dep in query4:
#     print(dep)
##########################################
# query5 = session.query(Employees)[2:4]
# print(query5)  # query5是由实例构成的列表，因取切片时，需要到数据库中取出数据
##########################################
# query6 = session.query(Departments).filter(Departments.dep_id==2)
# print(query6)
# for dep in query6:
#     print(dep)
##########################################
# query7 = session.query(Employees).filter(Employees.emp_id>1)\
#     .filter(Employees.emp_id<4)
# print(query7)
# for emp in query7:
#     print(emp)
##########################################
# query8 = session.query(Departments)\
#     .filter(Departments.dep_name.in_(['人事部', '运维部']))
# print(query8)
# for dep in query8:
#     print(dep.dep_id, dep.dep_name)
##########################################
# query9 = session.query(Departments)\
#     .filter(~Departments.dep_name.in_(['人事部', '运维部']))
# print(query9)
# for dep in query9:
#     print(dep.dep_id, dep.dep_name)
##########################################
# from sqlalchemy import and_, or_
# query10 = session.query(Employees)\
#     .filter(and_(Employees.emp_id>1, Employees.emp_id<4))
# print(query10)
# query11 = session.query(Employees)\
#     .filter(or_(Employees.emp_id==1, Employees.gender=='女'))
# print(query11)
##########################################
# from sqlalchemy import and_, or_
# query11 = session.query(Employees)\
#     .filter(or_(Employees.emp_id==1, Employees.gender=='女'))
# result = query11.all()  # all取出全部结果
# print(result)
# result1 = query11.first()  # first取出查询集中的第一个结果
# print(result1)
# result2 = query11.one()  # 报错，因为one要求只能得到一个结果
##########################################
# query12 = session.query(Departments).count()
# print(query12)  # 相当于select count(*) from departments;
##########################################
# query先写的是Employees.name，join时就要用Departments
# 如果query先写join时就要用Departments.dep_name，join时就要用query先写的是Employees
# query13 = session.query(Employees.name, Departments.dep_name)\
#     .join(Departments, Employees.dep_id==Departments.dep_id)
# print(query13)
# for name, dep in query13:
#     print(name, dep)
##########################################
# dep = session.query(Departments).get(1)  # 取出主键是1的部门
# dep.dep_name = '人力资源部'
# session.commit()
##########################################
emp = session.query(Employees).get(1)
session.delete(emp)
session.commit()

