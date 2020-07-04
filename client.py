import socket
import sys
from tkinter import *
import time
import cv2
import mss
import numpy as np
from PIL import ImageTk, Image
import cv2
import pickle
import struct
import threading
from view.login import Login
from view.login_pyqt import Ui_Login


class client:

    PORT = 9026
    #ip = '10.0.0.89'
    ip = '167.99.160.18'
    ADDR = (ip,PORT)

    #DEFAULT USERNAME
    #username = "User1"
    

    def __init__(self):
        #self.frame = frame
        
        #Video Capture UI
        #self.GUI()
        
        #Chat Room UI
        #self.tcp_connection()
        #self.chatroom = Chatroom( self.username, self.ADDR)
        self.login = Ui_Login()
        
        # newChatroom = chatroom.Chatroom(frame, username, ADDR)
        # newChatroom.tcp_connection()
        # newChatroom.chatroom_UI()
        
        

    
    #start to capture screen HOWEVER IT DOESNT WORK !!!!
    def startStream(self):
        self.scene = mss.mss()
        self.screen = {"top": 40, "left": 0,"width":1000,"height":900}
        self.readscreen_ms = scene.grab(self.screen)
        self.readscreen_np = np.array(self.readscreen_ms)
        self.readscreen = Image.fromarray(self.readscreen_np)
        self.readscreen_tk = ImageTk.PhotoImage(image = readscreen)
        self.showscreen = Label(mainframe, image = self.readscreen_tk)               
        self.showscreen.pack()
        print("HI")

    


    #GUI
    def GUI(self):
        self.frame = Tk()
        
        #self.Display = Label(self.frame, height=50,width = 200)
        #self.Display.grid(row=0, column=0, columnspan=4, sticky=W+E+N+S, padx=5, pady=5)
        
        #the Left frame of the GUI
        self.mainframe = Frame(self.frame, width = 500, height = 380, bg = 'lightgrey')
        self.mainframe.grid(row = 0, column = 0, padx = 5, pady = 5)
        
        #buttons frame to put buttons
        self.buttons_frame = Frame(self.frame, width = 500, height = 50, bg = 'lightgrey')
        self.buttons_frame.grid(row = 1, column = 0, padx = 10, pady = 0)

        #start button
        self.start_btn = Button(self.buttons_frame, text = 'Start', width=8, command = self.startStream)
        self.start_btn.grid(row = 0, column = 0, padx = 5, pady = 5)

        #stop button
        self.stop_btn = Button(self.buttons_frame, text = 'Stop', width=8)
        self.stop_btn.grid(row = 0, column = 1, padx = 5, pady = 5)

        #mute button
        self.mute_btn = Button(self.buttons_frame, text = 'Mute', width=8)
        self.mute_btn.grid(row = 0, column = 2, padx = 5, pady = 5)

        frame.mainloop()

    
    

    
        
    """
    def read_screen(self):
        ms = mss.mss()
        screen = {"top": 40, "left": 0,"width":1000,"height":900}
        while True:
            #capture screen pixel
            frame = ms.grab(screen)
            #cap = cv2.VideoCapture(0)
            #ret,frame = cap.read()
            #convert pixel to matrix and show it on cv2 
            #cv2.imshow('screen', np.array(frame))
            #print(readscreen_pil)
            #press q to quit

            data = pickle.dumps(frame) ### new code
            self.tcp_socket.sendall(struct.pack("L", len(data))+data) ### new code

            
            if cv2.waitKey(25) & 0XFF == ord('q'):
                cv2.destroyAllWindows()
                break
            

    def recv_screen(self):
        data = b''
        payload_size = struct.calcsize("L") 
        while True:
            while len(data) < payload_size:
                data += self.tcp_socket.recv(4096)
            packed_msg_size = data[:payload_size]
            data = data[payload_size:]
            msg_size = struct.unpack("L", packed_msg_size)[0]
            while len(data) < msg_size:
                data += self.tcp_socket.recv(4096)
            frame_data = data[:msg_size]
            data = data[msg_size:]

            
            ###
            
            frame=pickle.loads(frame_data)
            f2 = open('frame1.jpg','wb')
            f2.write(frame)
            #print frame
            #cv2.imshow('frame',np.array(frame))
    """

    



    


#frame.config(bg = "LightBlue1")


client()


