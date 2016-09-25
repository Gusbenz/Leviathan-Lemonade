#!/usr/bin/python
 # -*- coding: latin-1 -*-
import socket
from clint.textui import colored

addrs = ['rcus', 'atlus', 'bighorn', 'van-Gogh', 'db', 'fb']

for addr in addrs:
    try:
        print '|' + addr.upper() + '|' + ' ' + socket.gethostbyname(addr) + (colored.green(': ✔︎ OK!'))
    except:
        print '|' + addr.upper() + '|' + ' ' + (colored.red('✘ DOWN!'))
