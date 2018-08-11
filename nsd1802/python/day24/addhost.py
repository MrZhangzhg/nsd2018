import requests

url = 'http://127.0.0.1/hosts/addhost/'
data = {
    'hostname': 'node7.tedu.cn',
    'ipaddr': '192.168.4.7',
    'group': 'webservers',
}
requests.post(url, data=data)
# hosts = [
#     {'hostname': 'node2.tedu.cn','ipaddr': '192.168.4.2','group': 'webservers',},
#     {'hostname': 'node3.tedu.cn','ipaddr': '192.168.4.3','group': 'webservers',},
#     {'hostname': 'node4.tedu.cn','ipaddr': '192.168.4.4','group': 'webservers',},
#     {'hostname': 'node5.tedu.cn','ipaddr': '192.168.4.5','group': 'dbservers',},
#     {'hostname': 'node6.tedu.cn','ipaddr': '192.168.4.6','group': 'dbservers',},
# ]
# for data in hosts:
#     requests.post(url, data=data)

