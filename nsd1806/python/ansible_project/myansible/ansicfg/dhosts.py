#!/opt/djenv/bin/python

import json
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    'sqlite:////var/ftp/nsd2018/nsd1806/python/ansible_project/myansible/db.sqlite3',
    encoding='utf8',
)
Session = sessionmaker(bind=engine)
Base = declarative_base()

class HostGroup(Base):
    __tablename__ = 'webansi_hostgroup'
    id = Column(Integer, primary_key=True)
    groupname = Column(String(50), unique=True)

    def __str__(self):
        return self.groupname

class Host(Base):
    __tablename__ = 'webansi_host'
    id = Column(Integer, primary_key=True)
    hostname = Column(String(50), unique=True)
    ipaddr = Column(String(15))
    group_id = Column(Integer, ForeignKey('webansi_hostgroup.id'))

    def __str__(self):
        return "<%s: %s>" % (self.hostname, self.ipaddr)

if __name__ == '__main__':
    result = {}
    session = Session()
    qset = session.query(Host.ipaddr, HostGroup.groupname)\
        .join(HostGroup, HostGroup.id==Host.group_id)
    for ip, group in qset:
        if group not in result:
            result[group] = {}   # {'dbservers': {}}
            result[group]['hosts'] = []  # {'dbservers': {'hosts': []}}
        result[group]['hosts'].append(ip)

    print(json.dumps(result))
