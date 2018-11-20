from dbconn import Departments, Session

session = Session()

q1 = session.query(Departments).filter(Departments.dep_name=='人事部')
dep = q1.one()
print(dep)
dep.dep_name = '人力资源部'
session.commit()
session.close()

