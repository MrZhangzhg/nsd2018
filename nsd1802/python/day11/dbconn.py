from sqlalchemy import create_engine, Column, String, Integer, ForeignKey, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# 创建连接到数据库的引擎
engine = create_engine(
    'mysql+pymysql://root:tedu.cn@localhost/tarena?charset=utf8',
    encoding='utf8',
    # echo=True
)
Base = declarative_base()  # 生成ORM映射所需的基类
Session = sessionmaker(bind=engine)

class Departments(Base):  # 必须继承于Base
    __tablename__ = 'departments'  # 库中的表名
    # 每个属性都是表中的一个字段，是类属性
    dep_id = Column(Integer, primary_key=True)
    dep_name = Column(String(20), nullable=False, unique=True)

    def __str__(self):
        return '[部门ID：%s, 部门名称：%s]' % (self.dep_id, self.dep_name)

class Employees(Base):
    __tablename__ = 'employees'
    emp_id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    gender = Column(String(6))
    phone = Column(String(11))
    email = Column(String(50))
    dep_id = Column(Integer, ForeignKey('departments.dep_id'))

    def __str__(self):
        return '员工：%s' % self.name

class Salary(Base):
    __tablename__ = 'salary'
    auto_id = Column(Integer, primary_key=True)
    date = Column(Date)
    emp_id = Column(Integer, ForeignKey('employees.emp_id'))
    basic = Column(Integer)
    awards = Column(Integer)


if __name__ == '__main__':
    # 在数据库中创建表，如果库中已有同名的表，将不会创建
    Base.metadata.create_all(engine)

