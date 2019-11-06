# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'deleteByKeyWindow.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DeleteKeyDialog(object):
    def setupUi(self, DeleteKeyDialog):
        DeleteKeyDialog.setObjectName("DeleteKeyDialog")
        DeleteKeyDialog.resize(800, 450)
        DeleteKeyDialog.setMinimumSize(QtCore.QSize(800, 450))
        DeleteKeyDialog.setMaximumSize(QtCore.QSize(800, 450))
        self.label = QtWidgets.QLabel(DeleteKeyDialog)
        self.label.setGeometry(QtCore.QRect(300, 10, 241, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(DeleteKeyDialog)
        self.label_2.setGeometry(QtCore.QRect(230, 150, 391, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.idEdit = QtWidgets.QLineEdit(DeleteKeyDialog)
        self.idEdit.setGeometry(QtCore.QRect(330, 250, 181, 22))
        self.idEdit.setObjectName("idEdit")
        self.line = QtWidgets.QFrame(DeleteKeyDialog)
        self.line.setGeometry(QtCore.QRect(0, 50, 801, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.splitter = QtWidgets.QSplitter(DeleteKeyDialog)
        self.splitter.setGeometry(QtCore.QRect(580, 400, 186, 28))
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.okButton = QtWidgets.QPushButton(self.splitter)
        self.okButton.setEnabled(True)
        self.okButton.setDefault(True)
        self.okButton.setObjectName("okButton")
        self.cancelButton = QtWidgets.QPushButton(self.splitter)
        self.cancelButton.setObjectName("cancelButton")
        self.label_2.setBuddy(self.idEdit)

        self.retranslateUi(DeleteKeyDialog)
        QtCore.QMetaObject.connectSlotsByName(DeleteKeyDialog)

    def retranslateUi(self, DeleteKeyDialog):
        _translate = QtCore.QCoreApplication.translate
        DeleteKeyDialog.setWindowTitle(_translate("DeleteKeyDialog", "Deleting record by the key"))
        self.label.setText(_translate("DeleteKeyDialog", "Deleting record by key"))
        self.label_2.setText(_translate("DeleteKeyDialog", "Enter the id of the record you would like to delete:"))
        self.okButton.setText(_translate("DeleteKeyDialog", "Ok"))
        self.cancelButton.setText(_translate("DeleteKeyDialog", "Cancel"))
