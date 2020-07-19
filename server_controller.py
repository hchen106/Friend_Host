from server import server
import socket


class server_controller:

    ip = 'localhost'
    PORT = 7015


    def __init__(self): 
        self.start()
        self.printMenu()
        print("server closed")

    def start(self): 
        print("Establishing the server.......")
        self.tcp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.tcp_socket.bind(('',self.PORT))
        self.tcp_socket.listen(5)
        print("Done")
        server(self.PORT, self.ip, self.tcp_socket)
        

    """
    Print out Menu List for engineer to maintain the server
    Ask user to enter command
    """
    def printMenu(self): 
        while True: 
            print("(1)")
            print("(2).")
            print("(3)")
            print("(4)Print Clients list")
            print("(x)Close Server")

            command = input()
            if(command == "x"):
                print("Server is closing......")
                self.tcp_socket.close()
                self.makeCloseConnection()
                break
            else: 
                self.executeCommand(command)
    
    def makeCloseConnection(self):
        self.socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.socket.connect((self.ip,self.PORT))
        self.socket.close()

    def executeCommand(self, command):

        
        if command == "1": 
            i = 1
        elif command == "2": 
            i = 1
        elif command == "3": 
            i = 1
        else: 
            print("Invalid command")
            


server_controller()



