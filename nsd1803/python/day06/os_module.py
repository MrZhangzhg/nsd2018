import os

os.getcwd()  # pwd
os.listdir()  # ls
os.listdir('/tmp/mydemo')  # ls /tmp/mydemo
os.mkdir('/tmp/mydemo')
os.chdir('/tmp/mydemo')
os.mknod('mytest')  # touch mytest
os.symlink('/etc/hosts', 'zhuji')  # ln -s /etc/hosts zhuji
os.makedirs('aaa/bbb/ccc')  # mkdir -p aaa/bbb/ccc
os.path.isfile('zhuji')
os.path.isdir('/tmp')
os.path.exists('/abc')
os.path.abspath('zhuji')
os.path.basename('/tmp/abc/aaa.txt')
os.path.dirname('/tmp/abc/aaa.txt')
os.path.split('/tmp/abc/aaa.txt')
os.path.splitext('/tmp/abc/aaa.txt')
os.path.join('/tmp', 'abc')
os.remove('mytest')
os.rmdir('aaa/bbb/ccc')  # 删除空目录
os.chmod('aaa', 0o777)





