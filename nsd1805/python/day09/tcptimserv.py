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
            try:
                cli_sock, cli_addr = self.serv.accept()
            except KeyboardInterrupt:
                print()
                break
            pid = os.fork()
            if pid:
                cli_sock.close()
                while True:
                    # 一个waitpid只能处理一个僵尸进程，多个子进程需要循环执行
                    # waitpid优先处理僵尸进程，然后再处理非僵尸进程
                    result = os.waitpid(-1, 1)[0]
                    print(result)
                    if not result:  # 如果result值为0就break
                        break
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
        self.serv.close()

if __name__ == '__main__':
    serv = TcpTimeServ()
    serv.mainloop()
