import requests
import json

url = 'http://192.168.4.2/zabbix/api_jsonrpc.php'
headers = {'Content-Type': 'application/json-rpc'}
data = {
    "jsonrpc": "2.0",
    "method": "host.get",
    "params": {
        "output": ["hostid", "host"],
        "selectInterfaces":	["interfaceid",	"ip", "dns"]
    },
    "id": 2,
    "auth": "2301719709f1071a363d1186e69a53cc"
}

r = requests.post(url, headers=headers, data=json.dumps(data))
print(r.json())
