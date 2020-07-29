# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'input_sniffing.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
import psutil
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QRegExp
from PyQt5.QtGui import QRegExpValidator
from PyQt5.QtWidgets import QMessageBox

# from controller.sniffing import sniffing
# from controller.sniffing import sniffing


class Ui_sniffing_langsung(object):
    def setupUi(self, sniffing_langsung):
        sniffing_langsung.setObjectName("sniffing_langsung")
        sniffing_langsung.resize(800, 600)
        qss_file = open('../resource/style.qss').read()
        sniffing_langsung.setFocusPolicy(QtCore.Qt.NoFocus)
        sniffing_langsung.setStyleSheet(qss_file)
        self.centralwidget = QtWidgets.QWidget(sniffing_langsung)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(30, 30, 30, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Lato Heavy")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #90caf9, stop:1 #a6d4fa);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setContentsMargins(-1, 50, -1, 70)
        self.formLayout.setObjectName("formLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Lato Black")
        font.setPointSize(10)
        font.setBold(True)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #90caf9, stop:1 #a6d4fa);")
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.comboIface = QtWidgets.QComboBox(self.centralwidget)
        self.comboIface.setStyleSheet(qss_file)
        self.comboIface.setObjectName("comboIface")
        addrs = psutil.net_if_addrs()
        self.comboIface.addItems(addrs.keys())

        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.comboIface)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.formLayout.setItem(3, QtWidgets.QFormLayout.SpanningRole, spacerItem)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Lato Black")
        font.setPointSize(10)
        font.setBold(True)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #90caf9, stop:1 #a6d4fa);")
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.lineEdit.setObjectName("lineEdit")
        # Validasi line edit jumlah paket
        reg_ex = QRegExp("^\\d\\d?$")
        input_validator = QRegExpValidator(reg_ex, self.lineEdit)
        self.lineEdit.setValidator(input_validator)
        # ##############
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.lineEdit)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.FieldRole, self.label_4)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.formLayout.setItem(6, QtWidgets.QFormLayout.SpanningRole, spacerItem1)
        self.protokolDiSniffingLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Lato Black")
        font.setPointSize(10)
        font.setBold(True)
        self.protokolDiSniffingLabel.setFont(font)
        self.protokolDiSniffingLabel.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #90caf9, stop:1 #a6d4fa);")
        self.protokolDiSniffingLabel.setObjectName("protokolDiSniffingLabel")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.protokolDiSniffingLabel)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.arp = QtWidgets.QCheckBox(self.centralwidget)
        self.arp.setObjectName("arp")
        self.horizontalLayout.addWidget(self.arp)
        self.icmp = QtWidgets.QCheckBox(self.centralwidget)
        self.icmp.setObjectName("icmp")
        self.horizontalLayout.addWidget(self.icmp)
        self.udp_only = QtWidgets.QCheckBox(self.centralwidget)
        self.udp_only.setObjectName("udp_only")
        self.horizontalLayout.addWidget(self.udp_only)
        self.port53 = QtWidgets.QCheckBox(self.centralwidget)
        self.port53.setObjectName("port53")
        self.horizontalLayout.addWidget(self.port53)
        self.tcp_only = QtWidgets.QCheckBox(self.centralwidget)
        self.tcp_only.setObjectName("tcp_only")
        self.horizontalLayout.addWidget(self.tcp_only)
        self.DHCP_only = QtWidgets.QCheckBox(self.centralwidget)
        self.DHCP_only.setObjectName("DHCP_only")
        self.horizontalLayout.addWidget(self.DHCP_only)
        self.HTTP_only = QtWidgets.QCheckBox(self.centralwidget)
        self.HTTP_only.setObjectName("HTTP_only")
        self.horizontalLayout.addWidget(self.HTTP_only)
        self.formLayout.setLayout(7, QtWidgets.QFormLayout.FieldRole, self.horizontalLayout)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.formLayout.setItem(8, QtWidgets.QFormLayout.SpanningRole, spacerItem2)
        self.namaFileLabel = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Lato Black")
        font.setPointSize(10)
        font.setBold(True)
        self.namaFileLabel.setFont(font)
        self.namaFileLabel.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #90caf9, stop:1 #a6d4fa);")
        self.namaFileLabel.setObjectName("namaFileLabel")
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.LabelRole, self.namaFileLabel)
        self.nama_file = QtWidgets.QLineEdit(self.centralwidget)
        self.nama_file.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.nama_file.setObjectName("nama_file")
        # Validasi lineedit nama file

        reg_ex = QRegExp("^(?!.*  )(?=.*[\w-])[\w -]{1,20}$")
        input_validator = QRegExpValidator(reg_ex, self.nama_file)
        self.nama_file.setValidator(input_validator)
        self.formLayout.setWidget(10, QtWidgets.QFormLayout.FieldRole, self.nama_file)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.formLayout.setItem(13, QtWidgets.QFormLayout.LabelRole, spacerItem3)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(13, QtWidgets.QFormLayout.FieldRole, self.label_5)
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.formLayout.setItem(14, QtWidgets.QFormLayout.SpanningRole, spacerItem4)
        self.sniffing_btn = QtWidgets.QPushButton(self.centralwidget)
        self.sniffing_btn.setStyleSheet(qss_file)
        self.sniffing_btn.setObjectName("sniffing_btn")

        # self.sniffing_btn.clicked.connect(self.clicked)
        self.formLayout.setWidget(15, QtWidgets.QFormLayout.FieldRole, self.sniffing_btn)

        self.stop_sniff_btn = QtWidgets.QPushButton(self.centralwidget)
        self.stop_sniff_btn.setStyleSheet(qss_file)
        self.stop_sniff_btn.setObjectName("stop_sniff_btn")
        # self.stop_sniff_btn.clicked.connect(self.clicked)
        self.formLayout.setWidget(15, QtWidgets.QFormLayout.FieldRole, self.stop_sniff_btn)
        self.stop_sniff_btn.hide()

        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.formLayout.setLayout(15, QtWidgets.QFormLayout.LabelRole, self.horizontalLayout_2)
        self.verticalLayout_2.addLayout(self.formLayout)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.kembali_btn2 = QtWidgets.QPushButton(self.centralwidget)
        self.kembali_btn2.setStyleSheet(qss_file)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../resource/1x/Asset 2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.kembali_btn2.setIcon(icon)
        self.kembali_btn2.setObjectName("kembali_btn2")
        self.horizontalLayout_3.addWidget(self.kembali_btn2)
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.cek_glosarium_btn = QtWidgets.QPushButton(self.centralwidget)
        self.cek_glosarium_btn.setStyleSheet(qss_file)
        self.cek_glosarium_btn.setObjectName("cek_glosarium_btn")
        self.horizontalLayout_3.addWidget(self.cek_glosarium_btn)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        sniffing_langsung.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(sniffing_langsung)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 792, 21))
        self.menubar.setObjectName("menubar")
        sniffing_langsung.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(sniffing_langsung)
        self.statusbar.setObjectName("statusbar")
        sniffing_langsung.setStatusBar(self.statusbar)

        self.retranslateUi(sniffing_langsung)
        QtCore.QMetaObject.connectSlotsByName(sniffing_langsung)

    def retranslateUi(self, sniffing_langsung):
        _translate = QtCore.QCoreApplication.translate
        sniffing_langsung.setWindowTitle(_translate("sniffing_langsung", "Sniffing Langsung"))
        self.label.setText(_translate("sniffing_langsung", "Sniffing Langsung"))
        self.label_2.setText(_translate("sniffing_langsung", "Pilih Interface"))
        self.label_3.setText(_translate("sniffing_langsung", "Jumlah Paket yang Akan Di-sniffing"))
        self.label_4.setText(_translate("sniffing_langsung", "*Gunakan angka"))
        self.protokolDiSniffingLabel.setText(_translate("sniffing_langsung", "Protokol Yang Akan Di-Sniffing"))
        self.arp.setText(_translate("sniffing_langsung", "ARP"))
        self.icmp.setText(_translate("sniffing_langsung", "ICMP"))
        self.udp_only.setText(_translate("sniffing_langsung", "UDP"))
        self.port53.setText(_translate("sniffing_langsung", "DNS"))
        self.tcp_only.setText(_translate("sniffing_langsung", "TCP"))
        self.DHCP_only.setText(_translate("sniffing_langsung", "DHCP"))
        self.HTTP_only.setText(_translate("sniffing_langsung", "HTTP"))
        self.namaFileLabel.setText(_translate("sniffing_langsung", "Nama File"))
        self.label_5.setText(_translate("sniffing_langsung", "*Tentukan nama file hasil sniffing yang akan disimpan"))
        self.sniffing_btn.setText(_translate("sniffing_langsung", "Mulai Sniffing"))
        self.stop_sniff_btn.setText(_translate("sniffing_langsung", "Stop Sniffing"))
        self.kembali_btn2.setText(_translate("sniffing_langsung", "Kembali"))
        self.cek_glosarium_btn.setText(_translate("sniffing_langsung", "Bingung arti setiap kata? Cek Glosarium"))

    def clicked(self):
        kosong = ""

        # Mengambil data dari UI Sniffing Langsung
        self.in_net_iface = self.comboIface.currentText()
        print(self.in_net_iface)
        self.in_pkt_to_sniff2 = self.lineEdit.text()
        print(self.in_pkt_to_sniff2)
        self.name_file = self.nama_file.text()
        print(self.name_file)
        self.in_proto_to_sniff2 = ""
        check_one = 0

        # merubah status saat combo box dicentang
        if self.arp.isChecked():

            self.in_proto_to_sniff2 = "arp"
            if (check_one == 0):
                check_one = 1

        if self.icmp.isChecked():
            if (check_one == 0):
                check_one = 1
                self.in_proto_to_sniff2 += "icmp"
            elif (check_one == 1):
                self.in_proto_to_sniff2 += " or icmp"

        if self.port53.isChecked():
            if (check_one == 0):
                check_one = 1
                self.in_proto_to_sniff2 += "port 53"
            elif (check_one == 1):
                self.in_proto_to_sniff2 += " or port 53"
        if self.tcp_only.isChecked():
            if (check_one == 0):
                check_one = 1
                self.in_proto_to_sniff2 += "tcp"
            elif (check_one == 1):
                self.in_proto_to_sniff2 += " or tcp"
        if self.udp_only.isChecked():
            if (check_one == 0):
                check_one = 1
                self.in_proto_to_sniff2 += "udp"
            elif (check_one == 1):
                self.in_proto_to_sniff2 += " or udp"
        if self.DHCP_only.isChecked():
            if (check_one == 0):
                check_one = 1
                self.in_proto_to_sniff2 += "port 68 or port 69"
            elif (check_one == 1):
                self.in_proto_to_sniff2 += " or port 68 or port 69"
        if self.HTTP_only.isChecked():
            if (check_one == 0):
                check_one = 1
                self.in_proto_to_sniff2 += "port 80"
            elif (check_one == 1):
                self.in_proto_to_sniff2 += " or port 80"

        print(self.in_proto_to_sniff2)

        # Validasi Pop Up
        if self.lineEdit.text() == kosong:
            msg = QMessageBox()
            msg.setWindowTitle("Peringatan")
            msg.setText("Pastikan untuk mengisi jumlah paket")
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()
        elif self.nama_file.text() == kosong:
            msg = QMessageBox()
            msg.setWindowTitle("Peringatan")
            msg.setText("Pastikan untuk mengisi kolom nama file")
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()
        elif check_one == 0 :
            msg = QMessageBox()
            msg.setWindowTitle("Peringatan")
            msg.setText("Pastikan untuk memilih salah satu protokol")
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()
        else:
            print(self.in_proto_to_sniff2)
            # net_scan = sniffing(self.in_net_iface, self.in_pkt_to_sniff2, self.in_proto_to_sniff2, self.name_file)
            # net_scan.start()
            net_iface = sniffing(self.in_net_iface, self.in_pkt_to_sniff2, self.in_proto_to_sniff2, self.name_file)
            net_iface.scan_network()



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    sniffing_langsung = QtWidgets.QMainWindow()
    ui = Ui_sniffing_langsung()
    ui.setupUi(sniffing_langsung)
    sniffing_langsung.show()
    sys.exit(app.exec_())
