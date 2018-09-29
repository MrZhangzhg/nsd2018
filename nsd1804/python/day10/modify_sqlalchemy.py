from dbconn import Session, Department

session = Session()

# query1 = session.query(Department)\
#     .filter(Department.dep_name=='development')
# query1.update({'dep_name': '开发部'})
# query2 = session.query(Department).filter(Department.dep_name=='人事部')
# dep_hr = query2.one()
# dep_hr.dep_name = '人力资源部'
dep_fn = session.query(Department).get(2)
print(dep_fn)
session.delete(dep_fn)
session.commit()
session.close()
