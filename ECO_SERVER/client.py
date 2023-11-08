# An echo server, also known as a "ping server" or "loopback server," 
# is a type of server program that simply returns or echoes back any data it receives from a client. 
# It's a basic networking tool used for testing and troubleshooting network connections.

import socket

host ='127.0.0.1'
port = 5001
# it's AF_INET, which stands for Address Family Internet. This address family is used for IPv4 addresses.
# SOCK_STREAM, which indicates a TCP 
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((host,port))
s.listen(1)
conn,adrr = s.accept()
print("Connected to ..",adrr)

while 1:
    data="hello, brijesh"
    conn.send(data.encode('utf-8'))
    data = conn.recv(1024)
    if not data:
        break
    print("From server >> ",data.decode())
conn.close()
s.close()

