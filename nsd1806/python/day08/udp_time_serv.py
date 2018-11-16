import socket
import time

host = ''
port = 12345
addr = (host, port)
s = socket.socket(type=socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(addr)

while True:
    try:
        data, cli_addr = s.recvfrom(1024)
    except KeyboardInterrupt:
        print()
        break
    data = '[%s] %s' % (time.strftime('%H:%M:%S'), data.decode())
    s.sendto(data.encode(), cli_addr)

s.close()
