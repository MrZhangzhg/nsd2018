import requests
import json

url = 'http://192.168.4.2/zabbix/api_jsonrpc.php'
headers = {'Content-Type': 'application/json-rpc'}
# https://www.zabbix.com/documentation/3.4/zh/manual/api/reference/apiinfo/version
# data是从官方文档处获得的
data = {
    "jsonrpc": "2.0",
    "method": "apiinfo.version",
    "params": [],
    "id": 1
}

r = requests.post(url, headers=headers, data=json.dumps(data))
print(r.json())
