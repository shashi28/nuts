import sys
import time
from PySide.QtCore import *
from PySide.QtGui import *

import ui_pingmainwindow

class MainWindow(QMainWindow, ui_pingmainwindow.Ui_MainWindow ):
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent)

        self.setupUi(self)

        self.connect(self.pingBtn, SIGNAL('clicked()'), self.checkhostformat)

    def checkhostformat(self):
        if self.hostLineEdit.text() == '':
            self.hostLineEdit.setPlaceholderText(" Hostname can not be left empty")
            self.hostLabel.setText('<font color=red>Host / IP :</font>')


app = QApplication(sys.argv)
form = MainWindow()
form.show()
app.exec_()