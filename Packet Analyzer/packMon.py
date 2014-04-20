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

    def sniff(self,fil):
        with Handle(filter = fil,layer=Layer.NETWORK,priority = 1000,flags =Flag.SNIFF) as handle:
            while True:
                rawdata = handle.recv()
                #handle.send()
                self.pkt = self.dev.parse_packet(rawdata)
                self.emit(SIGNAL('tableinput(QString,QString,QString,QString)'),self.pkt.src_addr,self.pkt.dst_addr,self.pkt.ipv4_hdr.Protocol,self.calcInfo())
                #print(self.pkt)
                #print('\n-------------\n')
                #print("{}:{}".format(self.pkt.dst_addr, self.pkt.dst_port))
                #print("{}:{}".format(self.pkt.src_addr, self.pkt.src_port))

    def calcInfo(self):
        info = ''
        if self.pkt.Flow == 'outbound':
            info +'OUT '
        else:
            info +'IN '

        info + self.pkt.src_port + '>' + self.pkt.dst_port

        if self.pkt.tcp_hdr.Ack :
            info + '[ACK] '
        elif self.pkt.tcp_hdr.Syn :
            info + '[SYN] '
        elif self.pkt.tcp_hdr.Psh :
            info + '[PSH] '
        elif self.pkt.tcp_hdr.Rst :
            info + '[RST] '
        elif self.pkt.tcp_hdr.Fin :
            info + '[FIN] '
        elif self.pkt.tcp_hdr.Urg :
            info + '[URG] '

        info + 'seq = ' + self.pkt.tcp_hdr.SeqNum
        info + ' window = ' + self.pkt.tcp_hdr.Window
        info + ' len = '+ self.pkt.ipv4_hdr.Length

        return info

    def run(self):
        self.sniff(self.filter)
        self.exec_()

    def setFilter(self,filtr):
        self.filter = str (filtr)
