#!/usr/bin/env python

from sqlalchemy import create_engine, Column, String, Integer, ForeignKey, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import json

engine = create_engine(
    'sqlite:////var/ftp/nsd2018/nsd1802/python/ansible_project/myansible/db.sqlite3',
    encoding='utf8',
)
Base = declarative_base()
Session = sessionmaker(bind=engine)

class Group(Base):
    __tablename__ = 'webansi_group'

    id = Column(Integer, primary_key=True)
    group = Column(String(50))

    def __str__(self):
        return self.group

class Host(Base):
    __tablename__ = 'webansi_host'

    id = Column(Integer, primary_key=True)
    hostname = Column(String(50))
    ipaddr = Column(String(15))
    group_id = Column(Integer, ForeignKey('webansi_group.id'))

if __name__ == '__main__':
    session = Session()
    qset = session.query(Group.group, Host.ipaddr).\
        join(Host, Group.id==Host.group_id)
    host_list = qset.all()
    result = {}
    for g, h in host_list:
        if g not in result:
            result[g] = {}
            result[g]['hosts'] = []
        result[g]['hosts'].append(h)

    print json.dumps(result)



# {
#     'webservers': { 'hosts': []},
#     'dbservers': { 'hsots': []}
# }
