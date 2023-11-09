import socket
host = socket.gethostname()
port = 5004

server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server.bind((host,port))


while 1:
    data ,addr= server.recvfrom(1024)
    data = data.decode('utf-8')
    if data=='bye':
        break
    print('client >> ',data)
    replay=input('you >> ')
    server.sendto(bytes(replay,'utf-8'),addr)

server.close()