import pymysql

conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='tedu.cn',
    db='tedu',
    charset='utf8'
)
cursor = conn.cursor()

query1 = 'SELECT * FROM departments'
cursor.execute(query1)
r1 = cursor.fetchone()
print(r1)
print('#' * 20)
r2 = cursor.fetchmany(2)
print(r2)
print('#' * 20)
r3 = cursor.fetchall()
print(r3)

cursor.close()
conn.close()
