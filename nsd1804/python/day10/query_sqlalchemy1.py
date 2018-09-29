from dbconn import Session, Department, Employee

session = Session()
query1 = session.query(Department)
print(query1)  # 只是一条查询语句
for instance in query1:
    print(instance)  # 取出的是每个部门的实例
dep = query1[0]  # 取出第一个实例
print(dep)  # 打印实例
print(dep.dep_id, dep.dep_name)  # 打印实例的指定属性

print('#' * 40)
query2 = session.query(Department).order_by(Department.dep_id)
print(query2)
for instance in query2:
    print(instance)
print('#' * 40)

query3 = session.query(Employee.emp_name, Employee.phone)
print(query3)  # 只是一条查询语句
print(list(query3))  # query3取值时，返回的是元组，不是列表
for name, phone in query3:
    print('%s: %s' % (name, phone))
print('#' * 40)

query4 = session.query(Department.dep_name.label('部门'))
print(query4)
for dep in query4:
    print(dep.部门)
print('#' * 40)

query5 = session.query(Department).order_by(Department.dep_id)[2:5]
print(query5)  # 不是SQL语句，因为切片需要值，所以查询的是实例列表
for dep in query5:
    print(dep)
print('#' * 40)

query6 = session.query(Department).filter(Department.dep_id == 2)
print(query6)  # 返回SQL语句
for dep in query6:  # 即使过滤的结果只有一项，也会放到列表中
    print(dep)
print('#' * 40)

query7 = session.query(Department).filter(Department.dep_id>2)\
    .filter(Department.dep_id<4)  # 多次filter就是where...and...
print(query7)
for dep in query7:
    print(dep)
print('#' * 40)

query8 = session.query(Department).filter(Department.dep_id!=2)
print(query8)  # 返回SQL语句
for dep in query8:  # 即使过滤的结果只有一项，也会放到列表中
    print(dep)
print('#' * 40)

query9 = session.query(Department).filter(Department.dep_name.like('%部'))
print(query9)    # like与mysql查询一样，%表示0到多个字符
for dep in query9:
    print(dep)
print('#' * 40)

query10 = session.query(Department).filter(Department.dep_id.in_([1,3,4]))
print(query10)
for dep in query10:
    print(dep)
print('#' * 40)

query11 = session.query(Department).filter(~Department.dep_id.in_([1,3,4]))
print(query11)  # ~表示取反
for dep in query11:
    print(dep)
print('#' * 40)

query12 = session.query(Department).filter(Department.dep_name.is_(None))
print(query12)
for dep in query12:
    print(dep)
print('#' * 40)

query13 = session.query(Department).filter(Department.dep_name.isnot(None))
print(query13)
for dep in query13:
    print(dep)
print('#' * 40)

from sqlalchemy import and_, or_
query14 = session.query(Department)\
    .filter(and_(Department.dep_id>2, Department.dep_id<4))
print(query14)
for dep in query14:
    print(dep)
print('#' * 40)

query15 = session.query(Department)\
    .filter(or_(Department.dep_id<2, Department.dep_id>3))
print(query15)
for dep in query15:
    print(dep)
