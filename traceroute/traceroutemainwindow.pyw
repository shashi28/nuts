import sys
import time
from PySide.QtGui import *
from PySide.QtCore import *
import ui_traceroutemainwindow

class MainWindow(QMainWindow, ui_traceroutemainwindow.Ui_tracerouteMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)

app = QApplication(sys.argv)
form = MainWindow()
form.show()
app.exec_()