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
insert1 = "INSERT INTO departments(dep_id, dep_name) VALUES(%s, %s)"
data = [(2, '运维部'), (3, '开发部')]
cursor.executemany(insert1, data)
conn.commit()
cursor.close()
conn.close()
