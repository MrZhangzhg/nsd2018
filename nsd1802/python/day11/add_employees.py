from dbconn import Employees, Session

wj = Employees(
    emp_id=1,
    name='王俊',
    gender='男',
    phone='15678789090',
    email='wj@163.com',
    dep_id=3
)
wwc = Employees(
    emp_id=2,
    name='吴伟超',
    gender='男',
    phone='13499887755',
    email='wwc@qq.com',
    dep_id=3
)
dzj = Employees(
    emp_id=3, name='董枝俊', gender='男', phone='18900998877', email='dzj@163.com', dep_id=3
)
ltd = Employees(emp_id=4, name='李通达', gender='男', phone='13378904567', email='ltd@163.com', dep_id=2)
wxy = Employees(emp_id=5, name='王秀燕', gender='女', phone='15098765432', email='wxy@tedu.cn', dep_id=2)
gq = Employees(emp_id=6, name='高琦', gender='女', phone='15876543212', email='gq@tarena.com', dep_id=1)
wzf = Employees(emp_id=7, name='王召飞', gender='男', phone='15609871234', email='wzf@sohu.com', dep_id=1)
sy = Employees(emp_id=8, name='孙燕', gender='女', phone='18567895435', email='sy@163.com', dep_id=4)
gpf = Employees(emp_id=9, name='高鹏飞', gender='男', phone='13566889900', email='gpf@163.com', dep_id=2)
emps = [wj, wwc, dzj, ltd, wxy, gq, wzf, sy, gpf]
session = Session()
session.add_all(emps)
session.commit()
session.close()
