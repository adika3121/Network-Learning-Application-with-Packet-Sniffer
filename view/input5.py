# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'input_property2.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!
import os

import psutil
from PyQt5 import QtCore, QtGui, QtWidgets

from controller.sniffing import sniffing


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(567, 543)
        font = QtGui.QFont()
        font.setPointSize(11)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 30, 131, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 60, 311, 51))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.in_pkt_to_sniff = QtWidgets.QTextEdit(self.centralwidget)
        self.in_pkt_to_sniff.setGeometry(QtCore.QRect(400, 70, 61, 31))
        self.in_pkt_to_sniff.setObjectName("in_pkt_to_sniff")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 120, 221, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.in_time_to_sniff = QtWidgets.QTextEdit(self.centralwidget)
        self.in_time_to_sniff.setGeometry(QtCore.QRect(400, 110, 61, 31))
        self.in_time_to_sniff.setObjectName("in_time_to_sniff")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(70, 300, 281, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(400, 290, 104, 31))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(190, 380, 191, 25))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.clicked)
        self.comboIface = QtWidgets.QComboBox(self.centralwidget)
        self.comboIface.setGeometry(QtCore.QRect(400, 20, 101, 31))
        self.comboIface.setObjectName("comboIface")
        # list_iface = os.listdir('/sys/class/net/')
        addrs = psutil.net_if_addrs()
        self.comboIface.addItems(addrs.keys())
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(70, 180, 431, 81))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.groupBox.setFont(font)
        self.groupBox.setObjectName("groupBox")
        self.arp = QtWidgets.QCheckBox(self.groupBox)
        self.arp.setGeometry(QtCore.QRect(20, 30, 51, 23))
        self.arp.setObjectName("arp")
        self.icmp = QtWidgets.QCheckBox(self.groupBox)
        self.icmp.setGeometry(QtCore.QRect(70, 30, 51, 23))
        self.icmp.setObjectName("icmp")
        self.port53 = QtWidgets.QCheckBox(self.groupBox)
        self.port53.setGeometry(QtCore.QRect(130, 30, 51, 23))
        self.port53.setObjectName("port53")
        self.tcp_only = QtWidgets.QCheckBox(self.groupBox)
        self.tcp_only.setGeometry(QtCore.QRect(180, 30, 51, 23))
        self.tcp_only.setObjectName("tcp_only")
        self.udp_only = QtWidgets.QCheckBox(self.groupBox)
        self.udp_only.setGeometry(QtCore.QRect(230, 30, 51, 23))
        self.udp_only.setObjectName("udp_only")
        self.DHCP_only = QtWidgets.QCheckBox(self.groupBox)
        self.DHCP_only.setGeometry(QtCore.QRect(280, 30, 61, 23))
        self.DHCP_only.setObjectName("DHCP_only")
        self.HTTP_only = QtWidgets.QCheckBox(self.groupBox)
        self.HTTP_only.setGeometry(QtCore.QRect(340, 30, 61, 23))
        self.HTTP_only.setObjectName("checkBox_7")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(470, 120, 67, 17))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_5.setFont(font)
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(70, 140, 461, 21))
        font = QtGui.QFont()
        font.setPointSize(7)
        self.label_6.setFont(font)
        self.label_6.setObjectName("label_6")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 567, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Pilih Interface"))
        self.label_2.setText(_translate("MainWindow", "Masukan Jumah Packet yang akan di-sniffing*"))
        self.label_3.setText(_translate("MainWindow", "Masukan Lama Waktu Sniffing*"))
        self.label_4.setText(_translate("MainWindow", "Nama File Penyimpan Hasil Interpretasi"))
        self.pushButton.setText(_translate("MainWindow", "Mulai Sniffing"))
        self.groupBox.setTitle(_translate("MainWindow", "Protocol yang akan dilakukan Sniffing"))
        self.arp.setText(_translate("MainWindow", "ARP"))
        self.icmp.setText(_translate("MainWindow", "ICMP"))
        self.port53.setText(_translate("MainWindow", "DNS"))
        self.tcp_only.setText(_translate("MainWindow", "TCP"))
        self.udp_only.setText(_translate("MainWindow", "UDP"))
        self.DHCP_only.setText(_translate("MainWindow", "DHCP"))
        self.HTTP_only.setText(_translate("MainWindow", "HTTP"))
        self.label_5.setText(_translate("MainWindow", "Detik"))
        self.label_6.setText(_translate("MainWindow", "*(Proses capture akan berhenti apabila salah satu dari jumlah atau lama waktu terpenuhi lebih dulu)"))

    def clicked(self):
        self.in_net_iface = self.comboIface.currentText()
        print(self.in_net_iface)
        self.in_pkt_to_sniff2 = self.in_pkt_to_sniff.toPlainText()
        self.in_time_to_sniff2 = self.in_time_to_sniff.toPlainText()
        self.name_file = self.textEdit.toPlainText()
        self.in_proto_to_sniff2 = ""

        # Inisiasi Status Combo Box
        arp_status = 0
        icmp_status = 0
        dns_status = 0
        tcp_status = 0
        udp_status = 0
        dhcp_status = 0
        http_status = 0

        check_one = 0;

        # merubah status saat combo box dicentang
        if self.arp.isChecked():

            self.in_proto_to_sniff2 = "arp"
            if(check_one == 0):
                check_one = 1

        if self.icmp.isChecked():
            if (check_one == 0):
                check_one = 1
                self.in_proto_to_sniff2 += "icmp"
            elif(check_one == 1):
                self.in_proto_to_sniff2 += " or icmp"

        if self.port53.isChecked():
            if(check_one == 0):
                check_one = 1
                self.in_proto_to_sniff2 += "port 53"
            elif(check_one == 1):
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




        net_iface = sniffing(self.in_net_iface, self.in_pkt_to_sniff2, self.in_proto_to_sniff2, self.name_file)
        net_iface.scan_network()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
