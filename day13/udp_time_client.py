#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import socket
import sys
class UdpTimeClient(object):
    def __init__(self,host='',port=12345):
        self.addr = (host,port)
        self.cli = socket.socket(type=socket.SOCK_DGRAM)

    def communicate(self):
        while True:
            data = input(">") + '\r\n'
            data = data.encode('utf8')
            if data == b'quit':
                break
            self.cli.sendto(data,self.addr)
            print(self.cli.recvfrom(1024)[0].decode('utf8'),end='')
    def close(self):
        self.cli.close()
if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("%s host port"%sys.argv[0])
        sys.exit(1)
    ip = sys.argv[1]
    port = sys.argv[2]
    udp_cli = UdpTimeClient(ip,port)
    udp_cli.communicate()
    udp_cli.close()