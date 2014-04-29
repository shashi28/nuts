#!/usr/bin/python

import socket, sys
from PyQt4.QtCore import *
from PyQt4.QtGui import *

from ui_whois import Ui_Dialog

class MainWindow(QDialog,Ui_Dialog):
    def __init__(self,parent = None):
        super(MainWindow,self).__init__(parent)
        self.setupUi(self)
        self.connect(self.pushButton,SIGNAL('clicked()'),self.action)

    def action(self):
        self.host = self.lineEdit.text()
        whois_data = self.get_whois_data(str(self.host))
        self.textEdit.setText(whois_data)

    #Perform a generic whois query to a server and get the reply
    def perform_whois(self,server , query) :
        #socket connection
        s = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
        s.connect((server , 43))

        #send data
        s.send(query + '\r\n')

        #receive reply
        msg = ''
        while len(msg) < 10000:
            chunk = s.recv(100)
            if(chunk == ''):
                break
            msg = msg + chunk

        return msg
    #End

    #Function to perform the whois on a domain name
    def get_whois_data(self,domain):

        #remove http and www
        domain = domain.replace('http://','')
        domain = domain.replace('www.','')

        #get the extension , .com , .org , .edu
        ext = domain[-3:]

        #If top level domain .com .org .net
        if(ext == 'com' or ext == 'org' or ext == 'net'):
            whois = 'whois.internic.net'
            msg = self.perform_whois(whois , domain)

            #Now scan the reply for the whois server
            lines = msg.splitlines()
            for line in lines:
                if ':' in line:
                    words = line.split(':')
                    if  'Whois' in words[0] and 'whois.' in words[1]:
                        whois = words[1].strip()
                        break;

        #Or Country level - contact whois.iana.org to find the whois server of a particular TLD
        else:
            #Break again like , co.uk to uk
            ext = domain.split('.')[-1]

            #This will tell the whois server for the particular country
            whois = 'whois.iana.org'
            msg = self.perform_whois(whois , ext)

            #Now search the reply for a whois server
            lines = msg.splitlines()
            for line in lines:
                if ':' in line:
                    words = line.split(':')
                    if 'whois.' in words[1] and 'Whois Server (port 43)' in words[0]:
                        whois = words[1].strip()
                        break;

        #Now contact the final whois server
        msg = self.perform_whois(whois , domain)

        #Return the reply
        return msg
    # end
app = QApplication(sys.argv)
form = MainWindow()
form.show()
app.exec_()
