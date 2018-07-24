import socket

host = ''  # 表示本机所有地址 0.0.0.0
port = 12345  # 应该大于1024
addr = (host, port)
s = socket.socket()  # 默认值就是基于TCP的网络套接字
# 设置选项，程序结束之后可以立即再运行，否则要等60秒
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(addr)  # 绑定地址到套接字
s.listen(1)  # 启动侦听进程
cli_sock, cli_addr = s.accept()  # 等待客户端连接
print('Client connect from:', cli_addr)
print(cli_sock.recv(1024))  # 一次最多读1024字节数据
cli_sock.send(b'I 4 C U\r\n')  # 发送的数据要求是bytes类型
cli_sock.close()
s.close()
# yum install -y telnet
# telnet 127.0.0.1 12345
