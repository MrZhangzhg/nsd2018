from dbconn import Departments, Session, Salary

session = Session()

qset1 = session.query(Departments).order_by(Departments.dep_id)
print(qset1)  # qset1仅仅是一条SQL语句

for dep in qset1:  # 使用qset的时候，dep是一个个的实例
    print(dep)

for dep in qset1:
    print('%s: %s' % (dep.dep_id, dep.dep_name))

########################################################
qset2 = session.query(Departments.dep_id, Departments.dep_name)
print(qset2)

for did, dname in qset2:
    print(did, dname)

########################################################
qset3 = session.query(Departments)[1:3]  # 返回的不是SQL语句
print(qset3)
for dep in qset3:
    print(dep.dep_name)
########################################################
qset4 = session.query(Departments.dep_name).\
    filter(Departments.dep_id==2)
print(qset4)
for dep in qset4:
    print(dep.dep_name)

#############################################
qset5 = session.query(
    Salary.date, Salary.emp_id, Salary.basic + Salary.awards
)
print(qset5)
for date, emp_id, sal in qset5:
    print('%s: %s: %s' % (date, emp_id, sal))
