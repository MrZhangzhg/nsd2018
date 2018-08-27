from dbconn import Session, Salary

aug2018 = Salary(date='2018-8-10', emp_id=1, basic=10000, awards=2000)
session= Session()
session.add(aug2018)
session.commit()
session.close()

