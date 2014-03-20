import sys
import time
from PySide.QtCore import *
from PySide.QtGui import *

from ui_pingmainwindow import Ui_MainWindow

class MainWindow(QMainWindow,Ui_MainWindow ):
    def __init__(self, parent= None):
        super(MainWindow, self).__init__(parent)

        self.setupUi(self)

    def enableBtn(self):
        if self.hostLineEdit is not '':
            self.pingBtn.enabled(True)
            self.saveBtn.enabled(True)
            self.defaultsBtn.enabled(True)



def main():
    app = QApplication(sys.argv)
    form = MainWindow()
    form.show()
    app.exec_()