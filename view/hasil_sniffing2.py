# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hasil_sniffing2.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
import mysql
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget

from controller.db_connector import run_sql_all

from view.hasil_detail2 import Ui_hasil_detail2


class Ui_hasil_sniffing2(object):

    # def loadData(self, id_hasil):
    #     result = run_sql_all("SELECT hasil_jadi, waktu FROM tb_det_hasil WHERE id_tb_hasil = '%s'" %(id_hasil[0]))
    #     print(id_hasil)
    #     self.tableWidget.setRowCount(0)
    #     self.tableWidget.setColumnCount(4)
    #
    #
    #     self.detailButton = []
    #
    #     # self.detailButton = QtWidgets.QPushButton(self.centralwidget)
    #     # self.detailButton.setObjectName("detailButton")
    #     # self.detailButton.setGeometry(QtCore.QRect(200, 150, 93, 28))
    #
    #     # _translate = QtCore.QCoreApplication.translate
    #     # self.detailButton.setText(_translate("Hasil_sniffing", "Detail"))
    #     i = 0
    #     for row_number, row_data in enumerate(result):
    #         self.detailButton.append(row_number)
    #         self.detailButton[i] = QtWidgets.QPushButton(self.centralwidget)
    #         self.detailButton[i].setObjectName("detailButton")
    #
    #         self.detailButton[i].setGeometry(QtCore.QRect(200, 150, 93, 28))
    #
    #         self.tableWidget.insertRow(row_number)
    #         for column_number, data in enumerate(row_data):
    #             self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
    #             self.tableWidget.setCellWidget(row_number, 3, self.detailButton[i])
    #
    #         i+=1

    def setupUi(self, hasil_sniffing2, id_hasil):
        hasil_sniffing2.setObjectName("hasil_sniffing2")
        hasil_sniffing2.resize(800, 600)
        qss_file = open('../resource/style.qss').read()
        hasil_sniffing2.setStyleSheet(qss_file)
        self.centralwidget = QtWidgets.QWidget(hasil_sniffing2)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(-1, 20, -1, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Lato Heavy")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(30, 40, 30, 20)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setRowCount(0)
        self.tableWidget.setColumnCount(4)



        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)

        # # menerima hasil
        # result = run_sql_all("SELECT id_tb_det_hasil, hasil_jadi, waktu FROM tb_det_hasil WHERE id_tb_hasil = '%s'" % (id_hasil))
        # print(id_hasil)
        # print(result)
        #
        # self.detailButton = []
        #
        # # self.detailButton = QtWidgets.QPushButton(self.centralwidget)
        # # self.detailButton.setObjectName("detailButton")
        # # self.detailButton.setGeometry(QtCore.QRect(200, 150, 93, 28))
        #
        # # _translate = QtCore.QCoreApplication.translate
        # # self.detailButton.setText(_translate("Hasil_sniffing", "Detail"))
        # i = 0
        # for row_number, row_data in enumerate(result):
        #     self.detailButton.append(row_number)
        #
        #
        #     self.tableWidget.insertRow(row_number)
        #     for column_number, data in enumerate(row_data):
        #         self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        #         self.detailButton[i] = QtWidgets.QPushButton(self.centralwidget)
        #         self.detailButton[i].setObjectName("detailButton")
        #         self.detailButton[i].setStyleSheet(qss_file)
        #         self.detailButton[i].setText("Detail Paket")
        #         self.detailButton[i].clicked.connect(self.clickDetail)
        #         self.tableWidget.setCellWidget(row_number, 3, self.detailButton[i])
        #
        #     i += 1
        #
        # print(self.detailButton)

        font = QtGui.QFont()
        font.setFamily("Lato Heavy")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        self.tableWidget.setColumnHidden(0,True)

        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)

        font = QtGui.QFont()
        font.setFamily("Lato Heavy")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)

        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)

        font = QtGui.QFont()
        font.setFamily("Lato Heavy")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)

        font = QtGui.QFont()
        font.setFamily("Lato Heavy")
        font.setPointSize(10)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(3, item)



        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)

        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.Stretch)
        # self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        # self.tableWidget.verticalHeader().setVisible(True)
        self.verticalLayout_3.addWidget(self.tableWidget)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.kembali_btn3 = QtWidgets.QPushButton(self.centralwidget)
        self.kembali_btn3.setMinimumSize(QtCore.QSize(100, 0))
        self.kembali_btn3.setStyleSheet(qss_file)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../resource/1x/Asset 2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.kembali_btn3.setIcon(icon)
        self.kembali_btn3.setObjectName("kembali_btn3")
        self.gridLayout.addWidget(self.kembali_btn3, 0, 0, 1, 1)
        self.cek_glosarium_btn = QtWidgets.QPushButton(self.centralwidget)
        self.cek_glosarium_btn.setStyleSheet(qss_file)
        self.cek_glosarium_btn.setObjectName("cek_glosarium_btn")
        self.gridLayout.addWidget(self.cek_glosarium_btn, 0, 2, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        hasil_sniffing2.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(hasil_sniffing2)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        hasil_sniffing2.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(hasil_sniffing2)
        self.statusbar.setObjectName("statusbar")
        hasil_sniffing2.setStatusBar(self.statusbar)

        self.retranslateUi(hasil_sniffing2)
        QtCore.QMetaObject.connectSlotsByName(hasil_sniffing2)

    def retranslateUi(self, hasil_sniffing2):
        _translate = QtCore.QCoreApplication.translate
        hasil_sniffing2.setWindowTitle(_translate("hasil_sniffing2", "Hasil Sniffing"))
        self.label.setText(_translate("hasil_sniffing2", "Hasil Sniffing"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("hasil_sniffing2", "Hasil"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("hasil_sniffing2", "Waktu"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("hasil_sniffing2", "Detail Paket"))
        self.kembali_btn3.setText(_translate("hasil_sniffing2", "Kembali"))
        self.cek_glosarium_btn.setText(_translate("hasil_sniffing2", "Bingung arti setiap kata? Cek Glosarium"))


    def clickDetail(self):
        print("Ini sudah klik detail")
        if self.tableWidget.currentIndex():
            index = self.tableWidget.currentIndex().row()
            print("ini di kelas sa")
            id = self.tableWidget.item(index,0)
            id_det_hasil = id.text()
            print(id_det_hasil)
            # Buka Window baru
            self.window = QtWidgets.QMainWindow()
            self.ui = Ui_hasil_detail2()
            self.ui.setupUi(self.window, id_det_hasil)
            self.window.show()
            # db_id = self.tableWidget.index.value("Waktu")
            # return db_id

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    hasil_sniffing2 = QtWidgets.QMainWindow()
    ui = Ui_hasil_sniffing2()
    ui.setupUi(hasil_sniffing2)
    hasil_sniffing2.show()
    sys.exit(app.exec_())
