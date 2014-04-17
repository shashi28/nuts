import sys

from PySide.QtCore import *
from PySide.QtGui import *
import ui_pingmainwindow
import ping


class MainWindow(QMainWindow, ui_pingmainwindow.Ui_MainWindow ):
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)

        self.setupUi(self)
        self.ping_o = ping.Ping()
      #  self.work_o = Work()

     #   self.work_t = WorkThread()
     #   self.ping_t = PingThread()



        #self.ping_o.moveToThread(self.wthread)

        self.connect(self.ping_o, SIGNAL('setItem(int,int,float)'), self.setitem, Qt.DirectConnection)
        self.connect(self,SIGNAL('clickedBtn(QString)'), self.ping_o.slot)
        self.connect(self,SIGNAL('clickedBtn(QString)'), self.ping_o.verbose_ping)
        self.connect(self.pingBtn, SIGNAL('clicked()'), self.checkhost)

      #  self.ping_o.moveToThread(self.ping_t)
      #  self.work_o.moveToThread(self.work_t)

    def checkhost(self):

        if self.hostLineEdit.text() == '':
            self.hostLineEdit.setPlaceholderText(" Hostname can not be left empty")
            self.hostLabel.setText('<font color=red>Host / IP :</font>')

        else:
            self.emit(SIGNAL('clickedBtn(QString)'),self.hostLineEdit.text())
            row = self.statusTable.currentRow()+1
            col = self.statusTable.currentColumn()+1
            self.statusTable.insertRow(row)
            hostnametext = self.hostLineEdit.text()

            #self.ping_o.verbose_ping(hostnametext)


            #self.ping_o.start()

    def setitem(self,max,min,avg):
        print(max)
        print(min)
        print(avg)
        mintwi = QTableWidgetItem(str(min))
        self.statusTable.setItem(0,6,mintwi)
        maxtwi = QTableWidgetItem(str(max))
        self.statusTable.setItem(1,7,maxtwi)
        avgtwi = QTableWidgetItem(str(avg))
        self.statusTable.setItem(2,8,avgtwi)



#class Work(QObject):
    #def __init__(self, parent = None):
   #     super(Work, self).__init__(parent)

  #  def tslot(self,host):
  #      self.hostname = host
 #       print(self.hostname)


#class WorkThread(QThread):
#    def __init__(self, parent = None):
#        super(WorkThread, self).__init__(parent)
 #   def run(self):
#        self.exec_()

#class PingThread(QThread):
#    def __init__(self, parent = None):
#        super(PingThread, self).__init__(parent)
#        ping_o = ping.Ping()
#        ping_o.verbose_ping(self.hostname)

 #   def run(self):
 #       self.exec_()

app = QApplication(sys.argv)
form = MainWindow()
form.show()
app.exec_()