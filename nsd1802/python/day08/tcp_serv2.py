import socket

host = ''
port = 12345
addr = (host, port)
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(addr)
s.listen(1)
while True:
    cli_sock, cli_addr = s.accept()
    print('Client connect from:', cli_addr)
    while True:
        data = cli_sock.recv(1024)
        if data.strip() == b'end':
            break
        print(data.decode('utf8'))  # bytes类型转为string类型
        data = input('> ') + '\r\n'  # 获得的是string类型
        cli_sock.send(data.encode('utf8'))  # 转成bytes类型发送
    cli_sock.close()
s.close()
