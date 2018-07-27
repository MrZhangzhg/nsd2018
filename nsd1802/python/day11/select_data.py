import pymysql

conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='tedu.cn',
    db='tedu',
    charset='utf8'
)

cursor = conn.cursor()  # 创建游标

select1 = "select * from departments"
cursor.execute(select1)
result = cursor.fetchone()
print(result)
print('-' * 30)
result = cursor.fetchmany(2)
print(result)
print('-' * 30)
result = cursor.fetchall()
print(result)

cursor.close()
conn.close()