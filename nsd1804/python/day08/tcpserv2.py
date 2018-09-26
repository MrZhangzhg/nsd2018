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
    print('客户端:', cli_addr)
    while True:
        data = cli_sock.recv(1024)
        if data.strip() == b'quit':
            break
        print(data)
        # cli_sock.send(b'Hello!\r\n')
        rdata = input('> ') + '\r\n'
        cli_sock.send(rdata.encode())  # 将str转化成bytes
    cli_sock.close()
s.close()
