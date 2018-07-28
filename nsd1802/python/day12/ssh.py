import paramiko

ssh = paramiko.SSHClient()  # 创建实例
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())  # 相当于回答yes
ssh.connect(
    hostname='127.0.0.1',
    username='root',
    port=22,
    password='redhat'
)
a = ssh.exec_command('ls /home')
# a是由类文件对象组成的列表，共三项，分别是输入、输出、错误
print(len(a))
out = a[1].read()
error = a[2].read()
print(out.decode('utf8'))
print(error.decode('utf8'))
ssh.close()
