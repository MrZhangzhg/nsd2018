import pymysql

conn = pymysql.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='tedu.cn',
    db='tedu',
    charset='utf8'
)  # 创建到数据库的连接

cursor = conn.cursor()  # 创建游标，相当于打开文件返回文件对象
insert_dep1 = 'UPDATE departments SET dep_name=%s WHERE dep_name=%s'
cursor.execute(insert_dep1, ('人力资源部', '人事部'))
delete1 = 'DELETE FROM departments WHERE dep_name=%s'
cursor.execute(delete1, ('测试部',))
conn.commit()  # 增删改都需要commit
cursor.close()
conn.close()
