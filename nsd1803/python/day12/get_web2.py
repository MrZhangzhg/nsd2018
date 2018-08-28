'为了防止由于服务器限制，不能通过程序爬取页面，模拟使用Firefox浏览'
from urllib import request

url = 'http://127.0.0.1/'
header = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64; rv:52.0) Gecko/20100101 Firefox/52.0'
}
r = request.Request(url, headers=header)
html = request.urlopen(r)
data = html.read()
print(data.decode('utf8'))

# tail -f /var/log/httpd/access_log
