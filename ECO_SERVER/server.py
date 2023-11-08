import socket

host = '127.0.0.1'
port = 5001

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))
str ="Hello, Brijesh"
str=str.encode('utf-8')
data = s.recv(1024)
print("From Client : ",data.decode())
s.send(str)
s.close()
