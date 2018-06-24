#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import socket


class TcpCli(object):
    def __init__(self, host="127.0.0.1", port=12345):
        self.addr = (host, port)
        self.cli = socket.socket()
        self.cli.connect(self.addr)

    def handle_data(self, data):
        data.encode('utf8')
        self.cli.send(data)
        # self.cli.recv(1024)
        print(self.cli.recv(1024).decode('utf8'))

    def input_data(self):
        pass

    def tcp_close(self):
        self.cli.close()


if __name__ == '__main__':
    clis = TcpCli()
    while True:
        # try:
        data = input(">>>") + "\r\n"
        # except KeyboardInterrupt:
        #    print("Ctrl C")
        data = data.encode('utf8')
        clis.handle_data(data)
        if data == b"quit":
            clis.tcp_close()
            break
        # clis.input_data(data)
