import socket
import sys

def communicate(cli_sock):
    while True:
        data = input('> ') + '\r\n'
        cli_sock.send(data.encode())
        if data.strip() == 'quit':
            break
        print(cli_sock.recv(1024).decode())

if __name__ == '__main__':
    host = sys.argv[1]
    port = int(sys.argv[2])
    addr = (host, port)    # 客户端要连接的服务器地址
    c = socket.socket()
    c.connect(addr)
    communicate(c)
    c.close()
