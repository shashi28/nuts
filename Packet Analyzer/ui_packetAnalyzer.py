# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'packetAnalyzer.ui'
#
# Created: Mon Apr 21 01:42:15 2014
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
        MainWindow.resize(731, 600)
        MainWindow.setMinimumSize(QtCore.QSize(731, 600))
        MainWindow.setMaximumSize(QtCore.QSize(731, 600))
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tableWidget = QtGui.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(10, 80, 711, 251))
        self.tableWidget.setMinimumSize(QtCore.QSize(711, 251))
        self.tableWidget.setMaximumSize(QtCore.QSize(711, 251))
        self.tableWidget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(5)
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
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(100)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(True)
        self.captureBtn = QtGui.QPushButton(self.centralwidget)
        self.captureBtn.setGeometry(QtCore.QRect(440, 30, 91, 23))
        self.captureBtn.setObjectName(_fromUtf8("captureBtn"))
        self.stopBtn = QtGui.QPushButton(self.centralwidget)
        self.stopBtn.setGeometry(QtCore.QRect(584, 30, 81, 23))
        self.stopBtn.setObjectName(_fromUtf8("stopBtn"))
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 330, 711, 21))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 30, 41, 20))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.filterLineEdit = QtGui.QLineEdit(self.centralwidget)
        self.filterLineEdit.setGeometry(QtCore.QRect(70, 30, 311, 20))
        self.filterLineEdit.setObjectName(_fromUtf8("filterLineEdit"))
        self.plainTextEdit = QtGui.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setGeometry(QtCore.QRect(10, 350, 711, 241))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.plainTextEdit.setFont(font)
        self.plainTextEdit.setReadOnly(True)
        self.plainTextEdit.setObjectName(_fromUtf8("plainTextEdit"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.label.setBuddy(self.filterLineEdit)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.filterLineEdit, self.captureBtn)
        MainWindow.setTabOrder(self.captureBtn, self.stopBtn)
        MainWindow.setTabOrder(self.stopBtn, self.tableWidget)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "Packet Monitoring Tool", None))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Time", None))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Source", None))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Destination", None))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Protocol", None))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Info", None))
        self.captureBtn.setText(_translate("MainWindow", "Capture Packets", None))
        self.stopBtn.setText(_translate("MainWindow", "Stop Capture", None))
        self.label.setText(_translate("MainWindow", "Filter :", None))

