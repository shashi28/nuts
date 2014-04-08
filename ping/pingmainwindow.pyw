import sys
import time
import socket
from PySide.QtCore import *
from PySide.QtGui import *

import ui_pingmainwindow
import ping

hostlineedit = ''
stats = []
row = 0
col = 0

class MainWindow(QMainWindow, ui_pingmainwindow.Ui_MainWindow ):
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)

        self.setupUi(self)


        self.connect(self.pingBtn, SIGNAL('clicked()'), self.checkhostformat)


        self.mainthread = MainThread()
      #  self.statusthread = StatusThread()
        self.connect(self.mainthread, SIGNAL('setItem(int,int,QString,QString)'), self.setItem, Qt.DirectConnection)




    def checkhostformat(self):

        if self.hostLineEdit.text() == '':
            self.hostLineEdit.setPlaceholderText(" Hostname can not be left empty")
            self.hostLabel.setText('<font color=red>Host / IP :</font>')

        else:
            self.mainthread.start()
            row = self.statusTable.currentRow()+1
            col = self.statusTable.currentColumn()+1
            self.statusTable.insertRow(row)

            #stats = ping.quiet_ping(hostlineedit)
            #hostlineedit = self.hostLineEdit.text()
            pingf = ping.Ping()
            print(repr(pingf))
            stats = pingf.quiet_ping(self.hostLineEdit.text())
            self.mainthread.start()

    def setItem(self,max,min,avg,frac):
        mintwi = QTableWidgetItem(min)
        self.statusTable.setItem(1,6,mintwi)
        maxtwi = QTableWidgetItem(max)
        self.statusTable.setItem(1,7,maxtwi)
        avgtwi = QTableWidgetItem(avg)
        self.statusTable.setItem(1,8,avgtwi)



class MainThread(QThread):
    def __init__(self, parent = None):
        super(MainThread, self).__init__(parent)
    def run(self):
        stats = ping.Ping.quiet_ping(hostlineedit)



'''
class StatusThread(QThread):
    def __init__(self, parent = None):
        super(StatusThread, self).__init__(parent)

    def run(self):


        twi = []
        for i in range(8):
            twi.append(QTableWidgetItem())

            if i ==5 or i == 6 or i == 7:
                n = int(stats[i])
                s = str(n)
                twi[i].setText(s)
                #self.statusTable.setItem(row, col+i, twi[i])
                self.emit('setItem(int, int, QTableWidgetItem)', row, col+i, twi[i])
            elif stats[i] == 1:
                twi[i].setText('Finished')
                #self.statusTable.setItem(row, col+i, twi[i])
                self.emit('setItem(int, int, QTableWidgetItem)', row, col+i, twi[i])
            elif i == 2 and stats[i] == 0:
                twi[i].setText('Running')
                #self.statusTable.setItem(row, col+i, twi[i])
                self.emit('setItem(int, int, QTableWidgetItem)', row, col+i, twi[i])
            else:
                twi[i].setText(str(stats[i]))
                #self.statusTable.setItem(row, col+i, twi[i])
                self.emit('setItem(int, int, QTableWidgetItem)', row, col+i, twi[i])

'''
app = QApplication(sys.argv)
form = MainWindow()
form.show()
app.exec_()