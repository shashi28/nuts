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

class PackMon(QThread):
    def __init__(self,parent = None):
        super(PackMon,self).__init__(parent)

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

    def sniff(self):
        with Handle(filter=self.filter,layer=Layer.NETWORK,priority=0,flags=Flag.SNIFF) as handle:
            while True:
                rawdata = handle.recv()
                self.pkt = self.dev.parse_packet(rawdata)
                info = self.calcInfo()
                protocol = self.calcProtocol()
                self.emit(SIGNAL('tableinput(QString,QString,QString,QString,QString)'),str(self.pkt.src_addr),str(self.pkt.dst_addr),str(protocol),str(info),str(self.pkt))

    def calcInfo(self):
        info = ''
        if self.pkt.meta.is_outbound():
            info = info + 'OUT '
        else:
            info = info + 'IN '

        info = info + str(self.pkt.src_port) + ' > ' + str(self.pkt.dst_port)
        if self.pkt.tcp_hdr is not None and self.pkt is not None:
            if self.pkt.tcp_hdr.Ack == 1 :
                info = info + '[ACK] '
            if self.pkt.tcp_hdr.Syn == 1 :
                info = info + '[SYN] '
            if self.pkt.tcp_hdr.Psh  == 1:
                info = info + '[PSH] '
            if self.pkt.tcp_hdr.Rst == 1:
                info = info + '[RST] '
            if self.pkt.tcp_hdr.Fin == 1:
                info = info + '[FIN] '
            if self.pkt.tcp_hdr.Urg == 1:
                info = info + '[URG] '

            info = info + 'seq = ' + str(self.pkt.tcp_hdr.SeqNum)
            info = info + ' window = ' + str(self.pkt.tcp_hdr.Window)
        if self.pkt.ipv4_hdr is not None:
            info = info + ' len = '+ str(self.pkt.ipv4_hdr.Length)

        return info

    def calcProtocol(self):
        if self.pkt.ipv4_hdr is not None:
            if self.pkt.ipv4_hdr.Protocol == 1:
                return 'icmp'
            elif self.pkt.ipv4_hdr.Protocol ==  6:
                return 'tcp'
            elif self.pkt.ipv4_hdr.Protocol == 17:
                return 'udp'

    def run(self):
        self.sniff()
        self.exec_()

    def setFilter(self,filtr):
        self.filter = str(filtr)
