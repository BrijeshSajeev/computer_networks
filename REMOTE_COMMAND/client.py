import socket

host =socket.gethostname()
port = 5004
client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
command ='ls'
client.sendto(bytes(command,'utf-8'),(host,port))

client.close()
