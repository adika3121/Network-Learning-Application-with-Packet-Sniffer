# Importing the necessary modules
import logging
from datetime import datetime
import subprocess
import sys
from os import path
from pathlib import Path

import pcapkit
import psutil as psutil
import json
from PyQt5 import QtCore, QtGui, QtWidgets
# import wxPython
# from wx import xrc

# This will suppress all messages that have a lower level of seriousness than error messages, while running or loading Scapy
# from pip._vendor import ipaddress
import self as self
from scapy.layers import dns
from scapy.layers.dhcp import BOOTP, DHCP
import time
from scapy.layers.dns import DNS, DNSRRSOA, DNSRR
from scapy.layers.inet import IP, ICMP, TCP, UDP
from scapy.layers.http import HTTPRequest  # import HTTP packet
from scapy.layers.inet6 import IPv6
from scapy.layers.l2 import ARP

# from view import input2
# from view.input2 import *
# from controller.MainWindow import MainWindow
from controller.db_connector import run_sql, insert_sql, update_sql, run_sql_int, last_row_id
# from view.MainWindow import *
# from view.MainWindow import MainWindow

from view.hasil_pcap import Ui_hasil_sniff
from view.hasil_sniffing2 import Ui_hasil_sniffing2

logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
logging.getLogger("scapy.interactive").setLevel(logging.ERROR)
logging.getLogger("scapy.loading").setLevel(logging.ERROR)

try:
    from scapy.all import *

except ImportError:
    print("Scapy package for Python is not installed on your system.")
    sys.exit()


