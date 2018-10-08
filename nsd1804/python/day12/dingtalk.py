import json
import requests
import sys


def send_msg(url, reminders, msg):
    headers = {'Content-Type': 'application/json;charset=utf-8'}
    data = {
        "msgtype": "text",  # 发送消息类型为文本
        "at": {
            "atMobiles": reminders,
            "isAtAll": False,   # 不@所有人
        },
        "text": {
            "content": msg,   # 消息正文
        }
    }
    r = requests.post(url, data=json.dumps(data), headers=headers)
    return r.text

if __name__ == '__main__':
    msg = sys.argv[1]
    reminders = []  # 特殊提醒要查看的人,就是@某人一下
    url = '将钉钉机器人的网址粘贴过来'
    print(send_msg(url, reminders, msg))
