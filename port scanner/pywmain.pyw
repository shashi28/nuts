import sys
import socket as sk

from PyQt4.QtCore import *
from PyQt4.QtGui import *

#MAX_THREADS = 50

from ui_portScanner import Ui_portScanner

class MainWindow(QMainWindow,Ui_portScanner):
    def __init__(self, parent = None):
        super(MainWindow,self).__init__(parent)
        self.setupUi(self)

        self.thread = ScannerThread()

        self.connect(self.portFromSpinBox,SIGNAL('valueChanged(int)'),self.fromvaluechanged)
        self.connect(self.portToSpinBox,SIGNAL('valueChanged(int)'),self.tovaluechanged)
        self.connect(self.scanPushButton,SIGNAL('clicked()'), self.scan)
        self.connect(self , SIGNAL('t_slot(QString,int,int)'),self.thread.init_slot)
        self.connect(self.thread,SIGNAL('openPort(int)'),self.port_open)
        self.connect(self.stopPushButton,SIGNAL('clicked()'),self.stop)
        self.connect(self, SIGNAL('setStatus(QString)'),self.status)
        self.connect(self.thread, SIGNAL('isFinished(QString)'),self.status)

    def scan(self):
        self.host = self.hostLineEdit.text()
        self.start = self.portFromSpinBox.value()
        self.stop = self.portToSpinBox.value()
        self.emit(SIGNAL('t_slot(QString,int,int)'),self.host,self.start,self.stop)
        if self.thread.isRunning():
            self.thread.terminate()
        self.thread.start()
        self.emit(SIGNAL('setStatus(QString)'),'Scanning ...')

    def stop(self):
        if self.thread.isRunning():
            self.thread.terminate()
        self.emit(SIGNAL('setStatus(QString)'),'Scan Finished !')

    def status(self,stat):
        self.statusLabel.setText(stat)

    def port_open(self, p):
        #self.resultTable.
        row = self.resultTable.currentRow()+1
        self.resultTable.insertRow(row)
        p_twi = QTableWidgetItem(str(p))
        self.resultTable.setItem(row,0,p_twi)
        s_twi = QTableWidgetItem('Open')
        self.resultTable.setItem(row,1,s_twi)


    def fromvaluechanged(self,i):
        self.start = i
        self.portToSpinBox.setValue(i)
        self.portToSpinBox.setMinimum(i)

    def tovaluechanged(self,i):
        self.stop = i

class ScannerThread(QThread):
    def __init__(self, parent=None):
        super(ScannerThread,self).__init__(parent)
        qDebug('thread generation')
        self.sd = sk.socket(sk.AF_INET, sk.SOCK_STREAM)

    def run(self):
        qDebug('inside thread run')
        while self.start_port <= self.stop_port:
            self.checkport()
            self.start_port += 1
        self.emit(SIGNAL('isFinished(QString)'),'Scan Finished !')
        self.exec_()

    def checkport(self):
        try:
            #qDebug('inside checkport')
            #print('hostname :',self.host,'Port :' , self.start_port)
            self.sd.connect((self.host, self.start_port))
            #print('open',self.host,self.start_port)
            self.emit(SIGNAL('openPort(int)'),self.start_port)
            self.sd.close()
        except: pass

    def init_slot(self,hos,star, sto):
        #qDebug('inside thread slot')
        #print(hos)
        self.host = sk.gethostbyname(str(hos))
        #print(self.host)
        self.start_port = star
        self.stop_port = sto

app = QApplication(sys.argv)
form = MainWindow()
form.show()
app.exec_()