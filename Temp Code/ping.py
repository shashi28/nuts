#!/usr/bin/env python
# -*- coding: utf-8 -*-

#=============================================================================#
import os, sys, socket, struct, select, time, signal
from PySide.QtCore import *

if sys.platform == "win32":
    # On Windows, the best timer is time.clock()
    default_timer = time.clock
else:
    # On most other platforms the best timer is time.time()
    default_timer = time.time

#=============================================================================#
# ICMP parameters

ICMP_ECHOREPLY  =    0 # Echo reply (per RFC792)
ICMP_ECHO       =    8 # Echo request (per RFC792)
ICMP_MAX_RECV   = 2048 # Max size of incoming buffer

MAX_SLEEP = 1000

class MyStats:
    thisIP   = "0.0.0.0"
    pktsSent = 0
    pktsRcvd = 0
    minTime  = 999999999
    maxTime  = 0
    totTime  = 0
    avrgTime = 0
    fracLoss = 1.0

myStats = MyStats # NOT Used globally anymore.

class Ping(QThread):
    def __init__(self, parent = None):
        super(Ping,self).__init__(parent)
        #self.moveToThread(self)
    thisIP   = "0.0.0.0"
    pktsSent = 0
    pktsRcvd = 0
    minTime  = 999999999
    maxTime  = 0
    totTime  = 0
    avrgTime = 0
    fracLoss = 1.0
