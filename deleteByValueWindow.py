# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'deleteByValueWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DeleteByValueDialog(object):
    def setupUi(self, DeleteByValueDialog):
        DeleteByValueDialog.setObjectName("DeleteByValueDialog")
        DeleteByValueDialog.resize(800, 450)
        DeleteByValueDialog.setMinimumSize(QtCore.QSize(800, 450))
        DeleteByValueDialog.setMaximumSize(QtCore.QSize(800, 450))
        self.label = QtWidgets.QLabel(DeleteByValueDialog)
        self.label.setGeometry(QtCore.QRect(320, 20, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(DeleteByValueDialog)
        self.line.setGeometry(QtCore.QRect(0, 60, 801, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.splitter = QtWidgets.QSplitter(DeleteByValueDialog)
        self.splitter.setGeometry(QtCore.QRect(580, 400, 186, 28))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.okButton = QtWidgets.QPushButton(self.splitter)
        self.okButton.setEnabled(True)
        self.okButton.setDefault(True)
        self.okButton.setObjectName("okButton")
        self.cancelButton = QtWidgets.QPushButton(self.splitter)
        self.cancelButton.setObjectName("cancelButton")
        self.splitter_3 = QtWidgets.QSplitter(DeleteByValueDialog)
        self.splitter_3.setGeometry(QtCore.QRect(190, 270, 451, 24))
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName("splitter_3")
        self.label_3 = QtWidgets.QLabel(self.splitter_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.valueEdit = QtWidgets.QLineEdit(self.splitter_3)
        self.valueEdit.setObjectName("valueEdit")
        self.label_2 = QtWidgets.QLabel(DeleteByValueDialog)
        self.label_2.setGeometry(QtCore.QRect(270, 120, 271, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.splitter_2 = QtWidgets.QSplitter(DeleteByValueDialog)
        self.splitter_2.setGeometry(QtCore.QRect(150, 190, 541, 25))
        self.splitter_2.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_2.setObjectName("splitter_2")
        self.serialNameBox = QtWidgets.QCheckBox(self.splitter_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.serialNameBox.setFont(font)
        self.serialNameBox.setObjectName("serialNameBox")
        self.numSeriesBox = QtWidgets.QCheckBox(self.splitter_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.numSeriesBox.setFont(font)
        self.numSeriesBox.setObjectName("numSeriesBox")
        self.isWatchedBox = QtWidgets.QCheckBox(self.splitter_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.isWatchedBox.setFont(font)
        self.isWatchedBox.setObjectName("isWatchedBox")
        self.label_3.setBuddy(self.valueEdit)

        self.retranslateUi(DeleteByValueDialog)
        QtCore.QMetaObject.connectSlotsByName(DeleteByValueDialog)

    def retranslateUi(self, DeleteByValueDialog):
        _translate = QtCore.QCoreApplication.translate
        DeleteByValueDialog.setWindowTitle(_translate("DeleteByValueDialog", "Deleting by value"))
        self.label.setText(_translate("DeleteByValueDialog", "Deleting by value"))
        self.okButton.setText(_translate("DeleteByValueDialog", "Ok"))
        self.cancelButton.setText(_translate("DeleteByValueDialog", "Cancel"))
        self.label_3.setText(_translate("DeleteByValueDialog", "Enter the value of deleting:"))
        self.label_2.setText(_translate("DeleteByValueDialog", "Choose only one of them!!!"))
        self.serialNameBox.setText(_translate("DeleteByValueDialog", "serial_name"))
        self.numSeriesBox.setText(_translate("DeleteByValueDialog", "number_of_series"))
        self.isWatchedBox.setText(_translate("DeleteByValueDialog", "is_watched"))
