# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pilih_metode.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_lalulintas_type(object):
    def setupUi(self, lalulintas_type):
        lalulintas_type.setObjectName("lalulintas_type")
        lalulintas_type.resize(695, 492)
        self.centralwidget = QtWidgets.QWidget(lalulintas_type)
        self.centralwidget.setObjectName("centralwidget")
        self.file_pcap = QtWidgets.QPushButton(self.centralwidget)
        self.file_pcap.setGeometry(QtCore.QRect(180, 220, 151, 25))
        self.file_pcap.setObjectName("file_pcap")
        self.sniffing_langsung = QtWidgets.QPushButton(self.centralwidget)
        self.sniffing_langsung.setGeometry(QtCore.QRect(350, 220, 161, 25))
        self.sniffing_langsung.setObjectName("sniffing_langsung")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(180, 120, 331, 80))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label_pilih = QtWidgets.QLabel(self.frame)
        self.label_pilih.setGeometry(QtCore.QRect(60, 20, 251, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label_pilih.setFont(font)
        self.label_pilih.setObjectName("label_pilih")
        self.kembali_btn = QtWidgets.QPushButton(self.centralwidget)
        self.kembali_btn.setGeometry(QtCore.QRect(60, 370, 121, 31))
        self.kembali_btn.setObjectName("kembali_btn")
        lalulintas_type.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(lalulintas_type)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 695, 21))
        self.menubar.setObjectName("menubar")
        lalulintas_type.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(lalulintas_type)
        self.statusbar.setObjectName("statusbar")
        lalulintas_type.setStatusBar(self.statusbar)

        self.retranslateUi(lalulintas_type)
        QtCore.QMetaObject.connectSlotsByName(lalulintas_type)

    def retranslateUi(self, lalulintas_type):
        _translate = QtCore.QCoreApplication.translate
        lalulintas_type.setWindowTitle(_translate("lalulintas_type", "Pilih Metode Membaca Lalu Lintas"))
        self.file_pcap.setText(_translate("lalulintas_type", "File Pcap"))
        self.sniffing_langsung.setText(_translate("lalulintas_type", "Sniffing Langsung"))
        self.label_pilih.setText(_translate("lalulintas_type", "Pilih Metode Membaca Protocol"))
        self.kembali_btn.setText(_translate("lalulintas_type", "Kembali"))




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    lalulintas_type = QtWidgets.QMainWindow()
    ui = Ui_lalulintas_type()
    ui.setupUi(lalulintas_type)
    lalulintas_type.show()
    sys.exit(app.exec_())
