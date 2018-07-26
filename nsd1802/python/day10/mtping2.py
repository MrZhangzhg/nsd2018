import threading
import subprocess

class Ping:
    def __init__(self, host):
        self.host = host

    def __call__(self):
        rc = subprocess.call(
            'ping -c2 %s &> /dev/null' % self.host,
            shell=True
        )
        if rc:
            print('%s: down' % self.host)
        else:
            print('%s: up' % self.host)

if __name__ == '__main__':
    ips = ('172.40.58.%s' % i for i in range(1, 255))  # 创建生成器
    for ip in ips:
        t = threading.Thread(target=Ping(ip))  # 创建Ping的实例
        t.start()   # target()
