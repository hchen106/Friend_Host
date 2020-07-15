import socket

ip = "localhost"
port = 5004

ADDR = (ip,port)

tcp_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

tcp_socket.connect(ADDR)

#send mp4 file through socket

video = open("/home/matthew779/friend_host/test/Friend_Host/720p.mp4", 'rb')

while True: 

    buffer = video.read()

    
    if(buffer != b''):
        print(buffer)
        tcp_socket.sendall(buffer)

tcp_socket.close()