import socket

host = ''   # 服务侦听在0.0.0.0上
port = 12345  # 服务的端口号，我们自己定义的端口号，应该大于1024
addr = (host, port)
s = socket.socket()    # 创建套接字，默认使用TCP
# 如果没有下面的指令，程序结束后，需要等1分钟才能再次运行
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(addr)       # 为套接字绑定地址
s.listen(1)   # 启动侦听过程，1表示允许多少个客户端等待，但是写多少都没用
cli_sock, cli_addr = s.accept()  # 接受客户端连接，返回客户端的套接字和地址
print('Hello,', cli_addr)
data = cli_sock.recv(1024)  # 最多接收1024字节数据
print(data)
cli_sock.send(b'I 4 C U\r\n')   # 发送数据给客户端
cli_sock.close()    # 关闭套接字
s.close()

# yum install -y telnet
# telnet 127.0.0.1 12345
