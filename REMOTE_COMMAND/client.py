import socket

host =socket.gethostname()
port = 5004
client = socket.socket()
client.connect((host,port))
client.send(('ls').encode('utf-8'))
client.close()
