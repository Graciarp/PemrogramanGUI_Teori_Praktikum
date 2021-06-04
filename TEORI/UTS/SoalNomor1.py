# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Tugas_GraciaRizkaPasfica.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Frame(object):
    def setupUi(self, Frame):
        Frame.setObjectName("Frame")
        Frame.resize(673, 636)
        Frame.setAutoFillBackground(False)
        Frame.setStyleSheet("background-color : rgb(220, 212, 255)")
        Frame.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.label = QtWidgets.QLabel(Frame)
        self.label.setGeometry(QtCore.QRect(230, 40, 211, 16))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setTextFormat(QtCore.Qt.AutoText)
        self.label.setScaledContents(False)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Frame)
        self.label_2.setGeometry(QtCore.QRect(50, 360, 54, 14))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Frame)
        self.label_3.setGeometry(QtCore.QRect(50, 410, 61, 16))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Frame)
        self.label_4.setGeometry(QtCore.QRect(50, 460, 81, 16))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Frame)
        self.label_5.setGeometry(QtCore.QRect(50, 510, 71, 16))
        font = QtGui.QFont()
        font.setFamily("Poppins")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.tambah = QtWidgets.QPushButton(Frame)
        self.tambah.setGeometry(QtCore.QRect(270, 560, 82, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.tambah.setFont(font)
        self.tambah.setAcceptDrops(False)
        self.tambah.setStyleSheet("background-color : rgb(195, 195, 195)")
        self.tambah.setObjectName("tambah")
        self.edit = QtWidgets.QPushButton(Frame)
        self.edit.setGeometry(QtCore.QRect(360, 560, 82, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.edit.setFont(font)
        self.edit.setAcceptDrops(False)
        self.edit.setStyleSheet("background-color : rgb(195, 195, 195)")
        self.edit.setObjectName("edit")
        self.clear = QtWidgets.QPushButton(Frame)
        self.clear.setGeometry(QtCore.QRect(450, 560, 82, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.clear.setFont(font)
        self.clear.setAcceptDrops(False)
        self.clear.setStyleSheet("background-color : rgb(195, 195, 195)")
        self.clear.setObjectName("clear")
        self.hapus = QtWidgets.QPushButton(Frame)
        self.hapus.setGeometry(QtCore.QRect(540, 560, 82, 25))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.hapus.setFont(font)
        self.hapus.setAcceptDrops(False)
        self.hapus.setStyleSheet("background-color : rgb(195, 195, 195)")
        self.hapus.setObjectName("hapus")
        self.LineEditNama = QtWidgets.QLineEdit(Frame)
        self.LineEditNama.setGeometry(QtCore.QRect(160, 400, 461, 31))
        self.LineEditNama.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.LineEditNama.setObjectName("LineEditNama")
        self.LineEditNim = QtWidgets.QLineEdit(Frame)
        self.LineEditNim.setGeometry(QtCore.QRect(160, 350, 461, 31))
        self.LineEditNim.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.LineEditNim.setObjectName("LineEditNim")
        self.LineEditJurusan = QtWidgets.QLineEdit(Frame)
        self.LineEditJurusan.setGeometry(QtCore.QRect(160, 450, 461, 31))
        self.LineEditJurusan.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.LineEditJurusan.setObjectName("LineEditJurusan")
        self.LineEditTelp = QtWidgets.QLineEdit(Frame)
        self.LineEditTelp.setGeometry(QtCore.QRect(160, 500, 461, 31))
        self.LineEditTelp.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.LineEditTelp.setObjectName("LineEditTelp")
        self.LineEditTampil = QtWidgets.QLineEdit(Frame)
        self.LineEditTampil.setGeometry(QtCore.QRect(50, 80, 571, 231))
        self.LineEditTampil.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.LineEditTampil.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.LineEditTampil.setMaxLength(32755)
        self.LineEditTampil.setAlignment(QtCore.Qt.AlignCenter|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.LineEditTampil.setReadOnly(True)
        self.LineEditTampil.setObjectName("LineEditTampil")
        #   CONNECTING
        self.tambah.clicked.connect(self.addItemButtonClick)
        self.edit.clicked.connect(self.editItemButtonClick)
        self.hapus.clicked.connect(self.LineEditTampil.clear)

        self.retranslateUi(Frame)
        #   CLEAR
        self.clear.clicked.connect(self.LineEditNim.clear)
        self.clear.clicked.connect(self.LineEditNama.clear)
        self.clear.clicked.connect(self.LineEditJurusan.clear)
        self.clear.clicked.connect(self.LineEditTelp.clear)
        
        #   TAMBAH
    def addItemButtonClick(self):
        nama = self.LineEditNama.text()
        nim = self.LineEditNim.text()
        jurusan = self.LineEditJurusan.text()
        noTelp = self.LineEditTelp.text()
        self.LineEditTampil.setText("NIM : "+nim+" "
                                    "NAMA : "+nama+" "
                                    "Jurusan : "+jurusan+" "
                                    "No. Telp : "+noTelp)
        self.tambah.clicked.connect(self.LineEditNim.clear)
        self.tambah.clicked.connect(self.LineEditNama.clear)
        self.tambah.clicked.connect(self.LineEditJurusan.clear)
        self.tambah.clicked.connect(self.LineEditTelp.clear)

        #   EDIT
    def editItemButtonClick(self):
        nama = self.LineEditNama.text()
        nim = self.LineEditNim.text()
        jurusan = self.LineEditJurusan.text()
        noTelp = self.LineEditTelp.text()
        self.LineEditTampil.setText("NIM : "+nim+" "
                                    "NAMA : "+nama+" "
                                    "Jurusan : "+jurusan+" "
                                    "No. Telp : "+noTelp)

        QtCore.QMetaObject.connectSlotsByName(Frame)

    def retranslateUi(self, Frame):
        _translate = QtCore.QCoreApplication.translate
        Frame.setWindowTitle(_translate("Frame", "Frame"))
        self.label.setText(_translate("Frame", "DATA MAHASISWA"))
        self.label_2.setText(_translate("Frame", "NIM"))
        self.label_3.setText(_translate("Frame", "NAMA"))
        self.label_4.setText(_translate("Frame", "JURUSAN"))
        self.label_5.setText(_translate("Frame", "NO. TELP"))
        self.tambah.setText(_translate("Frame", "TAMBAH"))
        self.edit.setText(_translate("Frame", "EDIT"))
        self.clear.setText(_translate("Frame", "CLEAR"))
        self.hapus.setText(_translate("Frame", "HAPUS"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Frame = QtWidgets.QFrame()
    ui = Ui_Frame()
    ui.setupUi(Frame)
    Frame.show()
    sys.exit(app.exec_())