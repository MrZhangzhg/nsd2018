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
update1 = 'UPDATE departments SET dep_name=%s WHERE dep_name=%s'
data = ('人力资源部', 'HR')
cursor.execute(update1, data)
conn.commit()
cursor.close()
conn.close()









