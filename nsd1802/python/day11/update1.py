from dbconn import Departments, Session

session = Session()

ops = session.query(Departments).filter(Departments.dep_id==2)
ops.update({Departments.dep_name: '运维部'})
dev = session.query(Departments).get(3)  # 返回主键是3的条目
dev.dep_name = '开发部'

session.commit()
session.close()
