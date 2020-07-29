try:
    from scapy.all import *

except ImportError:
    print("Scapy package for Python is not installed on your system.")
    sys.exit()


# Printing a message to the user; always use "sudo scapy" in Linux!
print("\n! Pastikan Menjalankan Program Dengan Hak Akses Root !\n")

# Asking the user for some parameters: interface on which to sniff, the number of packets to sniff, the time interval to sniff, the protocol
# list_iface = get_windows_if_list()
# print(list_iface)
# Asking the user for input - the interface on which to run the sniffer
net_iface = input("* Enter the interface on which to run the sniffer (e.g. 'enp0s8'): ")

try:
    subprocess.call(["ifconfig", net_iface, "promisc"], stdout=None, stderr=None, shell=False)

except:
    print("\nFailed to configure interface as promiscuous.\n")

else:
    # Executed if the try clause does not raise an exception
    print("\nInterface %s was set to PROMISC mode.\n" % net_iface)