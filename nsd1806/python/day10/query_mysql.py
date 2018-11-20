import pymysql

conn = pymysql.connect(      # 设置连接数据库的参数
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='tedu.cn',
    db='nsd1806',
    charset='utf8'
)
cursor = conn.cursor()  # 创建游标，可以理解为指向某一位置的数据库指针
query1 = 'SELECT * FROM departments ORDER BY dep_id'
cursor.execute(query1)
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

