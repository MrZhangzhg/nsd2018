import json
import requests

url = 'http://192.168.4.2/zabbix/api_jsonrpc.php'
header = {'Content-Type': 'application/json-rpc'}
# data = {
#     "jsonrpc": "2.0",   # 固定的，jsonrpc协议的版本
#     "method": "apiinfo.version",   # 方法，在官方文档上查询
#     "params": [],    # 参数
#     "id": 1          # 随便给一个数字即可，表示任务的ID号
# }
###############################
# 获取令牌token
# data = {
#     "jsonrpc": "2.0",
#     "method": "user.login",
#     "params": {
#         "user": "Admin",
#         "password": "zabbix"
#     },
#     "id": 1
# }
# 540dcb9510a41ef32a78b4071d99dc76
################################
# 获取所有主机的信息
# data = {
#     "jsonrpc": "2.0",
#     "method": "host.get",
#     "params": {
#         "output": "extend",
#     },
#     "auth": "540dcb9510a41ef32a78b4071d99dc76",
#     "id": 1
# }
################################
# 将主机ID是10257和10258的主机从zabbix中删除
# data = {
#     "jsonrpc": "2.0",
#     "method": "host.delete",
#     "params": [
#         "10257",   # 被删除的主机id
#         "10258"
#     ],
#     "auth": "540dcb9510a41ef32a78b4071d99dc76",
#     "id": 1
# }
################################
# 获取Linux Servers 组的信息，如groupid
# data = {
#     "jsonrpc": "2.0",
#     "method": "hostgroup.get",
#     "params": {
#         "output": "extend",
#         "filter": {
#             "name": [
#                 "Linux servers"
#             ]
#         }
#     },
#     "auth": "540dcb9510a41ef32a78b4071d99dc76",
#     "id": 1
# }
#
################################
# 获取Template OS Linux模板信息，如它的ID
# data = {
#     "jsonrpc": "2.0",
#     "method": "template.get",
#     "params": {
#         "output": "extend",
#         "filter": {
#             "host": [
#                 "Template OS Linux",
#             ]
#         }
#     },
#     "auth": "540dcb9510a41ef32a78b4071d99dc76",
#     "id": 1
# }
################################

data = {
    "jsonrpc": "2.0",
    "method": "host.create",
    "params": {
        "host": "web_server1",
        "interfaces": [
            {
                "type": 1,
                "main": 1,
                "useip": 1,
                "ip": "192.168.4.10",
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
        "inventory_mode": 0,
        "inventory": {
            "macaddress_a": "01234",
            "macaddress_b": "56768"
        }
    },
    "auth": "540dcb9510a41ef32a78b4071d99dc76",
    "id": 1
}
r = requests.post(url, data=json.dumps(data), headers=header)
print(r.json())
