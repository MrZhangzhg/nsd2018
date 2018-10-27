from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine(
    'mysql+pymysql://root:tedu.cn@localhost/tarena1805',
    encoding='utf8',
    echo=True
)
Base = declarative_base()

class Departments(Base):
    __tablename__ = 'departments'  # 声明与数据库的哪张表对应
    dep_id = Column(Integer, primary_key=True)
    dep_name = Column(String(20), nullable=False, unique=True)

    def __str__(self):
        return "<部门：%s>" % self.dep_name

if __name__ == '__main__':
    # 如果数据库中没有对应的表，则创建，有的话与之建立对应
    Base.metadata.create_all(engine)
