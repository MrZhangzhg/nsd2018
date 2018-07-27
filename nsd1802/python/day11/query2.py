from dbconn import Departments, Employees, Salary, Session
from sqlalchemy import and_, or_

session = Session()
# qset = session.query(Employees.name).\
#     filter(and_(Employees.dep_id==2,Employees.gender=='女'))
# print(qset)
# for name in qset:
#     print(name)
###################################
# qset = session.query(Employees.name).\
#     filter(or_(Employees.dep_id==2, Employees.gender=='女'))
# print(qset)
# for name in qset:
#     print(name)
###################################
# qset = session.query(Employees.name, Employees.phone)
# print(qset.all())  # 返回列表
# print(qset.first())  # 返回满足条件的第一个值
###################################
# qset = session.query(Employees.name, Employees.phone).\
#     filter(Employees.emp_id==1)
# print(qset.one())  # 查询必须只有一项，否则报错
# print(qset.scalar())  # 调用one，返回第一列的值
###################################
# qset = session.query(Employees)
# print(qset.count())
###################################
qset = session.query(Employees.name, Departments.dep_name).\
    join(Departments, Employees.dep_id==Departments.dep_id)
print(qset.all())

session.close()
