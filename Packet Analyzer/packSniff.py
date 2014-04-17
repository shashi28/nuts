'''
Packet sniffer in python using the pcapy python library

Project website

http://oss.coresecurity.com/projects/pcapy.html

'''

import socket
from struct import *
import pcapy
from PyQt4.QtCore import *

class Sniffer(QThread):
    def main(self,dev):
        #list all devices
        qDebug('inside main')
        qDebug("Sniffing device " + dev)

        '''
        open device
        # Arguments here are:
        #   device
        #   snaplen (maximum number of bytes to capture _per_packet_)
        #   promiscious mode (1 for true)
        #   timeout (in milliseconds)
        '''
        cap = pcapy.open_live(dev , 65536 , 1 , 0)

        #start sniffing packets
        while(True):
            qDebug('inside while(1)')

            (header, packet) = cap.next()
            #print ('%s: captured %d bytes, truncated to %d bytes' %(datetime.datetime.now(), header.getlen(), header.getcaplen()))
            self.parse_packet(packet)

    #Convert a string of 6 characters of ethernet address into a dash separated hex string
    def eth_addr (self,a) :
        b = "%.2x:%.2x:%.2x:%.2x:%.2x:%.2x" % (ord(a[0]) , ord(a[1]) , ord(a[2]), ord(a[3]), ord(a[4]) , ord(a[5]))
        return b

    #function to parse a packet
    def parse_packet(self,packet) :

        qDebug('inside parse_packet')

        #parse ethernet header
        eth_length = 14

        eth_header = packet[:eth_length]
        eth = unpack('!6s6sH' , eth_header)
        eth_protocol = socket.ntohs(eth[2])

        print 'Destination MAC : ' + self.eth_addr(packet[0:6]) + ' Source MAC : ' + self.eth_addr(packet[6:12]) + ' Protocol : ' + str(eth_protocol)

        D_MAC = self.eth_addr(packet[0:6])
        S_MAC = self.eth_addr(packet[6:12])
        Pro = str(eth_protocol)

        self.emit(SIGNAL('MAC(QString,QString,QString)'),D_MAC,S_MAC,Pro)
        #Parse IP packets, IP Protocol number = 8
        if eth_protocol == 8 :
            #Parse IP header
            #take first 20 characters for the ip header
            ip_header = packet[eth_length:20+eth_length]

            #now unpack them :)
            iph = unpack('!BBHHHBBH4s4s' , ip_header)

            version_ihl = iph[0]
            version = version_ihl >> 4
            ihl = version_ihl & 0xF

            iph_length = ihl * 4

            ttl = iph[5]
            protocol = iph[6]
            s_addr = socket.inet_ntoa(iph[8]);
            d_addr = socket.inet_ntoa(iph[9]);

            print 'Version : ' + str(version) + ' IP Header Length : ' + str(ihl) + ' TTL : ' + str(ttl) + ' Protocol : ' + str(protocol) + ' Source Address : ' + str(s_addr) + ' Destination Address : ' + str(d_addr)

            Version = str(version)
            IP_Header_Length = str(ihl)
            TTL =  str(ttl)
            Protocol = str(protocol)
            Source_Address = str(s_addr)
            Destination_Address =  str(d_addr)

            self.emit(SIGNAL('IP(QString,QString,QString,QString,QString,QString)'),Version,IP_Header_Length,TTL,Protocol,Source_Address,Destination_Address)

            #TCP protocol
            if protocol == 6 :
                t = iph_length + eth_length
                tcp_header = packet[t:t+20]

                #now unpack them :)
                tcph = unpack('!HHLLBBHHH' , tcp_header)

                source_port = tcph[0]
                dest_port = tcph[1]
                sequence = tcph[2]
                acknowledgement = tcph[3]
                doff_reserved = tcph[4]
                tcph_length = doff_reserved >> 4

                print 'Source Port : ' + str(source_port) + ' Dest Port : ' + str(dest_port) + ' Sequence Number : ' + str(sequence) + ' Acknowledgement : ' + str(acknowledgement) + ' TCP header length : ' + str(tcph_length)

                Source_Port = str(source_port)
                Dest_Port = str(dest_port)
                Sequence_Number = str(sequence)
                Acknowledgement = str(acknowledgement)
                TCP_header_length = str(tcph_length)

                self.emit(SIGNAL('TCP(QString,QString,QString,QString,QString)'),Source_Port,Dest_Port,Sequence_Number,Acknowledgement,TCP_header_length)

                h_size = eth_length + iph_length + tcph_length * 4
                data_size = len(packet) - h_size

                #get data from the packet
                data = packet[h_size:]

                print 'Data : ' + data

                self.emit(SIGNAL('Data(QString)'),data)
            #ICMP Packets
            elif protocol == 1 :
                u = iph_length + eth_length
                icmph_length = 4
                icmp_header = packet[u:u+4]

                #now unpack them :)
                icmph = unpack('!BBH' , icmp_header)

                icmp_type = icmph[0]
                code = icmph[1]
                checksum = icmph[2]

                print 'Type : ' + str(icmp_type) + ' Code : ' + str(code) + ' Checksum : ' + str(checksum)

                Type = str(icmp_type)
                Code = str(code)
                Checksum = str(checksum)
                self.emit(SIGNAL('ICMP(QString,QString,QString)'),Type,Code,Checksum)

                h_size = eth_length + iph_length + icmph_length
                data_size = len(packet) - h_size

                #get data from the packet
                data = packet[h_size:]

                print 'Data : ' + data
                self.emit(SIGNAL('Data(QString)'),data)
            #UDP packets
            elif protocol == 17 :
                u = iph_length + eth_length
                udph_length = 8
                udp_header = packet[u:u+8]

                #now unpack them :)
                udph = unpack('!HHHH' , udp_header)

                source_port = udph[0]
                dest_port = udph[1]
                length = udph[2]
                checksum = udph[3]

                print 'Source Port : ' + str(source_port) + ' Dest Port : ' + str(dest_port) + ' Length : ' + str(length) + ' Checksum : ' + str(checksum)

                Source_Port = str(source_port)
                Dest_Port = str(dest_port)
                Length = str(length)
                Checksum = str(checksum)

                self.emit(SIGNAL('ICMP(QString,QString,QString,QString)'),Source_Port,Dest_Port,Length,Checksum)

                h_size = eth_length + iph_length + udph_length
                data_size = len(packet) - h_size

                #get data from the packet
                data = packet[h_size:]

                print 'Data : ' + data

            #some other IP packet like IGMP
            else :
                print 'Protocol other than TCP/UDP/ICMP'


    def run(self):
        qDebug('inside run')
        self.main(self.dev)
        self.exec_()

    def BtnClicked_Slot(self,device):
        self.dev = str(device)
        qDebug('inside slot BtnClicked device = '+device)