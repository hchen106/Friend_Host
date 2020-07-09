# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\85216\Desktop\Friend_Host\stream_display.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
import socket
import threading
import cv2
import time
from struct import pack
from struct import unpack
from PyQt5.QtGui import QIcon, QPixmap


class Ui_Stream(object):
    def __init__(self,username,ip,port,host):
        self.username = username
        self.ip = ip
        self.port = port
        self.host = host
        self.ADDR = (self.ip,self.port)
        print("UI")
        self.streamWindow = QtWidgets.QMainWindow()
        self.setupUi(self.streamWindow)
        self.streamWindow.show()
        threading.Thread(target = self.connection).start()
        self.buffer = []
    
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(703, 676)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 3)
        
        self.start_btn = QtWidgets.QPushButton(self.centralwidget)
        self.start_btn.setObjectName("pushButton")
        self.gridLayout.addWidget(self.start_btn, 1, 0, 1, 1)
        self.start_btn.clicked.connect(self.play)
        
        self.stop_btn = QtWidgets.QPushButton(self.centralwidget)
        self.stop_btn.setObjectName("stop_btn")
        self.gridLayout.addWidget(self.stop_btn, 1, 1, 1, 1)
        
        self.mute_btn = QtWidgets.QPushButton(self.centralwidget)
        self.mute_btn.setObjectName("mute_btn")
        self.gridLayout.addWidget(self.mute_btn, 1, 2, 1, 1)
        
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Stream"))
        self.start_btn.setText(_translate("MainWindow", "Start"))
        self.stop_btn.setText(_translate("MainWindow", "Stop"))
        self.mute_btn.setText(_translate("MainWindow", "Mute"))

    def connection(self):
        self.tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.tcp_socket.connect(self.ADDR)
        #threading.Thread(target = tself.sendFrame).start()
        mes = bytes(self.username, 'utf-8')
        self.tcp_socket.send(mes)
        
        
        threading.Thread(targer = self.recvFrame()).start()

    def play(self):
        if(self.host == True):
            threading.Thread(target = self.sendFrame).start()

    def sendFrame(self):
        print("sendFrame()")
        self.sender_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

        self.sender_socket.connect((self.ip,self.port+1))
        self.file = cv2.VideoCapture("/home/matthew779/friend_host/test/Friend_Host/view/720p.mp4")
        self.file.set(3,1280)
        self.file.set(4,720)
        
        while self.file.isOpened(): 
            #time.sleep(1.5)
            ret, frame = self.file.read()
            if ret: 
                cv2.imwrite("frame.jpg",frame)
                if cv2.waitKey(100) & 0xFF == ord('q'):
                    break
                F = open("frame.jpg",'rb')
                data = F.read()
                F.close()
                length = pack('>Q', len(data))
                #print(length)

                # sendall to make sure it blocks if there's back-pressure on the socket
                self.sender_socket.sendall(length)
                self.sender_socket.sendall(data)
                #self.sender_socket.sendall(b'ended')
                self.mess = b''
                while self.mess != b'ended':
                    self.mess = self.sender_socket.recv(4096)
                    
        
        self.sender_socket.close()

    def recvFrame(self):
        print("recvFrame()")
        frame_count = 0
        #threading.Thread(target = self.display).start()
        while True: 
            length =  self.tcp_socket.recv(8)
            
            if length:
                #print(length)       
                #print(length)
                (length,) = unpack('>Q', length)
                data = b''
                
                while len(data) < length:
                    
                    #to_read = length - len(data)
                    data += self.tcp_socket.recv(4096)
                
                self.tcp_socket.send(b'ended')
                # F = open("frame2.jpg","wb")
                # #data = self.buffer[0]
                # F.write(data)
                # F.close()
                pixmap = QPixmap()
                pixmap.loadFromData(data)
                self.label.setPixmap(pixmap)
                #self.buffer.remove(data)
                #self.buffer.append((frame_count, data))
                #frame_count += 1
                #threading.Thread(target = self.display, args = (data, )).start()
                #self.resize(pixmap.width(),pixmap.height())
                
    
    def display(self):
        while True: 
            print("loading")
            while len(self.buffer) < 200: 
                i = 1
            while len(self.buffer) >= 10: 
                F = open("frame2.jpg","wb")
                data = self.buffer[0]
                F.write(data[1])
                F.close()
                pixmap = QPixmap("frame2.jpg")
                self.label.setPixmap(pixmap)
                self.buffer.remove(data)
                time.sleep(0.04)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Stream()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
