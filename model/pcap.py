from controller.db_connector import run_sql_all

coba = run_sql_all("SELECT soal, pilihan1, pilihan2, pilihan3, pilihan4 FROM soal_kuis ")



for row in coba:
    print("Pertanyaan "+row[0])
    print("Pilihan 1 "+row[1])
    print("Pilihan 2 " + row[2])
    print("Pilihan 3 " + row[3])
    print("Pilihan 4 " + row[4])
