# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'hasil_kuis100.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_HasilKuis100(object):
    def setupUi(self, HasilKuis):
        HasilKuis.setObjectName("HasilKuis")
        HasilKuis.resize(800, 600)
        qss2_file = open('../resource/styleKuis.qss').read()
        HasilKuis.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #90caf9, stop:1 #a6d4fa);")
        self.centralwidget = QtWidgets.QWidget(HasilKuis)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
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
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(16)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Lato")
        font.setPointSize(12)
        self.label_3.setFont(font)
        self.label_3.setAlignment(QtCore.Qt.AlignCenter)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setContentsMargins(300, -1, 300, -1)
        self.gridLayout.setObjectName("gridLayout")
        self.kembaliBtn = QtWidgets.QPushButton(self.centralwidget)
        self.kembaliBtn.setStyleSheet(qss2_file)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../resource/1x/Asset 2.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.kembaliBtn.setIcon(icon)
        self.kembaliBtn.setObjectName("kembaliBtn")
        self.gridLayout.addWidget(self.kembaliBtn, 0, 0, 1, 1)
        self.verticalLayout.addLayout(self.gridLayout)
        HasilKuis.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(HasilKuis)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        HasilKuis.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(HasilKuis)
        self.statusbar.setObjectName("statusbar")
        HasilKuis.setStatusBar(self.statusbar)

        self.retranslateUi(HasilKuis)
        QtCore.QMetaObject.connectSlotsByName(HasilKuis)

    def retranslateUi(self, HasilKuis):
        _translate = QtCore.QCoreApplication.translate
        HasilKuis.setWindowTitle(_translate("HasilKuis", "Hasil Kuis"))
        self.label.setText(_translate("HasilKuis", "Luar Biasa"))
        self.label_2.setText(_translate("HasilKuis", "Skor Kuismu = 10"))
        self.label_3.setText(_translate("HasilKuis", "Kamu berhasil menjawab semua pertanyaan kuis. Pertahankan!"))
        self.kembaliBtn.setText(_translate("HasilKuis", "Kembali"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    HasilKuis = QtWidgets.QMainWindow()
    ui = Ui_HasilKuis100()
    ui.setupUi(HasilKuis)
    HasilKuis.show()
    sys.exit(app.exec_())
