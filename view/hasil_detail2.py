# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hasil_detail2.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
import jsbeautifier

from PyQt5 import QtCore, QtGui, QtWidgets
import json

from controller.db_connector import run_sql_all, run_sql, run_sql_spec


class Ui_hasil_detail2(object):
    def setupUi(self, hasil_detail, id_det_hasil):
        hasil_detail.setObjectName("hasil_detail")
        hasil_detail.resize(800, 600)
        qss_file = open('../resource/style.qss').read()
        hasil_detail.setStyleSheet(qss_file)
        self.centralwidget = QtWidgets.QWidget(hasil_detail)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setContentsMargins(30, 20, 30, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Lato Heavy")
        font.setPointSize(16)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(20, 30, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        self.verticalLayout_2.addItem(spacerItem)
        self.text_detail = QtWidgets.QPlainTextEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Lato")

        self.text_detail.setFont(font)
        self.text_detail.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.text_detail.setFrameShape(QtWidgets.QFrame.StyledPanel)

        # Menampilkan detail
        result = run_sql_spec(
            "SELECT hasil_awal FROM tb_det_hasil WHERE id_tb_det_hasil = '%s'" % (id_det_hasil))
        # str_result = ''.join(result[0])

        result2 = str(result[0])
        # print("Ini hasil result 2 "+result2)
        result3 = result2.replace("'", "").strip("'<>() ").replace('\'', '\"')
        # print("Ini hasil result 3 "+result3)
        # result_json = json.loads(result2)
        # print(result_json)

        # with open('outkul.json', 'rb') as f:
        #     d = json.load(f)
        #
        # string = json.dumps(d, indent=2)

        # str_result2 = str_result.replace('"', '')
        # str_result3 = str_result2.replace("'", "")
        # print("ini var str_result2 "+str_result3)
        # str_result.replace('""', '\\"')
        # str_result.replace("'", "\\'")
        # str_result.replace("''", "\\'")
        # str_result.replace("wasn't", "was not")

        Text = json.dumps(result3, indent=2)
        # print("ini var text "+Text)
        # print(result[0])

        # opts = jsbeautifier.default_options()
        # opts.indent_size = 2
        # opts.space_in_empty_paren = True
        # result_str = jsbeautifier.beautify(str(Text), opts)
        # print(result_str)
        self.text_detail.setPlainText(result3)
        # #######################################
        print("udah sampe sini")
        self.text_detail.setObjectName("text_detail")
        self.verticalLayout_2.addWidget(self.text_detail)
        self.verticalLayout_3 = QtWidgets.QVBoxLayout()
        self.verticalLayout_3.setContentsMargins(30, 40, 30, 20)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.kembaliBtn_detail = QtWidgets.QPushButton(self.centralwidget)
        self.kembaliBtn_detail.setMinimumSize(QtCore.QSize(100, 0))
        self.kembaliBtn_detail.setStyleSheet(qss_file)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../resource/1x/Asset 2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.kembaliBtn_detail.setIcon(icon)
        self.kembaliBtn_detail.setObjectName("kembaliBtn_detail")
        self.gridLayout.addWidget(self.kembaliBtn_detail, 1, 0, 1, 1)
        spacerItem1 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 1, 1, 1)
        self.cek_glosarium_btn = QtWidgets.QPushButton(self.centralwidget)
        self.cek_glosarium_btn.setStyleSheet(qss_file)
        self.cek_glosarium_btn.setObjectName("cek_glosarium_btn")
        self.gridLayout.addWidget(self.cek_glosarium_btn, 1, 2, 1, 1)
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
        hasil_detail.setWindowTitle(_translate("hasil_detail", "Hasil Sniffing"))
        self.label.setText(_translate("hasil_detail", "Detail Paket"))
        self.kembaliBtn_detail.setText(_translate("hasil_detail", "Kembali"))
        self.cek_glosarium_btn.setText(_translate("hasil_detail", "Bingung arti setiap kata? Cek Glosarium"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    hasil_detail = QtWidgets.QMainWindow()
    ui = Ui_hasil_detail2()
    ui.setupUi(hasil_detail)
    hasil_detail.show()
    sys.exit(app.exec_())
