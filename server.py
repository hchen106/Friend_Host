import socket
import sys
import threading
import pickle
import struct
from controller.message_encoder import message
from struct import unpack
from struct import pack

class server:
    
    PORT = 9394
    ADDR = ('',PORT)
    clients_address = []
    clients_socket = []
    visitor_list = {}
    buffer = []
    Size = 0
    closing_size = 0
    Host = False
    Host_num = 0
    visitor_num = 0
    #ip = '10.0.0.89'
    #ip = '167.99.160.18'
    ip = 'localhost'
    
   
    def __init__(self):
        self.tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.tcp_socket.bind(('',self.PORT))
        self.tcp_socket.listen(5)
        
        
        threading.Thread(target=self.tcp_connection).start()
        


    def print_clients(self):
        print("-------------clients_socket--------")
        for c in self.clients_socket:
            print(c)
        print("----------------------")
    
   

    def recv_message(self,num):
        #try: 
        while(True):
            try:
                mes = self.clients_socket[num][1].recv(4096)
                print(mes)
                
                self.send_message(num,mes)
            except:
                break
        #except: 
        #    print("Failed to receive message")
        
    def send_message(self,num,mes):
        if(mes != b''):
            m = message()
            m.decode(mes)
            
            if(m.get_username() == "server" and m.get_message() == ":"):
                self.clients_socket[num][1].send(mes)
                #self.closing_socket[num] = None
                self.Host = False
                self.clients_socket[num] = None
                print("One client log out")
                self.print_clients()
                #self.print_closing()
                #mes = b'User has quit the room'
            elif(m.get_username() == "server" and m.get_message() == " "):
                self.clients_socket[num][1].send(mes)
                print("streaming closed")
                print(mes)
                self.Host = False
            else:
                
                allow = True
                if(m.get_username() == "server"):
                    
                    code = m.get_message().split(' ', 1)
                    if(code[0] == "1"):
                        if(self.Host == False):
                            self.Host = True
                            self.Host_num = num
                            c = code[1].split(':',1)
                            self.clients_socket[num][1].send(b'server 2:You start streaming.')
                            #TODO: Establishing a thread to receive video and audio frames
                            threading.Thread(target = self.udp_connection).start()
                        else: 
                            self.clients_socket[num][1].send(b'server 3:Someone in the chatroom is streaming.')
                            allow = False
                #try: 
                    
                i = 0
                while(i < self.Size and allow == True) :
                    if(i!=num and self.clients_socket[i] != None): 
                        self.clients_socket[i][1].send(mes)
                    i += 1
                #except: 
                #    print("Failed to send message ")
    
    def recv_closing_message(self,num):
        index = 0
        print("enter closing")
       
        while(True):
            mes = self.closing_socket[num].recv(4096)
            s = mes.decode("utf-8")
            lst = s.split(' ', 1)
            print(lst)
            n = lst[0]
            c = lst[1]
            for i in self.clients_socket:
                if(i[0] == n):
                    i[1].send(b'closed')
                    self.clients_socket[index] = None
                    print("found")
                    break
                index += 1
        

        self.closing_socket[num] = None
        #self.clients_socket[num] = None
        print("One client log out")
        self.print_clients()
        self.print_closing()

   

    def tcp_connection(self):
        while True:
            c  = self.tcp_socket.accept()

            m = c[0].recv(4096)
            m = m.decode("utf-8")
            self.clients_socket.append((m,c[0]))
           
            #self.clients_socket.append(c[0])
            threading.Thread(target = self.recv_message,args = (self.Size,)).start()
            o = message()
            mes = o.encode("server", m + " has enter the chat room")
            self.send_message(self.Size,mes)
            
            addr = c[1]
            self.clients_address.append(addr) 
            self.Size += 1
            self.print_clients()
            

    def udp_connection(self):

        
        # self.visit_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        # self.visit_socket.bind(('',self.PORT+1))
        # self.visit_socket.listen(5)
        self.stream_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.stream_socket.bind((self.ip,self.PORT+1))
        self.stream_socket.listen(5)

        c, addr = self.stream_socket.accept()
        data = c.recv(4096)
        d = data.decode('utf-8')
        self.visitor_list[d] = c
        self.visitor_num += 1
        
        #print(addr)
        #threading.Thread(target = self.wait_for_join_stream).start()
        #self.receive_and_send_frame()
        self.receive_frame()


    
    def wait_for_join_stream(self):
        while True:
            data , addr = self.udp_socket.recvfrom(4096)
            d = data.decode('utf-8')
            
            self.visitor_list.append((d,addr))
            self.visitor_num += 1
        
    def receive_frame(self):
        #TODO: receive frame from the host
        frame_count = 0
        self.recv_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.recv_socket.bind((self.ip,self.PORT+2))
        self.recv_socket.listen(5)
        connection, addr = self.recv_socket.accept()
        #threading.Thread(target = self.send_frame).start()
        while True:
            #print(addr)
            l =  connection.recv(8)
            #print(l)
            (length,) = unpack('>Q', l)
            data = b''
            while len(data) < length:
                # doing it in batches is generally better than trying
                # to do it all in one go, so I believe.
                #to_read = length - len(data)
                data += connection.recv(4096)
            connection.send(b'ended')
            self.buffer.append((frame_count, l, data))
            frame_count += 1
            threading.Thread(target = self.send_frame, args = (l, data,)).start()
            # F = open("frame1.jpg","wb")
            # F.write(data)
            # F.close()
            #threading.Thread(target = self.send_frame, args = (video_frame,)).start()
    """
    def send_frame(self):
        
        #self.sender_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        current = 0
        while True:
            if(current < len(self.buffer)):
                frame = self.buffer[current]
                current += 1
                for visitor in self.visitor_list:
                    #TODO: send frame to all visitors
                    #length = pack('>Q', len(data))
                    #print(length)
                    #print(visitor)
                    # sendall to make sure it blocks if there's back-pressure on the socket
                    self.visitor_list[visitor].sendall(frame[1])
                    self.visitor_list[visitor].sendall(frame[2])

                    self.mess = b''
                    while self.mess != b'ended':
                        self.mess = self.visitor_list[visitor].recv(4096)
    """

    def send_frame(self, length, data):
        
        #self.sender_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        
        for visitor in self.visitor_list:
            #TODO: send frame to all visitors
            #length = pack('>Q', len(data))
            #print(length)
            #print(visitor)
            # sendall to make sure it blocks if there's back-pressure on the socket
            self.visitor_list[visitor].sendall(length)
            self.visitor_list[visitor].sendall(data)

            self.mess = b''
            while self.mess != b'ended':
                self.mess = self.visitor_list[visitor].recv(4096)



server()
    
    
    
    





    
