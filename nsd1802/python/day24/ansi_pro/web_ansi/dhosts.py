#!/usr/bin/env python

import json
from sqlalchemy import create_engine
from sqlalchemy import Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

#engine = create_engine('sqlite:///../db.sqlite3')
engine = create_engine('sqlite:////root/ansi_pro/db.sqlite3')
Base = declarative_base()
Session = sessionmaker(bind=engine)
session = Session()

class Hosts(Base):

    __tablename__ = "web_ansi_hosts"

    id = Column(Integer, primary_key=True)
    host = Column(String(20))
    group = Column(String(20))

if __name__ == '__main__':
    qset = session.query(Hosts.host, Hosts.group).all()
    host_list = {}
    for host, group in qset:
        if group not in host_list:
            host_list[group] = {}
            host_list[group]["hosts"] = [host]
        else:
            host_list[group]["hosts"].append(host)
    print json.dumps(host_list)
