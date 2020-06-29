from tkinter import *
import socket

class stream:
    def __init__(self,username,ip,port):
        self.username = username
        self.ip = ip
        self.port = port
        self.ADDR = (self.ip,self.port)
        self.frame = Tk()
        self.display_UI()
        self.frame.title("Streaming")
        self.udp_connection()
        #self.frame.geometry("400x300")
        self.frame.mainloop()
        

    
    def display_UI(self):
        #the Left frame of the GUI
        self.mainframe = Frame(self.frame, width = 500, height = 380, bg = 'lightgrey')
        self.mainframe.grid(row = 0, column = 0, padx = 5, pady = 5)
        
        #Label
        self.stream_label = Label(self.frame)
        self.stream_label.grid(row = 1, column = 0, padx = 5, pady = 5)

        #buttons frame to put buttons
        self.buttons_frame = Frame(self.frame, width = 500, height = 50, bg = 'lightgrey')
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

    def udp_connection(self):
        self.udp_socket = socket.socket(socket.AD_INET,socket.SOCK_DGRAM)
        
