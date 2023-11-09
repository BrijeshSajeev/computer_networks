import socket
import subprocess

host = socket.gethostname()
port =5004

server = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
server.bind((host,port))

data,addr = server.recvfrom(1024)
command = data.decode('utf-8')

# print(command)
subprocess.run(command)

server.close()