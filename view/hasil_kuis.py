# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hasil_kuis.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

from controller.check_soal import check_soal
from controller.db_connector import run_sql


class Ui_UI_hasil_kuis(object):
    def setupUi(self, UI_hasil_kuis, hasil_nilai):
        self.skor_kuis = hasil_nilai[0]
        self.index_soal = hasil_nilai[1]
        self.jawaban_user = hasil_nilai[2]
        self.counter = 0
        qss2_file = open('../resource/styleKuis.qss').read()

        UI_hasil_kuis.setObjectName("UI_hasil_kuis")
        UI_hasil_kuis.resize(800, 600)
        UI_hasil_kuis.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #90caf9, stop:1 #a6d4fa);")
        self.centralwidget = QtWidgets.QWidget(UI_hasil_kuis)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.kalimat_penyemangat = QtWidgets.QLabel(self.centralwidget)
        self.kalimat_penyemangat.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.kalimat_penyemangat.sizePolicy().hasHeightForWidth())
        self.kalimat_penyemangat.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Lato Heavy")
        font.setPointSize(20)
        self.kalimat_penyemangat.setFont(font)
        self.kalimat_penyemangat.setAlignment(QtCore.Qt.AlignCenter)
        self.kalimat_penyemangat.setObjectName("kalimat_penyemangat")
        if self.skor_kuis <= 7:
            self.kalimat_penyemangat.setText("Semangat")
        else:
            self.kalimat_penyemangat.setText("Selamat")

        self.verticalLayout_2.addWidget(self.kalimat_penyemangat)
        self.kalimat_skor = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.kalimat_skor.sizePolicy().hasHeightForWidth())
        self.kalimat_skor.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(16)
        self.kalimat_skor.setFont(font)
        self.kalimat_skor.setAlignment(QtCore.Qt.AlignCenter)
        self.kalimat_skor.setObjectName("kalimat_skor")
        self.kalimat_skor.setText("Skor Kuismu = "+str(self.skor_kuis))

        self.verticalLayout_2.addWidget(self.kalimat_skor)
        self.verticalLayout_4 = QtWidgets.QVBoxLayout()
        self.verticalLayout_4.setContentsMargins(30, -1, 30, -1)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_4.addWidget(self.label_3)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents_2 = QtWidgets.QWidget()
        self.scrollAreaWidgetContents_2.setGeometry(QtCore.QRect(0, 0, 770, 391))
        self.scrollAreaWidgetContents_2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.scrollAreaWidgetContents_2.setObjectName("scrollAreaWidgetContents_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.soal_kuis = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(10)
        self.soal_kuis.setFont(font)
        self.soal_kuis.setObjectName("soal_kuis")

        # Mengambil soal dan jawaban asli
        index = self.index_soal[self.counter]
        no_soal = index+1
        self.ambil_soal_jawaban = check_soal("", index)
        self.soal_jawaban = self.ambil_soal_jawaban.ambil_soal()
        self.kalimat_soal = self.soal_jawaban[0]
        self.kalimat_jawaban_benar = run_sql(f"Select {self.soal_jawaban[1]} from soal_kuis WHERE soal ='{self.kalimat_soal}'")
        self.kalimat_jawaban_user = run_sql(f"Select {self.jawaban_user[self.counter]} from soal_kuis WHERE soal ='{self.kalimat_soal}'")

        ##############

        self.soal_kuis.setText(f"{no_soal}. {self.kalimat_soal}")

        self.verticalLayout_5.addWidget(self.soal_kuis)
        self.jawaban_pengguna = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.jawaban_pengguna.sizePolicy().hasHeightForWidth())
        self.jawaban_pengguna.setSizePolicy(sizePolicy)
        self.jawaban_pengguna.setObjectName("jawaban_pengguna")

        self.jawaban_pengguna.setText(f"Kamu Menjawab = {str(self.kalimat_jawaban_user)}")

        self.verticalLayout_5.addWidget(self.jawaban_pengguna)
        self.jawaban_benar = QtWidgets.QLabel(self.scrollAreaWidgetContents_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.jawaban_benar.sizePolicy().hasHeightForWidth())
        self.jawaban_benar.setSizePolicy(sizePolicy)
        self.jawaban_benar.setObjectName("jawaban_benar")

        self.jawaban_benar.setText(f"Jawaban yang benar = {str(self.kalimat_jawaban_benar)}")

        self.verticalLayout_5.addWidget(self.jawaban_benar)
        self.gridLayout_3 = QtWidgets.QGridLayout()
        self.gridLayout_3.setContentsMargins(-1, 20, -1, -1)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.sebelumBtn = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.sebelumBtn.setStyleSheet(qss2_file)
        self.sebelumBtn.setObjectName("sebelumBtn")
        self.sebelumBtn.clicked.connect(self.klik_sebelumnya)




        self.gridLayout_3.addWidget(self.sebelumBtn, 0, 0, 1, 1)
        self.sesudahBtn = QtWidgets.QPushButton(self.scrollAreaWidgetContents_2)
        self.sesudahBtn.setStyleSheet(qss2_file)
        self.sesudahBtn.setObjectName("sesudahBtn")
        self.sesudahBtn.clicked.connect(self.klik_selanjutnya)
        if len(self.index_soal) == 1:
            self.sebelumBtn.hide()
            self.sesudahBtn.hide()
        else:
            self.sebelumBtn.hide()

        self.gridLayout_3.addWidget(self.sesudahBtn, 0, 1, 1, 1)
        self.verticalLayout_5.addLayout(self.gridLayout_3)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)
        self.verticalLayout_4.addWidget(self.scrollArea)
        self.verticalLayout_2.addLayout(self.verticalLayout_4)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(30, -1, 30, -1)
        self.gridLayout.setObjectName("gridLayout")
        self.kembali_hasilKuisBtn = QtWidgets.QPushButton(self.centralwidget)
        self.kembali_hasilKuisBtn.setStyleSheet(qss2_file)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../resource/1x/Asset 2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.kembali_hasilKuisBtn.setIcon(icon)
        self.kembali_hasilKuisBtn.setObjectName("kembali_hasilKuisBtn")

        self.gridLayout.addWidget(self.kembali_hasilKuisBtn, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        UI_hasil_kuis.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(UI_hasil_kuis)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        UI_hasil_kuis.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(UI_hasil_kuis)
        self.statusbar.setObjectName("statusbar")
        UI_hasil_kuis.setStatusBar(self.statusbar)

        self.retranslateUi(UI_hasil_kuis)
        QtCore.QMetaObject.connectSlotsByName(UI_hasil_kuis)

    def retranslateUi(self, UI_hasil_kuis):
        _translate = QtCore.QCoreApplication.translate
        UI_hasil_kuis.setWindowTitle(_translate("UI_hasil_kuis", "Hasil Kuis"))
        # self.kalimat_penyemangat.setText(_translate("UI_hasil_kuis", "Semangat"))
        # self.kalimat_skor.setText(_translate("UI_hasil_kuis", "Skor Kuismu = 7"))
        self.label_3.setText(_translate("UI_hasil_kuis", "Soal dengan Jawaban Salah"))
        # self.soal_kuis.setText(_translate("UI_hasil_kuis", "Protokol yang umum digunakan untuk mengetahui physical address dari sebuah komputer dengan IP address tertentu disebut sebagai"))
        # self.jawaban_pengguna.setText(_translate("UI_hasil_kuis", "Kamu menjawab = "))
        # self.jawaban_benar.setText(_translate("UI_hasil_kuis", "Jawaban yang benar = "))
        self.sebelumBtn.setText(_translate("UI_hasil_kuis", "Soal Sebelumnya"))
        self.sesudahBtn.setText(_translate("UI_hasil_kuis", "Soal Sesudahnya"))
        self.kembali_hasilKuisBtn.setText(_translate("UI_hasil_kuis", "Kembali"))

    def klik_selanjutnya(self):


        panjang_index = len(self.index_soal)-1
        self.counter += 1
        if self.counter <= panjang_index:
            self.sebelumBtn.show()

            if self.counter == panjang_index:
                self.sesudahBtn.hide()
            else:
                self.sesudahBtn.show()


            index = self.index_soal[self.counter]
            print(self.index_soal)
            no_soal = index + 1
            print("Ini counter di awal klik selanjutnya" + str(self.counter))

            self.ambil_soal_jawaban = check_soal("", index)
            self.soal_jawaban = self.ambil_soal_jawaban.ambil_soal()
            self.kalimat_soal = self.soal_jawaban[0]
            self.kalimat_jawaban_benar = run_sql(
                f"Select {self.soal_jawaban[1]} from soal_kuis WHERE soal ='{self.kalimat_soal}'")
            self.kalimat_jawaban_user = run_sql(
                f"Select {self.jawaban_user[self.counter]} from soal_kuis WHERE soal ='{self.kalimat_soal}'")

            print(self.counter)

            self.soal_kuis.setText(f"{no_soal}. {self.kalimat_soal}")
            self.jawaban_pengguna.setText(f"Kamu Menjawab = {str(self.kalimat_jawaban_user)}")
            self.jawaban_benar.setText(f"Jawaban yang benar = {str(self.kalimat_jawaban_benar)}")
        else:
            print("Sudah habis soalnya")
            self.counter -= 1

    def klik_sebelumnya(self):
        print("counter di klik sebelum dikurangi "+str(self.counter))
        if self.counter == 0 :
            print("Ini soal pertama")

        else:
            self.sesudahBtn.show()
            self.counter -= 1

            if self.counter == 0:
                self.sebelumBtn.hide()
            else:
                self.sebelumBtn.show()
            index = self.index_soal[self.counter]
            no_soal = index + 1
            print("Ini counter di awal klik sebelum" + str(self.counter))

            self.ambil_soal_jawaban = check_soal("", index)
            self.soal_jawaban = self.ambil_soal_jawaban.ambil_soal()
            self.kalimat_soal = self.soal_jawaban[0]
            self.kalimat_jawaban_benar = run_sql(
                f"Select {self.soal_jawaban[1]} from soal_kuis WHERE soal ='{self.kalimat_soal}'")
            self.kalimat_jawaban_user = run_sql(
                f"Select {self.jawaban_user[self.counter]} from soal_kuis WHERE soal ='{self.kalimat_soal}'")

            print(self.counter)

            self.soal_kuis.setText(f"{no_soal}. {self.kalimat_soal}")
            self.jawaban_pengguna.setText(f"Kamu Menjawab = {str(self.kalimat_jawaban_user)}")
            self.jawaban_benar.setText(f"Jawaban yang benar = {str(self.kalimat_jawaban_benar)}")



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    UI_hasil_kuis = QtWidgets.QMainWindow()
    ui = Ui_UI_hasil_kuis()
    ui.setupUi(UI_hasil_kuis)
    UI_hasil_kuis.show()
    sys.exit(app.exec_())
