from dbconn import Salary, Session

jan2018_1 = Salary(
    date='2018-01-10',
    emp_id=1,
    basic=10000,
    awards=2000
)
jan2018_2 = Salary(
    date='2018-01-10',
    emp_id=2,
    basic=11000,
    awards=1500
)
jan2018_3 = Salary(
    date='2018-01-10',
    emp_id=3,
    basic=11000,
    awards=2200
)
jan2018_4 = Salary(
    date='2018-01-10',
    emp_id=4,
    basic=11000,
    awards=3000
)
jan2018_5 = Salary(
    date='2018-01-10',
    emp_id=1,
    basic=13000,
    awards=2000
)
jan2018_6 = Salary(
    date='2018-01-10',
    emp_id=6,
    basic=15000,
    awards=3000
)
jan2018_7 = Salary(
    date='2018-01-10',
    emp_id=7,
    basic=9000,
    awards=3000
)
jan2018_8 = Salary(
    date='2018-01-10',
    emp_id=8,
    basic=13000,
    awards=2000
)
jan2018_9 = Salary(
    date='2018-01-10',
    emp_id=9,
    basic=13000,
    awards=1500
)
session = Session()
sals = [jan2018_1, jan2018_2, jan2018_3,jan2018_4, jan2018_5, jan2018_6, jan2018_7, jan2018_8, jan2018_9]
session.add_all(sals)
session.commit()
session.close()
