from sys import *
from getopt import *
from os import *
import signal
import sys
import os
import types
import datetime
import re, time, csv
import OpenOPC
import Pyro4

opc_class = 'Matrikon.OPC.Automation;Graybox.OPC.DAWrapper;HSCOPC.Automation;RSI.OPCAutomation;OPC.Automation'
client_name = 'OpenOPC'
opc_server = 'Matrikon.OPC.Simulation.1'
opc_host = '127.0.0.1'
taglist = ['Group0.opc_01', 'Group0.opc_02', 'Group1.rule1', 'Group1.rule2','Group0.sg1', 'Group0.sg2', 'Group1.sg2', 'Group1.sg1']


class SigHandler:
    def __init__(self):
        self.signaled = 0
        self.sn = None

    def __call__(self, sn, sf):
        self.sn = sn
        self.signaled += 1


# Establish signal handler for keyboard interrupts
def signalhandle():
    sh = SigHandler()
    signal.signal(signal.SIGINT, sh)
    if os.name == 'nt':
        signal.signal(signal.SIGBREAK, sh)
    signal.signal(signal.SIGTERM, sh)
    return sh


def test01():
    opc = OpenOPC.client(opc_class, client_name)
    print("###  create opc!")
    opc.connect(opc_server, opc_host)
    print("###  connect opc server:", opc_server)

    test02(opc)
    taglist_opc = opc.read(taglist)
    info_opc = opc.info()
    servers_opc = opc.servers(opc_host)
    tags = []
    data = opc.list(tags, flat=True)
    list_opc = opc.list
    list_data = list_opc(tags)

    opc.close()
    print("### close opc!")


    for i in range(len(taglist_opc)):
        (name, val, qual, time) = taglist_opc[i]
        print('name:', name)
        print('val:', val)
        print('qual:', qual)
        print('time:', time)
        print()

    print("value:", str(list(taglist_opc)))
    print("info:", str(list(info_opc)))
    print("servers:", str(list(servers_opc)))
    print("data:", str(list(data)))
    print("list:", str(list(list_data)))


def test02(opc):
    count0 = 0
    sh = signalhandle()
    while not sh.signaled:
        print("test02...    ", count0)
        data_opc = opc.read(tags=['Group0.opc_02'],
                            # group='test',
                            # size=group_size,
                            # pause=tx_pause,
                            # source=data_source,
                            update=1000,
                            # timeout=timeout,
                            # sync=sync,
                            # include_error=include_err_msg)
                            )
        print("[test02] data:", str(list(data_opc)))
        try:
            time.sleep(1)
        except IOError:
            break
        count0 += 1


def main():
    test01()


if __name__ == '__main__':
    main()