from controller.db_connector import run_sql_all


class check_soal(object):
    def __init__(self, jawaban, index):

        self.jawaban_user = jawaban

        self.index = index

        self.row_soal = []
        self.row_pilihan1 = []
        self.row_pilihan2 = []
        self.row_pilihan3 = []
        self.row_pilihan4 = []
        self.row_jawaban = []

        coba = run_sql_all("SELECT soal, pilihan1, pilihan2, pilihan3, pilihan4, jawaban FROM soal_kuis")

        for row in coba:
            self.row_soal.append(row[0])
            self.row_pilihan1.append(row[1])
            self.row_pilihan2.append(row[2])
            self.row_pilihan3.append(row[3])
            self.row_pilihan4.append(row[4])
            self.row_jawaban.append(row[5])
        # print(self.row_soal)
    def awal_soal(self):
        self.soal_pertama = self.row_soal[0]
        self.pilihan1_pertama = self.row_pilihan1[0]
        self.pilihan2_pertama = self.row_pilihan2[0]
        self.pilihan3_pertama = self.row_pilihan3[0]
        self.pilihan4_pertama = self.row_pilihan4[0]

        self.index_saat_ini = self.row_soal.index(str(self.row_soal[0]))
        # print(self.index_saat_ini)

        return self.soal_pertama, self.pilihan1_pertama, self.pilihan2_pertama, self.pilihan3_pertama, self.pilihan4_pertama, self.index_saat_ini

    def soal_selanjutnya(self):
        i = self.index
        # print(i)
        #
        # print(self.row_soal[i])
        # self.jawaban_user.append(self.jawab)
        # print(self.jawaban_user)
        self.soal_skrg = self.row_soal[i]
        self.pilihan1_skrg = self.row_pilihan1[i]
        self.pilihan2_skrg = self.row_pilihan2[i]
        self.pilihan3_skrg = self.row_pilihan3[i]
        self.pilihan4_skrg = self.row_pilihan4[i]

        self.index_saat_ini = self.row_soal.index(str(self.row_soal[i]))

        return self.soal_skrg, self.pilihan1_skrg, self.pilihan2_skrg, self.pilihan3_skrg, self.pilihan4_skrg, self.index_saat_ini, self.jawaban_user

    def soal_sebelumnya(self):
        i = self.index
        print(i)

        print(self.row_soal[i])
        self.soal_skrg = self.row_soal[i]
        # print(self.soal_skrg)
        self.pilihan1_skrg = self.row_pilihan1[i]
        self.pilihan2_skrg = self.row_pilihan2[i]
        self.pilihan3_skrg = self.row_pilihan3[i]
        self.pilihan4_skrg = self.row_pilihan4[i]

        self.index_saat_ini = self.row_soal.index(str(self.row_soal[i]))

        return self.soal_skrg, self.pilihan1_skrg, self.pilihan2_skrg, self.pilihan3_skrg, self.pilihan4_skrg, self.index_saat_ini

    def periksa_nilai(self):
        self.score = 0
        i=0
        index_soal_salah = []
        print("fungsi periksa nilai")
        print(self.row_jawaban)
        print(self.jawaban_user)
        for j in range(len(self.row_jawaban)):
            print(j)
            print("ini isi row jawaban " + self.row_jawaban[j])
            print("ini isi row jawaban user " + self.jawaban_user[j])
            if str(self.row_jawaban[j]) == str(self.jawaban_user[j]):
                print("udah bner sama jawabannya")
                self.score += 1
                print("Scorenya adalah " + str(self.score))

            else:
                index_soal_salah.append(j)
                print(index_soal_salah)
        # if len(self.row_jawaban) == len(self.jawaban_user):
        #     print("udah bner sama panjangnya")
        #
        #     for j in range(len(self.row_jawaban)):
        #         print(j)
        #         print("ini isi row jawaban "+self.row_jawaban[j])
        #         print("ini isi row jawaban user "+self.jawaban_user[j])
        #         if str(self.row_jawaban[j]) == str(self.jawaban_user[j]):
        #             print("udah bner sama jawabannya")
        #             self.score += 1
        #             print("Scorenya adalah "+str(self.score))
        #
        #         else:
        #             no_soal_salah.append(j+1)
        # else:
        #     print("Periksa jawaban lagi")

        print("Nilai-nya adalah " + str(self.score))
        return self.score, index_soal_salah, self.jawaban_user

    def ambil_soal(self):
        soal = self.row_soal[self.index]
        jawaban = self.row_jawaban[self.index]
        return soal, jawaban
