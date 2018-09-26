import socket

host = '192.168.4.254'
port = 12345
addr = (host, port)
c = socket.socket(type=socket.SOCK_DGRAM)

while True:
    data = input('> ') + '\r\n'
    if data.strip() == 'quit':
        break
    c.sendto(data.encode(), addr)
    data = c.recvfrom(1024)[0]
    print(data.decode(), end='')

c.close()
