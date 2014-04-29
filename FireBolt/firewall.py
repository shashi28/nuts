import platform
import pydivert
from pydivert.windivert import *
from pydivert.winutils import *
from pydivert.enum import *
from pydivert.models import *
from pydivert.decorators import *
from PyQt4.QtCore import *
import impacket
from impacket.ImpactDecoder import EthDecoder

version = '1.0'

class Bolt(QThread):
    def __init__(self,parent = None):
        super(Bolt,self).__init__(parent)
        self.block = True
        driver_dir = os.path.join(os.path.realpath(os.curdir), "lib", version)
        if platform.architecture()[0] == "32bit":
            driver_dir = os.path.join(driver_dir, "x86")
        else:
            driver_dir = os.path.join(driver_dir, "amd64")

        os.chdir(driver_dir)
        reg_key = r"SYSTEM\CurrentControlSet\Services\WinDivert" + version


        dll_path = os.path.join(driver_dir, "WinDivert.dll")

        self.dev = WinDivert(dll_path)
        self.dev.register()
        self.decoder = EthDecoder()

    def drop(self):
        with Handle(filter=self.filter,layer=Layer.NETWORK,priority=0,flags=0) as handle:

            while self.block:
                rawdata = handle.recv()
                self.pkt = self.dev.parse_packet(rawdata)
                protocol = self.calcProtocol()
                self.emit(SIGNAL('tableinput(QString,QString,QString,QString,QString,QString)'),str(self.pkt.src_addr),str(self.pkt.dst_addr),str(protocol),str(self.pkt.src_port),str(self.pkt.dst_port),str(self.pkt))


    def calcProtocol(self):
        if self.pkt.ipv4_hdr is not None:
            if self.pkt.ipv4_hdr.Protocol == 1:
                return 'icmp'
            elif self.pkt.ipv4_hdr.Protocol ==  6:
                return 'tcp'
            elif self.pkt.ipv4_hdr.Protocol == 17:
                return 'udp'

    def run(self):
        self.drop()
        self.exec_()

    def setFilter(self,filtr):
        self.filter = str(filtr)
        self.block = True

    def handle_slot_stop(self):
        self.block = False