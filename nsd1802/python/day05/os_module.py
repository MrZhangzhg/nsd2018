import os

os.getcwd()  # 显示当前路径
os.listdir()  # ls -a
os.listdir('/tmp')  # ls -a /tmp
os.mkdir('/tmp/mydemo')  # mkdir /tmp/mydemo
os.chdir('/tmp/mydemo')  # cd /tmp/mydemo
os.listdir()
os.mknod('test.txt')  # touch test.txt
os.symlink('/etc/hosts', 'zhuji')  # ln -s /etc/hosts zhuji
os.path.isfile('test.txt')  # 判断test.txt是不是文件
os.path.islink('zhuji')  # 判断zhuji是不是软链接
os.path.isdir('/etc')
os.path.exists('/tmp')  # 判断是否存在
os.path.basename('/tmp/abc/aaa.txt')
os.path.dirname('/tmp/abc/aaa.txt')
os.path.split('/tmp/abc/aaa.txt')
os.path.join('/home/tom', 'xyz.txt')
os.path.abspath('test.txt')  # 返回当前目录test.txt的绝对路径












