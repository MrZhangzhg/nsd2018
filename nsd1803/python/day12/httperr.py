from urllib import request, error

try:
    html = request.urlopen('http://127.0.0.1/xyz/')  # xyz不存在
except error.HTTPError as e:  # 把报错信息保存到变量e中
    print(e)

try:
    html = request.urlopen('http://127.0.0.1/ban')  # ban无访问权限
except error.HTTPError as e:
    print(e)