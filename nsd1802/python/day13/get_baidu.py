import requests

r = requests.get('http://www.baidu.com')
r.encoding = 'utf8'

# r.text     # 返回字符格式，适用于文本
# r.content  # 返回字节形式，适合二进制数据，如图片
# r.json()   # 返回json格式，适用于各种数据对象

with open('/tmp/bbdd.html', 'w') as fobj:
    fobj.write(r.text)
