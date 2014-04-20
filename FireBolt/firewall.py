import sys
import platform
import pydivert
from pydivert.windivert import *
from pydivert.winutils import *
from pydivert.enum import *
from pydivert.models import *
from pydivert.decorators import *

version = '1.0'

class Firewall():
    def __init__(self):
        self.setUp()

    def setUp(self):
        self.driver_dir = os.path.join(os.path.realpath(os.curdir), "lib", version)
        if platform.architecture()[0] == "32bit":
            self.driver_dir = os.path.join(self.driver_dir, "x86")
        else:
            self.driver_dir = os.path.join(self.driver_dir, "amd64")

        os.chdir(self.driver_dir)
        self.reg_key = r"SYSTEM\CurrentControlSet\Services\WinDivert" + version


        self.dll_path = os.path.join(self.driver_dir, "WinDivert.dll")

        dev = WinDivert(self.dll_path)
        dev.register()
        filter = 'outbound'
        self.devInit(dev,filter)

    def devInit(self,dev,fil):
        with Handle(dev,filter = fil,layer=Layer.NETWORK,priority= 1000,flags=Flag.SNIFF) as handle:
            while True:
                rawdata = handle.recv()
                #handle.send()
                pkt = dev.parse_packet(rawdata)
                print(pkt)
                print('\n-------------\n')
                #print("{}:{}".format(pkt.dst_addr, pkt.dst_port))
                #print("{}:{}".format(pkt.src_addr, pkt.src_port))
                #print(pkt.payload)


fw = Firewall()
