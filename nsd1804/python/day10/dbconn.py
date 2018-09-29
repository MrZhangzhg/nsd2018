from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    'mysql+pymysql://root:tedu.cn@127.0.0.1/tedu1804',
    encoding='utf8',
    echo=True  # 屏幕输出日志信息
)
Base = declarative_base()  # 生成ORM映射的基类
Session = sessionmaker(bind=engine)  # 创建会话类，用于连接数据库

class Department(Base):
    __tablename__ = 'department'   # 对应到数据库中的表名
    dep_id = Column(Integer, primary_key=True)
    dep_name = Column(String(20), unique=True, nullable=False)

if __name__ == '__main__':
    # 在数据库中创建表，如果表已存在则忽略
    Base.metadata.create_all(engine)
