import socket as sk
import sys
from PyQt4.QtCore import *
MAX_THREADS = 50

#def usage():
    #print("\npyScan 0.1")
    #print("usage: pyScan <host> [start port] [end port]")

class Scanner(QThread):
    def __init__(self):
        super(Scanner,self).__init__(self)
        # build up the socket obj
        self.sd = sk.socket(sk.AF_INET, sk.SOCK_STREAM)

    def run(self):
        try:
            # connect to the given host:port
            self.sd.connect((self.host, self.port))
            print("%s:%d OPEN" % (self.host, self.port))
            #self.emit('SIGNAL(QString),OPEN')
            self.sd.close()
        except: pass

    def init_slot(self,host,port):
        self.host = host
        self.port = port

class pyScan:
    def __init__(self, args=[]):
        try:
            sk.gethostbyname(self.host)
        except:
            print("hostname '%s' unknown" % self.host)
        self.scan(self.host, self.start, self.stop)

    def scan(self, host, start, stop):
        self.port = start
        while self.port <= stop:
            while threading.activeCount() < MAX_THREADS:
                Scanner(host, self.port).start()
                self.port += 1

if __name__ == "__main__":
    pyScan(sys.argv)
'''
#############################################################

# a simple portscanner with multithreading
# QUEUE BASED VERSION

import socket
import sys
import threading, Queue

MAX_THREADS = 50

class Scanner(threading.Thread):
    def __init__(self, inq, outq):
        threading.Thread.__init__(self)
        self.setDaemon(1)
        # queues for (host, port)
        self.inq = inq
        self.outq = outq

    def run(self):
        while 1:
            host, port = self.inq.get()
            sd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            try:
                # connect to the given host:port
                sd.connect((host, port))
            except socket.error:
                # set the CLOSED flag
                self.outq.put((host, port, 'CLOSED'))
            else:
                self.outq.put((host, port, 'OPEN'))
                sd.close()

def scan(host, start, stop, nthreads=MAX_THREADS):
    toscan = Queue.Queue()
    scanned = Queue.Queue()

    scanners = [Scanner(toscan, scanned) for i in range(nthreads)]
    for scanner in scanners:
        scanner.start()

    hostports = [(host, port) for port in xrange(start, stop+1)]
    for hostport in hostports:
        toscan.put(hostport)

    results = {}
    for host, port in hostports:
        while (host, port) not in results:
            nhost, nport, nstatus = scanned.get()
            results[(nhost, nport)] = nstatus
        status = results[(host, port)]
        if status <> 'CLOSED':
            print '%s:%d %s' % (host, port, status)

if __name__ == '__main__':
    scan('localhost', 0, 1024)
'''
None