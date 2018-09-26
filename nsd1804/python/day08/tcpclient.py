import socket

host = '192.168.4.254'
port = 12345
addr = (host, port)  # 指定要连接的服务器
c = socket.socket()
c.connect(addr)
while True:
    data = input('> ') + '\r\n'
    data = data.encode()
    c.send(data)
    if data.strip() == b'quit':
        break
    rdata = c.recv(1024).decode()  # 将bytes转成str类型
    print(rdata, end='')

c.close()
