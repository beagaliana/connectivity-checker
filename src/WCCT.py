# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'WCCT.ui'
#
# Created by: PyQt5 UI code generator 5.14.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.setEnabled(True)
        Dialog.resize(410, 329)
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        Dialog.setFont(font)
        Dialog.setMouseTracking(False)
        Dialog.setToolTipDuration(-1)
        Dialog.setWhatsThis("")
        Dialog.setStyleSheet("alternate-background-color: rgb(39, 39, 40);")
        self.Add = QtWidgets.QPushButton(Dialog)
        self.Add.setGeometry(QtCore.QRect(150, 70, 101, 32))
        self.Add.setObjectName("Add")
        self.Status = QtWidgets.QLabel(Dialog)
        self.Status.setGeometry(QtCore.QRect(20, 250, 371, 21))
        self.Status.setMaximumSize(QtCore.QSize(10000, 25))
        self.Status.setAlignment(QtCore.Qt.AlignCenter)
        self.Status.setWordWrap(False)
        self.Status.setTextInteractionFlags(QtCore.Qt.TextBrowserInteraction)
        self.Status.setObjectName("Status")
        self.Quit = QtWidgets.QPushButton(Dialog)
        self.Quit.setGeometry(QtCore.QRect(170, 280, 67, 32))
        self.Quit.setObjectName("Quit")
        self.List = QtWidgets.QComboBox(Dialog)
        self.List.setGeometry(QtCore.QRect(40, 110, 341, 31))
        self.List.setEditable(False)
        self.List.setObjectName("List")
        self.List.addItem("")
        self.List.addItem("")
        self.List.addItem("")
        self.Delete = QtWidgets.QPushButton(Dialog)
        self.Delete.setGeometry(QtCore.QRect(230, 150, 101, 32))
        self.Delete.setObjectName("Delete")
        self.Connect2 = QtWidgets.QPushButton(Dialog)
        self.Connect2.setGeometry(QtCore.QRect(70, 150, 101, 32))
        self.Connect2.setObjectName("Connect2")
        self.textwebsite = QtWidgets.QPlainTextEdit(Dialog)
        self.textwebsite.setGeometry(QtCore.QRect(40, 30, 331, 21))
        self.textwebsite.setObjectName("textwebsite")
        self.History = QtWidgets.QPushButton(Dialog)
        self.History.setGeometry(QtCore.QRect(70, 200, 101, 32))
        self.History.setObjectName("History")
        self.DeleteHistory = QtWidgets.QPushButton(Dialog)
        self.DeleteHistory.setGeometry(QtCore.QRect(220, 200, 121, 32))
        self.DeleteHistory.setObjectName("DeleteHistory")

        self.retranslateUi(Dialog)
        self.Quit.clicked.connect(Dialog.close)
        self.Delete.clicked.connect(self.List.clearEditText)
        self.Add.clicked.connect(self.textwebsite.selectAll)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "WEB CONNECTIVITY CHECKER TOOL"))
        Dialog.setStatusTip(_translate("Dialog", "Ready"))
        self.Add.setStatusTip(_translate("Dialog", "Add URL to the list"))
        self.Add.setText(_translate("Dialog", "Add"))
        self.Status.setText(_translate("Dialog", "Ready"))
        self.Quit.setText(_translate("Dialog", "Quit"))
        self.List.setCurrentText(_translate("Dialog", "www.esa.edu.agh.pl"))
        self.List.setItemText(0, _translate("Dialog", "www.esa.edu.agh.pl"))
        self.List.setItemText(1, _translate("Dialog", "www.google.com"))
        self.List.setItemText(2, _translate("Dialog", "www.facebook.com"))
        self.Delete.setText(_translate("Dialog", "Delete"))
        self.Connect2.setText(_translate("Dialog", "Connect"))
        self.History.setText(_translate("Dialog", "History"))
        self.DeleteHistory.setText(_translate("Dialog", "Delete History"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
