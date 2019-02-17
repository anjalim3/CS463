from scapy.all import *

src_port = 1024
while 1:
    dst_ip = "192.168.200.62"
    dst_port = 31337
    my_packet = IP(dst=dst_ip)/TCP(dport=dst_port, sport = seq_no)/"anjalim3"
    send(my_packet)
    seq_no = seq_no + 1
    if seq_no > 49151:
        seq_no = 1024
