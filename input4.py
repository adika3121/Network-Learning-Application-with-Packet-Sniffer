# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'input_property.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!
import os

import psutil
from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(567, 543)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.in_net_iface = QtWidgets.QTextEdit(self.centralwidget)
        self.in_net_iface.setGeometry(QtCore.QRect(400, 20, 104, 31))
        self.in_net_iface.setObjectName("in_net_iface")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 30, 131, 17))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(70, 60, 311, 51))
        self.label_2.setObjectName("label_2")
        self.in_pkt_to_sniff = QtWidgets.QTextEdit(self.centralwidget)
        self.in_pkt_to_sniff.setGeometry(QtCore.QRect(400, 70, 104, 31))
        self.in_pkt_to_sniff.setObjectName("in_pkt_to_sniff")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(70, 120, 221, 17))
        self.label_3.setObjectName("label_3")
        self.in_time_to_sniff = QtWidgets.QTextEdit(self.centralwidget)
        self.in_time_to_sniff.setGeometry(QtCore.QRect(400, 110, 104, 31))
        self.in_time_to_sniff.setObjectName("in_time_to_sniff")
        self.in_proto_sniff = QtWidgets.QGroupBox(self.centralwidget)
        self.in_proto_sniff.setGeometry(QtCore.QRect(60, 160, 441, 101))
        self.in_proto_sniff.setObjectName("in_proto_sniff")
        self.arp = QtWidgets.QRadioButton(self.in_proto_sniff)
        self.arp.setGeometry(QtCore.QRect(70, 30, 51, 23))
        self.arp.setObjectName("arp")
        self.icmp = QtWidgets.QRadioButton(self.in_proto_sniff)
        self.icmp.setGeometry(QtCore.QRect(130, 30, 61, 23))
        self.icmp.setObjectName("icmp")
        self.port53 = QtWidgets.QRadioButton(self.in_proto_sniff)
        self.port53.setGeometry(QtCore.QRect(10, 30, 51, 23))
        self.port53.setObjectName("port53")
        self.tcp_only = QtWidgets.QRadioButton(self.in_proto_sniff)
        self.tcp_only.setGeometry(QtCore.QRect(190, 30, 61, 23))
        self.tcp_only.setObjectName("tcp_only")
        self.udp_only = QtWidgets.QRadioButton(self.in_proto_sniff)
        self.udp_only.setGeometry(QtCore.QRect(240, 30, 61, 23))
        self.udp_only.setObjectName("udp_only")
        self.DHCP_only = QtWidgets.QRadioButton(self.in_proto_sniff)
        self.DHCP_only.setGeometry(QtCore.QRect(300, 30, 61, 23))
        self.DHCP_only.setObjectName("DHCP_only")
        self.HTTP_only = QtWidgets.QRadioButton(self.in_proto_sniff)
        self.HTTP_only.setGeometry(QtCore.QRect(370, 30, 61, 23))
        self.HTTP_only.setObjectName("HTTP_only")
        self.HTTP_only_2 = QtWidgets.QRadioButton(self.in_proto_sniff)
        self.HTTP_only_2.setGeometry(QtCore.QRect(130, 60, 181, 23))
        self.HTTP_only_2.setObjectName("HTTP_only_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(70, 270, 151, 17))
        self.label_4.setObjectName("label_4")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(400, 260, 104, 31))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(190, 350, 191, 25))
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.clicked)

        x = os.listdir('/sys/class/net/')
        print(x)
        # addrs = psutil.net_if_addrs()
        # print(addrs.keys())

        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(300, 20, 91, 31))
        self.comboBox.setObjectName("comboBox")

        self.comboBox.addItems(x)



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
        self.label.setText(_translate("MainWindow", "Masukan Interface"))
        self.label_2.setText(_translate("MainWindow", "Masukan Jumah Packet yang akan di-capture"))
        self.label_3.setText(_translate("MainWindow", "Masukan Lama Waktu Capture"))
        self.in_proto_sniff.setTitle(_translate("MainWindow", "Protocol yang akan Di-Capture"))
        self.arp.setText(_translate("MainWindow", "ARP"))
        self.icmp.setText(_translate("MainWindow", "ICMP"))
        self.port53.setText(_translate("MainWindow", "DNS"))
        self.tcp_only.setText(_translate("MainWindow", "TCP"))
        self.udp_only.setText(_translate("MainWindow", "UDP"))
        self.DHCP_only.setText(_translate("MainWindow", "DHCP"))
        self.HTTP_only.setText(_translate("MainWindow", "HTTP"))
        self.HTTP_only_2.setText(_translate("MainWindow", "Semua Protokol Diatas"))
        self.label_4.setText(_translate("MainWindow", "Nama File"))
        self.pushButton.setText(_translate("MainWindow", "Mulai Sniffing"))

    def clicked(self):
        XA = self.comboBox.currentText()
        print(XA)
        print(type(XA))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
