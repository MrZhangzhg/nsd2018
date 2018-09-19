import sys
import randpass
import subprocess

def adduser(username, passwd, fname):
    info = """user information:
username: %s
password: %s
"""
    subprocess.call('useradd %s' % username, shell=True)
    subprocess.call(
        'echo %s | passwd --stdin %s' % (passwd, username),
        shell=True
    )
    with open(fname, 'a') as fobj:
        fobj.write(info % (username, passwd))

if __name__ == '__main__':
    username = sys.argv[1]
    passwd = randpass.gen_pass()
    adduser(username, passwd, '/tmp/userinfo.txt')
