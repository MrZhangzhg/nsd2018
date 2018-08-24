import threading
import subprocess

class Ping:
    def __init__(self, host):
        self.host = host

    def __call__(self):
        result = subprocess.call(
            'ping -c2 %s &> /dev/null' % self.host,
            shell=True
        )
        if result == 0:  # result的值就是ping命令的退出码，即$?
            print('%s:up' % self.host)
        else:
            print('%s:down' % self.host)

if __name__ == '__main__':
    ips = ['172.40.58.%s' % i for i in range(1, 255)]
    for ip in ips:
        t = threading.Thread(target=Ping(ip))
        t.start()  # Ping(ip)() <==> target()




