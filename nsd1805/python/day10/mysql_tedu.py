import pymysql

conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='tedu.cn',
    db='tedu1805',
    charset='utf8'
)
cursor = conn.cursor()

insert1 = 'INSERT INTO departments(dep_id, dep_name) VALUES (%s, %s)'
# result1 = cursor.execute(insert1, (1, '人事部'))
# result2 = cursor.executemany(insert1, [(2, '运维部'), (3, '开发部')])
# result3 = cursor.executemany(insert1, [(4, '财务部'), (5, '市场部'), (6, '销售部')])
#############################################
# query1 = "SELECT * FROM departments"
# result4 = cursor.execute(query1)
# print(cursor.fetchone())
# print('-' * 30)
# print(cursor.fetchmany(2))
# print('-' * 30)
# print(cursor.fetchall())
#############################################
# query1 = "SELECT * FROM departments"
# result4 = cursor.execute(query1)
# print(cursor.fetchone())
# print('-' * 30)
# cursor.scroll(0, mode='absolute')  # 移回开头
# print(cursor.fetchone())
# print('-' * 30)
# cursor.scroll(2)  # mode默认是relative相对
# print(cursor.fetchone())
#############################################
# update1 = 'UPDATE departments SET dep_name=%s WHERE dep_name=%s'
# result5 = cursor.execute(update1, ('人力资源部', '人事部'))
# print(result5)  # 返回值是1，表示影响一行记录
#############################################
delete1 = 'DELETE FROM departments WHERE dep_id=%s'
result6 = cursor.execute(delete1, (5,))



conn.commit()  # 如果不确认，数据库表不会真正插入数据
cursor.close()
conn.close()

