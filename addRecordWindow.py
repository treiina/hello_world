# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'addRecordWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_AddDialog(object):
    def setupUi(self, AddDialog):
        AddDialog.setObjectName("AddDialog")
        AddDialog.resize(800, 450)
        AddDialog.setMinimumSize(QtCore.QSize(0, 0))
        AddDialog.setMaximumSize(QtCore.QSize(16777215, 16777215))
        AddDialog.setWindowOpacity(2.0)
        self.label = QtWidgets.QLabel(AddDialog)
        self.label.setGeometry(QtCore.QRect(310, 20, 201, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.line = QtWidgets.QFrame(AddDialog)
        self.line.setGeometry(QtCore.QRect(0, 70, 801, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.splitter = QtWidgets.QSplitter(AddDialog)
        self.splitter.setGeometry(QtCore.QRect(580, 400, 186, 28))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.okButton = QtWidgets.QPushButton(self.splitter)
        self.okButton.setEnabled(True)
        self.okButton.setDefault(True)
        self.okButton.setObjectName("okButton")
        self.cancelButton = QtWidgets.QPushButton(self.splitter)
        self.cancelButton.setObjectName("cancelButton")
        self.splitter_2 = QtWidgets.QSplitter(AddDialog)
        self.splitter_2.setGeometry(QtCore.QRect(42, 200, 137, 45))
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.label_2 = QtWidgets.QLabel(self.splitter_2)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.idEdit = QtWidgets.QLineEdit(self.splitter_2)
        self.idEdit.setObjectName("idEdit")
        self.splitter_3 = QtWidgets.QSplitter(AddDialog)
        self.splitter_3.setGeometry(QtCore.QRect(231, 200, 137, 45))
        self.splitter_3.setOrientation(QtCore.Qt.Vertical)
        self.splitter_3.setObjectName("splitter_3")
        self.label_3 = QtWidgets.QLabel(self.splitter_3)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.serialNameEdit = QtWidgets.QLineEdit(self.splitter_3)
        self.serialNameEdit.setObjectName("serialNameEdit")
        self.splitter_4 = QtWidgets.QSplitter(AddDialog)
        self.splitter_4.setGeometry(QtCore.QRect(420, 200, 138, 45))
        self.splitter_4.setOrientation(QtCore.Qt.Vertical)
        self.splitter_4.setObjectName("splitter_4")
        self.label_4 = QtWidgets.QLabel(self.splitter_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.numSeriesEdit = QtWidgets.QLineEdit(self.splitter_4)
        self.numSeriesEdit.setObjectName("numSeriesEdit")
        self.splitter_5 = QtWidgets.QSplitter(AddDialog)
        self.splitter_5.setGeometry(QtCore.QRect(610, 200, 137, 45))
        self.splitter_5.setOrientation(QtCore.Qt.Vertical)
        self.splitter_5.setObjectName("splitter_5")
        self.label_5 = QtWidgets.QLabel(self.splitter_5)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.isWatchedEdit = QtWidgets.QLineEdit(self.splitter_5)
        self.isWatchedEdit.setObjectName("isWatchedEdit")
        self.label_2.setBuddy(self.idEdit)
        self.label_3.setBuddy(self.serialNameEdit)
        self.label_4.setBuddy(self.numSeriesEdit)
        self.label_5.setBuddy(self.isWatchedEdit)

        self.retranslateUi(AddDialog)
        QtCore.QMetaObject.connectSlotsByName(AddDialog)

    def retranslateUi(self, AddDialog):
        _translate = QtCore.QCoreApplication.translate
        AddDialog.setWindowTitle(_translate("AddDialog", "Adding new record"))
        self.label.setText(_translate("AddDialog", "Adding new record"))
        self.okButton.setText(_translate("AddDialog", "Ok"))
        self.cancelButton.setText(_translate("AddDialog", "Cancel"))
        self.label_2.setText(_translate("AddDialog", "id:"))
        self.label_3.setText(_translate("AddDialog", "serial_name:"))
        self.label_4.setText(_translate("AddDialog", "number_of_series:"))
        self.label_5.setText(_translate("AddDialog", "is_watched:"))
