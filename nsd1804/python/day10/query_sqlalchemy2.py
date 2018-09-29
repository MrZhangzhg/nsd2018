from dbconn import Session, Department, Employee

session = Session()
query1 = session.query(Department)
print(query1.all())  # 返回列表
print(query1.first())  # 返回匹配条件的第一个记录
query2 = session.query(Department.dep_name, Department.dep_id)\
    .filter(Department.dep_id==2)
print(query2.one())  # one要求查询只有一项，如果有多项则报错
print(query2.scalar())  # 调用one，返回one结果中的第一个字段

query3 = session.query(Department).count()
print(query3)

query4 = session.query(Employee.emp_name, Department.dep_name)\
    .join(Department, Employee.dep_id==Department.dep_id)
# 注意：query先写Employee.emp_name，join就要先写Department
# query先写Department.dep_name，join就要先写Employee
print(query4)
for name, dep_name in query4:
    print('%s: %s' % (name, dep_name))

