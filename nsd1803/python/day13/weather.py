from urllib import request
import json

weather = request.urlopen('http://www.weather.com.cn/data/sk/101010100.html')
info = request.urlopen('http://www.weather.com.cn/data/cityinfo/101010100.html')
zhishu = request.urlopen('http://www.weather.com.cn/data/zs/101010100.html')
weather_data = weather.read()
info_data = info.read()
zs_data = zhishu.read()
print(json.loads(weather_data))
print('*' * 50)
print(json.loads(info_data))
print('*' * 50)
print(json.loads(zs_data))


