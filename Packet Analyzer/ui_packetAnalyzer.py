# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'packetAnalyzer.ui'
#
# Created: Tue Apr 15 14:17:49 2014
#      by: PyQt4 UI code generator 4.9.1
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    _fromUtf8 = lambda s: s

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
        self.tableWidget.setColumnCount(6)
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
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(100)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.comboBox = QtGui.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(150, 20, 251, 22))
        self.comboBox.setObjectName(_fromUtf8("comboBox"))
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 101, 20))
        self.label.setObjectName(_fromUtf8("label"))
        self.captureBtn = QtGui.QPushButton(self.centralwidget)
        self.captureBtn.setGeometry(QtCore.QRect(460, 20, 91, 23))
        self.captureBtn.setObjectName(_fromUtf8("captureBtn"))
        self.stopBtn = QtGui.QPushButton(self.centralwidget)
        self.stopBtn.setGeometry(QtCore.QRect(610, 20, 75, 23))
        self.stopBtn.setObjectName(_fromUtf8("stopBtn"))
        self.line = QtGui.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(10, 330, 711, 21))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.textBrowser = QtGui.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(10, 350, 711, 241))
        self.textBrowser.setDocumentTitle(_fromUtf8(""))
        self.textBrowser.setTextInteractionFlags(QtCore.Qt.LinksAccessibleByKeyboard|QtCore.Qt.LinksAccessibleByMouse|QtCore.Qt.TextBrowserInteraction|QtCore.Qt.TextSelectableByKeyboard|QtCore.Qt.TextSelectableByMouse)
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.label.setBuddy(self.comboBox)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.captureBtn, self.stopBtn)
        MainWindow.setTabOrder(self.stopBtn, self.comboBox)
        MainWindow.setTabOrder(self.comboBox, self.tableWidget)
        MainWindow.setTabOrder(self.tableWidget, self.textBrowser)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "MainWindow", None, QtGui.QApplication.UnicodeUTF8))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(QtGui.QApplication.translate("MainWindow", "Index", None, QtGui.QApplication.UnicodeUTF8))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(QtGui.QApplication.translate("MainWindow", "Time", None, QtGui.QApplication.UnicodeUTF8))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(QtGui.QApplication.translate("MainWindow", "Source", None, QtGui.QApplication.UnicodeUTF8))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(QtGui.QApplication.translate("MainWindow", "Destination", None, QtGui.QApplication.UnicodeUTF8))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(QtGui.QApplication.translate("MainWindow", "Protocol", None, QtGui.QApplication.UnicodeUTF8))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(QtGui.QApplication.translate("MainWindow", "Data", None, QtGui.QApplication.UnicodeUTF8))
        self.label.setText(QtGui.QApplication.translate("MainWindow", "Select Interface :", None, QtGui.QApplication.UnicodeUTF8))
        self.captureBtn.setText(QtGui.QApplication.translate("MainWindow", "Capture Packets", None, QtGui.QApplication.UnicodeUTF8))
        self.stopBtn.setText(QtGui.QApplication.translate("MainWindow", "Stop Capture", None, QtGui.QApplication.UnicodeUTF8))

