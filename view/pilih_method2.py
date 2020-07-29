# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'pilih_method2.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_LaluLintas_type2(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        qss_file = open('../resource/style.qss').read()
        MainWindow.setStyleSheet(qss_file)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(30, -1, 30, 150)
        self.gridLayout.setObjectName("gridLayout")
        self.file_pcap = QtWidgets.QPushButton(self.centralwidget)
        self.file_pcap.setStyleSheet(qss_file)
        self.file_pcap.setObjectName("file_pcap")
        self.gridLayout.addWidget(self.file_pcap, 0, 0, 1, 1)
        self.sniffing_langsung = QtWidgets.QPushButton(self.centralwidget)
        self.sniffing_langsung.setStyleSheet(qss_file)
        self.sniffing_langsung.setObjectName("sniffing_langsung")
        self.gridLayout.addWidget(self.sniffing_langsung, 0, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(30, -1, -1, -1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.kembali_btn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.kembali_btn.sizePolicy().hasHeightForWidth())
        self.kembali_btn.setSizePolicy(sizePolicy)
        self.kembali_btn.setMinimumSize(QtCore.QSize(90, 0))
        self.kembali_btn.setStyleSheet(qss_file)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../resource/1x/Asset 2.png"), QtGui.QIcon.Normal, QtGui.QIcon.On)
        self.kembali_btn.setIcon(icon)
        self.kembali_btn.setObjectName("kembali_btn")
        self.verticalLayout_4.addWidget(self.kembali_btn)
        self.verticalLayout_2.addLayout(self.verticalLayout_4)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Pilih Metode"))
        self.label.setText(_translate("MainWindow", "Pilih Metode Membaca Protokol"))
        self.file_pcap.setText(_translate("MainWindow", "Lihat Hasil Sebelumnya"))
        self.sniffing_langsung.setText(_translate("MainWindow", "Sniffing Langsung"))
        self.kembali_btn.setText(_translate("MainWindow", "Kembali"))


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())
