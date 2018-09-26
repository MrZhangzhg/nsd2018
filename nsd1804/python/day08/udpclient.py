import socket

host = '192.168.4.254'
port = 12345
addr = (host, port)

c = socket.socket(type=socket.SOCK_DGRAM)
c.sendto(b'hello world!\r\n', addr)
data = c.recvfrom(1024)[0]
print(data.decode(), end='')
c.close()
