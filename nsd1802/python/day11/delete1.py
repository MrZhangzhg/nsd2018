from dbconn import Departments, Session

session = Session()

# xz = Departments(dep_id=5, dep_name='行政部')
# session.add(xz)
xz = session.query(Departments).get(5)
session.delete(xz)

session.commit()
session.close()


