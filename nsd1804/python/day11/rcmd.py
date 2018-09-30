import paramiko

def rcmd(host, passwd, command, user='root', port=22):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, username=user, password=passwd, port=port)
    stdin, stdout, stderr = ssh.exec_command(command)
    out = stdout.read()
    err = stderr.read()
    if out:
        print('%s[OUT]:\n%s' % (host, out.decode()))
    if err:
        print('%s[ERROR]:\n%s' % (host, err.decode()))

if __name__ == '__main__':
    rcmd('192.168.4.2', '123456', 'id zhangsan; id wangwu')
