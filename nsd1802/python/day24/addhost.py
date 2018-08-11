import requests

url = 'http://127.0.0.1/hosts/addhost/'
data = {
    'hostname': 'node1.tedu.cn',
    'ipaddr': '192.168.4.1',
    'group': 'webservers',
}
requests.post(url, data=data)
