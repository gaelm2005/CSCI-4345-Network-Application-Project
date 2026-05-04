from scapy.all import sniff, Dot11, Dot11Beacon, Dot11Elt
from threading import Thread
import pandas
import time
import os

#networks will inlcude all access points(AP) nearby -> AP being wifi networks i assume
networks = pandas.DataFrame(columns=["BSSID","SSID","dBm_Signal","Channel","Crypto"])

#set the BSSID index
networks.set_index("BSSID",inplace=True)

def callback(packet):
    if packet.haslayer(Dot11Beacon):
        # extract the MAC address of the network
        bssid = packet[Dot11].addr2
        # get the name of it
        ssid = packet[Dot11Elt].info.decode()
        try:
            dbm_signal = packet.dBm_AntSignal
        except:
            dbm_signal = "N/A"
        # extract network stats
        stats = packet[Dot11Beacon].network_stats()
        # get the channel of the AP
        channel = stats.get("channel")
        # get the crypto
        crypto = stats.get("crypto")
        networks.loc[bssid] = (ssid, dbm_signal, channel, crypto)

def print_all():
    while True:
        os.system("clear")
        print(networks)     
        time.sleep(0.5)

def change_channel():
    ch = 1
    while True:
        os.system(f"ifconfig {interface} channel {ch}")

        #switch channel from 1 to 14 each .5s
        ch = ch% 14+1
        time.sleep(0.5)


if __name__ == "__main__":
    # interface name, check using ifconfig
    interface = "wlp0s20f3mon"
    # start the thread that prints all the networks
    printer = Thread(target=print_all)
    printer.daemon = True
    printer.start()
    # start sniffing
    sniff(prn=callback, iface=interface)
    # start the channel changer
    channel_changer = Thread(target=change_channel)
    channel_changer.daemon = True
    channel_changer.start()