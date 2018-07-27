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
cursor.scroll(2)  # 默认相对当前位置移动
print(cursor.fetchall())
print('-' * 30)
cursor.scroll(0, mode='absolute')
print(cursor.fetchall())

cursor.close()
conn.close()