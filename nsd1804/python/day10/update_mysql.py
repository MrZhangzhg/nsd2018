import pymysql

conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='tedu.cn',
    db='tarena1804',
    charset='utf8'
)
cursor = conn.cursor()
update1 = 'update department set dep_name=%s where dep_name=%s'
delete1 = 'delete from department where dep_id=%s'
cursor.execute(update1, ('人力资源部', '人事部',))
cursor.execute(delete1, (5,))
conn.commit()
cursor.close()
conn.close()
