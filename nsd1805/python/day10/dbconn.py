from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    'mysql+pymysql://root:tedu.cn@localhost/tarena1805?charset=utf8',
    encoding='utf8',
    # echo=True
)
Base = declarative_base()
Session = sessionmaker(bind=engine)


class Departments(Base):
    __tablename__ = 'departments'  # 声明与数据库的哪张表对应
    dep_id = Column(Integer, primary_key=True)
    dep_name = Column(String(20), nullable=False, unique=True)

    def __str__(self):
        return "<部门%s：%s>" % (self.dep_id, self.dep_name)


class Employees(Base):
    __tablename__ = 'employees'
    emp_id = Column(Integer, primary_key=True)
    name = Column(String(20))
    gender = Column(String(6))
    birth_date = Column(Date)
    phone = Column(String(11))
    email = Column(String(50))
    dep_id = Column(Integer, ForeignKey('departments.dep_id'))

    def __str__(self):
        return "<员工：%s>" % self.name


class Salary(Base):
    __tablename__ = 'salary'
    auto_id = Column(Integer, primary_key=True)
    date = Column(Date)
    emp_id = Column(Integer, ForeignKey('employees.emp_id'))
    basic = Column(Integer)
    awards = Column(Integer)


if __name__ == '__main__':
    # 如果数据库中没有对应的表，则创建，有的话与之建立对应
    Base.metadata.create_all(engine)
