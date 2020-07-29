# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lihat_hasil_sebelumnya.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

from controller.db_connector import run_sql_all
# from controller.MainWindow import startUI_hasilSniffing


class Ui_lihat_hasil_sebelumnya(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        qss2_file = open('../resource/styleLihatHasilSebelum.qss').read()
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #90caf9, stop:1 #a6d4fa);")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMaximumSize(QtCore.QSize(16777215, 120))
        font = QtGui.QFont()
        font.setFamily("Lato Heavy")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.inputCari = QtWidgets.QLineEdit(self.frame)
        self.inputCari.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.inputCari.setObjectName("inputCari")
        self.gridLayout.addWidget(self.inputCari, 0, 0, 1, 1)
        self.cariBtn = QtWidgets.QPushButton(self.frame)
        self.cariBtn.setStyleSheet(qss2_file)
        self.cariBtn.setObjectName("cariBtn")
        self.cariBtn.setAutoDefault(True)
        # self.cariBtn.clicked.connect(self.clickCari)
        self.gridLayout.addWidget(self.cariBtn, 0, 1, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout)
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setRowCount(0)

        # # menerima hasil
        # result = run_sql_all(
        #     "SELECT id_tb_hasil, nama_hasil, tgl_n_waktu FROM tb_hasil order by tgl_n_waktu desc")
        # print(result)
        # self.tableWidget.setColumnCount(4)
        # self.tableWidget.setRowCount(0)
        #
        # self.detailButton = []
        #
        # i = 0
        # for row_number, row_data in enumerate(result):
        #     self.detailButton.append(row_number)
        #
        #     self.tableWidget.insertRow(row_number)
        #     for column_number, data in enumerate(row_data):
        #         self.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        #         self.detailButton[i] = QtWidgets.QPushButton(self.centralwidget)
        #         self.detailButton[i].setObjectName("detailButton")
        #         self.detailButton[i].setStyleSheet(qss2_file)
        #         self.detailButton[i].setText("Detail Paket")
        #         self.detailButton[i].clicked.connect(self.clickDetail)
        #         self.tableWidget.setCellWidget(row_number, 3, self.detailButton[i])
        #
        #     i += 1


        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        self.tableWidget.setColumnHidden(0, True)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        header = self.tableWidget.horizontalHeader()
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.Stretch)
        header.setSectionResizeMode(2, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(3, QtWidgets.QHeaderView.ResizeToContents)
        # self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        # self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.verticalLayout_3.addWidget(self.tableWidget)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.kembaliBtn = QtWidgets.QPushButton(self.frame)
        self.kembaliBtn.setStyleSheet(qss2_file)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../resource/1x/Asset 2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.kembaliBtn.setIcon(icon)
        self.kembaliBtn.setObjectName("kembaliBtn")
        self.horizontalLayout_2.addWidget(self.kembaliBtn)
        spacerItem = QtWidgets.QSpacerItem(650, 20, QtWidgets.QSizePolicy.Maximum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.verticalLayout.addWidget(self.frame)
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
        MainWindow.setWindowTitle(_translate("MainWindow", "Hasil Sniffing Sebelumnya"))
        self.label.setText(_translate("MainWindow", "Hasil Sniffing Tersimpan"))
        self.cariBtn.setText(_translate("MainWindow", "Cari File"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Nama File Hasil"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Waktu"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Detail"))
        self.kembaliBtn.setText(_translate("MainWindow", "Kembali"))

    # def clickDetail(self):
    #     print("klik detail")
    #     index = self.tableWidget.currentIndex().row()
    #     print("ini di kelas sa")
    #     id = self.tableWidget.item(index, 0)
    #     id_hasil = id.text()
    #
    #
    #
    # def clickCari(self):
    #     self.cariString = self.inputCari.text()
    #     print(self.cariString)




if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_lihat_hasil_sebelumnya()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
