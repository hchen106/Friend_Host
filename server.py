import socket
import sys
import threading
import pickle
import struct
from message_encoder import message

class server:
    
    PORT = 9054
    ADDR = ('',PORT)
    clients_address = []
    clients_socket = []
    closing_socket = []
    Size = 0
    closing_size = 0
    
    #d = b''
    def __init__(self):
        self.tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.tcp_socket.bind(('',self.PORT))
        self.tcp_socket.listen(5)
        self.closing_tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.closing_tcp_socket.bind(('',self.PORT+1))
        self.closing_tcp_socket.listen(5)

        threading.Thread(target=self.tcp_connection).start()
        threading.Thread(target=self.closing_tcp_connection).start()
        #self.print_list()


    def print_clients(self):
        print("-------------clients_socket--------")
        for c in self.clients_socket:
            print(c)
        print("----------------------")
    
    def print_closing(self):
        print("-------------closing_socket--------")
        for c in self.closing_socket:
            print(c)
        print("----------------------")

    """
    def recv_screen(self):
        print("in recv_screen")
        data = b''
        payload_size = struct.calcsize("L") 
        while True:
            while len(data) < payload_size:
                data += self.clients_socket[0].recv(4096)
            packed_msg_size = data[:payload_size]
            data = data[payload_size:]
            msg_size = struct.unpack("L", packed_msg_size)[0]
            while len(data) < msg_size:
                data += self.clients_socket[0].recv(4096)
            frame_data = data[:msg_size]
            data = data[msg_size:]

            if self.Size > 1:

                d = pickle.dumps(frame_data) ### new code
                self.clients_socket[1].sendall(struct.pack("L", len(d))+d) ### new code
            
            ###
            
            frame=pickle.loads(frame_data)
            print frame
            cv2.imshow('framd = pickle.dumps(frame_data) ### new code
            self.tcp_socket.sendall(struct.pack("H", len(d))+d) ### new codeonnection
            
        """

    def recv_message(self,num):
        try: 
            while(True):
                mes = self.clients_socket[num][1].recv(4096)
                """
                try: 
                    self.clients_socket[num].send(b'received')
                except:
                    print("Failed to reply ")
                """
                self.send_message(num,mes)
        except: 
            print("Failed to receive message")
        
    def send_message(self,num,mes):
        if(mes == b''):
            self.clients_socket[num][1].send(mes)
            #self.closing_socket[num] = None
            self.clients_socket[num] = None
            print("One client log out")
            self.print_clients()
            #self.print_closing()
            #mes = b'User has quit the room'
        else:
            try: 
                
                i = 0
                while(i < self.Size) :
                    if(i!=num and self.clients_socket[i] != None): 
                        self.clients_socket[i][1].send(mes)
                    i += 1
            except: 
                print("Failed to send message ")
    
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

    def closing_tcp_connection(self):
        while True:
            c  = self.closing_tcp_socket.accept()

           
            self.closing_socket.append(c[0])
            threading.Thread(target = self.recv_closing_message,args = (self.closing_size ,)).start()
            addr = c[1]
            #self.clients_address.append(addr)

            self.closing_size += 1
            self.print_closing()
            """
            if self.Size == 0:
                c[0].send(b'host')
               # threading.Thread(target = self.recv_message,args = (self.Size)).start()
            else:
                c[0].send(b'client')
            """


            
            """
            print("Get connection from: ", addr)
            m = ("welcome to chat room").encode('utf-8')
            c[0].send(m)
            """



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
            """
            if self.Size == 0:
                c[0].send(b'host')
               # threading.Thread(target = self.recv_message,args = (self.Size)).start()
            else:
                c[0].send(b'client')
            """

            
            self.Size += 1
            self.print_clients()
            
            """
            print("Get connection from: ", addr)
            m = ("welcome to chat room").encode('utf-8')
            c[0].send(m)
            """


server()
    
    
    
    





    
