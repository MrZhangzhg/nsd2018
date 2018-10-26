import os
import socket
import time

class TcpTimeServ:
    def __init__(self, host='', port=21567):
        self.addr = (host, port)
        self.serv = socket.socket()
        self.serv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.serv.bind(self.addr)
        self.serv.listen(1)

    def mainloop(self):
        while True:
            cli_sock, cli_addr = self.serv.accept()
            pid = os.fork()
            if pid:
                cli_sock.close()
            else:
                self.serv.close()
                while True:
                    data = cli_sock.recv(1024).decode()
                    if data.strip() == 'quit':
                        break
                    sdata = '[%s] %s' % (time.strftime('%H:%M:%S'), data)
                    cli_sock.send(sdata.encode())
                cli_sock.close()
                exit()

if __name__ == '__main__':
    serv = TcpTimeServ()
    serv.mainloop()
