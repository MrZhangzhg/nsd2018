import requests
import json

url = 'http://192.168.4.2/zabbix/api_jsonrpc.php'
header = {'Content-Type': 'application/json-rpc'}

# 获得版本
data = {
    "jsonrpc": "2.0",   # json-rpc协议版本，固定的
    "method": "apiinfo.version",  # 在手册上查取的，获得版本的方法
    "params": [],   # 参数
    "id": 1    # 访问序号，随意填个数字即可
}

r = requests.post(url, headers=header, data=json.dumps(data))
print(r.json())
