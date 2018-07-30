from urllib.request import urlopen
import json

def get_weather(city_code):
    url = 'http://www.weather.com.cn/data/sk/%s.html' % city_code
    html = urlopen(url)
    data = json.loads(html.read())
    output = '风向：%s, 风力: %s， 温度：%s, 温度：%s' % (
        data['weatherinfo']['WD'],
        data['weatherinfo']['WS'],
        data['weatherinfo']['temp'],
        data['weatherinfo']['SD']
    )
    return output



if __name__ == '__main__':
    city_codes = { '0': '101010100', '1': '101121404'}
    prompt = """(0) 北京
(1) 台儿庄
请选择(0/1): """
    choice = input(prompt)
    print(get_weather(city_codes[choice]))