#=============================================================================#
    def checksum(self, source_string):
        """
        A port of the functionality of in_cksum() from ping.c
        Ideally this would act on the string as a series of 16-bit ints (host
        packed), but this works.
        Network data is big-endian, hosts are typically little-endian
        """
        countTo = (int(len(source_string)/2))*2
        sum = 0
        count = 0
    
        # Handle bytes in pairs (decoding as short ints)
        loByte = 0
        hiByte = 0
        while count < countTo:
            if (sys.byteorder == "little"):
                loByte = source_string[count]
                hiByte = source_string[count + 1]
            else:
                loByte = source_string[count + 1]
                hiByte = source_string[count]
            try:     # For Python3
                sum = sum + (hiByte * 256 + loByte)
            except:  # For Python2
                sum = sum + (ord(hiByte) * 256 + ord(loByte))
            count += 2
    
        # Handle last byte if applicable (odd-number of bytes)
        # Endianness should be irrelevant in this case
        if countTo < len(source_string): # Check for odd length
            loByte = source_string[len(source_string)-1]
            try:      # For Python3
                sum += loByte
            except:   # For Python2
                sum += ord(loByte)
    
        sum &= 0xffffffff # Truncate sum to 32 bits (a variance from ping.c, which
                          # uses signed ints, but overflow is unlikely in ping)
    
        sum = (sum >> 16) + (sum & 0xffff)    # Add high 16 bits to low 16 bits
        sum += (sum >> 16)                    # Add carry from above (if any)
        answer = ~sum & 0xffff                # Invert and truncate to 16 bits
        answer = socket.htons(answer)
    
        return answer
    
    #=============================================================================#
    def do_one(self, destIP, hostname, timeout, mySeqNumber, numDataBytes, quiet = False):
        """
        Returns either the delay (in ms) or None on timeout.
        """
        delay = None
    
        try: # One could use UDP here, but it's obscure
            mySocket = socket.socket(socket.AF_INET, socket.SOCK_RAW, socket.getprotobyname("icmp"))
        except socket.error as e:
            print("failed. (socket error: '%s')" % e.args[1])
            raise # raise the original error
    
        my_ID = os.getpid() & 0xFFFF
    
        sentTime = self.send_one_ping(mySocket, destIP, my_ID, mySeqNumber, numDataBytes)
        if sentTime == None:
            mySocket.close()
            return delay
    
        self.pktsSent += 1
    
        recvTime, dataSize, iphSrcIP, icmpSeqNumber, iphTTL = self.receive_one_ping(mySocket, my_ID, timeout)
    
        mySocket.close()
    
        if recvTime:
            delay = (recvTime-sentTime)*1000
            if not quiet:
                print("%d bytes from %s: icmp_seq=%d ttl=%d time=%d ms" % (dataSize, socket.inet_ntoa(struct.pack("!I", iphSrcIP)), icmpSeqNumber, iphTTL, delay))
                #print('dataSize',type(dataSize))
                #print('socket.inet_ntoa(struct.pack("!I", iphSrcIP))',type(socket.inet_ntoa(struct.pack("!I", iphSrcIP))))
                #print('icmpSeqNumber',type(icmpSeqNumber))
                #print('iphTTL',type(iphTTL))
                #print('delay',type(delay))
                #self.emit(SIGNAL(''),)
            self.pktsRcvd += 1
            self.totTime += delay
            if self.minTime > delay:
                self.minTime = delay
            if self.maxTime < delay:
                self.maxTime = delay
        else:
            delay = None
            self.emit(SIGNAL('pingErr(QString)'),'Request timed out')
            #print("Request timed out.")
    
        return delay
    
    #=============================================================================#
    def send_one_ping(self, mySocket, destIP, myID, mySeqNumber, numDataBytes):
        """
        Send one ping to the given >destIP<.
        """
        #destIP  =  socket.gethostbyname(destIP)
    
        # Header is type (8), code (8), checksum (16), id (16), sequence (16)
        # (numDataBytes - 8) - Remove header size from packet size
        myChecksum = 0
    
        # Make a dummy heder with a 0 checksum.
        header = struct.pack(
            "!BBHHH", ICMP_ECHO, 0, myChecksum, myID, mySeqNumber
        )
    
        padBytes = []
        startVal = 0x42
        # 'cose of the string/byte changes in python 2/3 we have
        # to build the data differnely for different version
        # or it will make packets with unexpected size.
        if sys.version[:1] == '2':
            bytes = struct.calcsize("d")
            data = ((numDataBytes - 8) - bytes) * "Q"
            data = struct.pack("d", default_timer()) + data
        else:
            for i in range(startVal, startVal + (numDataBytes-8)):
                padBytes += [(i & 0xff)]  # Keep chars in the 0-255 range
            #data = bytes(padBytes)
            data = bytearray(padBytes)
    
    
        # Calculate the checksum on the data and the dummy header.
        myChecksum = self.checksum(header + data) # Checksum is in network order
    
        # Now that we have the right checksum, we put that in. It's just easier
        # to make up a new header than to stuff it into the dummy.
        header = struct.pack(
            "!BBHHH", ICMP_ECHO, 0, myChecksum, myID, mySeqNumber
        )
    
        packet = header + data
    
        sendTime = default_timer()
    
        try:
            mySocket.sendto(packet, (destIP, 1)) # Port number is irrelevant for ICMP
        except socket.error as e:
            self.emit(SIGNAL('pingErr(QString)','General Failure'))
            #print("General failure (%s)" % (e.args[1]))
            return
    
        return sendTime
    
    #=============================================================================#
    def receive_one_ping(self,mySocket, myID, timeout):
        """
        Receive the ping from the socket. Timeout = in ms
        """
        timeLeft = timeout/1000
    
        while True: # Loop while waiting for packet or timeout
            startedSelect = default_timer()
            whatReady = select.select([mySocket], [], [], timeLeft)
            howLongInSelect = (default_timer() - startedSelect)
            if whatReady[0] == []: # Timeout
                return None, 0, 0, 0, 0
    
            timeReceived = default_timer()
    
            recPacket, addr = mySocket.recvfrom(ICMP_MAX_RECV)
    
            ipHeader = recPacket[:20]
            iphVersion, iphTypeOfSvc, iphLength, \
            iphID, iphFlags, iphTTL, iphProtocol, \
            iphChecksum, iphSrcIP, iphDestIP = struct.unpack(
                "!BBHHHBBHII", ipHeader
            )
    
            icmpHeader = recPacket[20:28]
            icmpType, icmpCode, icmpChecksum, \
            icmpPacketID, icmpSeqNumber = struct.unpack(
                "!BBHHH", icmpHeader
            )
    
            if icmpPacketID == myID: # Our packet
                dataSize = len(recPacket) - 28
                #print (len(recPacket.encode()))
                return timeReceived, (dataSize+8), iphSrcIP, icmpSeqNumber, iphTTL
    
            timeLeft = timeLeft - howLongInSelect
            if timeLeft <= 0:
                return None, 0, 0, 0, 0
    
    #=============================================================================#
    def dump_stats(self):
        """
        Show stats when pings are done
        """
        print("\n----%s PYTHON PING Statistics----" % (self.thisIP))
    
        if self.pktsSent > 0:
            self.fracLoss = (self.pktsSent - self.pktsRcvd)/self.pktsSent
    
        print("%d packets transmitted, %d packets received, %0.1f%% packet loss" % (self.pktsSent, self.pktsRcvd, 100.0 * self.fracLoss ))
        ##print('self.pktsSent',type(self.pktsSent))
        #print('self.pktsRcvd',type(self.pktsRcvd))
        #print('100.0 * self.fracLoss',type(100.0 * self.fracLoss))

        if self.pktsRcvd > 0:
            print("round-trip (ms)  min/avg/max = %d/%0.1f/%d" % (self.minTime, self.totTime/self.pktsRcvd, self.maxTime))
           # print('self.minTime', type(self.minTime))
            #print('self.totTime/self.pktsRcvd', type(self.totTime/self.pktsRcvd))
            #print('self.maxTime', type(self.maxTime))
            #self.emit(SIGNAL(''),)
            self.emit(SIGNAL('setItem(int, int, float)'), self.maxTime, self.minTime, self.totTime/self.pktsRcvd )
        print("")
        return
    
    #=============================================================================#
   # def signal_handler(self, signum, frame):
        """
        Handle exit via signals
        """
     #   self.dump_stats()
     #   print("\n(Terminated with signal %d)\n" % (signum))
     #   sys.exit(0)
    
    #=============================================================================#
    def verbose_ping(self, hostname, timeout = 3000, count = 3,numDataBytes = 64, path_finder = False):
        """
        Send >count< ping to >destIP< with the given >timeout< and display
        the result.
        """
        #signal.signal(signal.SIGINT, self.signal_handler)   # Handle Ctrl-C
        #if hasattr(signal, "SIGBREAK"):
            # Handle Ctrl-Break e.g. under Windows
         #   signal.signal(signal.SIGBREAK, self.signal_handler)
        self.host = hostname
        qDebug('inside verbose_ping :host : '+ hostname)
        #self = self() # Reset the stats
    
        mySeqNumber = 0 # Starting value
    
        try:
            destIP = socket.gethostbyname(hostname)
            print("\nPYTHON PING %s (%s): %d data bytes" % (hostname, destIP, numDataBytes))
           # print('hostname', type(hostname))
           # print('destIp', type(destIP))
           # print('numDataBytes', type(numDataBytes))
            #self.emit(SIGNAL(''),)
        except socket.gaierror as e:
            #print("\nPYTHON PING: Unknown host: %s (%s)" % (hostname, e.args[1]))
            self.emit(SIGNAL('pingErr(QString)'),'PYTHON PING: Unknown host:'+ hostname)
            return
    
        self.thisIP = destIP
    
        for i in range(count):
            delay = self.do_one(destIP, hostname, timeout, mySeqNumber, numDataBytes)
    
            if delay == None:
                delay = 0
    
            mySeqNumber += 1
    
            # Pause for the remainder of the MAX_SLEEP period (if applicable)
            if (MAX_SLEEP > delay):
                time.sleep((MAX_SLEEP - delay)/1000)
    
        self.dump_stats()
        self.exec_()
    #=============================================================================#
    def quiet_ping(self,hostname, timeout = 3000, count = 3,
                         numDataBytes = 64, path_finder = False):
        """
        Same as verbose_ping, but the results are returned as tuple
        """
        #myStats = MyStats() # Reset the stats
        mySeqNumber = 0 # Starting value
    
        try:
            destIP = socket.gethostbyname(hostname)
        except socket.gaierror as e:
            return False
    
        self.thisIP = destIP
    
        # This will send packet that we dont care about 0.5 seconds before it starts
        # acrutally pinging. This is needed in big MAN/LAN networks where you sometimes
        # loose the first packet. (while the switches find the way... :/ )
        if path_finder:
            #fakeStats = MyStats()
            #self.do_one(fakeStats, destIP, hostname, timeout, mySeqNumber, numDataBytes, quiet=True)
            time.sleep(0.5)
    
        for i in range(count):
            delay = self.do_one(destIP, hostname, timeout,
                            mySeqNumber, numDataBytes, quiet=True)
    
            if delay == None:
                delay = 0
    
            mySeqNumber += 1
    
            # Pause for the remainder of the MAX_SLEEP period (if applicable)
            if (MAX_SLEEP > delay):
                time.sleep((MAX_SLEEP - delay)/1000)
    
        if self.pktsSent > 0:
            self.fracLoss = (self.pktsSent - self.pktsRcvd)/self.pktsSent
        if self.pktsRcvd > 0:
            self.avrgTime = self.totTime / self.pktsRcvd
    
        # return tuple(max_rtt, min_rtt, avrg_rtt, percent_lost)
        self.emit(SIGNAL('setItem(int, int, int, QString)'), self.maxTime, self.minTime, str(self.avrgTime) )
        return self.maxTime, self.minTime, self.avrgTime, self.fracLoss
    
    #=============================================================================#
    def run(self):
        self.verbose_ping(self.host)
        qDebug('inside run :host : '+self.host)
        self.exec_()

    def slot(self,host):
        self.host = host
        qDebug('inside slot :host : '+ host)