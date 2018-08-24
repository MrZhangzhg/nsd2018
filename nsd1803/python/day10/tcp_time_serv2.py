import socket
import os
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
            pid = os.fork()  # 创建子进程
            if pid:
                while True:
                    # 通过循环，处理所有的子进程，waitpid会优先处理僵尸进程
                    # 正在运行的子进程返回(0,0)，则中断循环
                    result = os.waitpid(-1, 1)
                    # print(result)
                    if result[0] == 0:
                        break
                cli_sock.close()  # 父进程只负责响应客户端，不用和客户通信
            else:
                self.serv.close()  # 子进程只负责与客户通信，不负责建立连接
                self.handle_child(cli_sock)
                exit()  # 子进程通信完后，要退出，不要再进入循环
        self.serv.close()

if __name__ == '__main__':
    s = TcpTimeServer()
    s.mainloop()
