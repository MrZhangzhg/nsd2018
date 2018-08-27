from dbconn import Session, Departments

hr = Departments(dep_name='hr')
print(hr.dep_id)    # 此时还没有在数据库中创建记录，所以是None
print(hr.dep_name)

session = Session()  # 建立到数据库的会话连接
session.add(hr)      # 真正向数据库写入记录
session.commit()
print(hr.dep_id)
session.close()
