from dbconn import Departments, Session

session = Session()

q1 = session.query(Departments).filter(Departments.dep_name=='运维部')
dep = q1.one()
# print(dep)
session.delete(dep)
session.commit()
session.close()
