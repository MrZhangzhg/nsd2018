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
data = {
    "jsonrpc": "2.0",
    "method": "host.get",
    "params": {
        "output": "extend",
    },
    "auth": "540dcb9510a41ef32a78b4071d99dc76",
    "id": 1
}
r = requests.post(url, data=json.dumps(data), headers=header)
print(r.json())
