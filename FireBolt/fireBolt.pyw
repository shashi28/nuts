import sys
import time
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import ui_fireBolt
import firewall

class MainWindow(QMainWindow, ui_fireBolt.Ui_MainWindow):
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.filterThread = firewall.Bolt()

        self.connect(self.startBtn,SIGNAL('clicked()'),self.handle_start)
        self.connect(self.stopBtn,SIGNAL('clicked()'),self.handle_stop)
        #self.connect(self.stopBtn,SIGNAL('clicked()'),self.filterThread.handle_slot_stop)
        self.connect(self.filterBtn,SIGNAL('clicked()'),self.handle_start)
        self.connect(self.restartBtn,SIGNAL('clicked()'),self.handle_restart)
        self.connect(self.filterThread,SIGNAL('tableinput(QString,QString,QString,QString,QString,QString)'),self.setupTable)
        self.connect(self.tableWidget,SIGNAL('cellClicked(int,int)'),self.table2txt)
        self.connect(self,SIGNAL('stopthread()'),self.filterThread.handle_slot_stop)

    def handle_start(self):
        self.timeS = time.time()
        if self.lineEdit.text() == '':
            self.Filter = 'false'
        elif self.lineEdit.text() == 'all':
            self.Filter = 'true'
        else:
            self.Filter = self.lineEdit.text()
        self.filterThread.setFilter(self.Filter)

        if self.filterThread.isRunning() == False:
            self.filterThread.start()
        else:
            self.filterThread.terminate()
            self.filterThread.start()

    def handle_stop(self):
        if self.filterThread.isRunning():
            #self.filterThread.terminate()
            self.emit(SIGNAL('stopthread()'))
            #qDebug('Thread stop')
    
    def handle_restart(self):
        self.handle_stop()
        self.handle_start()


    def setupTable(self,sip,dip,pro,sport,dport,pkt):
        #qDebug('inside setupTable')
        tm = time.strftime('%H:%M:%S')
        self.row = self.tableWidget.currentRow() + 1
        self.tableWidget.insertRow(self.row)

        tableitem = QTableWidgetItem('BLOCKED')
        self.tableWidget.setItem(self.row,0,tableitem)

        tableitem = QTableWidgetItem(tm)
        self.tableWidget.setItem(self.row,1,tableitem)

        tableitem = QTableWidgetItem(sip)
        self.tableWidget.setItem(self.row,2,tableitem)

        tableitem = QTableWidgetItem(dip)
        self.tableWidget.setItem(self.row,3,tableitem)

        tableitem = QTableWidgetItem(pro)
        self.tableWidget.setItem(self.row,4,tableitem)

        tableitem = QTableWidgetItem(sport)
        self.tableWidget.setItem(self.row,5,tableitem)

        tableitem = QTableWidgetItem(dport)
        self.tableWidget.setItem(self.row,6,tableitem)

        tableitem = QTableWidgetItem(pkt)
        self.tableWidget.setItem(self.row,7,tableitem)

    def table2txt(self,row):
        item = QTableWidgetItem
        item = self.tableWidget.item(row,7)
        data = item.text()
        self.plainTextEdit.setPlainText(data)

app = QApplication(sys.argv)
form = MainWindow()
form.show()
app.exec_()
