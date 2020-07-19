import socket
import sys
import threading
import pickle
import struct
from controller.message_encoder import message
from struct import unpack
from struct import pack
import time
import cv2

class server:
    
    PORT = 8007
    ADDR = ('',PORT)
    clients_address = []
    clients_socket = {}
    visitor_list = {}
    buffer = []
    Size = 0
    closing_size = 0
    Host = False
    Host_num = 0
    visitor_num = 0
    FORCE_CLOSED = False
    #ip = '10.0.0.89'threading
    #ip = '167.99.160.18'
    ip = 'localhost'
    
   
    def __init__(self,port,ip, connection):
        #print("server established")
        # self.tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        # self.tcp_socket.bind(('',self.PORT))
        # self.tcp_socket.listen(5)
        self.PORT = port
        self.ip = ip
        self.tcp_socket = connection
        
        #self.tcp_connection()
        threading.Thread(target=self.tcp_connection).start()
        
    
    
    def print_clients(self):
        print("-------------clients_socket--------")
        for c in self.clients_socket:
            print(c)
        print("----------------------")
    
   

    def recv_message(self,user):
        #try: 
        while(True):
            try:
                mes = self.clients_socket[user].recv(4096)
                print(mes)
                
                self.send_message(user,mes)
            except:
                break
        #except: 
        #    print("Failed to receive message")
        
    def send_message(self,user,mes):
        if(mes != b''):
            m = message()
            m.decode(mes)
            
            if(m.get_username() == "server" and m.get_message() == ":"):
                self.clients_socket[user].send(mes)
                #self.closing_socket[num] = None
                self.Host = False
                del self.clients_socket[user]
                print("One client log out")
                self.print_clients()
                #self.print_closing()
                #mes = b'User has quit the room'
            elif(m.get_username() == "server" and m.get_message() == " "):
                self.clients_socket[use].send(mes)
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
                            self.Host_num = user
                            c = code[1].split(':',1)
                            self.clients_socket[user].send(b'server 2:You start streaming.')
                            #TODO: Establishing a thread to receive video and audio frames
                            threading.Thread(target = self.udp_connection).start()
                        else: 
                            self.clients_socket[user].send(b'server 3:Someone in the chatroom is streaming.')
                            allow = False
                #try: 
                    
                i = 0
                if(allow == True):
                    for users in self.clients_socket: 
                        if(users != user and self.clients_socket[users] != None): 
                            self.clients_socket[users].send(mes)
                """
                while(i < self.Size and allow == True) :
                    if(i!=num and self.clients_socket[i] != None): 
                        self.clients_socket[i][1].send(mes)
                    i += 1
                """
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
            if(m == b''): 
                break
            m = m.decode("utf-8")
            self.clients_socket[m] = c[0]
           
            #self.clients_socket.append(c[0])
            threading.Thread(target = self.recv_message,args = (m,)).start()
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
        threading.Thread(target = self.wait_for_join_stream).start()
        #self.receive_and_send_frame()
        #self.receive_frame()
        self.receive_File()

    
    def wait_for_join_stream(self):
        while self.Host:
            c, addr = self.stream_socket.accept()
            data = c.recv(4096)
            d = data.decode('utf-8')
            self.visitor_list[d] = c
            self.visitor_num += 1
            """
            data , addr = self.udp_socket.recvfrom(4096)
            d = data.decode('utf-8')
            
            self.visitor_list.append((d,addr))
            self.visitor_num += 1
            """
    
    def receive_File(self): 
        count = 0
        self.recv_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.recv_socket.bind((self.ip, self.PORT+2))
        self.recv_socket.listen(5)

        connection, addr = self.recv_socket.accept()
        finished = False
        video = open("result.mp4","wb")
        print(connection)
        while True: 

            buf = connection.recv(4096)

            if buf != b'': 
                print(buf)
                count += 1
                video.write(buf)
            else: 
                print(buf)
                break
        
        self.recv_socket.close()
        threading.Thread(target = self.send_frame).start()
        
        
        

        
        
    def receive_frame(self):
        #TODO: receive frame from the host
        frame_count = 0
        self.recv_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.recv_socket.bind((self.ip,self.PORT+2))
        self.recv_socket.listen(5)
        connection, addr = self.recv_socket.accept()
        payload_size = struct.calcsize("L")
        #threading.Thread(target = self.send_frame).start()
        while True:
            #print(addr)
            data = b''
            print(frame_count)
            
            data += connection.recv(4096)
            #print(data)
            if data == b'': 
                break
            while len(data) < payload_size:
                data += connection.recv(4096)
            
            packed_msg_size = data[:payload_size]
            data = data[payload_size:]
            msg_size = unpack("L", packed_msg_size)[0] ### CHANGED

            # Retrieve all data based on message size
            while len(data) < msg_size:
                data += connection.recv(4096)

            
            """
            l =  connection.recv(8)
            print(l)
            if l == b'': 
                break
            
            (length,) = unpack('>Q', l)
            data = b''
            while len(data) < length:
                # doing it in batches is generally better than trying
                # to do it all in one go, so I believe.
                #to_read = length - len(data)
                data += connection.recv(100000)
            """
            connection.send(b'ended')
            
            #self.buffer.append((frame_count, l, data))
            self.buffer.append((frame_count, packed_msg_size, data))
            frame_count += 1
            
            
            #threading.Thread(target = self.send_frame, args = (l, data,)).start()
            # F = open("frame1.jpg","wb")
            # F.write(data)
            # F.close()
            #threading.Thread(target = self.send_frame, args = (video_frame,)).start()
        self.send_frame()
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
            #time.sleep(0.04)
    """

    def send_frame(self):
        print("send_frame")
        #self.sender_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        current = 0
        while True:
            #TODO: send frame to all visitors
            #length = pack('>Q', len(data))
            #print(length)
            #print(visitor)
            # sendall to make sure it blocks if there's back-pressure on the socket
            self.file = cv2.VideoCapture("result.mp4")
            self.file.set(3,1280)
            self.file.set(4,720)
            count = 0
            while self.file.isOpened(): 
                #time.sleep(1.5)
        

                ret, frame = self.file.read()
                if ret: 
                    
                    cv2.imwrite("frame.jpg",frame)
                    if cv2.waitKey(10) & 0xFF == ord('q'):
                        break
                    F = open("frame.jpg",'rb')
                    data = F.read()
                    F.close()

                    
                    length = pack('>Q', len(data))
                    print(length)
                    #print(length)
                    count += 1
                    # sendall to make sure it blocks if there's back-pressure on the socket
                    
                    for visitor in self.visitor_list:
                    
                        self.visitor_list[visitor].sendall(length)
                        self.visitor_list[visitor].sendall(data)
                    #self.sender_socket.sendall(b'ended')
                        self.mess = b''
                        while self.mess != b'ended':
                            self.mess = self.visitor_list[visitor].recv(4096)
                    """

                    data = pickle.dumps(data)

                    # Send message length first
                    message_size = pack("L", len(data)) ### CHANGED

                    # Then data
                    self.sender_socket.sendall(message_size + data)


                        print(frame[1])
                        self.visitor_list[visitor].sendall(frame[1] + frame[2])
                    """
                    
                    #self.visitor_list[visitor].sendall(frame[2])
                    
                #time.sleep(0.04)
        

                    

    """
    def send_frame(self, length, data):
        
        #self.sender_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        
        for visitor in self.visitor_list:
            #TODO: send frame to all visitors
            #length = pack('>Q', len(data))
            #print(length)
            #print(visitor)
            # sendall to make sure it blocks if there's back-pressure on the socket
            length = pack('>Q', len(data))
            self.visitor_list[visitor].sendall(length)
            self.visitor_list[visitor].sendall(data)

            self.mess = b''
            while self.mess != b'ended':
                self.mess = self.visitor_list[visitor].recv(4096)
    """


#server()
    
    
    
    





    
