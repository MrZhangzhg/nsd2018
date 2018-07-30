import requests

def get_weather(city_code):
    url = 'http://www.weather.com.cn/data/sk/%s.html' % city_code
    r = requests.get(url)
    r.encoding = 'utf8'
    data = r.json()
    output = '风向：%s, 风力: %s， 温度：%s, 湿度：%s' % (
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

