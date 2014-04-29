# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'portScanner.ui'
#
# Created: Tue Apr 29 18:10:30 2014
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

class Ui_portScanner(object):
    def setupUi(self, portScanner):
        portScanner.setObjectName(_fromUtf8("portScanner"))
        portScanner.resize(372, 389)
        portScanner.setMinimumSize(QtCore.QSize(372, 389))
        portScanner.setMaximumSize(QtCore.QSize(372, 389))
        self.hostLabel = QtGui.QLabel(portScanner)
        self.hostLabel.setGeometry(QtCore.QRect(20, 30, 61, 16))
        self.hostLabel.setObjectName(_fromUtf8("hostLabel"))
        self.hostLineEdit = QtGui.QLineEdit(portScanner)
        self.hostLineEdit.setGeometry(QtCore.QRect(80, 30, 171, 20))
        self.hostLineEdit.setObjectName(_fromUtf8("hostLineEdit"))
        self.portFromSpinBox = QtGui.QSpinBox(portScanner)
        self.portFromSpinBox.setGeometry(QtCore.QRect(110, 70, 42, 22))
        self.portFromSpinBox.setMinimum(20)
        self.portFromSpinBox.setMaximum(65535)
        self.portFromSpinBox.setObjectName(_fromUtf8("portFromSpinBox"))
        self.portToSpinBox = QtGui.QSpinBox(portScanner)
        self.portToSpinBox.setGeometry(QtCore.QRect(210, 70, 42, 22))
        self.portToSpinBox.setMinimum(21)
        self.portToSpinBox.setMaximum(65536)
        self.portToSpinBox.setObjectName(_fromUtf8("portToSpinBox"))
        self.fromLabel = QtGui.QLabel(portScanner)
        self.fromLabel.setGeometry(QtCore.QRect(20, 70, 81, 16))
        self.fromLabel.setObjectName(_fromUtf8("fromLabel"))
        self.toLabel = QtGui.QLabel(portScanner)
        self.toLabel.setGeometry(QtCore.QRect(170, 70, 31, 16))
        self.toLabel.setObjectName(_fromUtf8("toLabel"))
        self.scanPushButton = QtGui.QPushButton(portScanner)
        self.scanPushButton.setGeometry(QtCore.QRect(290, 30, 75, 23))
        self.scanPushButton.setObjectName(_fromUtf8("scanPushButton"))
        self.resultTable = QtGui.QTableWidget(portScanner)
        self.resultTable.setGeometry(QtCore.QRect(10, 110, 351, 271))
        self.resultTable.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.resultTable.setTabKeyNavigation(False)
        self.resultTable.setProperty("showDropIndicator", False)
        self.resultTable.setDragDropOverwriteMode(False)
        self.resultTable.setAlternatingRowColors(True)
        self.resultTable.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.resultTable.setObjectName(_fromUtf8("resultTable"))
        self.resultTable.setColumnCount(2)
        self.resultTable.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.resultTable.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.resultTable.setHorizontalHeaderItem(1, item)
        self.resultTable.horizontalHeader().setStretchLastSection(True)
        self.resultTable.verticalHeader().setVisible(False)
        self.stopPushButton = QtGui.QPushButton(portScanner)
        self.stopPushButton.setGeometry(QtCore.QRect(290, 60, 75, 23))
        self.stopPushButton.setObjectName(_fromUtf8("stopPushButton"))
        self.statusLabel = QtGui.QLabel(portScanner)
        self.statusLabel.setGeometry(QtCore.QRect(265, 90, 91, 20))
        self.statusLabel.setText(_fromUtf8(""))
        self.statusLabel.setObjectName(_fromUtf8("statusLabel"))
        self.hostLabel.setBuddy(self.hostLineEdit)

        self.retranslateUi(portScanner)
        QtCore.QMetaObject.connectSlotsByName(portScanner)

    def retranslateUi(self, portScanner):
        portScanner.setWindowTitle(_translate("portScanner", "Port Scanner - Nuts and Bolts", None))
        self.hostLabel.setText(_translate("portScanner", "&Host / IP :", None))
        self.hostLineEdit.setPlaceholderText(_translate("portScanner", "Enter Hostname or IP Address", None))
        self.fromLabel.setText(_translate("portScanner", "Port No from :", None))
        self.toLabel.setText(_translate("portScanner", "to :", None))
        self.scanPushButton.setText(_translate("portScanner", "Scan", None))
        item = self.resultTable.horizontalHeaderItem(0)
        item.setText(_translate("portScanner", "Port No", None))
        item = self.resultTable.horizontalHeaderItem(1)
        item.setText(_translate("portScanner", "Status", None))
        self.stopPushButton.setText(_translate("portScanner", "Stop", None))

