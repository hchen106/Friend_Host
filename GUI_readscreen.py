from tkinter import *
import cv2
import mss
import numpy as np
from PIL import ImageTk


window = Tk()
window.title("Read Screen")
window.config(bg = "LightBlue1")
#window.resizable()

mainframe = Frame(window, width = 500, height = 380, bg = 'lightgrey')
mainframe.grid(row = 0, column = 0, padx = 5, pady = 5)

def start(self):
    scene = mss.mss()
    screen = {"top": 40, "left": 0,"width":1000,"height":900}
    readscreen_ms = scene.grab(screen)
    readscreen_tk = ImageTk.PhotoImage(readscreen_ms)
    showscreen = Label(mainframe, image = readscreen_tk)
    showscreen.pack()

subframe = Frame(window, width = 170, height = 380, bg = 'lightgrey')
subframe.grid(row = 0, column = 1, padx = 5, pady = 5)

chat_room = Text(subframe, width = 30, height = 19)
chat_room.grid(row = 0, column = 0, padx = 5, pady = 5)

text_entry = Entry(subframe, width = 30)
text_entry.grid(row = 1, column = 0, padx = 5, pady =5)

def sendText(self):
    chat_room.insert(END, "User : " + text_entry.get() + "\n")
    text_entry.delete(0, END)
text_entry.bind('<Return>', sendText)
send_btn = Button(subframe, text = 'Send', width = 8, command=sendText)
send_btn.grid(row = 2, column = 0, padx = 5, pady = 5)

buttons_frame = Frame(window, width = 500, height = 50, bg = 'lightgrey')
buttons_frame.grid(row = 1, column = 0, padx = 10, pady = 0)

start_btn = Button(buttons_frame, text = 'Start', width=8, command=start)
start_btn.grid(row = 0, column = 0, padx = 5, pady = 5)

stop_btn = Button(buttons_frame, text = 'Stop', width=8)
stop_btn.grid(row = 0, column = 1, padx = 5, pady = 5)

mute_btn = Button(buttons_frame, text = 'Mute', width=8)
mute_btn.grid(row = 0, column = 2, padx = 5, pady = 5)




window.mainloop()

