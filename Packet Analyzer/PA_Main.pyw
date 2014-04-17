import sys
import pcapy
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import ui_packetAnalyzer
import pcapy
import packSniff

class MainWindow(QMainWindow, ui_packetAnalyzer.Ui_MainWindow):
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.sniffThread_o = packSniff.Sniffer()

        devices = pcapy.findalldevs()
        for d in devices :
            self.comboBox.addItem(d)
        self.connect(self.captureBtn,SIGNAL('clicked()'),self.handle_cap)
        self.connect(self.stopBtn,SIGNAL('clicked()'),self.handle_stop)
        self.connect(self.sniffThread_o,SIGNAL('MAC(QString,QString,Qstring)'),self.handle_MAC)
        self.connect(self.sniffThread_o,SIGNAL('IP(QString,QString,QString,QString,QString,QString'),self.handle_IP)
        self.connect(self.sniffThread_o,SIGNAL('TCP(QString,QString,QString,QString,QString)'), self.handle_TCP)
        self.connect(self.sniffThread_o,SIGNAL('ICMP(QString,QString,QString)'),self.handle_ICMP)
        self.connect(self.sniffThread_o,SIGNAL('UDP(QString,QString,QString,QString)'),self.handle_UDP)


    def handle_cap(self):
        if self.comboBox.currentText() is None:
            QMessageBox.warning(self,'Interface Error!', 'No Interfaces Found !')
        else:
            self.sniffThread_o.BtnClicked_Slot(self.comboBox.currentText())
            self.sniffThread_o.start()

    def handle_stop(self):
        if self.sniffThread_o.isRunning():
            self.sniffThread_o.exit()
            qDebug('Thread Stopped')
        elif self.sniffThread_o.isFinished():
            QMessageBox.warning(self,'Finished', 'Aready Finished Sniffing')

    def handle_MAC(self,des,sou,pro):
        dest = str(des)
        source = str(sou)
        prot = str(pro)

    def handle_IP(self,ver,ip,ttl,pro,source,des):
        version = str(ver)
        ip_head_len = str(ip)
        TTL = str(ttl)
        protocol = str(pro)
        source_ip = str(source)
        dest_ip = str(des)

    def handle_TCP(self,Source_Port,Dest_Port,Sequence_Number,Acknowledgement,TCP_header_length):
        str(Source_Port)
        str(Dest_Port)
        str(Sequence_Number)
        str(Acknowledgement)
        str(TCP_header_length)

    def handle_ICMP(self,Type,Code,Checksum):
        str(Type)
        str(Code)
        str(Checksum)

    def handle_UDP(self,Source_Port,Dest_Port,Code,Checksum):
        str(Source_Port)
        str(Dest_Port)
        str(Code)
        str(Checksum)

app = QApplication(sys.argv)
form = MainWindow()
form.show()
app.exec_()
