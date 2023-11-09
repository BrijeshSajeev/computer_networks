import socket
host = socket.gethostname()
port = 5004
client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while 1:
    data = input("you >> ")
    client.sendto(bytes(data,'utf-8'),(host,port))
    if data=='bye':
        break
    rec,addr = client.recvfrom(1024)
    print('server >> ',rec.decode('utf-8'))

client.close()