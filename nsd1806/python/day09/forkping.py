import subprocess
import os

def ping(host):
    rc = subprocess.call(
        'ping -c2 %s &> /dev/null' % host,
        shell=True
    )
    if rc == 0:
        print('\033[32;1m%s:up\033[0m' % host)
    else:
        print('\033[31;1m%s:down\033[0m' % host)

if __name__ == '__main__':
    ips = ['172.40.58.%s' % i for i in range(1, 255)]
    for ip in ips:
        pid = os.fork()
        if not pid:
            ping(ip)
            exit()
