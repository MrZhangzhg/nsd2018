import pymysql

conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='tedu.cn',
    db='tarena1804',
    charset='utf8'
)
cursor = conn.cursor()  # 创建游标用于操作数据库
insert1 = 'INSERT INTO department VALUES (%s, %s)'
result1 = cursor.execute(insert1, (1, 'development'))
depts1 = [(2, 'operations'), (3, 'QA')]
depts2 = [(4, '人事部'), (5, '财务部')]
result2 = cursor.executemany(insert1, depts1)
result3 = cursor.executemany(insert1, depts2)

conn.commit()
cursor.close()
conn.close()
