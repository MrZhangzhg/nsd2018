import requests
import json

url = 'http://192.168.4.2/zabbix/api_jsonrpc.php'
header = {'Content-Type': 'application/json-rpc'}

# data = {
#     "jsonrpc": "2.0",
#     "method": "user.login",
#     "params": {
#         "user": "Admin",
#         "password": "zabbix"
#     },
#     "id": 1
# }
# b357b8f09561f4134f7f417f76dffa3b

# data = {
#     "jsonrpc": "2.0",
#     "method": "host.get",
#     "params": {
#         "output": "extend",
#         "filter": {
#             "host": [
#                 "Zabbix server",
#                 "Linux server"
#             ]
#         }
#     },
#     "auth": "b357b8f09561f4134f7f417f76dffa3b",
#     "id": 1
# }

# data = {
#     "jsonrpc": "2.0",
#     "method": "hostgroup.get",
#     "params": {
#         "output": "extend",
#         "filter": {
#             "name": [
#                 "Zabbix servers",
#                 "Linux servers"
#             ]
#         }
#     },
#     "auth": "b357b8f09561f4134f7f417f76dffa3b",
#     "id": 1
# }

# data = {
#     "jsonrpc": "2.0",
#     "method": "template.get",
#     "params": {
#         "output": "extend",
#         "filter": {
#             "host": [
#                 "Template OS Linux",  # 10001
#             ]
#         }
#     },
#     "auth": "b357b8f09561f4134f7f417f76dffa3b",
#     "id": 1
# }

data = {
    "jsonrpc": "2.0",
    "method": "host.create",
    "params": {
        "host": "webserver2",
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
        "inventory_mode": 1,
        "inventory": {  # 主机资产清单
            "macaddress_a": "01234",
            "macaddress_b": "56768"
        }
    },
    "auth": "b357b8f09561f4134f7f417f76dffa3b",
    "id": 1
}

r = requests.post(url, headers=header, data=json.dumps(data))
print(r.json())
