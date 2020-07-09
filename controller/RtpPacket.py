import sys
import time

class RtpPacket:

    def __init__(self):
        self.seqNum = 0
    
    def encode(self,seqnum, payload):
        self.seqNum = seqnum
        self.payload = payload

        return bytes(str(self.seqNum) + " " + self.payload, 'utf-8')        

    
    def decode(self, packet):
        mes = packet.decode('utf-8')
        mes = mes.split(' ', 1)
        self.seqNum = mes[0]
        self.payload = mes[1]

    def get_seqnum(self):
        return self.seqNum

    def get_payload(self):
        return self.payload

