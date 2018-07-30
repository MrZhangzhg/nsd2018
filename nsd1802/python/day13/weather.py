from urllib.request import urlopen
import json

html = urlopen('http://www.weather.com.cn/data/sk/101010100.html')
data = html.read()
print(json.loads(data))

html.close()

# 城市代码
# http://www.360docs.net/doc/info-9501c425af45b307e871976b-2.html

# 图片位置
# http://m.weather.com.cn/img/c0.gif
#
# http://m.weather.com.cn/img/b0.gif
#
# http://www.weather.com.cn/m/i/weatherpic/29x20/d0.gif
#
# http://www.weather.com.cn/m2/i/icon_weather/29x20/n00.gif
