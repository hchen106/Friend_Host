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
from PyQt5 import QtCore, QtGui, QtWidgets
from view.chatroom_pyqt import Ui_Chatroom
from view.signup_pyqt import Ui_SignUp


class client:



    def __init__(self):
        
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        ui = Ui_Login(MainWindow)
        #ui = Ui_Login()
        ui.setupUi(app,MainWindow)
        print("Matthew")

        sys.exit(app.exec_())
        
     
        




client()


