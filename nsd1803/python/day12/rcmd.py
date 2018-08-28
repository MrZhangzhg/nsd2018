import paramiko
import sys
import getpass
import threading
import os

def rcmd(host, password, cmd, port=22, username='root'):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(
        hostname=host,
        username=username,
        password=password,
        port=port
    )
    stdin, stdout, stderr = ssh.exec_command(cmd)
    data = stdout.read().decode('utf8')
    error = stderr.read().decode('utf8')
    if data:
        print('[%s: OUT]:\n%s' % (host, data))
    if error:
        print('[%s: ERROR]:\n%s' % (host, error))

    ssh.close()

if __name__ == '__main__':
    # rcmd('192.168.4.2', '123456', 'ls /root')
    if len(sys.argv) != 3:
        print('Usage: %s ipfile "command"' % sys.argv[0])
        exit(1)
    pwd = getpass.getpass()
    ipfile = sys.argv[1]  # IP地址文件
    cmd = sys.argv[2]
    if not os.path.isfile(ipfile):
        print('No such file:', ipfile)
        exit(2)

    with open(ipfile) as fobj:
        for line in fobj:
            ip = line.strip()
            t = threading.Thread(target=rcmd, args=(ip, pwd, cmd))
            t.start()
