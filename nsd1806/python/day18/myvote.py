import requests

url = 'http://192.168.4.254/polls/4/vote/'
data = {"choice_id": "16"}

for i in range(100):
    requests.post(url, data=data)
