from tkinter import *
from chatroom import Chatroom
import threading

PORT = 9056
#ip = '10.0.0.89'
ip = '167.99.160.18'


class Login:
    
    def __init__(self):
        self.container = Tk()
        self.login_UI()
        self.ADDR = (ip,PORT)
        self.container.mainloop()
    
    def login_UI(self):
        self.login_frame = Frame(self.container, width = 170, height = 380, bg = 'lightgrey')
        self.login_frame.grid(row = 0, column = 1, padx = 5, pady = 5)

        self.username_label = Label(self.login_frame, text = "Username")
        self.username_label.grid(row = 1, column = 0, padx = 5, pady = 5)

        self.username_entry = Entry(self.login_frame, width = 30)
        self.username_entry.grid(row = 1, column = 1, padx = 5, pady = 5)

        self.password_label = Label(self.login_frame, text = "Password")
        self.password_label.grid(row = 2, column = 0, padx = 5, pady = 5)
        
        self.password_entry = Entry(self.login_frame, show = "*" ,width = 30)
        self.password_entry.grid(row = 2, column = 1, padx = 5, pady = 5) 

        
        self.login_btn = Button(self.login_frame, text =  "Login" , width = 8, command = self.login_pressed )
        self.login_btn.grid(row = 3, column = 0, padx = 5, pady = 5)

    def login_account(self):
        self.chatroom = Chatroom( self.name, self.ADDR)
        


    def login_destroy(self):
        self.container.destroy()
        #self.container.withdraw()
        

    def login_pressed(self):
        self.name = self.username_entry.get()
        threading.Thread(target = self.login_account).start()
        print("destory")
        self.login_destroy()
        

    def logout(self):
        self.container.deiconify()
        
        


