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
query1 = 'select * from department'
cursor.execute(query1)
cursor.scroll(1, 'absolute')
data1 = cursor.fetchone()
print(data1)
print('*' * 50)
cursor.scroll(2)  # 不指定移动方式，默认是relative相对
data2 = cursor.fetchone()
print(data2)


