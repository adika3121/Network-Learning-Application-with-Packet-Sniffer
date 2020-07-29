from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMainWindow, QMessageBox

# from controller.sniffing import sniffing
from PyQt5.uic.properties import QtGui

from controller.check_soal import check_soal
from controller.db_connector import run_sql_all, run_sql_int
from controller.sniffing import sniffing
from view.glosarium import Ui_Glosarium_Protokol
from view.glosarium_istilah import Ui_Glosarium_Istilah
from view.hasil_detail2 import Ui_hasil_detail2
from view.hasil_detail4 import Ui_hasil_detail4
from view.hasil_kuis import Ui_UI_hasil_kuis
from view.hasil_kuis100 import Ui_HasilKuis100

from view.hasil_sniffing2 import Ui_hasil_sniffing2
from view.input_sniffing import Ui_sniffing_langsung
from view.kuis2v1 import Ui_kuis2
from view.kuis4v1 import Ui_Ui_kuis2
from view.lihat_hasil_sebelumnya import Ui_lihat_hasil_sebelumnya
from view.pilih_method2 import Ui_LaluLintas_type2
from view.tentang_aplikasi import Ui_tentang_aplikasi
from view.welcome_page2 import Ui_mainWindow


class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.ui_mainWindow = Ui_mainWindow()
        self.ui_lalulintas_type = Ui_LaluLintas_type2()
        self.ui_sniffing_langsung = Ui_sniffing_langsung()
        self.ui_hasil_sniffing = Ui_hasil_sniffing2()
        self.ui_kuis = Ui_Ui_kuis2()
        self.ui_hasil_kuis = Ui_UI_hasil_kuis()
        self.ui_hasil_kuis_benar = Ui_HasilKuis100()
        self.ui_glosa_istilah = Ui_Glosarium_Istilah()
        self.ui_glosa_protokol = Ui_Glosarium_Protokol()
        self.ui_tentang_aplikasi = Ui_tentang_aplikasi()
        self.ui_lihat_hasil_sebelum = Ui_lihat_hasil_sebelumnya()
        self.ui_hasil_detail = Ui_hasil_detail2()
        # self.ui_hasil_detail = Ui_hasil_detail4()


        self.startUI_mainWindow()

    def startUI_LaluLintas_type(self):
        self.ui_lalulintas_type.setupUi(self)
        self.ui_lalulintas_type.kembali_btn.clicked.connect(self.startUI_mainWindow)
        self.ui_lalulintas_type.sniffing_langsung.clicked.connect(self.startUI_SniffingLangsung)
        self.ui_lalulintas_type.file_pcap.clicked.connect(self.startUI_hasilSebelum)
        # self.uiToolTab.CPSBTN.clicked.connect(self.startUIWindow)
        self.show()

    def startUI_mainWindow(self):
        self.ui_mainWindow.setupUi(self)
        self.ui_mainWindow.lihat_protocolBtn.clicked.connect(self.startUI_LaluLintas_type)
        self.ui_mainWindow.quizBtn.clicked.connect(self.startUI_kuis)
        self.ui_mainWindow.glosariumBtn.clicked.connect(self.startUI_glosa_istilah)
        self.ui_mainWindow.aboutBtn.clicked.connect(self.startUI_tentang_aplikasi)
        self.show()
    def startUI_tentang_aplikasi(self):
        self.ui_tentang_aplikasi.setupUi(self)
        self.ui_tentang_aplikasi.pushButton.clicked.connect(self.startUI_mainWindow)
        self.show()

    # ########## Lihat Hasil Sebelumnya #################
    def startUI_hasilSebelum(self):
        self.ui_lihat_hasil_sebelum.setupUi(self)
        qss2_file = open('../resource/styleLihatHasilSebelum.qss').read()
        self.ui_lihat_hasil_sebelum.kembaliBtn.clicked.connect(self.startUI_LaluLintas_type)
        self.ui_lihat_hasil_sebelum.cariBtn.clicked.connect(self.clickCari)
        # menerima hasil
        result = run_sql_all(
            "SELECT id_tb_hasil, nama_hasil, tgl_n_waktu FROM tb_hasil order by tgl_n_waktu desc")
        print(result)


        self.ui_lihat_hasil_sebelum.detailButton = []

        i = 0
        for row_number, row_data in enumerate(result):
            self.ui_lihat_hasil_sebelum.detailButton.append(row_number)

            self.ui_lihat_hasil_sebelum.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui_lihat_hasil_sebelum.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
                self.ui_lihat_hasil_sebelum.detailButton[i] = QtWidgets.QPushButton(self.ui_lihat_hasil_sebelum.centralwidget)
                self.ui_lihat_hasil_sebelum.detailButton[i].setObjectName("detailButton")
                self.ui_lihat_hasil_sebelum.detailButton[i].setStyleSheet(qss2_file)
                self.ui_lihat_hasil_sebelum.detailButton[i].setText("Detail Paket")
                self.ui_lihat_hasil_sebelum.detailButton[i].clicked.connect(self.clickDetailSebelum)
                self.ui_lihat_hasil_sebelum.tableWidget.setCellWidget(row_number, 3, self.ui_lihat_hasil_sebelum.detailButton[i])

            i += 1
        self.show()

    def clickDetailSebelum(self):
        print("klik detail")
        index = self.ui_lihat_hasil_sebelum.tableWidget.currentIndex().row()
        print("ini index "+str(index))
        print("ini di kelas sa")
        id = self.ui_lihat_hasil_sebelum.tableWidget.item(index, 0)
        id_hasil = id.text()
        print(id_hasil)
        status = 0
        self.startUI_hasilSniffing(id_hasil, status)

    def clickCari(self):
        self.cariString = self.ui_lihat_hasil_sebelum.inputCari.text()
        cari = "%{0}%".format(self.cariString)
        qss2_file = open('../resource/styleLihatHasilSebelum.qss').read()
        self.ui_lihat_hasil_sebelum.tableWidget.clearContents()
        self.ui_lihat_hasil_sebelum.tableWidget.setRowCount(0)

        # menerima hasil
        result = run_sql_all(
            "SELECT id_tb_hasil, nama_hasil, tgl_n_waktu FROM tb_hasil where nama_hasil like '%s'order by tgl_n_waktu desc" % cari)
        print(result)

        self.ui_lihat_hasil_sebelum.detailButton = []

        i = 0
        for row_number, row_data in enumerate(result):
            self.ui_lihat_hasil_sebelum.detailButton.append(row_number)
            print(row_number)

            self.ui_lihat_hasil_sebelum.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui_lihat_hasil_sebelum.tableWidget.setItem(row_number, column_number,
                                                                QtWidgets.QTableWidgetItem(str(data)))

                self.ui_lihat_hasil_sebelum.detailButton[i] = QtWidgets.QPushButton(self.ui_lihat_hasil_sebelum.centralwidget)
                self.ui_lihat_hasil_sebelum.detailButton[i].setObjectName("detailButton")
                self.ui_lihat_hasil_sebelum.detailButton[i].setStyleSheet(qss2_file)
                self.ui_lihat_hasil_sebelum.detailButton[i].setText("Detail Paket")
                self.ui_lihat_hasil_sebelum.detailButton[i].clicked.connect(self.clickDetailSebelum)
                self.ui_lihat_hasil_sebelum.tableWidget.setCellWidget(row_number, 3,self.ui_lihat_hasil_sebelum.detailButton[i])

            i += 1



    ####################################################################################################


    ############ Sniffing Langsung #############################
    def startUI_SniffingLangsung(self):
        self.ui_sniffing_langsung.setupUi(self)
        self.ui_sniffing_langsung.kembali_btn2.clicked.connect(self.startUI_LaluLintas_type)
        self.ui_sniffing_langsung.sniffing_btn.clicked.connect(self.start_Sniff)
        self.ui_sniffing_langsung.cek_glosarium_btn.clicked.connect(self.startUI_glosa_istilah)

        self.show()


    def start_Sniff(self):
        kosong = ""
        # self.ui_sniffing_langsung.stop_sniff_btn.show()
        # self.ui_sniffing_langsung.sniffing_btn.hide()

        # Mengambil data dari UI Sniffing Langsung
        self.in_net_iface = self.ui_sniffing_langsung.comboIface.currentText()
        print(self.in_net_iface)
        self.in_pkt_to_sniff2 = self.ui_sniffing_langsung.lineEdit.text()
        print(self.in_pkt_to_sniff2)
        self.name_file = self.ui_sniffing_langsung.nama_file.text()
        print(self.name_file)
        self.in_proto_to_sniff2 = ""
        check_one = 0

        # merubah status saat combo box dicentang
        if self.ui_sniffing_langsung.arp.isChecked():

            self.in_proto_to_sniff2 = "arp"
            if (check_one == 0):
                check_one = 1

        if self.ui_sniffing_langsung.icmp.isChecked():
            if (check_one == 0):
                check_one = 1
                self.in_proto_to_sniff2 += "icmp"
            elif (check_one == 1):
                self.in_proto_to_sniff2 += " or icmp"

        if self.ui_sniffing_langsung.port53.isChecked():
            if (check_one == 0):
                check_one = 1
                self.in_proto_to_sniff2 += "port 53"
            elif (check_one == 1):
                self.in_proto_to_sniff2 += " or port 53"
        if self.ui_sniffing_langsung.tcp_only.isChecked():
            if (check_one == 0):
                check_one = 1
                self.in_proto_to_sniff2 += "tcp"
            elif (check_one == 1):
                self.in_proto_to_sniff2 += " or tcp"
        if self.ui_sniffing_langsung.udp_only.isChecked():
            if (check_one == 0):
                check_one = 1
                self.in_proto_to_sniff2 += "udp"
            elif (check_one == 1):
                self.in_proto_to_sniff2 += " or udp"
        if self.ui_sniffing_langsung.DHCP_only.isChecked():
            if (check_one == 0):
                check_one = 1
                self.in_proto_to_sniff2 += "port 68 or port 69"
            elif (check_one == 1):
                self.in_proto_to_sniff2 += " or port 68 or port 69"
        if self.ui_sniffing_langsung.HTTP_only.isChecked():
            if (check_one == 0):
                check_one = 1
                self.in_proto_to_sniff2 += "port 80"
            elif (check_one == 1):
                self.in_proto_to_sniff2 += " or port 80"

        # Validasi Pop UP
        if self.ui_sniffing_langsung.lineEdit.text() == kosong:
            msg = QMessageBox()
            msg.setWindowTitle("Peringatan")
            msg.setText("Pastikan untuk mengisi kolom jumlah paket")
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()
            # self.ui_sniffing_langsung.stop_sniff_btn.hide()
            # self.ui_sniffing_langsung.sniffing_btn.show()
        elif self.ui_sniffing_langsung.nama_file.text() == kosong:
            msg = QMessageBox()
            msg.setWindowTitle("Peringatan")
            msg.setText("Pastikan untuk mengisi kolom nama file")
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()
            # self.ui_sniffing_langsung.stop_sniff_btn.hide()
            # self.ui_sniffing_langsung.sniffing_btn.show()
        elif check_one == 0 :
            msg = QMessageBox()
            msg.setWindowTitle("Peringatan")
            msg.setText("Pastikan untuk memilih salah satu protokol")
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()
            # self.ui_sniffing_langsung.stop_sniff_btn.hide()
            # self.ui_sniffing_langsung.sniffing_btn.show()
        else:
            print(self.in_proto_to_sniff2)
            # net_scan = sniffing(self.in_net_iface, self.in_pkt_to_sniff2, self.in_proto_to_sniff2, self.name_file)
            # net_scan.start()
            net_iface = sniffing(self.in_net_iface, self.in_pkt_to_sniff2, self.in_proto_to_sniff2, self.name_file)
            id_hasil = net_iface.scan_network()
            res = int(''.join(map(str, id_hasil)))

            print("isi dari variabel ini adalah "+str(res))
            status =1
            self.startUI_hasilSniffing(res, status)

            # try:
            #     net_iface.scan_network()
            #     self.startUI_hasilSniffing()
            # except:
            #     self.ui_sniffing_langsung.stop_sniff_btn.show()
            #     self.ui_sniffing_langsung.sniffing_btn.hide()


    ###########################################################################################

    def startUI_hasilSniffing(self, id_hasil, status):
        # time.sleep(100)
        id = id_hasil
        print("Ini adalah penanda baris terakhir yg jalan1")
        self.ui_hasil_sniffing.setupUi(self, id_hasil)
        print("Ini adalah penanda baris terakhir yg jalan")
        qss_file = open('../resource/style.qss').read()
        self.ui_hasil_sniffing.label_3 = QtWidgets.QLabel(self.ui_hasil_sniffing.centralwidget)
        self.ui_hasil_sniffing.label_3.setText(str(status))
        self.ui_hasil_sniffing.label_3.hide()
        self.ui_hasil_sniffing.cek_glosarium_btn.clicked.connect(self.startUI_glosa_istilah)
        print("cek status "+str(status))

        if status == 0:
            self.ui_hasil_sniffing.kembali_btn3.clicked.connect(self.startUI_hasilSebelum)
            print("yg jalan ui sebelum")
        else:
            self.ui_hasil_sniffing.kembali_btn3.clicked.connect(self.startUI_SniffingLangsung)
            print("yg jalan ui sniffing")
        # qss_file = open('../resource/style.qss').read()

        # menerima hasil
        result = run_sql_all("SELECT id_tb_det_hasil, hasil_jadi, waktu FROM tb_det_hasil WHERE id_tb_hasil = '%s'" % (id_hasil))

        print(result)

        # self.ui_hasil_sniffing.tableWidget.setRowCount(0)
        # self.ui_hasil_sniffing.tableWidget.setColumnCount(4)

        self.ui_hasil_sniffing.detailButton = []



        # _translate = QtCore.QCoreApplication.translate
        # self.detailButton.setText(_translate("Hasil_sniffing", "Detail"))
        i = 0
        for row_number, row_data in enumerate(result):
            self.ui_hasil_sniffing.detailButton.append(row_number)

            self.ui_hasil_sniffing.tableWidget.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.ui_hasil_sniffing.tableWidget.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
                self.ui_hasil_sniffing.detailButton[i] = QtWidgets.QPushButton(self.ui_hasil_sniffing.centralwidget)
                self.ui_hasil_sniffing.detailButton[i].setObjectName("detailButton")
                self.ui_hasil_sniffing.detailButton[i].setStyleSheet(qss_file)
                self.ui_hasil_sniffing.detailButton[i].setText("Detail Paket")
                self.ui_hasil_sniffing.detailButton[i].clicked.connect(self.clickDetail2)
                self.ui_hasil_sniffing.tableWidget.setCellWidget(row_number, 3, self.ui_hasil_sniffing.detailButton[i])

            i += 1

        self.show()

    def clickDetail2(self):
        print("Ini sudah klik detail")
        index = self.ui_hasil_sniffing.tableWidget.currentIndex().row()
        print(index)
        id = self.ui_hasil_sniffing.tableWidget.item(index, 0)
        id_det_hasil = id.text()
        # id2 = self.ui_hasil_sniffing.tableWidget.item(index, 1)
        # id_hasil = id2.text()
        print(id_det_hasil)
        stat = self.ui_hasil_sniffing.label_3.text()
        print(stat)
        # print("ini id hasil "+id_hasil)
        self.startUI_hasil_detail(id_det_hasil, stat)

    def startUI_hasil_detail(self, id_det_hasil, stat):
        print("baru masuk ni")
        self.ui_hasil_detail.setupUi(self, id_det_hasil)
        self.ui_hasil_detail.status = stat
        self.ui_hasil_detail.id_hasil = run_sql_int("Select id_tb_hasil from tb_det_hasil where id_tb_det_hasil = '%s'" %(id_det_hasil))
        self.ui_hasil_detail.kembaliBtn_detail.clicked.connect(self.perantara_hasil_sniff)
        self.ui_hasil_detail.cek_glosarium_btn.clicked.connect(self.startUI_glosa_istilah)
        self.show()

    def perantara_hasil_sniff(self):
        status = self.ui_hasil_detail.status
        status2 = int(status)
        print("Ini stat "+status)
        res = self.ui_hasil_detail.id_hasil
        id_hasil = int(''.join(map(str, res)))
        print("Ini hasil "+str(id_hasil))
        self.startUI_hasilSniffing(id_hasil, status2)



    ######### Kuis ############################
    def startUI_kuis(self):
        self.ui_kuis.setupUi(self)
        # self.ui_kuis.kembaliBtn.clicked.connect(self.startUI_mainWindow)
        self.ui_kuis.menuAwalBtn.clicked.connect(self.startUI_mainWindow)
        self.ui_kuis.nilaiBtn.clicked.connect(self.klik_nilai)
        self.show()

    def klik_nilai(self):
        print("fungsi klik nilai")
        panjang_soal = run_sql_all("SELECT soal FROM soal_kuis")
        if len(panjang_soal) == len(self.ui_kuis.jawaban):

            print(self.ui_kuis.panjang_index)
            print(self.ui_kuis.jawaban)
            soal = check_soal(self.ui_kuis.jawaban, 0)
            hasil_nilai = soal.periksa_nilai()
            if hasil_nilai[0] == len(panjang_soal):
                self.startUI_hasil_kuis_benar()
            else:
                self.startUI_hasil_kuis(hasil_nilai)


        elif len(panjang_soal)-len(self.ui_kuis.jawaban)==1:
            if self.ui_kuis.pilihan1.isChecked():
                jawab = "pilihan1"
                self.ui_kuis.jawaban.append(jawab)
                print(self.ui_kuis.jawaban)
                soal = check_soal(self.ui_kuis.jawaban, 0)
                hasil_nilai = soal.periksa_nilai()
                if hasil_nilai[0] == len(panjang_soal):
                    self.startUI_hasil_kuis_benar()
                else:
                    self.startUI_hasil_kuis(hasil_nilai)
            elif self.ui_kuis.pilihan2.isChecked():
                jawab = "pilihan2"
                self.ui_kuis.jawaban.append(jawab)
                print(self.ui_kuis.jawaban)
                soal = check_soal(self.ui_kuis.jawaban, 0)
                hasil_nilai = soal.periksa_nilai()
                if hasil_nilai[0] == len(panjang_soal):
                    self.startUI_hasil_kuis_benar()
                else:
                    self.startUI_hasil_kuis(hasil_nilai)
            elif self.ui_kuis.pilihan3.isChecked():
                jawab = "pilihan3"
                self.ui_kuis.jawaban.append(jawab)
                print(self.ui_kuis.jawaban)
                soal = check_soal(self.ui_kuis.jawaban, 0)
                hasil_nilai = soal.periksa_nilai()
                if hasil_nilai[0] == len(panjang_soal):
                    self.startUI_hasil_kuis_benar()
                else:
                    self.startUI_hasil_kuis(hasil_nilai)
            elif self.ui_kuis.pilihan4.isChecked():
                jawab = "pilihan4"
                self.ui_kuis.jawaban.append(jawab)
                print(self.ui_kuis.jawaban)
                soal = check_soal(self.ui_kuis.jawaban, 0)
                hasil_nilai = soal.periksa_nilai()
                if hasil_nilai[0] == len(panjang_soal):
                    self.startUI_hasil_kuis_benar()
                else:
                    self.startUI_hasil_kuis(hasil_nilai)
            else:
                print("Pilihan habis")
        else:
            msg = QMessageBox()
            msg.setWindowTitle("Peringatan")
            msg.setText("Ada Soal yang Belum Dijawab")
            msg.setIcon(QMessageBox.Warning)
            msg.exec_()
            print("Ada soal yg belum dijawab")

    def startUI_hasil_kuis(self, hasil_nilai):
        self.ui_hasil_kuis.setupUi(self, hasil_nilai)
        self.ui_hasil_kuis.kembali_hasilKuisBtn.clicked.connect(self.startUI_kuis)
        self.show()
    def startUI_hasil_kuis_benar(self):
        self.ui_hasil_kuis_benar.setupUi(self)
        self.ui_hasil_kuis_benar.kembaliBtn.clicked.connect(self.startUI_kuis)
        self.show()
    ###################################################################


    ######## Glosarium ################

    def startUI_glosa_istilah(self):
        self.ui_glosa_istilah.setupUi(self)
        self.ui_glosa_istilah.kembaliBtn.clicked.connect(self.startUI_mainWindow)
        self.ui_glosa_istilah.sekilas_protokol.clicked.connect(self.startUI_glosa_protokol)
        self.show()

    def startUI_glosa_protokol(self):
        self.ui_glosa_protokol.setupUi(self)
        self.ui_glosa_protokol.kembaliBtn.clicked.connect(self.startUI_mainWindow)
        self.ui_glosa_protokol.sniff_app.clicked.connect(self.startUI_glosa_istilah)
        self.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    # mainWindow = QtWidgets.QMainWindow()
    # app = QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())
    # ui = MainWindow()
    # ui.setupUi(mainWindow)
    # mainWindow.show()
    # sys.exit(app.exec_())