import urllib.error
from urllib import request

url1 = 'http://127.0.0.1/abc'
url2 = 'http://127.0.0.1/ban'
url3 = 'http://127.0.0.1/'

try:
    r1 = request.urlopen(url1)
except urllib.error.HTTPError as e:
    print('错误：', e)
else:
    print(r1.read())

try:
    r2 = request.urlopen(url2)
except urllib.error.HTTPError as e:
    print('错误：', e)
else:
    print(r2.read())

r3 = request.urlopen(url3)
print(r3.read())
