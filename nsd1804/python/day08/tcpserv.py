import socket

host = ''   # 空串意思是0.0.0.0
port = 12345   # 端口号，应该大于1024
addr = (host, port)
s = socket.socket()  # 默认用的是AF_INET和SOCK_STREAM
# 默认情况下，系统会为程序保留端口号1分钟，1分钟内关闭再启动将报错：端口已占用
# 加上以下的选项，程序可以停止后立即再运行起来
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(addr)
s.listen(1)  # 数字表示可以有多少客户端排队等待服务
cli_sock, cli_addr = s.accept()  # 接受客户端，返回客户端的套接字和地址
print('客户端:', cli_addr)
data = cli_sock.recv(1024)  # 最多一次读1024字节
print(data)   # 网络传输的数据是bytes类型的
cli_sock.send(b'Hello!\r\n')  # 发送数据给客户端
cli_sock.close()  # 关闭套接字
s.close()
# yum install -y telnet; telnet 127.0.0.1 12345


