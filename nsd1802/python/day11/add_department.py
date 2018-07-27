from dbconn import Departments, Session

hr = Departments(dep_id=1, dep_name='hr')
ops = Departments(dep_id=2, dep_name='operations')
dev = Departments(dep_id=3, dep_name='development')
finance = Departments(dep_id=4, dep_name='财务部')
deps = [ops, dev]
# print(hr.dep_name)
# print(hr.dep_id)
session = Session()
session.add(hr)
session.add_all(deps)
session.add(finance)
session.commit()
session.close()

