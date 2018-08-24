import threading
import subprocess

class Ping:
    # def __init__(self, host):
    #     self.host = host

    def __call__(self, host):
        result = subprocess.call(
            'ping -c2 %s &> /dev/null' % host,
            shell=True
        )
        if result == 0:  # result的值就是ping命令的退出码，即$?
            print('%s:up' % host)
        else:
            print('%s:down' % host)

if __name__ == '__main__':
    ips = ['172.40.58.%s' % i for i in range(1, 255)]
    for ip in ips:
        t = threading.Thread(target=Ping(), args=(ip,))
        t.start()  # Ping(ip)() <==> target()




