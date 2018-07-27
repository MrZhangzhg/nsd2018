from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


# 创建连接到数据库的引擎
engine = create_engine(
    'mysql+pymysql://root:tedu.cn@localhost/tarena?charset=utf8',
    encoding='utf8',
    echo=True
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

if __name__ == '__main__':
    # 在数据库中创建表，如果库中已有同名的表，将不会创建
    Base.metadata.create_all(engine)

