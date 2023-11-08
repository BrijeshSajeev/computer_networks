import socket

host = socket.gethostname()
port = 5003
server = socket.socket();
server.connect((host,port))
data =''
while 1:
    if data==('bye').casefold():
        break
    data=server.recv(1024).decode()
    print("client >> ",data)
    
    snd = input("you >> ")
    server.send(snd.encode('utf-8'))

server.close()





