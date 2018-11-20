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
insert1 = 'INSERT INTO departments VALUES (%s, %s)'
hr = (1, 'HR')
deps = [(2, '运维部'), (3, '开发部'), (4, '财务部')]
cursor.execute(insert1, hr)   # 插入单条记录
cursor.executemany(insert1, deps)    # 插入多行记录
conn.commit()   # 增删改都要确认
cursor.close()  # 关闭游标
conn.close()    # 关闭连接
