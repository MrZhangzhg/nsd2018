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
insert_dep1 = 'INSERT INTO departments VALUES(%s, %s)'
# cursor.execute(insert_dep1, ('1', '人事部'))
insert_deps = [(2, '运维部'), (3, '开发部'), (4, '测试部')]
cursor.executemany(insert_dep1, insert_deps)
conn.commit()  # 增删改都需要commit
cursor.close()
conn.close()
