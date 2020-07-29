# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'welcome_page.ui'
#
# Created by: PyQt5 UI code generator 5.13.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets

from view.pilih_metode import Ui_lalulintas_type


class Ui_welcome_home(object):
    def setupUi(self, welcome_home):
        welcome_home.setObjectName("welcome_home")
        welcome_home.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(welcome_home)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(100, 90, 661, 61))
        font = QtGui.QFont()
        font.setPointSize(17)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.lihat_protocolBtn = QtWidgets.QPushButton(self.centralwidget)
        self.lihat_protocolBtn.setGeometry(QtCore.QRect(250, 290, 241, 25))
        self.lihat_protocolBtn.setObjectName("lihat_protocolBtn")
        self.lihat_protocolBtn.clicked.connect(self.open_inputSniffing)
        self.quizBtn = QtWidgets.QPushButton(self.centralwidget)
        self.quizBtn.setGeometry(QtCore.QRect(250, 340, 241, 25))
        self.quizBtn.setObjectName("quizBtn")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(250, 390, 241, 25))
        self.pushButton_3.setObjectName("pushButton_3")
        welcome_home.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(welcome_home)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        welcome_home.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(welcome_home)
        self.statusbar.setObjectName("statusbar")
        welcome_home.setStatusBar(self.statusbar)

        self.retranslateUi(welcome_home)
        QtCore.QMetaObject.connectSlotsByName(welcome_home)

    def retranslateUi(self, welcome_home):
        _translate = QtCore.QCoreApplication.translate
        welcome_home.setWindowTitle(_translate("welcome_home", "Aplikasi Pembelajaran Lalu Lintas Protocol Jaringan"))
        self.label.setText(_translate("welcome_home", "Aplikasi Pembelajaran Lalu Lintas Protocol Jaringan"))
        self.lihat_protocolBtn.setText(_translate("welcome_home", "Lihat Lalu Lintas Protocol"))
        self.quizBtn.setText(_translate("welcome_home", "Quiz"))
        self.pushButton_3.setText(_translate("welcome_home", "Tentang Aplikasi"))

    def open_inputSniffing(self):
        self.window = QtWidgets.QMainWindow()
        self.ui2 = Ui_lalulintas_type()
        self.ui2.setupUi(self.window)
        welcome_home = QtWidgets.QMainWindow()
        welcome_home.hide()
        self.window.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    welcome_home = QtWidgets.QMainWindow()
    ui = Ui_welcome_home()
    ui.setupUi(welcome_home)
    welcome_home.show()
    sys.exit(app.exec_())
