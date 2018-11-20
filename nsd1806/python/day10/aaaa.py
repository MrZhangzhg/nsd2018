import pymysql

conn = pymysql.connect(      # 设置连接数据库的参数
    host='127.0.0.1',
    port=3306,
    user='root',
    passwd='tedu.cn',
    db='nsd1806',
    charset='utf8'
)
cursor = conn.cursor()
create1 = 'CREATE TABLE mytest(name VARCHAR(20))'
cursor.execute(create1)
conn.commit()
cursor.close()
conn.close()
