import socket

host = ''
port = 12345
addr = (host, port)
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(addr)
s.listen(1)

while True:
    try:
        cli_sock, cli_addr = s.accept()
    except KeyboardInterrupt:
        break
    print('Hello,', cli_addr)

    while True:
        data = cli_sock.recv(1024).decode()   # 把bytes类型解码为str类型
        if data.strip() == 'quit':
            break
        print(data)
        sdata = input('> ') + '\r\n'
        cli_sock.send(sdata.encode())   # 将str编码为bytes

    cli_sock.close()

s.close()
