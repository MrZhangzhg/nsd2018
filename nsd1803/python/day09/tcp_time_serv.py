import socket
from time import strftime

class TcpTimeServer:
    def __init__(self, host='', port=12345):
        self.addr = (host, port)
        self.serv = socket.socket()
        self.serv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.serv.bind(self.addr)
        self.serv.listen(1)

    def handle_child(self, cli_sock):
        while True:
            data = cli_sock.recv(1024)
            if data.strip() == b'quit':
                break
            data = data.decode('utf8')
            sdata = '[%s] %s' % (strftime('%H:%M:%S'), data)
            cli_sock.send(sdata.encode('utf8'))
        cli_sock.close()

    def mainloop(self):
        while True:
            try:
                cli_sock, cli_addr = self.serv.accept()
            except KeyboardInterrupt:
                break
            self.handle_child(cli_sock)
            cli_sock.close()
        self.serv.close()

if __name__ == '__main__':
    s = TcpTimeServer()
    s.mainloop()
