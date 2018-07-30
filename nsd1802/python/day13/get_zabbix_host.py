import requests
import json

url = 'http://192.168.4.2/zabbix/api_jsonrpc.php'
headers = {'Content-Type': 'application/json-rpc'}
data = {
    "jsonrpc": "2.0",
    "method": "host.get",
    "params": {
        "output": "extend",
        "filter": {
            "host": [
                "Zabbix server",
            ]
        }
    },
    "auth": "2301719709f1071a363d1186e69a53cc",
    "id": 1
}

r = requests.post(url, headers=headers, data=json.dumps(data))
print(r.json())
