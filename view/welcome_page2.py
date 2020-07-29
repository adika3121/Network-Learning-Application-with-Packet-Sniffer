# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'welcome_page2.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!
import self
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QPushButton, QGraphicsDropShadowEffect, QWidget, QMainWindow, QApplication

from view.hasil_sniffing2 import Ui_hasil_sniffing2
from view.input_sniffing import Ui_sniffing_langsung
from view.pilih_method2 import Ui_LaluLintas_type2


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        qss_file = open('../resource/style.qss').read()
        mainWindow.resize(800, 600)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(mainWindow.sizePolicy().hasHeightForWidth())
        mainWindow.setSizePolicy(sizePolicy)
        mainWindow.setStyleSheet(qss_file)
        mainWindow.setAnimated(True)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setContentsMargins(20, -1, 20, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setSizeConstraint(QtWidgets.QLayout.SetDefaultConstraint)
        self.verticalLayout_2.setContentsMargins(20, -1, 20, -1)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")



        self.label = QtWidgets.QLabel(self.centralwidget)
        # self.label.setGraphicsEffect(self.shadow)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(0, 100))
        self.label.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setFamily("Lato")
        font.setBold(True)
        self.label.setFont(font)
        self.label.setFrameShadow(QtWidgets.QFrame.Plain)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.gridLayout_2 = QtWidgets.QGridLayout()
        self.gridLayout_2.setContentsMargins(10, -1, -1, -1)
        self.gridLayout_2.setObjectName("gridLayout_2")

        # About Button
        self.aboutBtn = QtWidgets.QPushButton(self.centralwidget)
        self.aboutBtn.setMinimumSize(QtCore.QSize(0, 50))
        # self.aboutBtn.setGraphicsEffect(self.shadow)
        font = QtGui.QFont()
        font.setFamily("Century")
        font.setPointSize(-1)
        self.aboutBtn.setFont(font)
        self.aboutBtn.setStyleSheet(qss_file)
        self.aboutBtn.setObjectName("aboutBtn")
        self.gridLayout_2.addWidget(self.aboutBtn, 3, 0, 1, 1)
        self.glosariumBtn = QtWidgets.QPushButton(self.centralwidget)
        self.glosariumBtn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Century")
        font.setPointSize(-1)
        self.glosariumBtn.setFont(font)
        self.glosariumBtn.setStyleSheet(qss_file)
        self.glosariumBtn.setObjectName("glosariumBtn")
        self.gridLayout_2.addWidget(self.glosariumBtn, 2, 0, 1, 1)
        self.quizBtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.quizBtn.sizePolicy().hasHeightForWidth())
        self.quizBtn.setSizePolicy(sizePolicy)
        self.quizBtn.setMinimumSize(QtCore.QSize(0, 50))
        font = QtGui.QFont()
        font.setFamily("Century")
        font.setPointSize(-1)
        self.quizBtn.setFont(font)
        self.quizBtn.setStyleSheet(qss_file)
        self.quizBtn.setObjectName("quizBtn")
        self.gridLayout_2.addWidget(self.quizBtn, 1, 0, 1, 1)
        self.lihat_protocolBtn = QtWidgets.QPushButton(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lihat_protocolBtn.sizePolicy().hasHeightForWidth())
        self.lihat_protocolBtn.setSizePolicy(sizePolicy)
        self.lihat_protocolBtn.setMinimumSize(QtCore.QSize(20, 50))
        font = QtGui.QFont()
        font.setFamily("Century")
        font.setPointSize(-1)
        self.lihat_protocolBtn.setFont(font)



        self.lihat_protocolBtn.setStyleSheet(qss_file)

        self.lihat_protocolBtn.setAutoDefault(False)
        self.lihat_protocolBtn.setDefault(False)
        self.lihat_protocolBtn.setFlat(False)
        self.lihat_protocolBtn.setObjectName("lihat_protocolBtn")
        self.gridLayout_2.addWidget(self.lihat_protocolBtn, 0, 0, 1, 1)


        self.verticalLayout_2.addLayout(self.gridLayout_2)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)


        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "Aplikasi Pembelajaran Lalu Lintas Protokol"))
        self.label.setText(_translate("mainWindow", "Aplikasi Pembelajaran Lalu Lintas Protokol"))
        self.aboutBtn.setText(_translate("mainWindow", "Tentang Aplikasi"))
        self.glosariumBtn.setText(_translate("mainWindow", "Glosarium"))
        self.quizBtn.setText(_translate("mainWindow", "Kuis"))
        self.lihat_protocolBtn.setText(_translate("mainWindow", "Lihat Lalu Lintas Protokol"))





# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     # mainWindow = QtWidgets.QMainWindow()
#     # app = QApplication(sys.argv)
#     w = MainWindow()
#     sys.exit(app.exec_())
#     # ui = MainWindow()
#     # ui.setupUi(mainWindow)
#     # mainWindow.show()
#     # sys.exit(app.exec_())
