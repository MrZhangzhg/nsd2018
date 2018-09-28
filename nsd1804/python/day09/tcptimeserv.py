import socket
from time import strftime
import os

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
            pid = os.fork()  # 服务器、客户端套接字在父子进程中都有

            if pid:
                cli_sock.close()   # 父进程关闭客户端套接字
                while True:
                    rc = os.waitpid(-1, 1)  # 每个waitpid只能处理一个子进程
                    print(rc)
                    if rc[0] == 0:
                        break
            else:
                self.serv.close()  # 子进程关闭服务器套接字
                self.handle_child(cli_sock)
                exit(0)

        self.serv.close()

if __name__ == '__main__':
    s = TcpTimeServ()
    s.mainloop()
