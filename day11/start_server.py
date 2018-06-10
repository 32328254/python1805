#!/usr/bin/env python3
# -*- coding:utf-8 -*-
import sys
import os
from subprocess import Popen, PIPE


class Process:
    def __init__(self, workdir, name, program, args):
        """

        :param workdir: /var/tmp/memcached
        :param name: memcached
        :param program: /usr/bin/memcached
        :param args:
        """
        self.workdir = workdir
        self.name = name
        self.program = program
        self.args = args

    def _init(self):
        if not os.path.exists(self.workdir):
            os.mkdir(self.workdir)
            os.chdir(self.workdir)
            os.system("chown memcached %s" % self.workdir)

    def start(self):
        self._init()
        cmd = self.program + ' ' + self.args + ' ' + '- P %s.pid' % os.path.join(self.workdir, self.name)
        p = Popen(cmd, stdout=PIPE, stderr=PIPE, shell=True)
        if not p.stderr.read():  # 如果程序正常启动,err是null,if null 是条件不成立的,加上not 是条件成立.
            print("%s start successful" % self.name)

    def stop(self):
        pass

    def restart(self):
        self.stop()
        self.start()

    def status(self):
        pass


if __name__ == '__main__':
    workdir = '/var/tmp/memcached'
    name = 'memcached'
    program = '/usr/bin/memcached'
    args = '-u memcached -p 11211 -m 64 -c 1024 -d'
    pm = Process(workdir=workdir, name=name, program=program, args=args)
    cmd = sys.argv[1]
    if cmd == 'start':
        pm.start()
    elif cmd == 'stop':
        pm.stop()
    elif cmd == 'restart':
        pm.restart()
    elif cmd == 'status':
        pm.status()
    else:
        print("Invaid argment")
