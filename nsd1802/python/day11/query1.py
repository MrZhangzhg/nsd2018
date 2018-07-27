from dbconn import Departments, Employees, Salary, Session

session = Session()
# qset = session.query(Departments).order_by(Departments.dep_id)
# print(qset)  # qset此时只是一条SQL语句
# for dep in qset:  # 向qset取值时，得到一个个实例
#     print("%s: %s" % (dep.dep_id, dep.dep_name))
#####################################
# qset = session.query(Employees.name, Employees.phone)
# print(qset)
# for name, phone in qset:  # qset执行后返回的是元组
#     print('%s: %s' % (name, phone))
########################################
# qset = session.query(Departments.dep_name.label('部门'))
# print(qset)
# for row in qset:
#     print(row.部门)
########################################
# qset = session.query(Employees.name, Employees.email).\
#     order_by(Employees.emp_id)[3:6]
# print(qset)  # qset因为切片的原因，已经是元组组成的列表了，不再是SQL语句
########################################
# qset = session.query(Employees.name).\
#     filter(Employees.dep_id==2).filter(Employees.gender=='女')
# print(qset)
# for name in qset:
#     print(name)
########################################
# qset = session.query(Employees.name).\
#     filter(Employees.name.like('王%'))
# print(qset)
# for name in qset:
#     print(name)
########################################
# qset = session.query(Employees.name).\
#     filter(Employees.name.in_(['吴伟超', '李通达', '董枝俊']))
# print(qset)
# for name in qset:
#     print(name)
########################################
# qset = session.query(Employees.name).\
#     filter(~Employees.name.in_(['吴伟超', '李通达', '董枝俊']))
# print(qset)
# for name in qset:
#     print(name)
########################################
qset = session.query(Employees.name).\
    filter(Employees.name.isnot(None))
print(qset)
for name in qset:
    print(name)
session.close()


