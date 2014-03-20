import sys
import time
from PySide.QtCore import *
from PySide.QtGui import *

import ui_pingmainwindow

class MainWindow(QMainWindow, ui_pingmainwindow.Ui_MainWindow ):
    def __init__(self, parent= None):
        super(MainWindow, self).__init__(parent)

        self.connect(self.hostLineEdit, SIGNAL('text()'), self.enableBtn())

        self.setupUi(self)

    def enableBtn(self):
        self.pingBtn.enabled(True)
        self.saveBtn.enabled(True)
        self.defaultsBtn.enabled(True)



def main():
    app = QApplication(sys.argv)
    form = MainWindow()
    form.show()
    app.exec_()