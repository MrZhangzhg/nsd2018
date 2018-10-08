import requests
import json

# 获取版本信息
# url = 'http://192.168.4.2/zabbix/api_jsonrpc.php'
# headers = {'Content-Type':	'application/json-rpc'}
# data = {
#     "jsonrpc": "2.0",
#     "method": "apiinfo.version",
#     "params": [],
#     "id": 1   # 随便指定的一个事件顺序ID
# }
# r = requests.post(url, headers=headers, data=json.dumps(data))
# print(r.json())
###############################################################
#
# 获取用户token
# url = 'http://192.168.4.2/zabbix/api_jsonrpc.php'
# headers = {'Content-Type':	'application/json-rpc'}
# data = {
#     "jsonrpc": "2.0",
#     "method": "user.login",
#     "params": {
#         "user": "Admin",
#         "password": "zabbix"
#     },
#     "id": 1,
# }
# r = requests.post(url, headers=headers, data=json.dumps(data))
# print(r.json())
# 7936d4d6c3116a17365f6e02a9abe8da
###############################################################
#
# 获取所有的主机信息
# url = 'http://192.168.4.2/zabbix/api_jsonrpc.php'
# headers = {'Content-Type':	'application/json-rpc'}
# data = {
#     "jsonrpc": "2.0",
#     "method": "host.get",
#     "params": {
#         "output": "extend",
#     },
#     "auth": "7936d4d6c3116a17365f6e02a9abe8da",
#     "id": 1
# }
# r = requests.post(url, headers=headers, data=json.dumps(data))
# print(r.json())
###############################################################
#
# 获取特定主机信息
# url = 'http://192.168.4.2/zabbix/api_jsonrpc.php'
# headers = {'Content-Type':	'application/json-rpc'}
# data = {
#     "jsonrpc": "2.0",
#     "method": "host.get",
#     "params": {
#         "output": "extend",
#         "filter": {
#             "host": [
#                 "Zabbix server",
#             ]
#         }
#     },
#     "auth": "7936d4d6c3116a17365f6e02a9abe8da",
#     "id": 1
# }
# r = requests.post(url, headers=headers, data=json.dumps(data))
# print(r.json())
###############################################################
#
# 获取主机组信息
# url = 'http://192.168.4.2/zabbix/api_jsonrpc.php'
# headers = {'Content-Type':	'application/json-rpc'}
# data = {
#     "jsonrpc": "2.0",
#     "method": "hostgroup.get",
#     "params": {
#         "output": "extend",
#         "filter": {
#             "name": [
#                 "Linux servers"    # 2
#             ]
#         }
#     },
#     "auth": "7936d4d6c3116a17365f6e02a9abe8da",
#     "id": 1
# }
# r = requests.post(url, headers=headers, data=json.dumps(data))
# print(r.json())
###############################################################
#
# 获取模板信息
# url = 'http://192.168.4.2/zabbix/api_jsonrpc.php'
# headers = {'Content-Type':	'application/json-rpc'}
# data = {
#     "jsonrpc": "2.0",
#     "method": "template.get",
#     "params": {
#         "output": "extend",
#         "filter": {
#             "host": [
#                 "Template OS Linux",   # 10001
#             ]
#         }
#     },
#     "auth": "7936d4d6c3116a17365f6e02a9abe8da",
#     "id": 1
# }
# r = requests.post(url, headers=headers, data=json.dumps(data))
# print(r.json())
###############################################################
#
# 创建主机，位于Linux servers组，应用Template OS Linux模板
url = 'http://192.168.4.2/zabbix/api_jsonrpc.php'
headers = {'Content-Type':	'application/json-rpc'}
data = {
    "jsonrpc": "2.0",
    "method": "host.create",
    "params": {
        "host": "Mysql server1",
        "interfaces": [
            {
                "type": 1,
                "main": 1,
                "useip": 1,
                "ip": "192.168.4.3",
                "dns": "",
                "port": "10050"
            }
        ],
        "groups": [
            {
                "groupid": "2"
            }
        ],
        "templates": [
            {
                "templateid": "10001"
            }
        ],
        # "inventory_mode": 0,
        # "inventory": {
        #     "macaddress_a": "01234",
        #     "macaddress_b": "56768"
        # }
    },
    "auth": "7936d4d6c3116a17365f6e02a9abe8da",
    "id": 1
}
r = requests.post(url, headers=headers, data=json.dumps(data))
print(r.json())
