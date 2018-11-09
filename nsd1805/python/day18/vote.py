import requests

url = 'http://127.0.0.1/polls/3/vote/'
data = {'choice': "6"}

for i in range(100):
    r = requests.post(url, data=data)
