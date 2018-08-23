import socket

host = '192.168.4.254'
port = 12345
addr = (host, port)  # 客户机要连接哪台服务器
c = socket.socket()
c.connect(addr)

while True:
    data = input('> ')
    sdata = '%s\r\n' % data
    c.send(sdata.encode('utf8'))
    if data.strip() == 'quit':
        break
    rdata = c.recv(1024)
    print(rdata.decode('utf8'))

c.close()
