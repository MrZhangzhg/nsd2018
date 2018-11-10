#!/opt/djenv/bin/python

from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    'sqlite:////var/ftp/nsd2018/nsd1805/python/ansible_project/myansible/db.sqlite3',
    encoding='utf8',
)
Base = declarative_base()
Session = sessionmaker(bind=engine)

class HostGroup(Base):
    __tablename__ = 'webansi_hostgroup'
    id = Column(Integer, primary_key=True)
    hostgroup = Column(String(20), unique=True, nullable=False)

    def __str__(self):
        return self.hostgroup

class Host(Base):
    __tablename__ = 'webansi_host'
    id = Column(Integer, primary_key=True)
    hostname = Column(String(50), unique=True, nullable=False)
    ipaddr = Column(String(15), unique=True, nullable=False)
    group_id = Column(Integer, ForeignKey('webansi_hostgroup.id'))

    def __str__(self):
        return "[%s: %s]" % (self.hostname, self.ipaddr)

if __name__ == '__main__':
    
