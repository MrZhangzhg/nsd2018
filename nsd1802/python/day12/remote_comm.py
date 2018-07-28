import sys
import getpass
import paramiko
import threading
import os

def remote_comm(host, pwd, command):
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname=host, username='root', password=pwd)
    stdin, stdout, stderr = ssh.exec_command(command)
    out = stdout.read()
    error = stderr.read()
    if out:
        print('[%s] OUT:\n%s' % (host, out.decode('utf8')))
    if error:
        print('[%s] ERROR:\n%s' % (host, error.decode('utf8')))
    ssh.close()

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Usage: %s ipaddr_file "command"' % sys.argv[0])
        exit(1)
    if not os.path.isfile(sys.argv[1]):
        print('No such file:', sys.argv[1])
        exit(2)
    fname = sys.argv[1]
    command = sys.argv[2]
    pwd = getpass.getpass()
    with open(fname) as fobj:
        ips = [line.strip() for line in fobj]

    for ip in ips:
        t = threading.Thread(target=remote_comm, args=(ip, pwd, command))
        t.start()
