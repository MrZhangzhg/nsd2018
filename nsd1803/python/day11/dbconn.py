"MariaDB [(none)]> CREATE DATABASE tarena DEFAULT CHARSET='utf8';"

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    'mysql+pymysql://root:tedu.cn@localhost/tarena?charset=utf8',
    encoding='utf8'
    # echo=True
)
# mysql+pymysql://用户名:密码@主机/库名
Base = declarative_base()  # 创建ORM所需要的基类
Session = sessionmaker(bind=engine)

class Departments(Base):
    __tablename__ = 'departments'  # 库中表名
    dep_id = Column(Integer, primary_key=True)  # dep_id是表中字段
    dep_name = Column(String(20), unique=True)  # dep_name是字段

    def __str__(self):
        return '[%s: %s]' % (self.dep_id, self.dep_name)

class Employees(Base):
    __tablename__ = 'employees'

    emp_id = Column(Integer, primary_key=True)
    emp_name = Column(String(20), nullable=False)
    gender = Column(String(6))
    birth_date = Column(Date)
    email = Column(String(50))
    dep_id = Column(Integer, ForeignKey('departments.dep_id'))

    def __str__(self):
        return '[%s: %s]' % (self.emp_id, self.emp_name)

class Salary(Base):
    __tablename__ = 'salary'

    auto_id = Column(Integer, primary_key=True)
    date = Column(Date)
    emp_id = Column(Integer, ForeignKey('employees.emp_id'))
    basic = Column(Integer)
    awards = Column(Integer)

if __name__ == '__main__':
    Base.metadata.create_all(engine)  # 没有时创建，已有不创建
