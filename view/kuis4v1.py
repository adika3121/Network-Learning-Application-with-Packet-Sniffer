# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'kuis4.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox

from controller.check_soal import check_soal
from controller.db_connector import run_sql_all


class Ui_Ui_kuis2(object):
    def setupUi(self, Ui_kuis2):
        Ui_kuis2.setObjectName("Ui_kuis2")
        Ui_kuis2.resize(800, 600)
        qss2_file = open('../resource/styleKuis2.qss').read()
        Ui_kuis2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #90caf9, stop:1 #b0ceff);")
        self.centralwidget = QtWidgets.QWidget(Ui_kuis2)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setContentsMargins(30, 30, 30, -1)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Lato Heavy")
        font.setPointSize(32)
        self.label.setFont(font)
        self.label.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #90caf9, stop:1 #b0ceff);")
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.verticalLayout.addItem(spacerItem)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(11)
        self.label_2.setFont(font)
        self.label_2.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #90caf9, stop:1 #b0ceff);")
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.scrollArea = QtWidgets.QScrollArea(self.centralwidget)
        self.scrollArea.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 720, 381))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.soal_kuis = QtWidgets.QLabel(self.scrollAreaWidgetContents)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.soal_kuis.sizePolicy().hasHeightForWidth())
        self.soal_kuis.setSizePolicy(sizePolicy)

        self.jawaban = []
        soal = check_soal("", 0)
        soal_awal = soal.awal_soal()
        self.index_soal = soal_awal[5]
        no_soal = self.index_soal + 1
        print("Ini var index di awal " + str(self.index_soal))




        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(11)
        self.soal_kuis.setFont(font)
        self.soal_kuis.setText(f"{no_soal}. {soal_awal[0]}")
        self.soal_kuis.setObjectName("soal_kuis")
        self.verticalLayout_2.addWidget(self.soal_kuis)
        self.pilihan1 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(12)
        self.pilihan1.setFont(font)
        self.pilihan1.setObjectName("pilihan1")
        self.verticalLayout_2.addWidget(self.pilihan1)

        self.pilihan1.setText(soal_awal[1])

        self.pilihan2 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(12)
        self.pilihan2.setFont(font)
        self.pilihan2.setObjectName("pilihan2")
        self.verticalLayout_2.addWidget(self.pilihan2)
        self.pilihan2.setText(soal_awal[2])

        self.pilihan3 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(12)
        self.pilihan3.setFont(font)
        self.pilihan3.setObjectName("pilihan3")
        self.verticalLayout_2.addWidget(self.pilihan3)
        self.pilihan3.setText(soal_awal[3])

        self.pilihan4 = QtWidgets.QRadioButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(12)
        self.pilihan4.setFont(font)
        self.pilihan4.setObjectName("pilihan4")
        self.pilihan4.setText(soal_awal[4])

        self.verticalLayout_2.addWidget(self.pilihan4)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.menuAwalBtn = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.menuAwalBtn.setFont(font)
        self.menuAwalBtn.setStyleSheet(qss2_file)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../resource/1x/Asset 2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.menuAwalBtn.setIcon(icon)
        self.menuAwalBtn.setObjectName("menuAwalBtn")
        self.gridLayout.addWidget(self.menuAwalBtn, 3, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem1, 2, 0, 1, 1)
        self.sebelumBtn = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.sebelumBtn.setStyleSheet(qss2_file)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap("../resource/sebelumnya.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.sebelumBtn.setIcon(icon1)
        self.sebelumBtn.setObjectName("sebelumBtn")

        self.sebelumBtn.clicked.connect(self.klik_sebelum)
        self.sebelumBtn.hide()


        self.gridLayout.addWidget(self.sebelumBtn, 1, 3, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        self.pushButton_2.setStyleSheet(qss2_file)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap("../resource/selanjutnya.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon2)
        self.pushButton_2.setObjectName("pushButton_2")

        self.pushButton_2.clicked.connect(self.klik_selanjutnya)

        self.gridLayout.addWidget(self.pushButton_2, 1, 4, 1, 1)
        self.nilaiBtn = QtWidgets.QPushButton(self.scrollAreaWidgetContents)
        font = QtGui.QFont()
        font.setPointSize(-1)
        self.nilaiBtn.setFont(font)
        self.nilaiBtn.setStyleSheet(qss2_file)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap("../resource/cek_nilai_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.nilaiBtn.setIcon(icon3)
        self.nilaiBtn.setObjectName("nilaiBtn")
        self.gridLayout.addWidget(self.nilaiBtn, 3, 5, 1, 1)
        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.gridLayout.addItem(spacerItem2, 2, 5, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)
        self.verticalLayout.addWidget(self.scrollArea)
        self.horizontalLayout.addLayout(self.verticalLayout)
        Ui_kuis2.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Ui_kuis2)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        Ui_kuis2.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Ui_kuis2)
        self.statusbar.setObjectName("statusbar")
        Ui_kuis2.setStatusBar(self.statusbar)

        self.retranslateUi(Ui_kuis2)
        QtCore.QMetaObject.connectSlotsByName(Ui_kuis2)

    def retranslateUi(self, Ui_kuis2):
        _translate = QtCore.QCoreApplication.translate
        Ui_kuis2.setWindowTitle(_translate("Ui_kuis2", "Kuis"))
        self.label.setText(_translate("Ui_kuis2", "Kuis"))
        self.label_2.setText(_translate("Ui_kuis2", "Jawab pertanyaan dibawah dengan memilih salah satu pilihan yang ada kemudian menekan tombol lanjut. "))
        # self.soal_kuis.setText(_translate("Ui_kuis2", "Soal"))
        # self.pilihan1.setText(_translate("Ui_kuis2", "Pilihan 1"))
        # self.pilihan2.setText(_translate("Ui_kuis2", "Pilihan 2"))
        # self.pilihan3.setText(_translate("Ui_kuis2", "Pilihan 3"))
        # self.pilihan4.setText(_translate("Ui_kuis2", "Pilihan 4"))
        self.menuAwalBtn.setText(_translate("Ui_kuis2", "Menu Awal"))
        self.sebelumBtn.setText(_translate("Ui_kuis2", "Sebelum "))
        self.pushButton_2.setText(_translate("Ui_kuis2", "Selanjutnya"))
        self.nilaiBtn.setText(_translate("Ui_kuis2", "Cek Nilai"))

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
    Ui_kuis2 = QtWidgets.QMainWindow()
    ui = Ui_Ui_kuis2()
    ui.setupUi(Ui_kuis2)
    Ui_kuis2.show()
    sys.exit(app.exec_())
