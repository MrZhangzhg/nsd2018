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
    print('Client connected from:', cli_addr)
    while True:
        data = cli_sock.recv(1024)
        if data.strip() == b'quit':
            break
        print(data.decode('utf8'))
        sdata = input('> ')
        sdata = '%s\r\n' % sdata
        cli_sock.send(sdata.encode('utf8'))

    cli_sock.close()
s.close()
