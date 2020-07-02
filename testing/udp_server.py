import socket
import threading

class server:

    def __init__(self):
        self.ip = '167.99.160.18'
        self.port = 4006
        self.ADDR = (self.ip, self.port)
        #self.tcp_connecion()
        self.receive_connection()

    def tcp_connecion(self):
        print("In Tcp_connection")
        self.tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.tcp_socket.bind(('',self.port+1))
        self.tcp_socket.listen(5)
        client = self.tcp_socket.accept()
        
        while True:
            
            print("accept socket")
            data= client[0].recv(4096)
            print(data)
            mes = bytes(str(self.addr[1]), 'utf-8')
            client[0].send(mes)
            break


    def receive_connection(self):
        self.udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.udp_socket.bind(self.ADDR)
        self.sender_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        
        while True:
            data, self.addr = self.udp_socket.recvfrom(4096)
            print(self.addr)
            if(data == b'go'):
                #self.tcp_connecion()
                break
        
        self.sender_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sender_socket.sendto(b'how are you',(self.addr))

server()
