import sys
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
        self.connect(self.sniffThread,SIGNAL('tableinput(QString,QString,QString,QString)'),self.setupTable)



    def handle_cap(self):
        if self.filterLineEdit.text() is None:
            self.Filter = 'true'
        else:
            self.Filter = self.filterLineEdit.text()
        
        self.sniffThread.setFilter(self.Filter)
        self.sniffThread.start()

    def handle_stop(self):
        if self.sniffThread.isRunning():
            self.sniffThread.exit()
            if self.sniffThread.isFinished():
                qDebug('Thread Stopped')

    def setupTable(self,src,dst,pro,info):
        self.row = self.tableWidget.rowCount()+1
        self.tableWidget.insertRow(self.row)

        tableitem = QTableWidgetItem(src)
        self.tableWidget.setItem(self.row,1,tableitem)

        tableitem = QTableWidgetItem(dst)
        self.tableWidget.setItem(self.row,2,tableitem)

        tableitem = QTableWidgetItem(pro)
        self.tableWidget.setItem(self.row,3,tableitem)

        tableitem = QTableWidgetItem(info)
        self.tableWidget.setItem(self.row,4,tableitem)




app = QApplication(sys.argv)
form = MainWindow()
form.show()
app.exec_()
