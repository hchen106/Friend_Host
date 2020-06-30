from tkinter import *
import threading
import socket
import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'controller')))
from controller.message_encoder import message
from view.stream_display import stream


class Chatroom:

    stop_thread = False

    #TODO: 
    def __init__(self, username, ADDR):
        pass
        self.username = username
        self.ADDR = ADDR
        self.tcp_connection()
        self.frame = Tk()
        self.frame.resizable(0, 0)
        self.frame.geometry("275x400")
        self.frame.title("Friend Host")
        self.frame.protocol("WM_DELETE_WINDOW",self.close)
        self.chatroom_UI()
        self.initialize()
        self.frame.mainloop()

    def chatroom_UI(self):
         #the Right frame of the GUI
        self.subframe = Frame(self.frame, width = 170, height = 380, bg = 'lightgrey')
        self.subframe.grid(row = 0, column = 1, padx = 5, pady = 5, sticky="nsew")

        #Chat room Text display
        self.chat_room = Text(self.subframe, width = 30, height = 19)
        self.scroll_bar = Scrollbar(self.subframe, command=self.chat_room.yview, orient = "vertical")
        self.chat_room.grid(row = 0, column = 0, padx = 5, pady = 5, sticky="nsew")
        self.scroll_bar.grid(row = 0, column = 1, sticky = "ns")
        self.chat_room.configure(yscrollcommand = self.scroll_bar.set)
        self.text_entry = Entry(self.subframe, width = 30)
        self.text_entry.bind("<Return>", self.pressEnter)
        self.text_entry.grid(row = 1, column = 0, padx = 5, pady = 5, sticky="nsew")   
        
        
        self.btn_frame = Frame(self.subframe, width = 30)
        self.btn_frame.grid(row = 2, column = 0, padx = 5, pady = 5)   

        
        #send button to send / show message in chat room
        self.send_btn = Button(self.btn_frame, text = 'Send', width = 8, command=self.sendText)
        self.send_btn.grid(row = 2, column = 0, padx = 5, pady = 5)

        self.stream_btn = Button(self.btn_frame, text = 'Stream', width = 8, command=self.start_stream)
        self.stream_btn.grid(row = 2, column = 1, padx = 5, pady = 5)

        

    
    def pressEnter(self, event) :
        a = event
        self.sendText()


    #function for text entry displays in chat room
    def sendText(self):
        m = message()
        mes = m.encode(self.username,self.text_entry.get())
        #mes = bytes(self.text_entry.get(), 'utf-8')
        try:
            self.tcp_socket.send(mes)
            print("Message Sent")
        except:
            print("Failed to send message")
        """
        try:
            response = self.tcp_socket.recv(4096)
            if(response == b'received'): 
                print("response received")
        except:
            print("Failed to receive Response")
        """
        #auto scroll when text is full
        self.is_text_full = self.chat_room.yview()[1] == 1.0
        self.chat_room.insert(END, self.username + " : " + self.text_entry.get() + "\n")
        if self.is_text_full:
            self.chat_room.see("end")
        self.text_entry.delete(0, END)

    def update_chat_room(self):
        self.chat_room.insert(END, "You have entered the chat room")
        #TODO: 
        while True: 
            #print("1")
            
            mes = self.tcp_socket.recv(4096)
            
            if(mes == b''):
                break
            m = message()
            m.decode(mes)

            if(m.get_username() == "server"):
                code = m.get_message().split(':',1)
                #print(code[0])
                #print(code[1])
                if(code[0] == "2"):
                    threading.Thread(target = self.stream_room).start()
                    #print("enter")
                    self.chat_room.insert(END,code[1] + "\n")
                elif(code[0] == "3"):
                    self.chat_room.insert(END,code[1] + "\n")
                else:
                    self.chat_room.insert(END, m.get_message() + "\n")
            else:
                #s = mes.decode("utf-8")
                self.chat_room.insert(END, m.get_username() + " : " + m.get_message() + "\n")
                self.text_entry.delete(0, END)
            
        
        try:
            self.tcp_socket.close()
            print("finished")
        except:
            print("Failed to close the tcp socket.")
        print("done")

    def stream_room(self):
        self.stream = stream(self.username,self.ADDR[0],self.ADDR[1]+1)

    def close(self):


        self.tcp_socket.send(b'')
        
        
        m = "" + self.username + " closed"
        m = bytes(m,'utf-8')
        #self.closing_tcp_socket.send(m)


        self.frame.destroy()
        
        
        
        print("finished")
        
        #print(self.updateThread.is_alive())
        #sys.exit()
            

    #Establish tcp_connecton for chat room
    def tcp_connection(self):   
        #First Socket: Dara receive tcp socket
        self.tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.tcp_socket.connect(self.ADDR)
        #self.tcp_socket.send(b'first')
        #threading.Thread(target=self.initialize).start()
        m = bytes(self.username, 'utf-8')
        self.tcp_socket.send(m)

        #Second Socket: closing command transistion tcp socket
        # self.closing_tcp_socket =socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        # self.closing_tcp_socket.connect((self.ADDR[0],self.ADDR[1] + 1))
        

    #Initialization of all the functionalities. 
    def initialize(self): 
        #Initialize a thread to wait for messages from other clients.
        self.stop_thread = False
        self.updateThread = threading.Thread(target=self.update_chat_room)
        self.updateThread.start()
        #self.updateThread.start()
        #self.updateThread.set()
    
    def start_stream(self):
        m = message()
        mes = m.encode("server","1 " + self.username + " has started a streaming.")
        self.tcp_socket.send(mes)
        #self.stream = stream(self.username,self.ADDR[0],self.ADDR[1]+1)
    


   
