import paramiko
import sys
import getpass
import os
import threading

def rcmd(host, username='root', password=None, cmd=None):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(host, username=username, password=password)
    stdin, stdout, stderr = ssh.exec_command(cmd)
    out = stdout.read()
    err = stderr.read()
    if out:
        print('[%s] OUT:\n%s' % (host, out.decode()))
    if err:
        print('[%s] ERROR:\n%s' % (host, err.decode()))
    ssh.close()

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: %s ipfile "command"' % sys.argv[0])
        exit(1)
    ipfile = sys.argv[1]
    if not os.path.isfile(ipfile):
        print('No such file:', ipfile)
        exit(2)
    cmd = sys.argv[2]
    password = getpass.getpass()
    with open(ipfile) as fobj:
        for line in fobj:
            ip = line.strip()
            t = threading.Thread(target=rcmd, args=(ip, 'root', password, cmd))
            t.start()
            # rcmd(ip, password=password, cmd=cmd)
