# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'firebolt.ui'
#
# Created: Mon Apr 21 02:47:18 2014
#      by: PyQt4 UI code generator 4.10.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(561, 510)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 63, 41, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.lineEdit = QtGui.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(110, 60, 271, 20))
        self.lineEdit.setObjectName(_fromUtf8("lineEdit"))
        self.startBtn = QtGui.QPushButton(self.centralwidget)
        self.startBtn.setGeometry(QtCore.QRect(40, 20, 75, 23))
        self.startBtn.setObjectName(_fromUtf8("startBtn"))
        self.stopBtn = QtGui.QPushButton(self.centralwidget)
        self.stopBtn.setGeometry(QtCore.QRect(240, 20, 75, 23))
        self.stopBtn.setObjectName(_fromUtf8("stopBtn"))
        self.restartBtn = QtGui.QPushButton(self.centralwidget)
        self.restartBtn.setGeometry(QtCore.QRect(440, 20, 75, 23))
        self.restartBtn.setObjectName(_fromUtf8("restartBtn"))
        self.filterBtn = QtGui.QPushButton(self.centralwidget)
        self.filterBtn.setGeometry(QtCore.QRect(410, 60, 75, 23))
        self.filterBtn.setObjectName(_fromUtf8("filterBtn"))
        self.tableWidget = QtGui.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 103, 541, 192))
        self.tableWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(8)
        self.tableWidget.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        item = QtGui.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, item)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.plainTextEdit = QtGui.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 313, 541, 191))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(36, 80, 491, 31))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.line_2 = QtGui.QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(35, 290, 491, 31))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.label.setBuddy(self.lineEdit)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.startBtn, self.stopBtn)
        MainWindow.setTabOrder(self.stopBtn, self.restartBtn)
        MainWindow.setTabOrder(self.restartBtn, self.lineEdit)
        MainWindow.setTabOrder(self.lineEdit, self.filterBtn)
        MainWindow.setTabOrder(self.filterBtn, self.tableWidget)
        MainWindow.setTabOrder(self.tableWidget, self.plainTextEdit)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "FireBolt", None))
        self.label.setText(_translate("MainWindow", "Filter :", None))
        self.startBtn.setText(_translate("MainWindow", "START", None))
        self.stopBtn.setText(_translate("MainWindow", "STOP", None))
        self.restartBtn.setText(_translate("MainWindow", "RESTART", None))
        self.filterBtn.setText(_translate("MainWindow", "Set Filter", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Status", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Time", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Src IP Addr", None))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Dest IP Addr", None))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Protocol", None))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Src Port", None))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Dst Port", None))
        item = self.tableWidget.horizontalHeaderItem(7)
        item.setText(_translate("MainWindow", "Full Packet", None))

