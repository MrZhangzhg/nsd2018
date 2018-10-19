#!/opt/djenv/bin/python

import json
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine(
    'sqlite:////var/ftp/nsd2018/nsd1804/python/ansible_project/myansible/db.sqlite3',
    encoding='utf8',
)
Base = declarative_base()
Session = sessionmaker(bind=engine)

class HostGroup(Base):
    __tablename__ = 'webansi_hostgroup'
    id = Column(Integer, primary_key=True)
    group_name = Column(String(30), unique=True)

    def __str__(self):
        return self.group_name

class Host(Base):
    __tablename__ = 'webansi_host'
    id = Column(Integer, primary_key=True)
    hostname = Column(String(50), unique=True)
    ipaddr = Column(String(15))
    hostgroup_id = Column(Integer, ForeignKey('webansi_hostgroup.id'))

    def __str__(self):
        return "<%s: %s>" % (self.hostname, self.ipaddr)

if __name__ == '__main__':
    session = Session()
    groups = session.query(HostGroup.group_name, Host.ipaddr)\
             .join(Host, HostGroup.id==Host.hostgroup_id)
    result = {}
    for group, host in groups.all():
        if group not in result:
            result[group] = {}
            result[group]["hosts"] = [host]
            # result['webservers'] = {}
            # result['webservers']['hosts'] = ['192.168.4.3']
        else:
            result[group]["hosts"].append(host)

    print(json.dumps(result))
