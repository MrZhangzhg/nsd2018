import requests

url = 'http://127.0.0.1/polls/4/vote/'
data = {'c_id': 9}

r = requests.post(url, data=data)
print(r.text)
