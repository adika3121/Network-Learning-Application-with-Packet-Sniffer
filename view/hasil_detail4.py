# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hasil_detail4.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
import json

from PyQt5.QtWidgets import QMessageBox

from controller.db_connector import run_sql_spec


class Ui_hasil_detail4(object):
    def setupUi(self, hasil_detail, id_det_hasil):
        hasil_detail.setObjectName("hasil_detail")
        hasil_detail.resize(800, 600)
        qss_file = open('../resource/style.qss').read()
        hasil_detail.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #90caf9, stop:1 #a6d4fa);")
        self.centralwidget = QtWidgets.QWidget(hasil_detail)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(30, 20, 30, 0)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Lato Heavy")
        font.setPointSize(18)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.cariField = QtWidgets.QLineEdit(self.centralwidget)
        self.cariField.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.cariField.setObjectName("cariField")
        self.horizontalLayout_2.addWidget(self.cariField)
        self.cariKata_Bttn = QtWidgets.QPushButton(self.centralwidget)
        self.cariKata_Bttn.setStyleSheet("padding: 4px 15px;\n"
"font-size: 11px;\n"
"text-align: center;\n"
"cursor: pointer;\n"
"outline: none;\n"
"color: #fff;\n"
"background-color: #3949AB;\n"
"border: none;\n"
"border-radius: 15px;\n"
"box-shadow: 0 9px #999;")
        self.cariKata_Bttn.setObjectName("cariKata_Bttn")
        self.cariKata_Bttn.clicked.connect(self.clickCari)
        self.cariKata_Bttn.setAutoDefault(True)
        self.horizontalLayout_2.addWidget(self.cariKata_Bttn)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.text_detail = QtWidgets.QTextEdit(self.centralwidget)
        self.text_detail.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.text_detail.setObjectName("text_detail")
        self.verticalLayout_2.addWidget(self.text_detail)



        # Menampilkan detail
        result = run_sql_spec(
            "SELECT hasil_awal FROM tb_det_hasil WHERE id_tb_det_hasil = '%s'" % (id_det_hasil))

        result2 = str(result[0])
        # print("Ini hasil result 2 "+result2)
        result3 = result2.replace("'", "").strip("'<>() ").replace('\'', '\"')


        # Text = json.dumps(result3, indent=2)

        self.text_detail.setPlainText(result3)
        # #######################################
        print("udah sampe sini")

        self.simpanCariKata = []

        ## Bikin Cursor
        self.cursor = self.text_detail.textCursor()

        ##Format pas searchnya dah ketemu

        self.format = QtGui.QTextCharFormat()
        self.format.setBackground(QtGui.QBrush(QtGui.QColor("yellow")))


        ## Pointer Searchnya


        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.kembaliBtn_detail = QtWidgets.QPushButton(self.centralwidget)
        self.kembaliBtn_detail.setStyleSheet(qss_file)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../resource/1x/Asset 2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.kembaliBtn_detail.setIcon(icon)
        self.kembaliBtn_detail.setObjectName("kembaliBtn_detail")
        self.horizontalLayout_3.addWidget(self.kembaliBtn_detail)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.cek_glosarium_btn = QtWidgets.QPushButton(self.centralwidget)
        self.cek_glosarium_btn.setStyleSheet(qss_file)
        self.cek_glosarium_btn.setObjectName("cek_glosarium_btn")
        self.horizontalLayout_3.addWidget(self.cek_glosarium_btn)
        self.verticalLayout_2.addLayout(self.horizontalLayout_3)
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
        hasil_detail.setWindowTitle(_translate("hasil_detail", "Hasil Detail"))
        self.label.setText(_translate("hasil_detail", "Detail Paket"))
        self.cariKata_Bttn.setText(_translate("hasil_detail", "Cari Kata"))
        self.kembaliBtn_detail.setText(_translate("hasil_detail", "Kembali"))
        self.cek_glosarium_btn.setText(_translate("hasil_detail", "Bingung arti setiap kata? Cek Glosarium"))


    def clickCari(self):
        cariKata = self.cariField.text()
        print(cariKata)

        # Menghapus sisa highlight sebelumnya
        if len(self.simpanCariKata) == 0:
            print("Belum ada apa")
        else:
            for i in range(len(self.simpanCariKata)):
                self.format2 = QtGui.QTextCharFormat()
                self.format2.setBackground(QtGui.QBrush(QtGui.QColor("white")))
                print(self.simpanCariKata[i])
                regex2 = QtCore.QRegExp(self.simpanCariKata[i])

                # Process the displayed document
                pos = 0
                index = regex2.indexIn(self.text_detail.toPlainText(), pos)
                print("ini index " + str(index))
                while (index != -1):
                    # Select the matched text and apply the desired format
                    self.cursor.setPosition(index)
                    self.cursor.movePosition(QtGui.QTextCursor.EndOfBlock, 1)
                    self.cursor.mergeCharFormat(self.format2)

                    # Move to the next match
                    pos = index + regex2.matchedLength()
                    index = regex2.indexIn(self.text_detail.toPlainText(), pos)
                    print("ini index 2 " + str(index))



        self.simpanCariKata.append(cariKata)
        regex = QtCore.QRegExp(cariKata)

        # Process the displayed document
        pos = 0
        index = regex.indexIn(self.text_detail.toPlainText(), pos)
        print("ini index "+str(index))

        if index == -1:
            msg = QMessageBox()
            msg.setWindowTitle("Peringatan")
            msg.setText("Kata yang anda cari tidak ditemukan")
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()
            print("Tidak ada kata ini")
        else:
            while (index != -1):
                # Select the matched text and apply the desired format
                self.cursor.setPosition(index)
                self.cursor.movePosition(QtGui.QTextCursor.EndOfBlock, 1)
                self.cursor.mergeCharFormat(self.format)
                self.text_detail.ensureCursorVisible()
                # Move to the next match
                pos = index + regex.matchedLength()
                index = regex.indexIn(self.text_detail.toPlainText(), pos)
                print("ini index 2 "+str(index))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    hasil_detail = QtWidgets.QMainWindow()
    ui = Ui_hasil_detail4()
    ui.setupUi(hasil_detail)
    hasil_detail.show()
    sys.exit(app.exec_())
