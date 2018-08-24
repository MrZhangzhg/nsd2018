import subprocess
import os

def ping(host):
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
        pid = os.fork()  # 父进程负责生成子进程
        if not pid:  # 子进程负责ping
            ping(ip)
            exit()  # 子进程ping完一个地址后结束，不要再循环


