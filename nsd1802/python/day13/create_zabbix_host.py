import requests
import json

url = 'http://192.168.4.2/zabbix/api_jsonrpc.php'
headers = {'Content-Type': 'application/json-rpc'}
data = {
    "jsonrpc": "2.0",
    "method": "host.create",
    "params": {
        "host": "python linux server",
        "interfaces": [
            {
                "type": 1,
                "main": 1,
                "useip": 1,
                "ip": "192.168.4.2",
                "dns": "192.168.4.5",
                "port": "10050"
            }
        ],
        "groups": [
            {
                "groupid": "2"
            }
        ],
    },
    "auth": "2301719709f1071a363d1186e69a53cc",
    "id": 1
}

r = requests.post(url, headers=headers, data=json.dumps(data))
print(r.json())
