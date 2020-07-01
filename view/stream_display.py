from __future__ import division
from tkinter import *
import socket
import threading
import cv2
import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'controller')))
from controller.message_encoder import message
import time
import struct
import math
import numpy as np


class stream:
    
    """
    Constructor: Initialize every necessary information
    """
    def __init__(self, frame, username,ip,port,host):
       # self.tcp_socket = tcp_socket
        self.username = username
        self.ip = ip
        self.port = port
        self.ADDR = (self.ip,self.port)
        self.stream_frame = Tk()
        self.display_UI()
        #self.stream_frame.protocol("WM_DELETE_WINDOW",self.close_stream)
        self.stream_frame.title("Streaming")
        #self.udp_connection()
        self.host = host
        threading.Thread(target = self.udp_connection).start()
        #self.frame.geometry("400x300")
        self.stream_frame.mainloop()
        

    """
    GUI for the Streaming window
    """
    def display_UI(self):
        #the Left frame of the GUI
        self.mainframe = Frame(self.stream_frame, width = 500, height = 380, bg = 'lightgrey')
        self.mainframe.grid(row = 0, column = 0, padx = 5, pady = 5)
        
        #Label
        self.stream_label = Label(self.stream_frame)
        self.stream_label.grid(row = 1, column = 0, padx = 5, pady = 5)

        #buttons frame to put buttons
        self.buttons_frame = Frame(self.stream_frame, width = 500, height = 50, bg = 'lightgrey')
        self.buttons_frame.grid(row = 2, column = 0, padx = 5, pady = 5)

        #start button
        self.start_btn = Button(self.buttons_frame, text = 'Start', width=8)
        self.start_btn.grid(row = 0, column = 0, padx = 5, pady = 5)

        #stop button
        self.stop_btn = Button(self.buttons_frame, text = 'Stop', width=8)
        self.stop_btn.grid(row = 0, column = 1, padx = 5, pady = 5)

        #mute button
        self.mute_btn = Button(self.buttons_frame, text = 'Mute', width=8)
        self.mute_btn.grid(row = 0, column = 2, padx = 5, pady = 5)
    
    """
    Take action when the user clicks on the close button on the top-left corner of the frame
    """
    def close_stream(self):
        

        #time.sleep(0.3)

        self.stream_frame.quit()
        self.stream_frame.destroy()
        print("streaming closed")

    """
    Establish a UDP socket with the server to send video frames
    """
    def udp_connection(self):
        self.udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        #threading.Thread(target = tself.sendFrame).start()
        mes = bytes(self.username, 'utf-8')
        self.udp_socket.sendto(mes ,self.ADDR)
        
        if(self.host == True):
            threading.Thread(target = self.sendFrame).start()
        self.recvFrame()
        
        



    
    def sendFrame(self):
        """
        self.filename = ""
        self.seqnum = 0
        self.file = cv2.VideoCapture(self.filename)
        self.file.set(3,1280)
        self.file.set(4,720)

        while self.file.isOpened():
            ret,frame = self.file.read()
            if ret:
        """
        self.file = cv2.VideoCapture(0)
        # self.file.set(3,1280)
        # self.file.set(4,720)
        #encode_param = [int(cv2.IMWRITE_JPEG_QUALITY),90]
        self.sender_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
        #self.sender_socket.sendto(b'hi',(self.ip,self.port+1))
        
        while (self.file.isOpened()):
            ret, frame = self.file.read()
            #cv2.imshow('frame',frame)
            #if cv2.waitKey(1) & 0xFF == ord('q'):
            #    break
            frame = cv2.imencode('.jpg',frame)[1]
            #result, frame = cv2.imencode('.jpg',frame,encode_param)
            data = frame.tostring()
            data_size = len(data)
            count = math.ceil(data_size/(4096-64))
            start_pos = 0
            #print("send")
            while count: 
                #print("hi")
                end_pos = min(data_size, start_pos + 4096-64)
                self.sender_socket.sendto(struct.pack("B",count) + data[start_pos:end_pos] ,(self.ip,self.port+1))
                start_pos = end_pos
                count -= 1
                
        
        self.file.release()
            
        mes = bytes("hi", 'utf-8')
        
    
    def recvFrame(self):
        self.buffer()
        print("yo")
        frame = b''
        while True:
            #data , addr = self.udp_socket.recvfrom(4096)
            #print(data)
            print("hi")
            
            data ,addr = self.udp_socket.recvfrom(4096)
            if(data):
                if struct.unpack("B",data[0:1])[0] > 1:
                    frame += data[1:]
                    
                else:
                    frame += data[1:]
                    frame = cv2.imdecode(np.fromstring(frame,dtype = np.uint8),1)
                    
                    try:
                        cv2.imshow('frame',frame)
                        if cv2.waitKey(1) & 0xFF == ord('q'):
                            break
                    except:
                        print("Packet Loss")
                    
                    #f = open("frame.jpg","wb")
                    #f.write(frame)
                    #f.close()
                    frame = b''
                print("done")

    def buffer(self):
        while True:
            print("oh")
            data, addr = self.udp_socket.recvfrom(4096)
            if(data):
                if(struct.unpack("B",data[0:1])[0] == 1):
                    break

    

