import subprocess
import threading

def ping(host):
    rc = subprocess.call(
        'ping -c2 %s &> /dev/null' % host,
        shell=True
    )
    if rc:
        print('%s: down' % host)
    else:
        print('%s: up' % host)

if __name__ == '__main__':
    ips = ['172.40.58.%s' % i for i in range(1, 255)]
    for ip in ips:
        # 创建线程，ping是上面定义的函数, args是传给ping函数的参数
        t = threading.Thread(target=ping, args=(ip,))
        t.start()  # 执行ping(ip)
