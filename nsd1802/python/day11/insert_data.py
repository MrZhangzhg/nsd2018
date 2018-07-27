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
result = cursor.execute(insert1, (1, '人事部'))
conn.commit()
cursor.close()
conn.close()
