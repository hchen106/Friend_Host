# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\85216\Desktop\Friend_Host\login.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
import threading
from PyQt5 import QtCore, QtGui, QtWidgets
from view.chatroom_pyqt import Ui_Chatroom
from view.signup_pyqt import Ui_SignUp
from PyQt5.QtWidgets import QMessageBox

#PORT = sef
#ip = '10.0.0.89'
#ip = '167.99.160.18'
#ip = 'localhost'


class Ui_Login(object):
    
    def __init__(self, MainWindow):
        #super(Ui_Login, self).__init__()
        #self.app = QtWidgets.QApplication(sys.argv)
        #self.MainWindow = QtWidgets.QMainWindow()
        #self.ui = Ui_Login()
        #self.ui.setupUi(self.MainWindow)
        
        self.MainWindow = MainWindow
        self.MainWindow.show()
        


    def loginAccount(self):
        threading.Thread(target = self.openChatroom).start()
    
    def openChatroom(self):
        self.name = self.username_entry.text()
        if self.ip_entry.text() != "" and self.port_entry.text() != "" and self.name != "" and self.password_entry.text() != "":
            
            self.ADDR = (self.ip_entry.text() ,int(self.port_entry.text()))
            self.ui = Ui_Chatroom(self.app,self.name, self.ADDR)
            self.MainWindow.close()
        else:
            self.msg = QMessageBox()
            self.msg.setWindowTitle("Warning")
            self.msg.setText("Please enter all information")
            self.x = self.msg.exec_()

        
       
       

    
    def openSignup(self):
        self.signupWindow = QtWidgets.QMainWindow()
        self.ui = Ui_SignUp()
        self.ui.setupUi(self.signupWindow)
        self.signupWindow.show()

    
    
    def setupUi(self, app, MainWindow):
        self.app = app 
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(422, 228)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")

        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")

        self.ip_label = QtWidgets.QLabel(self.centralwidget)
        self.ip_label.setObjectName("ip_label")
        self.gridLayout.addWidget(self.ip_label, 2, 0, 1, 1)

        self.username_entry = QtWidgets.QLineEdit(self.centralwidget)
        self.username_entry.setObjectName("username_entry")
        self.username_entry.returnPressed.connect(self.openChatroom)
        self.gridLayout.addWidget(self.username_entry, 0, 1, 1, 1)

        self.passward_label = QtWidgets.QLabel(self.centralwidget)
        self.passward_label.setObjectName("passward_label")
        self.gridLayout.addWidget(self.passward_label, 1, 0, 1, 1)

        self.password_entry = QtWidgets.QLineEdit(self.centralwidget)
        self.password_entry.setObjectName("password_entry")
        self.password_entry.setEchoMode(self.password_entry.Password)
        self.password_entry.returnPressed.connect(self.openChatroom)
        self.gridLayout.addWidget(self.password_entry, 1, 1, 1, 1)

        self.port_label = QtWidgets.QLabel(self.centralwidget)
        self.port_label.setObjectName("port_label")
        self.gridLayout.addWidget(self.port_label, 3, 0, 1, 1)

        self.ip_entry = QtWidgets.QLineEdit(self.centralwidget)
        self.ip_entry.setObjectName("ip_entry")
        self.ip_entry.returnPressed.connect(self.openChatroom)
        self.gridLayout.addWidget(self.ip_entry, 2, 1, 1, 1)

        self.username_label = QtWidgets.QLabel(self.centralwidget)
        self.username_label.setObjectName("username_label")
        self.gridLayout.addWidget(self.username_label, 0, 0, 1, 1)

        self.port_entry = QtWidgets.QLineEdit(self.centralwidget)
        self.port_entry.setObjectName("port_entry")
        self.port_entry.returnPressed.connect(self.openChatroom)
        self.gridLayout.addWidget(self.port_entry, 3, 1, 1, 1)

        self.verticalLayout.addLayout(self.gridLayout)

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.signup_btn = QtWidgets.QPushButton(self.centralwidget)
        self.signup_btn.setObjectName("signup_btn")
        self.signup_btn.clicked.connect(self.openSignup)
        self.horizontalLayout.addWidget(self.signup_btn)

        self.login_btn = QtWidgets.QPushButton(self.centralwidget)
        self.login_btn.setObjectName("login_btn")
        self.login_btn.clicked.connect(self.openChatroom)
        self.horizontalLayout.addWidget(self.login_btn)

        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)


        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ip_label.setText(_translate("MainWindow", "IP Address"))
        self.passward_label.setText(_translate("MainWindow", "Password"))
        self.port_label.setText(_translate("MainWindow", "Ports"))
        self.username_label.setText(_translate("MainWindow", "Username"))
        self.signup_btn.setText(_translate("MainWindow", "Sign Up"))
        self.login_btn.setText(_translate("MainWindow", "Login"))







