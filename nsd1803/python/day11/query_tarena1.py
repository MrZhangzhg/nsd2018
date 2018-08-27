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

###################################################
qset6 = session.query(Departments.dep_id).\
    filter(Departments.dep_name.in_(['运维部', '开发部']))
print(qset6)  # 查询两个部门的ID号
for did in qset6:
    print(did)
###################################################
qset7 = session.query(Departments.dep_id).\
    filter(~Departments.dep_name.in_(['运维部', '开发部']))
print(qset7)  # 查询名字不是这两个部门的ID
for did in qset7:
    print(did)
###################################################
from sqlalchemy import and_, or_
from dbconn import Employees

qset8 = session.query(Employees).\
    filter(and_(Employees.gender=='male', Employees.dep_id==3))
print(qset8)
for emp in qset8:
    print(emp.emp_name)
###################################################
qset9 = session.query(Employees).\
    filter(or_(Employees.gender=='female', Employees.dep_id==3))
print(qset9)
for emp in qset9:
    print(emp.emp_name)

###################################################
qset10 = session.query(Departments).order_by(Departments.dep_id)
print(qset10.all())  # 返回所有查到的结果，组成列表
print(qset10.first())  # 只返回查询到的第一个结果
# print(qset10.one())  # 报错，one要求返回的结果只有一个
qset11 = session.query(Departments.dep_id, Departments.dep_name).\
    filter(Departments.dep_id==1)
print(qset11.one())
print(qset11.scalar())  # 调用one()，返回第一列
###################################################
# 统计一共有几个部门
qset12 = session.query(Departments).count()
print(qset12)
###################################################
# 得到每个员工在哪个部门，部门使用名字，不用ID
qset13 = session.query(Employees.emp_name, Departments.dep_name).\
    join(Departments, Employees.dep_id==Departments.dep_id)
print(qset13.all())
# 注意query()中先写Employees.emp_name，join()中就要先用Departments
###################################################
###################################################
# 第一种修改记录的方法，通过查询语句的update方法
hr = session.query(Departments).filter(Departments.dep_name=='hr')
print(hr)
hr.update({'dep_name': '人力资源部'})
session.commit()
session.close()
###################################################
hr = session.query(Departments).get(1)  # 获取主键是1的实例
print(hr)
hr.dep_name = '人事部'
session.commit()
session.close()
###################################################
# 删除ID号为5的员工记录
tom = session.query(Employees).get(5)
session.delete(tom)
session.commit()
session.close()
