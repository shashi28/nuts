import sys
import time
from PyQt4.QtCore import *
from PyQt4.QtGui import *
import ui_packetAnalyzer
import packMon

class MainWindow(QMainWindow, ui_packetAnalyzer.Ui_MainWindow):
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.sniffThread = packMon.PackMon()

        self.connect(self.captureBtn,SIGNAL('clicked()'),self.handle_cap)
        self.connect(self.stopBtn,SIGNAL('clicked()'),self.handle_stop)
        self.connect(self.sniffThread,SIGNAL('tableinput(QString,QString,QString,QString,QString)'),self.setupTable)
        self.connect(self.tableWidget,SIGNAL('cellClicked(int,int)'),self.table2txt)

    def handle_cap(self):
        self.timeS = time.time()
        if self.filterLineEdit.text() == '':
            self.Filter = 'true'
        else:
            self.Filter = self.filterLineEdit.text()
        self.sniffThread.setFilter(self.Filter)

        if self.sniffThread.isRunning() == False:
            self.sniffThread.start()
        else:
            self.sniffThread.terminate()
            self.sniffThread.start()

    def handle_stop(self):
        if self.sniffThread.isRunning():
            self.sniffThread.terminate()
            #qDebug('Thread stop')
    def setupTable(self,src,dst,pro,info,pkt):
        #qDebug('inside setupTable')
        timediff = time.time()-self.timeS
        timediff = '%.3f'%timediff
        info = info+'\n'+pkt
        self.row = self.tableWidget.currentRow() + 1
        self.tableWidget.insertRow(self.row)

        tableitem = QTableWidgetItem(str(timediff))
        self.tableWidget.setItem(self.row,0,tableitem)

        tableitem = QTableWidgetItem(src)
        self.tableWidget.setItem(self.row,1,tableitem)

        tableitem = QTableWidgetItem(dst)
        self.tableWidget.setItem(self.row,2,tableitem)

        tableitem = QTableWidgetItem(pro)
        self.tableWidget.setItem(self.row,3,tableitem)

        tableitem = QTableWidgetItem(info)
        self.tableWidget.setItem(self.row,4,tableitem)

    def table2txt(self,row):
        item = self.tableWidget.item(row,4)
        data = item.text()
        self.plainTextEdit.setPlainText(data)

app = QApplication(sys.argv)
form = MainWindow()
form.show()
app.exec_()
