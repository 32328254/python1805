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

    def _get_pid(self):
        pid = Popen('pidof %s' % self.name, stdout=PIPE, stderr=PIPE, shell=True)
        return pid.stdout.read().strip()

    def start(self):
        self._init()
        cmd = self.program + ' ' + self.args + ' ' + '- P %s.pid' % os.path.join(self.workdir, self.name)
        p = Popen(cmd, stdout=PIPE, stderr=PIPE, shell=True)
        if not p.stderr.read():  # 如果程序正常启动,err是null,if null 是条件不成立的,加上not 是条件成立.
            print("%s started successful" % self.name)

    def stop(self):
        pid = self._get_pid()
        if pid:  #有值则执行
            os.kill(int(pid),15)
            self.status()
        else:
            print("%s stoped "%self.name)

    def restart(self):
        self.stop()
        self.start()

    def status(self):
        pid = self._get_pid()
        if pid:  #有值则执行
            print("%s is runing"%self.name)
        else:
            print("%s stoped "%self.name)
    def help(self):
        print("Usage: %s [start/stop/restart/status]"%sys.argv[0])

if __name__ == '__main__':
    workdir = '/var/tmp/memcached'
    name = 'memcached'
    program = '/usr/bin/memcached'
    args = '-u memcached -p 11211 -m 64 -c 1024 -d'
    pm = Process(workdir=workdir, name=name, program=program, args=args)
    try:
        cmd = sys.argv[1]
    except IndexError:
        pm.help()
        sys.exit(1)
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
        pm.help()
