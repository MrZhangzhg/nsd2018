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
cursor.scroll(1, mode='absolute')
result = cursor.fetchone()
print(result)
cursor.scroll(1, mode='relative')   # 默认就是相对移动
result = cursor.fetchone()
print(result)
cursor.close()
conn.close()
