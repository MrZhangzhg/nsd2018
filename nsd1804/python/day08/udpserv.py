import socket
from time import strftime

host = ''
port = 12345
addr = (host, port)
s = socket.socket(type=socket.SOCK_DGRAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind(addr)

data, cli_addr = s.recvfrom(1024)
data = data.decode()
sdata = '[%s] %s' % (strftime('%Y-%m-%d %H:%M:%S'), data)
s.sendto(sdata.encode(), cli_addr)
s.close()
