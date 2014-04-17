# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'psw.ui'
#
# Created: Fri Apr 11 02:26:38 2014
#      by: pyside-uic 0.2.14 running on PySide 1.2.0
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

class Ui_portScanner(object):
    def setupUi(self, portScanner):
        portScanner.setObjectName("portScanner")
        portScanner.resize(372, 389)
        portScanner.setMinimumSize(QtCore.QSize(372, 389))
        portScanner.setMaximumSize(QtCore.QSize(372, 389))
        self.hostLabel = QtGui.QLabel(portScanner)
        self.hostLabel.setGeometry(QtCore.QRect(20, 30, 61, 16))
        self.hostLabel.setObjectName("hostLabel")
        self.hostLineEdit = QtGui.QLineEdit(portScanner)
        self.hostLineEdit.setGeometry(QtCore.QRect(80, 30, 171, 20))
        self.hostLineEdit.setObjectName("hostLineEdit")
        self.portFromSpinBox = QtGui.QSpinBox(portScanner)
        self.portFromSpinBox.setGeometry(QtCore.QRect(110, 70, 42, 22))
        self.portFromSpinBox.setMinimum(20)
        self.portFromSpinBox.setMaximum(65535)
        self.portFromSpinBox.setObjectName("portFromSpinBox")
        self.portToSpinBox = QtGui.QSpinBox(portScanner)
        self.portToSpinBox.setGeometry(QtCore.QRect(210, 70, 42, 22))
        self.portToSpinBox.setMinimum(21)
        self.portToSpinBox.setMaximum(65536)
        self.portToSpinBox.setObjectName("portToSpinBox")
        self.fromLabel = QtGui.QLabel(portScanner)
        self.fromLabel.setGeometry(QtCore.QRect(20, 70, 81, 16))
        self.fromLabel.setObjectName("fromLabel")
        self.toLabel = QtGui.QLabel(portScanner)
        self.toLabel.setGeometry(QtCore.QRect(170, 70, 31, 16))
        self.toLabel.setObjectName("toLabel")
        self.scanPushButton = QtGui.QPushButton(portScanner)
        self.scanPushButton.setGeometry(QtCore.QRect(290, 30, 75, 23))
        self.scanPushButton.setObjectName("scanPushButton")
        self.resultTable = QtGui.QTableWidget(portScanner)
        self.resultTable.setGeometry(QtCore.QRect(10, 110, 351, 271))
        self.resultTable.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.resultTable.setTabKeyNavigation(False)
        self.resultTable.setProperty("showDropIndicator", False)
        self.resultTable.setDragDropOverwriteMode(False)
        self.resultTable.setAlternatingRowColors(True)
        self.resultTable.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        self.resultTable.setObjectName("resultTable")
        self.resultTable.setColumnCount(2)
        self.resultTable.setRowCount(0)
        item = QtGui.QTableWidgetItem()
        self.resultTable.setHorizontalHeaderItem(0, item)
        item = QtGui.QTableWidgetItem()
        self.resultTable.setHorizontalHeaderItem(1, item)
        self.resultTable.horizontalHeader().setStretchLastSection(True)
        self.resultTable.verticalHeader().setVisible(False)
        self.hostLabel.setBuddy(self.hostLineEdit)

        self.retranslateUi(portScanner)
        QtCore.QMetaObject.connectSlotsByName(portScanner)

    def retranslateUi(self, portScanner):
        portScanner.setWindowTitle(QtGui.QApplication.translate("portScanner", "Port Scanner - Nuts and Bolts", None, QtGui.QApplication.UnicodeUTF8))
        self.hostLabel.setText(QtGui.QApplication.translate("portScanner", "&Host / IP :", None, QtGui.QApplication.UnicodeUTF8))
        self.hostLineEdit.setPlaceholderText(QtGui.QApplication.translate("portScanner", "Enter Hostname or IP Address", None, QtGui.QApplication.UnicodeUTF8))
        self.fromLabel.setText(QtGui.QApplication.translate("portScanner", "Port No from :", None, QtGui.QApplication.UnicodeUTF8))
        self.toLabel.setText(QtGui.QApplication.translate("portScanner", "to :", None, QtGui.QApplication.UnicodeUTF8))
        self.scanPushButton.setText(QtGui.QApplication.translate("portScanner", "Scan", None, QtGui.QApplication.UnicodeUTF8))
        self.resultTable.horizontalHeaderItem(0).setText(QtGui.QApplication.translate("portScanner", "Port No", None, QtGui.QApplication.UnicodeUTF8))
        self.resultTable.horizontalHeaderItem(1).setText(QtGui.QApplication.translate("portScanner", "Status", None, QtGui.QApplication.UnicodeUTF8))

