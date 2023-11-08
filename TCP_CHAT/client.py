import socket

host = socket.gethostname()
port = 5003
client = socket.socket()
client.bind((host,port))
client.listen(1)
conn,addr = client.accept()
recv =''
while 1:
    if recv==('bye').casefold():
        break
    data=input("you  >> ")
    conn.send(data.encode('utf-8'))
    recv = conn.recv(1024).decode()
    print("Server >> ",recv)
    
conn.close()
client.close()
