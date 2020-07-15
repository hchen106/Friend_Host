import socket

ip = "localhost"
port = 5004
ADDR = (ip,port)

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
tcp_socket.bind(ADDR)
tcp_socket.listen(5)

connection, addr = tcp_socket.accept()

#receive mp4 file 
video = open("result.mp4","wb")
print(connection)
while True: 

    buffer = connection.recv(4096)
    print(buffer)
    if buffer: 
        video.write(buffer)

connection.close()





