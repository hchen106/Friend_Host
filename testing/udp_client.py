import socket
import threading
import time
class client:

    def __init__(self):
        self.ip = '167.99.160.18'
        self.port = 4006
        self.ADDR = (self.ip, self.port)
        self.establish_connection()


    def tcp_connection(self):
        print("In TCP connection")
        self.tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        time.sleep(2)
        self.tcp_socket.connect((self.ip  ,self.port+1))
        self.tcp_socket.send(b'hi')

        while True:
            
            data= self.tcp_socket.recv(4096)
            if(data != b''):
                self.ad = data.decode("utf-8")
                print(data)
                break
    
    def establish_connection(self):
        self.udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.udp_socket.sendto(b'hi',self.ADDR)
        self.udp_socket.sendto(b'go',self.ADDR)


        #self.tcp_connection()
        self.recv_connection()
        

    def recv_connection(self):
        
        #self.receive_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        #self.receive_socket.bind(("localhost",int(self.ad)))

        while True:
            data, addr = self.udp_socket.recvfrom(4096)
            if(data):
                print(data)
        

client()