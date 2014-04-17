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
        self.host = self.hostLineEdit.text()
        self.start = self.portFromSpinBox.value()
        self.stop = self.portToSpinBox.value()
        self.thread = ScannerThread()

        self.connect(self.portFromSpinBox,SIGNAL('valueChanged(int)'),self.fromvaluechanged)
        self.connect(self.portToSpinBox,SIGNAL('valueChanged(int)'),self.tovaluechanged)
        self.connect(self.scanPushButton,SIGNAL('clicked()'), self.scan)
        self.connect(self , SIGNAL('t_slot(QString,int,int)'),self.thread.init_slot)
        self.connect(self.thread,SIGNAL('openPort(int)'),self.port_open)

    def scan(self):
        self.emit(SIGNAL('t_slot(QString,int,int)'),self.host,self.start,self.stop)
        self.thread.start()


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
        while self.start <= self.stop:
            self.checkport()
            self.start += 1
        self.exec_()

    def checkport(self):
        try:
            print(self.host,self.port)
            self.sd.connect((self.host, self.port))
            print('open',self.host,self.port)
            self.emit(SIGNAL('openPort(int)'),self.port)
            self.sd.close()
        except: pass

    def init_slot(self,hos,star, sto):
        qDebug('inside thread slot')
        self.host = hos
        self.start = star
        self.stop = sto

app = QApplication(sys.argv)
form = MainWindow()
form.show()
app.exec_()