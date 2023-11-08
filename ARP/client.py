import socket

client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
port = 5002
host = socket.gethostname()

message ='177.0.32.9'
client.sendto(bytes(message,'utf-8'),(host,port))
client.close()





