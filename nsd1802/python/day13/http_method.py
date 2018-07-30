import requests


payload = {'wd': 'hello world!'}
# http://www.baidu.com/s?wd=hello%20world%21
r = requests.get('http://www.baidu.com/s', params=payload)
data = r.content

with open('/tmp/bbb.html', 'wb') as fobj:
    fobj.write(data)
