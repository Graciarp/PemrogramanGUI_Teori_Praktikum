# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'GUI_Gracia.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(804, 710)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(250, 100, 251, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setIndent(-4)
        self.label.setObjectName("label")
        self.namaEdit = QtWidgets.QLineEdit(Form)
        self.namaEdit.setGeometry(QtCore.QRect(250, 140, 251, 31))
        self.namaEdit.setObjectName("namaEdit")
        self.Halo = QtWidgets.QPushButton(Form)
        self.Halo.setGeometry(QtCore.QRect(240, 250, 82, 25))
        self.Halo.setObjectName("Halo")
        self.Clear = QtWidgets.QPushButton(Form)
        self.Clear.setGeometry(QtCore.QRect(420, 250, 82, 25))
        self.Clear.setObjectName("Clear")
        self.Keluar = QtWidgets.QPushButton(Form)
        self.Keluar.setGeometry(QtCore.QRect(330, 310, 82, 25))
        self.Keluar.setObjectName("Keluar")

        self.retranslateUi(Form)
        self.Keluar.clicked.connect(Form.close)
        self.Clear.clicked.connect(self.namaEdit.clear)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Masukkan Nama Anda"))
        self.Halo.setText(_translate("Form", "Halo"))
        self.Clear.setText(_translate("Form", "Clear"))
        self.Keluar.setText(_translate("Form", "Keluar"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
