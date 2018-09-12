#!/usr/bin/env python

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import sessionmaker
import json

engine = create_engine(
    'sqlite:////var/ftp/nsd2018/nsd1803/python/ansible_project/myansible/db.sqlite3',
    encoding='utf8'
)
Base = declarative_base()
Session = sessionmaker(bind=engine)

class Group(Base):
    __tablename__ = 'webansi_group'
    id = Column(Integer, primary_key=True)
    hostgroup = Column(String(50))

    def __str__(self):
        return self.hostgroup

class Host(Base):
    __tablename__ = 'webansi_host'
    id = Column(Integer, primary_key=True)
    hostname = Column(String(50))
    ipaddr = Column(String(15))
    group_id = Column(Integer, ForeignKey('webansi_group.id'))

if __name__ == '__main__':
    session = Session()
    qset = session.query(Group.hostgroup, Host.ipaddr).\
        join(Host, Group.id==Host.group_id)
    hosts = qset.all()
    result = {}
    # [(u'webservers', u'192.168.4.2'), (u'webservers', u'192.168.4.3')]
    for group, ip in hosts:
        if group not in result:
            result[group] = {'hosts': []}
        result[group]['hosts'].append(ip)
    print(json.dumps(result))
