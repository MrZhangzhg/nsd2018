from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    # mysql+pymysql://用户:密码@服务器/数据库?参数
    'mysql+pymysql://root:tedu.cn@localhost/tedu1806?charset=utf8',
    encoding='utf8',
    # echo=True   # 开启日志输出，生产环境设置为False
)
Session = sessionmaker(bind=engine)
Base = declarative_base()   # 生成ORM类的基类

class Departments(Base):
    __tablename__ = 'departments'   # 表名
    dep_id = Column(Integer, primary_key=True)
    dep_name = Column(String(20), unique=True, nullable=False)

    def __str__(self):
        return "<部门：%s>" % self.dep_name

class Employees(Base):
    __tablename__ = 'employees'
    emp_id = Column(Integer, primary_key=True)
    emp_name = Column(String(20), nullable=False)
    gender = Column(String(6))
    birth_date = Column(Date)
    phone = Column(String(11))
    email = Column(String(50))
    dep_id = Column(Integer, ForeignKey('departments.dep_id'))

    def __str__(self):
        return '<员工：%s>' % self.emp_name

class Salary(Base):
    __tablename__ = 'salary'
    auto_id = Column(Integer, primary_key=True)
    salary_date = Column(Date)
    emp_id = Column(Integer, ForeignKey('employees.emp_id'))
    basic = Column(Integer)
    awards = Column(Integer)

if __name__ == '__main__':
    # 如果库中不存在表则创建，已存在不会重复创建
    Base.metadata.create_all(engine)
