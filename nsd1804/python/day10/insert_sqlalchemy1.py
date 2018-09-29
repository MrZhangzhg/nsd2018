from dbconn import Department, Session

session = Session()
dep_dev = Department(dep_name='development')
# print(dep_dev.dep_name)
# print(dep_dev.dep_id)
session.add(dep_dev)
session.commit()
session.close()
