import socket
import threading
from time import strftime

class TcpTimeServ:
    def __init__(self, host='', port=12345):
        self.addr = (host, port)
        self.serv = socket.socket()
        self.serv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.serv.bind(self.addr)
        self.serv.listen(1)

    def handle_child(self, c_sock):
        while True:
            data = c_sock.recv(1024)
            if data.strip() == b'quit':
                break
            data = '[%s] %s' % (strftime('%Y-%m-%d %H:%M:%S'), data.decode())
            c_sock.send(data.encode())
        c_sock.close()

    def mainloop(self):
        while True:
            try:
                cli_sock, cli_addr = self.serv.accept()
            except:
                break

            t = threading.Thread(target=self.handle_child, args=(cli_sock,))
            t.start()

        self.serv.close()

if __name__ == '__main__':
    s = TcpTimeServ()
    s.mainloop()
