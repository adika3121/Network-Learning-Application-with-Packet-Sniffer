# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kuis2.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from controller.check_soal import check_soal
from controller.db_connector import run_sql_all


class Ui_kuis2(object):
    def setupUi(self, hasil_detail):
        hasil_detail.setObjectName("hasil_detail")
        hasil_detail.resize(800, 600)
        qss2_file = open('../resource/styleKuis.qss').read()
        hasil_detail.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #90caf9, stop:1 #a6d4fa);")
        self.centralwidget = QtWidgets.QWidget(hasil_detail)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(30, 20, 30, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Lato Heavy")
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout_2.addItem(spacerItem)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout_2.addWidget(self.label_3)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(30, 10, 30, 20)
        self.verticalLayout_3.setObjectName("verticalLayout_3")

        self.jawaban = []
        soal = check_soal("",0)
        soal_awal = soal.awal_soal()
        self.index_soal = soal_awal[5]
        no_soal = self.index_soal +1
        print("Ini var index di awal "+str(self.index_soal))


        self.soal_kuis = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.soal_kuis.sizePolicy().hasHeightForWidth())
        self.soal_kuis.setSizePolicy(sizePolicy)
        self.soal_kuis.setMinimumSize(QtCore.QSize(0, 40))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.soal_kuis.setFont(font)
        self.soal_kuis.setText(f"{no_soal}. {soal_awal[0]}")
        self.soal_kuis.setObjectName("soal_kuis")
        self.verticalLayout_3.addWidget(self.soal_kuis)

        self.pilihan1 = QtWidgets.QRadioButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pilihan1.sizePolicy().hasHeightForWidth())
        self.pilihan1.setSizePolicy(sizePolicy)
        self.pilihan1.setText(soal_awal[1])
        self.pilihan1.setMinimumSize(QtCore.QSize(0, 30))
        self.pilihan1.setObjectName("pilihan1")

        self.verticalLayout_3.addWidget(self.pilihan1)
        self.pilihan2 = QtWidgets.QRadioButton(self.centralwidget)
        self.pilihan2.setMinimumSize(QtCore.QSize(0, 30))
        self.pilihan2.setObjectName("pilihan2")
        self.pilihan2.setText(soal_awal[2])
        self.verticalLayout_3.addWidget(self.pilihan2)
        self.pilihan3 = QtWidgets.QRadioButton(self.centralwidget)
        self.pilihan3.setMinimumSize(QtCore.QSize(0, 30))
        self.pilihan3.setObjectName("pilihan3")
        self.pilihan3.setText(soal_awal[3])
        self.verticalLayout_3.addWidget(self.pilihan3)
        self.pilihan4 = QtWidgets.QRadioButton(self.centralwidget)
        self.pilihan4.setMinimumSize(QtCore.QSize(0, 30))
        self.pilihan4.setObjectName("pilihan4")
        self.pilihan4.setText(soal_awal[4])
        self.verticalLayout_3.addWidget(self.pilihan4)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.menuAwalBtn = QtWidgets.QPushButton(self.centralwidget)
        self.menuAwalBtn.setMinimumSize(QtCore.QSize(100, 0))
        self.menuAwalBtn.setStyleSheet(qss2_file)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../resource/1x/Asset 2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuAwalBtn.setIcon(icon)
        self.menuAwalBtn.setObjectName("menuAwalBtn")
        self.gridLayout.addWidget(self.menuAwalBtn, 3, 0, 1, 1)
        self.nilaiBtn = QtWidgets.QPushButton(self.centralwidget)
        self.nilaiBtn.setStyleSheet(qss2_file)
        self.nilaiBtn.setObjectName("nilaiBtn")
        # self.nilaiBtn.clicked.connect(self.klik_nilai)
        self.gridLayout.addWidget(self.nilaiBtn, 3, 3, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setStyleSheet(qss2_file)
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_2.clicked.connect(self.klik_selanjutnya)
        self.gridLayout.addWidget(self.pushButton_2, 0, 2, 1, 1)
        self.sebelumBtn = QtWidgets.QPushButton(self.centralwidget)
        self.sebelumBtn.setStyleSheet(qss2_file)
        self.sebelumBtn.setObjectName("sebelumBtn")
        self.sebelumBtn.clicked.connect(self.klik_sebelum)
        self.sebelumBtn.hide()
        self.gridLayout.addWidget(self.sebelumBtn, 0, 1, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 3, 1, 1, 2)
        spacerItem2 = QtWidgets.QSpacerItem(20, 100, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem2, 0, 0, 1, 1)
        self.verticalLayout_3.addLayout(self.gridLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout_3)
        self.verticalLayout.addLayout(self.verticalLayout_2)
        hasil_detail.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(hasil_detail)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        hasil_detail.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(hasil_detail)
        self.statusbar.setObjectName("statusbar")
        hasil_detail.setStatusBar(self.statusbar)

        self.retranslateUi(hasil_detail)
        QtCore.QMetaObject.connectSlotsByName(hasil_detail)

    def retranslateUi(self, hasil_detail):
        _translate = QtCore.QCoreApplication.translate
        hasil_detail.setWindowTitle(_translate("hasil_detail", "Kuis"))
        self.label.setText(_translate("hasil_detail", "Kuis"))
        self.label_3.setText(_translate("hasil_detail", "Jawab pertanyaan dibawah dengan memilih salah satu pilihan yang ada kemudian menekan tombol lanjut. "))
        self.menuAwalBtn.setText(_translate("hasil_detail", "Menu Awal"))
        self.nilaiBtn.setText(_translate("hasil_detail", "Cek Nilai"))
        self.pushButton_2.setText(_translate("hasil_detail", "Selanjutnya"))
        self.sebelumBtn.setText(_translate("hasil_detail", "Sebelum"))

    def klik_sebelum(self):
        print("klik sebelum")
        if self.index_soal == 0 :
            print("Ini soal pertama")

        else:
            self.pushButton_2.show()
            i = self.index_soal - 1
            self.jawaban.pop(i)
            print(self.jawaban)
            soal = check_soal("",i)
            soal_sebelum = soal.soal_sebelumnya()
            self.soal_kuis.setText(f"{self.index_soal}. {soal_sebelum[0]}")
            self.pilihan1.setText(soal_sebelum[1])
            self.pilihan2.setText(soal_sebelum[2])
            self.pilihan3.setText(soal_sebelum[3])
            self.pilihan4.setText(soal_sebelum[4])
            self.index_soal -= 1
            if self.index_soal == 0:
                self.sebelumBtn.hide()

            else:
                self.sebelumBtn.show()


    def klik_selanjutnya(self):
        print("klik selanjutnya")
        print("Var index sebelum ditambah "+str(self.index_soal))

        i = self.index_soal + 1
        panjang_soal = run_sql_all("SELECT soal FROM soal_kuis")
        panjang_soal = run_sql_all("SELECT soal FROM soal_kuis")

        self.panjang_index = len(panjang_soal) -1
        no_soal = i+1

        if i <= self.panjang_index:

            if self.pilihan1.isChecked():
                self.sebelumBtn.show()
                jawaban = "pilihan1"
                self.jawaban.append(jawaban)
                soal = check_soal(self.jawaban, i)
                soal_selanjutnya = soal.soal_selanjutnya()
                # print(soal_selanjutnya[0])
                self.soal_kuis.setText(f"{no_soal}. {str(soal_selanjutnya[0])}")
                self.pilihan1.setText(str(soal_selanjutnya[1]))
                self.pilihan2.setText(str(soal_selanjutnya[2]))
                self.pilihan3.setText(str(soal_selanjutnya[3]))
                self.pilihan4.setText(str(soal_selanjutnya[4]))
                if i == self.panjang_index:
                    self.pushButton_2.hide()
                else:
                    self.pushButton_2.show()

                self.index_soal += 1
                # self.jawaban.clear()
                print(self.jawaban)



                print("ini var index stelah klik slanjutnya "+str(self.index_soal))
            elif self.pilihan2.isChecked():
                self.sebelumBtn.show()
                jawaban = "pilihan2"
                self.jawaban.append(jawaban)
                soal = check_soal(self.jawaban, i)
                soal_selanjutnya = soal.soal_selanjutnya()
                self.soal_kuis.setText(f"{no_soal}. {str(soal_selanjutnya[0])}")
                self.pilihan1.setText(soal_selanjutnya[1])
                self.pilihan2.setText(soal_selanjutnya[2])
                self.pilihan3.setText(soal_selanjutnya[3])
                self.pilihan4.setText(soal_selanjutnya[4])
                if i == self.panjang_index:
                    self.pushButton_2.hide()
                else:
                    self.pushButton_2.show()
                self.index_soal += 1
                print(self.jawaban)

            elif self.pilihan3.isChecked():
                self.sebelumBtn.show()
                jawaban = "pilihan3"
                self.jawaban.append(jawaban)
                soal = check_soal(self.jawaban, i)
                soal_selanjutnya = soal.soal_selanjutnya()
                self.soal_kuis.setText(f"{no_soal}. {str(soal_selanjutnya[0])}")
                self.pilihan1.setText(soal_selanjutnya[1])
                self.pilihan2.setText(soal_selanjutnya[2])
                self.pilihan3.setText(soal_selanjutnya[3])
                self.pilihan4.setText(soal_selanjutnya[4])
                if i == self.panjang_index:
                    self.pushButton_2.hide()
                else:
                    self.pushButton_2.show()
                self.index_soal += 1
                print(self.jawaban)

            elif self.pilihan4.isChecked():
                self.sebelumBtn.show()
                jawaban = "pilihan4"
                self.jawaban.append(jawaban)
                soal = check_soal(self.jawaban, i)
                soal_selanjutnya = soal.soal_selanjutnya()
                self.soal_kuis.setText(f"{no_soal}. {str(soal_selanjutnya[0])}")
                self.pilihan1.setText(soal_selanjutnya[1])
                self.pilihan2.setText(soal_selanjutnya[2])
                self.pilihan3.setText(soal_selanjutnya[3])
                self.pilihan4.setText(soal_selanjutnya[4])
                if i == self.panjang_index:
                    self.pushButton_2.hide()
                else:
                    self.pushButton_2.show()
                self.index_soal += 1
                print(self.jawaban)

            else:
                msg = QMessageBox()
                msg.setWindowTitle("Peringatan")
                msg.setText("Pastikan untuk menjawab dahulu sebelum melanjutkan")
                msg.setIcon(QMessageBox.Warning)
                msg.exec_()
                print("Pilih dulu baru lanjut")

        else:

            print("Soal Sudah Habis")
            check_sisa = self.panjang_index - len(self.jawaban)
            if check_sisa == 0:

                if self.pilihan1.isChecked():
                    jawab = "pilihan1"
                    self.jawaban.append(jawab)
                    print(self.jawaban)
                    self.index_soal += 1
                elif self.pilihan2.isChecked():
                    jawab = "pilihan2"
                    self.jawaban.append(jawab)
                    print(self.jawaban)
                    self.index_soal += 1
                elif self.pilihan3.isChecked():
                    jawab = "pilihan3"
                    self.jawaban.append(jawab)
                    print(self.jawaban)
                    self.index_soal += 1
                elif self.pilihan4.isChecked():
                    jawab = "pilihan4"
                    self.jawaban.append(jawab)
                    print(self.jawaban)
                    self.index_soal += 1
                else:
                    print("Pilihan habis")
            else:
                print("Pilihan Habis")

    def klik_nilai(self):
        print("fungsi klik nilai")
        panjang_soal = run_sql_all("SELECT soal FROM soal_kuis")
        if len(panjang_soal) == len(self.jawaban):

            print(self.panjang_index)
            print(self.jawaban)
            soal = check_soal(self.jawaban, 0)
            hasil_nilai = soal.periksa_nilai()

        elif len(panjang_soal)-len(self.jawaban)==1:
            if self.pilihan1.isChecked():
                jawab = "pilihan1"
                self.jawaban.append(jawab)
                print(self.jawaban)
                soal = check_soal(self.jawaban, 0)
                hasil_nilai = soal.periksa_nilai()
            elif self.pilihan2.isChecked():
                jawab = "pilihan2"
                self.jawaban.append(jawab)
                print(self.jawaban)
                soal = check_soal(self.jawaban, 0)
                hasil_nilai = soal.periksa_nilai()
            elif self.pilihan3.isChecked():
                jawab = "pilihan3"
                self.jawaban.append(jawab)
                print(self.jawaban)
                soal = check_soal(self.jawaban, 0)
                hasil_nilai = soal.periksa_nilai()
            elif self.pilihan4.isChecked():
                jawab = "pilihan4"
                self.jawaban.append(jawab)
                print(self.jawaban)
                soal = check_soal(self.jawaban, 0)
                hasil_nilai = soal.periksa_nilai()
            else:
                print("Pilihan habis")
        else:

            print("Ada soal yg belum dijawab")






if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    hasil_detail = QtWidgets.QMainWindow()
    ui = Ui_kuis2()
    ui.setupUi(hasil_detail)
    hasil_detail.show()
    sys.exit(app.exec_())