class sniffing(object):

    def __init__(self, value1, value2, value4, value5):
        self.pkt_to_sniff = value2
        self.net_iface = value1
        self.proto_to_sniff = value4
        self.file_name = value5
        self.stop_sniffing = False

    def ngeprint(self):
        print(self.net_iface)

    def scan_network(self):
        net_iface = self.net_iface

        # try:
        #     subprocess.call(["ifconfig", net_iface, "promisc"], stdout=None, stderr=None, shell=False)
        #
        # except:
        #     print("\nFailed to configure interface as promiscuous.\n")
        #
        # else:
        #     # Executed if the try clause does not raise an exception
        #     print("\nInterface %s was set to PROMISC mode.\n" % net_iface)
        addrs = psutil.net_if_addrs()
        print(addrs.keys())
        pkt_to_sniff = self.pkt_to_sniff

        # Considering the case when the user enters 0 (infinity)
        if int(pkt_to_sniff) != 0:
            print("\nThe program will capture %d packets.\n" % int(pkt_to_sniff))

        elif int(pkt_to_sniff) == 0:
            print("\nThe program will capture packets until the timeout expires.\n")

        # time_to_sniff = self.time_to_sniff
        #
        # # Handling the value entered by the user
        # if int(time_to_sniff) != 0:
        #     print("\nThe program will capture packets for %d seconds.\n" % int(time_to_sniff))

        proto_sniff = self.proto_to_sniff
        print(proto_sniff)

        print("\nThe program will capture only %s packets.\n" % proto_sniff.upper())
        # if proto_sniff in ["arp", "icmp", "port 53", "tcp", "udp", "port 68 or port 69", "port 80"
        #     , "arp or icmp or udp or port 53 or port 68 or port 69 or tcp"]:
        #     print("\nThe program will capture only %s packets.\n" % proto_sniff.upper())
        #
        # # Considering the case when the user enters 0 (meaning all protocols)
        # # if (proto_sniff == "arp") or (proto_sniff == "icmp") or (
        # #         proto_sniff == "port 53") or (proto_sniff == "tcp") or (proto_sniff == "udp") or (
        # #         proto_sniff == "port 68 or port 69") or (proto_sniff == "port 80"):
        # #     print("\nThe program will capture only %s packets.\n" % proto_sniff.upper())
        #
        # elif (proto_sniff) == "arp or icmp or udp or port 53 or port 80 or port 68 or port 69 or tcp":
        #     print("\nThe program will capture all protocols.\n")

        file_name = self.file_name
        data_folder = Path("hasil/")
        file_to_open = data_folder/file_name

        # Creating the text file (if it doesn't exist) for packet logging and/or opening it for appending
        sniffer_log = open(file_to_open, "a")
        # snif2 = open("snif2", "a")
        now = time.strftime('%Y-%m-%d %H:%M:%S')
        query_tb_hasil = "INSERT INTO `packet_sniff`.`tb_hasil` (`nama_hasil`, `tgl_n_waktu`) VALUES ('%s', '%s');" % (file_name,now)
        insert_sql(query_tb_hasil)

        rows_id = []


        # Fungsi untuk menemukan beberapa parameter untuk DHCP
        def get_option(dhcp_options, key):

            must_decode = ['hostname', 'domain', 'vendor_class_id']
            try:
                for i in dhcp_options:
                    if i[0] == key:
                        # If DHCP Server Returned multiple name servers
                        # return all as comma seperated string.
                        if key == 'name_server' and len(i) > 2:
                            return ",".join(i[1:])
                        # domain and hostname are binary strings,
                        # decode to unicode string before returning
                        elif key in must_decode:
                            return i[1].decode()
                        else:
                            return i[1]
            except:
                pass

        # This is the function that will be called for each captured packet
        # The function will extract parameters from the packet and then log each packet to the log file
        def packet_log(packet):
            # Getting the current timestamp
            waktu = datetime.now()
            now = time.strftime('%Y-%m-%d %H:%M:%S')

            # Writing the packet information to the log file, also considering the protocol or 0 for all protocols
            # if proto_sniff == "icmp":
            print ("ini jumlah awal packet "+ str(len(packet)))
            translate = ""
            if ARP in packet:
                if packet[ARP].op == 1:
                    # Save ke database
                    query_id = "SELECT MAX(id_tb_hasil) FROM tb_hasil"
                    id_hasil = run_sql_int(query_id)
                    translate = "[ARP]\t "+ run_sql("select kalimat2 from arp_packet where flag='op_1'") + str(
                        packet[ARP].psrc) + run_sql("select kalimat3 from arp_packet where flag='op_1'") + str(packet[ARP].pdst)
                    query = "INSERT INTO `packet_sniff`.`tb_det_hasil` (`id_tb_hasil`,`hasil_jadi`, `waktu`) VALUES ('%s', '%s', '%s')" % (id_hasil[0],
                        translate, now)

                    id_row = insert_sql(query)
                    rows_id.append(id_row)

                    # Save ke File TXT
                    print("[ARP]\t "+run_sql("select kalimat1 from arp_packet where flag='op_1'") + str(now) + run_sql("select kalimat2 from arp_packet where flag='op_1'") + str(
                        packet[ARP].psrc) + run_sql("select kalimat3 from arp_packet where flag='op_1'") + str(packet[ARP].pdst),
                          file=sniffer_log)
                elif packet[ARP].op == 2:
                    # Save ke database
                    query_id = "SELECT MAX(id_tb_hasil) FROM tb_hasil"
                    id_hasil = run_sql_int(query_id)
                    translate = "[ARP]\t " + run_sql("select kalimat2 from arp_packet where flag='op_2'") + str(
                        packet[ARP].psrc) + run_sql("select kalimat3 from arp_packet where flag='op_2'") + str(
                        packet[ARP].hwsrc)
                    query = "INSERT INTO `packet_sniff`.`tb_det_hasil` (`id_tb_hasil`,`hasil_jadi`, `waktu`) VALUES ('%s', '%s', '%s')" % (id_hasil[0], translate, now)

                    id_row = insert_sql(query)
                    rows_id.append(id_row)

                    # Save ke File TXT
                    print("[ARP]\t "+run_sql("select kalimat2 from arp_packet where flag='op_2'") + str(
                        packet[ARP].psrc) + run_sql("select kalimat3 from arp_packet where flag='op_2'") + str(
                        packet[ARP].hwsrc), file=sniffer_log)
                else:
                    # Save ke database
                    query_id = "SELECT MAX(id_tb_hasil) FROM tb_hasil"
                    id_hasil = run_sql_int(query_id)
                    translate = "[ARP]\t Paket ARP lainnya"
                    query = "INSERT INTO `packet_sniff`.`tb_det_hasil` (`id_tb_hasil`,`hasil_jadi`, `waktu`) VALUES ('%s', '%s', '%s')" % (
                    id_hasil[0], translate, now)

                    id_row = insert_sql(query)
                    rows_id.append(id_row)

            elif ICMP in packet:
                if packet[ICMP].type == 8:
                    # Save ke Database
                    query_id = "SELECT MAX(id_tb_hasil) FROM tb_hasil"
                    id_hasil = run_sql_int(query_id)
                    translate ="[ICMP]\t "+run_sql("Select kalimat1 from icmp_packet where flag='type==8'") + str(now) + run_sql("Select kalimat2 from icmp_packet where flag='type==8'") + str(
                        packet[IP].src) + run_sql("Select kalimat3 from icmp_packet where flag='type==8'") + str(
                        packet[IP].dst)
                    query = "INSERT INTO `packet_sniff`.`tb_det_hasil` (`id_tb_hasil`,`hasil_jadi`, `waktu`) VALUES ('%s', '%s', '%s')" % (id_hasil[0], translate, now)

                    id_row = insert_sql(query)
                    rows_id.append(id_row)

                    # Save ke File TXT
                    print("[ICMP]\t "+run_sql("Select kalimat1 from icmp_packet where flag='type==8'") + str(now) + run_sql("Select kalimat2 from icmp_packet where flag='type==8'") + str(
                        packet[IP].src) + run_sql("Select kalimat3 from icmp_packet where flag='type==8'") + str(
                        packet[IP].dst), file=sniffer_log)
                elif packet[ICMP].type == 0:
                    # Save ke Database
                    query_id = "SELECT MAX(id_tb_hasil) FROM tb_hasil"
                    id_hasil = run_sql_int(query_id)
                    translate = "[ICMP]\t "+run_sql("Select kalimat1 from icmp_packet where flag='type==0'") + str(now) + run_sql("Select kalimat2 from icmp_packet where flag='type==0'") + str(packet[IP].src)+ run_sql("Select kalimat3 from icmp_packet where flag='type==0'") + str(
                            packet[IP].dst)
                    query = "INSERT INTO `packet_sniff`.`tb_det_hasil` (`id_tb_hasil`,`hasil_jadi`, `waktu`) VALUES ('%s', '%s', '%s')" % (id_hasil[0], translate, now)

                    id_row = insert_sql(query)
                    rows_id.append(id_row)

                    # Save ke File TXT
                    print(
                        "[ICMP]\t "+run_sql("Select kalimat1 from icmp_packet where flag='type==0'") + str(now) + run_sql("Select kalimat2 from icmp_packet where flag='type==0'") + str(packet[IP].src)
                        + run_sql("Select kalimat3 from icmp_packet where flag='type==0'") + str(
                            packet[IP].dst), file=sniffer_log)
                elif packet[ICMP].type == 3 and packet[ICMP].code == 0:
                    # Save ke Database
                    query_id = "SELECT MAX(id_tb_hasil) FROM tb_hasil"
                    id_hasil = run_sql_int(query_id)
                    translate = "[ICMP]\t " + run_sql("Select kalimat1 from icmp_packet where flag='type==3&&code==0'") + str(packet[IP].src) + run_sql("Select kalimat2 from icmp_packet where flag='type==3&&code==0'") + str(
                        packet[IP].dst) + run_sql("Select kalimat3 from icmp_packet where flag='type==3&&code==0'")
                    query = "INSERT INTO `packet_sniff`.`tb_det_hasil` (`id_tb_hasil`,`hasil_jadi`, `waktu`) VALUES ('%s', '%s', '%s')" % (
                    id_hasil[0], translate, now)

                    id_row = insert_sql(query)
                    rows_id.append(id_row)
                elif packet[ICMP].type == 3 and packet[ICMP].code == 1:
                    # Save ke Database
                    query_id = "SELECT MAX(id_tb_hasil) FROM tb_hasil"
                    id_hasil = run_sql_int(query_id)
                    translate = "[ICMP]\t " + run_sql(
                        "Select kalimat1 from icmp_packet where flag='type==3&&code==1'") + str(
                        packet[IP].src) + run_sql(
                        "Select kalimat2 from icmp_packet where flag='type==3&&code==1'") + str(
                        packet[IP].dst) + run_sql("Select kalimat3 from icmp_packet where flag='type==3&&code==1'")
                    query = "INSERT INTO `packet_sniff`.`tb_det_hasil` (`id_tb_hasil`,`hasil_jadi`, `waktu`) VALUES ('%s', '%s', '%s')" % (
                        id_hasil[0], translate, now)

                    id_row = insert_sql(query)
                    rows_id.append(id_row)
                elif packet[ICMP].type == 3 and packet[ICMP].code ==2:
                    # Save ke Database
                    query_id = "SELECT MAX(id_tb_hasil) FROM tb_hasil"
                    id_hasil = run_sql_int(query_id)
                    translate = "[ICMP]\t " + run_sql(
                        "Select kalimat1 from icmp_packet where flag='type==3&&code==2'") + str(
                        packet[IP].src) + run_sql(
                        "Select kalimat2 from icmp_packet where flag='type==3&&code==2'") + str(
                        packet[IP].dst) + run_sql("Select kalimat3 from icmp_packet where flag='type==3&&code==2'")
                    query = "INSERT INTO `packet_sniff`.`tb_det_hasil` (`id_tb_hasil`,`hasil_jadi`, `waktu`) VALUES ('%s', '%s', '%s')" % (
                        id_hasil[0], translate, now)

                    id_row = insert_sql(query)
                    rows_id.append(id_row)
                elif packet[ICMP].type == 3 and packet[ICMP].code == 3:
                    # Save ke Database
                    query_id = "SELECT MAX(id_tb_hasil) FROM tb_hasil"
                    id_hasil = run_sql_int(query_id)
                    translate = "[ICMP]\t " + run_sql(
                        "Select kalimat1 from icmp_packet where flag='type==3&&code==3'") + str(
                        packet[IP].src) + run_sql(
                        "Select kalimat2 from icmp_packet where flag='type==3&&code==3'") + str(
                        packet[IP].dst) + run_sql("Select kalimat3 from icmp_packet where flag='type==3&&code==3'")
                    query = "INSERT INTO `packet_sniff`.`tb_det_hasil` (`id_tb_hasil`,`hasil_jadi`, `waktu`) VALUES ('%s', '%s', '%s')" % (
                        id_hasil[0], translate, now)

                    id_row = insert_sql(query)
                    rows_id.append(id_row)
                elif packet[ICMP].type == 3 and packet[ICMP].code == 4:
                    # Save ke Database
                    query_id = "SELECT MAX(id_tb_hasil) FROM tb_hasil"
                    id_hasil = run_sql_int(query_id)
                    translate = "[ICMP]\t " + run_sql(
                        "Select kalimat1 from icmp_packet where flag='type==3&&code==4'") + str(
                        packet[IP].src) + run_sql(
                        "Select kalimat2 from icmp_packet where flag='type==3&&code==4'") + str(
                        packet[IP].dst) + run_sql("Select kalimat3 from icmp_packet where flag='type==3&&code==4'")
                    query = "INSERT INTO `packet_sniff`.`tb_det_hasil` (`id_tb_hasil`,`hasil_jadi`, `waktu`) VALUES ('%s', '%s', '%s')" % (
                        id_hasil[0], translate, now)

                    id_row = insert_sql(query)
                    rows_id.append(id_row)
                elif packet[ICMP].type == 3 and packet[ICMP].code == 5:
                    # Save ke Database
                    query_id = "SELECT MAX(id_tb_hasil) FROM tb_hasil"
                    id_hasil = run_sql_int(query_id)
                    translate = "[ICMP]\t " + run_sql(
                        "Select kalimat1 from icmp_packet where flag='type==3&&code==5'") + str(
                        packet[IP].src) + run_sql(
                        "Select kalimat2 from icmp_packet where flag='type==3&&code==5'") + str(
                        packet[IP].dst) + run_sql("Select kalimat3 from icmp_packet where flag='type==3&&code==5'")
                    query = "INSERT INTO `packet_sniff`.`tb_det_hasil` (`id_tb_hasil`,`hasil_jadi`, `waktu`) VALUES ('%s', '%s', '%s')" % (
                        id_hasil[0], translate, now)

                    id_row = insert_sql(query)
                    rows_id.append(id_row)
                elif packet[ICMP].type == 3 and packet[ICMP].code == 6:
                    # Save ke Database
                    query_id = "SELECT MAX(id_tb_hasil) FROM tb_hasil"
                    id_hasil = run_sql_int(query_id)
                    translate = "[ICMP]\t " + run_sql(
                        "Select kalimat1 from icmp_packet where flag='type==3&&code==6'") + str(
                        packet[IP].src) + run_sql(
                        "Select kalimat2 from icmp_packet where flag='type==3&&code==6'") + str(
                        packet[IP].dst) + run_sql("Select kalimat3 from icmp_packet where flag='type==3&&code==6'")
                    query = "INSERT INTO `packet_sniff`.`tb_det_hasil` (`id_tb_hasil`,`hasil_jadi`, `waktu`) VALUES ('%s', '%s', '%s')" % (
                        id_hasil[0], translate, now)

                    id_row = insert_sql(query)
                    rows_id.append(id_row)
                elif packet[ICMP].type == 3 and packet[ICMP].code == 7:
                    # Save ke Database
                    query_id = "SELECT MAX(id_tb_hasil) FROM tb_hasil"
                    id_hasil = run_sql_int(query_id)
                    translate = "[ICMP]\t " + run_sql(
                        "Select kalimat1 from icmp_packet where flag='type==3&&code==7'") + str(
                        packet[IP].src) + run_sql(
                        "Select kalimat2 from icmp_packet where flag='type==3&&code==7'") + str(
                        packet[IP].dst) + run_sql("Select kalimat3 from icmp_packet where flag='type==3&&code==7'")
                    query = "INSERT INTO `packet_sniff`.`tb_det_hasil` (`id_tb_hasil`,`hasil_jadi`, `waktu`) VALUES ('%s', '%s', '%s')" % (
                        id_hasil[0], translate, now)

                    id_row = insert_sql(query)
                    rows_id.append(id_row)
                else:
                    # Save ke Database
                    query_id = "SELECT MAX(id_tb_hasil) FROM tb_hasil"
                    id_hasil = run_sql_int(query_id)
                    translate = "[ICMP]\t Paket ICMP lainnya"
                    query = "INSERT INTO `packet_sniff`.`tb_det_hasil` (`id_tb_hasil`,`hasil_jadi`, `waktu`) VALUES ('%s', '%s', '%s')" % (
                        id_hasil[0], translate, now)

                    id_row = insert_sql(query)
                    rows_id.append(id_row)

            elif DNS in packet:
                if IP in packet:
                    ip_src = packet[IP].src
                    ip_dst = packet[IP].dst
                    if packet.haslayer(DNS) and packet.getlayer(DNS).qr == 0:
                        url = str(packet.getlayer(DNS).qd.qname.decode())
                        url_trans = url.replace("'","")
                        print(url)
                        print(url_trans)

                        dns_kal1 = "Select kalimat1 from dns_packet where flag = 'query'"
                        dns_kal2 = "Select kalimat2 from dns_packet where flag = 'query'"
                        dns_kal3 = "Select kalimat3 from dns_packet where flag = 'query'"

                        # Save ke Database
                        query_id = "SELECT MAX(id_tb_hasil) FROM tb_hasil"
                        id_hasil = run_sql_int(query_id)
                        translate = f"[DNS]\t {run_sql(dns_kal1)} {str(ip_src)} {run_sql(dns_kal2)} " \
                                    f"{url_trans} {run_sql(dns_kal3)}" \
                                    f" {str(ip_dst)} "
                        query = "INSERT INTO `packet_sniff`.`tb_det_hasil` (`id_tb_hasil`,`hasil_jadi`, `waktu`) VALUES ('%s', '%s', '%s')" % (id_hasil[0], translate, now)

                        id_row = insert_sql(query)
                        rows_id.append(id_row)

                        # Save ke File TXT
                        print("[DNS]\t "+run_sql("Select kalimat1 from dns_packet") + str(ip_src) + run_sql("Select kalimat2 from dns_packet") + str(
                            packet.getlayer(DNS).qd.qname) + run_sql("Select kalimat3 from dns_packet") + str(ip_dst),
                              file=sniffer_log)
                    elif packet.haslayer(DNS) and packet.getlayer(DNS).qr == 1:
                        url = str(packet.getlayer(DNS).qd.qname.decode())
                        url_trans = url.replace("'", "")
                        ip_url = []

                        # ip_url.append(DNS.an.rdata)

                        if packet.haslayer(DNSRR):
                            for i in range(packet.getlayer(DNS).ancount):
                                dnsrr = packet.getlayer(DNS).an[i]
                                if dnsrr.rdata is not None:
                                    if type(dnsrr.rdata) == str:
                                        status_dns_r = 0
                                        ip_url.append(dnsrr.rdata)
                                    # elif type(dnsrr.rdata) == bytes:
                                    #     break
                                else:
                                    break

                            print(ip_url)
                            print(type(ip_url))

                            record = ', '.join(ip_url)
                            # if status_dns_r == 0:
                            #     record = ', '.join(ip_url)
                            # elif status_dns_r == 1:
                            #     record = ''.join(map(bytes.decode, ip_url))

                            print(record)

                            dns_kal1_r2 = "Select kalimat1 from dns_packet where flag = 'response'"
                            dns_kal2_r2 = "Select kalimat2 from dns_packet where flag = 'response'"
                            dns_kal3_r2 = "Select kalimat3 from dns_packet where flag = 'response'"
                            dns_kal4_r2 = "Select kalimat4 from dns_packet where flag = 'response'"

                            # Save ke Database
                            query_id = "SELECT MAX(id_tb_hasil) FROM tb_hasil"
                            id_hasil = run_sql_int(query_id)
                            translate = f"[DNS]\t {run_sql(dns_kal1_r2)} {str(ip_src)} {run_sql(dns_kal2_r2)} " \
                                        f"{str(ip_dst)} {run_sql(dns_kal3_r2)} {url_trans} {run_sql(dns_kal4_r2)} " \
                                        f" {str(record)} "

                            print(translate)
                            # {str(record)}
                            query = "INSERT INTO `packet_sniff`.`tb_det_hasil` (`id_tb_hasil`,`hasil_jadi`, `waktu`) VALUES ('%s', '%s', '%s')" % (id_hasil[0], translate, now)

                            id_row = insert_sql(query)
                            rows_id.append(id_row)
                        elif packet.haslayer(DNSRRSOA):
                            url = str(packet.getlayer(DNS).qd.qname.decode())
                            url_trans = url.replace("'", "")

                            url_auth = packet.getlayer(DNSRRSOA).rrname.decode()

                            dns_kal1_r3 = "Select kalimat1 from dns_packet where flag = 'SOA'"
                            dns_kal2_r3 = "Select kalimat2 from dns_packet where flag = 'SOA'"
                            dns_kal3_r3 = "Select kalimat3 from dns_packet where flag = 'SOA'"
                            dns_kal4_r4 = "Select kalimat4 from dns_packet where flag = 'SOA'"

                            # Save ke Database
                            query_id = "SELECT MAX(id_tb_hasil) FROM tb_hasil"
                            id_hasil = run_sql_int(query_id)
                            translate = f"[DNS SOA]\t {run_sql(dns_kal1_r3)} {str(ip_src)} {run_sql(dns_kal2_r3)} " \
                                        f"{str(ip_dst)} {run_sql(dns_kal3_r3)} {url_trans} {run_sql(dns_kal4_r4)} " \
                                        f" {str(url_auth)} "

                            print(translate)
                            # {str(record)}
                            query = "INSERT INTO `packet_sniff`.`tb_det_hasil` (`id_tb_hasil`,`hasil_jadi`, `waktu`) VALUES ('%s', '%s', '%s')" % (id_hasil[0], translate, now)
                            id_row = insert_sql(query)
                            rows_id.append(id_row)
                        else:
                            url = str(packet.getlayer(DNS).qd.qname.decode())
                            url_trans = url.replace("'", "")
                            print(url)
                            print(url_trans)

                            dns_kal1 = "Select kalimat1 from dns_packet where flag = 'query'"
                            dns_kal2 = "Select kalimat2 from dns_packet where flag = 'query'"
                            dns_kal3 = "Select kalimat3 from dns_packet where flag = 'query'"

                            # Save ke Database
                            query_id = "SELECT MAX(id_tb_hasil) FROM tb_hasil"
                            id_hasil = run_sql_int(query_id)
                            translate = f"[DNS]\t {run_sql(dns_kal1)} {str(ip_src)} {run_sql(dns_kal2)} " \
                                        f"{url_trans} {run_sql(dns_kal3)}" \
                                        f" {str(ip_dst)} "
                            query = "INSERT INTO `packet_sniff`.`tb_det_hasil` (`id_tb_hasil`,`hasil_jadi`, `waktu`) VALUES ('%s', '%s', '%s')" % (id_hasil[0], translate, now)

                            id_row = insert_sql(query)
                            rows_id.append(id_row)
                    else:
                        # Save ke Database
                        query_id = "SELECT MAX(id_tb_hasil) FROM tb_hasil"
                        id_hasil = run_sql_int(query_id)
                        translate = f"[DNS]\t Paket DNS Lainnya"
                        query = "INSERT INTO `packet_sniff`.`tb_det_hasil` (`id_tb_hasil`,`hasil_jadi`, `waktu`) VALUES ('%s', '%s', '%s')" % (
                        id_hasil[0], translate, now)

                        id_row = insert_sql(query)
                        rows_id.append(id_row)




                elif IPv6 in packet:
                    ip_src = packet[IPv6].src
                    ip_dst = packet[IPv6].dst
                    if packet.haslayer(DNS) and packet.getlayer(DNS).qr == 0:
                        url = str(packet.getlayer(DNS).qd.qname.decode())
                        url_trans = url.replace("'", "")
                        print(url)
                        print(url_trans)

                        dns_kal1_q = "Select kalimat1 from dns_packet where flag = 'query'"
                        dns_kal2_q = "Select kalimat2 from dns_packet where flag = 'query'"
                        dns_kal3_q = "Select kalimat3 from dns_packet where flag = 'query'"

                        # Save ke Database
                        query_id = "SELECT MAX(id_tb_hasil) FROM tb_hasil"
                        id_hasil = run_sql_int(query_id)
                        translate = f"[DNS]\t {run_sql(dns_kal1_q)} {str(ip_src)} {run_sql(dns_kal2_q)} " \
                                    f"{url_trans} {run_sql(dns_kal3_q)}" \
                                    f" {str(ip_dst)} "
                        query = "INSERT INTO `packet_sniff`.`tb_det_hasil` (`id_tb_hasil`,`hasil_jadi`, `waktu`) VALUES ('%s', '%s', '%s')" % (id_hasil[0], translate, now)

                        id_row = insert_sql(query)
                        rows_id.append(id_row)

                        # Save ke File TXT
                        print("[DNS]\t " + run_sql("Select kalimat1 from dns_packet") + str(ip_src) + run_sql(
                            "Select kalimat2 from dns_packet") + str(
                            packet.getlayer(DNS).qd.qname) + run_sql("Select kalimat3 from dns_packet") + str(ip_dst),
                              file=sniffer_log)
                    elif packet.haslayer(DNS) and packet.getlayer(DNS).qr == 1:
                        url = str(packet.getlayer(DNS).qd.qname.decode())
                        url_trans = url.replace("'", "")
                        ip_url = []



                        # ip_url.append(DNS.an.rdata)

                        if packet.haslayer(DNSRR):
                            for i in range(packet.getlayer(DNS).ancount):
                                dnsrr = packet.getlayer(DNS).an[i]
                                if dnsrr.rdata is not None:
                                    if type(dnsrr.rdata) == str:
                                        status_dns_r = 0
                                        ip_url.append(dnsrr.rdata)
                                    # elif type(dnsrr.rdata) == bytes:
                                    #     break
                                else:
                                    break

                            print(ip_url)
                            print(type(ip_url))

                            record = ', '.join(ip_url)
                            # if status_dns_r == 0:
                            #     record = ', '.join(ip_url)
                            # elif status_dns_r == 1:
                            #     record = ''.join(map(bytes.decode, ip_url))

                            print(record)

                            dns_kal1_r2 = "Select kalimat1 from dns_packet where flag = 'response'"
                            dns_kal2_r2 = "Select kalimat2 from dns_packet where flag = 'response'"
                            dns_kal3_r2 = "Select kalimat3 from dns_packet where flag = 'response'"
                            dns_kal4_r2 = "Select kalimat4 from dns_packet where flag = 'response'"

                            # Save ke Database
                            query_id = "SELECT MAX(id_tb_hasil) FROM tb_hasil"
                            id_hasil = run_sql_int(query_id)
                            translate = f"[DNS]\t {run_sql(dns_kal1_r2)} {str(ip_src)} {run_sql(dns_kal2_r2)} " \
                                        f"{str(ip_dst)} {run_sql(dns_kal3_r2)} {url_trans} {run_sql(dns_kal4_r2)} " \
                                        f" {str(record)} "

                            print(translate)
                            # {str(record)}
                            query = "INSERT INTO `packet_sniff`.`tb_det_hasil` (`id_tb_hasil`,`hasil_jadi`, `waktu`) VALUES ('%s', '%s', '%s')" % (id_hasil[0], translate, now)

                            id_row = insert_sql(query)
                            rows_id.append(id_row)
                        elif packet.haslayer(DNSRRSOA):
                            url = str(packet.getlayer(DNS).qd.qname.decode())
                            url_trans = url.replace("'", "")

                            url_auth = packet.getlayer(DNSRRSOA).rrname.decode()

                            dns_kal1_r3 = "Select kalimat1 from dns_packet where flag = 'SOA'"
                            dns_kal2_r3 = "Select kalimat2 from dns_packet where flag = 'SOA'"
                            dns_kal3_r3 = "Select kalimat3 from dns_packet where flag = 'SOA'"
                            dns_kal4_r4 = "Select kalimat4 from dns_packet where flag = 'SOA'"

                            # Save ke Database
                            query_id = "SELECT MAX(id_tb_hasil) FROM tb_hasil"
                            id_hasil = run_sql_int(query_id)
                            translate = f"[DNS SOA]\t {run_sql(dns_kal1_r3)} {str(ip_src)} {run_sql(dns_kal2_r3)} " \
                                        f"{str(ip_dst)} {run_sql(dns_kal3_r3)} {url_trans} {run_sql(dns_kal4_r4)} " \
                                        f" {str(url_auth)} "

                            print(translate)
                            # {str(record)}
                            query = "INSERT INTO `packet_sniff`.`tb_det_hasil` (`id_tb_hasil`,`hasil_jadi`, `waktu`) VALUES ('%s', '%s', '%s')" % (id_hasil[0], translate, now)
                            id_row = insert_sql(query)
                            rows_id.append(id_row)
                        else:
                            url = str(packet.getlayer(DNS).qd.qname.decode())
                            url_trans = url.replace("'", "")
                            print(url)
                            print(url_trans)

                            dns_kal1 = "Select kalimat1 from dns_packet where flag = 'query'"
                            dns_kal2 = "Select kalimat2 from dns_packet where flag = 'query'"
                            dns_kal3 = "Select kalimat3 from dns_packet where flag = 'query'"

                            # Save ke Database
                            query_id = "SELECT MAX(id_tb_hasil) FROM tb_hasil"
                            id_hasil = run_sql_int(query_id)
                            translate = f"[DNS]\t {run_sql(dns_kal1)} {str(ip_src)} {run_sql(dns_kal2)} " \
                                        f"{url_trans} {run_sql(dns_kal3)}" \
                                        f" {str(ip_dst)} "
                            query = "INSERT INTO `packet_sniff`.`tb_det_hasil` (`id_tb_hasil`,`hasil_jadi`, `waktu`) VALUES ('%s', '%s', '%s')" % (id_hasil[0], translate, now)

                            id_row = insert_sql(query)
                            rows_id.append(id_row)
                    else:
                        # Save ke Database
                        query_id = "SELECT MAX(id_tb_hasil) FROM tb_hasil"
                        id_hasil = run_sql_int(query_id)
                        translate = f"[DNS]\t Paket DNS Lainnya"
                        query = "INSERT INTO `packet_sniff`.`tb_det_hasil` (`id_tb_hasil`,`hasil_jadi`, `waktu`) VALUES ('%s', '%s', '%s')" % (
                        id_hasil[0], translate, now)

                        id_row = insert_sql(query)
                        rows_id.append(id_row)


            # Untuk HTTP
            elif packet.haslayer(HTTPRequest):
                # if this packet is an HTTP Request
                # get the requested URL
                url = packet[HTTPRequest].Host.decode() + packet[HTTPRequest].Path.decode()
                # get the requester's IP Address
                ip = packet[IP].src
                # get the request method
                method = packet[HTTPRequest].Method.decode()
                # SQL command
                sql_http_req_kal1 = "Select kalimat1 from http_packet where flag = 'http_request'"
                sql_http_req_kal2 = "Select kalimat2 from http_packet where flag = 'http_request'"
                sql_http_req_kal3 = "Select kalimat3 from http_packet where flag = 'http_request'"
                sql_http_post = "Select kalimat1 from http_packet where flag = 'method==post'"

                # Save ke database
                query_id = "SELECT MAX(id_tb_hasil) FROM tb_hasil"
                id_hasil = run_sql_int(query_id)
                translate = f"[<HTTP>]\t {run_sql(sql_http_req_kal1)} {ip} {run_sql(sql_http_req_kal2)} {url} {run_sql(sql_http_req_kal3)} {method}"
                query = "INSERT INTO `packet_sniff`.`tb_det_hasil` (`id_tb_hasil`,`hasil_jadi`, `waktu`) VALUES ('%s', '%s', '%s')" % (id_hasil[0], translate, now)

                id_row = insert_sql(query)
                rows_id.append(id_row)

                # Save ke File TXT
                print(
                    f"[<HTTP>]\t {run_sql(sql_http_req_kal1)} {ip} {run_sql(sql_http_req_kal2)} {url} {run_sql(sql_http_req_kal3)} {method}",
                    file=sniffer_log)
                if packet.haslayer(Raw) and method == "POST":
                    # if show_raw flag is enabled, has raw data, and the requested method is "POST"
                    # then show raw

                    # Save ke Database
                    query_id = "SELECT MAX(id_tb_hasil) FROM tb_hasil"
                    id_hasil = run_sql_int(query_id)
                    translate = f"[<HTTP>]\t {run_sql(sql_http_post)} {packet[Raw].load}"
                    query = "INSERT INTO `packet_sniff`.`tb_det_hasil` (`id_tb_hasil`,`hasil_jadi`, `waktu`) VALUES ('%s', '%s', '%s')" % (id_hasil[0], translate, now)

                    id_row = insert_sql(query)
                    rows_id.append(id_row)

                    # Save ke File TXT
                    print(f"[<HTTP>]\t {run_sql(sql_http_post)} {packet[Raw].load}", file=sniffer_log)
                else:
                    # Save ke Database
                    query_id = "SELECT MAX(id_tb_hasil) FROM tb_hasil"
                    id_hasil = run_sql_int(query_id)
                    translate = f"[HTTP]\t Paket HTTP Lainnya"
                    query = "INSERT INTO `packet_sniff`.`tb_det_hasil` (`id_tb_hasil`,`hasil_jadi`, `waktu`) VALUES ('%s', '%s', '%s')" % (
                        id_hasil[0], translate, now)

                    id_row = insert_sql(query)
                    rows_id.append(id_row)

            elif TCP in packet:
                ip_src = packet[IP].src
                ip_dst = packet[IP].dst
                flag = str(packet.getlayer(TCP).flags)
                syn = packet.getlayer(TCP).seq
                ack = packet.getlayer(TCP).ack
                ket = ""
                # cek http
                if packet.haslayer(HTTPRequest):
                    # if this packet is an HTTP Request
                    # get the requested URL
                    url = packet[HTTPRequest].Host.decode() + packet[HTTPRequest].Path.decode()
                    # get the requester's IP Address
                    ip = packet[IP].src
                    # get the request method
                    method = packet[HTTPRequest].Method.decode()
                    # SQL command
                    sql_http_req_kal1 = "Select kalimat1 from http_packet where flag = 'http_request'"
                    sql_http_req_kal2 = "Select kalimat2 from http_packet where flag = 'http_request'"
                    sql_http_req_kal3 = "Select kalimat3 from http_packet where flag = 'http_request'"
                    sql_http_post = "Select kalimat1 from http_packet where flag = 'method==post'"

                    # Save ke database
                    query_id = "SELECT MAX(id_tb_hasil) FROM tb_hasil"
                    id_hasil = run_sql_int(query_id)
                    translate = f"[<HTTP>]\t {run_sql(sql_http_req_kal1)} {ip} {run_sql(sql_http_req_kal2)} {url} {run_sql(sql_http_req_kal3)} {method}"
                    query = "INSERT INTO `packet_sniff`.`tb_det_hasil` (`id_tb_hasil`,`hasil_jadi`, `waktu`) VALUES ('%s', '%s', '%s')" % (
                    id_hasil[0], translate, now)

                    id_row = insert_sql(query)
                    rows_id.append(id_row)

                    # Save ke File TXT
                    print(
                        f"[<HTTP>]\t {run_sql(sql_http_req_kal1)} {ip} {run_sql(sql_http_req_kal2)} {url} {run_sql(sql_http_req_kal3)} {method}",
                        file=sniffer_log)
                    if packet.haslayer(Raw) and method == "POST":
                        # if show_raw flag is enabled, has raw data, and the requested method is "POST"
                        # then show raw

                        # Save ke Database
                        query_id = "SELECT MAX(id_tb_hasil) FROM tb_hasil"
                        id_hasil = run_sql_int(query_id)
                        translate = f"[<HTTP>]\t {run_sql(sql_http_post)} {packet[Raw].load}"
                        query = "INSERT INTO `packet_sniff`.`tb_det_hasil` (`id_tb_hasil`,`hasil_jadi`, `waktu`) VALUES ('%s', '%s', '%s')" % (
                        id_hasil[0], translate, now)

                        id_row = insert_sql(query)
                        rows_id.append(id_row)

                        # Save ke File TXT
                        print(f"[<HTTP>]\t {run_sql(sql_http_post)} {packet[Raw].load}", file=sniffer_log)
                    else:
                        # Save ke Database
                        query_id = "SELECT MAX(id_tb_hasil) FROM tb_hasil"
                        id_hasil = run_sql_int(query_id)
                        translate = f"[DNS]\t Paket HTTP Lainnya"
                        query = "INSERT INTO `packet_sniff`.`tb_det_hasil` (`id_tb_hasil`,`hasil_jadi`, `waktu`) VALUES ('%s', '%s', '%s')" % (
                            id_hasil[0], translate, now)

                        id_row = insert_sql(query)
                        rows_id.append(id_row)

                # Flag SYN
                elif flag == "S":
                    # Save ke database
                    query_id = "SELECT MAX(id_tb_hasil) FROM tb_hasil"
                    id_hasil = run_sql_int(query_id)
                    translate = "[TCP <SYN>]\t "+run_sql("Select kalimat1 from tcp_packet where flag = 'S'") + str(
                        ip_src) + run_sql("Select kalimat2 from tcp_packet where flag = 'S'")+str(ip_dst) + run_sql("Select kalimat3 from tcp_packet where flag = 'S'") + str(syn) + run_sql("Select kalimat4 from tcp_packet where flag = 'S'") + str(ip_dst)
                    query = "INSERT INTO `packet_sniff`.`tb_det_hasil` (`id_tb_hasil`,`hasil_jadi`, `waktu`) VALUES ('%s', '%s', '%s')" % (id_hasil[0], translate, now)

                    id_row = insert_sql(query)
                    rows_id.append(id_row)
                    print("Jumlah packet skarang "+str(len(packet)))

                    # Save ke File TXT
                    print("[TCP <SYN>]\t "+run_sql("Select kalimat1 from tcp_packet where flag = 'S'") + str(
                        ip_src) + run_sql("Select kalimat2 from tcp_packet where flag = 'S'")
                          + str(ip_dst) + run_sql("Select kalimat3 from tcp_packet where flag = 'S'") + str(syn) + run_sql("Select kalimat4 from tcp_packet where flag = 'S'") + str(ip_dst),
                          file=sniffer_log)
                # Flag SYN + ACK
                elif flag == "SA":

                    # Command SQL
                    SA_kal1 = "Select kalimat1 from tcp_packet where flag = 'SA'"
                    SA_kal2 = "Select kalimat2 from tcp_packet where flag = 'SA'"
                    SA_kal3 = "Select kalimat3 from tcp_packet where flag = 'SA'"
                    SA_kal4 = "Select kalimat4 from tcp_packet where flag = 'SA'"
                    SA_kal5 = "Select kalimat5 from tcp_packet where flag = 'SA'"
                    SA_kal6 = "Select kalimat6 from tcp_packet where flag = 'SA'"
                    SA_kal7 = "Select kalimat7 from tcp_packet where flag = 'SA'"

                    # Save ke Database
                    query_id = "SELECT MAX(id_tb_hasil) FROM tb_hasil"
                    id_hasil = run_sql_int(query_id)
                    translate = "[TCP <SYN+ACK>]\t "+run_sql(SA_kal1) + str(ip_dst) + run_sql(SA_kal2) + str(
                        ip_src) +run_sql(SA_kal3) + str(ack) + run_sql(SA_kal4) + str(ip_src) +run_sql(SA_kal5) + str(ip_src) + run_sql(SA_kal6) + str(ip_dst) +run_sql(SA_kal7)+ str(syn)
                    query = "INSERT INTO `packet_sniff`.`tb_det_hasil` (`id_tb_hasil`,`hasil_jadi`, `waktu`) VALUES ('%s', '%s', '%s')" % (id_hasil[0], translate, now)

                    id_row = insert_sql(query)
                    rows_id.append(id_row)
                    print("Jumlah packet skarang "+str(len(packet)))

                    # Save ke File TXT
                    print("[TCP <SYN+ACK>]\t "+run_sql(SA_kal1) + str(ip_src) + run_sql(SA_kal2) + str(
                        ip_dst) +
                          run_sql(SA_kal3) + str(ack) + run_sql(SA_kal4) + str(ip_src) +
                          run_sql(SA_kal5) + str(ip_src) + run_sql(SA_kal6) + str(ip_dst) +
                           run_sql(SA_kal7)+ str(syn), file=sniffer_log)
                # Flag ACK
                elif flag == "A":

                    # COmmand SQL
                    A_kal1 = "Select kalimat1 from tcp_packet where flag = 'A'"
                    A_kal2 = "Select kalimat2 from tcp_packet where flag = 'A'"
                    A_kal3 = "Select kalimat3 from tcp_packet where flag = 'A'"
                    A_kal4 = "Select kalimat4 from tcp_packet where flag = 'A'"

                    # Save ke Database
                    query_id = "SELECT MAX(id_tb_hasil) FROM tb_hasil"
                    id_hasil = run_sql_int(query_id)
                    translate = "[TCP <ACK>]\t "+run_sql(A_kal1) + str(ip_src) + run_sql(A_kal2) + str(ip_dst) +run_sql(A_kal3) + str(ack) + run_sql(A_kal4) + str(ip_src)
                    query = "INSERT INTO `packet_sniff`.`tb_det_hasil` (`id_tb_hasil`,`hasil_jadi`, `waktu`) VALUES ('%s', '%s', '%s')" % (id_hasil[0], translate, now)

                    id_row = insert_sql(query)
                    rows_id.append(id_row)
                    print("Jumlah packet skarang "+str(len(packet)))

                    # Save ke File TXT
                    print("[TCP <ACK>]\t "+run_sql(A_kal1) + str(ip_src) + run_sql(A_kal2) + str(ip_dst) +
                          run_sql(A_kal3) + str(ack) + run_sql(A_kal4) + str(ip_src),
                          file=sniffer_log)
                # Flag PSH
                elif flag == "P":

                    #Command SQL
                    P_kal1 = "Select kalimat1 from tcp_packet where flag = 'P'"
                    P_kal2 = "Select kalimat2 from tcp_packet where flag = 'P'"

                    # Save ke Database
                    query_id = "SELECT MAX(id_tb_hasil) FROM tb_hasil"
                    id_hasil = run_sql_int(query_id)
                    translate = "[TCP <PSH>]\t "+run_sql(P_kal1) + str(ip_src) + run_sql(P_kal2) + str(
                        ip_dst)
                    query = "INSERT INTO `packet_sniff`.`tb_det_hasil` (`id_tb_hasil`,`hasil_jadi`, `waktu`) VALUES ('%s', '%s', '%s')" % (id_hasil[0], translate, now)

                    id_row = insert_sql(query)
                    rows_id.append(id_row)
                    print("Jumlah packet skarang "+str(len(packet)))
                    # Save ke File TXT
                    print("[TCP <PSH>]\t "+run_sql(P_kal1) + str(ip_src) + run_sql(P_kal2) + str(
                        ip_dst),
                          file=sniffer_log)
                # Flag PSH + ACK
                elif flag == "PA":

                    # Command SQL
                    PA_kal1 = "Select kalimat1 from tcp_packet where flag = 'PA'"
                    PA_kal2 = "Select kalimat2 from tcp_packet where flag = 'PA'"
                    PA_kal3 = "Select kalimat3 from tcp_packet where flag = 'PA'"
                    PA_kal4 = "Select kalimat4 from tcp_packet where flag = 'PA'"
                    PA_kal5 = "Select kalimat5 from tcp_packet where flag = 'PA'"
                    PA_kal6 = "Select kalimat6 from tcp_packet where flag = 'PA'"

                    # Save ke Database
                    query_id = "SELECT MAX(id_tb_hasil) FROM tb_hasil"
                    id_hasil = run_sql_int(query_id)
                    translate = "[TCP <PSH+ACK>]\t "+run_sql(PA_kal1) + str(ip_src) + run_sql(PA_kal2) + str(
                        ip_dst) +run_sql(PA_kal3) + str(ack) + run_sql(PA_kal4) + str(
                        ip_src) +run_sql(PA_kal5) + str(ip_src) + run_sql(PA_kal6) + str(
                        ip_dst)
                    query = "INSERT INTO `packet_sniff`.`tb_det_hasil` (`id_tb_hasil`,`hasil_jadi`, `waktu`) VALUES ('%s', '%s', '%s')" % (id_hasil[0], translate, now)

                    id_row = insert_sql(query)
                    rows_id.append(id_row)
                    print("Jumlah packet skarang "+str(len(packet)))

                    # Save ke file TXT
                    print("[TCP <PSH+ACK>]\t "+run_sql(PA_kal1) + str(ip_src) + run_sql(PA_kal2) + str(
                        ip_dst) +
                          run_sql(PA_kal3) + str(ack) + run_sql(PA_kal4) + str(ip_src) +
                          run_sql(PA_kal5) + str(ip_src) + run_sql(PA_kal6) + str(
                        ip_dst),
                          file=sniffer_log)
                # Flag URG
                elif flag == "U":

                    #  Command SQL
                    U_kal1 = "Select kalimat1 from tcp_packet where flag = 'U'"
                    U_kal2 = "Select kalimat2 from tcp_packet where flag = 'U'"

                    # Save ke Database
                    query_id = "SELECT MAX(id_tb_hasil) FROM tb_hasil"
                    id_hasil = run_sql_int(query_id)
                    translate = "[TCP <URG>]\t "+run_sql(U_kal1) + str(
                        ip_src) + run_sql(U_kal2) + str(
                        ip_dst)
                    query = "INSERT INTO `packet_sniff`.`tb_det_hasil` (`id_tb_hasil`,`hasil_jadi`, `waktu`) VALUES ('%s', '%s', '%s')" % (id_hasil[0], translate, now)

                    id_row = insert_sql(query)
                    rows_id.append(id_row)
                    print("Jumlah packet skarang "+str(len(packet)))

                    # Save ke File TXT
                    print("[TCP <URG>]\t "+run_sql(U_kal1) + str(
                        ip_src) + run_sql(U_kal2) + str(
                        ip_dst),
                          file=sniffer_log)
                # Flag RST
                elif flag == "R":

                    # Command SQL
                    R_kal1 = "Select kalimat1 from tcp_packet where flag = 'R'"
                    R_kal2 = "Select kalimat2 from tcp_packet where flag = 'R'"
                    R_kal3 = "Select kalimat3 from tcp_packet where flag = 'R'"

                    # Save ke database
                    query_id = "SELECT MAX(id_tb_hasil) FROM tb_hasil"
                    id_hasil = run_sql_int(query_id)
                    translate = "[TCP <RST>]\t "+run_sql(R_kal1) + str(
                        ip_dst) + run_sql(R_kal2) + str(
                        ip_src) +run_sql(R_kal3)
                    query = "INSERT INTO `packet_sniff`.`tb_det_hasil` (`id_tb_hasil`,`hasil_jadi`, `waktu`) VALUES ('%s', '%s', '%s')" % (id_hasil[0], translate, now)

                    id_row = insert_sql(query)
                    rows_id.append(id_row)
                    print("Jumlah packet skarang "+str(len(packet)))

                    # Save ke File TXT
                    print("[TCP <RST>]\t "+run_sql(R_kal1) + str(
                        ip_dst) + run_sql(R_kal2) + str(
                        ip_src) +
                          run_sql(R_kal3), file=sniffer_log)

                # Flag RST+ACK
                elif flag == "RA":

                    # Command SQL
                    RA_kal1 = "Select kalimat1 from tcp_packet where flag = 'RA'"
                    RA_kal2 = "Select kalimat2 from tcp_packet where flag = 'RA'"
                    RA_kal3 = "Select kalimat3 from tcp_packet where flag = 'RA'"
                    RA_kal4 = "Select kalimat4 from tcp_packet where flag = 'RA'"
                    RA_kal5 = "Select kalimat5 from tcp_packet where flag = 'RA'"
                    RA_kal6 = "Select kalimat6 from tcp_packet where flag = 'RA'"
                    RA_kal7 = "Select kalimat7 from tcp_packet where flag = 'RA'"

                    # Save ke Database
                    query_id = "SELECT MAX(id_tb_hasil) FROM tb_hasil"
                    id_hasil = run_sql_int(query_id)
                    translate = "[TCP <RST+ACK>]\t "+run_sql(RA_kal1) + str(ip_src) + run_sql(RA_kal2) + str(
                        ip_dst) +run_sql(RA_kal3) + str(ack) + run_sql(RA_kal4) + str(ip_src) +run_sql(RA_kal5) + str(
                        ip_dst) + run_sql(RA_kal6)+ str(ip_src) +run_sql(RA_kal7)
                    query = "INSERT INTO `packet_sniff`.`tb_det_hasil` (`id_tb_hasil`,`hasil_jadi`, `waktu`) VALUES ('%s', '%s', '%s')" % (id_hasil[0], translate, now)

                    id_row = insert_sql(query)
                    rows_id.append(id_row)
                    print("Jumlah packet skarang "+str(len(packet)))

                    # Save ke File TXT
                    print("[TCP <RST+ACK>]\t "+run_sql(RA_kal1) + str(ip_src) + run_sql(RA_kal2) + str(
                        ip_dst) +
                          run_sql(RA_kal3) + str(ack) + run_sql(RA_kal4) + str(ip_src) +
                          run_sql(RA_kal5) + str(
                        ip_dst) + run_sql(RA_kal6)+ str(ip_src) +
                          run_sql(RA_kal7), file=sniffer_log)
                # Flag FIN
                elif flag == "F":

                    # Command SQL
                    F_kal1 = "Select kalimat1 from tcp_packet where flag = 'F'"
                    F_kal2 = "Select kalimat2 from tcp_packet where flag = 'F'"
                    F_kal3 = "Select kalimat3 from tcp_packet where flag = 'F'"

                    # Save ke Database
                    query_id = "SELECT MAX(id_tb_hasil) FROM tb_hasil"
                    id_hasil = run_sql_int(query_id)
                    translate = "[TCP <FIN>]\t "+run_sql(F_kal1) + str(ip_src) + run_sql(F_kal2) + str(
                        ip_dst) + run_sql(F_kal3)
                    query = "INSERT INTO `packet_sniff`.`tb_det_hasil` (`id_tb_hasil`,`hasil_jadi`, `waktu`) VALUES ('%s', '%s', '%s')" % (id_hasil[0], translate, now)

                    id_row = insert_sql(query)
                    rows_id.append(id_row)
                    print("Jumlah packet skarang "+str(len(packet)))

                    # Save ke File TXT
                    print("[TCP <FIN>]\t "+run_sql(F_kal1) + str(ip_src) + run_sql(F_kal2) + str(
                        ip_dst) + run_sql(F_kal3),
                          file=sniffer_log)
                # Flag FIN+ACK
                elif flag == "FA":

                    # Command SQL
                    FA_kal1 = "Select kalimat1 from tcp_packet where flag = 'FA'"
                    FA_kal2 = "Select kalimat2 from tcp_packet where flag = 'FA'"
                    FA_kal3 = "Select kalimat3 from tcp_packet where flag = 'FA'"

                    # Save ke Database
                    query_id = "SELECT MAX(id_tb_hasil) FROM tb_hasil"
                    id_hasil = run_sql_int(query_id)
                    translate = "[TCP <FIN+ACK>]\t "+run_sql(FA_kal1) + str(ip_src) + run_sql(FA_kal2) + str(
                        ip_dst) + run_sql(FA_kal3)+ str(ack)
                    query = "INSERT INTO `packet_sniff`.`tb_det_hasil` (`id_tb_hasil`,`hasil_jadi`, `waktu`) VALUES ('%s', '%s', '%s')" % (id_hasil[0], translate, now)

                    id_row = insert_sql(query)
                    rows_id.append(id_row)
                    print("Jumlah packet skarang "+str(len(packet)))

                    # Save ke File TXT
                    print("[TCP <FIN+ACK>]\t "+run_sql(FA_kal1) + str(ip_src) + run_sql(FA_kal2) + str(
                        ip_dst) + run_sql(FA_kal3)
                          + str(ack), file=sniffer_log)
                else:
                    # Save ke Database
                    query_id = "SELECT MAX(id_tb_hasil) FROM tb_hasil"
                    id_hasil = run_sql_int(query_id)
                    translate = f"[DNS]\t Paket TCP Lainnya"
                    query = "INSERT INTO `packet_sniff`.`tb_det_hasil` (`id_tb_hasil`,`hasil_jadi`, `waktu`) VALUES ('%s', '%s', '%s')" % (
                        id_hasil[0], translate, now)

                    id_row = insert_sql(query)
                    rows_id.append(id_row)


            elif UDP in packet:
                if IP in packet:
                    ip_src = packet[IP].src
                    ip_dst = packet[IP].dst
                    if Raw in packet:
                        s_port = packet.getlayer(UDP).sport
                        d_port = packet.getlayer(UDP).dport
                        data_length = packet.getlayer(UDP).len
                        udp_kal1 = "Select kalimat1 from udp_packet"
                        udp_kal2 = "Select kalimat2 from udp_packet"
                        udp_kal3 = "Select kalimat3 from udp_packet"
                        udp_kal4 = "Select kalimat4 from udp_packet"
                        udp_kal5 = "Select kalimat5 from udp_packet"
                        udp_kal6 = "Select kalimat6 from udp_packet"

                        # Save ke Database
                        query_id = "SELECT MAX(id_tb_hasil) FROM tb_hasil"
                        id_hasil = run_sql_int(query_id)
                        translate = "[UDP]\t "+run_sql(udp_kal1) + str(ip_src) + run_sql(udp_kal2) + str(
                            ip_dst) +run_sql(udp_kal3) + str(s_port) + run_sql(udp_kal4) + str(d_port) +run_sql(udp_kal5) + str(data_length) + run_sql(udp_kal6)
                        query = "INSERT INTO `packet_sniff`.`tb_det_hasil` (`id_tb_hasil`,`hasil_jadi`, `waktu`) VALUES ('%s', '%s', '%s')" % (id_hasil[0], translate, now)

                        id_row = insert_sql(query)
                        rows_id.append(id_row)

                        # Save ke File TXT
                        print("[UDP]\t "+run_sql(udp_kal1) + str(ip_src) + run_sql(udp_kal2) + str(
                            ip_dst) +
                              run_sql(udp_kal3) + str(s_port) + run_sql(udp_kal4) + str(d_port) +
                              run_sql(udp_kal5) + str(data_length) + run_sql(udp_kal6) , file=sniffer_log)
                    # elif packet.haslayer(DNS) and packet.getlayer(DNS).qr == 0:
                    #     if IP in packet:
                    #         ip_src = packet[IP].src
                    #         ip_dst = packet[IP].dst
                    #         if packet.haslayer(DNS) and packet.getlayer(DNS).qr == 0:
                    #             url = str(packet.getlayer(DNS).qd.qname.decode())
                    #             url_trans = url.replace("'", "")
                    #             print(url)
                    #             print(url_trans)
                    #
                    #             dns_kal1 = "Select kalimat1 from dns_packet"
                    #             dns_kal2 = "Select kalimat2 from dns_packet"
                    #             dns_kal3 = "Select kalimat3 from dns_packet"
                    #
                    #             # Save ke Database
                    #             query_id = "select id_tb_hasil from tb_hasil where nama_hasil = '%s'" % (file_name)
                    #             id_hasil = run_sql_int(query_id)
                    #             translate = f"[DNS]\t {run_sql(dns_kal1)} {str(ip_src)} {run_sql(dns_kal2)} " \
                    #                         f"{url_trans} {run_sql(dns_kal3)}" \
                    #                         f" {str(ip_dst)} "
                    #             query = "INSERT INTO `packet_sniff`.`tb_det_hasil` (`id_tb_hasil`,`hasil_jadi`) VALUES ('%s', '%s')" % (
                    #             id_hasil[0],
                    #             translate)
                    #
                    #             id_row = insert_sql(query)
                    #             rows_id.append(id_row)
                    #
                    #             # Save ke File TXT
                    #             print("[DNS]\t " + run_sql("Select kalimat1 from dns_packet") + str(ip_src) + run_sql(
                    #                 "Select kalimat2 from dns_packet") + str(
                    #                 packet.getlayer(DNS).qd.qname) + run_sql("Select kalimat3 from dns_packet") + str(
                    #                 ip_dst),
                    #                   file=sniffer_log)
                    elif DHCP in packet:
                    # Match DHCP discover
                        if DHCP in packet and packet[DHCP].options[0][1] == 1:
                            print('---')
                            print('New DHCP Discover')
                            # print(packet.summary())
                            # print(ls(packet))
                            hostname = get_option(packet[DHCP].options, 'hostname')

                            Discover_kal1 = "Select kalimat1 from dhcp_packet where flag = 'message-type=discover'"
                            Discover_kal2 = "Select kalimat2 from dhcp_packet where flag = 'message-type=discover'"
                            Discover_kal3 = "Select kalimat3 from dhcp_packet where flag = 'message-type=discover'"

                            # Save ke Database
                            query_id = "SELECT MAX(id_tb_hasil) FROM tb_hasil"
                            id_hasil = run_sql_int(query_id)
                            translate = f"{run_sql(Discover_kal1)} {hostname} {run_sql(Discover_kal2)} {packet.src} {run_sql(Discover_kal3)}"
                            query = "INSERT INTO `packet_sniff`.`tb_det_hasil` (`id_tb_hasil`,`hasil_jadi`, `waktu`) VALUES ('%s', '%s', '%s')" % (id_hasil[0], translate, now)

                            id_row = insert_sql(query)
                            rows_id.append(id_row)

                            # Save ke File TXT
                            print(f"[DHCP Discover]\t {run_sql(Discover_kal1)} {hostname} {run_sql(Discover_kal2)} ({packet.src})", file=sniffer_log)
                            print(f"Host {hostname} ({packet.src}) meminta IP")


                        # Match DHCP offer
                        elif DHCP in packet and packet[DHCP].options[0][1] == 2:
                            print('---')
                            print('New DHCP Offer')
                            # print(packet.summary())
                            # print(ls(packet))

                            subnet_mask = get_option(packet[DHCP].options, 'subnet_mask')
                            lease_time = get_option(packet[DHCP].options, 'lease_time')
                            router = get_option(packet[DHCP].options, 'router')
                            name_server = get_option(packet[DHCP].options, 'name_server')
                            domain = get_option(packet[DHCP].options, 'domain')

                            Offer_kal1 = "Select kalimat1 from dhcp_packet where flag = 'message-type=offer'"
                            Offer_kal2 = "Select kalimat2 from dhcp_packet where flag = 'message-type=offer'"
                            Offer_kal3 = "Select kalimat3 from dhcp_packet where flag = 'message-type=offer'"

                            # Save ke Database
                            query_id = "SELECT MAX(id_tb_hasil) FROM tb_hasil"
                            id_hasil = run_sql_int(query_id)
                            translate = f"{run_sql(Offer_kal1)} {packet[IP].src} {run_sql(Offer_kal2)} {packet[BOOTP].yiaddr} {run_sql(Offer_kal3)} ({packet.dst}) "
                            query = "INSERT INTO `packet_sniff`.`tb_det_hasil` (`id_tb_hasil`,`hasil_jadi`, `waktu`) VALUES ('%s', '%s', '%s')" % (id_hasil[0], translate, now)

                            id_row = insert_sql(query)
                            rows_id.append(id_row)


                            # Save ke file TXT
                            print(f"[DHCP Offer]\t {run_sql(Offer_kal1)} {packet[IP].src} {run_sql(Offer_kal2)} ({packet.src}) {run_sql(Offer_kal3)} {packet[BOOTP].yiaddr}", file=sniffer_log)
                            print(f"DHCP Server {packet[IP].src} ({packet.src}) "
                                  f"menawarkan {packet[BOOTP].yiaddr}")

                            print(f"DHCP Options: subnet_mask: {subnet_mask}, lease_time: "
                                  f"{lease_time}, router: {router}, name_server: {name_server}, "
                                  f"domain: {domain}")


                        # Match DHCP request
                        elif DHCP in packet and packet[DHCP].options[0][1] == 3:
                            print('---')
                            print('New DHCP Request')
                            # print(packet.summary())
                            # print(ls(packet))

                            requested_addr = get_option(packet[DHCP].options, 'requested_addr')
                            hostname = get_option(packet[DHCP].options, 'hostname')

                            Request_kal1 = "Select kalimat1 from dhcp_packet where flag = 'message-type=request'"
                            Request_kal2 = "Select kalimat2 from dhcp_packet where flag = 'message-type=request'"
                            Request_kal3 = "Select kalimat3 from dhcp_packet where flag = 'message-type=request'"

                            # Save ke Database
                            query_id = "SELECT MAX(id_tb_hasil) FROM tb_hasil"
                            id_hasil = run_sql_int(query_id)
                            translate = f"{run_sql(Request_kal1)} {hostname} {run_sql(Request_kal2)} {requested_addr} {run_sql(Request_kal3)} "
                            query = "INSERT INTO `packet_sniff`.`tb_det_hasil` (`id_tb_hasil`,`hasil_jadi`, `waktu`) VALUES ('%s', '%s', '%s')" % (id_hasil[0], translate, now)

                            id_row = insert_sql(query)
                            rows_id.append(id_row)

                            # Save ke File TXT
                            print(f"[DHCP Request]\t {run_sql(Request_kal1)} {hostname} {run_sql(Request_kal2)} ({packet.src}) {run_sql(Request_kal3)} {requested_addr}", file=sniffer_log)
                            print(f"Host {hostname} ({packet.src}) requested {requested_addr}")


                        # Match DHCP ack
                        elif DHCP in packet and packet[DHCP].options[0][1] == 5:
                            print('---')
                            print('New DHCP Ack')
                            # print(packet.summary())
                            # print(ls(packet))

                            subnet_mask = get_option(packet[DHCP].options, 'subnet_mask')
                            lease_time = get_option(packet[DHCP].options, 'lease_time')
                            router = get_option(packet[DHCP].options, 'router')
                            name_server = get_option(packet[DHCP].options, 'name_server')

                            Ack_kal1 = "Select kalimat1 from dhcp_packet where flag = 'messgae-type=ack'"
                            Ack_kal2 = "Select kalimat2 from dhcp_packet where flag = 'messgae-type=ack'"
                            Ack_kal3 = "Select kalimat3 from dhcp_packet where flag = 'messgae-type=ack'"

                            # Save ke Database
                            query_id = "SELECT MAX(id_tb_hasil) FROM tb_hasil"
                            id_hasil = run_sql_int(query_id)
                            translate = f"{run_sql(Ack_kal1)} {packet[IP].src} {run_sql(Ack_kal2)} ({packet.dst}) {run_sql(Ack_kal3)} {packet[BOOTP].yiaddr}"
                            query = "INSERT INTO `packet_sniff`.`tb_det_hasil` (`id_tb_hasil`,`hasil_jadi`, `waktu`) VALUES ('%s', '%s', '%s')" % (id_hasil[0], translate, now)

                            id_row = insert_sql(query)
                            rows_id.append(id_row)

                            # Save ke File TXT
                            print(f"[DHCP ACK]\t {run_sql(Ack_kal1)} {packet[IP].src} {run_sql(Ack_kal2)} ({packet.src}) {run_sql(Ack_kal3)} {packet[BOOTP].yiaddr}", file=sniffer_log)
                            print(f"DHCP Server {packet[IP].src} ({packet.src}) "
                                  f"acked {packet[BOOTP].yiaddr}")

                            print(f"DHCP Options: subnet_mask: {subnet_mask}, lease_time: "
                                  f"{lease_time}, router: {router}, name_server: {name_server}")

                        # Match DHCP inform
                        elif DHCP in packet and packet[DHCP].options[0][1] == 8:
                            print('---')
                            print('New DHCP Inform')
                            # print(packet.summary())
                            # print(ls(packet))

                            hostname = get_option(packet[DHCP].options, 'hostname')
                            vendor_class_id = get_option(packet[DHCP].options, 'vendor_class_id')

                            Inform_kal1 = "Select kalimat1 from dhcp_packet where flag = 'inform'"
                            Inform_kal2 = "Select kalimat2 from dhcp_packet where flag = 'inform'"
                            Inform_kal3 = "Select kalimat3 from dhcp_packet where flag = 'inform'"

                            # Save ke Database
                            query_id = "SELECT MAX(id_tb_hasil) FROM tb_hasil"
                            id_hasil = run_sql_int(query_id)
                            translate = f"[DHCP Inform]\t {run_sql(Inform_kal1)} {packet[IP].src} ({packet.src}) {run_sql(Inform_kal2)} {hostname} {run_sql(Inform_kal3)} {vendor_class_id}"
                            query = "INSERT INTO `packet_sniff`.`tb_det_hasil` (`id_tb_hasil`,`hasil_jadi`, `waktu`) VALUES ('%s', '%s', '%s')" % (id_hasil[0], translate, now)

                            id_row = insert_sql(query)
                            rows_id.append(id_row)

                            # Save ke File TXT
                            print(f"[DHCP Inform]\t {run_sql(Inform_kal1)} {packet[IP].src} ({packet.src}) {run_sql(Inform_kal2)} {hostname} {run_sql(Inform_kal3)} {vendor_class_id}", file=sniffer_log)
                            print(f"DHCP Inform from {packet[IP].src} ({packet.src}) "
                                  f"hostname: {hostname}, vendor_class_id: {vendor_class_id}")

                        else:
                            # Save ke Database
                            query_id = "SELECT MAX(id_tb_hasil) FROM tb_hasil"
                            id_hasil = run_sql_int(query_id)
                            translate = f"[DNS]\t Paket DHCP Lainnya"
                            query = "INSERT INTO `packet_sniff`.`tb_det_hasil` (`id_tb_hasil`,`hasil_jadi`, `waktu`) VALUES ('%s', '%s', '%s')" % (
                                id_hasil[0], translate, now)

                            id_row = insert_sql(query)
                            rows_id.append(id_row)
                    else:
                        # Save ke Database
                        query_id = "SELECT MAX(id_tb_hasil) FROM tb_hasil"
                        id_hasil = run_sql_int(query_id)
                        translate = f"[DNS]\t Paket UDP Lainnya"
                        query = "INSERT INTO `packet_sniff`.`tb_det_hasil` (`id_tb_hasil`,`hasil_jadi`, `waktu`) VALUES ('%s', '%s', '%s')" % (
                            id_hasil[0], translate, now)

                        id_row = insert_sql(query)
                        rows_id.append(id_row)
            elif len(packet) == 0:
                time.sleep(2)
                self.stop_sniffing = True

            else:
                #Kalo protokol yg didapetin selain ARP, ICMP, DNS, TCP, UDP, DHCP, HTTP
                # Save ke Database
                query_id = "SELECT MAX(id_tb_hasil) FROM tb_hasil"
                id_hasil = run_sql_int(query_id)
                translate = "Translasi protokol ini tidak didukung oleh aplikasi "
                query = "INSERT INTO `packet_sniff`.`tb_det_hasil` (`id_tb_hasil`,`hasil_jadi`, `waktu`) VALUES ('%s', '%s', '%s')" % (id_hasil[0], translate, now)

                id_row = insert_sql(query)
                rows_id.append(id_row)
            # pcapkit.extract(fin=file_name + '.cap', fout='out.json', format='json', extension=False)
            #
            # import json
            #
            # with open('out.json') as f:
            #     d = json.load(f)
            #
            #     for attribute, value in d.items():
            #         if attribute != 'Global Header':
            #             print(attribute, value)
            #             query = 'update tb_det_hasil set hasil_awal="%s" where id_tb_hasil = 1 AND hasil_awal is null' % (
            #                 value)
            #             update_sql(query)
            ################################################################################################




        # def should_stop_sniff(packet):
        #     time.sleep(2)
        #     if len(packet) == 0:
        #         return True
        #     else :
        #         return False

        # Printing an informational message to the screen
        print("\n* Starting the capture...")
        # timeout = int(time_to_sniff),
        pkt = sniff(iface=net_iface, filter=proto_sniff, count=int(pkt_to_sniff),
                    prn=packet_log, stop_filter=self.stop_sniffing)

        print(rows_id)
        # print(len(rows_id))
        name_no_space = file_name.replace(" ","")
        wrpcap("hasil/"+name_no_space + ".cap", pkt)
        # waktu_jeda = int(time_to_sniff)
        # time.sleep(waktu_jeda)
        if path.exists("hasil/"+name_no_space + ".cap"):

            print("Sudah ada pcapnya")

            # pcapkit.extract(fin=file_name+'.cap', fout='out', format='json', extension=False)
            # subprocess.call('dir', shell=True)

            subprocess.call(f'tshark -r hasil/{name_no_space}.cap -T json >outkul.json', shell=True)

            # try:
            #     subprocess.call(f'tshark -r {file_name}.cap -T json >out.json', shell=False)
            #
            # except:
            #     print("\nGagal Mengkonversi \n")
            #
            # else:
            #     # Executed if the try clause does not raise an exception
            #     print("\nInterface %s was set to PROMISC mode.\n" % net_iface)

            with open('outkul.json', 'rb') as f:
                d = json.load(f)


            i=0

            for value in d:
                # for i in range(len(rows_id)):
                # if i < len(rows_id)-1:
                #     break


                # print(value)
                # query_id = "select id_tb_hasil from tb_hasil where nama_hasil = '%s'" % (file_name)


                str32 = json.dumps(value, indent=2)
                value2 = str(value)
                print("ini adalaah value 2 "+value2)
                value3 = value2.replace("'",'"')
                print("Ini adalah value 3 "+value3)

                # query = "update tb_det_hasil set hasil_awal='%s' where id_tb_det_hasil = '%s'" % (value3, rows_id[i])
                query = 'update tb_det_hasil set hasil_awal=%s where id_tb_det_hasil = %s'
                # print(rows_id[i])
                # print(value)
                # id_row = rows_id[i]

                param = (str32, rows_id[i])
                print(value)

                # query2 = query.replace("''",'""')
                # query3 = query2.replace("'",'"')
                #
                # query4 = query3.replace("wasn't", "was not")
                # eval(query)
                i+=1
                print(query)

                update_sql(query, param)

            # for i in len(rows_id):
        rows_id.clear()
        # Printing the closing message
        print("\n* Please check the %s file to see the captured packets.\n" % file_name)

        # Closing the log file
        sniffer_log.close()
        query_id = "SELECT MAX(id_tb_hasil) FROM tb_hasil"
        id_hasil = run_sql_int(query_id)
        return id_hasil

    def testPrint(self):
        print("Yeh Bro Dika")


