'pip3 install requests'

import requests

# payload = {'wd': 'centos7'}
# r = requests.get('http://www.baidu.com/s', params=payload)
# 相当于访问http://www.baidu.com/s?wd=centos7
#####################################################
# 请求时加上指定的头部信息
header = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'}
r = requests.get('http://127.0.0.1/', headers=header)
#####################################################
# data用于提交表单数据
# data = {'username': 'xxx', 'password': 'yyyyy'}
# r = requests.post('http://login.baidu.com', data=data)
#
#####################################################
# 获得网页信息
r = requests.get('http://www.baidu.com/')
r.text  # 查看页面内容，默认的文字编码是ISO8859-1
r.encoding
r.encoding = 'utf8'
data = r.text
#####################################################
r2 = requests.get('http://i.tq121.com.cn/i/weather2015/index/indexImg_gl.png')
with open('a.png', 'wb') as fobj:
    fobj.write(r2.content)  # content是bytes类型，更适合非文本文件
#####################################################
r3 = requests.get('http://www.weather.com.cn/data/sk/101010100.html')
r3.encoding = 'utf8'
r3.json()  # 自带json解码











