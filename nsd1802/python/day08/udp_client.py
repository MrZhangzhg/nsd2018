import socket

host = '192.168.4.254'
port = 12345
addr = (host, port)

c = socket.socket(type=socket.SOCK_DGRAM)

while True:
    data = input('> ')
    if data.strip() == 'quit':
        break
    c.sendto(data.encode('utf8'), addr)
    print(c.recvfrom(1024)[0].decode('utf8'))
    # print(c.recvfrom(1024))

c.close()
