from urllib import request, error

no_url = 'http://127.0.0.1/abc/'
ban_url = 'http://127.0.0.1/ban/'

try:
    html1 = request.urlopen(no_url)
except error.HTTPError as e:  # 将报错信息保存到变量e中
    print(e)
# mkdir -m 700 /var/www/html/ban/
try:
    html2 = request.urlopen(ban_url)
except error.HTTPError as e:
    print(e)
