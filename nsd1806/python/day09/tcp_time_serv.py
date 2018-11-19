import time
import socket
import os

class TcpTimeServ:
    def __init__(self, host='', port=12345):
        self.addr = (host, port)
        self.serv = socket.socket()
        self.serv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.serv.bind(self.addr)
        self.serv.listen(1)

    def chat(self, cli_sock):
        while True:
            data = cli_sock.recv(1024).decode()
            if data.strip() == 'quit':
                break
            data = '[%s] %s' % (time.strftime('%H:%M:%S'), data)
            cli_sock.send(data.encode())

    def mainloop(self):
        while True:
            try:
                cli_sock, cli_addr = self.serv.accept()
            except KeyboardInterrupt:
                print()
                break

            pid = os.fork()
            if not pid:
                self.chat(cli_sock)
                cli_sock.close()
                exit()

            cli_sock.close()
            while True:
                result = os.waitpid(-1, 1)  # 优先处理僵尸进程
                print(result)
                if result[0] == 0:
                    break


        self.serv.close()

if __name__ == '__main__':
    s = TcpTimeServ()
    s.mainloop()
