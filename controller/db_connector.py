import mysql.connector


def run_sql(sql):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="packet_sniff"
    )

    if mydb.is_connected():
        print("Berhasil terhubung ke database")
    else:
        print("ada masalah")

    cursor = mydb.cursor()

    # sql = "Select kalimat1 from icmp_packet where flag='type==8'"

    cursor.execute(sql)

    rec = cursor.fetchone()

    str = "".join(rec)

    # str = "".join(records)
    #
    # print(str)
    # print(record)
    #
    return str

def run_sql_spec(sql):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="packet_sniff"
    )

    if mydb.is_connected():
        print("Berhasil terhubung ke database")
    else:
        print("ada masalah")

    cursor = mydb.cursor()

    # sql = "Select kalimat1 from icmp_packet where flag='type==8'"

    cursor.execute(sql)

    rec = cursor.fetchone()
    print (rec)

    # str = "".join(records)
    #
    # print(str)
    # print(record)
    #
    return rec

def run_sql_all(sql):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="packet_sniff"
    )

    if mydb.is_connected():
        print("Berhasil terhubung ke database dengan fungsi run_sql_all")
    else:
        print("ada masalah")

    cursor = mydb.cursor()

    cursor.execute(sql)
    result= cursor.fetchall()
    # print(result)

    return result

def insert_sql(sql):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="packet_sniff"
    )

    if mydb.is_connected():
        print("Berhasil terhubung ke database")
    else:
        print("ada masalah")

    cursor = mydb.cursor()

    cursor.execute(sql)

    mydb.commit()

    print(cursor.lastrowid, "record inserted.")
    last_id = cursor.lastrowid
    return last_id

def last_row_id():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="packet_sniff"
    )

    if mydb.is_connected():
        print("Berhasil terhubung ke database")
    else:
        print("ada masalah")

    cursor = mydb.cursor()

    cursor.execute("select * from tb_det_hasil")
    last_id = cursor.lastrowid
    return last_id

def update_sql(sql, param):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="packet_sniff"
    )

    if mydb.is_connected():
        print("Berhasil terhubung ke database")
    else:
        print("ada masalah")

    cursor = mydb.cursor()

    cursor.execute(sql, param)

    mydb.commit()

    print(cursor.rowcount, "record updated.")


def run_sql_int(sql):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        passwd="",
        database="packet_sniff"
    )

    if mydb.is_connected():
        print("Berhasil terhubung ke database")
    else:
        print("ada masalah")

    cursor = mydb.cursor()

    # sql = "Select kalimat1 from icmp_packet where flag='type==8'"

    cursor.execute(sql)

    a = cursor.fetchone()

    # str = "".join(records)
    #
    # print(str)
    # print(record)
    #
    return a
