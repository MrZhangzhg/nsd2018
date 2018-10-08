import json
from urllib import request

html = request.urlopen('http://www.weather.com.cn/data/sk/101010100.html')
data = html.read()
data = json.loads(data)
print(data)
print("%s: %s" % (data['weatherinfo']['city'], data['weatherinfo']['temp']))
###############################
#
# html = request.urlopen('http://www.weather.com.cn/data/cityinfo/101010100.html')
# data = html.read()
# print(json.loads(data))
# 图标网址是：http://m.weather.com.cn/img/
###############################
#
# html = request.urlopen('http://www.weather.com.cn/data/zs/101010100.html')
# data = html.read()
# print(json.loads(data))
