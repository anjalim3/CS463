from scapy.all import *

while 1:
    dst_ip = "192.168.200.62"
    dst_port = 31337
    my_packet = IP(dst=dst_ip)/TCP(dport=dst_port)/"anjalim3"
    send(my_packet)
