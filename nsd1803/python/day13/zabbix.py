import json
import requests

# 获取zabbix版本号
# url = 'http://192.168.4.2/zabbix/api_jsonrpc.php'
# headers = {'Content-Type': 'application/json-rpc'}
# data = {
#     'jsonrpc': '2.0',  # jsonrpc协议的版本号，固定的
#     'method': 'apiinfo.version',  # 在zabbix手册上查到的，查询zabbix版本
#     'id': 1,  # 随便写个数字
#     'auth':	None,  # 不需要身份认证
#     'params': {},  # 没有额外参数
# }
# # zabbix要求提交的数据是json格式
# r = requests.post(url, headers=headers, data=json.dumps(data))
# print(r.json())   # zabbix返回的数据都是json格式
#############################################
# 获取admin的令牌
# url = 'http://192.168.4.2/zabbix/api_jsonrpc.php'
# headers = {'Content-Type': 'application/json-rpc'}
# data = {
#     "jsonrpc": "2.0",
#     "method": "user.login",
#     "params": {
#         "user": "Admin",
#         "password": "zabbix"
#     },
#     "id": 1
# }
# r = requests.post(url, headers=headers, data=json.dumps(data))
# print(r.json())
#############################################
# 检索所有的主机
# url = 'http://192.168.4.2/zabbix/api_jsonrpc.php'
# headers = {'Content-Type': 'application/json-rpc'}
# data = {
#     "jsonrpc": "2.0",
#     "method": "host.get",
#     "params": {
#         "output": "extend",
#         # "filter": {      # 过滤，如果不过滤，显示所有主机
#         #     "host": [
#         #         "Zabbix server",
#         #         "Linux server"
#         #     ]
#         # }
#     },
#     "auth": "29a3043ce80e57ae52e4f5a621a18c5a",  # 上一步获得的令牌
#     "id": 1
# }
# r = requests.post(url, headers=headers, data=json.dumps(data))
# print(r.json())
#############################################
# 检索主机Zabbix server所在的组
# url = 'http://192.168.4.2/zabbix/api_jsonrpc.php'
# headers = {'Content-Type': 'application/json-rpc'}
# data = {
#     "jsonrpc": "2.0",
#     "method": "host.get",
#     "params": {
#         "output": ["hostid"],
#         "selectGroups": "extend",
#         "filter": {
#             "host": [
#                 "Zabbix server"
#             ]
#         }
#     },
#     "auth": "29a3043ce80e57ae52e4f5a621a18c5a",
#     "id": 2
# }
# r = requests.post(url, headers=headers, data=json.dumps(data))
# print(r.json())
#############################################
# 检索组
# url = 'http://192.168.4.2/zabbix/api_jsonrpc.php'
# headers = {'Content-Type': 'application/json-rpc'}
# data = {
#     "jsonrpc": "2.0",
#     "method": "hostgroup.get",
#     "params": {
#         "output": "extend",
#         # "filter": {
#         #     "name": [
#         #         "Zabbix servers",
#         #         "Linux servers"
#         #     ]
#         # }
#     },
#     "auth": "29a3043ce80e57ae52e4f5a621a18c5a",
#     "id": 1
# }
# r = requests.post(url, headers=headers, data=json.dumps(data))
# ginfo = r.json()
# print(ginfo['result'])
# for item in ginfo['result']:
#     print(item['groupid'], item['name'])
#############################################
# 检索模板
# url = 'http://192.168.4.2/zabbix/api_jsonrpc.php'
# headers = {'Content-Type': 'application/json-rpc'}
# data = {
#     "jsonrpc": "2.0",
#     "method": "template.get",
#     "params": {
#         "output": "extend",
#         # "filter": {
#         #     "host": [
#         #         "Template OS Linux",
#         #         "Template OS Windows"
#         #     ]
#         # }
#     },
#     "auth": "29a3043ce80e57ae52e4f5a621a18c5a",
#     "id": 1
# }
# r = requests.post(url, headers=headers, data=json.dumps(data))
# tinfo = r.json()
# # print(tinfo)
# for item in tinfo['result']:
#     print(item['templateid'], item['host'])
#############################################
# 创建主机，主机名为mylinux，加入到Linux Servers组，应用Template os Linux模板
url = 'http://192.168.4.2/zabbix/api_jsonrpc.php'
headers = {'Content-Type': 'application/json-rpc'}
data = {
    "jsonrpc": "2.0",
    "method": "host.create",
    "params": {
        "host": "mylinux",
        "interfaces": [
            {
                "type": 1,  # 1 agent; 2 SNMP; 3 IPMI; 4 JMX
                "main": 1,  # 该接口是否在主机上用作默认接口。1 默认
                "useip": 1,  # 是否应通过IP进行连接
                "ip": "192.168.4.3",
                "dns": "",
                "port": "10050"
            }
        ],
        "groups": [
            {
                "groupid": "1"
            }
        ],
        "templates": [
            {
                "templateid": "10001"
            }
        ],
        "inventory_mode": 0,
    },
    "auth": "29a3043ce80e57ae52e4f5a621a18c5a",
    "id": 1
}
r = requests.post(url, headers=headers, data=json.dumps(data))
