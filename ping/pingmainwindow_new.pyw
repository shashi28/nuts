import sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

import ui_pingmainwindow
import ping_new

HOSTNAME = ''
TIMEOUT = 3000
COUNT = 3
PACKET_SIZE = 64


class MainWindow(QMainWindow, ui_pingmainwindow.Ui_MainWindow ):
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)

        self.setupUi(self)
        self.ping_o = ping_new.Ping()

        # Connections for StatusTable
        self.connect(self.ping_o, SIGNAL('setStatusTableRcv(int,int,float)'), self.StatusTableRcv)
        self.connect(self.ping_o, SIGNAL('setStatusTableSnt(int,int,float)'),self.StatusTableSnt)
        self.connect(self.ping_o,SIGNAL('setHostData(QString,QString,int)'),self.HostData)
        self.connect(self.ping_o,SIGNAL('setStatus(QString)'),self.handleStatus)
        self.connect(self,SIGNAL('setStatus(QString)'),self.handleStatus)
        self.connect(self,SIGNAL('clickedBtn(QString,int,int,int)'), self.ping_o.BtnClicked_Slot)
        self.connect(self.pingBtn, SIGNAL('clicked()'), self.checkhost)
        self.connect(self.ping_o, SIGNAL('pingErr(QString)'),self.handlePingErr)
        self.connect(self,SIGNAL('pingErr(QString)'),self.handlePingErr)

        self.connect(self.stopBtn, SIGNAL('clicked()'),self.stopThread)
        self.connect(self.saveBtn,SIGNAL('clicked()'),self.saveHost)

        #Connections from settings tab
        self.connect(self.defaultsSetBtn,SIGNAL('clicked()'),self.defaultSet)
        self.connect(self.applySetBtn,SIGNAL('clicked()'),self.applySet)
        self.connect(self.saveSetBtn,SIGNAL('clicked()'),self.saveSet)

        # Connections for runTable
        self.connect(self.ping_o,SIGNAL('newPacket(QString,QString,int,int,int,int)'),self.handlePacket)

    def checkhost(self):

        if self.hostComboBox.currentText() == '':
            self.emit(SIGNAL('pingErr(QString)'),'Hostname cannot be left empty')

        elif self.ping_o.isRunning():
            None

        else:
            HOSTNAME = self.hostComboBox.currentText()
            TIMEOUT = int(self.timeoutLineEdit.text())
            COUNT = int(self.countLineEdit.text())
            PACKET_SIZE = int(self.packetsizeLineEdit.text())
            self.emit(SIGNAL('clickedBtn(QString,int,int,int)'),HOSTNAME,TIMEOUT,COUNT,PACKET_SIZE)
            self.status_row = self.statusTable.currentRow()+1
            #col = self.statusTable.currentColumn()+1
            self.statusTable.insertRow(self.status_row)
            self.ping_o.start()

    def StatusTableRcv(self,max,min,avg):
        mintwi = QTableWidgetItem(str(min))
        self.statusTable.setItem(self.status_row,7,mintwi)
        maxtwi = QTableWidgetItem(str(max))
        self.statusTable.setItem(self.status_row,8,maxtwi)
        avgtwi = QTableWidgetItem(str(avg))
        self.statusTable.setItem(self.status_row,9,avgtwi)

    def StatusTableSnt(self,p_sent,p_rcv,p_lost):
        senttwi = QTableWidgetItem(str(p_sent))
        self.statusTable.setItem(self.status_row,4,senttwi)
        rcvtwi = QTableWidgetItem(str(p_rcv))
        self.statusTable.setItem(self.status_row,5,rcvtwi)
        losttwi = QTableWidgetItem(str(p_lost))
        self.statusTable.setItem(self.status_row,6,losttwi)

    def HostData(self,hostname,ip,data_bytes):
        hosttwi = QTableWidgetItem(hostname)
        self.statusTable.setItem(self.status_row,0,hosttwi)
        iptwi = QTableWidgetItem(str(ip))
        self.statusTable.setItem(self.status_row,1,iptwi)
        p_sizetwi = QTableWidgetItem(str(data_bytes))
        self.statusTable.setItem(self.status_row,3,p_sizetwi)

    def handleStatus(self,status):
        statwi = QTableWidgetItem(status)
        self.statusTable.setItem(self.status_row,2,statwi)

    def handlePingErr(self,error):
        QMessageBox.warning(self, 'Ping Error', error)

    def stopThread(self):
        self.ping_o.terminate()
        self.emit(SIGNAL('setStatus(QString)'),'Stopped')

    def defaultSet(self):
        self.timeoutLineEdit.setText(str(TIMEOUT))
        self.countLineEdit.setText(str(COUNT))
        self.packetsizeLineEdit.setText(str(PACKET_SIZE))

    def applySet(self):
        TIMEOUT = self.timeoutLineEdit.text()
        COUNT = self.countLineEdit.text()
        PACKET_SIZE = self.packetsizeLineEdit.text()

    def saveSet(self):
        #Do the Code for saving Settings permanently
        None

    def saveHost(self):
        self.hostComboBox.addItem(self.hostComboBox.currentText())

    def handlePacket(self,host,ip,seq,data_size,ttl,delay):
        run_row = self.runTable.currentRow()+1
        self.runTable.insertRow(run_row)
        hosttwi = QTableWidgetItem(host)
        self.runTable.setItem(run_row,0,hosttwi)
        seqtwi = QTableWidgetItem(str(seq))
        self.runTable.setItem(run_row,2,seqtwi)
        iptwi = QTableWidgetItem(ip)
        self.runTable.setItem(run_row,1,iptwi)
        dstwi = QTableWidgetItem(str(data_size))
        self.runTable.setItem(run_row,3,dstwi)
        ttltwi = QTableWidgetItem(str(ttl))
        self.runTable.setItem(run_row,4,ttltwi)
        delaytwi = QTableWidgetItem(str(delay))
        self.runTable.setItem(run_row,5,delaytwi)




app = QApplication(sys.argv)
form = MainWindow()
form.show()
app.exec_()