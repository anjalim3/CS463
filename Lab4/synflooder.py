from scapy.all import *
import os

src_port = 1024
os.system("sudo iptables -A OUTPUT -p tcp --tcp-flags RST RST -s $(hostname -I) -j DROP")
while 1:
    dst_ip = "192.168.200.62"
    dst_port = 31337
    my_packet = IP(dst=dst_ip)/TCP(dport=dst_port, sport = src_port)/"anjalim3"
    send(my_packet)
    src_port = src_port + 1
    if src_port > 49151:
        src_port = 1024
