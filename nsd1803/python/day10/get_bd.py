from urllib import request

html = request.urlopen('http://www.baidu.com/')
print(html.read().decode('utf8'))

