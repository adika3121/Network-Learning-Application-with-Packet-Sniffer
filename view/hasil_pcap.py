# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hasil_pcap.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_hasil_sniff(object):

    # def __init__(self,file_name):
    #     self.file_name = file_name

    def setupUi(self, hasil_sniff):
        hasil_sniff.setObjectName("hasil_sniff")
        hasil_sniff.resize(776, 600)
        self.centralwidget = QtWidgets.QWidget(hasil_sniff)
        self.centralwidget.setObjectName("centralwidget")
        self.hasilSniffing_label = QtWidgets.QLabel(self.centralwidget)
        self.hasilSniffing_label.setGeometry(QtCore.QRect(266, 60, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.hasilSniffing_label.setFont(font)
        self.hasilSniffing_label.setScaledContents(False)
        self.hasilSniffing_label.setObjectName("hasilSniffing_label")
        self.nameFile_label = QtWidgets.QLabel(self.centralwidget)
        self.nameFile_label.setGeometry(QtCore.QRect(400, 60, 101, 31))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.nameFile_label.setFont(font)
        self.nameFile_label.setObjectName("nameFile_label")
        self.pcap_table = QtWidgets.QTableWidget(self.centralwidget)
        self.pcap_table.setEnabled(True)
        self.pcap_table.setGeometry(QtCore.QRect(50, 110, 681, 401))
        self.pcap_table.setColumnCount(6)
        self.pcap_table.setObjectName("pcap_table")
        self.pcap_table.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.pcap_table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.pcap_table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.pcap_table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.pcap_table.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.pcap_table.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.pcap_table.setHorizontalHeaderItem(5, item)
        self.penjelasanBtn = QtWidgets.QPushButton(self.centralwidget)
        self.penjelasanBtn.setGeometry(QtCore.QRect(300, 520, 131, 31))
        self.penjelasanBtn.setObjectName("penjelasanBtn")
        hasil_sniff.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(hasil_sniff)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 776, 22))
        self.menubar.setObjectName("menubar")
        hasil_sniff.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(hasil_sniff)
        self.statusbar.setObjectName("statusbar")
        hasil_sniff.setStatusBar(self.statusbar)

        self.retranslateUi(hasil_sniff)
        QtCore.QMetaObject.connectSlotsByName(hasil_sniff)

    def retranslateUi(self, hasil_sniff):
        _translate = QtCore.QCoreApplication.translate
        hasil_sniff.setWindowTitle(_translate("hasil_sniff", "Hasil Sniffing"))
        self.hasilSniffing_label.setText(_translate("hasil_sniff", "Hasil Sniffing "))
        self.nameFile_label.setText(_translate("hasil_sniff", "File.pcap"))
        item = self.pcap_table.horizontalHeaderItem(0)
        item.setText(_translate("hasil_sniff", "No"))
        item = self.pcap_table.horizontalHeaderItem(1)
        item.setText(_translate("hasil_sniff", "Waktu"))
        item = self.pcap_table.horizontalHeaderItem(2)
        item.setText(_translate("hasil_sniff", "Sumber"))
        item = self.pcap_table.horizontalHeaderItem(3)
        item.setText(_translate("hasil_sniff", "Tujuan"))
        item = self.pcap_table.horizontalHeaderItem(4)
        item.setText(_translate("hasil_sniff", "Panjang Frame"))
        item = self.pcap_table.horizontalHeaderItem(5)
        item.setText(_translate("hasil_sniff", "Keterangan"))
        self.penjelasanBtn.setText(_translate("hasil_sniff", "Penjelasan"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    hasil_sniff = QtWidgets.QMainWindow()
    ui = Ui_hasil_sniff()
    ui.setupUi(hasil_sniff)
    hasil_sniff.show()
    sys.exit(app.exec_())
